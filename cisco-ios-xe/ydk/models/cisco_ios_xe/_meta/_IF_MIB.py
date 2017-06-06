


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IfMib.Interfaces' : {
        'meta_info' : _MetaInfoClass('IfMib.Interfaces',
            False, 
            [
            _MetaInfoClassMember('ifNumber', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of network interfaces (regardless of their
                current state) present on this system.
                ''',
                'ifnumber',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'interfaces',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Ifmibobjects' : {
        'meta_info' : _MetaInfoClass('IfMib.Ifmibobjects',
            False, 
            [
            _MetaInfoClassMember('ifStackLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the last change of
                the (whole) interface stack.  A change of the interface
                stack is defined to be any creation, deletion, or change in
                value of any instance of ifStackStatus.  If the interface
                stack has been unchanged since the last re-initialization of
                the local network management subsystem, then this object
                contains a zero value.
                ''',
                'ifstacklastchange',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTableLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the last creation or
                deletion of an entry in the ifTable.  If the number of
                entries has been unchanged since the last re-initialization
                of the local network management subsystem, then this object
                contains a zero value.
                ''',
                'iftablelastchange',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifMIBObjects',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Iftable.Ifentry.IfadminstatusEnum' : _MetaInfoEnum('IfadminstatusEnum', 'ydk.models.cisco_ios_xe.IF_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
        }, 'IF-MIB', _yang_ns._namespaces['IF-MIB']),
    'IfMib.Iftable.Ifentry.IflinkupdowntrapenableEnum' : _MetaInfoEnum('IflinkupdowntrapenableEnum', 'ydk.models.cisco_ios_xe.IF_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'IF-MIB', _yang_ns._namespaces['IF-MIB']),
    'IfMib.Iftable.Ifentry.IfoperstatusEnum' : _MetaInfoEnum('IfoperstatusEnum', 'ydk.models.cisco_ios_xe.IF_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
            'unknown':'unknown',
            'dormant':'dormant',
            'notPresent':'notPresent',
            'lowerLayerDown':'lowerLayerDown',
        }, 'IF-MIB', _yang_ns._namespaces['IF-MIB']),
    'IfMib.Iftable.Ifentry.IftestresultEnum' : _MetaInfoEnum('IftestresultEnum', 'ydk.models.cisco_ios_xe.IF_MIB',
        {
            'none':'none',
            'success':'success',
            'inProgress':'inProgress',
            'notSupported':'notSupported',
            'unAbleToRun':'unAbleToRun',
            'aborted':'aborted',
            'failed':'failed',
        }, 'IF-MIB', _yang_ns._namespaces['IF-MIB']),
    'IfMib.Iftable.Ifentry.IfteststatusEnum' : _MetaInfoEnum('IfteststatusEnum', 'ydk.models.cisco_ios_xe.IF_MIB',
        {
            'notInUse':'notInUse',
            'inUse':'inUse',
        }, 'IF-MIB', _yang_ns._namespaces['IF-MIB']),
    'IfMib.Iftable.Ifentry' : {
        'meta_info' : _MetaInfoClass('IfMib.Iftable.Ifentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                A unique value, greater than zero, for each interface.  It
                is recommended that values are assigned contiguously
                starting from 1.  The value for each interface sub-layer
                must remain constant at least from one re-initialization of
                the entity's network management system to the next re-
                initialization.
                ''',
                'ifindex',
                'IF-MIB', True),
            _MetaInfoClassMember('ifAdminStatus', REFERENCE_ENUM_CLASS, 'IfadminstatusEnum' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable.Ifentry.IfadminstatusEnum', 
                [], [], 
                '''                The desired state of the interface.  The testing(3) state
                indicates that no operational packets can be passed.  When a
                managed system initializes, all interfaces start with
                ifAdminStatus in the down(2) state.  As a result of either
                explicit management action or per configuration information
                retained by the managed system, ifAdminStatus is then
                changed to either the up(1) or testing(3) states (or remains
                in the down(2) state).
                ''',
                'ifadminstatus',
                'IF-MIB', False),
            _MetaInfoClassMember('ifAlias', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object is an 'alias' name for the interface as
                specified by a network manager, and provides a non-volatile
                'handle' for the interface.
                
                On the first instantiation of an interface, the value of
                ifAlias associated with that interface is the zero-length
                string.  As and when a value is written into an instance of
                ifAlias through a network management set operation, then the
                agent must retain the supplied value in the ifAlias instance
                associated with the same interface for as long as that
                interface remains instantiated, including across all re-
                initializations/reboots of the network management system,
                including those which result in a change of the interface's
                ifIndex value.
                
                An example of the value which a network manager might store
                in this object for a WAN interface is the (Telco's) circuit
                number/identifier of the interface.
                
                Some agents may support write-access only for interfaces
                having particular values of ifType.  An agent which supports
                write access to this object is required to keep the value in
                non-volatile storage, but it may limit the length of new
                values depending on how much storage is already occupied by
                the current values for other interfaces.
                ''',
                'ifalias',
                'IF-MIB', False),
            _MetaInfoClassMember('ifConnectorPresent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object has the value 'true(1)' if the interface
                sublayer has a physical connector and the value 'false(2)'
                otherwise.
                ''',
                'ifconnectorpresent',
                'IF-MIB', False),
            _MetaInfoClassMember('ifCounterDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                any one or more of this interface's counters suffered a
                discontinuity.  The relevant counters are the specific
                instances associated with this interface of any Counter32 or
                Counter64 object contained in the ifTable or ifXTable.  If
                no such discontinuities have occurred since the last re-
                initialization of the local management subsystem, then this
                object contains a zero value.
                ''',
                'ifcounterdiscontinuitytime',
                'IF-MIB', False),
            _MetaInfoClassMember('ifDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A textual string containing information about the
                interface.  This string should include the name of the
                manufacturer, the product name and the version of the
                interface hardware/software.
                ''',
                'ifdescr',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCInBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were addressed to a broadcast
                address at this sub-layer.  This object is a 64-bit version
                of ifInBroadcastPkts.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcinbroadcastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCInMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were addressed to a multicast
                address at this sub-layer.  For a MAC layer protocol, this
                includes both Group and Functional addresses.  This object
                is a 64-bit version of ifInMulticastPkts.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcinmulticastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received on the interface,
                including framing characters.  This object is a 64-bit
                version of ifInOctets.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcinoctets',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCInUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were not addressed to a multicast
                or broadcast address at this sub-layer.  This object is a
                64-bit version of ifInUcastPkts.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcinucastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCOutBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were addressed to a
                broadcast address at this sub-layer, including those that
                were discarded or not sent.  This object is a 64-bit version
                of ifOutBroadcastPkts.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcoutbroadcastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCOutMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were addressed to a
                multicast address at this sub-layer, including those that
                were discarded or not sent.  For a MAC layer protocol, this
                includes both Group and Functional addresses.  This object
                is a 64-bit version of ifOutMulticastPkts.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcoutmulticastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets transmitted out of the
                interface, including framing characters.  This object is a
                64-bit version of ifOutOctets.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcoutoctets',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHCOutUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were not addressed to a
                multicast or broadcast address at this sub-layer, including
                those that were discarded or not sent.  This object is a
                64-bit version of ifOutUcastPkts.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifhcoutucastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifHighSpeed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An estimate of the interface's current bandwidth in units
                of 1,000,000 bits per second.  If this object reports a
                value of `n' then the speed of the interface is somewhere in
                the range of `n-500,000' to `n+499,999'.  For interfaces
                which do not vary in bandwidth or for those where no
                accurate estimation can be made, this object should contain
                the nominal bandwidth.  For a sub-layer which has no concept
                of bandwidth, this object should be zero.
                ''',
                'ifhighspeed',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were addressed to a broadcast
                address at this sub-layer.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifinbroadcastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of inbound packets which were chosen to be
                discarded even though no errors had been detected to prevent
                their being deliverable to a higher-layer protocol.  One
                possible reason for discarding such a packet could be to
                free up buffer space.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifindiscards',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of inbound
                packets that contained errors preventing them from being
                deliverable to a higher-layer protocol.  For character-
                oriented or fixed-length interfaces, the number of inbound
                transmission units that contained errors preventing them
                from being deliverable to a higher-layer protocol.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifinerrors',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were addressed to a multicast
                address at this sub-layer.  For a MAC layer protocol, this
                includes both Group and Functional addresses.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifinmulticastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInNUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were addressed to a multicast or
                broadcast address at this sub-layer.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                
                This object is deprecated in favour of ifInMulticastPkts and
                ifInBroadcastPkts.
                ''',
                'ifinnucastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets received on the interface,
                including framing characters.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifinoctets',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, which were not addressed to a multicast
                or broadcast address at this sub-layer.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifinucastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifInUnknownProtos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of packets
                received via the interface which were discarded because of
                an unknown or unsupported protocol.  For character-oriented
                or fixed-length interfaces that support protocol
                multiplexing the number of transmission units received via
                the interface which were discarded because of an unknown or
                unsupported protocol.  For any interface that does not
                support protocol multiplexing, this counter will always be
                0.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifinunknownprotos',
                'IF-MIB', False),
            _MetaInfoClassMember('ifLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time the interface entered
                its current operational state.  If the current state was
                entered prior to the last re-initialization of the local
                network management subsystem, then this object contains a
                zero value.
                ''',
                'iflastchange',
                'IF-MIB', False),
            _MetaInfoClassMember('ifLinkUpDownTrapEnable', REFERENCE_ENUM_CLASS, 'IflinkupdowntrapenableEnum' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable.Ifentry.IflinkupdowntrapenableEnum', 
                [], [], 
                '''                Indicates whether linkUp/linkDown traps should be generated
                for this interface.
                
                By default, this object should have the value enabled(1) for
                interfaces which do not operate on 'top' of any other
                interface (as defined in the ifStackTable), and disabled(2)
                otherwise.
                ''',
                'iflinkupdowntrapenable',
                'IF-MIB', False),
            _MetaInfoClassMember('ifMtu', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The size of the largest packet which can be sent/received
                on the interface, specified in octets.  For interfaces that
                are used for transmitting network datagrams, this is the
                size of the largest network datagram that can be sent on the
                interface.
                ''',
                'ifmtu',
                'IF-MIB', False),
            _MetaInfoClassMember('ifName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The textual name of the interface.  The value of this
                object should be the name of the interface as assigned by
                the local device and should be suitable for use in commands
                entered at the device's `console'.  This might be a text
                name, such as `le0' or a simple port number, such as `1',
                depending on the interface naming syntax of the device.  If
                several entries in the ifTable together represent a single
                interface as named by the device, then each will have the
                same value of ifName.  Note that for an agent which responds
                to SNMP queries concerning an interface on some other
                (proxied) device, then the value of ifName for such an
                interface is the proxied device's local name for it.
                
                If there is no local name, or this object is otherwise not
                applicable, then this object contains a zero-length string.
                ''',
                'ifname',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOperStatus', REFERENCE_ENUM_CLASS, 'IfoperstatusEnum' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable.Ifentry.IfoperstatusEnum', 
                [], [], 
                '''                The current operational state of the interface.  The
                testing(3) state indicates that no operational packets can
                be passed.  If ifAdminStatus is down(2) then ifOperStatus
                should be down(2).  If ifAdminStatus is changed to up(1)
                then ifOperStatus should change to up(1) if the interface is
                ready to transmit and receive network traffic; it should
                change to dormant(5) if the interface is waiting for
                external actions (such as a serial line waiting for an
                incoming connection); it should remain in the down(2) state
                if and only if there is a fault that prevents it from going
                to the up(1) state; it should remain in the notPresent(6)
                state if the interface has missing (typically, hardware)
                components.
                ''',
                'ifoperstatus',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were addressed to a
                broadcast address at this sub-layer, including those that
                were discarded or not sent.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifoutbroadcastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of outbound packets which were chosen to be
                discarded even though no errors had been detected to prevent
                their being transmitted.  One possible reason for discarding
                such a packet could be to free up buffer space.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifoutdiscards',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of outbound
                packets that could not be transmitted because of errors.
                For character-oriented or fixed-length interfaces, the
                number of outbound transmission units that could not be
                transmitted because of errors.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifouterrors',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were addressed to a
                multicast address at this sub-layer, including those that
                were discarded or not sent.  For a MAC layer protocol, this
                includes both Group and Functional addresses.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifoutmulticastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutNUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were addressed to a
                multicast or broadcast address at this sub-layer, including
                those that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                
                This object is deprecated in favour of ifOutMulticastPkts
                and ifOutBroadcastPkts.
                ''',
                'ifoutnucastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of octets transmitted out of the
                interface, including framing characters.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifoutoctets',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutQLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The length of the output packet queue (in packets).
                ''',
                'ifoutqlen',
                'IF-MIB', False),
            _MetaInfoClassMember('ifOutUcastPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and which were not addressed to a
                multicast or broadcast address at this sub-layer, including
                those that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other
                times as indicated by the value of
                ifCounterDiscontinuityTime.
                ''',
                'ifoutucastpkts',
                'IF-MIB', False),
            _MetaInfoClassMember('ifPhysAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The interface's address at its protocol sub-layer.  For
                example, for an 802.x interface, this object normally
                contains a MAC address.  The interface's media-specific MIB
                must define the bit and byte ordering and the format of the
                value of this object.  For interfaces which do not have such
                an address (e.g., a serial line), this object should contain
                an octet string of zero length.
                ''',
                'ifphysaddress',
                'IF-MIB', False),
            _MetaInfoClassMember('ifPromiscuousMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object has a value of false(2) if this interface only
                accepts packets/frames that are addressed to this station.
                This object has a value of true(1) when the station accepts
                all packets/frames transmitted on the media.  The value
                true(1) is only legal on certain types of media.  If legal,
                setting this object to a value of true(1) may require the
                interface to be reset before becoming effective.
                
                The value of ifPromiscuousMode does not affect the reception
                of broadcast and multicast packets/frames by the interface.
                ''',
                'ifpromiscuousmode',
                'IF-MIB', False),
            _MetaInfoClassMember('ifSpecific', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A reference to MIB definitions specific to the particular
                media being used to realize the interface.  It is
                recommended that this value point to an instance of a MIB
                object in the media-specific MIB, i.e., that this object
                have the semantics associated with the InstancePointer
                textual convention defined in RFC 2579.  In fact, it is
                recommended that the media-specific MIB specify what value
                ifSpecific should/can take for values of ifType.  If no MIB
                definitions specific to the particular media are available,
                the value should be set to the OBJECT IDENTIFIER { 0 0 }.
                ''',
                'ifspecific',
                'IF-MIB', False),
            _MetaInfoClassMember('ifSpeed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An estimate of the interface's current bandwidth in bits
                per second.  For interfaces which do not vary in bandwidth
                or for those where no accurate estimation can be made, this
                object should contain the nominal bandwidth.  If the
                bandwidth of the interface is greater than the maximum value
                reportable by this object then this object should report its
                maximum value (4,294,967,295) and ifHighSpeed must be used
                to report the interace's speed.  For a sub-layer which has
                no concept of bandwidth, this object should be zero.
                ''',
                'ifspeed',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTestCode', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object contains a code which contains more specific
                information on the test result, for example an error-code
                after a failed test.  Error codes and other values this
                object may take are specific to the type of interface and/or
                test.  The value may have the semantics of either the
                AutonomousType or InstancePointer textual conventions as
                defined in RFC 2579.  The identifier:
                
                    testCodeUnknown  OBJECT IDENTIFIER ::= { 0 0 }
                
                is defined for use if no additional result code is
                available.
                ''',
                'iftestcode',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTestId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object identifies the current invocation of the
                interface's test.
                ''',
                'iftestid',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTestOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity which currently has the 'ownership' required to
                invoke a test on this interface.
                ''',
                'iftestowner',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTestResult', REFERENCE_ENUM_CLASS, 'IftestresultEnum' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable.Ifentry.IftestresultEnum', 
                [], [], 
                '''                This object contains the result of the most recently
                requested test, or the value none(1) if no tests have been
                requested since the last reset.  Note that this facility
                provides no provision for saving the results of one test
                when starting another, as could be required if used by
                multiple managers concurrently.
                ''',
                'iftestresult',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTestStatus', REFERENCE_ENUM_CLASS, 'IfteststatusEnum' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable.Ifentry.IfteststatusEnum', 
                [], [], 
                '''                This object indicates whether or not some manager currently
                has the necessary 'ownership' required to invoke a test on
                this interface.  A write to this object is only successful
                when it changes its value from 'notInUse(1)' to 'inUse(2)'.
                After completion of a test, the agent resets the value back
                to 'notInUse(1)'.
                ''',
                'ifteststatus',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTestType', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A control variable used to start and stop operator-
                initiated interface tests.  Most OBJECT IDENTIFIER values
                assigned to tests are defined elsewhere, in association with
                specific types of interface.  However, this document assigns
                a value for a full-duplex loopback test, and defines the
                special meanings of the subject identifier:
                
                    noTest  OBJECT IDENTIFIER ::= { 0 0 }
                
                When the value noTest is written to this object, no action
                is taken unless a test is in progress, in which case the
                test is aborted.  Writing any other value to this object is
                only valid when no test is currently in progress, in which
                case the indicated test is initiated.
                
                When read, this object always returns the most recent value
                that ifTestType was set to.  If it has not been set since
                the last initialization of the network management subsystem
                on the agent, a value of noTest is returned.
                ''',
                'iftesttype',
                'IF-MIB', False),
            _MetaInfoClassMember('ifType', REFERENCE_ENUM_CLASS, 'IanaiftypeEnum' , 'ydk.models.cisco_ios_xe.IANAifType_MIB', 'IanaiftypeEnum', 
                [], [], 
                '''                The type of interface.  Additional values for ifType are
                assigned by the Internet Assigned Numbers Authority (IANA),
                through updating the syntax of the IANAifType textual
                convention.
                ''',
                'iftype',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifEntry',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Iftable' : {
        'meta_info' : _MetaInfoClass('IfMib.Iftable',
            False, 
            [
            _MetaInfoClassMember('ifEntry', REFERENCE_LIST, 'Ifentry' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable.Ifentry', 
                [], [], 
                '''                An entry containing management information applicable to a
                particular interface.
                ''',
                'ifentry',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifTable',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Ifstacktable.Ifstackentry' : {
        'meta_info' : _MetaInfoClass('IfMib.Ifstacktable.Ifstackentry',
            False, 
            [
            _MetaInfoClassMember('ifStackHigherLayer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The value of ifIndex corresponding to the higher sub-layer
                of the relationship, i.e., the sub-layer which runs on 'top'
                of the sub-layer identified by the corresponding instance of
                ifStackLowerLayer.  If there is no higher sub-layer (below
                the internetwork layer), then this object has the value 0.
                ''',
                'ifstackhigherlayer',
                'IF-MIB', True),
            _MetaInfoClassMember('ifStackLowerLayer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The value of ifIndex corresponding to the lower sub-layer
                of the relationship, i.e., the sub-layer which runs 'below'
                the sub-layer identified by the corresponding instance of
                ifStackHigherLayer.  If there is no lower sub-layer, then
                this object has the value 0.
                ''',
                'ifstacklowerlayer',
                'IF-MIB', True),
            _MetaInfoClassMember('ifStackStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of the relationship between two sub-layers.
                
                Changing the value of this object from 'active' to
                'notInService' or 'destroy' will likely have consequences up
                and down the interface stack.  Thus, write access to this
                object is likely to be inappropriate for some types of
                interfaces, and many implementations will choose not to
                support write-access for any type of interface.
                ''',
                'ifstackstatus',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifStackEntry',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Ifstacktable' : {
        'meta_info' : _MetaInfoClass('IfMib.Ifstacktable',
            False, 
            [
            _MetaInfoClassMember('ifStackEntry', REFERENCE_LIST, 'Ifstackentry' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Ifstacktable.Ifstackentry', 
                [], [], 
                '''                Information on a particular relationship between two sub-
                layers, specifying that one sub-layer runs on 'top' of the
                other sub-layer.  Each sub-layer corresponds to a conceptual
                row in the ifTable.
                ''',
                'ifstackentry',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifStackTable',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Ifrcvaddresstable.Ifrcvaddressentry.IfrcvaddresstypeEnum' : _MetaInfoEnum('IfrcvaddresstypeEnum', 'ydk.models.cisco_ios_xe.IF_MIB',
        {
            'other':'other',
            'volatile':'volatile',
            'nonVolatile':'nonVolatile',
        }, 'IF-MIB', _yang_ns._namespaces['IF-MIB']),
    'IfMib.Ifrcvaddresstable.Ifrcvaddressentry' : {
        'meta_info' : _MetaInfoClass('IfMib.Ifrcvaddresstable.Ifrcvaddressentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'IF-MIB', True),
            _MetaInfoClassMember('ifRcvAddressAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                An address for which the system will accept packets/frames
                on this entry's interface.
                ''',
                'ifrcvaddressaddress',
                'IF-MIB', True),
            _MetaInfoClassMember('ifRcvAddressStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create and delete rows in the
                ifRcvAddressTable.
                ''',
                'ifrcvaddressstatus',
                'IF-MIB', False),
            _MetaInfoClassMember('ifRcvAddressType', REFERENCE_ENUM_CLASS, 'IfrcvaddresstypeEnum' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Ifrcvaddresstable.Ifrcvaddressentry.IfrcvaddresstypeEnum', 
                [], [], 
                '''                This object has the value nonVolatile(3) for those entries
                in the table which are valid and will not be deleted by the
                next restart of the managed system.  Entries having the
                value volatile(2) are valid and exist, but have not been
                saved, so that will not exist after the next restart of the
                managed system.  Entries having the value other(1) are valid
                and exist but are not classified as to whether they will
                continue to exist after the next restart.
                ''',
                'ifrcvaddresstype',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifRcvAddressEntry',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib.Ifrcvaddresstable' : {
        'meta_info' : _MetaInfoClass('IfMib.Ifrcvaddresstable',
            False, 
            [
            _MetaInfoClassMember('ifRcvAddressEntry', REFERENCE_LIST, 'Ifrcvaddressentry' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Ifrcvaddresstable.Ifrcvaddressentry', 
                [], [], 
                '''                A list of objects identifying an address for which the
                system will accept packets/frames on the particular
                interface identified by the index value ifIndex.
                ''',
                'ifrcvaddressentry',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'ifRcvAddressTable',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
    'IfMib' : {
        'meta_info' : _MetaInfoClass('IfMib',
            False, 
            [
            _MetaInfoClassMember('ifMIBObjects', REFERENCE_CLASS, 'Ifmibobjects' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Ifmibobjects', 
                [], [], 
                '''                ''',
                'ifmibobjects',
                'IF-MIB', False),
            _MetaInfoClassMember('ifRcvAddressTable', REFERENCE_CLASS, 'Ifrcvaddresstable' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Ifrcvaddresstable', 
                [], [], 
                '''                This table contains an entry for each address (broadcast,
                multicast, or uni-cast) for which the system will receive
                packets/frames on a particular interface, except as follows:
                
                - for an interface operating in promiscuous mode, entries
                are only required for those addresses for which the system
                would receive frames were it not operating in promiscuous
                mode.
                
                - for 802.5 functional addresses, only one entry is
                required, for the address which has the functional address
                bit ANDed with the bit mask of all functional addresses for
                which the interface will accept frames.
                
                A system is normally able to use any unicast address which
                corresponds to an entry in this table as a source address.
                ''',
                'ifrcvaddresstable',
                'IF-MIB', False),
            _MetaInfoClassMember('ifStackTable', REFERENCE_CLASS, 'Ifstacktable' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Ifstacktable', 
                [], [], 
                '''                The table containing information on the relationships
                between the multiple sub-layers of network interfaces.  In
                particular, it contains information on which sub-layers run
                'on top of' which other sub-layers, where each sub-layer
                corresponds to a conceptual row in the ifTable.  For
                example, when the sub-layer with ifIndex value x runs over
                the sub-layer with ifIndex value y, then this table
                contains:
                
                  ifStackStatus.x.y=active
                
                For each ifIndex value, I, which identifies an active
                interface, there are always at least two instantiated rows
                in this table associated with I.  For one of these rows, I
                is the value of ifStackHigherLayer; for the other, I is the
                value of ifStackLowerLayer.  (If I is not involved in
                multiplexing, then these are the only two rows associated
                with I.)
                
                For example, two rows exist even for an interface which has
                no others stacked on top or below it:
                
                  ifStackStatus.0.x=active
                  ifStackStatus.x.0=active 
                ''',
                'ifstacktable',
                'IF-MIB', False),
            _MetaInfoClassMember('ifTable', REFERENCE_CLASS, 'Iftable' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Iftable', 
                [], [], 
                '''                A list of interface entries.  The number of entries is
                given by the value of ifNumber.
                ''',
                'iftable',
                'IF-MIB', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xe.IF_MIB', 'IfMib.Interfaces', 
                [], [], 
                '''                ''',
                'interfaces',
                'IF-MIB', False),
            ],
            'IF-MIB',
            'IF-MIB',
            _yang_ns._namespaces['IF-MIB'],
        'ydk.models.cisco_ios_xe.IF_MIB'
        ),
    },
}
_meta_table['IfMib.Iftable.Ifentry']['meta_info'].parent =_meta_table['IfMib.Iftable']['meta_info']
_meta_table['IfMib.Ifstacktable.Ifstackentry']['meta_info'].parent =_meta_table['IfMib.Ifstacktable']['meta_info']
_meta_table['IfMib.Ifrcvaddresstable.Ifrcvaddressentry']['meta_info'].parent =_meta_table['IfMib.Ifrcvaddresstable']['meta_info']
_meta_table['IfMib.Interfaces']['meta_info'].parent =_meta_table['IfMib']['meta_info']
_meta_table['IfMib.Ifmibobjects']['meta_info'].parent =_meta_table['IfMib']['meta_info']
_meta_table['IfMib.Iftable']['meta_info'].parent =_meta_table['IfMib']['meta_info']
_meta_table['IfMib.Ifstacktable']['meta_info'].parent =_meta_table['IfMib']['meta_info']
_meta_table['IfMib.Ifrcvaddresstable']['meta_info'].parent =_meta_table['IfMib']['meta_info']
