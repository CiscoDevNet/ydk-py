""" UDP_MIB 

The MIB module for managing UDP implementations.
Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4113;
see the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class UDPMIB(Entity):
    """
    
    
    .. attribute:: udp
    
    	
    	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xe.UDP_MIB.UDPMIB.Udp>`
    
    .. attribute:: udptable
    
    	A table containing IPv4\-specific UDP listener information.  It contains information about all local IPv4 UDP end\-points on which an application is currently accepting datagrams.  This table has been deprecated in favor of the version neutral udpEndpointTable
    	**type**\:  :py:class:`Udptable <ydk.models.cisco_ios_xe.UDP_MIB.UDPMIB.Udptable>`
    
    	**status**\: deprecated
    
    .. attribute:: udpendpointtable
    
    	A table containing information about this entity's UDP endpoints on which a local application is currently accepting or sending datagrams.  The address type in this table represents the address type used for the communication, irrespective of the higher\-layer abstraction.  For example, an application using IPv6 'sockets' to communicate via IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use InetAddressType ipv4(1).  Unlike the udpTable in RFC 2013, this table also allows the representation of an application that completely specifies both local and remote addresses and ports.  A listening application is represented in three possible ways\:  1) An application that is willing to accept both IPv4    and IPv6 datagrams is represented by a    udpEndpointLocalAddressType of unknown(0) and a    udpEndpointLocalAddress of ''h (a zero\-length    octet\-string).  2) An application that is willing to accept only IPv4    or only IPv6 datagrams is represented by a    udpEndpointLocalAddressType of the appropriate    address type and a udpEndpointLocalAddress of    '0.0.0.0' or '\:\:' respectively.  3) An application that is listening for datagrams only    for a specific IP address but from any remote    system is represented by a    udpEndpointLocalAddressType of the appropriate    address type, with udpEndpointLocalAddress    specifying the local address.  In all cases where the remote is a wildcard, the udpEndpointRemoteAddressType is unknown(0), the udpEndpointRemoteAddress is ''h (a zero\-length octet\-string), and the udpEndpointRemotePort is 0.  If the operating system is demultiplexing UDP packets by remote address and port, or if the application has 'connected' the socket specifying a default remote address and port, the udpEndpointRemote\* values should be used to reflect this
    	**type**\:  :py:class:`Udpendpointtable <ydk.models.cisco_ios_xe.UDP_MIB.UDPMIB.Udpendpointtable>`
    
    

    """

    _prefix = 'UDP-MIB'
    _revision = '2005-05-20'

    def __init__(self):
        super(UDPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "UDP-MIB"
        self.yang_parent_name = "UDP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("udp", ("udp", UDPMIB.Udp)), ("udpTable", ("udptable", UDPMIB.Udptable)), ("udpEndpointTable", ("udpendpointtable", UDPMIB.Udpendpointtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.udp = UDPMIB.Udp()
        self.udp.parent = self
        self._children_name_map["udp"] = "udp"
        self._children_yang_names.add("udp")

        self.udptable = UDPMIB.Udptable()
        self.udptable.parent = self
        self._children_name_map["udptable"] = "udpTable"
        self._children_yang_names.add("udpTable")

        self.udpendpointtable = UDPMIB.Udpendpointtable()
        self.udpendpointtable.parent = self
        self._children_name_map["udpendpointtable"] = "udpEndpointTable"
        self._children_yang_names.add("udpEndpointTable")
        self._segment_path = lambda: "UDP-MIB:UDP-MIB"


    class Udp(Entity):
        """
        
        
        .. attribute:: udpindatagrams
        
        	The total number of UDP datagrams delivered to UDP users.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpnoports
        
        	The total number of received UDP datagrams for which there was no application at the destination port.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpinerrors
        
        	The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpoutdatagrams
        
        	The total number of UDP datagrams sent from this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udphcindatagrams
        
        	The total number of UDP datagrams delivered to UDP users, for devices that can receive more than 1 million UDP datagrams per second.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: udphcoutdatagrams
        
        	The total number of UDP datagrams sent from this entity, for devices that can transmit more than 1 million UDP datagrams per second.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'UDP-MIB'
        _revision = '2005-05-20'

        def __init__(self):
            super(UDPMIB.Udp, self).__init__()

            self.yang_name = "udp"
            self.yang_parent_name = "UDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('udpindatagrams', YLeaf(YType.uint32, 'udpInDatagrams')),
                ('udpnoports', YLeaf(YType.uint32, 'udpNoPorts')),
                ('udpinerrors', YLeaf(YType.uint32, 'udpInErrors')),
                ('udpoutdatagrams', YLeaf(YType.uint32, 'udpOutDatagrams')),
                ('udphcindatagrams', YLeaf(YType.uint64, 'udpHCInDatagrams')),
                ('udphcoutdatagrams', YLeaf(YType.uint64, 'udpHCOutDatagrams')),
            ])
            self.udpindatagrams = None
            self.udpnoports = None
            self.udpinerrors = None
            self.udpoutdatagrams = None
            self.udphcindatagrams = None
            self.udphcoutdatagrams = None
            self._segment_path = lambda: "udp"
            self._absolute_path = lambda: "UDP-MIB:UDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(UDPMIB.Udp, ['udpindatagrams', 'udpnoports', 'udpinerrors', 'udpoutdatagrams', 'udphcindatagrams', 'udphcoutdatagrams'], name, value)


    class Udptable(Entity):
        """
        A table containing IPv4\-specific UDP listener
        information.  It contains information about all local
        IPv4 UDP end\-points on which an application is
        currently accepting datagrams.  This table has been
        deprecated in favor of the version neutral
        udpEndpointTable.
        
        .. attribute:: udpentry
        
        	Information about a particular current UDP listener
        	**type**\: list of  		 :py:class:`Udpentry <ydk.models.cisco_ios_xe.UDP_MIB.UDPMIB.Udptable.Udpentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'UDP-MIB'
        _revision = '2005-05-20'

        def __init__(self):
            super(UDPMIB.Udptable, self).__init__()

            self.yang_name = "udpTable"
            self.yang_parent_name = "UDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("udpEntry", ("udpentry", UDPMIB.Udptable.Udpentry))])
            self._leafs = OrderedDict()

            self.udpentry = YList(self)
            self._segment_path = lambda: "udpTable"
            self._absolute_path = lambda: "UDP-MIB:UDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(UDPMIB.Udptable, [], name, value)


        class Udpentry(Entity):
            """
            Information about a particular current UDP listener.
            
            .. attribute:: udplocaladdress  (key)
            
            	The local IP address for this UDP listener.  In the case of a UDP listener that is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: udplocalport  (key)
            
            	The local port number for this UDP listener
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'UDP-MIB'
            _revision = '2005-05-20'

            def __init__(self):
                super(UDPMIB.Udptable.Udpentry, self).__init__()

                self.yang_name = "udpEntry"
                self.yang_parent_name = "udpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['udplocaladdress','udplocalport']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('udplocaladdress', YLeaf(YType.str, 'udpLocalAddress')),
                    ('udplocalport', YLeaf(YType.int32, 'udpLocalPort')),
                ])
                self.udplocaladdress = None
                self.udplocalport = None
                self._segment_path = lambda: "udpEntry" + "[udpLocalAddress='" + str(self.udplocaladdress) + "']" + "[udpLocalPort='" + str(self.udplocalport) + "']"
                self._absolute_path = lambda: "UDP-MIB:UDP-MIB/udpTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(UDPMIB.Udptable.Udpentry, ['udplocaladdress', 'udplocalport'], name, value)


    class Udpendpointtable(Entity):
        """
        A table containing information about this entity's UDP
        endpoints on which a local application is currently
        accepting or sending datagrams.
        
        The address type in this table represents the address
        type used for the communication, irrespective of the
        higher\-layer abstraction.  For example, an application
        using IPv6 'sockets' to communicate via IPv4 between
        \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use
        InetAddressType ipv4(1).
        
        Unlike the udpTable in RFC 2013, this table also allows
        the representation of an application that completely
        specifies both local and remote addresses and ports.  A
        listening application is represented in three possible
        ways\:
        
        1) An application that is willing to accept both IPv4
           and IPv6 datagrams is represented by a
           udpEndpointLocalAddressType of unknown(0) and a
           udpEndpointLocalAddress of ''h (a zero\-length
           octet\-string).
        
        2) An application that is willing to accept only IPv4
           or only IPv6 datagrams is represented by a
           udpEndpointLocalAddressType of the appropriate
           address type and a udpEndpointLocalAddress of
           '0.0.0.0' or '\:\:' respectively.
        
        3) An application that is listening for datagrams only
           for a specific IP address but from any remote
           system is represented by a
           udpEndpointLocalAddressType of the appropriate
           address type, with udpEndpointLocalAddress
           specifying the local address.
        
        In all cases where the remote is a wildcard, the
        udpEndpointRemoteAddressType is unknown(0), the
        udpEndpointRemoteAddress is ''h (a zero\-length
        octet\-string), and the udpEndpointRemotePort is 0.
        
        If the operating system is demultiplexing UDP packets
        by remote address and port, or if the application has
        'connected' the socket specifying a default remote
        address and port, the udpEndpointRemote\* values should
        be used to reflect this.
        
        .. attribute:: udpendpointentry
        
        	Information about a particular current UDP endpoint.  Implementers need to be aware that if the total number of elements (octets or sub\-identifiers) in udpEndpointLocalAddress and udpEndpointRemoteAddress exceeds 111, then OIDs of column instances in this table will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of  		 :py:class:`Udpendpointentry <ydk.models.cisco_ios_xe.UDP_MIB.UDPMIB.Udpendpointtable.Udpendpointentry>`
        
        

        """

        _prefix = 'UDP-MIB'
        _revision = '2005-05-20'

        def __init__(self):
            super(UDPMIB.Udpendpointtable, self).__init__()

            self.yang_name = "udpEndpointTable"
            self.yang_parent_name = "UDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("udpEndpointEntry", ("udpendpointentry", UDPMIB.Udpendpointtable.Udpendpointentry))])
            self._leafs = OrderedDict()

            self.udpendpointentry = YList(self)
            self._segment_path = lambda: "udpEndpointTable"
            self._absolute_path = lambda: "UDP-MIB:UDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(UDPMIB.Udpendpointtable, [], name, value)


        class Udpendpointentry(Entity):
            """
            Information about a particular current UDP endpoint.
            
            Implementers need to be aware that if the total number
            of elements (octets or sub\-identifiers) in
            udpEndpointLocalAddress and udpEndpointRemoteAddress
            exceeds 111, then OIDs of column instances in this table
            will have more than 128 sub\-identifiers and cannot be
            accessed using SNMPv1, SNMPv2c, or SNMPv3.
            
            .. attribute:: udpendpointlocaladdresstype  (key)
            
            	The address type of udpEndpointLocalAddress.  Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all local IP addresses are accepted
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: udpendpointlocaladdress  (key)
            
            	The local IP address for this UDP endpoint.  The value of this object can be represented in three  possible ways, depending on the characteristics of the listening application\:  1. For an application that is willing to accept both    IPv4 and IPv6 datagrams, the value of this object    must be ''h (a zero\-length octet\-string), with    the value of the corresponding instance of the    udpEndpointLocalAddressType object being unknown(0).  2. For an application that is willing to accept only IPv4    or only IPv6 datagrams, the value of this object    must be '0.0.0.0' or '\:\:', respectively, while the    corresponding instance of the    udpEndpointLocalAddressType object represents the    appropriate address type.  3. For an application that is listening for data    destined only to a specific IP address, the value    of this object is the specific IP address for which    this node is receiving packets, with the    corresponding instance of the    udpEndpointLocalAddressType object representing the    appropriate address type.  As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: udpendpointlocalport  (key)
            
            	The local port number for this UDP endpoint
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: udpendpointremoteaddresstype  (key)
            
            	The address type of udpEndpointRemoteAddress.  Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all remote IP addresses are accepted.  Also, note that some combinations of  udpEndpointLocalAdressType and udpEndpointRemoteAddressType are not supported.  In particular, if the value of this object is not unknown(0), it is expected to always refer to the same IP version as udpEndpointLocalAddressType
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: udpendpointremoteaddress  (key)
            
            	The remote IP address for this UDP endpoint.  If datagrams from any remote system are to be accepted, this value is ''h (a zero\-length octet\-string). Otherwise, it has the type described by udpEndpointRemoteAddressType and is the address of the remote system from which datagrams are to be accepted (or to which all datagrams will be sent).  As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: udpendpointremoteport  (key)
            
            	The remote port number for this UDP endpoint.  If datagrams from any remote system are to be accepted, this value is zero
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: udpendpointinstance  (key)
            
            	The instance of this tuple.  This object is used to distinguish among multiple processes 'connected' to the same UDP endpoint.  For example, on a system implementing the BSD sockets interface, this would be used to support the SO\_REUSEADDR and SO\_REUSEPORT socket options
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: udpendpointprocess
            
            	The system's process ID for the process associated with this endpoint, or zero if there is no such process. This value is expected to be the same as HOST\-RESOURCES\-MIB\:\:hrSWRunIndex or SYSAPPL\-MIB\:\: sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'UDP-MIB'
            _revision = '2005-05-20'

            def __init__(self):
                super(UDPMIB.Udpendpointtable.Udpendpointentry, self).__init__()

                self.yang_name = "udpEndpointEntry"
                self.yang_parent_name = "udpEndpointTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['udpendpointlocaladdresstype','udpendpointlocaladdress','udpendpointlocalport','udpendpointremoteaddresstype','udpendpointremoteaddress','udpendpointremoteport','udpendpointinstance']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('udpendpointlocaladdresstype', YLeaf(YType.enumeration, 'udpEndpointLocalAddressType')),
                    ('udpendpointlocaladdress', YLeaf(YType.str, 'udpEndpointLocalAddress')),
                    ('udpendpointlocalport', YLeaf(YType.uint16, 'udpEndpointLocalPort')),
                    ('udpendpointremoteaddresstype', YLeaf(YType.enumeration, 'udpEndpointRemoteAddressType')),
                    ('udpendpointremoteaddress', YLeaf(YType.str, 'udpEndpointRemoteAddress')),
                    ('udpendpointremoteport', YLeaf(YType.uint16, 'udpEndpointRemotePort')),
                    ('udpendpointinstance', YLeaf(YType.uint32, 'udpEndpointInstance')),
                    ('udpendpointprocess', YLeaf(YType.uint32, 'udpEndpointProcess')),
                ])
                self.udpendpointlocaladdresstype = None
                self.udpendpointlocaladdress = None
                self.udpendpointlocalport = None
                self.udpendpointremoteaddresstype = None
                self.udpendpointremoteaddress = None
                self.udpendpointremoteport = None
                self.udpendpointinstance = None
                self.udpendpointprocess = None
                self._segment_path = lambda: "udpEndpointEntry" + "[udpEndpointLocalAddressType='" + str(self.udpendpointlocaladdresstype) + "']" + "[udpEndpointLocalAddress='" + str(self.udpendpointlocaladdress) + "']" + "[udpEndpointLocalPort='" + str(self.udpendpointlocalport) + "']" + "[udpEndpointRemoteAddressType='" + str(self.udpendpointremoteaddresstype) + "']" + "[udpEndpointRemoteAddress='" + str(self.udpendpointremoteaddress) + "']" + "[udpEndpointRemotePort='" + str(self.udpendpointremoteport) + "']" + "[udpEndpointInstance='" + str(self.udpendpointinstance) + "']"
                self._absolute_path = lambda: "UDP-MIB:UDP-MIB/udpEndpointTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(UDPMIB.Udpendpointtable.Udpendpointentry, ['udpendpointlocaladdresstype', 'udpendpointlocaladdress', 'udpendpointlocalport', 'udpendpointremoteaddresstype', 'udpendpointremoteaddress', 'udpendpointremoteport', 'udpendpointinstance', 'udpendpointprocess'], name, value)

    def clone_ptr(self):
        self._top_entity = UDPMIB()
        return self._top_entity

