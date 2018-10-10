""" TCP_MIB 

The MIB module for managing TCP implementations.

Copyright (C) The Internet Society (2005). This version
of this MIB module is a part of RFC 4022; see the RFC
itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class TCPMIB(Entity):
    """
    
    
    .. attribute:: tcp
    
    	
    	**type**\:  :py:class:`Tcp <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.Tcp>`
    
    .. attribute:: tcpconntable
    
    	A table containing information about existing IPv4\-specific TCP connections or listeners.  This table has been deprecated in favor of the version neutral tcpConnectionTable
    	**type**\:  :py:class:`TcpConnTable <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpConnTable>`
    
    	**status**\: deprecated
    
    .. attribute:: tcpconnectiontable
    
    	A table containing information about existing TCP connections.  Note that unlike earlier TCP MIBs, there is a separate table for connections in the LISTEN state
    	**type**\:  :py:class:`TcpConnectionTable <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpConnectionTable>`
    
    .. attribute:: tcplistenertable
    
    	A table containing information about TCP listeners.  A listening application can be represented in three possible ways\:  1. An application that is willing to accept both IPv4 and    IPv6 datagrams is represented by     a tcpListenerLocalAddressType of unknown (0) and    a tcpListenerLocalAddress of ''h (a zero\-length    octet\-string).  2. An application that is willing to accept only IPv4 or    IPv6 datagrams is represented by a    tcpListenerLocalAddressType of the appropriate address    type and a tcpListenerLocalAddress of '0.0.0.0' or '\:\:'    respectively.  3. An application that is listening for data destined    only to a specific IP address, but from any remote    system, is represented by a tcpListenerLocalAddressType    of an appropriate address type, with    tcpListenerLocalAddress as the specific local address.  NOTE\: The address type in this table represents the address type used for the communication, irrespective of the higher\-layer abstraction.  For example, an application using IPv6 'sockets' to communicate via IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use InetAddressType ipv4(1))
    	**type**\:  :py:class:`TcpListenerTable <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpListenerTable>`
    
    

    """

    _prefix = 'TCP-MIB'
    _revision = '2005-02-18'

    def __init__(self):
        super(TCPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "TCP-MIB"
        self.yang_parent_name = "TCP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("tcp", ("tcp", TCPMIB.Tcp)), ("tcpConnTable", ("tcpconntable", TCPMIB.TcpConnTable)), ("tcpConnectionTable", ("tcpconnectiontable", TCPMIB.TcpConnectionTable)), ("tcpListenerTable", ("tcplistenertable", TCPMIB.TcpListenerTable))])
        self._leafs = OrderedDict()

        self.tcp = TCPMIB.Tcp()
        self.tcp.parent = self
        self._children_name_map["tcp"] = "tcp"

        self.tcpconntable = TCPMIB.TcpConnTable()
        self.tcpconntable.parent = self
        self._children_name_map["tcpconntable"] = "tcpConnTable"

        self.tcpconnectiontable = TCPMIB.TcpConnectionTable()
        self.tcpconnectiontable.parent = self
        self._children_name_map["tcpconnectiontable"] = "tcpConnectionTable"

        self.tcplistenertable = TCPMIB.TcpListenerTable()
        self.tcplistenertable.parent = self
        self._children_name_map["tcplistenertable"] = "tcpListenerTable"
        self._segment_path = lambda: "TCP-MIB:TCP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TCPMIB, [], name, value)


    class Tcp(Entity):
        """
        
        
        .. attribute:: tcprtoalgorithm
        
        	The algorithm used to determine the timeout value used for retransmitting unacknowledged octets
        	**type**\:  :py:class:`TcpRtoAlgorithm <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.Tcp.TcpRtoAlgorithm>`
        
        .. attribute:: tcprtomin
        
        	The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides a minimum value
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: milliseconds
        
        .. attribute:: tcprtomax
        
        	The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides an upper bound (as part of an adaptive backoff algorithm)
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**units**\: milliseconds
        
        .. attribute:: tcpmaxconn
        
        	The limit on the total number of TCP connections the entity can support.  In entities where the maximum number of connections is dynamic, this object should contain the value \-1
        	**type**\: int
        
        	**range:** \-1..2147483647
        
        .. attribute:: tcpactiveopens
        
        	The number of times that TCP connections have made a direct transition to the SYN\-SENT state from the CLOSED state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcppassiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-RCVD state from the LISTEN state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpattemptfails
        
        	The number of times that TCP connections have made a direct transition to the CLOSED state from either the SYN\-SENT state or the SYN\-RCVD state, plus the number of times that TCP connections have made a direct transition to the LISTEN state from the SYN\-RCVD state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpestabresets
        
        	The number of times that TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE\-WAIT state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpcurrestab
        
        	The number of TCP connections for which the current state is either ESTABLISHED or CLOSE\-WAIT
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received on currently established connections.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpretranssegs
        
        	The total number of segments retransmitted; that is, the number of TCP segments transmitted containing one or more previously transmitted octets.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinerrs
        
        	The total number of segments received in error (e.g., bad TCP checksums).  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutrsts
        
        	The number of TCP segments sent containing the RST flag.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
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
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TCPMIB.Tcp, self).__init__()

            self.yang_name = "tcp"
            self.yang_parent_name = "TCP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('tcprtoalgorithm', (YLeaf(YType.enumeration, 'tcpRtoAlgorithm'), [('ydk.models.cisco_ios_xe.TCP_MIB', 'TCPMIB', 'Tcp.TcpRtoAlgorithm')])),
                ('tcprtomin', (YLeaf(YType.int32, 'tcpRtoMin'), ['int'])),
                ('tcprtomax', (YLeaf(YType.int32, 'tcpRtoMax'), ['int'])),
                ('tcpmaxconn', (YLeaf(YType.int32, 'tcpMaxConn'), ['int'])),
                ('tcpactiveopens', (YLeaf(YType.uint32, 'tcpActiveOpens'), ['int'])),
                ('tcppassiveopens', (YLeaf(YType.uint32, 'tcpPassiveOpens'), ['int'])),
                ('tcpattemptfails', (YLeaf(YType.uint32, 'tcpAttemptFails'), ['int'])),
                ('tcpestabresets', (YLeaf(YType.uint32, 'tcpEstabResets'), ['int'])),
                ('tcpcurrestab', (YLeaf(YType.uint32, 'tcpCurrEstab'), ['int'])),
                ('tcpinsegs', (YLeaf(YType.uint32, 'tcpInSegs'), ['int'])),
                ('tcpoutsegs', (YLeaf(YType.uint32, 'tcpOutSegs'), ['int'])),
                ('tcpretranssegs', (YLeaf(YType.uint32, 'tcpRetransSegs'), ['int'])),
                ('tcpinerrs', (YLeaf(YType.uint32, 'tcpInErrs'), ['int'])),
                ('tcpoutrsts', (YLeaf(YType.uint32, 'tcpOutRsts'), ['int'])),
                ('tcphcinsegs', (YLeaf(YType.uint64, 'tcpHCInSegs'), ['int'])),
                ('tcphcoutsegs', (YLeaf(YType.uint64, 'tcpHCOutSegs'), ['int'])),
            ])
            self.tcprtoalgorithm = None
            self.tcprtomin = None
            self.tcprtomax = None
            self.tcpmaxconn = None
            self.tcpactiveopens = None
            self.tcppassiveopens = None
            self.tcpattemptfails = None
            self.tcpestabresets = None
            self.tcpcurrestab = None
            self.tcpinsegs = None
            self.tcpoutsegs = None
            self.tcpretranssegs = None
            self.tcpinerrs = None
            self.tcpoutrsts = None
            self.tcphcinsegs = None
            self.tcphcoutsegs = None
            self._segment_path = lambda: "tcp"
            self._absolute_path = lambda: "TCP-MIB:TCP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TCPMIB.Tcp, ['tcprtoalgorithm', 'tcprtomin', 'tcprtomax', 'tcpmaxconn', 'tcpactiveopens', 'tcppassiveopens', 'tcpattemptfails', 'tcpestabresets', 'tcpcurrestab', 'tcpinsegs', 'tcpoutsegs', 'tcpretranssegs', 'tcpinerrs', 'tcpoutrsts', 'tcphcinsegs', 'tcphcoutsegs'], name, value)

        class TcpRtoAlgorithm(Enum):
            """
            TcpRtoAlgorithm (Enum Class)

            The algorithm used to determine the timeout value used for

            retransmitting unacknowledged octets.

            .. data:: other = 1

            .. data:: constant = 2

            .. data:: rsre = 3

            .. data:: vanj = 4

            .. data:: rfc2988 = 5

            """

            other = Enum.YLeaf(1, "other")

            constant = Enum.YLeaf(2, "constant")

            rsre = Enum.YLeaf(3, "rsre")

            vanj = Enum.YLeaf(4, "vanj")

            rfc2988 = Enum.YLeaf(5, "rfc2988")



    class TcpConnTable(Entity):
        """
        A table containing information about existing IPv4\-specific
        TCP connections or listeners.  This table has been
        deprecated in favor of the version neutral
        tcpConnectionTable.
        
        .. attribute:: tcpconnentry
        
        	A conceptual row of the tcpConnTable containing information about a particular current IPv4 TCP connection.  Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of  		 :py:class:`TcpConnEntry <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpConnTable.TcpConnEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TCPMIB.TcpConnTable, self).__init__()

            self.yang_name = "tcpConnTable"
            self.yang_parent_name = "TCP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tcpConnEntry", ("tcpconnentry", TCPMIB.TcpConnTable.TcpConnEntry))])
            self._leafs = OrderedDict()

            self.tcpconnentry = YList(self)
            self._segment_path = lambda: "tcpConnTable"
            self._absolute_path = lambda: "TCP-MIB:TCP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TCPMIB.TcpConnTable, [], name, value)


        class TcpConnEntry(Entity):
            """
            A conceptual row of the tcpConnTable containing information
            about a particular current IPv4 TCP connection.  Each row
            of this table is transient in that it ceases to exist when
            (or soon after) the connection makes the transition to the
            CLOSED state.
            
            .. attribute:: tcpconnlocaladdress  (key)
            
            	The local IP address for this TCP connection.  In the case of a connection in the listen state willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnlocalport  (key)
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnremaddress  (key)
            
            	The remote IP address for this TCP connection
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnremport  (key)
            
            	The remote port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnstate
            
            	The state of this TCP connection.  The only value that may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably)
            	**type**\:  :py:class:`TcpConnState <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpConnTable.TcpConnEntry.TcpConnState>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'TCP-MIB'
            _revision = '2005-02-18'

            def __init__(self):
                super(TCPMIB.TcpConnTable.TcpConnEntry, self).__init__()

                self.yang_name = "tcpConnEntry"
                self.yang_parent_name = "tcpConnTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tcpconnlocaladdress','tcpconnlocalport','tcpconnremaddress','tcpconnremport']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tcpconnlocaladdress', (YLeaf(YType.str, 'tcpConnLocalAddress'), ['str'])),
                    ('tcpconnlocalport', (YLeaf(YType.int32, 'tcpConnLocalPort'), ['int'])),
                    ('tcpconnremaddress', (YLeaf(YType.str, 'tcpConnRemAddress'), ['str'])),
                    ('tcpconnremport', (YLeaf(YType.int32, 'tcpConnRemPort'), ['int'])),
                    ('tcpconnstate', (YLeaf(YType.enumeration, 'tcpConnState'), [('ydk.models.cisco_ios_xe.TCP_MIB', 'TCPMIB', 'TcpConnTable.TcpConnEntry.TcpConnState')])),
                ])
                self.tcpconnlocaladdress = None
                self.tcpconnlocalport = None
                self.tcpconnremaddress = None
                self.tcpconnremport = None
                self.tcpconnstate = None
                self._segment_path = lambda: "tcpConnEntry" + "[tcpConnLocalAddress='" + str(self.tcpconnlocaladdress) + "']" + "[tcpConnLocalPort='" + str(self.tcpconnlocalport) + "']" + "[tcpConnRemAddress='" + str(self.tcpconnremaddress) + "']" + "[tcpConnRemPort='" + str(self.tcpconnremport) + "']"
                self._absolute_path = lambda: "TCP-MIB:TCP-MIB/tcpConnTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TCPMIB.TcpConnTable.TcpConnEntry, ['tcpconnlocaladdress', 'tcpconnlocalport', 'tcpconnremaddress', 'tcpconnremport', 'tcpconnstate'], name, value)

            class TcpConnState(Enum):
                """
                TcpConnState (Enum Class)

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

                .. data:: closed = 1

                .. data:: listen = 2

                .. data:: synSent = 3

                .. data:: synReceived = 4

                .. data:: established = 5

                .. data:: finWait1 = 6

                .. data:: finWait2 = 7

                .. data:: closeWait = 8

                .. data:: lastAck = 9

                .. data:: closing = 10

                .. data:: timeWait = 11

                .. data:: deleteTCB = 12

                """

                closed = Enum.YLeaf(1, "closed")

                listen = Enum.YLeaf(2, "listen")

                synSent = Enum.YLeaf(3, "synSent")

                synReceived = Enum.YLeaf(4, "synReceived")

                established = Enum.YLeaf(5, "established")

                finWait1 = Enum.YLeaf(6, "finWait1")

                finWait2 = Enum.YLeaf(7, "finWait2")

                closeWait = Enum.YLeaf(8, "closeWait")

                lastAck = Enum.YLeaf(9, "lastAck")

                closing = Enum.YLeaf(10, "closing")

                timeWait = Enum.YLeaf(11, "timeWait")

                deleteTCB = Enum.YLeaf(12, "deleteTCB")



    class TcpConnectionTable(Entity):
        """
        A table containing information about existing TCP
        connections.  Note that unlike earlier TCP MIBs, there
        is a separate table for connections in the LISTEN state.
        
        .. attribute:: tcpconnectionentry
        
        	A conceptual row of the tcpConnectionTable containing information about a particular current TCP connection. Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of  		 :py:class:`TcpConnectionEntry <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpConnectionTable.TcpConnectionEntry>`
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TCPMIB.TcpConnectionTable, self).__init__()

            self.yang_name = "tcpConnectionTable"
            self.yang_parent_name = "TCP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tcpConnectionEntry", ("tcpconnectionentry", TCPMIB.TcpConnectionTable.TcpConnectionEntry))])
            self._leafs = OrderedDict()

            self.tcpconnectionentry = YList(self)
            self._segment_path = lambda: "tcpConnectionTable"
            self._absolute_path = lambda: "TCP-MIB:TCP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TCPMIB.TcpConnectionTable, [], name, value)


        class TcpConnectionEntry(Entity):
            """
            A conceptual row of the tcpConnectionTable containing
            information about a particular current TCP connection.
            Each row of this table is transient in that it ceases to
            exist when (or soon after) the connection makes the
            transition to the CLOSED state.
            
            .. attribute:: tcpconnectionlocaladdresstype  (key)
            
            	The address type of tcpConnectionLocalAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: tcpconnectionlocaladdress  (key)
            
            	The local IP address for this TCP connection.  The type of this address is determined by the value of tcpConnectionLocalAddressType.  As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: tcpconnectionlocalport  (key)
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnectionremaddresstype  (key)
            
            	The address type of tcpConnectionRemAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: tcpconnectionremaddress  (key)
            
            	The remote IP address for this TCP connection.  The type of this address is determined by the value of tcpConnectionRemAddressType.  As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: tcpconnectionremport  (key)
            
            	The remote port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnectionstate
            
            	The state of this TCP connection.  The value listen(2) is included only for parallelism to the old tcpConnTable and should not be used.  A connection in LISTEN state should be present in the tcpListenerTable.  The only value that may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably)
            	**type**\:  :py:class:`TcpConnectionState <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpConnectionTable.TcpConnectionEntry.TcpConnectionState>`
            
            .. attribute:: tcpconnectionprocess
            
            	The system's process ID for the process associated with this connection, or zero if there is no such process.  This value is expected to be the same as HOST\-RESOURCES\-MIB\:\: hrSWRunIndex or SYSAPPL\-MIB\:\:sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TCP-MIB'
            _revision = '2005-02-18'

            def __init__(self):
                super(TCPMIB.TcpConnectionTable.TcpConnectionEntry, self).__init__()

                self.yang_name = "tcpConnectionEntry"
                self.yang_parent_name = "tcpConnectionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tcpconnectionlocaladdresstype','tcpconnectionlocaladdress','tcpconnectionlocalport','tcpconnectionremaddresstype','tcpconnectionremaddress','tcpconnectionremport']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tcpconnectionlocaladdresstype', (YLeaf(YType.enumeration, 'tcpConnectionLocalAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('tcpconnectionlocaladdress', (YLeaf(YType.str, 'tcpConnectionLocalAddress'), ['str'])),
                    ('tcpconnectionlocalport', (YLeaf(YType.uint16, 'tcpConnectionLocalPort'), ['int'])),
                    ('tcpconnectionremaddresstype', (YLeaf(YType.enumeration, 'tcpConnectionRemAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('tcpconnectionremaddress', (YLeaf(YType.str, 'tcpConnectionRemAddress'), ['str'])),
                    ('tcpconnectionremport', (YLeaf(YType.uint16, 'tcpConnectionRemPort'), ['int'])),
                    ('tcpconnectionstate', (YLeaf(YType.enumeration, 'tcpConnectionState'), [('ydk.models.cisco_ios_xe.TCP_MIB', 'TCPMIB', 'TcpConnectionTable.TcpConnectionEntry.TcpConnectionState')])),
                    ('tcpconnectionprocess', (YLeaf(YType.uint32, 'tcpConnectionProcess'), ['int'])),
                ])
                self.tcpconnectionlocaladdresstype = None
                self.tcpconnectionlocaladdress = None
                self.tcpconnectionlocalport = None
                self.tcpconnectionremaddresstype = None
                self.tcpconnectionremaddress = None
                self.tcpconnectionremport = None
                self.tcpconnectionstate = None
                self.tcpconnectionprocess = None
                self._segment_path = lambda: "tcpConnectionEntry" + "[tcpConnectionLocalAddressType='" + str(self.tcpconnectionlocaladdresstype) + "']" + "[tcpConnectionLocalAddress='" + str(self.tcpconnectionlocaladdress) + "']" + "[tcpConnectionLocalPort='" + str(self.tcpconnectionlocalport) + "']" + "[tcpConnectionRemAddressType='" + str(self.tcpconnectionremaddresstype) + "']" + "[tcpConnectionRemAddress='" + str(self.tcpconnectionremaddress) + "']" + "[tcpConnectionRemPort='" + str(self.tcpconnectionremport) + "']"
                self._absolute_path = lambda: "TCP-MIB:TCP-MIB/tcpConnectionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TCPMIB.TcpConnectionTable.TcpConnectionEntry, ['tcpconnectionlocaladdresstype', 'tcpconnectionlocaladdress', 'tcpconnectionlocalport', 'tcpconnectionremaddresstype', 'tcpconnectionremaddress', 'tcpconnectionremport', 'tcpconnectionstate', 'tcpconnectionprocess'], name, value)

            class TcpConnectionState(Enum):
                """
                TcpConnectionState (Enum Class)

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

                .. data:: closed = 1

                .. data:: listen = 2

                .. data:: synSent = 3

                .. data:: synReceived = 4

                .. data:: established = 5

                .. data:: finWait1 = 6

                .. data:: finWait2 = 7

                .. data:: closeWait = 8

                .. data:: lastAck = 9

                .. data:: closing = 10

                .. data:: timeWait = 11

                .. data:: deleteTCB = 12

                """

                closed = Enum.YLeaf(1, "closed")

                listen = Enum.YLeaf(2, "listen")

                synSent = Enum.YLeaf(3, "synSent")

                synReceived = Enum.YLeaf(4, "synReceived")

                established = Enum.YLeaf(5, "established")

                finWait1 = Enum.YLeaf(6, "finWait1")

                finWait2 = Enum.YLeaf(7, "finWait2")

                closeWait = Enum.YLeaf(8, "closeWait")

                lastAck = Enum.YLeaf(9, "lastAck")

                closing = Enum.YLeaf(10, "closing")

                timeWait = Enum.YLeaf(11, "timeWait")

                deleteTCB = Enum.YLeaf(12, "deleteTCB")



    class TcpListenerTable(Entity):
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
        	**type**\: list of  		 :py:class:`TcpListenerEntry <ydk.models.cisco_ios_xe.TCP_MIB.TCPMIB.TcpListenerTable.TcpListenerEntry>`
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TCPMIB.TcpListenerTable, self).__init__()

            self.yang_name = "tcpListenerTable"
            self.yang_parent_name = "TCP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tcpListenerEntry", ("tcplistenerentry", TCPMIB.TcpListenerTable.TcpListenerEntry))])
            self._leafs = OrderedDict()

            self.tcplistenerentry = YList(self)
            self._segment_path = lambda: "tcpListenerTable"
            self._absolute_path = lambda: "TCP-MIB:TCP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TCPMIB.TcpListenerTable, [], name, value)


        class TcpListenerEntry(Entity):
            """
            A conceptual row of the tcpListenerTable containing
            information about a particular TCP listener.
            
            .. attribute:: tcplistenerlocaladdresstype  (key)
            
            	The address type of tcpListenerLocalAddress.  The value should be unknown (0) if connection initiations to all local IP addresses are accepted
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: tcplistenerlocaladdress  (key)
            
            	The local IP address for this TCP connection.  The value of this object can be represented in three possible ways, depending on the characteristics of the listening application\:  1. For an application willing to accept both IPv4 and    IPv6 datagrams, the value of this object must be    ''h (a zero\-length octet\-string), with the value    of the corresponding tcpListenerLocalAddressType    object being unknown (0).  2. For an application willing to accept only IPv4 or    IPv6 datagrams, the value of this object must be    '0.0.0.0' or '\:\:' respectively, with    tcpListenerLocalAddressType representing the    appropriate address type.  3. For an application which is listening for data    destined only to a specific IP address, the value    of this object is the specific local address, with    tcpListenerLocalAddressType representing the    appropriate address type.  As this object is used in the index for the tcpListenerTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: tcplistenerlocalport  (key)
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcplistenerprocess
            
            	The system's process ID for the process associated with this listener, or zero if there is no such process.  This value is expected to be the same as HOST\-RESOURCES\-MIB\:\: hrSWRunIndex or SYSAPPL\-MIB\:\:sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TCP-MIB'
            _revision = '2005-02-18'

            def __init__(self):
                super(TCPMIB.TcpListenerTable.TcpListenerEntry, self).__init__()

                self.yang_name = "tcpListenerEntry"
                self.yang_parent_name = "tcpListenerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tcplistenerlocaladdresstype','tcplistenerlocaladdress','tcplistenerlocalport']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tcplistenerlocaladdresstype', (YLeaf(YType.enumeration, 'tcpListenerLocalAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('tcplistenerlocaladdress', (YLeaf(YType.str, 'tcpListenerLocalAddress'), ['str'])),
                    ('tcplistenerlocalport', (YLeaf(YType.uint16, 'tcpListenerLocalPort'), ['int'])),
                    ('tcplistenerprocess', (YLeaf(YType.uint32, 'tcpListenerProcess'), ['int'])),
                ])
                self.tcplistenerlocaladdresstype = None
                self.tcplistenerlocaladdress = None
                self.tcplistenerlocalport = None
                self.tcplistenerprocess = None
                self._segment_path = lambda: "tcpListenerEntry" + "[tcpListenerLocalAddressType='" + str(self.tcplistenerlocaladdresstype) + "']" + "[tcpListenerLocalAddress='" + str(self.tcplistenerlocaladdress) + "']" + "[tcpListenerLocalPort='" + str(self.tcplistenerlocalport) + "']"
                self._absolute_path = lambda: "TCP-MIB:TCP-MIB/tcpListenerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TCPMIB.TcpListenerTable.TcpListenerEntry, ['tcplistenerlocaladdresstype', 'tcplistenerlocaladdress', 'tcplistenerlocalport', 'tcplistenerprocess'], name, value)

    def clone_ptr(self):
        self._top_entity = TCPMIB()
        return self._top_entity

