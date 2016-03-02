""" UDP_MIB 

The MIB module for managing UDP implementations.
Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4113;
see the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum


class UDPMIB(object):
    """
    
    
    .. attribute:: udp
    
    	
    	**type**\: :py:class:`Udp <ydk.models.udp.UDP_MIB.UDPMIB.Udp>`
    
    .. attribute:: udpendpointtable
    
    	A table containing information about this entity's UDP endpoints on which a local application is currently accepting or sending datagrams.  The address type in this table represents the address type used for the communication, irrespective of the higher\-layer abstraction.  For example, an application using IPv6 'sockets' to communicate via IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use InetAddressType ipv4(1).  Unlike the udpTable in RFC 2013, this table also allows the representation of an application that completely specifies both local and remote addresses and ports.  A listening application is represented in three possible ways\:  1) An application that is willing to accept both IPv4    and IPv6 datagrams is represented by a    udpEndpointLocalAddressType of unknown(0) and a    udpEndpointLocalAddress of ''h (a zero\-length    octet\-string).  2) An application that is willing to accept only IPv4    or only IPv6 datagrams is represented by a    udpEndpointLocalAddressType of the appropriate    address type and a udpEndpointLocalAddress of    '0.0.0.0' or '\:\:' respectively.  3) An application that is listening for datagrams only    for a specific IP address but from any remote    system is represented by a    udpEndpointLocalAddressType of the appropriate    address type, with udpEndpointLocalAddress    specifying the local address.  In all cases where the remote is a wildcard, the udpEndpointRemoteAddressType is unknown(0), the udpEndpointRemoteAddress is ''h (a zero\-length octet\-string), and the udpEndpointRemotePort is 0.  If the operating system is demultiplexing UDP packets by remote address and port, or if the application has 'connected' the socket specifying a default remote address and port, the udpEndpointRemote\* values should be used to reflect this
    	**type**\: :py:class:`UdpEndpointTable <ydk.models.udp.UDP_MIB.UDPMIB.UdpEndpointTable>`
    
    .. attribute:: udptable
    
    	A table containing IPv4\-specific UDP listener information.  It contains information about all local IPv4 UDP end\-points on which an application is currently accepting datagrams.  This table has been deprecated in favor of the version neutral udpEndpointTable
    	**type**\: :py:class:`UdpTable <ydk.models.udp.UDP_MIB.UDPMIB.UdpTable>`
    
    

    """

    _prefix = 'udp-mib'
    _revision = '2005-05-20'

    def __init__(self):
        self.udp = UDPMIB.Udp()
        self.udp.parent = self
        self.udpendpointtable = UDPMIB.UdpEndpointTable()
        self.udpendpointtable.parent = self
        self.udptable = UDPMIB.UdpTable()
        self.udptable.parent = self


    class Udp(object):
        """
        
        
        .. attribute:: udphcindatagrams
        
        	The total number of UDP datagrams delivered to UDP users, for devices that can receive more than 1 million UDP datagrams per second.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: udphcoutdatagrams
        
        	The total number of UDP datagrams sent from this entity, for devices that can transmit more than 1 million UDP datagrams per second.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: udpindatagrams
        
        	The total number of UDP datagrams delivered to UDP users.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpinerrors
        
        	The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpnoports
        
        	The total number of received UDP datagrams for which there was no application at the destination port.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpoutdatagrams
        
        	The total number of UDP datagrams sent from this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'udp-mib'
        _revision = '2005-05-20'

        def __init__(self):
            self.parent = None
            self.udphcindatagrams = None
            self.udphcoutdatagrams = None
            self.udpindatagrams = None
            self.udpinerrors = None
            self.udpnoports = None
            self.udpoutdatagrams = None

        @property
        def _common_path(self):

            return '/UDP-MIB:UDP-MIB/UDP-MIB:udp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.udphcindatagrams is not None:
                return True

            if self.udphcoutdatagrams is not None:
                return True

            if self.udpindatagrams is not None:
                return True

            if self.udpinerrors is not None:
                return True

            if self.udpnoports is not None:
                return True

            if self.udpoutdatagrams is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.udp._meta import _UDP_MIB as meta
            return meta._meta_table['UDPMIB.Udp']['meta_info']


    class UdpEndpointTable(object):
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
        	**type**\: list of :py:class:`UdpEndpointEntry <ydk.models.udp.UDP_MIB.UDPMIB.UdpEndpointTable.UdpEndpointEntry>`
        
        

        """

        _prefix = 'udp-mib'
        _revision = '2005-05-20'

        def __init__(self):
            self.parent = None
            self.udpendpointentry = YList()
            self.udpendpointentry.parent = self
            self.udpendpointentry.name = 'udpendpointentry'


        class UdpEndpointEntry(object):
            """
            Information about a particular current UDP endpoint.
            
            Implementers need to be aware that if the total number
            of elements (octets or sub\-identifiers) in
            udpEndpointLocalAddress and udpEndpointRemoteAddress
            exceeds 111, then OIDs of column instances in this table
            will have more than 128 sub\-identifiers and cannot be
            accessed using SNMPv1, SNMPv2c, or SNMPv3.
            
            .. attribute:: udpendpointinstance
            
            	The instance of this tuple.  This object is used to distinguish among multiple processes 'connected' to the same UDP endpoint.  For example, on a system implementing the BSD sockets interface, this would be used to support the SO\_REUSEADDR and SO\_REUSEPORT socket options
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: udpendpointlocaladdress
            
            	The local IP address for this UDP endpoint.  The value of this object can be represented in three  possible ways, depending on the characteristics of the listening application\:  1. For an application that is willing to accept both    IPv4 and IPv6 datagrams, the value of this object    must be ''h (a zero\-length octet\-string), with    the value of the corresponding instance of the    udpEndpointLocalAddressType object being unknown(0).  2. For an application that is willing to accept only IPv4    or only IPv6 datagrams, the value of this object    must be '0.0.0.0' or '\:\:', respectively, while the    corresponding instance of the    udpEndpointLocalAddressType object represents the    appropriate address type.  3. For an application that is listening for data    destined only to a specific IP address, the value    of this object is the specific IP address for which    this node is receiving packets, with the    corresponding instance of the    udpEndpointLocalAddressType object representing the    appropriate address type.  As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: udpendpointlocaladdresstype
            
            	The address type of udpEndpointLocalAddress.  Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all local IP addresses are accepted
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: udpendpointlocalport
            
            	The local port number for this UDP endpoint
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: udpendpointremoteaddress
            
            	The remote IP address for this UDP endpoint.  If datagrams from any remote system are to be accepted, this value is ''h (a zero\-length octet\-string). Otherwise, it has the type described by udpEndpointRemoteAddressType and is the address of the remote system from which datagrams are to be accepted (or to which all datagrams will be sent).  As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: udpendpointremoteaddresstype
            
            	The address type of udpEndpointRemoteAddress.  Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all remote IP addresses are accepted.  Also, note that some combinations of  udpEndpointLocalAdressType and udpEndpointRemoteAddressType are not supported.  In particular, if the value of this object is not unknown(0), it is expected to always refer to the same IP version as udpEndpointLocalAddressType
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: udpendpointremoteport
            
            	The remote port number for this UDP endpoint.  If datagrams from any remote system are to be accepted, this value is zero
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: udpendpointprocess
            
            	The system's process ID for the process associated with this endpoint, or zero if there is no such process. This value is expected to be the same as HOST\-RESOURCES\-MIB\:\:hrSWRunIndex or SYSAPPL\-MIB\:\: sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'udp-mib'
            _revision = '2005-05-20'

            def __init__(self):
                self.parent = None
                self.udpendpointinstance = None
                self.udpendpointlocaladdress = None
                self.udpendpointlocaladdresstype = None
                self.udpendpointlocalport = None
                self.udpendpointremoteaddress = None
                self.udpendpointremoteaddresstype = None
                self.udpendpointremoteport = None
                self.udpendpointprocess = None

            @property
            def _common_path(self):
                if self.udpendpointinstance is None:
                    raise YPYDataValidationError('Key property udpendpointinstance is None')
                if self.udpendpointlocaladdress is None:
                    raise YPYDataValidationError('Key property udpendpointlocaladdress is None')
                if self.udpendpointlocaladdresstype is None:
                    raise YPYDataValidationError('Key property udpendpointlocaladdresstype is None')
                if self.udpendpointlocalport is None:
                    raise YPYDataValidationError('Key property udpendpointlocalport is None')
                if self.udpendpointremoteaddress is None:
                    raise YPYDataValidationError('Key property udpendpointremoteaddress is None')
                if self.udpendpointremoteaddresstype is None:
                    raise YPYDataValidationError('Key property udpendpointremoteaddresstype is None')
                if self.udpendpointremoteport is None:
                    raise YPYDataValidationError('Key property udpendpointremoteport is None')

                return '/UDP-MIB:UDP-MIB/UDP-MIB:udpEndpointTable/UDP-MIB:udpEndpointEntry[UDP-MIB:udpEndpointInstance = ' + str(self.udpendpointinstance) + '][UDP-MIB:udpEndpointLocalAddress = ' + str(self.udpendpointlocaladdress) + '][UDP-MIB:udpEndpointLocalAddressType = ' + str(self.udpendpointlocaladdresstype) + '][UDP-MIB:udpEndpointLocalPort = ' + str(self.udpendpointlocalport) + '][UDP-MIB:udpEndpointRemoteAddress = ' + str(self.udpendpointremoteaddress) + '][UDP-MIB:udpEndpointRemoteAddressType = ' + str(self.udpendpointremoteaddresstype) + '][UDP-MIB:udpEndpointRemotePort = ' + str(self.udpendpointremoteport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.udpendpointinstance is not None:
                    return True

                if self.udpendpointlocaladdress is not None:
                    return True

                if self.udpendpointlocaladdresstype is not None:
                    return True

                if self.udpendpointlocalport is not None:
                    return True

                if self.udpendpointremoteaddress is not None:
                    return True

                if self.udpendpointremoteaddresstype is not None:
                    return True

                if self.udpendpointremoteport is not None:
                    return True

                if self.udpendpointprocess is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.udp._meta import _UDP_MIB as meta
                return meta._meta_table['UDPMIB.UdpEndpointTable.UdpEndpointEntry']['meta_info']

        @property
        def _common_path(self):

            return '/UDP-MIB:UDP-MIB/UDP-MIB:udpEndpointTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.udpendpointentry is not None:
                for child_ref in self.udpendpointentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.udp._meta import _UDP_MIB as meta
            return meta._meta_table['UDPMIB.UdpEndpointTable']['meta_info']


    class UdpTable(object):
        """
        A table containing IPv4\-specific UDP listener
        information.  It contains information about all local
        IPv4 UDP end\-points on which an application is
        currently accepting datagrams.  This table has been
        deprecated in favor of the version neutral
        udpEndpointTable.
        
        .. attribute:: udpentry
        
        	Information about a particular current UDP listener
        	**type**\: list of :py:class:`UdpEntry <ydk.models.udp.UDP_MIB.UDPMIB.UdpTable.UdpEntry>`
        
        

        """

        _prefix = 'udp-mib'
        _revision = '2005-05-20'

        def __init__(self):
            self.parent = None
            self.udpentry = YList()
            self.udpentry.parent = self
            self.udpentry.name = 'udpentry'


        class UdpEntry(object):
            """
            Information about a particular current UDP listener.
            
            .. attribute:: udplocaladdress
            
            	The local IP address for this UDP listener.  In the case of a UDP listener that is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udplocalport
            
            	The local port number for this UDP listener
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'udp-mib'
            _revision = '2005-05-20'

            def __init__(self):
                self.parent = None
                self.udplocaladdress = None
                self.udplocalport = None

            @property
            def _common_path(self):
                if self.udplocaladdress is None:
                    raise YPYDataValidationError('Key property udplocaladdress is None')
                if self.udplocalport is None:
                    raise YPYDataValidationError('Key property udplocalport is None')

                return '/UDP-MIB:UDP-MIB/UDP-MIB:udpTable/UDP-MIB:udpEntry[UDP-MIB:udpLocalAddress = ' + str(self.udplocaladdress) + '][UDP-MIB:udpLocalPort = ' + str(self.udplocalport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.udplocaladdress is not None:
                    return True

                if self.udplocalport is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.udp._meta import _UDP_MIB as meta
                return meta._meta_table['UDPMIB.UdpTable.UdpEntry']['meta_info']

        @property
        def _common_path(self):

            return '/UDP-MIB:UDP-MIB/UDP-MIB:udpTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.udpentry is not None:
                for child_ref in self.udpentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.udp._meta import _UDP_MIB as meta
            return meta._meta_table['UDPMIB.UdpTable']['meta_info']

    @property
    def _common_path(self):

        return '/UDP-MIB:UDP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.udp is not None and self.udp._has_data():
            return True

        if self.udp is not None and self.udp.is_presence():
            return True

        if self.udpendpointtable is not None and self.udpendpointtable._has_data():
            return True

        if self.udpendpointtable is not None and self.udpendpointtable.is_presence():
            return True

        if self.udptable is not None and self.udptable._has_data():
            return True

        if self.udptable is not None and self.udptable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.udp._meta import _UDP_MIB as meta
        return meta._meta_table['UDPMIB']['meta_info']


