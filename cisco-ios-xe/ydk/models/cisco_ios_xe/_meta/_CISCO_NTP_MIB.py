


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NtpleapindicatorEnum' : _MetaInfoEnum('NtpleapindicatorEnum', 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB',
        {
            'noWarning':'noWarning',
            'addSecond':'addSecond',
            'subtractSecond':'subtractSecond',
            'alarm':'alarm',
        }, 'CISCO-NTP-MIB', _yang_ns._namespaces['CISCO-NTP-MIB']),
    'CiscoNtpMib.Cntpsystem.CntpsyssrvstatusEnum' : _MetaInfoEnum('CntpsyssrvstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB',
        {
            'unknown':'unknown',
            'notRunning':'notRunning',
            'notSynchronized':'notSynchronized',
            'syncToLocal':'syncToLocal',
            'syncToRefclock':'syncToRefclock',
            'syncToRemoteServer':'syncToRemoteServer',
        }, 'CISCO-NTP-MIB', _yang_ns._namespaces['CISCO-NTP-MIB']),
    'CiscoNtpMib.Cntpsystem' : {
        'meta_info' : _MetaInfoClass('CiscoNtpMib.Cntpsystem',
            False, 
            [
            _MetaInfoClassMember('cntpSysClock', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The current local time.  Local time is derived from
                the hardware clock of the particular machine and
                increments at intervals depending on the design used.
                ''',
                'cntpsysclock',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysLeap', REFERENCE_ENUM_CLASS, 'NtpleapindicatorEnum' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'NtpleapindicatorEnum', 
                [], [], 
                '''                Two-bit code warning of an impending leap second to
                be inserted in the NTP timescale. This object can be
                set only when the cntpSysStratum has a value of 1.
                ''',
                'cntpsysleap',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysPeer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The current synchronization source.  This will
                contain the unique association identifier
                cntpPeersAssocId of the corresponding peer entry in
                the cntpPeersVarTable of the peer acting as the
                synchronization source.  If there is no peer, the
                value will be 0.
                ''',
                'cntpsyspeer',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysPoll', ATTRIBUTE, 'int' , None, None, 
                [('-20', '20')], [], 
                '''                The interval at which the NTP server polls other NTP
                servers to synchronize its clock.
                ''',
                'cntpsyspoll',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysPrecision', ATTRIBUTE, 'int' , None, None, 
                [('-20', '20')], [], 
                '''                Signed integer indicating the precision
                of the system clock, in seconds to the nearest
                power of two.  The value must be rounded to the
                next larger power of two; for instance, a 50-Hz
                (20 ms) or 60-Hz (16.67 ms) power-frequency clock
                would be assigned the value -5 (31.25 ms), while a
                1000-Hz (1 ms) crystal-controlled clock would be
                assigned the value -9 (1.95 ms).
                ''',
                'cntpsysprecision',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysRefId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The reference identifier of the local clock.
                ''',
                'cntpsysrefid',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysRefTime', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The local time when the local clock was last
                updated.  If the local clock has never been
                synchronized, the value is zero.
                ''',
                'cntpsysreftime',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysRootDelay', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                A signed fixed-point number indicating the total
                round-trip delay in seconds, to the primary reference
                source at the root of the synchronization subnet.
                ''',
                'cntpsysrootdelay',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysRootDispersion', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The maximum error in seconds, relative to the
                primary reference source at the root of the
                synchronization subnet.  Only positive values greater
                than zero are possible.
                ''',
                'cntpsysrootdispersion',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysSrvStatus', REFERENCE_ENUM_CLASS, 'CntpsyssrvstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntpsystem.CntpsyssrvstatusEnum', 
                [], [], 
                '''                Current state of the NTP server with values coded as follows:
                1: server status is unknown
                2: server is not running
                3: server is not synchronized to any time source
                4: server is synchronized to its own local clock
                5: server is synchronized to a local hardware refclock (e.g. GPS)
                6: server is synchronized to a remote NTP server
                ''',
                'cntpsyssrvstatus',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSysStratum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The stratum of the local clock. If the value is set
                to 1, i.e., this is a primary reference, then the
                Primary-Clock procedure described in Section 3.4.6,
                in RFC-1305 is invoked.
                ''',
                'cntpsysstratum',
                'CISCO-NTP-MIB', False),
            ],
            'CISCO-NTP-MIB',
            'cntpSystem',
            _yang_ns._namespaces['CISCO-NTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NTP_MIB'
        ),
    },
    'CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry.CntppeersmodeEnum' : _MetaInfoEnum('CntppeersmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB',
        {
            'unspecified':'unspecified',
            'symmetricActive':'symmetricActive',
            'symmetricPassive':'symmetricPassive',
            'client':'client',
            'server':'server',
            'broadcast':'broadcast',
            'reservedControl':'reservedControl',
            'reservedPrivate':'reservedPrivate',
        }, 'CISCO-NTP-MIB', _yang_ns._namespaces['CISCO-NTP-MIB']),
    'CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry' : {
        'meta_info' : _MetaInfoClass('CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry',
            False, 
            [
            _MetaInfoClassMember('cntpPeersAssocId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                An integer value greater than 0 that uniquely
                identifies a peer with which the local NTP server
                is associated.
                ''',
                'cntppeersassocid',
                'CISCO-NTP-MIB', True),
            _MetaInfoClassMember('cntpPeersConfigured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This is a bit indicating that the association
                was created from configuration information and
                should not be de-associated even if the peer
                becomes unreachable.
                ''',
                'cntppeersconfigured',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersDelay', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The estimated round-trip delay of the peer clock
                relative to the local clock over the network path
                between them, in seconds.  The host determines the
                value of this object using the NTP clock-filter
                algorithm.
                ''',
                'cntppeersdelay',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersDispersion', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The estimated maximum error of the peer clock
                relative to the local clock over the network path
                between them, in seconds.  The host determines the
                value of this object using the NTP clock-filter
                algorithm.
                ''',
                'cntppeersdispersion',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status object for this row. When a management
                station is creating a new row, it should set the
                value for cntpPeersPeerAddress at least, before the
                row can be made active(1).
                ''',
                'cntppeersentrystatus',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersFilterValidEntries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of valid entries for a peer in the
                Filter Register Table. Since, the Filter Register
                Table is optional, this object will have a value 0
                if the Filter Register Table is not implemented.
                ''',
                'cntppeersfiltervalidentries',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersHostAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the local host.  Multi-homing can
                be supported using this object.
                ''',
                'cntppeershostaddress',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersHostPoll', ATTRIBUTE, 'int' , None, None, 
                [('-20', '20')], [], 
                '''                The interval at which the local host polls the peer.
                ''',
                'cntppeershostpoll',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersHostPort', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The UDP port number on which the local host receives
                NTP messages.
                ''',
                'cntppeershostport',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersLeap', REFERENCE_ENUM_CLASS, 'NtpleapindicatorEnum' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'NtpleapindicatorEnum', 
                [], [], 
                '''                Two-bit code warning of an impending leap
                second to be inserted in the NTP timescale of
                the peer.
                ''',
                'cntppeersleap',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersMode', REFERENCE_ENUM_CLASS, 'CntppeersmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry.CntppeersmodeEnum', 
                [], [], 
                '''                The association mode of the NTP server, with values
                coded as follows,
                0, unspecified
                1, symmetric active - A host operating in this mode
                        sends periodic messages regardless of the
                        reachability state or stratum of its peer.  By
                        operating in this mode the host announces its
                        willingness to synchronize and be synchronized
                        by the peer
                2, symmetric passive - This type of association is
                        ordinarily created upon arrival of a message
                        from a peer operating in the symmetric active
                        mode and persists only as long as the peer is
                        reachable and operating at a stratum level
                        less than or equal to the host; otherwise, the
                        association is dissolved.  However, the
                        association will always persist until at least
                        one message has been sent in reply.  By
                        operating in this mode the host announces its
                        willingness to synchronize and be synchronized
                        by the peer
                3, client -  A host operating in this mode sends
                        periodic messages regardless of the
                        reachability state or stratum of its peer.  By
                        operating in this mode the host, usually a LAN
                        workstation, announces its willingness to be
                        synchronized by, but not to synchronize the peer
                4, server - This type of association is ordinarily
                        created upon arrival of a client request message
                        and exists only in order to reply to that
                        request, after which the association is
                        dissolved.  By operating in this mode the host,
                        usually a LAN time server, announces its
                        willingness to synchronize, but not to be
                        synchronized by the peer
                5, broadcast - A host operating in this mode sends
                        periodic messages regardless of the
                        reachability state or stratum of the peers.
                        By operating in this mode the host, usually a
                        LAN time server operating on a high-speed
                        broadcast medium, announces its willingness to
                        synchronize all of the peers, but not to be
                        synchronized by any of them
                6, reserved for NTP control messages
                7, reserved for private use.
                
                When creating a new peer association, if no value
                is specified for this object, it defaults to
                symmetricActive(1).
                ''',
                'cntppeersmode',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersOffset', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The estimated offset of the peer clock relative to
                the local clock, in seconds.  The host determines the
                value of this object using the NTP clock-filter
                algorithm.
                ''',
                'cntppeersoffset',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersOrgTime', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The local time at the peer, when its latest
                NTP message was sent.  If the peer becomes unreachable
                the value is set to zero.
                ''',
                'cntppeersorgtime',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPeerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the peer.  When creating a new
                association, a value should be set either for this
                object or the corresponding instance of 
                cntpPeersPeerName, before the row is made active.
                ''',
                'cntppeerspeeraddress',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPeerName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the peer. When creating a new
                association, a value must be set for either this
                object or the corresponding instance of
                cntpPeersPeerAddress object, before the row
                is made active.
                ''',
                'cntppeerspeername',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPeerPoll', ATTRIBUTE, 'int' , None, None, 
                [('-20', '20')], [], 
                '''                The interval at which the peer polls the local host.
                ''',
                'cntppeerspeerpoll',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPeerPort', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The UDP port number on which the peer receives NTP
                messages.
                ''',
                'cntppeerspeerport',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPeerType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Represents the type of the corresponding instance
                of cntpPeersPeerName object.
                ''',
                'cntppeerspeertype',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPrecision', ATTRIBUTE, 'int' , None, None, 
                [('-20', '20')], [], 
                '''                Signed integer indicating the precision of the peer
                clock, in seconds to the nearest power of two.  The
                value must be rounded to the next larger power of
                two; for instance, a 50-Hz (20 ms) or 60-Hz
                (16.67 ms) power-frequency clock would be assigned
                the value -5 (31.25 ms), while a 1000-Hz (1 ms)
                crystal-controlled clock would be assigned the value
                -9 (1.95 ms).
                ''',
                'cntppeersprecision',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersPrefPeer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether this peer is the
                preferred one over the others. By default, when
                the value of this object is 'false', NTP chooses 
                the peer with which to synchronize the time on 
                the local system. If this object is set
                to 'true', NTP will choose the corresponding
                peer to synchronize the time with. If multiple
                entries have this object set to 'true', NTP will
                choose the first one to be set. This object is
                a means to override the selection of the peer by
                NTP.
                ''',
                'cntppeersprefpeer',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersReach', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                A shift register of used to determine the
                reachability status of the peer, with bits entering
                from the least significant (rightmost) end.  A peer is
                considered reachable if at least one bit in this
                register is set to one i.e, if the value of this
                object is non-zero.
                The data in the shift register would be populated by
                the NTP protocol procedures.
                ''',
                'cntppeersreach',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersReceiveTime', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The local time, when the latest NTP message from
                the peer arrived.  If the peer becomes unreachable
                the value is set to zero.
                ''',
                'cntppeersreceivetime',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersRefId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The reference identifier of the peer.
                ''',
                'cntppeersrefid',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersRefTime', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The local time at the peer when its clock was last
                updated.  If the peer clock has never been
                synchronized, the value is zero.
                ''',
                'cntppeersreftime',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersRootDelay', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                A signed fixed-point number indicating the total
                round-trip delay in seconds, from the peer to the
                primary reference source at the root of the
                synchronization subnet.
                ''',
                'cntppeersrootdelay',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersRootDispersion', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The maximum error in seconds, of the peer clock
                relative to the primary reference source at the root
                of the synchronization subnet.  Only positive values
                greater than zero are possible.
                ''',
                'cntppeersrootdispersion',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersStratum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The stratum of the peer clock.
                ''',
                'cntppeersstratum',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The interval in seconds, between transmitted NTP
                messages from the local host to the peer.
                ''',
                'cntppeerstimer',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersTransmitTime', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The local time at which the NTP message departed the
                sender.
                ''',
                'cntppeerstransmittime',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersUpdateTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The local time, when the most recent NTP message was
                received from the peer that was used to calculate the
                skew dispersion.  This represents only the 32-bit
                integer part of the NTPTimestamp.
                ''',
                'cntppeersupdatetime',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersUpdateTimeRev1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local time, when the most recent NTP message was
                received from the peer that was used to calculate the
                skew dispersion.  This represents only the 32-bit
                integer part of the NTPTimestamp.
                ''',
                'cntppeersupdatetimerev1',
                'CISCO-NTP-MIB', False),
            ],
            'CISCO-NTP-MIB',
            'cntpPeersVarEntry',
            _yang_ns._namespaces['CISCO-NTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NTP_MIB'
        ),
    },
    'CiscoNtpMib.Cntppeersvartable' : {
        'meta_info' : _MetaInfoClass('CiscoNtpMib.Cntppeersvartable',
            False, 
            [
            _MetaInfoClassMember('cntpPeersVarEntry', REFERENCE_LIST, 'Cntppeersvarentry' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry', 
                [], [], 
                '''                Each peers' entry provides NTP information retrieved
                from a particular peer NTP server.  Each peer is
                identified by a unique association identifier.
                
                Entries are automatically created when the user
                configures the NTP server to be associated with remote
                peers.  Similarly entries are deleted when the user
                removes the peer association from the NTP server.
                
                Entries can also be created by the management station
                by setting values for the following objects:
                cntpPeersPeerAddress or cntpPeersPeerName, 
                cntpPeersHostAddress and
                cntpPeersMode and making the cntpPeersEntryStatus as
                active(1).  At the least, the management station has
                to set a value for cntpPeersPeerAddress or
                cntpPeersPeerName to make the row active.
                ''',
                'cntppeersvarentry',
                'CISCO-NTP-MIB', False),
            ],
            'CISCO-NTP-MIB',
            'cntpPeersVarTable',
            _yang_ns._namespaces['CISCO-NTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NTP_MIB'
        ),
    },
    'CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry' : {
        'meta_info' : _MetaInfoClass('CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry',
            False, 
            [
            _MetaInfoClassMember('cntpPeersAssocId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ''',
                'cntppeersassocid',
                'CISCO-NTP-MIB', True),
            _MetaInfoClassMember('cntpFilterIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                An integer value in the specified range that is used
                to index into the table.  The size of the table is
                fixed at 8.  Each entry identifies a particular
                reading of the clock filter variables in the shift
                register.
                
                Entries are added starting at index 1.  The index
                wraps back to 1 when it reaches 8.  When the index
                wraps back, the new entries will overwrite the old
                entries effectively deleting the old entry.
                ''',
                'cntpfilterindex',
                'CISCO-NTP-MIB', True),
            _MetaInfoClassMember('cntpFilterPeersDelay', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Round-trip delay of the peer clock relative to the
                local clock over the network path between them, in
                seconds.  This variable can take on both positive and
                negative values, depending on clock precision and
                skew-error accumulation.
                ''',
                'cntpfilterpeersdelay',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpFilterPeersDispersion', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The maximum error of the peer clock relative to the
                local clock over the network path between them, in
                seconds.  Only positive values greater than zero are
                possible.
                ''',
                'cntpfilterpeersdispersion',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpFilterPeersOffset', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The offset of the peer clock relative to the
                local clock in seconds.
                ''',
                'cntpfilterpeersoffset',
                'CISCO-NTP-MIB', False),
            ],
            'CISCO-NTP-MIB',
            'cntpFilterRegisterEntry',
            _yang_ns._namespaces['CISCO-NTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NTP_MIB'
        ),
    },
    'CiscoNtpMib.Cntpfilterregistertable' : {
        'meta_info' : _MetaInfoClass('CiscoNtpMib.Cntpfilterregistertable',
            False, 
            [
            _MetaInfoClassMember('cntpFilterRegisterEntry', REFERENCE_LIST, 'Cntpfilterregisterentry' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry', 
                [], [], 
                '''                Each entry corresponds to one stage of the shift
                register, i.e., one reading of the variables clock
                delay, clock offset and clock dispersion.
                
                Entries are automatically created whenever a peer is
                configured and deleted when the peer is removed.
                ''',
                'cntpfilterregisterentry',
                'CISCO-NTP-MIB', False),
            ],
            'CISCO-NTP-MIB',
            'cntpFilterRegisterTable',
            _yang_ns._namespaces['CISCO-NTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NTP_MIB'
        ),
    },
    'CiscoNtpMib' : {
        'meta_info' : _MetaInfoClass('CiscoNtpMib',
            False, 
            [
            _MetaInfoClassMember('cntpFilterRegisterTable', REFERENCE_CLASS, 'Cntpfilterregistertable' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntpfilterregistertable', 
                [], [], 
                '''                The following table contains NTP state variables
                used by the NTP clock filter and selection algorithms.
                This table depicts a shift register.  Each stage in
                the shift register is a 3-tuple consisting of the
                measured clock offset, measured clock delay and
                measured clock dispersion associated with a single
                observation.
                
                An important factor affecting the accuracy and
                reliability of time distribution is the complex of
                algorithms used to reduce the effect of statistical
                errors and falsetickers due to failure of various
                subnet components, reference sources or propagation
                media.  The NTP clock-filter and selection algorithms
                are designed to do exactly this.  The objects in the
                filter register table below are used by these
                algorthims to minimize the error in the calculated
                time.
                ''',
                'cntpfilterregistertable',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpPeersVarTable', REFERENCE_CLASS, 'Cntppeersvartable' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntppeersvartable', 
                [], [], 
                '''                This table provides information on the peers with
                which the local NTP server has associations.  The
                peers are also NTP servers but running on different
                hosts.
                ''',
                'cntppeersvartable',
                'CISCO-NTP-MIB', False),
            _MetaInfoClassMember('cntpSystem', REFERENCE_CLASS, 'Cntpsystem' , 'ydk.models.cisco_ios_xe.CISCO_NTP_MIB', 'CiscoNtpMib.Cntpsystem', 
                [], [], 
                '''                ''',
                'cntpsystem',
                'CISCO-NTP-MIB', False),
            ],
            'CISCO-NTP-MIB',
            'CISCO-NTP-MIB',
            _yang_ns._namespaces['CISCO-NTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NTP_MIB'
        ),
    },
}
_meta_table['CiscoNtpMib.Cntppeersvartable.Cntppeersvarentry']['meta_info'].parent =_meta_table['CiscoNtpMib.Cntppeersvartable']['meta_info']
_meta_table['CiscoNtpMib.Cntpfilterregistertable.Cntpfilterregisterentry']['meta_info'].parent =_meta_table['CiscoNtpMib.Cntpfilterregistertable']['meta_info']
_meta_table['CiscoNtpMib.Cntpsystem']['meta_info'].parent =_meta_table['CiscoNtpMib']['meta_info']
_meta_table['CiscoNtpMib.Cntppeersvartable']['meta_info'].parent =_meta_table['CiscoNtpMib']['meta_info']
_meta_table['CiscoNtpMib.Cntpfilterregistertable']['meta_info'].parent =_meta_table['CiscoNtpMib']['meta_info']
