""" UDP_MIB 

The MIB module for managing UDP implementations.
Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4113;
see the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class UdpMib(Entity):
    """
    
    
    .. attribute:: udp
    
    	
    	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xe.UDP_MIB.UdpMib.Udp>`
    
    .. attribute:: udpendpointtable
    
    	A table containing information about this entity's UDP endpoints on which a local application is currently accepting or sending datagrams.  The address type in this table represents the address type used for the communication, irrespective of the higher\-layer abstraction.  For example, an application using IPv6 'sockets' to communicate via IPv4 between \:\:ffff\:10.0.0.1 and \:\:ffff\:10.0.0.2 would use InetAddressType ipv4(1).  Unlike the udpTable in RFC 2013, this table also allows the representation of an application that completely specifies both local and remote addresses and ports.  A listening application is represented in three possible ways\:  1) An application that is willing to accept both IPv4    and IPv6 datagrams is represented by a    udpEndpointLocalAddressType of unknown(0) and a    udpEndpointLocalAddress of ''h (a zero\-length    octet\-string).  2) An application that is willing to accept only IPv4    or only IPv6 datagrams is represented by a    udpEndpointLocalAddressType of the appropriate    address type and a udpEndpointLocalAddress of    '0.0.0.0' or '\:\:' respectively.  3) An application that is listening for datagrams only    for a specific IP address but from any remote    system is represented by a    udpEndpointLocalAddressType of the appropriate    address type, with udpEndpointLocalAddress    specifying the local address.  In all cases where the remote is a wildcard, the udpEndpointRemoteAddressType is unknown(0), the udpEndpointRemoteAddress is ''h (a zero\-length octet\-string), and the udpEndpointRemotePort is 0.  If the operating system is demultiplexing UDP packets by remote address and port, or if the application has 'connected' the socket specifying a default remote address and port, the udpEndpointRemote\* values should be used to reflect this
    	**type**\:   :py:class:`Udpendpointtable <ydk.models.cisco_ios_xe.UDP_MIB.UdpMib.Udpendpointtable>`
    
    .. attribute:: udptable
    
    	A table containing IPv4\-specific UDP listener information.  It contains information about all local IPv4 UDP end\-points on which an application is currently accepting datagrams.  This table has been deprecated in favor of the version neutral udpEndpointTable
    	**type**\:   :py:class:`Udptable <ydk.models.cisco_ios_xe.UDP_MIB.UdpMib.Udptable>`
    
    	**status**\: deprecated
    
    

    """

    _prefix = 'UDP-MIB'
    _revision = '2005-05-20'

    def __init__(self):
        super(UdpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "UDP-MIB"
        self.yang_parent_name = "UDP-MIB"

        self.udp = UdpMib.Udp()
        self.udp.parent = self
        self._children_name_map["udp"] = "udp"
        self._children_yang_names.add("udp")

        self.udpendpointtable = UdpMib.Udpendpointtable()
        self.udpendpointtable.parent = self
        self._children_name_map["udpendpointtable"] = "udpEndpointTable"
        self._children_yang_names.add("udpEndpointTable")

        self.udptable = UdpMib.Udptable()
        self.udptable.parent = self
        self._children_name_map["udptable"] = "udpTable"
        self._children_yang_names.add("udpTable")


    class Udp(Entity):
        """
        
        
        .. attribute:: udphcindatagrams
        
        	The total number of UDP datagrams delivered to UDP users, for devices that can receive more than 1 million UDP datagrams per second.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: udphcoutdatagrams
        
        	The total number of UDP datagrams sent from this entity, for devices that can transmit more than 1 million UDP datagrams per second.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: udpindatagrams
        
        	The total number of UDP datagrams delivered to UDP users.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpinerrors
        
        	The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpnoports
        
        	The total number of received UDP datagrams for which there was no application at the destination port.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpoutdatagrams
        
        	The total number of UDP datagrams sent from this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by discontinuities in the value of sysUpTime
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'UDP-MIB'
        _revision = '2005-05-20'

        def __init__(self):
            super(UdpMib.Udp, self).__init__()

            self.yang_name = "udp"
            self.yang_parent_name = "UDP-MIB"

            self.udphcindatagrams = YLeaf(YType.uint64, "udpHCInDatagrams")

            self.udphcoutdatagrams = YLeaf(YType.uint64, "udpHCOutDatagrams")

            self.udpindatagrams = YLeaf(YType.uint32, "udpInDatagrams")

            self.udpinerrors = YLeaf(YType.uint32, "udpInErrors")

            self.udpnoports = YLeaf(YType.uint32, "udpNoPorts")

            self.udpoutdatagrams = YLeaf(YType.uint32, "udpOutDatagrams")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("udphcindatagrams",
                            "udphcoutdatagrams",
                            "udpindatagrams",
                            "udpinerrors",
                            "udpnoports",
                            "udpoutdatagrams") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(UdpMib.Udp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(UdpMib.Udp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.udphcindatagrams.is_set or
                self.udphcoutdatagrams.is_set or
                self.udpindatagrams.is_set or
                self.udpinerrors.is_set or
                self.udpnoports.is_set or
                self.udpoutdatagrams.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.udphcindatagrams.yfilter != YFilter.not_set or
                self.udphcoutdatagrams.yfilter != YFilter.not_set or
                self.udpindatagrams.yfilter != YFilter.not_set or
                self.udpinerrors.yfilter != YFilter.not_set or
                self.udpnoports.yfilter != YFilter.not_set or
                self.udpoutdatagrams.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "udp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "UDP-MIB:UDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.udphcindatagrams.is_set or self.udphcindatagrams.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udphcindatagrams.get_name_leafdata())
            if (self.udphcoutdatagrams.is_set or self.udphcoutdatagrams.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udphcoutdatagrams.get_name_leafdata())
            if (self.udpindatagrams.is_set or self.udpindatagrams.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udpindatagrams.get_name_leafdata())
            if (self.udpinerrors.is_set or self.udpinerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udpinerrors.get_name_leafdata())
            if (self.udpnoports.is_set or self.udpnoports.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udpnoports.get_name_leafdata())
            if (self.udpoutdatagrams.is_set or self.udpoutdatagrams.yfilter != YFilter.not_set):
                leaf_name_data.append(self.udpoutdatagrams.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "udpHCInDatagrams" or name == "udpHCOutDatagrams" or name == "udpInDatagrams" or name == "udpInErrors" or name == "udpNoPorts" or name == "udpOutDatagrams"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "udpHCInDatagrams"):
                self.udphcindatagrams = value
                self.udphcindatagrams.value_namespace = name_space
                self.udphcindatagrams.value_namespace_prefix = name_space_prefix
            if(value_path == "udpHCOutDatagrams"):
                self.udphcoutdatagrams = value
                self.udphcoutdatagrams.value_namespace = name_space
                self.udphcoutdatagrams.value_namespace_prefix = name_space_prefix
            if(value_path == "udpInDatagrams"):
                self.udpindatagrams = value
                self.udpindatagrams.value_namespace = name_space
                self.udpindatagrams.value_namespace_prefix = name_space_prefix
            if(value_path == "udpInErrors"):
                self.udpinerrors = value
                self.udpinerrors.value_namespace = name_space
                self.udpinerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "udpNoPorts"):
                self.udpnoports = value
                self.udpnoports.value_namespace = name_space
                self.udpnoports.value_namespace_prefix = name_space_prefix
            if(value_path == "udpOutDatagrams"):
                self.udpoutdatagrams = value
                self.udpoutdatagrams.value_namespace = name_space
                self.udpoutdatagrams.value_namespace_prefix = name_space_prefix


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
        	**type**\: list of    :py:class:`Udpentry <ydk.models.cisco_ios_xe.UDP_MIB.UdpMib.Udptable.Udpentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'UDP-MIB'
        _revision = '2005-05-20'

        def __init__(self):
            super(UdpMib.Udptable, self).__init__()

            self.yang_name = "udpTable"
            self.yang_parent_name = "UDP-MIB"

            self.udpentry = YList(self)

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
                        super(UdpMib.Udptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(UdpMib.Udptable, self).__setattr__(name, value)


        class Udpentry(Entity):
            """
            Information about a particular current UDP listener.
            
            .. attribute:: udplocaladdress  <key>
            
            	The local IP address for this UDP listener.  In the case of a UDP listener that is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: udplocalport  <key>
            
            	The local port number for this UDP listener
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'UDP-MIB'
            _revision = '2005-05-20'

            def __init__(self):
                super(UdpMib.Udptable.Udpentry, self).__init__()

                self.yang_name = "udpEntry"
                self.yang_parent_name = "udpTable"

                self.udplocaladdress = YLeaf(YType.str, "udpLocalAddress")

                self.udplocalport = YLeaf(YType.int32, "udpLocalPort")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("udplocaladdress",
                                "udplocalport") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(UdpMib.Udptable.Udpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(UdpMib.Udptable.Udpentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.udplocaladdress.is_set or
                    self.udplocalport.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.udplocaladdress.yfilter != YFilter.not_set or
                    self.udplocalport.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "udpEntry" + "[udpLocalAddress='" + self.udplocaladdress.get() + "']" + "[udpLocalPort='" + self.udplocalport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "UDP-MIB:UDP-MIB/udpTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.udplocaladdress.is_set or self.udplocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udplocaladdress.get_name_leafdata())
                if (self.udplocalport.is_set or self.udplocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udplocalport.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "udpLocalAddress" or name == "udpLocalPort"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "udpLocalAddress"):
                    self.udplocaladdress = value
                    self.udplocaladdress.value_namespace = name_space
                    self.udplocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "udpLocalPort"):
                    self.udplocalport = value
                    self.udplocalport.value_namespace = name_space
                    self.udplocalport.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.udpentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.udpentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "udpTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "UDP-MIB:UDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "udpEntry"):
                for c in self.udpentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = UdpMib.Udptable.Udpentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.udpentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "udpEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Udpendpointentry <ydk.models.cisco_ios_xe.UDP_MIB.UdpMib.Udpendpointtable.Udpendpointentry>`
        
        

        """

        _prefix = 'UDP-MIB'
        _revision = '2005-05-20'

        def __init__(self):
            super(UdpMib.Udpendpointtable, self).__init__()

            self.yang_name = "udpEndpointTable"
            self.yang_parent_name = "UDP-MIB"

            self.udpendpointentry = YList(self)

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
                        super(UdpMib.Udpendpointtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(UdpMib.Udpendpointtable, self).__setattr__(name, value)


        class Udpendpointentry(Entity):
            """
            Information about a particular current UDP endpoint.
            
            Implementers need to be aware that if the total number
            of elements (octets or sub\-identifiers) in
            udpEndpointLocalAddress and udpEndpointRemoteAddress
            exceeds 111, then OIDs of column instances in this table
            will have more than 128 sub\-identifiers and cannot be
            accessed using SNMPv1, SNMPv2c, or SNMPv3.
            
            .. attribute:: udpendpointlocaladdresstype  <key>
            
            	The address type of udpEndpointLocalAddress.  Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all local IP addresses are accepted
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: udpendpointlocaladdress  <key>
            
            	The local IP address for this UDP endpoint.  The value of this object can be represented in three  possible ways, depending on the characteristics of the listening application\:  1. For an application that is willing to accept both    IPv4 and IPv6 datagrams, the value of this object    must be ''h (a zero\-length octet\-string), with    the value of the corresponding instance of the    udpEndpointLocalAddressType object being unknown(0).  2. For an application that is willing to accept only IPv4    or only IPv6 datagrams, the value of this object    must be '0.0.0.0' or '\:\:', respectively, while the    corresponding instance of the    udpEndpointLocalAddressType object represents the    appropriate address type.  3. For an application that is listening for data    destined only to a specific IP address, the value    of this object is the specific IP address for which    this node is receiving packets, with the    corresponding instance of the    udpEndpointLocalAddressType object representing the    appropriate address type.  As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: udpendpointlocalport  <key>
            
            	The local port number for this UDP endpoint
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: udpendpointremoteaddresstype  <key>
            
            	The address type of udpEndpointRemoteAddress.  Only IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or unknown(0) if datagrams for all remote IP addresses are accepted.  Also, note that some combinations of  udpEndpointLocalAdressType and udpEndpointRemoteAddressType are not supported.  In particular, if the value of this object is not unknown(0), it is expected to always refer to the same IP version as udpEndpointLocalAddressType
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: udpendpointremoteaddress  <key>
            
            	The remote IP address for this UDP endpoint.  If datagrams from any remote system are to be accepted, this value is ''h (a zero\-length octet\-string). Otherwise, it has the type described by udpEndpointRemoteAddressType and is the address of the remote system from which datagrams are to be accepted (or to which all datagrams will be sent).  As this object is used in the index for the udpEndpointTable, implementors of this table should be careful not to create entries that would result in OIDs with more than 128 subidentifiers; else the information cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: udpendpointremoteport  <key>
            
            	The remote port number for this UDP endpoint.  If datagrams from any remote system are to be accepted, this value is zero
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: udpendpointinstance  <key>
            
            	The instance of this tuple.  This object is used to distinguish among multiple processes 'connected' to the same UDP endpoint.  For example, on a system implementing the BSD sockets interface, this would be used to support the SO\_REUSEADDR and SO\_REUSEPORT socket options
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: udpendpointprocess
            
            	The system's process ID for the process associated with this endpoint, or zero if there is no such process. This value is expected to be the same as HOST\-RESOURCES\-MIB\:\:hrSWRunIndex or SYSAPPL\-MIB\:\: sysApplElmtRunIndex for some row in the appropriate tables
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'UDP-MIB'
            _revision = '2005-05-20'

            def __init__(self):
                super(UdpMib.Udpendpointtable.Udpendpointentry, self).__init__()

                self.yang_name = "udpEndpointEntry"
                self.yang_parent_name = "udpEndpointTable"

                self.udpendpointlocaladdresstype = YLeaf(YType.enumeration, "udpEndpointLocalAddressType")

                self.udpendpointlocaladdress = YLeaf(YType.str, "udpEndpointLocalAddress")

                self.udpendpointlocalport = YLeaf(YType.uint16, "udpEndpointLocalPort")

                self.udpendpointremoteaddresstype = YLeaf(YType.enumeration, "udpEndpointRemoteAddressType")

                self.udpendpointremoteaddress = YLeaf(YType.str, "udpEndpointRemoteAddress")

                self.udpendpointremoteport = YLeaf(YType.uint16, "udpEndpointRemotePort")

                self.udpendpointinstance = YLeaf(YType.uint32, "udpEndpointInstance")

                self.udpendpointprocess = YLeaf(YType.uint32, "udpEndpointProcess")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("udpendpointlocaladdresstype",
                                "udpendpointlocaladdress",
                                "udpendpointlocalport",
                                "udpendpointremoteaddresstype",
                                "udpendpointremoteaddress",
                                "udpendpointremoteport",
                                "udpendpointinstance",
                                "udpendpointprocess") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(UdpMib.Udpendpointtable.Udpendpointentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(UdpMib.Udpendpointtable.Udpendpointentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.udpendpointlocaladdresstype.is_set or
                    self.udpendpointlocaladdress.is_set or
                    self.udpendpointlocalport.is_set or
                    self.udpendpointremoteaddresstype.is_set or
                    self.udpendpointremoteaddress.is_set or
                    self.udpendpointremoteport.is_set or
                    self.udpendpointinstance.is_set or
                    self.udpendpointprocess.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.udpendpointlocaladdresstype.yfilter != YFilter.not_set or
                    self.udpendpointlocaladdress.yfilter != YFilter.not_set or
                    self.udpendpointlocalport.yfilter != YFilter.not_set or
                    self.udpendpointremoteaddresstype.yfilter != YFilter.not_set or
                    self.udpendpointremoteaddress.yfilter != YFilter.not_set or
                    self.udpendpointremoteport.yfilter != YFilter.not_set or
                    self.udpendpointinstance.yfilter != YFilter.not_set or
                    self.udpendpointprocess.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "udpEndpointEntry" + "[udpEndpointLocalAddressType='" + self.udpendpointlocaladdresstype.get() + "']" + "[udpEndpointLocalAddress='" + self.udpendpointlocaladdress.get() + "']" + "[udpEndpointLocalPort='" + self.udpendpointlocalport.get() + "']" + "[udpEndpointRemoteAddressType='" + self.udpendpointremoteaddresstype.get() + "']" + "[udpEndpointRemoteAddress='" + self.udpendpointremoteaddress.get() + "']" + "[udpEndpointRemotePort='" + self.udpendpointremoteport.get() + "']" + "[udpEndpointInstance='" + self.udpendpointinstance.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "UDP-MIB:UDP-MIB/udpEndpointTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.udpendpointlocaladdresstype.is_set or self.udpendpointlocaladdresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointlocaladdresstype.get_name_leafdata())
                if (self.udpendpointlocaladdress.is_set or self.udpendpointlocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointlocaladdress.get_name_leafdata())
                if (self.udpendpointlocalport.is_set or self.udpendpointlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointlocalport.get_name_leafdata())
                if (self.udpendpointremoteaddresstype.is_set or self.udpendpointremoteaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointremoteaddresstype.get_name_leafdata())
                if (self.udpendpointremoteaddress.is_set or self.udpendpointremoteaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointremoteaddress.get_name_leafdata())
                if (self.udpendpointremoteport.is_set or self.udpendpointremoteport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointremoteport.get_name_leafdata())
                if (self.udpendpointinstance.is_set or self.udpendpointinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointinstance.get_name_leafdata())
                if (self.udpendpointprocess.is_set or self.udpendpointprocess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udpendpointprocess.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "udpEndpointLocalAddressType" or name == "udpEndpointLocalAddress" or name == "udpEndpointLocalPort" or name == "udpEndpointRemoteAddressType" or name == "udpEndpointRemoteAddress" or name == "udpEndpointRemotePort" or name == "udpEndpointInstance" or name == "udpEndpointProcess"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "udpEndpointLocalAddressType"):
                    self.udpendpointlocaladdresstype = value
                    self.udpendpointlocaladdresstype.value_namespace = name_space
                    self.udpendpointlocaladdresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointLocalAddress"):
                    self.udpendpointlocaladdress = value
                    self.udpendpointlocaladdress.value_namespace = name_space
                    self.udpendpointlocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointLocalPort"):
                    self.udpendpointlocalport = value
                    self.udpendpointlocalport.value_namespace = name_space
                    self.udpendpointlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointRemoteAddressType"):
                    self.udpendpointremoteaddresstype = value
                    self.udpendpointremoteaddresstype.value_namespace = name_space
                    self.udpendpointremoteaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointRemoteAddress"):
                    self.udpendpointremoteaddress = value
                    self.udpendpointremoteaddress.value_namespace = name_space
                    self.udpendpointremoteaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointRemotePort"):
                    self.udpendpointremoteport = value
                    self.udpendpointremoteport.value_namespace = name_space
                    self.udpendpointremoteport.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointInstance"):
                    self.udpendpointinstance = value
                    self.udpendpointinstance.value_namespace = name_space
                    self.udpendpointinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "udpEndpointProcess"):
                    self.udpendpointprocess = value
                    self.udpendpointprocess.value_namespace = name_space
                    self.udpendpointprocess.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.udpendpointentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.udpendpointentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "udpEndpointTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "UDP-MIB:UDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "udpEndpointEntry"):
                for c in self.udpendpointentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = UdpMib.Udpendpointtable.Udpendpointentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.udpendpointentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "udpEndpointEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.udp is not None and self.udp.has_data()) or
            (self.udpendpointtable is not None and self.udpendpointtable.has_data()) or
            (self.udptable is not None and self.udptable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.udp is not None and self.udp.has_operation()) or
            (self.udpendpointtable is not None and self.udpendpointtable.has_operation()) or
            (self.udptable is not None and self.udptable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "UDP-MIB:UDP-MIB" + path_buffer

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

        if (child_yang_name == "udp"):
            if (self.udp is None):
                self.udp = UdpMib.Udp()
                self.udp.parent = self
                self._children_name_map["udp"] = "udp"
            return self.udp

        if (child_yang_name == "udpEndpointTable"):
            if (self.udpendpointtable is None):
                self.udpendpointtable = UdpMib.Udpendpointtable()
                self.udpendpointtable.parent = self
                self._children_name_map["udpendpointtable"] = "udpEndpointTable"
            return self.udpendpointtable

        if (child_yang_name == "udpTable"):
            if (self.udptable is None):
                self.udptable = UdpMib.Udptable()
                self.udptable.parent = self
                self._children_name_map["udptable"] = "udpTable"
            return self.udptable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "udp" or name == "udpEndpointTable" or name == "udpTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = UdpMib()
        return self._top_entity

