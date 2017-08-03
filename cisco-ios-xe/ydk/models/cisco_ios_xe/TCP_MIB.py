""" TCP_MIB 

The MIB module for managing TCP implementations.

Copyright (C) The Internet Society (2005). This version
of this MIB module is a part of RFC 4022; see the RFC
itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TcpMib(Entity):
    """
    
    
    .. attribute:: tcp
    
    	
    	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcp>`
    
    .. attribute:: tcpconnectiontable
    
    	A table containing information about existing TCP connections.  Note that unlike earlier TCP MIBs, there is a separate table for connections in the LISTEN state
    	**type**\:   :py:class:`Tcpconnectiontable <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcpconnectiontable>`
    
    .. attribute:: tcpconntable
    
    	A table containing information about existing IPv4\-specific TCP connections or listeners.  This table has been deprecated in favor of the version neutral tcpConnectionTable
    	**type**\:   :py:class:`Tcpconntable <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcpconntable>`
    
    	**status**\: deprecated
    
    .. attribute:: tcplistenertable
    
    	A table containing information about TCP listeners.  A listening application can be represented in three possible ways\:  1. An application that is willing to accept both IPv4 and    IPv6 datagrams is represented by     a tcpListenerLocalAddressType of unknown (0) and    a tcpListenerLocalAddress of ''h (a zero\-length    octet\-string).  2. An application that is willing to accept only IPv4 or    IPv6 datagrams is represented by a    tcpListenerLocalAddressType of the appropriate address    type and a tcpListenerLocalAddress of '0.0.0.0' or '\:\:'    respectively.  3. An application that is listening for data destined    only to a specific IP address, but from any remote    system, is represented by a tcpListenerLocalAddressType    of an appropriate address type, with    tcpListenerLocalAddress as the specific local address.  NOTE\: The address type in this table represents the address type used for the communication, irrespective of the higher\-layer abstraction.  For example, an application using IPv6 'sockets' to communicate via IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use InetAddressType ipv4(1))
    	**type**\:   :py:class:`Tcplistenertable <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcplistenertable>`
    
    

    """

    _prefix = 'TCP-MIB'
    _revision = '2005-02-18'

    def __init__(self):
        super(TcpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "TCP-MIB"
        self.yang_parent_name = "TCP-MIB"

        self.tcp = TcpMib.Tcp()
        self.tcp.parent = self
        self._children_name_map["tcp"] = "tcp"
        self._children_yang_names.add("tcp")

        self.tcpconnectiontable = TcpMib.Tcpconnectiontable()
        self.tcpconnectiontable.parent = self
        self._children_name_map["tcpconnectiontable"] = "tcpConnectionTable"
        self._children_yang_names.add("tcpConnectionTable")

        self.tcpconntable = TcpMib.Tcpconntable()
        self.tcpconntable.parent = self
        self._children_name_map["tcpconntable"] = "tcpConnTable"
        self._children_yang_names.add("tcpConnTable")

        self.tcplistenertable = TcpMib.Tcplistenertable()
        self.tcplistenertable.parent = self
        self._children_name_map["tcplistenertable"] = "tcpListenerTable"
        self._children_yang_names.add("tcpListenerTable")


    class Tcp(Entity):
        """
        
        
        .. attribute:: tcpactiveopens
        
        	The number of times that TCP connections have made a direct transition to the SYN\-SENT state from the CLOSED state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpattemptfails
        
        	The number of times that TCP connections have made a direct transition to the CLOSED state from either the SYN\-SENT state or the SYN\-RCVD state, plus the number of times that TCP connections have made a direct transition to the LISTEN state from the SYN\-RCVD state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpcurrestab
        
        	The number of TCP connections for which the current state is either ESTABLISHED or CLOSE\-WAIT
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpestabresets
        
        	The number of times that TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE\-WAIT state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcphcinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received  on currently established connections.  This object is the 64\-bit equivalent of tcpInSegs.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tcphcoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.  This object is the 64\-bit equivalent of tcpOutSegs.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: tcpinerrs
        
        	The total number of segments received in error (e.g., bad TCP checksums).  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received on currently established connections.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpmaxconn
        
        	The limit on the total number of TCP connections the entity can support.  In entities where the maximum number of connections is dynamic, this object should contain the value \-1
        	**type**\:  int
        
        	**range:** \-1..2147483647
        
        .. attribute:: tcpoutrsts
        
        	The number of TCP segments sent containing the RST flag.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcppassiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-RCVD state from the LISTEN state.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpretranssegs
        
        	The total number of segments retransmitted; that is, the number of TCP segments transmitted containing one or more previously transmitted octets.  Discontinuities in the value of this counter are indicated via discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcprtoalgorithm
        
        	The algorithm used to determine the timeout value used for retransmitting unacknowledged octets
        	**type**\:   :py:class:`Tcprtoalgorithm <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcp.Tcprtoalgorithm>`
        
        .. attribute:: tcprtomax
        
        	The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides an upper bound (as part of an adaptive backoff algorithm)
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: milliseconds
        
        .. attribute:: tcprtomin
        
        	The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend on the algorithm used to determine the retransmission timeout; in particular, the IETF standard algorithm rfc2988(5) provides a minimum value
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: milliseconds
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TcpMib.Tcp, self).__init__()

            self.yang_name = "tcp"
            self.yang_parent_name = "TCP-MIB"

            self.tcpactiveopens = YLeaf(YType.uint32, "tcpActiveOpens")

            self.tcpattemptfails = YLeaf(YType.uint32, "tcpAttemptFails")

            self.tcpcurrestab = YLeaf(YType.uint32, "tcpCurrEstab")

            self.tcpestabresets = YLeaf(YType.uint32, "tcpEstabResets")

            self.tcphcinsegs = YLeaf(YType.uint64, "tcpHCInSegs")

            self.tcphcoutsegs = YLeaf(YType.uint64, "tcpHCOutSegs")

            self.tcpinerrs = YLeaf(YType.uint32, "tcpInErrs")

            self.tcpinsegs = YLeaf(YType.uint32, "tcpInSegs")

            self.tcpmaxconn = YLeaf(YType.int32, "tcpMaxConn")

            self.tcpoutrsts = YLeaf(YType.uint32, "tcpOutRsts")

            self.tcpoutsegs = YLeaf(YType.uint32, "tcpOutSegs")

            self.tcppassiveopens = YLeaf(YType.uint32, "tcpPassiveOpens")

            self.tcpretranssegs = YLeaf(YType.uint32, "tcpRetransSegs")

            self.tcprtoalgorithm = YLeaf(YType.enumeration, "tcpRtoAlgorithm")

            self.tcprtomax = YLeaf(YType.int32, "tcpRtoMax")

            self.tcprtomin = YLeaf(YType.int32, "tcpRtoMin")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("tcpactiveopens",
                            "tcpattemptfails",
                            "tcpcurrestab",
                            "tcpestabresets",
                            "tcphcinsegs",
                            "tcphcoutsegs",
                            "tcpinerrs",
                            "tcpinsegs",
                            "tcpmaxconn",
                            "tcpoutrsts",
                            "tcpoutsegs",
                            "tcppassiveopens",
                            "tcpretranssegs",
                            "tcprtoalgorithm",
                            "tcprtomax",
                            "tcprtomin") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(TcpMib.Tcp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TcpMib.Tcp, self).__setattr__(name, value)

        class Tcprtoalgorithm(Enum):
            """
            Tcprtoalgorithm

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


        def has_data(self):
            return (
                self.tcpactiveopens.is_set or
                self.tcpattemptfails.is_set or
                self.tcpcurrestab.is_set or
                self.tcpestabresets.is_set or
                self.tcphcinsegs.is_set or
                self.tcphcoutsegs.is_set or
                self.tcpinerrs.is_set or
                self.tcpinsegs.is_set or
                self.tcpmaxconn.is_set or
                self.tcpoutrsts.is_set or
                self.tcpoutsegs.is_set or
                self.tcppassiveopens.is_set or
                self.tcpretranssegs.is_set or
                self.tcprtoalgorithm.is_set or
                self.tcprtomax.is_set or
                self.tcprtomin.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.tcpactiveopens.yfilter != YFilter.not_set or
                self.tcpattemptfails.yfilter != YFilter.not_set or
                self.tcpcurrestab.yfilter != YFilter.not_set or
                self.tcpestabresets.yfilter != YFilter.not_set or
                self.tcphcinsegs.yfilter != YFilter.not_set or
                self.tcphcoutsegs.yfilter != YFilter.not_set or
                self.tcpinerrs.yfilter != YFilter.not_set or
                self.tcpinsegs.yfilter != YFilter.not_set or
                self.tcpmaxconn.yfilter != YFilter.not_set or
                self.tcpoutrsts.yfilter != YFilter.not_set or
                self.tcpoutsegs.yfilter != YFilter.not_set or
                self.tcppassiveopens.yfilter != YFilter.not_set or
                self.tcpretranssegs.yfilter != YFilter.not_set or
                self.tcprtoalgorithm.yfilter != YFilter.not_set or
                self.tcprtomax.yfilter != YFilter.not_set or
                self.tcprtomin.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tcp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TCP-MIB:TCP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.tcpactiveopens.is_set or self.tcpactiveopens.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpactiveopens.get_name_leafdata())
            if (self.tcpattemptfails.is_set or self.tcpattemptfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpattemptfails.get_name_leafdata())
            if (self.tcpcurrestab.is_set or self.tcpcurrestab.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpcurrestab.get_name_leafdata())
            if (self.tcpestabresets.is_set or self.tcpestabresets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpestabresets.get_name_leafdata())
            if (self.tcphcinsegs.is_set or self.tcphcinsegs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcphcinsegs.get_name_leafdata())
            if (self.tcphcoutsegs.is_set or self.tcphcoutsegs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcphcoutsegs.get_name_leafdata())
            if (self.tcpinerrs.is_set or self.tcpinerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpinerrs.get_name_leafdata())
            if (self.tcpinsegs.is_set or self.tcpinsegs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpinsegs.get_name_leafdata())
            if (self.tcpmaxconn.is_set or self.tcpmaxconn.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpmaxconn.get_name_leafdata())
            if (self.tcpoutrsts.is_set or self.tcpoutrsts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpoutrsts.get_name_leafdata())
            if (self.tcpoutsegs.is_set or self.tcpoutsegs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpoutsegs.get_name_leafdata())
            if (self.tcppassiveopens.is_set or self.tcppassiveopens.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcppassiveopens.get_name_leafdata())
            if (self.tcpretranssegs.is_set or self.tcpretranssegs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcpretranssegs.get_name_leafdata())
            if (self.tcprtoalgorithm.is_set or self.tcprtoalgorithm.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcprtoalgorithm.get_name_leafdata())
            if (self.tcprtomax.is_set or self.tcprtomax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcprtomax.get_name_leafdata())
            if (self.tcprtomin.is_set or self.tcprtomin.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcprtomin.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcpActiveOpens" or name == "tcpAttemptFails" or name == "tcpCurrEstab" or name == "tcpEstabResets" or name == "tcpHCInSegs" or name == "tcpHCOutSegs" or name == "tcpInErrs" or name == "tcpInSegs" or name == "tcpMaxConn" or name == "tcpOutRsts" or name == "tcpOutSegs" or name == "tcpPassiveOpens" or name == "tcpRetransSegs" or name == "tcpRtoAlgorithm" or name == "tcpRtoMax" or name == "tcpRtoMin"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "tcpActiveOpens"):
                self.tcpactiveopens = value
                self.tcpactiveopens.value_namespace = name_space
                self.tcpactiveopens.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpAttemptFails"):
                self.tcpattemptfails = value
                self.tcpattemptfails.value_namespace = name_space
                self.tcpattemptfails.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpCurrEstab"):
                self.tcpcurrestab = value
                self.tcpcurrestab.value_namespace = name_space
                self.tcpcurrestab.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpEstabResets"):
                self.tcpestabresets = value
                self.tcpestabresets.value_namespace = name_space
                self.tcpestabresets.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpHCInSegs"):
                self.tcphcinsegs = value
                self.tcphcinsegs.value_namespace = name_space
                self.tcphcinsegs.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpHCOutSegs"):
                self.tcphcoutsegs = value
                self.tcphcoutsegs.value_namespace = name_space
                self.tcphcoutsegs.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpInErrs"):
                self.tcpinerrs = value
                self.tcpinerrs.value_namespace = name_space
                self.tcpinerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpInSegs"):
                self.tcpinsegs = value
                self.tcpinsegs.value_namespace = name_space
                self.tcpinsegs.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpMaxConn"):
                self.tcpmaxconn = value
                self.tcpmaxconn.value_namespace = name_space
                self.tcpmaxconn.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpOutRsts"):
                self.tcpoutrsts = value
                self.tcpoutrsts.value_namespace = name_space
                self.tcpoutrsts.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpOutSegs"):
                self.tcpoutsegs = value
                self.tcpoutsegs.value_namespace = name_space
                self.tcpoutsegs.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpPassiveOpens"):
                self.tcppassiveopens = value
                self.tcppassiveopens.value_namespace = name_space
                self.tcppassiveopens.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpRetransSegs"):
                self.tcpretranssegs = value
                self.tcpretranssegs.value_namespace = name_space
                self.tcpretranssegs.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpRtoAlgorithm"):
                self.tcprtoalgorithm = value
                self.tcprtoalgorithm.value_namespace = name_space
                self.tcprtoalgorithm.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpRtoMax"):
                self.tcprtomax = value
                self.tcprtomax.value_namespace = name_space
                self.tcprtomax.value_namespace_prefix = name_space_prefix
            if(value_path == "tcpRtoMin"):
                self.tcprtomin = value
                self.tcprtomin.value_namespace = name_space
                self.tcprtomin.value_namespace_prefix = name_space_prefix


    class Tcpconntable(Entity):
        """
        A table containing information about existing IPv4\-specific
        TCP connections or listeners.  This table has been
        deprecated in favor of the version neutral
        tcpConnectionTable.
        
        .. attribute:: tcpconnentry
        
        	A conceptual row of the tcpConnTable containing information about a particular current IPv4 TCP connection.  Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of    :py:class:`Tcpconnentry <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcpconntable.Tcpconnentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TcpMib.Tcpconntable, self).__init__()

            self.yang_name = "tcpConnTable"
            self.yang_parent_name = "TCP-MIB"

            self.tcpconnentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(TcpMib.Tcpconntable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TcpMib.Tcpconntable, self).__setattr__(name, value)


        class Tcpconnentry(Entity):
            """
            A conceptual row of the tcpConnTable containing information
            about a particular current IPv4 TCP connection.  Each row
            of this table is transient in that it ceases to exist when
            (or soon after) the connection makes the transition to the
            CLOSED state.
            
            .. attribute:: tcpconnlocaladdress  <key>
            
            	The local IP address for this TCP connection.  In the case of a connection in the listen state willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnlocalport  <key>
            
            	The local port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnremaddress  <key>
            
            	The remote IP address for this TCP connection
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnremport  <key>
            
            	The remote port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: tcpconnstate
            
            	The state of this TCP connection.  The only value that may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably)
            	**type**\:   :py:class:`Tcpconnstate <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcpconntable.Tcpconnentry.Tcpconnstate>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'TCP-MIB'
            _revision = '2005-02-18'

            def __init__(self):
                super(TcpMib.Tcpconntable.Tcpconnentry, self).__init__()

                self.yang_name = "tcpConnEntry"
                self.yang_parent_name = "tcpConnTable"

                self.tcpconnlocaladdress = YLeaf(YType.str, "tcpConnLocalAddress")

                self.tcpconnlocalport = YLeaf(YType.int32, "tcpConnLocalPort")

                self.tcpconnremaddress = YLeaf(YType.str, "tcpConnRemAddress")

                self.tcpconnremport = YLeaf(YType.int32, "tcpConnRemPort")

                self.tcpconnstate = YLeaf(YType.enumeration, "tcpConnState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tcpconnlocaladdress",
                                "tcpconnlocalport",
                                "tcpconnremaddress",
                                "tcpconnremport",
                                "tcpconnstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TcpMib.Tcpconntable.Tcpconnentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TcpMib.Tcpconntable.Tcpconnentry, self).__setattr__(name, value)

            class Tcpconnstate(Enum):
                """
                Tcpconnstate

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


            def has_data(self):
                return (
                    self.tcpconnlocaladdress.is_set or
                    self.tcpconnlocalport.is_set or
                    self.tcpconnremaddress.is_set or
                    self.tcpconnremport.is_set or
                    self.tcpconnstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tcpconnlocaladdress.yfilter != YFilter.not_set or
                    self.tcpconnlocalport.yfilter != YFilter.not_set or
                    self.tcpconnremaddress.yfilter != YFilter.not_set or
                    self.tcpconnremport.yfilter != YFilter.not_set or
                    self.tcpconnstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tcpConnEntry" + "[tcpConnLocalAddress='" + self.tcpconnlocaladdress.get() + "']" + "[tcpConnLocalPort='" + self.tcpconnlocalport.get() + "']" + "[tcpConnRemAddress='" + self.tcpconnremaddress.get() + "']" + "[tcpConnRemPort='" + self.tcpconnremport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TCP-MIB:TCP-MIB/tcpConnTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tcpconnlocaladdress.is_set or self.tcpconnlocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnlocaladdress.get_name_leafdata())
                if (self.tcpconnlocalport.is_set or self.tcpconnlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnlocalport.get_name_leafdata())
                if (self.tcpconnremaddress.is_set or self.tcpconnremaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnremaddress.get_name_leafdata())
                if (self.tcpconnremport.is_set or self.tcpconnremport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnremport.get_name_leafdata())
                if (self.tcpconnstate.is_set or self.tcpconnstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tcpConnLocalAddress" or name == "tcpConnLocalPort" or name == "tcpConnRemAddress" or name == "tcpConnRemPort" or name == "tcpConnState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tcpConnLocalAddress"):
                    self.tcpconnlocaladdress = value
                    self.tcpconnlocaladdress.value_namespace = name_space
                    self.tcpconnlocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnLocalPort"):
                    self.tcpconnlocalport = value
                    self.tcpconnlocalport.value_namespace = name_space
                    self.tcpconnlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnRemAddress"):
                    self.tcpconnremaddress = value
                    self.tcpconnremaddress.value_namespace = name_space
                    self.tcpconnremaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnRemPort"):
                    self.tcpconnremport = value
                    self.tcpconnremport.value_namespace = name_space
                    self.tcpconnremport.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnState"):
                    self.tcpconnstate = value
                    self.tcpconnstate.value_namespace = name_space
                    self.tcpconnstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tcpconnentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tcpconnentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tcpConnTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TCP-MIB:TCP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tcpConnEntry"):
                for c in self.tcpconnentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TcpMib.Tcpconntable.Tcpconnentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tcpconnentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcpConnEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tcpconnectiontable(Entity):
        """
        A table containing information about existing TCP
        connections.  Note that unlike earlier TCP MIBs, there
        is a separate table for connections in the LISTEN state.
        
        .. attribute:: tcpconnectionentry
        
        	A conceptual row of the tcpConnectionTable containing information about a particular current TCP connection. Each row of this table is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of    :py:class:`Tcpconnectionentry <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcpconnectiontable.Tcpconnectionentry>`
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TcpMib.Tcpconnectiontable, self).__init__()

            self.yang_name = "tcpConnectionTable"
            self.yang_parent_name = "TCP-MIB"

            self.tcpconnectionentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(TcpMib.Tcpconnectiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TcpMib.Tcpconnectiontable, self).__setattr__(name, value)


        class Tcpconnectionentry(Entity):
            """
            A conceptual row of the tcpConnectionTable containing
            information about a particular current TCP connection.
            Each row of this table is transient in that it ceases to
            exist when (or soon after) the connection makes the
            transition to the CLOSED state.
            
            .. attribute:: tcpconnectionlocaladdresstype  <key>
            
            	The address type of tcpConnectionLocalAddress
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: tcpconnectionlocaladdress  <key>
            
            	The local IP address for this TCP connection.  The type of this address is determined by the value of tcpConnectionLocalAddressType.  As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tcpconnectionlocalport  <key>
            
            	The local port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnectionremaddresstype  <key>
            
            	The address type of tcpConnectionRemAddress
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: tcpconnectionremaddress  <key>
            
            	The remote IP address for this TCP connection.  The type of this address is determined by the value of tcpConnectionRemAddressType.  As this object is used in the index for the tcpConnectionTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tcpconnectionremport  <key>
            
            	The remote port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnectionprocess
            
            	The system's process ID for the process associated with this connection, or zero if there is no such process.  This value is expected to be the same as HOST\-RESOURCES\-MIB\:\: hrSWRunIndex or SYSAPPL\-MIB\:\:sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tcpconnectionstate
            
            	The state of this TCP connection.  The value listen(2) is included only for parallelism to the old tcpConnTable and should not be used.  A connection in LISTEN state should be present in the tcpListenerTable.  The only value that may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then the TCB (as defined in [RFC793]) of the corresponding connection on the managed node is deleted, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note, however, that RST segments are not sent reliably)
            	**type**\:   :py:class:`Tcpconnectionstate <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcpconnectiontable.Tcpconnectionentry.Tcpconnectionstate>`
            
            

            """

            _prefix = 'TCP-MIB'
            _revision = '2005-02-18'

            def __init__(self):
                super(TcpMib.Tcpconnectiontable.Tcpconnectionentry, self).__init__()

                self.yang_name = "tcpConnectionEntry"
                self.yang_parent_name = "tcpConnectionTable"

                self.tcpconnectionlocaladdresstype = YLeaf(YType.enumeration, "tcpConnectionLocalAddressType")

                self.tcpconnectionlocaladdress = YLeaf(YType.str, "tcpConnectionLocalAddress")

                self.tcpconnectionlocalport = YLeaf(YType.uint16, "tcpConnectionLocalPort")

                self.tcpconnectionremaddresstype = YLeaf(YType.enumeration, "tcpConnectionRemAddressType")

                self.tcpconnectionremaddress = YLeaf(YType.str, "tcpConnectionRemAddress")

                self.tcpconnectionremport = YLeaf(YType.uint16, "tcpConnectionRemPort")

                self.tcpconnectionprocess = YLeaf(YType.uint32, "tcpConnectionProcess")

                self.tcpconnectionstate = YLeaf(YType.enumeration, "tcpConnectionState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tcpconnectionlocaladdresstype",
                                "tcpconnectionlocaladdress",
                                "tcpconnectionlocalport",
                                "tcpconnectionremaddresstype",
                                "tcpconnectionremaddress",
                                "tcpconnectionremport",
                                "tcpconnectionprocess",
                                "tcpconnectionstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TcpMib.Tcpconnectiontable.Tcpconnectionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TcpMib.Tcpconnectiontable.Tcpconnectionentry, self).__setattr__(name, value)

            class Tcpconnectionstate(Enum):
                """
                Tcpconnectionstate

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


            def has_data(self):
                return (
                    self.tcpconnectionlocaladdresstype.is_set or
                    self.tcpconnectionlocaladdress.is_set or
                    self.tcpconnectionlocalport.is_set or
                    self.tcpconnectionremaddresstype.is_set or
                    self.tcpconnectionremaddress.is_set or
                    self.tcpconnectionremport.is_set or
                    self.tcpconnectionprocess.is_set or
                    self.tcpconnectionstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tcpconnectionlocaladdresstype.yfilter != YFilter.not_set or
                    self.tcpconnectionlocaladdress.yfilter != YFilter.not_set or
                    self.tcpconnectionlocalport.yfilter != YFilter.not_set or
                    self.tcpconnectionremaddresstype.yfilter != YFilter.not_set or
                    self.tcpconnectionremaddress.yfilter != YFilter.not_set or
                    self.tcpconnectionremport.yfilter != YFilter.not_set or
                    self.tcpconnectionprocess.yfilter != YFilter.not_set or
                    self.tcpconnectionstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tcpConnectionEntry" + "[tcpConnectionLocalAddressType='" + self.tcpconnectionlocaladdresstype.get() + "']" + "[tcpConnectionLocalAddress='" + self.tcpconnectionlocaladdress.get() + "']" + "[tcpConnectionLocalPort='" + self.tcpconnectionlocalport.get() + "']" + "[tcpConnectionRemAddressType='" + self.tcpconnectionremaddresstype.get() + "']" + "[tcpConnectionRemAddress='" + self.tcpconnectionremaddress.get() + "']" + "[tcpConnectionRemPort='" + self.tcpconnectionremport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TCP-MIB:TCP-MIB/tcpConnectionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tcpconnectionlocaladdresstype.is_set or self.tcpconnectionlocaladdresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionlocaladdresstype.get_name_leafdata())
                if (self.tcpconnectionlocaladdress.is_set or self.tcpconnectionlocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionlocaladdress.get_name_leafdata())
                if (self.tcpconnectionlocalport.is_set or self.tcpconnectionlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionlocalport.get_name_leafdata())
                if (self.tcpconnectionremaddresstype.is_set or self.tcpconnectionremaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionremaddresstype.get_name_leafdata())
                if (self.tcpconnectionremaddress.is_set or self.tcpconnectionremaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionremaddress.get_name_leafdata())
                if (self.tcpconnectionremport.is_set or self.tcpconnectionremport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionremport.get_name_leafdata())
                if (self.tcpconnectionprocess.is_set or self.tcpconnectionprocess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionprocess.get_name_leafdata())
                if (self.tcpconnectionstate.is_set or self.tcpconnectionstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcpconnectionstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tcpConnectionLocalAddressType" or name == "tcpConnectionLocalAddress" or name == "tcpConnectionLocalPort" or name == "tcpConnectionRemAddressType" or name == "tcpConnectionRemAddress" or name == "tcpConnectionRemPort" or name == "tcpConnectionProcess" or name == "tcpConnectionState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tcpConnectionLocalAddressType"):
                    self.tcpconnectionlocaladdresstype = value
                    self.tcpconnectionlocaladdresstype.value_namespace = name_space
                    self.tcpconnectionlocaladdresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionLocalAddress"):
                    self.tcpconnectionlocaladdress = value
                    self.tcpconnectionlocaladdress.value_namespace = name_space
                    self.tcpconnectionlocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionLocalPort"):
                    self.tcpconnectionlocalport = value
                    self.tcpconnectionlocalport.value_namespace = name_space
                    self.tcpconnectionlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionRemAddressType"):
                    self.tcpconnectionremaddresstype = value
                    self.tcpconnectionremaddresstype.value_namespace = name_space
                    self.tcpconnectionremaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionRemAddress"):
                    self.tcpconnectionremaddress = value
                    self.tcpconnectionremaddress.value_namespace = name_space
                    self.tcpconnectionremaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionRemPort"):
                    self.tcpconnectionremport = value
                    self.tcpconnectionremport.value_namespace = name_space
                    self.tcpconnectionremport.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionProcess"):
                    self.tcpconnectionprocess = value
                    self.tcpconnectionprocess.value_namespace = name_space
                    self.tcpconnectionprocess.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpConnectionState"):
                    self.tcpconnectionstate = value
                    self.tcpconnectionstate.value_namespace = name_space
                    self.tcpconnectionstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tcpconnectionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tcpconnectionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tcpConnectionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TCP-MIB:TCP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tcpConnectionEntry"):
                for c in self.tcpconnectionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TcpMib.Tcpconnectiontable.Tcpconnectionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tcpconnectionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcpConnectionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tcplistenertable(Entity):
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
        	**type**\: list of    :py:class:`Tcplistenerentry <ydk.models.cisco_ios_xe.TCP_MIB.TcpMib.Tcplistenertable.Tcplistenerentry>`
        
        

        """

        _prefix = 'TCP-MIB'
        _revision = '2005-02-18'

        def __init__(self):
            super(TcpMib.Tcplistenertable, self).__init__()

            self.yang_name = "tcpListenerTable"
            self.yang_parent_name = "TCP-MIB"

            self.tcplistenerentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(TcpMib.Tcplistenertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TcpMib.Tcplistenertable, self).__setattr__(name, value)


        class Tcplistenerentry(Entity):
            """
            A conceptual row of the tcpListenerTable containing
            information about a particular TCP listener.
            
            .. attribute:: tcplistenerlocaladdresstype  <key>
            
            	The address type of tcpListenerLocalAddress.  The value should be unknown (0) if connection initiations to all local IP addresses are accepted
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: tcplistenerlocaladdress  <key>
            
            	The local IP address for this TCP connection.  The value of this object can be represented in three possible ways, depending on the characteristics of the listening application\:  1. For an application willing to accept both IPv4 and    IPv6 datagrams, the value of this object must be    ''h (a zero\-length octet\-string), with the value    of the corresponding tcpListenerLocalAddressType    object being unknown (0).  2. For an application willing to accept only IPv4 or    IPv6 datagrams, the value of this object must be    '0.0.0.0' or '\:\:' respectively, with    tcpListenerLocalAddressType representing the    appropriate address type.  3. For an application which is listening for data    destined only to a specific IP address, the value    of this object is the specific local address, with    tcpListenerLocalAddressType representing the    appropriate address type.  As this object is used in the index for the tcpListenerTable, implementors should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; otherwise the information cannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tcplistenerlocalport  <key>
            
            	The local port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: tcplistenerprocess
            
            	The system's process ID for the process associated with this listener, or zero if there is no such process.  This value is expected to be the same as HOST\-RESOURCES\-MIB\:\: hrSWRunIndex or SYSAPPL\-MIB\:\:sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TCP-MIB'
            _revision = '2005-02-18'

            def __init__(self):
                super(TcpMib.Tcplistenertable.Tcplistenerentry, self).__init__()

                self.yang_name = "tcpListenerEntry"
                self.yang_parent_name = "tcpListenerTable"

                self.tcplistenerlocaladdresstype = YLeaf(YType.enumeration, "tcpListenerLocalAddressType")

                self.tcplistenerlocaladdress = YLeaf(YType.str, "tcpListenerLocalAddress")

                self.tcplistenerlocalport = YLeaf(YType.uint16, "tcpListenerLocalPort")

                self.tcplistenerprocess = YLeaf(YType.uint32, "tcpListenerProcess")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tcplistenerlocaladdresstype",
                                "tcplistenerlocaladdress",
                                "tcplistenerlocalport",
                                "tcplistenerprocess") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TcpMib.Tcplistenertable.Tcplistenerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TcpMib.Tcplistenertable.Tcplistenerentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tcplistenerlocaladdresstype.is_set or
                    self.tcplistenerlocaladdress.is_set or
                    self.tcplistenerlocalport.is_set or
                    self.tcplistenerprocess.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tcplistenerlocaladdresstype.yfilter != YFilter.not_set or
                    self.tcplistenerlocaladdress.yfilter != YFilter.not_set or
                    self.tcplistenerlocalport.yfilter != YFilter.not_set or
                    self.tcplistenerprocess.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tcpListenerEntry" + "[tcpListenerLocalAddressType='" + self.tcplistenerlocaladdresstype.get() + "']" + "[tcpListenerLocalAddress='" + self.tcplistenerlocaladdress.get() + "']" + "[tcpListenerLocalPort='" + self.tcplistenerlocalport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TCP-MIB:TCP-MIB/tcpListenerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tcplistenerlocaladdresstype.is_set or self.tcplistenerlocaladdresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcplistenerlocaladdresstype.get_name_leafdata())
                if (self.tcplistenerlocaladdress.is_set or self.tcplistenerlocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcplistenerlocaladdress.get_name_leafdata())
                if (self.tcplistenerlocalport.is_set or self.tcplistenerlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcplistenerlocalport.get_name_leafdata())
                if (self.tcplistenerprocess.is_set or self.tcplistenerprocess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tcplistenerprocess.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tcpListenerLocalAddressType" or name == "tcpListenerLocalAddress" or name == "tcpListenerLocalPort" or name == "tcpListenerProcess"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tcpListenerLocalAddressType"):
                    self.tcplistenerlocaladdresstype = value
                    self.tcplistenerlocaladdresstype.value_namespace = name_space
                    self.tcplistenerlocaladdresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpListenerLocalAddress"):
                    self.tcplistenerlocaladdress = value
                    self.tcplistenerlocaladdress.value_namespace = name_space
                    self.tcplistenerlocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpListenerLocalPort"):
                    self.tcplistenerlocalport = value
                    self.tcplistenerlocalport.value_namespace = name_space
                    self.tcplistenerlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "tcpListenerProcess"):
                    self.tcplistenerprocess = value
                    self.tcplistenerprocess.value_namespace = name_space
                    self.tcplistenerprocess.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tcplistenerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tcplistenerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tcpListenerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TCP-MIB:TCP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tcpListenerEntry"):
                for c in self.tcplistenerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TcpMib.Tcplistenertable.Tcplistenerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tcplistenerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tcpListenerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.tcp is not None and self.tcp.has_data()) or
            (self.tcpconnectiontable is not None and self.tcpconnectiontable.has_data()) or
            (self.tcpconntable is not None and self.tcpconntable.has_data()) or
            (self.tcplistenertable is not None and self.tcplistenertable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.tcp is not None and self.tcp.has_operation()) or
            (self.tcpconnectiontable is not None and self.tcpconnectiontable.has_operation()) or
            (self.tcpconntable is not None and self.tcpconntable.has_operation()) or
            (self.tcplistenertable is not None and self.tcplistenertable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "TCP-MIB:TCP-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "tcp"):
            if (self.tcp is None):
                self.tcp = TcpMib.Tcp()
                self.tcp.parent = self
                self._children_name_map["tcp"] = "tcp"
            return self.tcp

        if (child_yang_name == "tcpConnectionTable"):
            if (self.tcpconnectiontable is None):
                self.tcpconnectiontable = TcpMib.Tcpconnectiontable()
                self.tcpconnectiontable.parent = self
                self._children_name_map["tcpconnectiontable"] = "tcpConnectionTable"
            return self.tcpconnectiontable

        if (child_yang_name == "tcpConnTable"):
            if (self.tcpconntable is None):
                self.tcpconntable = TcpMib.Tcpconntable()
                self.tcpconntable.parent = self
                self._children_name_map["tcpconntable"] = "tcpConnTable"
            return self.tcpconntable

        if (child_yang_name == "tcpListenerTable"):
            if (self.tcplistenertable is None):
                self.tcplistenertable = TcpMib.Tcplistenertable()
                self.tcplistenertable.parent = self
                self._children_name_map["tcplistenertable"] = "tcpListenerTable"
            return self.tcplistenertable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "tcp" or name == "tcpConnectionTable" or name == "tcpConnTable" or name == "tcpListenerTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TcpMib()
        return self._top_entity

