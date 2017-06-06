


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TcpMib.Tcp.TcprtoalgorithmEnum' : _MetaInfoEnum('TcprtoalgorithmEnum', 'ydk.models.cisco_ios_xe.TCP_MIB',
        {
            'other':'other',
            'constant':'constant',
            'rsre':'rsre',
            'vanj':'vanj',
            'rfc2988':'rfc2988',
        }, 'TCP-MIB', _yang_ns._namespaces['TCP-MIB']),
    'TcpMib.Tcp' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcp',
            False, 
            [
            _MetaInfoClassMember('tcpActiveOpens', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times that TCP connections have made a direct
                transition to the SYN-SENT state from the CLOSED state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpactiveopens',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpAttemptFails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times that TCP connections have made a direct
                transition to the CLOSED state from either the SYN-SENT
                state or the SYN-RCVD state, plus the number of times that
                TCP connections have made a direct transition to the
                LISTEN state from the SYN-RCVD state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpattemptfails',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpCurrEstab', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of TCP connections for which the current state
                is either ESTABLISHED or CLOSE-WAIT.
                ''',
                'tcpcurrestab',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpEstabResets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times that TCP connections have made a direct
                transition to the CLOSED state from either the ESTABLISHED
                state or the CLOSE-WAIT state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpestabresets',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpHCInSegs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of segments received, including those
                received in error.  This count includes segments received
                
                on currently established connections.  This object is
                the 64-bit equivalent of tcpInSegs.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcphcinsegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpHCOutSegs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of segments sent, including those on
                current connections but excluding those containing only
                retransmitted octets.  This object is the 64-bit
                equivalent of tcpOutSegs.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcphcoutsegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpInErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of segments received in error (e.g., bad
                TCP checksums).
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpinerrs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpInSegs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of segments received, including those
                received in error.  This count includes segments received
                on currently established connections.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpinsegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpMaxConn', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The limit on the total number of TCP connections the entity
                can support.  In entities where the maximum number of
                connections is dynamic, this object should contain the
                value -1.
                ''',
                'tcpmaxconn',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpOutRsts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of TCP segments sent containing the RST flag.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpoutrsts',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpOutSegs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of segments sent, including those on
                current connections but excluding those containing only
                retransmitted octets.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpoutsegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpPassiveOpens', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times TCP connections have made a direct
                transition to the SYN-RCVD state from the LISTEN state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcppassiveopens',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRetransSegs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of segments retransmitted; that is, the
                number of TCP segments transmitted containing one or more
                previously transmitted octets.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpretranssegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRtoAlgorithm', REFERENCE_ENUM_CLASS, 'TcprtoalgorithmEnum' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcp.TcprtoalgorithmEnum', 
                [], [], 
                '''                The algorithm used to determine the timeout value used for
                retransmitting unacknowledged octets.
                ''',
                'tcprtoalgorithm',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRtoMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The maximum value permitted by a TCP implementation for
                the retransmission timeout, measured in milliseconds.
                More refined semantics for objects of this type depend
                on the algorithm used to determine the retransmission
                timeout; in particular, the IETF standard algorithm
                rfc2988(5) provides an upper bound (as part of an
                adaptive backoff algorithm).
                ''',
                'tcprtomax',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRtoMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The minimum value permitted by a TCP implementation for
                the retransmission timeout, measured in milliseconds.
                More refined semantics for objects of this type depend
                on the algorithm used to determine the retransmission
                timeout; in particular, the IETF standard algorithm
                rfc2988(5) provides a minimum value.
                ''',
                'tcprtomin',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcp',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib.Tcpconntable.Tcpconnentry.TcpconnstateEnum' : _MetaInfoEnum('TcpconnstateEnum', 'ydk.models.cisco_ios_xe.TCP_MIB',
        {
            'closed':'closed',
            'listen':'listen',
            'synSent':'synSent',
            'synReceived':'synReceived',
            'established':'established',
            'finWait1':'finWait1',
            'finWait2':'finWait2',
            'closeWait':'closeWait',
            'lastAck':'lastAck',
            'closing':'closing',
            'timeWait':'timeWait',
            'deleteTCB':'deleteTCB',
        }, 'TCP-MIB', _yang_ns._namespaces['TCP-MIB']),
    'TcpMib.Tcpconntable.Tcpconnentry' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcpconntable.Tcpconnentry',
            False, 
            [
            _MetaInfoClassMember('tcpConnLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address for this TCP connection.  In the case
                of a connection in the listen state willing to
                accept connections for any IP interface associated with the
                node, the value 0.0.0.0 is used.
                ''',
                'tcpconnlocaladdress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcpconnlocalport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnRemAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The remote IP address for this TCP connection.
                ''',
                'tcpconnremaddress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnRemPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote port number for this TCP connection.
                ''',
                'tcpconnremport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnState', REFERENCE_ENUM_CLASS, 'TcpconnstateEnum' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcpconntable.Tcpconnentry.TcpconnstateEnum', 
                [], [], 
                '''                The state of this TCP connection.
                
                The only value that may be set by a management station is
                deleteTCB(12).  Accordingly, it is appropriate for an agent
                to return a `badValue' response if a management station
                attempts to set this object to any other value.
                
                If a management station sets this object to the value
                deleteTCB(12), then the TCB (as defined in [RFC793]) of
                the corresponding connection on the managed node is
                deleted, resulting in immediate termination of the
                connection.
                
                As an implementation-specific option, a RST segment may be
                sent from the managed node to the other TCP endpoint (note,
                however, that RST segments are not sent reliably).
                ''',
                'tcpconnstate',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcpConnEntry',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib.Tcpconntable' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcpconntable',
            False, 
            [
            _MetaInfoClassMember('tcpConnEntry', REFERENCE_LIST, 'Tcpconnentry' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcpconntable.Tcpconnentry', 
                [], [], 
                '''                A conceptual row of the tcpConnTable containing information
                about a particular current IPv4 TCP connection.  Each row
                of this table is transient in that it ceases to exist when
                (or soon after) the connection makes the transition to the
                CLOSED state.
                ''',
                'tcpconnentry',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcpConnTable',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib.Tcpconnectiontable.Tcpconnectionentry.TcpconnectionstateEnum' : _MetaInfoEnum('TcpconnectionstateEnum', 'ydk.models.cisco_ios_xe.TCP_MIB',
        {
            'closed':'closed',
            'listen':'listen',
            'synSent':'synSent',
            'synReceived':'synReceived',
            'established':'established',
            'finWait1':'finWait1',
            'finWait2':'finWait2',
            'closeWait':'closeWait',
            'lastAck':'lastAck',
            'closing':'closing',
            'timeWait':'timeWait',
            'deleteTCB':'deleteTCB',
        }, 'TCP-MIB', _yang_ns._namespaces['TCP-MIB']),
    'TcpMib.Tcpconnectiontable.Tcpconnectionentry' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcpconnectiontable.Tcpconnectionentry',
            False, 
            [
            _MetaInfoClassMember('tcpConnectionLocalAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of tcpConnectionLocalAddress.
                ''',
                'tcpconnectionlocaladdresstype',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The local IP address for this TCP connection.  The type
                of this address is determined by the value of
                tcpConnectionLocalAddressType.
                
                As this object is used in the index for the
                tcpConnectionTable, implementors should be
                careful not to create entries that would result in OIDs
                with more than 128 subidentifiers; otherwise the information
                cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'tcpconnectionlocaladdress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcpconnectionlocalport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionRemAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of tcpConnectionRemAddress.
                ''',
                'tcpconnectionremaddresstype',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionRemAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The remote IP address for this TCP connection.  The type
                of this address is determined by the value of
                tcpConnectionRemAddressType.
                
                As this object is used in the index for the
                tcpConnectionTable, implementors should be
                careful not to create entries that would result in OIDs
                with more than 128 subidentifiers; otherwise the information
                cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'tcpconnectionremaddress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionRemPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote port number for this TCP connection.
                ''',
                'tcpconnectionremport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionProcess', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The system's process ID for the process associated with
                this connection, or zero if there is no such process.  This
                value is expected to be the same as HOST-RESOURCES-MIB::
                hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some
                row in the appropriate tables.
                ''',
                'tcpconnectionprocess',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpConnectionState', REFERENCE_ENUM_CLASS, 'TcpconnectionstateEnum' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcpconnectiontable.Tcpconnectionentry.TcpconnectionstateEnum', 
                [], [], 
                '''                The state of this TCP connection.
                
                The value listen(2) is included only for parallelism to the
                old tcpConnTable and should not be used.  A connection in
                LISTEN state should be present in the tcpListenerTable.
                
                The only value that may be set by a management station is
                deleteTCB(12).  Accordingly, it is appropriate for an agent
                to return a `badValue' response if a management station
                attempts to set this object to any other value.
                
                If a management station sets this object to the value
                deleteTCB(12), then the TCB (as defined in [RFC793]) of
                the corresponding connection on the managed node is
                deleted, resulting in immediate termination of the
                connection.
                
                As an implementation-specific option, a RST segment may be
                sent from the managed node to the other TCP endpoint (note,
                however, that RST segments are not sent reliably).
                ''',
                'tcpconnectionstate',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcpConnectionEntry',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib.Tcpconnectiontable' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcpconnectiontable',
            False, 
            [
            _MetaInfoClassMember('tcpConnectionEntry', REFERENCE_LIST, 'Tcpconnectionentry' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcpconnectiontable.Tcpconnectionentry', 
                [], [], 
                '''                A conceptual row of the tcpConnectionTable containing
                information about a particular current TCP connection.
                Each row of this table is transient in that it ceases to
                exist when (or soon after) the connection makes the
                transition to the CLOSED state.
                ''',
                'tcpconnectionentry',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcpConnectionTable',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib.Tcplistenertable.Tcplistenerentry' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcplistenertable.Tcplistenerentry',
            False, 
            [
            _MetaInfoClassMember('tcpListenerLocalAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of tcpListenerLocalAddress.  The value
                should be unknown (0) if connection initiations to all
                local IP addresses are accepted.
                ''',
                'tcplistenerlocaladdresstype',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpListenerLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The local IP address for this TCP connection.
                
                The value of this object can be represented in three
                possible ways, depending on the characteristics of the
                listening application:
                
                1. For an application willing to accept both IPv4 and
                   IPv6 datagrams, the value of this object must be
                   ''h (a zero-length octet-string), with the value
                   of the corresponding tcpListenerLocalAddressType
                   object being unknown (0).
                
                2. For an application willing to accept only IPv4 or
                   IPv6 datagrams, the value of this object must be
                   '0.0.0.0' or '::' respectively, with
                   tcpListenerLocalAddressType representing the
                   appropriate address type.
                
                3. For an application which is listening for data
                   destined only to a specific IP address, the value
                   of this object is the specific local address, with
                   tcpListenerLocalAddressType representing the
                   appropriate address type.
                
                As this object is used in the index for the
                tcpListenerTable, implementors should be
                careful not to create entries that would result in OIDs
                with more than 128 subidentifiers; otherwise the information
                cannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'tcplistenerlocaladdress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpListenerLocalPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcplistenerlocalport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpListenerProcess', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The system's process ID for the process associated with
                this listener, or zero if there is no such process.  This
                value is expected to be the same as HOST-RESOURCES-MIB::
                hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some
                row in the appropriate tables.
                ''',
                'tcplistenerprocess',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcpListenerEntry',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib.Tcplistenertable' : {
        'meta_info' : _MetaInfoClass('TcpMib.Tcplistenertable',
            False, 
            [
            _MetaInfoClassMember('tcpListenerEntry', REFERENCE_LIST, 'Tcplistenerentry' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcplistenertable.Tcplistenerentry', 
                [], [], 
                '''                A conceptual row of the tcpListenerTable containing
                information about a particular TCP listener.
                ''',
                'tcplistenerentry',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'tcpListenerTable',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
    'TcpMib' : {
        'meta_info' : _MetaInfoClass('TcpMib',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcp', 
                [], [], 
                '''                ''',
                'tcp',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpConnectionTable', REFERENCE_CLASS, 'Tcpconnectiontable' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcpconnectiontable', 
                [], [], 
                '''                A table containing information about existing TCP
                connections.  Note that unlike earlier TCP MIBs, there
                is a separate table for connections in the LISTEN state.
                ''',
                'tcpconnectiontable',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpConnTable', REFERENCE_CLASS, 'Tcpconntable' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcpconntable', 
                [], [], 
                '''                A table containing information about existing IPv4-specific
                TCP connections or listeners.  This table has been
                deprecated in favor of the version neutral
                tcpConnectionTable.
                ''',
                'tcpconntable',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpListenerTable', REFERENCE_CLASS, 'Tcplistenertable' , 'ydk.models.cisco_ios_xe.TCP_MIB', 'TcpMib.Tcplistenertable', 
                [], [], 
                '''                A table containing information about TCP listeners.  A
                listening application can be represented in three
                possible ways:
                
                1. An application that is willing to accept both IPv4 and
                   IPv6 datagrams is represented by
                
                   a tcpListenerLocalAddressType of unknown (0) and
                   a tcpListenerLocalAddress of ''h (a zero-length
                   octet-string).
                
                2. An application that is willing to accept only IPv4 or
                   IPv6 datagrams is represented by a
                   tcpListenerLocalAddressType of the appropriate address
                   type and a tcpListenerLocalAddress of '0.0.0.0' or '::'
                   respectively.
                
                3. An application that is listening for data destined
                   only to a specific IP address, but from any remote
                   system, is represented by a tcpListenerLocalAddressType
                   of an appropriate address type, with
                   tcpListenerLocalAddress as the specific local address.
                
                NOTE: The address type in this table represents the
                address type used for the communication, irrespective
                of the higher-layer abstraction.  For example, an
                application using IPv6 'sockets' to communicate via
                IPv4 between ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would
                use InetAddressType ipv4(1)).
                ''',
                'tcplistenertable',
                'TCP-MIB', False),
            ],
            'TCP-MIB',
            'TCP-MIB',
            _yang_ns._namespaces['TCP-MIB'],
        'ydk.models.cisco_ios_xe.TCP_MIB'
        ),
    },
}
_meta_table['TcpMib.Tcpconntable.Tcpconnentry']['meta_info'].parent =_meta_table['TcpMib.Tcpconntable']['meta_info']
_meta_table['TcpMib.Tcpconnectiontable.Tcpconnectionentry']['meta_info'].parent =_meta_table['TcpMib.Tcpconnectiontable']['meta_info']
_meta_table['TcpMib.Tcplistenertable.Tcplistenerentry']['meta_info'].parent =_meta_table['TcpMib.Tcplistenertable']['meta_info']
_meta_table['TcpMib.Tcp']['meta_info'].parent =_meta_table['TcpMib']['meta_info']
_meta_table['TcpMib.Tcpconntable']['meta_info'].parent =_meta_table['TcpMib']['meta_info']
_meta_table['TcpMib.Tcpconnectiontable']['meta_info'].parent =_meta_table['TcpMib']['meta_info']
_meta_table['TcpMib.Tcplistenertable']['meta_info'].parent =_meta_table['TcpMib']['meta_info']
