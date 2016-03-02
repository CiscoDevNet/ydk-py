""" TCP_MIB 

The MIB module for managing TCP implementations.

Copyright (C) The Internet Society (2005). This version
of this MIB module is a part of RFC 4022; see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum


class TCPMIB(object):
    """
    
    
    .. attribute:: tcp
    
    	
    	**type**\: :py:class:`Tcp <ydk.models.tcp.TCP_MIB.TCPMIB.Tcp>`
    
    .. attribute:: tcpconnectiontable
    
    	A table containing information about existing TCP connections.  Note that unlike earlier TCP MIBs, there is a separate table for connections in the LISTEN state
    	**type**\: :py:class:`TcpConnectionTable <ydk.models.tcp.TCP_MIB.TCPMIB.TcpConnectionTable>`
    
    .. attribute:: tcpconntable
    
    	A table containing information about existing IPv4\-specific TCP connections or listeners.  This table has been deprecated in favor of the version neutral tcpConnectionTable
    	**type**\: :py:class:`TcpConnTable <ydk.models.tcp.TCP_MIB.TCPMIB.TcpConnTable>`
    
    .. attribute:: tcplistenertable
    
    	A table containing information about TCP listeners.  A listening application can be represented in three possible ways\:  1. An application that is willing to accept both IPv4 and    IPv6 datagrams is represented by     a tcpListenerLocalAddressType of unknown (0) and    a tcpListenerLocalAddress of ''h (a zero\-length    octet\-string).  2. An application that is willing to accept only IPv4 or    IPv6 datagrams is represented by a    tcpListenerLocalAddressType of the appropriate address    type and a tcpListenerLocalAddress of '0.0.0.0' or '\:\:'    respectively.  3. An application that is listening for data destined    only to a specific IP address, but from any remote    system, is represented by a tcpListenerLocalAddressType    of an appropriate address type, with    tcpListenerLocalAddress as the specific local address.  NOTE\: The address type in this table represents the address type used for the communication, irrespective of the higher\-layer abstraction.  For example, an application using IPv6 'sockets' to communicate via IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use InetAddressType ipv4(1))
    	**type**\: :py:class:`TcpListenerTable <ydk.models.tcp.TCP_MIB.TCPMIB.TcpListenerTable>`
    
    

    """

    _prefix = 'tcp-mib'
    _revision = '2005-02-18'

    def __init__(self):
        self.tcp = TCPMIB.Tcp()
        self.tcp.parent = self
        self.tcpconnectiontable = TCPMIB.TcpConnectionTable()
        self.tcpconnectiontable.parent = self
        self.tcpconntable = TCPMIB.TcpConnTable()
        self.tcpconntable.parent = self
        self.tcplistenertable = TCPMIB.TcpListenerTable()
        self.tcplistenertable.parent = self


    class Tcp(object):
        """
        
        
        .. attribute:: tcpactiveopens
        
        	The number of times that TCP connections have made a direct transition to the SYN\-SENT state from the CLOSED state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpattemptfails
        
        	The number of times that TCP connections have made a direct transition to the CLOSED state from either the SYN\-SENT state or the SYN\-RCVD state, plus the number of times that TCP connections have made a direct transition to the LISTEN state from the SYN\-RCVD state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpcurrestab
        
        	The number of TCP connections for which the current state is either ESTABLISHED or CLOSE\-WAIT
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpestabresets
        
        	The number of times that TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE\-WAIT state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcphcinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received  on currently established connections.  This object is the 64\-bit equivalent of tcpInSegs.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tcphcoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.  This object is the 64\-bit equivalent of tcpOutSegs.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tcpinerrs
        
        	The total number of segments received in error (e.g., bad TCP checksums).  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received on currently established connections.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpmaxconn
        
        	The limit on the total number of TCP connections the entity can support.  In entities where the maximum number of connections is dynamic, this object should contain the value \-1
        	**type**\: int
        
        	**range:** \-1..2147483647
        
        .. attribute:: tcpoutrsts
        
        	The number of TCP segments sent containing the RST flag.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcppassiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-RCVD state from the LISTEN state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpretranssegs
        
        	The total number of segments retransmitted; that is, the number of TCP segments transmitted containing one or more previously transmitted octets.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcprtoalgorithm
        
        	The algorithm used to determine the timeout value used for retransmitting unacknowledged octets
        	**type**\: :py:class:`TcpRtoAlgorithm_Enum <ydk.models.tcp.TCP_MIB.TCPMIB.Tcp.TcpRtoAlgorithm_Enum>`
        
        .. attribute:: tcprtomax
        
        	The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides an upper bound (as part of an adaptive backoff algorithm)
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: tcprtomin
        
        	The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides a minimum value
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'tcp-mib'
        _revision = '2005-02-18'

        def __init__(self):
            self.parent = None
            self.tcpactiveopens = None
            self.tcpattemptfails = None
            self.tcpcurrestab = None
            self.tcpestabresets = None
            self.tcphcinsegs = None
            self.tcphcoutsegs = None
            self.tcpinerrs = None
            self.tcpinsegs = None
            self.tcpmaxconn = None
            self.tcpoutrsts = None
            self.tcpoutsegs = None
            self.tcppassiveopens = None
            self.tcpretranssegs = None
            self.tcprtoalgorithm = None
            self.tcprtomax = None
            self.tcprtomin = None

        class TcpRtoAlgorithm_Enum(Enum):
            """
            TcpRtoAlgorithm_Enum

            The algorithm used to determine the timeout value used for
            retransmitting unacknowledged octets.

            """

            OTHER = 1

            CONSTANT = 2

            RSRE = 3

            VANJ = 4

            RFC2988 = 5


            @staticmethod
            def _meta_info():
                from ydk.models.tcp._meta import _TCP_MIB as meta
                return meta._meta_table['TCPMIB.Tcp.TcpRtoAlgorithm_Enum']


        @property
        def _common_path(self):

            return '/TCP-MIB:TCP-MIB/TCP-MIB:tcp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tcpactiveopens is not None:
                return True

            if self.tcpattemptfails is not None:
                return True

            if self.tcpcurrestab is not None:
                return True

            if self.tcpestabresets is not None:
                return True

            if self.tcphcinsegs is not None:
                return True

            if self.tcphcoutsegs is not None:
                return True

            if self.tcpinerrs is not None:
                return True

            if self.tcpinsegs is not None:
                return True

            if self.tcpmaxconn is not None:
                return True

            if self.tcpoutrsts is not None:
                return True

            if self.tcpoutsegs is not None:
                return True

            if self.tcppassiveopens is not None:
                return True

            if self.tcpretranssegs is not None:
                return True

            if self.tcprtoalgorithm is not None:
                return True

            if self.tcprtomax is not None:
                return True

            if self.tcprtomin is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tcp._meta import _TCP_MIB as meta
            return meta._meta_table['TCPMIB.Tcp']['meta_info']


    class TcpConnTable(object):
        """
        A table containing information about existing IPv4\-specific
        TCP connections or listeners.  This table has been
        deprecated in favor of the version neutral
        tcpConnectionTable.
        
        .. attribute:: tcpconnentry
        
        	A conceptual row of the tcpConnTable containing information about a particular current IPv4 TCP connection.  Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of :py:class:`TcpConnEntry <ydk.models.tcp.TCP_MIB.TCPMIB.TcpConnTable.TcpConnEntry>`
        
        

        """

        _prefix = 'tcp-mib'
        _revision = '2005-02-18'

        def __init__(self):
            self.parent = None
            self.tcpconnentry = YList()
            self.tcpconnentry.parent = self
            self.tcpconnentry.name = 'tcpconnentry'


        class TcpConnEntry(object):
            """
            A conceptual row of the tcpConnTable containing information
            about a particular current IPv4 TCP connection.  Each row
            of this table is transient in that it ceases to exist when
            (or soon after) the connection makes the transition to the
            CLOSED state.
            
            .. attribute:: tcpconnlocaladdress
            
            	The local IP address for this TCP connection.  In the case of a connection in the listen state willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnlocalport
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnremaddress
            
            	The remote IP address for this TCP connection
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnremport
            
            	The remote port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnstate
            
            	The state of this TCP connection.  The only value that may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably)
            	**type**\: :py:class:`TcpConnState_Enum <ydk.models.tcp.TCP_MIB.TCPMIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum>`
            
            

            """

            _prefix = 'tcp-mib'
            _revision = '2005-02-18'

            def __init__(self):
                self.parent = None
                self.tcpconnlocaladdress = None
                self.tcpconnlocalport = None
                self.tcpconnremaddress = None
                self.tcpconnremport = None
                self.tcpconnstate = None

            class TcpConnState_Enum(Enum):
                """
                TcpConnState_Enum

                The state of this TCP connection.
                
                The only value that may be set by a management station is
                deleteTCB(12).  Accordingly, it is appropriate for an agent
                to return a `badValue' response if a management station
                attempts to set this object to any other value.
                
                If a management station sets this object to the value
                deleteTCB(12), then the TCB (as defined in [RFC793]) of
                the corresponding connection on the managed node is
                deleted, resulting in immediate termination of the
                connection.
                
                As an implementation\-specific option, a RST segment may be
                sent from the managed node to the other TCP endpoint (note,
                however, that RST segments are not sent reliably).

                """

                CLOSED = 1

                LISTEN = 2

                SYNSENT = 3

                SYNRECEIVED = 4

                ESTABLISHED = 5

                FINWAIT1 = 6

                FINWAIT2 = 7

                CLOSEWAIT = 8

                LASTACK = 9

                CLOSING = 10

                TIMEWAIT = 11

                DELETETCB = 12


                @staticmethod
                def _meta_info():
                    from ydk.models.tcp._meta import _TCP_MIB as meta
                    return meta._meta_table['TCPMIB.TcpConnTable.TcpConnEntry.TcpConnState_Enum']


            @property
            def _common_path(self):
                if self.tcpconnlocaladdress is None:
                    raise YPYDataValidationError('Key property tcpconnlocaladdress is None')
                if self.tcpconnlocalport is None:
                    raise YPYDataValidationError('Key property tcpconnlocalport is None')
                if self.tcpconnremaddress is None:
                    raise YPYDataValidationError('Key property tcpconnremaddress is None')
                if self.tcpconnremport is None:
                    raise YPYDataValidationError('Key property tcpconnremport is None')

                return '/TCP-MIB:TCP-MIB/TCP-MIB:tcpConnTable/TCP-MIB:tcpConnEntry[TCP-MIB:tcpConnLocalAddress = ' + str(self.tcpconnlocaladdress) + '][TCP-MIB:tcpConnLocalPort = ' + str(self.tcpconnlocalport) + '][TCP-MIB:tcpConnRemAddress = ' + str(self.tcpconnremaddress) + '][TCP-MIB:tcpConnRemPort = ' + str(self.tcpconnremport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tcpconnlocaladdress is not None:
                    return True

                if self.tcpconnlocalport is not None:
                    return True

                if self.tcpconnremaddress is not None:
                    return True

                if self.tcpconnremport is not None:
                    return True

                if self.tcpconnstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tcp._meta import _TCP_MIB as meta
                return meta._meta_table['TCPMIB.TcpConnTable.TcpConnEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TCP-MIB:TCP-MIB/TCP-MIB:tcpConnTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tcpconnentry is not None:
                for child_ref in self.tcpconnentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tcp._meta import _TCP_MIB as meta
            return meta._meta_table['TCPMIB.TcpConnTable']['meta_info']


    class TcpConnectionTable(object):
        """
        A table containing information about existing TCP
        connections.  Note that unlike earlier TCP MIBs, there
        is a separate table for connections in the LISTEN state.
        
        .. attribute:: tcpconnectionentry
        
        	A conceptual row of the tcpConnectionTable containing information about a particular current TCP connection. Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of :py:class:`TcpConnectionEntry <ydk.models.tcp.TCP_MIB.TCPMIB.TcpConnectionTable.TcpConnectionEntry>`
        
        

        """

        _prefix = 'tcp-mib'
        _revision = '2005-02-18'

        def __init__(self):
            self.parent = None
            self.tcpconnectionentry = YList()
            self.tcpconnectionentry.parent = self
            self.tcpconnectionentry.name = 'tcpconnectionentry'


        class TcpConnectionEntry(object):
            """
            A conceptual row of the tcpConnectionTable containing
            information about a particular current TCP connection.
            Each row of this table is transient in that it ceases to
            exist when (or soon after) the connection makes the
            transition to the CLOSED state.
            
            .. attribute:: tcpconnectionlocaladdress
            
            	The local IP address for this TCP connection.  The type of this address is determined by the value of tcpConnectionLocalAddressType.  As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tcpconnectionlocaladdresstype
            
            	The address type of tcpConnectionLocalAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: tcpconnectionlocalport
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnectionremaddress
            
            	The remote IP address for this TCP connection.  The type of this address is determined by the value of tcpConnectionRemAddressType.  As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tcpconnectionremaddresstype
            
            	The address type of tcpConnectionRemAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: tcpconnectionremport
            
            	The remote port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnectionprocess
            
            	The system's process ID for the process associated with this connection, or zero if there is no such process.  This value is expected to be the same as HOST\-RESOURCES\-MIB\:\: hrSWRunIndex or SYSAPPL\-MIB\:\:sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tcpconnectionstate
            
            	The state of this TCP connection.  The value listen(2) is included only for parallelism to the old tcpConnTable and should not be used.  A connection in LISTEN state should be present in the tcpListenerTable.  The only value that may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably)
            	**type**\: :py:class:`TcpConnectionState_Enum <ydk.models.tcp.TCP_MIB.TCPMIB.TcpConnectionTable.TcpConnectionEntry.TcpConnectionState_Enum>`
            
            

            """

            _prefix = 'tcp-mib'
            _revision = '2005-02-18'

            def __init__(self):
                self.parent = None
                self.tcpconnectionlocaladdress = None
                self.tcpconnectionlocaladdresstype = None
                self.tcpconnectionlocalport = None
                self.tcpconnectionremaddress = None
                self.tcpconnectionremaddresstype = None
                self.tcpconnectionremport = None
                self.tcpconnectionprocess = None
                self.tcpconnectionstate = None

            class TcpConnectionState_Enum(Enum):
                """
                TcpConnectionState_Enum

                The state of this TCP connection.
                
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
                
                As an implementation\-specific option, a RST segment may be
                sent from the managed node to the other TCP endpoint (note,
                however, that RST segments are not sent reliably).

                """

                CLOSED = 1

                LISTEN = 2

                SYNSENT = 3

                SYNRECEIVED = 4

                ESTABLISHED = 5

                FINWAIT1 = 6

                FINWAIT2 = 7

                CLOSEWAIT = 8

                LASTACK = 9

                CLOSING = 10

                TIMEWAIT = 11

                DELETETCB = 12


                @staticmethod
                def _meta_info():
                    from ydk.models.tcp._meta import _TCP_MIB as meta
                    return meta._meta_table['TCPMIB.TcpConnectionTable.TcpConnectionEntry.TcpConnectionState_Enum']


            @property
            def _common_path(self):
                if self.tcpconnectionlocaladdress is None:
                    raise YPYDataValidationError('Key property tcpconnectionlocaladdress is None')
                if self.tcpconnectionlocaladdresstype is None:
                    raise YPYDataValidationError('Key property tcpconnectionlocaladdresstype is None')
                if self.tcpconnectionlocalport is None:
                    raise YPYDataValidationError('Key property tcpconnectionlocalport is None')
                if self.tcpconnectionremaddress is None:
                    raise YPYDataValidationError('Key property tcpconnectionremaddress is None')
                if self.tcpconnectionremaddresstype is None:
                    raise YPYDataValidationError('Key property tcpconnectionremaddresstype is None')
                if self.tcpconnectionremport is None:
                    raise YPYDataValidationError('Key property tcpconnectionremport is None')

                return '/TCP-MIB:TCP-MIB/TCP-MIB:tcpConnectionTable/TCP-MIB:tcpConnectionEntry[TCP-MIB:tcpConnectionLocalAddress = ' + str(self.tcpconnectionlocaladdress) + '][TCP-MIB:tcpConnectionLocalAddressType = ' + str(self.tcpconnectionlocaladdresstype) + '][TCP-MIB:tcpConnectionLocalPort = ' + str(self.tcpconnectionlocalport) + '][TCP-MIB:tcpConnectionRemAddress = ' + str(self.tcpconnectionremaddress) + '][TCP-MIB:tcpConnectionRemAddressType = ' + str(self.tcpconnectionremaddresstype) + '][TCP-MIB:tcpConnectionRemPort = ' + str(self.tcpconnectionremport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tcpconnectionlocaladdress is not None:
                    return True

                if self.tcpconnectionlocaladdresstype is not None:
                    return True

                if self.tcpconnectionlocalport is not None:
                    return True

                if self.tcpconnectionremaddress is not None:
                    return True

                if self.tcpconnectionremaddresstype is not None:
                    return True

                if self.tcpconnectionremport is not None:
                    return True

                if self.tcpconnectionprocess is not None:
                    return True

                if self.tcpconnectionstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tcp._meta import _TCP_MIB as meta
                return meta._meta_table['TCPMIB.TcpConnectionTable.TcpConnectionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TCP-MIB:TCP-MIB/TCP-MIB:tcpConnectionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tcpconnectionentry is not None:
                for child_ref in self.tcpconnectionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tcp._meta import _TCP_MIB as meta
            return meta._meta_table['TCPMIB.TcpConnectionTable']['meta_info']


    class TcpListenerTable(object):
        """
        A table containing information about TCP listeners.  A
        listening application can be represented in three
        possible ways\:
        
        1. An application that is willing to accept both IPv4 and
           IPv6 datagrams is represented by
        
           a tcpListenerLocalAddressType of unknown (0) and
           a tcpListenerLocalAddress of ''h (a zero\-length
           octet\-string).
        
        2. An application that is willing to accept only IPv4 or
           IPv6 datagrams is represented by a
           tcpListenerLocalAddressType of the appropriate address
           type and a tcpListenerLocalAddress of '0.0.0.0' or '\:\:'
           respectively.
        
        3. An application that is listening for data destined
           only to a specific IP address, but from any remote
           system, is represented by a tcpListenerLocalAddressType
           of an appropriate address type, with
           tcpListenerLocalAddress as the specific local address.
        
        NOTE\: The address type in this table represents the
        address type used for the communication, irrespective
        of the higher\-layer abstraction.  For example, an
        application using IPv6 'sockets' to communicate via
        IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would
        use InetAddressType ipv4(1)).
        
        .. attribute:: tcplistenerentry
        
        	A conceptual row of the tcpListenerTable containing information about a particular TCP listener
        	**type**\: list of :py:class:`TcpListenerEntry <ydk.models.tcp.TCP_MIB.TCPMIB.TcpListenerTable.TcpListenerEntry>`
        
        

        """

        _prefix = 'tcp-mib'
        _revision = '2005-02-18'

        def __init__(self):
            self.parent = None
            self.tcplistenerentry = YList()
            self.tcplistenerentry.parent = self
            self.tcplistenerentry.name = 'tcplistenerentry'


        class TcpListenerEntry(object):
            """
            A conceptual row of the tcpListenerTable containing
            information about a particular TCP listener.
            
            .. attribute:: tcplistenerlocaladdress
            
            	The local IP address for this TCP connection.  The value of this object can be represented in three possible ways, depending on the characteristics of the listening application\:  1. For an application willing to accept both IPv4 and    IPv6 datagrams, the value of this object must be    ''h (a zero\-length octet\-string), with the value    of the corresponding tcpListenerLocalAddressType    object being unknown (0).  2. For an application willing to accept only IPv4 or    IPv6 datagrams, the value of this object must be    '0.0.0.0' or '\:\:' respectively, with    tcpListenerLocalAddressType representing the    appropriate address type.  3. For an application which is listening for data    destined only to a specific IP address, the value    of this object is the specific local address, with    tcpListenerLocalAddressType representing the    appropriate address type.  As this object is used in the index for the tcpListenerTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tcplistenerlocaladdresstype
            
            	The address type of tcpListenerLocalAddress.  The value should be unknown (0) if connection initiations to all local IP addresses are accepted
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: tcplistenerlocalport
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcplistenerprocess
            
            	The system's process ID for the process associated with this listener, or zero if there is no such process.  This value is expected to be the same as HOST\-RESOURCES\-MIB\:\: hrSWRunIndex or SYSAPPL\-MIB\:\:sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tcp-mib'
            _revision = '2005-02-18'

            def __init__(self):
                self.parent = None
                self.tcplistenerlocaladdress = None
                self.tcplistenerlocaladdresstype = None
                self.tcplistenerlocalport = None
                self.tcplistenerprocess = None

            @property
            def _common_path(self):
                if self.tcplistenerlocaladdress is None:
                    raise YPYDataValidationError('Key property tcplistenerlocaladdress is None')
                if self.tcplistenerlocaladdresstype is None:
                    raise YPYDataValidationError('Key property tcplistenerlocaladdresstype is None')
                if self.tcplistenerlocalport is None:
                    raise YPYDataValidationError('Key property tcplistenerlocalport is None')

                return '/TCP-MIB:TCP-MIB/TCP-MIB:tcpListenerTable/TCP-MIB:tcpListenerEntry[TCP-MIB:tcpListenerLocalAddress = ' + str(self.tcplistenerlocaladdress) + '][TCP-MIB:tcpListenerLocalAddressType = ' + str(self.tcplistenerlocaladdresstype) + '][TCP-MIB:tcpListenerLocalPort = ' + str(self.tcplistenerlocalport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tcplistenerlocaladdress is not None:
                    return True

                if self.tcplistenerlocaladdresstype is not None:
                    return True

                if self.tcplistenerlocalport is not None:
                    return True

                if self.tcplistenerprocess is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tcp._meta import _TCP_MIB as meta
                return meta._meta_table['TCPMIB.TcpListenerTable.TcpListenerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TCP-MIB:TCP-MIB/TCP-MIB:tcpListenerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tcplistenerentry is not None:
                for child_ref in self.tcplistenerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tcp._meta import _TCP_MIB as meta
            return meta._meta_table['TCPMIB.TcpListenerTable']['meta_info']

    @property
    def _common_path(self):

        return '/TCP-MIB:TCP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.tcp is not None and self.tcp._has_data():
            return True

        if self.tcp is not None and self.tcp.is_presence():
            return True

        if self.tcpconnectiontable is not None and self.tcpconnectiontable._has_data():
            return True

        if self.tcpconnectiontable is not None and self.tcpconnectiontable.is_presence():
            return True

        if self.tcpconntable is not None and self.tcpconntable._has_data():
            return True

        if self.tcpconntable is not None and self.tcpconntable.is_presence():
            return True

        if self.tcplistenertable is not None and self.tcplistenertable._has_data():
            return True

        if self.tcplistenertable is not None and self.tcplistenertable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.tcp._meta import _TCP_MIB as meta
        return meta._meta_table['TCPMIB']['meta_info']


