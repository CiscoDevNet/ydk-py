


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TCPMIB.Tcp.TcpRtoAlgorithm_Enum' : _MetaInfoEnum('TcpRtoAlgorithm_Enum', 'ydk.models.tcp.TCP_MIB',
        {
            'other':'OTHER',
            'constant':'CONSTANT',
            'rsre':'RSRE',
            'vanj':'VANJ',
            'rfc2988':'RFC2988',
        }, 'TCP-MIB', _yang_ns._namespaces['TCP-MIB']),
    'TCPMIB.Tcp' : {
        'meta_info' : _MetaInfoClass('TCPMIB.Tcp',
            False, 
            [
            _MetaInfoClassMember('tcpActiveOpens', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times that TCP connections have made a direct
                transition to the SYN-SENT state from the CLOSED state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpactiveopens',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpAttemptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The number of TCP connections for which the current state
                is either ESTABLISHED or CLOSE-WAIT.
                ''',
                'tcpcurrestab',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpEstabResets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times that TCP connections have made a direct
                transition to the CLOSED state from either the ESTABLISHED
                state or the CLOSE-WAIT state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpestabresets',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpHCInSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
                [(0, 18446744073709551615L)], [], 
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
                [(0, 4294967295)], [], 
                '''                The total number of segments received in error (e.g., bad
                TCP checksums).
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpinerrs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpInSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments received, including those
                received in error.  This count includes segments received
                on currently established connections.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpinsegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpMaxConn', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The limit on the total number of TCP connections the entity
                can support.  In entities where the maximum number of
                connections is dynamic, this object should contain the
                value -1.
                ''',
                'tcpmaxconn',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpOutRsts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of TCP segments sent containing the RST flag.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpoutrsts',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpOutSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments sent, including those on
                current connections but excluding those containing only
                retransmitted octets.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpoutsegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpPassiveOpens', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times TCP connections have made a direct
                transition to the SYN-RCVD state from the LISTEN state.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcppassiveopens',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRetransSegs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of segments retransmitted; that is, the
                number of TCP segments transmitted containing one or more
                previously transmitted octets.
                
                Discontinuities in the value of this counter are
                indicated via discontinuities in the value of sysUpTime.
                ''',
                'tcpretranssegs',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRtoAlgorithm', REFERENCE_ENUM_CLASS, 'TcpRtoAlgorithm_Enum' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.Tcp.TcpRtoAlgorithm_Enum', 
                [], [], 
                '''                The algorithm used to determine the timeout value used for
                retransmitting unacknowledged octets.
                ''',
                'tcprtoalgorithm',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpRtoMax', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
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
                [(0, 2147483647)], [], 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum' : _MetaInfoEnum('TcpConnState_Enum', 'ydk.models.tcp.TCP_MIB',
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
        }, 'TCP-MIB', _yang_ns._namespaces['TCP-MIB']),
    'TCPMIB.TcpConnTable.TcpConnEntry' : {
        'meta_info' : _MetaInfoClass('TCPMIB.TcpConnTable.TcpConnEntry',
            False, 
            [
            _MetaInfoClassMember('tcpConnLocalAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address for this TCP connection.  In the case
                of a connection in the listen state willing to
                accept connections for any IP interface associated with the
                node, the value 0.0.0.0 is used.
                ''',
                'tcpconnlocaladdress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcpconnlocalport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnRemAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The remote IP address for this TCP connection.
                ''',
                'tcpconnremaddress',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnRemPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The remote port number for this TCP connection.
                ''',
                'tcpconnremport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnState', REFERENCE_ENUM_CLASS, 'TcpConnState_Enum' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum', 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB.TcpConnTable' : {
        'meta_info' : _MetaInfoClass('TCPMIB.TcpConnTable',
            False, 
            [
            _MetaInfoClassMember('tcpConnEntry', REFERENCE_LIST, 'TcpConnEntry' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpConnTable.TcpConnEntry', 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB.TcpConnectionTable.TcpConnectionEntry.TcpConnectionState_Enum' : _MetaInfoEnum('TcpConnectionState_Enum', 'ydk.models.tcp.TCP_MIB',
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
        }, 'TCP-MIB', _yang_ns._namespaces['TCP-MIB']),
    'TCPMIB.TcpConnectionTable.TcpConnectionEntry' : {
        'meta_info' : _MetaInfoClass('TCPMIB.TcpConnectionTable.TcpConnectionEntry',
            False, 
            [
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
            _MetaInfoClassMember('tcpConnectionLocalAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The address type of tcpConnectionLocalAddress.
                ''',
                'tcpconnectionlocaladdresstype',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcpconnectionlocalport',
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
            _MetaInfoClassMember('tcpConnectionRemAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The address type of tcpConnectionRemAddress.
                ''',
                'tcpconnectionremaddresstype',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionRemPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The remote port number for this TCP connection.
                ''',
                'tcpconnectionremport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpConnectionProcess', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The system's process ID for the process associated with
                this connection, or zero if there is no such process.  This
                value is expected to be the same as HOST-RESOURCES-MIB::
                hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some
                row in the appropriate tables.
                ''',
                'tcpconnectionprocess',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpConnectionState', REFERENCE_ENUM_CLASS, 'TcpConnectionState_Enum' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpConnectionTable.TcpConnectionEntry.TcpConnectionState_Enum', 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB.TcpConnectionTable' : {
        'meta_info' : _MetaInfoClass('TCPMIB.TcpConnectionTable',
            False, 
            [
            _MetaInfoClassMember('tcpConnectionEntry', REFERENCE_LIST, 'TcpConnectionEntry' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpConnectionTable.TcpConnectionEntry', 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB.TcpListenerTable.TcpListenerEntry' : {
        'meta_info' : _MetaInfoClass('TCPMIB.TcpListenerTable.TcpListenerEntry',
            False, 
            [
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
            _MetaInfoClassMember('tcpListenerLocalAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The address type of tcpListenerLocalAddress.  The value
                should be unknown (0) if connection initiations to all
                local IP addresses are accepted.
                ''',
                'tcplistenerlocaladdresstype',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpListenerLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The local port number for this TCP connection.
                ''',
                'tcplistenerlocalport',
                'TCP-MIB', True),
            _MetaInfoClassMember('tcpListenerProcess', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB.TcpListenerTable' : {
        'meta_info' : _MetaInfoClass('TCPMIB.TcpListenerTable',
            False, 
            [
            _MetaInfoClassMember('tcpListenerEntry', REFERENCE_LIST, 'TcpListenerEntry' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpListenerTable.TcpListenerEntry', 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
    'TCPMIB' : {
        'meta_info' : _MetaInfoClass('TCPMIB',
            False, 
            [
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.Tcp', 
                [], [], 
                '''                ''',
                'tcp',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpConnectionTable', REFERENCE_CLASS, 'TcpConnectionTable' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpConnectionTable', 
                [], [], 
                '''                A table containing information about existing TCP
                connections.  Note that unlike earlier TCP MIBs, there
                is a separate table for connections in the LISTEN state.
                ''',
                'tcpconnectiontable',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpConnTable', REFERENCE_CLASS, 'TcpConnTable' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpConnTable', 
                [], [], 
                '''                A table containing information about existing IPv4-specific
                TCP connections or listeners.  This table has been
                deprecated in favor of the version neutral
                tcpConnectionTable.
                ''',
                'tcpconntable',
                'TCP-MIB', False),
            _MetaInfoClassMember('tcpListenerTable', REFERENCE_CLASS, 'TcpListenerTable' , 'ydk.models.tcp.TCP_MIB', 'TCPMIB.TcpListenerTable', 
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
        'ydk.models.tcp.TCP_MIB'
        ),
    },
}
_meta_table['TCPMIB.TcpConnTable.TcpConnEntry']['meta_info'].parent =_meta_table['TCPMIB.TcpConnTable']['meta_info']
_meta_table['TCPMIB.TcpConnectionTable.TcpConnectionEntry']['meta_info'].parent =_meta_table['TCPMIB.TcpConnectionTable']['meta_info']
_meta_table['TCPMIB.TcpListenerTable.TcpListenerEntry']['meta_info'].parent =_meta_table['TCPMIB.TcpListenerTable']['meta_info']
_meta_table['TCPMIB.Tcp']['meta_info'].parent =_meta_table['TCPMIB']['meta_info']
_meta_table['TCPMIB.TcpConnTable']['meta_info'].parent =_meta_table['TCPMIB']['meta_info']
_meta_table['TCPMIB.TcpConnectionTable']['meta_info'].parent =_meta_table['TCPMIB']['meta_info']
_meta_table['TCPMIB.TcpListenerTable']['meta_info'].parent =_meta_table['TCPMIB']['meta_info']
