""" RFC1213_MIB 


"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Rfc1213Mib(Entity):
    """
    
    
    .. attribute:: attable
    
    	The Address Translation tables contain the NetworkAddress to `physical' address equivalences. Some interfaces do not use translation tables for determining address equivalences (e.g., DDN\-X.25 has an algorithmic method); if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries
    	**type**\:   :py:class:`Attable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Attable>`
    
    	**status**\: obsolete
    
    .. attribute:: egp
    
    	
    	**type**\:   :py:class:`Egp <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Egp>`
    
    .. attribute:: egpneightable
    
    	The EGP neighbor table
    	**type**\:   :py:class:`Egpneightable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Egpneightable>`
    
    .. attribute:: icmp
    
    	
    	**type**\:   :py:class:`Icmp <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Icmp>`
    
    .. attribute:: iftable
    
    	A list of interface entries.  The number of entries is given by the value of ifNumber
    	**type**\:   :py:class:`Iftable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iftable>`
    
    .. attribute:: interfaces
    
    	
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Interfaces>`
    
    .. attribute:: ip
    
    	
    	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ip>`
    
    .. attribute:: ipaddrtable
    
    	The table of addressing information relevant to this entity's IP addresses
    	**type**\:   :py:class:`Ipaddrtable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ipaddrtable>`
    
    .. attribute:: ipnettomediatable
    
    	The IP Address Translation table used for mapping from IP addresses to physical addresses
    	**type**\:   :py:class:`Ipnettomediatable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ipnettomediatable>`
    
    .. attribute:: iproutetable
    
    	This entity's IP Routing table
    	**type**\:   :py:class:`Iproutetable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iproutetable>`
    
    .. attribute:: snmp
    
    	
    	**type**\:   :py:class:`Snmp <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Snmp>`
    
    .. attribute:: system
    
    	
    	**type**\:   :py:class:`System <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.System>`
    
    .. attribute:: tcp
    
    	
    	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Tcp>`
    
    .. attribute:: tcpconntable
    
    	A table containing TCP connection\-specific information
    	**type**\:   :py:class:`Tcpconntable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Tcpconntable>`
    
    .. attribute:: udp
    
    	
    	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Udp>`
    
    .. attribute:: udptable
    
    	A table containing UDP listener information
    	**type**\:   :py:class:`Udptable <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Udptable>`
    
    

    """

    _prefix = 'RFC1213-MIB'

    def __init__(self):
        super(Rfc1213Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "RFC1213-MIB"
        self.yang_parent_name = "RFC1213-MIB"

        self.attable = Rfc1213Mib.Attable()
        self.attable.parent = self
        self._children_name_map["attable"] = "atTable"
        self._children_yang_names.add("atTable")

        self.egp = Rfc1213Mib.Egp()
        self.egp.parent = self
        self._children_name_map["egp"] = "egp"
        self._children_yang_names.add("egp")

        self.egpneightable = Rfc1213Mib.Egpneightable()
        self.egpneightable.parent = self
        self._children_name_map["egpneightable"] = "egpNeighTable"
        self._children_yang_names.add("egpNeighTable")

        self.icmp = Rfc1213Mib.Icmp()
        self.icmp.parent = self
        self._children_name_map["icmp"] = "icmp"
        self._children_yang_names.add("icmp")

        self.iftable = Rfc1213Mib.Iftable()
        self.iftable.parent = self
        self._children_name_map["iftable"] = "ifTable"
        self._children_yang_names.add("ifTable")

        self.interfaces = Rfc1213Mib.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.ip = Rfc1213Mib.Ip()
        self.ip.parent = self
        self._children_name_map["ip"] = "ip"
        self._children_yang_names.add("ip")

        self.ipaddrtable = Rfc1213Mib.Ipaddrtable()
        self.ipaddrtable.parent = self
        self._children_name_map["ipaddrtable"] = "ipAddrTable"
        self._children_yang_names.add("ipAddrTable")

        self.ipnettomediatable = Rfc1213Mib.Ipnettomediatable()
        self.ipnettomediatable.parent = self
        self._children_name_map["ipnettomediatable"] = "ipNetToMediaTable"
        self._children_yang_names.add("ipNetToMediaTable")

        self.iproutetable = Rfc1213Mib.Iproutetable()
        self.iproutetable.parent = self
        self._children_name_map["iproutetable"] = "ipRouteTable"
        self._children_yang_names.add("ipRouteTable")

        self.snmp = Rfc1213Mib.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")

        self.system = Rfc1213Mib.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"
        self._children_yang_names.add("system")

        self.tcp = Rfc1213Mib.Tcp()
        self.tcp.parent = self
        self._children_name_map["tcp"] = "tcp"
        self._children_yang_names.add("tcp")

        self.tcpconntable = Rfc1213Mib.Tcpconntable()
        self.tcpconntable.parent = self
        self._children_name_map["tcpconntable"] = "tcpConnTable"
        self._children_yang_names.add("tcpConnTable")

        self.udp = Rfc1213Mib.Udp()
        self.udp.parent = self
        self._children_name_map["udp"] = "udp"
        self._children_yang_names.add("udp")

        self.udptable = Rfc1213Mib.Udptable()
        self.udptable.parent = self
        self._children_name_map["udptable"] = "udpTable"
        self._children_yang_names.add("udpTable")


    class System(Entity):
        """
        
        
        .. attribute:: syscontact
        
        	The textual identification of the contact person for this managed node, together with information on how to contact this person
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: sysdescr
        
        	A textual description of the entity.  This value should include the full name and version identification of the system's hardware type, software operating\-system, and networking software.  It is mandatory that this only contain printable ASCII characters
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: syslocation
        
        	The physical location of this node (e.g., `telephone closet, 3rd floor')
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: sysname
        
        	An administratively\-assigned name for this managed node.  By convention, this is the node's fully\-qualified domain name
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: sysobjectid
        
        	The vendor's authoritative identification of the network management subsystem contained in the entity.  This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed.  For example, if vendor `Flintstones, Inc.' was assigned the subtree 1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'
        	**type**\:  str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        .. attribute:: sysservices
        
        	A value which indicates the set of services that this entity primarily offers.  The value is a sum.  This sum initially takes the value zero, Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L \- 1) is added to the sum.  For example, a node which performs primarily routing functions would have a value of 4 (2^(3\-1)).  In contrast, a node which is a host offering application services would have a value of 72 (2^(4\-1) + 2^(7\-1)).  Note that in the context of the Internet suite of protocols, values should be calculated accordingly\:       layer  functionality          1  physical (e.g., repeaters)          2  datalink/subnetwork (e.g., bridges)          3  internet (e.g., IP gateways)          4  end\-to\-end  (e.g., IP hosts)          7  applications (e.g., mail relays)  For systems including OSI protocols, layers 5 and 6 may also be counted
        	**type**\:  int
        
        	**range:** 0..127
        
        .. attribute:: sysuptime
        
        	The time (in hundredths of a second) since the network management portion of the system was last re\-initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "RFC1213-MIB"

            self.syscontact = YLeaf(YType.str, "sysContact")

            self.sysdescr = YLeaf(YType.str, "sysDescr")

            self.syslocation = YLeaf(YType.str, "sysLocation")

            self.sysname = YLeaf(YType.str, "sysName")

            self.sysobjectid = YLeaf(YType.str, "sysObjectID")

            self.sysservices = YLeaf(YType.int32, "sysServices")

            self.sysuptime = YLeaf(YType.uint32, "sysUpTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("syscontact",
                            "sysdescr",
                            "syslocation",
                            "sysname",
                            "sysobjectid",
                            "sysservices",
                            "sysuptime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.System, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.System, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.syscontact.is_set or
                self.sysdescr.is_set or
                self.syslocation.is_set or
                self.sysname.is_set or
                self.sysobjectid.is_set or
                self.sysservices.is_set or
                self.sysuptime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.syscontact.yfilter != YFilter.not_set or
                self.sysdescr.yfilter != YFilter.not_set or
                self.syslocation.yfilter != YFilter.not_set or
                self.sysname.yfilter != YFilter.not_set or
                self.sysobjectid.yfilter != YFilter.not_set or
                self.sysservices.yfilter != YFilter.not_set or
                self.sysuptime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "system" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.syscontact.is_set or self.syscontact.yfilter != YFilter.not_set):
                leaf_name_data.append(self.syscontact.get_name_leafdata())
            if (self.sysdescr.is_set or self.sysdescr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysdescr.get_name_leafdata())
            if (self.syslocation.is_set or self.syslocation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.syslocation.get_name_leafdata())
            if (self.sysname.is_set or self.sysname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysname.get_name_leafdata())
            if (self.sysobjectid.is_set or self.sysobjectid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysobjectid.get_name_leafdata())
            if (self.sysservices.is_set or self.sysservices.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysservices.get_name_leafdata())
            if (self.sysuptime.is_set or self.sysuptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysuptime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sysContact" or name == "sysDescr" or name == "sysLocation" or name == "sysName" or name == "sysObjectID" or name == "sysServices" or name == "sysUpTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "sysContact"):
                self.syscontact = value
                self.syscontact.value_namespace = name_space
                self.syscontact.value_namespace_prefix = name_space_prefix
            if(value_path == "sysDescr"):
                self.sysdescr = value
                self.sysdescr.value_namespace = name_space
                self.sysdescr.value_namespace_prefix = name_space_prefix
            if(value_path == "sysLocation"):
                self.syslocation = value
                self.syslocation.value_namespace = name_space
                self.syslocation.value_namespace_prefix = name_space_prefix
            if(value_path == "sysName"):
                self.sysname = value
                self.sysname.value_namespace = name_space
                self.sysname.value_namespace_prefix = name_space_prefix
            if(value_path == "sysObjectID"):
                self.sysobjectid = value
                self.sysobjectid.value_namespace = name_space
                self.sysobjectid.value_namespace_prefix = name_space_prefix
            if(value_path == "sysServices"):
                self.sysservices = value
                self.sysservices.value_namespace = name_space
                self.sysservices.value_namespace_prefix = name_space_prefix
            if(value_path == "sysUpTime"):
                self.sysuptime = value
                self.sysuptime.value_namespace = name_space
                self.sysuptime.value_namespace_prefix = name_space_prefix


    class Interfaces(Entity):
        """
        
        
        .. attribute:: ifnumber
        
        	The number of network interfaces (regardless of their current state) present on this system
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "RFC1213-MIB"

            self.ifnumber = YLeaf(YType.int32, "ifNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Interfaces, self).__setattr__(name, value)

        def has_data(self):
            return self.ifnumber.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifnumber.is_set or self.ifnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifNumber"):
                self.ifnumber = value
                self.ifnumber.value_namespace = name_space
                self.ifnumber.value_namespace_prefix = name_space_prefix


    class Ip(Entity):
        """
        
        
        .. attribute:: ipdefaultttl
        
        	The default value inserted into the Time\-To\-Live field of the IP header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer protocol
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ipforwarding
        
        	The indication of whether this entity is acting as an IP gateway in respect to the forwarding of datagrams received by, but not addressed to, this entity.  IP gateways forward datagrams.  IP hosts do not (except those source\-routed via the host).  Note that for some managed nodes, this object may take on only a subset of the values possible. Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to change this object to an inappropriate value
        	**type**\:   :py:class:`Ipforwarding <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ip.Ipforwarding>`
        
        .. attribute:: ipforwdatagrams
        
        	The number of input datagrams for which this entity was not their final IP destination, as a result of which an attempt was made to find a route to forward them to that final destination. In entities which do not act as IP Gateways, this counter will include only those packets which were Source\-Routed via this entity, and the Source\- Route option processing was successful
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragcreates
        
        	The number of IP datagram fragments that have been generated as a result of fragmentation at this entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragfails
        
        	The number of IP datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragoks
        
        	The number of IP datagrams that have been successfully fragmented at this entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinaddrerrors
        
        	The number of input datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E).  For entities which are not IP Gateways and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipindelivers
        
        	The total number of input datagrams successfully delivered to IP user\-protocols (including ICMP)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipindiscards
        
        	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinhdrerrors
        
        	The number of input datagrams discarded due to errors in their IP headers, including bad checksums, version number mismatch, other format errors, time\-to\-live exceeded, errors discovered in processing their IP options, etc
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinreceives
        
        	The total number of input datagrams received from interfaces, including those received in error
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinunknownprotos
        
        	The number of locally\-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutdiscards
        
        	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutnoroutes
        
        	The number of IP datagrams discarded because no route could be found to transmit them to their destination.  Note that this counter includes any packets counted in ipForwDatagrams which meet this `no\-route' criterion.  Note that this includes any datagrams which a host cannot route because all of its default gateways are down
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutrequests
        
        	The total number of IP datagrams which local IP user\-protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipForwDatagrams
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmfails
        
        	The number of failures detected by the IP re\- assembly algorithm (for whatever reason\: timed out, errors, etc).  Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmoks
        
        	The number of IP datagrams successfully re\- assembled
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmreqds
        
        	The number of IP fragments received which needed to be reassembled at this entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmtimeout
        
        	The maximum number of seconds which received fragments are held while they are awaiting reassembly at this entity
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: iproutingdiscards
        
        	The number of routing entries which were chosen to be discarded even though they are valid.  One possible reason for discarding such an entry could be to free\-up buffer space for other routing entries
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Ip, self).__init__()

            self.yang_name = "ip"
            self.yang_parent_name = "RFC1213-MIB"

            self.ipdefaultttl = YLeaf(YType.int32, "ipDefaultTTL")

            self.ipforwarding = YLeaf(YType.enumeration, "ipForwarding")

            self.ipforwdatagrams = YLeaf(YType.uint32, "ipForwDatagrams")

            self.ipfragcreates = YLeaf(YType.uint32, "ipFragCreates")

            self.ipfragfails = YLeaf(YType.uint32, "ipFragFails")

            self.ipfragoks = YLeaf(YType.uint32, "ipFragOKs")

            self.ipinaddrerrors = YLeaf(YType.uint32, "ipInAddrErrors")

            self.ipindelivers = YLeaf(YType.uint32, "ipInDelivers")

            self.ipindiscards = YLeaf(YType.uint32, "ipInDiscards")

            self.ipinhdrerrors = YLeaf(YType.uint32, "ipInHdrErrors")

            self.ipinreceives = YLeaf(YType.uint32, "ipInReceives")

            self.ipinunknownprotos = YLeaf(YType.uint32, "ipInUnknownProtos")

            self.ipoutdiscards = YLeaf(YType.uint32, "ipOutDiscards")

            self.ipoutnoroutes = YLeaf(YType.uint32, "ipOutNoRoutes")

            self.ipoutrequests = YLeaf(YType.uint32, "ipOutRequests")

            self.ipreasmfails = YLeaf(YType.uint32, "ipReasmFails")

            self.ipreasmoks = YLeaf(YType.uint32, "ipReasmOKs")

            self.ipreasmreqds = YLeaf(YType.uint32, "ipReasmReqds")

            self.ipreasmtimeout = YLeaf(YType.int32, "ipReasmTimeout")

            self.iproutingdiscards = YLeaf(YType.uint32, "ipRoutingDiscards")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ipdefaultttl",
                            "ipforwarding",
                            "ipforwdatagrams",
                            "ipfragcreates",
                            "ipfragfails",
                            "ipfragoks",
                            "ipinaddrerrors",
                            "ipindelivers",
                            "ipindiscards",
                            "ipinhdrerrors",
                            "ipinreceives",
                            "ipinunknownprotos",
                            "ipoutdiscards",
                            "ipoutnoroutes",
                            "ipoutrequests",
                            "ipreasmfails",
                            "ipreasmoks",
                            "ipreasmreqds",
                            "ipreasmtimeout",
                            "iproutingdiscards") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.Ip, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Ip, self).__setattr__(name, value)

        class Ipforwarding(Enum):
            """
            Ipforwarding

            The indication of whether this entity is acting

            as an IP gateway in respect to the forwarding of

            datagrams received by, but not addressed to, this

            entity.  IP gateways forward datagrams.  IP hosts

            do not (except those source\-routed via the host).

            Note that for some managed nodes, this object may

            take on only a subset of the values possible.

            Accordingly, it is appropriate for an agent to

            return a `badValue' response if a management

            station attempts to change this object to an

            inappropriate value.

            .. data:: forwarding = 1

            .. data:: not_forwarding = 2

            """

            forwarding = Enum.YLeaf(1, "forwarding")

            not_forwarding = Enum.YLeaf(2, "not-forwarding")


        def has_data(self):
            return (
                self.ipdefaultttl.is_set or
                self.ipforwarding.is_set or
                self.ipforwdatagrams.is_set or
                self.ipfragcreates.is_set or
                self.ipfragfails.is_set or
                self.ipfragoks.is_set or
                self.ipinaddrerrors.is_set or
                self.ipindelivers.is_set or
                self.ipindiscards.is_set or
                self.ipinhdrerrors.is_set or
                self.ipinreceives.is_set or
                self.ipinunknownprotos.is_set or
                self.ipoutdiscards.is_set or
                self.ipoutnoroutes.is_set or
                self.ipoutrequests.is_set or
                self.ipreasmfails.is_set or
                self.ipreasmoks.is_set or
                self.ipreasmreqds.is_set or
                self.ipreasmtimeout.is_set or
                self.iproutingdiscards.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ipdefaultttl.yfilter != YFilter.not_set or
                self.ipforwarding.yfilter != YFilter.not_set or
                self.ipforwdatagrams.yfilter != YFilter.not_set or
                self.ipfragcreates.yfilter != YFilter.not_set or
                self.ipfragfails.yfilter != YFilter.not_set or
                self.ipfragoks.yfilter != YFilter.not_set or
                self.ipinaddrerrors.yfilter != YFilter.not_set or
                self.ipindelivers.yfilter != YFilter.not_set or
                self.ipindiscards.yfilter != YFilter.not_set or
                self.ipinhdrerrors.yfilter != YFilter.not_set or
                self.ipinreceives.yfilter != YFilter.not_set or
                self.ipinunknownprotos.yfilter != YFilter.not_set or
                self.ipoutdiscards.yfilter != YFilter.not_set or
                self.ipoutnoroutes.yfilter != YFilter.not_set or
                self.ipoutrequests.yfilter != YFilter.not_set or
                self.ipreasmfails.yfilter != YFilter.not_set or
                self.ipreasmoks.yfilter != YFilter.not_set or
                self.ipreasmreqds.yfilter != YFilter.not_set or
                self.ipreasmtimeout.yfilter != YFilter.not_set or
                self.iproutingdiscards.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ip" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ipdefaultttl.is_set or self.ipdefaultttl.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipdefaultttl.get_name_leafdata())
            if (self.ipforwarding.is_set or self.ipforwarding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipforwarding.get_name_leafdata())
            if (self.ipforwdatagrams.is_set or self.ipforwdatagrams.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipforwdatagrams.get_name_leafdata())
            if (self.ipfragcreates.is_set or self.ipfragcreates.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipfragcreates.get_name_leafdata())
            if (self.ipfragfails.is_set or self.ipfragfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipfragfails.get_name_leafdata())
            if (self.ipfragoks.is_set or self.ipfragoks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipfragoks.get_name_leafdata())
            if (self.ipinaddrerrors.is_set or self.ipinaddrerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinaddrerrors.get_name_leafdata())
            if (self.ipindelivers.is_set or self.ipindelivers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipindelivers.get_name_leafdata())
            if (self.ipindiscards.is_set or self.ipindiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipindiscards.get_name_leafdata())
            if (self.ipinhdrerrors.is_set or self.ipinhdrerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinhdrerrors.get_name_leafdata())
            if (self.ipinreceives.is_set or self.ipinreceives.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinreceives.get_name_leafdata())
            if (self.ipinunknownprotos.is_set or self.ipinunknownprotos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinunknownprotos.get_name_leafdata())
            if (self.ipoutdiscards.is_set or self.ipoutdiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipoutdiscards.get_name_leafdata())
            if (self.ipoutnoroutes.is_set or self.ipoutnoroutes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipoutnoroutes.get_name_leafdata())
            if (self.ipoutrequests.is_set or self.ipoutrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipoutrequests.get_name_leafdata())
            if (self.ipreasmfails.is_set or self.ipreasmfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmfails.get_name_leafdata())
            if (self.ipreasmoks.is_set or self.ipreasmoks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmoks.get_name_leafdata())
            if (self.ipreasmreqds.is_set or self.ipreasmreqds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmreqds.get_name_leafdata())
            if (self.ipreasmtimeout.is_set or self.ipreasmtimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmtimeout.get_name_leafdata())
            if (self.iproutingdiscards.is_set or self.iproutingdiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.iproutingdiscards.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipDefaultTTL" or name == "ipForwarding" or name == "ipForwDatagrams" or name == "ipFragCreates" or name == "ipFragFails" or name == "ipFragOKs" or name == "ipInAddrErrors" or name == "ipInDelivers" or name == "ipInDiscards" or name == "ipInHdrErrors" or name == "ipInReceives" or name == "ipInUnknownProtos" or name == "ipOutDiscards" or name == "ipOutNoRoutes" or name == "ipOutRequests" or name == "ipReasmFails" or name == "ipReasmOKs" or name == "ipReasmReqds" or name == "ipReasmTimeout" or name == "ipRoutingDiscards"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ipDefaultTTL"):
                self.ipdefaultttl = value
                self.ipdefaultttl.value_namespace = name_space
                self.ipdefaultttl.value_namespace_prefix = name_space_prefix
            if(value_path == "ipForwarding"):
                self.ipforwarding = value
                self.ipforwarding.value_namespace = name_space
                self.ipforwarding.value_namespace_prefix = name_space_prefix
            if(value_path == "ipForwDatagrams"):
                self.ipforwdatagrams = value
                self.ipforwdatagrams.value_namespace = name_space
                self.ipforwdatagrams.value_namespace_prefix = name_space_prefix
            if(value_path == "ipFragCreates"):
                self.ipfragcreates = value
                self.ipfragcreates.value_namespace = name_space
                self.ipfragcreates.value_namespace_prefix = name_space_prefix
            if(value_path == "ipFragFails"):
                self.ipfragfails = value
                self.ipfragfails.value_namespace = name_space
                self.ipfragfails.value_namespace_prefix = name_space_prefix
            if(value_path == "ipFragOKs"):
                self.ipfragoks = value
                self.ipfragoks.value_namespace = name_space
                self.ipfragoks.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInAddrErrors"):
                self.ipinaddrerrors = value
                self.ipinaddrerrors.value_namespace = name_space
                self.ipinaddrerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInDelivers"):
                self.ipindelivers = value
                self.ipindelivers.value_namespace = name_space
                self.ipindelivers.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInDiscards"):
                self.ipindiscards = value
                self.ipindiscards.value_namespace = name_space
                self.ipindiscards.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInHdrErrors"):
                self.ipinhdrerrors = value
                self.ipinhdrerrors.value_namespace = name_space
                self.ipinhdrerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInReceives"):
                self.ipinreceives = value
                self.ipinreceives.value_namespace = name_space
                self.ipinreceives.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInUnknownProtos"):
                self.ipinunknownprotos = value
                self.ipinunknownprotos.value_namespace = name_space
                self.ipinunknownprotos.value_namespace_prefix = name_space_prefix
            if(value_path == "ipOutDiscards"):
                self.ipoutdiscards = value
                self.ipoutdiscards.value_namespace = name_space
                self.ipoutdiscards.value_namespace_prefix = name_space_prefix
            if(value_path == "ipOutNoRoutes"):
                self.ipoutnoroutes = value
                self.ipoutnoroutes.value_namespace = name_space
                self.ipoutnoroutes.value_namespace_prefix = name_space_prefix
            if(value_path == "ipOutRequests"):
                self.ipoutrequests = value
                self.ipoutrequests.value_namespace = name_space
                self.ipoutrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmFails"):
                self.ipreasmfails = value
                self.ipreasmfails.value_namespace = name_space
                self.ipreasmfails.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmOKs"):
                self.ipreasmoks = value
                self.ipreasmoks.value_namespace = name_space
                self.ipreasmoks.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmReqds"):
                self.ipreasmreqds = value
                self.ipreasmreqds.value_namespace = name_space
                self.ipreasmreqds.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmTimeout"):
                self.ipreasmtimeout = value
                self.ipreasmtimeout.value_namespace = name_space
                self.ipreasmtimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "ipRoutingDiscards"):
                self.iproutingdiscards = value
                self.iproutingdiscards.value_namespace = name_space
                self.iproutingdiscards.value_namespace_prefix = name_space_prefix


    class Icmp(Entity):
        """
        
        
        .. attribute:: icmpinaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinaddrmasks
        
        	The number of ICMP Address Mask Request messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpindestunreachs
        
        	The number of ICMP Destination Unreachable messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinechoreps
        
        	The number of ICMP Echo Reply messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinechos
        
        	The number of ICMP Echo (request) messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinerrors
        
        	The number of ICMP messages which the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinmsgs
        
        	The total number of ICMP messages which the entity received.  Note that this counter includes all those counted by icmpInErrors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinparmprobs
        
        	The number of ICMP Parameter Problem messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinredirects
        
        	The number of ICMP Redirect messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinsrcquenchs
        
        	The number of ICMP Source Quench messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimeexcds
        
        	The number of ICMP Time Exceeded messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimestampreps
        
        	The number of ICMP Timestamp Reply messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimestamps
        
        	The number of ICMP Timestamp (request) messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutaddrmasks
        
        	The number of ICMP Address Mask Request messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutdestunreachs
        
        	The number of ICMP Destination Unreachable messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutechoreps
        
        	The number of ICMP Echo Reply messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutechos
        
        	The number of ICMP Echo (request) messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouterrors
        
        	The number of ICMP messages which this entity did not send due to problems discovered within ICMP such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer such as the inability of IP to route the resultant datagram.  In some implementations there may be no types of error which contribute to this counter's value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutmsgs
        
        	The total number of ICMP messages which this entity attempted to send.  Note that this counter includes all those counted by icmpOutErrors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutparmprobs
        
        	The number of ICMP Parameter Problem messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutredirects
        
        	The number of ICMP Redirect messages sent.  For a host, this object will always be zero, since hosts do not send redirects
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutsrcquenchs
        
        	The number of ICMP Source Quench messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimeexcds
        
        	The number of ICMP Time Exceeded messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimestampreps
        
        	The number of ICMP Timestamp Reply messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimestamps
        
        	The number of ICMP Timestamp (request) messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Icmp, self).__init__()

            self.yang_name = "icmp"
            self.yang_parent_name = "RFC1213-MIB"

            self.icmpinaddrmaskreps = YLeaf(YType.uint32, "icmpInAddrMaskReps")

            self.icmpinaddrmasks = YLeaf(YType.uint32, "icmpInAddrMasks")

            self.icmpindestunreachs = YLeaf(YType.uint32, "icmpInDestUnreachs")

            self.icmpinechoreps = YLeaf(YType.uint32, "icmpInEchoReps")

            self.icmpinechos = YLeaf(YType.uint32, "icmpInEchos")

            self.icmpinerrors = YLeaf(YType.uint32, "icmpInErrors")

            self.icmpinmsgs = YLeaf(YType.uint32, "icmpInMsgs")

            self.icmpinparmprobs = YLeaf(YType.uint32, "icmpInParmProbs")

            self.icmpinredirects = YLeaf(YType.uint32, "icmpInRedirects")

            self.icmpinsrcquenchs = YLeaf(YType.uint32, "icmpInSrcQuenchs")

            self.icmpintimeexcds = YLeaf(YType.uint32, "icmpInTimeExcds")

            self.icmpintimestampreps = YLeaf(YType.uint32, "icmpInTimestampReps")

            self.icmpintimestamps = YLeaf(YType.uint32, "icmpInTimestamps")

            self.icmpoutaddrmaskreps = YLeaf(YType.uint32, "icmpOutAddrMaskReps")

            self.icmpoutaddrmasks = YLeaf(YType.uint32, "icmpOutAddrMasks")

            self.icmpoutdestunreachs = YLeaf(YType.uint32, "icmpOutDestUnreachs")

            self.icmpoutechoreps = YLeaf(YType.uint32, "icmpOutEchoReps")

            self.icmpoutechos = YLeaf(YType.uint32, "icmpOutEchos")

            self.icmpouterrors = YLeaf(YType.uint32, "icmpOutErrors")

            self.icmpoutmsgs = YLeaf(YType.uint32, "icmpOutMsgs")

            self.icmpoutparmprobs = YLeaf(YType.uint32, "icmpOutParmProbs")

            self.icmpoutredirects = YLeaf(YType.uint32, "icmpOutRedirects")

            self.icmpoutsrcquenchs = YLeaf(YType.uint32, "icmpOutSrcQuenchs")

            self.icmpouttimeexcds = YLeaf(YType.uint32, "icmpOutTimeExcds")

            self.icmpouttimestampreps = YLeaf(YType.uint32, "icmpOutTimestampReps")

            self.icmpouttimestamps = YLeaf(YType.uint32, "icmpOutTimestamps")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("icmpinaddrmaskreps",
                            "icmpinaddrmasks",
                            "icmpindestunreachs",
                            "icmpinechoreps",
                            "icmpinechos",
                            "icmpinerrors",
                            "icmpinmsgs",
                            "icmpinparmprobs",
                            "icmpinredirects",
                            "icmpinsrcquenchs",
                            "icmpintimeexcds",
                            "icmpintimestampreps",
                            "icmpintimestamps",
                            "icmpoutaddrmaskreps",
                            "icmpoutaddrmasks",
                            "icmpoutdestunreachs",
                            "icmpoutechoreps",
                            "icmpoutechos",
                            "icmpouterrors",
                            "icmpoutmsgs",
                            "icmpoutparmprobs",
                            "icmpoutredirects",
                            "icmpoutsrcquenchs",
                            "icmpouttimeexcds",
                            "icmpouttimestampreps",
                            "icmpouttimestamps") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.Icmp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Icmp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.icmpinaddrmaskreps.is_set or
                self.icmpinaddrmasks.is_set or
                self.icmpindestunreachs.is_set or
                self.icmpinechoreps.is_set or
                self.icmpinechos.is_set or
                self.icmpinerrors.is_set or
                self.icmpinmsgs.is_set or
                self.icmpinparmprobs.is_set or
                self.icmpinredirects.is_set or
                self.icmpinsrcquenchs.is_set or
                self.icmpintimeexcds.is_set or
                self.icmpintimestampreps.is_set or
                self.icmpintimestamps.is_set or
                self.icmpoutaddrmaskreps.is_set or
                self.icmpoutaddrmasks.is_set or
                self.icmpoutdestunreachs.is_set or
                self.icmpoutechoreps.is_set or
                self.icmpoutechos.is_set or
                self.icmpouterrors.is_set or
                self.icmpoutmsgs.is_set or
                self.icmpoutparmprobs.is_set or
                self.icmpoutredirects.is_set or
                self.icmpoutsrcquenchs.is_set or
                self.icmpouttimeexcds.is_set or
                self.icmpouttimestampreps.is_set or
                self.icmpouttimestamps.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.icmpinaddrmaskreps.yfilter != YFilter.not_set or
                self.icmpinaddrmasks.yfilter != YFilter.not_set or
                self.icmpindestunreachs.yfilter != YFilter.not_set or
                self.icmpinechoreps.yfilter != YFilter.not_set or
                self.icmpinechos.yfilter != YFilter.not_set or
                self.icmpinerrors.yfilter != YFilter.not_set or
                self.icmpinmsgs.yfilter != YFilter.not_set or
                self.icmpinparmprobs.yfilter != YFilter.not_set or
                self.icmpinredirects.yfilter != YFilter.not_set or
                self.icmpinsrcquenchs.yfilter != YFilter.not_set or
                self.icmpintimeexcds.yfilter != YFilter.not_set or
                self.icmpintimestampreps.yfilter != YFilter.not_set or
                self.icmpintimestamps.yfilter != YFilter.not_set or
                self.icmpoutaddrmaskreps.yfilter != YFilter.not_set or
                self.icmpoutaddrmasks.yfilter != YFilter.not_set or
                self.icmpoutdestunreachs.yfilter != YFilter.not_set or
                self.icmpoutechoreps.yfilter != YFilter.not_set or
                self.icmpoutechos.yfilter != YFilter.not_set or
                self.icmpouterrors.yfilter != YFilter.not_set or
                self.icmpoutmsgs.yfilter != YFilter.not_set or
                self.icmpoutparmprobs.yfilter != YFilter.not_set or
                self.icmpoutredirects.yfilter != YFilter.not_set or
                self.icmpoutsrcquenchs.yfilter != YFilter.not_set or
                self.icmpouttimeexcds.yfilter != YFilter.not_set or
                self.icmpouttimestampreps.yfilter != YFilter.not_set or
                self.icmpouttimestamps.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "icmp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.icmpinaddrmaskreps.is_set or self.icmpinaddrmaskreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinaddrmaskreps.get_name_leafdata())
            if (self.icmpinaddrmasks.is_set or self.icmpinaddrmasks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinaddrmasks.get_name_leafdata())
            if (self.icmpindestunreachs.is_set or self.icmpindestunreachs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpindestunreachs.get_name_leafdata())
            if (self.icmpinechoreps.is_set or self.icmpinechoreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinechoreps.get_name_leafdata())
            if (self.icmpinechos.is_set or self.icmpinechos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinechos.get_name_leafdata())
            if (self.icmpinerrors.is_set or self.icmpinerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinerrors.get_name_leafdata())
            if (self.icmpinmsgs.is_set or self.icmpinmsgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinmsgs.get_name_leafdata())
            if (self.icmpinparmprobs.is_set or self.icmpinparmprobs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinparmprobs.get_name_leafdata())
            if (self.icmpinredirects.is_set or self.icmpinredirects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinredirects.get_name_leafdata())
            if (self.icmpinsrcquenchs.is_set or self.icmpinsrcquenchs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinsrcquenchs.get_name_leafdata())
            if (self.icmpintimeexcds.is_set or self.icmpintimeexcds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpintimeexcds.get_name_leafdata())
            if (self.icmpintimestampreps.is_set or self.icmpintimestampreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpintimestampreps.get_name_leafdata())
            if (self.icmpintimestamps.is_set or self.icmpintimestamps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpintimestamps.get_name_leafdata())
            if (self.icmpoutaddrmaskreps.is_set or self.icmpoutaddrmaskreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutaddrmaskreps.get_name_leafdata())
            if (self.icmpoutaddrmasks.is_set or self.icmpoutaddrmasks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutaddrmasks.get_name_leafdata())
            if (self.icmpoutdestunreachs.is_set or self.icmpoutdestunreachs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutdestunreachs.get_name_leafdata())
            if (self.icmpoutechoreps.is_set or self.icmpoutechoreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutechoreps.get_name_leafdata())
            if (self.icmpoutechos.is_set or self.icmpoutechos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutechos.get_name_leafdata())
            if (self.icmpouterrors.is_set or self.icmpouterrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouterrors.get_name_leafdata())
            if (self.icmpoutmsgs.is_set or self.icmpoutmsgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutmsgs.get_name_leafdata())
            if (self.icmpoutparmprobs.is_set or self.icmpoutparmprobs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutparmprobs.get_name_leafdata())
            if (self.icmpoutredirects.is_set or self.icmpoutredirects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutredirects.get_name_leafdata())
            if (self.icmpoutsrcquenchs.is_set or self.icmpoutsrcquenchs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutsrcquenchs.get_name_leafdata())
            if (self.icmpouttimeexcds.is_set or self.icmpouttimeexcds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouttimeexcds.get_name_leafdata())
            if (self.icmpouttimestampreps.is_set or self.icmpouttimestampreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouttimestampreps.get_name_leafdata())
            if (self.icmpouttimestamps.is_set or self.icmpouttimestamps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouttimestamps.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "icmpInAddrMaskReps" or name == "icmpInAddrMasks" or name == "icmpInDestUnreachs" or name == "icmpInEchoReps" or name == "icmpInEchos" or name == "icmpInErrors" or name == "icmpInMsgs" or name == "icmpInParmProbs" or name == "icmpInRedirects" or name == "icmpInSrcQuenchs" or name == "icmpInTimeExcds" or name == "icmpInTimestampReps" or name == "icmpInTimestamps" or name == "icmpOutAddrMaskReps" or name == "icmpOutAddrMasks" or name == "icmpOutDestUnreachs" or name == "icmpOutEchoReps" or name == "icmpOutEchos" or name == "icmpOutErrors" or name == "icmpOutMsgs" or name == "icmpOutParmProbs" or name == "icmpOutRedirects" or name == "icmpOutSrcQuenchs" or name == "icmpOutTimeExcds" or name == "icmpOutTimestampReps" or name == "icmpOutTimestamps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "icmpInAddrMaskReps"):
                self.icmpinaddrmaskreps = value
                self.icmpinaddrmaskreps.value_namespace = name_space
                self.icmpinaddrmaskreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInAddrMasks"):
                self.icmpinaddrmasks = value
                self.icmpinaddrmasks.value_namespace = name_space
                self.icmpinaddrmasks.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInDestUnreachs"):
                self.icmpindestunreachs = value
                self.icmpindestunreachs.value_namespace = name_space
                self.icmpindestunreachs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInEchoReps"):
                self.icmpinechoreps = value
                self.icmpinechoreps.value_namespace = name_space
                self.icmpinechoreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInEchos"):
                self.icmpinechos = value
                self.icmpinechos.value_namespace = name_space
                self.icmpinechos.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInErrors"):
                self.icmpinerrors = value
                self.icmpinerrors.value_namespace = name_space
                self.icmpinerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInMsgs"):
                self.icmpinmsgs = value
                self.icmpinmsgs.value_namespace = name_space
                self.icmpinmsgs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInParmProbs"):
                self.icmpinparmprobs = value
                self.icmpinparmprobs.value_namespace = name_space
                self.icmpinparmprobs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInRedirects"):
                self.icmpinredirects = value
                self.icmpinredirects.value_namespace = name_space
                self.icmpinredirects.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInSrcQuenchs"):
                self.icmpinsrcquenchs = value
                self.icmpinsrcquenchs.value_namespace = name_space
                self.icmpinsrcquenchs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInTimeExcds"):
                self.icmpintimeexcds = value
                self.icmpintimeexcds.value_namespace = name_space
                self.icmpintimeexcds.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInTimestampReps"):
                self.icmpintimestampreps = value
                self.icmpintimestampreps.value_namespace = name_space
                self.icmpintimestampreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInTimestamps"):
                self.icmpintimestamps = value
                self.icmpintimestamps.value_namespace = name_space
                self.icmpintimestamps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutAddrMaskReps"):
                self.icmpoutaddrmaskreps = value
                self.icmpoutaddrmaskreps.value_namespace = name_space
                self.icmpoutaddrmaskreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutAddrMasks"):
                self.icmpoutaddrmasks = value
                self.icmpoutaddrmasks.value_namespace = name_space
                self.icmpoutaddrmasks.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutDestUnreachs"):
                self.icmpoutdestunreachs = value
                self.icmpoutdestunreachs.value_namespace = name_space
                self.icmpoutdestunreachs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutEchoReps"):
                self.icmpoutechoreps = value
                self.icmpoutechoreps.value_namespace = name_space
                self.icmpoutechoreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutEchos"):
                self.icmpoutechos = value
                self.icmpoutechos.value_namespace = name_space
                self.icmpoutechos.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutErrors"):
                self.icmpouterrors = value
                self.icmpouterrors.value_namespace = name_space
                self.icmpouterrors.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutMsgs"):
                self.icmpoutmsgs = value
                self.icmpoutmsgs.value_namespace = name_space
                self.icmpoutmsgs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutParmProbs"):
                self.icmpoutparmprobs = value
                self.icmpoutparmprobs.value_namespace = name_space
                self.icmpoutparmprobs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutRedirects"):
                self.icmpoutredirects = value
                self.icmpoutredirects.value_namespace = name_space
                self.icmpoutredirects.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutSrcQuenchs"):
                self.icmpoutsrcquenchs = value
                self.icmpoutsrcquenchs.value_namespace = name_space
                self.icmpoutsrcquenchs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutTimeExcds"):
                self.icmpouttimeexcds = value
                self.icmpouttimeexcds.value_namespace = name_space
                self.icmpouttimeexcds.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutTimestampReps"):
                self.icmpouttimestampreps = value
                self.icmpouttimestampreps.value_namespace = name_space
                self.icmpouttimestampreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutTimestamps"):
                self.icmpouttimestamps = value
                self.icmpouttimestamps.value_namespace = name_space
                self.icmpouttimestamps.value_namespace_prefix = name_space_prefix


    class Tcp(Entity):
        """
        
        
        .. attribute:: tcpactiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-SENT state from the CLOSED state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpattemptfails
        
        	The number of times TCP connections have made a direct transition to the CLOSED state from either the SYN\-SENT state or the SYN\-RCVD state, plus the number of times TCP connections have made a direct transition to the LISTEN state from the SYN\-RCVD state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpcurrestab
        
        	The number of TCP connections for which the current state is either ESTABLISHED or CLOSE\- WAIT
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpestabresets
        
        	The number of times TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE\-WAIT state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinerrs
        
        	The total number of segments received in error (e.g., bad TCP checksums)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received on currently established connections
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpmaxconn
        
        	The limit on the total number of TCP connections the entity can support.  In entities where the maximum number of connections is dynamic, this object should contain the value \-1
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcpoutrsts
        
        	The number of TCP segments sent containing the RST flag
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcppassiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-RCVD state from the LISTEN state
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpretranssegs
        
        	The total number of segments retransmitted \- that is, the number of TCP segments transmitted containing one or more previously transmitted octets
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcprtoalgorithm
        
        	The algorithm used to determine the timeout value used for retransmitting unacknowledged octets
        	**type**\:   :py:class:`Tcprtoalgorithm <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Tcp.Tcprtoalgorithm>`
        
        .. attribute:: tcprtomax
        
        	The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds.  More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout.  In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the UBOUND quantity described in RFC 793
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcprtomin
        
        	The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds.  More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout.  In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the LBOUND quantity described in RFC 793
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Tcp, self).__init__()

            self.yang_name = "tcp"
            self.yang_parent_name = "RFC1213-MIB"

            self.tcpactiveopens = YLeaf(YType.uint32, "tcpActiveOpens")

            self.tcpattemptfails = YLeaf(YType.uint32, "tcpAttemptFails")

            self.tcpcurrestab = YLeaf(YType.uint32, "tcpCurrEstab")

            self.tcpestabresets = YLeaf(YType.uint32, "tcpEstabResets")

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
                        super(Rfc1213Mib.Tcp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Tcp, self).__setattr__(name, value)

        class Tcprtoalgorithm(Enum):
            """
            Tcprtoalgorithm

            The algorithm used to determine the timeout value

            used for retransmitting unacknowledged octets.

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
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
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
            if(name == "tcpActiveOpens" or name == "tcpAttemptFails" or name == "tcpCurrEstab" or name == "tcpEstabResets" or name == "tcpInErrs" or name == "tcpInSegs" or name == "tcpMaxConn" or name == "tcpOutRsts" or name == "tcpOutSegs" or name == "tcpPassiveOpens" or name == "tcpRetransSegs" or name == "tcpRtoAlgorithm" or name == "tcpRtoMax" or name == "tcpRtoMin"):
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


    class Udp(Entity):
        """
        
        
        .. attribute:: udpindatagrams
        
        	The total number of UDP datagrams delivered to UDP users
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpinerrors
        
        	The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpnoports
        
        	The total number of received UDP datagrams for which there was no application at the destination port
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpoutdatagrams
        
        	The total number of UDP datagrams sent from this entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Udp, self).__init__()

            self.yang_name = "udp"
            self.yang_parent_name = "RFC1213-MIB"

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
                if name in ("udpindatagrams",
                            "udpinerrors",
                            "udpnoports",
                            "udpoutdatagrams") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.Udp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Udp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.udpindatagrams.is_set or
                self.udpinerrors.is_set or
                self.udpnoports.is_set or
                self.udpoutdatagrams.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
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
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
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
            if(name == "udpInDatagrams" or name == "udpInErrors" or name == "udpNoPorts" or name == "udpOutDatagrams"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
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


    class Egp(Entity):
        """
        
        
        .. attribute:: egpas
        
        	The autonomous system number of this EGP entity
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: egpinerrors
        
        	The number of EGP messages received that proved to be in error
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpinmsgs
        
        	The number of EGP messages received without error
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpouterrors
        
        	The number of locally generated EGP messages not sent due to resource limitations within an EGP entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpoutmsgs
        
        	The total number of locally generated EGP messages
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Egp, self).__init__()

            self.yang_name = "egp"
            self.yang_parent_name = "RFC1213-MIB"

            self.egpas = YLeaf(YType.int32, "egpAs")

            self.egpinerrors = YLeaf(YType.uint32, "egpInErrors")

            self.egpinmsgs = YLeaf(YType.uint32, "egpInMsgs")

            self.egpouterrors = YLeaf(YType.uint32, "egpOutErrors")

            self.egpoutmsgs = YLeaf(YType.uint32, "egpOutMsgs")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("egpas",
                            "egpinerrors",
                            "egpinmsgs",
                            "egpouterrors",
                            "egpoutmsgs") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.Egp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Egp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.egpas.is_set or
                self.egpinerrors.is_set or
                self.egpinmsgs.is_set or
                self.egpouterrors.is_set or
                self.egpoutmsgs.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.egpas.yfilter != YFilter.not_set or
                self.egpinerrors.yfilter != YFilter.not_set or
                self.egpinmsgs.yfilter != YFilter.not_set or
                self.egpouterrors.yfilter != YFilter.not_set or
                self.egpoutmsgs.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "egp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.egpas.is_set or self.egpas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.egpas.get_name_leafdata())
            if (self.egpinerrors.is_set or self.egpinerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.egpinerrors.get_name_leafdata())
            if (self.egpinmsgs.is_set or self.egpinmsgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.egpinmsgs.get_name_leafdata())
            if (self.egpouterrors.is_set or self.egpouterrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.egpouterrors.get_name_leafdata())
            if (self.egpoutmsgs.is_set or self.egpoutmsgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.egpoutmsgs.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "egpAs" or name == "egpInErrors" or name == "egpInMsgs" or name == "egpOutErrors" or name == "egpOutMsgs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "egpAs"):
                self.egpas = value
                self.egpas.value_namespace = name_space
                self.egpas.value_namespace_prefix = name_space_prefix
            if(value_path == "egpInErrors"):
                self.egpinerrors = value
                self.egpinerrors.value_namespace = name_space
                self.egpinerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "egpInMsgs"):
                self.egpinmsgs = value
                self.egpinmsgs.value_namespace = name_space
                self.egpinmsgs.value_namespace_prefix = name_space_prefix
            if(value_path == "egpOutErrors"):
                self.egpouterrors = value
                self.egpouterrors.value_namespace = name_space
                self.egpouterrors.value_namespace_prefix = name_space_prefix
            if(value_path == "egpOutMsgs"):
                self.egpoutmsgs = value
                self.egpoutmsgs.value_namespace = name_space
                self.egpoutmsgs.value_namespace_prefix = name_space_prefix


    class Snmp(Entity):
        """
        
        
        .. attribute:: snmpenableauthentraps
        
        	Indicates whether the SNMP agent process is permitted to generate authentication\-failure traps.  The value of this object overrides any configuration information; as such, it provides a means whereby all authentication\-failure traps may be disabled.  Note that it is strongly recommended that this object be stored in non\-volatile memory so that it remains constant between re\-initializations of the network management system
        	**type**\:   :py:class:`Snmpenableauthentraps <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Snmp.Snmpenableauthentraps>`
        
        .. attribute:: snmpinasnparseerrs
        
        	The total number of ASN.1 or BER errors encountered by the SNMP protocol entity when decoding received SNMP Messages
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunitynames
        
        	The total number of SNMP Messages delivered to the SNMP protocol entity which used a SNMP community name not known to said entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunityuses
        
        	The total number of SNMP Messages delivered to the SNMP protocol entity which represented an SNMP operation which was not allowed by the SNMP community named in the Message
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadvalues
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `badValue'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadversions
        
        	The total number of SNMP Messages which were delivered to the SNMP protocol entity and were for an unsupported SNMP version
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingenerrs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `genErr'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinnosuchnames
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `noSuchName'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinpkts
        
        	The total number of Messages delivered to the SNMP entity from the transport service
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinreadonlys
        
        	The total number valid SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `readOnly'.  It should be noted that it is a protocol error to generate an SNMP PDU which contains the value `readOnly' in the error\-status field, as such this object is provided as a means of detecting incorrect implementations of the SNMP
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintoobigs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `tooBig'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintotalreqvars
        
        	The total number of MIB objects which have been retrieved successfully by the SNMP protocol entity as the result of receiving valid SNMP Get\-Request and Get\-Next PDUs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintotalsetvars
        
        	The total number of MIB objects which have been altered successfully by the SNMP protocol entity as the result of receiving valid SNMP Set\-Request PDUs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintraps
        
        	The total number of SNMP Trap PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutbadvalues
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `badValue'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgenerrs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `genErr'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutnosuchnames
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status is `noSuchName'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutpkts
        
        	The total number of SNMP Messages which were passed from the SNMP protocol entity to the transport service
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpouttoobigs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `tooBig.'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpouttraps
        
        	The total number of SNMP Trap PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "RFC1213-MIB"

            self.snmpenableauthentraps = YLeaf(YType.enumeration, "snmpEnableAuthenTraps")

            self.snmpinasnparseerrs = YLeaf(YType.uint32, "snmpInASNParseErrs")

            self.snmpinbadcommunitynames = YLeaf(YType.uint32, "snmpInBadCommunityNames")

            self.snmpinbadcommunityuses = YLeaf(YType.uint32, "snmpInBadCommunityUses")

            self.snmpinbadvalues = YLeaf(YType.uint32, "snmpInBadValues")

            self.snmpinbadversions = YLeaf(YType.uint32, "snmpInBadVersions")

            self.snmpingenerrs = YLeaf(YType.uint32, "snmpInGenErrs")

            self.snmpingetnexts = YLeaf(YType.uint32, "snmpInGetNexts")

            self.snmpingetrequests = YLeaf(YType.uint32, "snmpInGetRequests")

            self.snmpingetresponses = YLeaf(YType.uint32, "snmpInGetResponses")

            self.snmpinnosuchnames = YLeaf(YType.uint32, "snmpInNoSuchNames")

            self.snmpinpkts = YLeaf(YType.uint32, "snmpInPkts")

            self.snmpinreadonlys = YLeaf(YType.uint32, "snmpInReadOnlys")

            self.snmpinsetrequests = YLeaf(YType.uint32, "snmpInSetRequests")

            self.snmpintoobigs = YLeaf(YType.uint32, "snmpInTooBigs")

            self.snmpintotalreqvars = YLeaf(YType.uint32, "snmpInTotalReqVars")

            self.snmpintotalsetvars = YLeaf(YType.uint32, "snmpInTotalSetVars")

            self.snmpintraps = YLeaf(YType.uint32, "snmpInTraps")

            self.snmpoutbadvalues = YLeaf(YType.uint32, "snmpOutBadValues")

            self.snmpoutgenerrs = YLeaf(YType.uint32, "snmpOutGenErrs")

            self.snmpoutgetnexts = YLeaf(YType.uint32, "snmpOutGetNexts")

            self.snmpoutgetrequests = YLeaf(YType.uint32, "snmpOutGetRequests")

            self.snmpoutgetresponses = YLeaf(YType.uint32, "snmpOutGetResponses")

            self.snmpoutnosuchnames = YLeaf(YType.uint32, "snmpOutNoSuchNames")

            self.snmpoutpkts = YLeaf(YType.uint32, "snmpOutPkts")

            self.snmpoutsetrequests = YLeaf(YType.uint32, "snmpOutSetRequests")

            self.snmpouttoobigs = YLeaf(YType.uint32, "snmpOutTooBigs")

            self.snmpouttraps = YLeaf(YType.uint32, "snmpOutTraps")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("snmpenableauthentraps",
                            "snmpinasnparseerrs",
                            "snmpinbadcommunitynames",
                            "snmpinbadcommunityuses",
                            "snmpinbadvalues",
                            "snmpinbadversions",
                            "snmpingenerrs",
                            "snmpingetnexts",
                            "snmpingetrequests",
                            "snmpingetresponses",
                            "snmpinnosuchnames",
                            "snmpinpkts",
                            "snmpinreadonlys",
                            "snmpinsetrequests",
                            "snmpintoobigs",
                            "snmpintotalreqvars",
                            "snmpintotalsetvars",
                            "snmpintraps",
                            "snmpoutbadvalues",
                            "snmpoutgenerrs",
                            "snmpoutgetnexts",
                            "snmpoutgetrequests",
                            "snmpoutgetresponses",
                            "snmpoutnosuchnames",
                            "snmpoutpkts",
                            "snmpoutsetrequests",
                            "snmpouttoobigs",
                            "snmpouttraps") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rfc1213Mib.Snmp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Snmp, self).__setattr__(name, value)

        class Snmpenableauthentraps(Enum):
            """
            Snmpenableauthentraps

            Indicates whether the SNMP agent process is

            permitted to generate authentication\-failure

            traps.  The value of this object overrides any

            configuration information; as such, it provides a

            means whereby all authentication\-failure traps may

            be disabled.

            Note that it is strongly recommended that this

            object be stored in non\-volatile memory so that it

            remains constant between re\-initializations of the

            network management system.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")


        def has_data(self):
            return (
                self.snmpenableauthentraps.is_set or
                self.snmpinasnparseerrs.is_set or
                self.snmpinbadcommunitynames.is_set or
                self.snmpinbadcommunityuses.is_set or
                self.snmpinbadvalues.is_set or
                self.snmpinbadversions.is_set or
                self.snmpingenerrs.is_set or
                self.snmpingetnexts.is_set or
                self.snmpingetrequests.is_set or
                self.snmpingetresponses.is_set or
                self.snmpinnosuchnames.is_set or
                self.snmpinpkts.is_set or
                self.snmpinreadonlys.is_set or
                self.snmpinsetrequests.is_set or
                self.snmpintoobigs.is_set or
                self.snmpintotalreqvars.is_set or
                self.snmpintotalsetvars.is_set or
                self.snmpintraps.is_set or
                self.snmpoutbadvalues.is_set or
                self.snmpoutgenerrs.is_set or
                self.snmpoutgetnexts.is_set or
                self.snmpoutgetrequests.is_set or
                self.snmpoutgetresponses.is_set or
                self.snmpoutnosuchnames.is_set or
                self.snmpoutpkts.is_set or
                self.snmpoutsetrequests.is_set or
                self.snmpouttoobigs.is_set or
                self.snmpouttraps.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.snmpenableauthentraps.yfilter != YFilter.not_set or
                self.snmpinasnparseerrs.yfilter != YFilter.not_set or
                self.snmpinbadcommunitynames.yfilter != YFilter.not_set or
                self.snmpinbadcommunityuses.yfilter != YFilter.not_set or
                self.snmpinbadvalues.yfilter != YFilter.not_set or
                self.snmpinbadversions.yfilter != YFilter.not_set or
                self.snmpingenerrs.yfilter != YFilter.not_set or
                self.snmpingetnexts.yfilter != YFilter.not_set or
                self.snmpingetrequests.yfilter != YFilter.not_set or
                self.snmpingetresponses.yfilter != YFilter.not_set or
                self.snmpinnosuchnames.yfilter != YFilter.not_set or
                self.snmpinpkts.yfilter != YFilter.not_set or
                self.snmpinreadonlys.yfilter != YFilter.not_set or
                self.snmpinsetrequests.yfilter != YFilter.not_set or
                self.snmpintoobigs.yfilter != YFilter.not_set or
                self.snmpintotalreqvars.yfilter != YFilter.not_set or
                self.snmpintotalsetvars.yfilter != YFilter.not_set or
                self.snmpintraps.yfilter != YFilter.not_set or
                self.snmpoutbadvalues.yfilter != YFilter.not_set or
                self.snmpoutgenerrs.yfilter != YFilter.not_set or
                self.snmpoutgetnexts.yfilter != YFilter.not_set or
                self.snmpoutgetrequests.yfilter != YFilter.not_set or
                self.snmpoutgetresponses.yfilter != YFilter.not_set or
                self.snmpoutnosuchnames.yfilter != YFilter.not_set or
                self.snmpoutpkts.yfilter != YFilter.not_set or
                self.snmpoutsetrequests.yfilter != YFilter.not_set or
                self.snmpouttoobigs.yfilter != YFilter.not_set or
                self.snmpouttraps.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.snmpenableauthentraps.is_set or self.snmpenableauthentraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpenableauthentraps.get_name_leafdata())
            if (self.snmpinasnparseerrs.is_set or self.snmpinasnparseerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinasnparseerrs.get_name_leafdata())
            if (self.snmpinbadcommunitynames.is_set or self.snmpinbadcommunitynames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadcommunitynames.get_name_leafdata())
            if (self.snmpinbadcommunityuses.is_set or self.snmpinbadcommunityuses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadcommunityuses.get_name_leafdata())
            if (self.snmpinbadvalues.is_set or self.snmpinbadvalues.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadvalues.get_name_leafdata())
            if (self.snmpinbadversions.is_set or self.snmpinbadversions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadversions.get_name_leafdata())
            if (self.snmpingenerrs.is_set or self.snmpingenerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingenerrs.get_name_leafdata())
            if (self.snmpingetnexts.is_set or self.snmpingetnexts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingetnexts.get_name_leafdata())
            if (self.snmpingetrequests.is_set or self.snmpingetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingetrequests.get_name_leafdata())
            if (self.snmpingetresponses.is_set or self.snmpingetresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingetresponses.get_name_leafdata())
            if (self.snmpinnosuchnames.is_set or self.snmpinnosuchnames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinnosuchnames.get_name_leafdata())
            if (self.snmpinpkts.is_set or self.snmpinpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinpkts.get_name_leafdata())
            if (self.snmpinreadonlys.is_set or self.snmpinreadonlys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinreadonlys.get_name_leafdata())
            if (self.snmpinsetrequests.is_set or self.snmpinsetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinsetrequests.get_name_leafdata())
            if (self.snmpintoobigs.is_set or self.snmpintoobigs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintoobigs.get_name_leafdata())
            if (self.snmpintotalreqvars.is_set or self.snmpintotalreqvars.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintotalreqvars.get_name_leafdata())
            if (self.snmpintotalsetvars.is_set or self.snmpintotalsetvars.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintotalsetvars.get_name_leafdata())
            if (self.snmpintraps.is_set or self.snmpintraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintraps.get_name_leafdata())
            if (self.snmpoutbadvalues.is_set or self.snmpoutbadvalues.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutbadvalues.get_name_leafdata())
            if (self.snmpoutgenerrs.is_set or self.snmpoutgenerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgenerrs.get_name_leafdata())
            if (self.snmpoutgetnexts.is_set or self.snmpoutgetnexts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgetnexts.get_name_leafdata())
            if (self.snmpoutgetrequests.is_set or self.snmpoutgetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgetrequests.get_name_leafdata())
            if (self.snmpoutgetresponses.is_set or self.snmpoutgetresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgetresponses.get_name_leafdata())
            if (self.snmpoutnosuchnames.is_set or self.snmpoutnosuchnames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutnosuchnames.get_name_leafdata())
            if (self.snmpoutpkts.is_set or self.snmpoutpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutpkts.get_name_leafdata())
            if (self.snmpoutsetrequests.is_set or self.snmpoutsetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutsetrequests.get_name_leafdata())
            if (self.snmpouttoobigs.is_set or self.snmpouttoobigs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpouttoobigs.get_name_leafdata())
            if (self.snmpouttraps.is_set or self.snmpouttraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpouttraps.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpEnableAuthenTraps" or name == "snmpInASNParseErrs" or name == "snmpInBadCommunityNames" or name == "snmpInBadCommunityUses" or name == "snmpInBadValues" or name == "snmpInBadVersions" or name == "snmpInGenErrs" or name == "snmpInGetNexts" or name == "snmpInGetRequests" or name == "snmpInGetResponses" or name == "snmpInNoSuchNames" or name == "snmpInPkts" or name == "snmpInReadOnlys" or name == "snmpInSetRequests" or name == "snmpInTooBigs" or name == "snmpInTotalReqVars" or name == "snmpInTotalSetVars" or name == "snmpInTraps" or name == "snmpOutBadValues" or name == "snmpOutGenErrs" or name == "snmpOutGetNexts" or name == "snmpOutGetRequests" or name == "snmpOutGetResponses" or name == "snmpOutNoSuchNames" or name == "snmpOutPkts" or name == "snmpOutSetRequests" or name == "snmpOutTooBigs" or name == "snmpOutTraps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "snmpEnableAuthenTraps"):
                self.snmpenableauthentraps = value
                self.snmpenableauthentraps.value_namespace = name_space
                self.snmpenableauthentraps.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInASNParseErrs"):
                self.snmpinasnparseerrs = value
                self.snmpinasnparseerrs.value_namespace = name_space
                self.snmpinasnparseerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadCommunityNames"):
                self.snmpinbadcommunitynames = value
                self.snmpinbadcommunitynames.value_namespace = name_space
                self.snmpinbadcommunitynames.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadCommunityUses"):
                self.snmpinbadcommunityuses = value
                self.snmpinbadcommunityuses.value_namespace = name_space
                self.snmpinbadcommunityuses.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadValues"):
                self.snmpinbadvalues = value
                self.snmpinbadvalues.value_namespace = name_space
                self.snmpinbadvalues.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadVersions"):
                self.snmpinbadversions = value
                self.snmpinbadversions.value_namespace = name_space
                self.snmpinbadversions.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGenErrs"):
                self.snmpingenerrs = value
                self.snmpingenerrs.value_namespace = name_space
                self.snmpingenerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGetNexts"):
                self.snmpingetnexts = value
                self.snmpingetnexts.value_namespace = name_space
                self.snmpingetnexts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGetRequests"):
                self.snmpingetrequests = value
                self.snmpingetrequests.value_namespace = name_space
                self.snmpingetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGetResponses"):
                self.snmpingetresponses = value
                self.snmpingetresponses.value_namespace = name_space
                self.snmpingetresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInNoSuchNames"):
                self.snmpinnosuchnames = value
                self.snmpinnosuchnames.value_namespace = name_space
                self.snmpinnosuchnames.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInPkts"):
                self.snmpinpkts = value
                self.snmpinpkts.value_namespace = name_space
                self.snmpinpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInReadOnlys"):
                self.snmpinreadonlys = value
                self.snmpinreadonlys.value_namespace = name_space
                self.snmpinreadonlys.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInSetRequests"):
                self.snmpinsetrequests = value
                self.snmpinsetrequests.value_namespace = name_space
                self.snmpinsetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTooBigs"):
                self.snmpintoobigs = value
                self.snmpintoobigs.value_namespace = name_space
                self.snmpintoobigs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTotalReqVars"):
                self.snmpintotalreqvars = value
                self.snmpintotalreqvars.value_namespace = name_space
                self.snmpintotalreqvars.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTotalSetVars"):
                self.snmpintotalsetvars = value
                self.snmpintotalsetvars.value_namespace = name_space
                self.snmpintotalsetvars.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTraps"):
                self.snmpintraps = value
                self.snmpintraps.value_namespace = name_space
                self.snmpintraps.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutBadValues"):
                self.snmpoutbadvalues = value
                self.snmpoutbadvalues.value_namespace = name_space
                self.snmpoutbadvalues.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGenErrs"):
                self.snmpoutgenerrs = value
                self.snmpoutgenerrs.value_namespace = name_space
                self.snmpoutgenerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGetNexts"):
                self.snmpoutgetnexts = value
                self.snmpoutgetnexts.value_namespace = name_space
                self.snmpoutgetnexts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGetRequests"):
                self.snmpoutgetrequests = value
                self.snmpoutgetrequests.value_namespace = name_space
                self.snmpoutgetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGetResponses"):
                self.snmpoutgetresponses = value
                self.snmpoutgetresponses.value_namespace = name_space
                self.snmpoutgetresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutNoSuchNames"):
                self.snmpoutnosuchnames = value
                self.snmpoutnosuchnames.value_namespace = name_space
                self.snmpoutnosuchnames.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutPkts"):
                self.snmpoutpkts = value
                self.snmpoutpkts.value_namespace = name_space
                self.snmpoutpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutSetRequests"):
                self.snmpoutsetrequests = value
                self.snmpoutsetrequests.value_namespace = name_space
                self.snmpoutsetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutTooBigs"):
                self.snmpouttoobigs = value
                self.snmpouttoobigs.value_namespace = name_space
                self.snmpouttoobigs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutTraps"):
                self.snmpouttraps = value
                self.snmpouttraps.value_namespace = name_space
                self.snmpouttraps.value_namespace_prefix = name_space_prefix


    class Iftable(Entity):
        """
        A list of interface entries.  The number of
        entries is given by the value of ifNumber.
        
        .. attribute:: ifentry
        
        	An interface entry containing objects at the subnetwork layer and below for a particular interface
        	**type**\: list of    :py:class:`Ifentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iftable.Ifentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Iftable, self).__init__()

            self.yang_name = "ifTable"
            self.yang_parent_name = "RFC1213-MIB"

            self.ifentry = YList(self)

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
                        super(Rfc1213Mib.Iftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Iftable, self).__setattr__(name, value)


        class Ifentry(Entity):
            """
            An interface entry containing objects at the
            subnetwork layer and below for a particular
            interface.
            
            .. attribute:: ifindex  <key>
            
            	A unique value for each interface.  Its value ranges between 1 and the value of ifNumber.  The value for each interface must remain constant at least from one re\-initialization of the entity's network management system to the next re\- initialization
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifadminstatus
            
            	The desired state of the interface.  The testing(3) state indicates that no operational packets can be passed
            	**type**\:   :py:class:`Ifadminstatus <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iftable.Ifentry.Ifadminstatus>`
            
            .. attribute:: ifdescr
            
            	A textual string containing information about the interface.  This string should include the name of the manufacturer, the product name and the version of the hardware interface
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ifindiscards
            
            	The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinerrors
            
            	The number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinnucastpkts
            
            	The number of non\-unicast (i.e., subnetwork\- broadcast or subnetwork\-multicast) packets delivered to a higher\-layer protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinoctets
            
            	The total number of octets received on the interface, including framing characters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinucastpkts
            
            	The number of subnetwork\-unicast packets delivered to a higher\-layer protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinunknownprotos
            
            	The number of packets received via the interface which were discarded because of an unknown or unsupported protocol
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iflastchange
            
            	The value of sysUpTime at the time the interface entered its current operational state.  If the current state was entered prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifmtu
            
            	The size of the largest datagram which can be sent/received on the interface, specified in octets.  For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifoperstatus
            
            	The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed
            	**type**\:   :py:class:`Ifoperstatus <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iftable.Ifentry.Ifoperstatus>`
            
            .. attribute:: ifoutdiscards
            
            	The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifouterrors
            
            	The number of outbound packets that could not be transmitted because of errors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutnucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted to a non\- unicast (i.e., a subnetwork\-broadcast or subnetwork\-multicast) address, including those that were discarded or not sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutqlen
            
            	The length of the output packet queue (in packets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted to a subnetwork\-unicast address, including those that were discarded or not sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifphysaddress
            
            	The interface's address at the protocol layer immediately `below' the network layer in the protocol stack.  For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length
            	**type**\:  str
            
            .. attribute:: ifspecific
            
            	A reference to MIB definitions specific to the particular media being used to realize the interface.  For example, if the interface is realized by an ethernet, then the value of this object refers to a document defining objects specific to ethernet.  If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ifspeed
            
            	An estimate of the interface's current bandwidth in bits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iftype
            
            	The type of interface.  Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention
            	**type**\:   :py:class:`Ianaiftype <ydk.models.cisco_ios_xe.IANAifType_MIB.Ianaiftype>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Iftable.Ifentry, self).__init__()

                self.yang_name = "ifEntry"
                self.yang_parent_name = "ifTable"

                self.ifindex = YLeaf(YType.int32, "ifIndex")

                self.ifadminstatus = YLeaf(YType.enumeration, "ifAdminStatus")

                self.ifdescr = YLeaf(YType.str, "ifDescr")

                self.ifindiscards = YLeaf(YType.uint32, "ifInDiscards")

                self.ifinerrors = YLeaf(YType.uint32, "ifInErrors")

                self.ifinnucastpkts = YLeaf(YType.uint32, "ifInNUcastPkts")

                self.ifinoctets = YLeaf(YType.uint32, "ifInOctets")

                self.ifinucastpkts = YLeaf(YType.uint32, "ifInUcastPkts")

                self.ifinunknownprotos = YLeaf(YType.uint32, "ifInUnknownProtos")

                self.iflastchange = YLeaf(YType.uint32, "ifLastChange")

                self.ifmtu = YLeaf(YType.int32, "ifMtu")

                self.ifoperstatus = YLeaf(YType.enumeration, "ifOperStatus")

                self.ifoutdiscards = YLeaf(YType.uint32, "ifOutDiscards")

                self.ifouterrors = YLeaf(YType.uint32, "ifOutErrors")

                self.ifoutnucastpkts = YLeaf(YType.uint32, "ifOutNUcastPkts")

                self.ifoutoctets = YLeaf(YType.uint32, "ifOutOctets")

                self.ifoutqlen = YLeaf(YType.uint32, "ifOutQLen")

                self.ifoutucastpkts = YLeaf(YType.uint32, "ifOutUcastPkts")

                self.ifphysaddress = YLeaf(YType.str, "ifPhysAddress")

                self.ifspecific = YLeaf(YType.str, "ifSpecific")

                self.ifspeed = YLeaf(YType.uint32, "ifSpeed")

                self.iftype = YLeaf(YType.enumeration, "ifType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "ifadminstatus",
                                "ifdescr",
                                "ifindiscards",
                                "ifinerrors",
                                "ifinnucastpkts",
                                "ifinoctets",
                                "ifinucastpkts",
                                "ifinunknownprotos",
                                "iflastchange",
                                "ifmtu",
                                "ifoperstatus",
                                "ifoutdiscards",
                                "ifouterrors",
                                "ifoutnucastpkts",
                                "ifoutoctets",
                                "ifoutqlen",
                                "ifoutucastpkts",
                                "ifphysaddress",
                                "ifspecific",
                                "ifspeed",
                                "iftype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1213Mib.Iftable.Ifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Iftable.Ifentry, self).__setattr__(name, value)

            class Ifadminstatus(Enum):
                """
                Ifadminstatus

                The desired state of the interface.  The

                testing(3) state indicates that no operational

                packets can be passed.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Ifoperstatus(Enum):
                """
                Ifoperstatus

                The current operational state of the interface.

                The testing(3) state indicates that no operational

                packets can be passed.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")

                unknown = Enum.YLeaf(4, "unknown")

                dormant = Enum.YLeaf(5, "dormant")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.ifadminstatus.is_set or
                    self.ifdescr.is_set or
                    self.ifindiscards.is_set or
                    self.ifinerrors.is_set or
                    self.ifinnucastpkts.is_set or
                    self.ifinoctets.is_set or
                    self.ifinucastpkts.is_set or
                    self.ifinunknownprotos.is_set or
                    self.iflastchange.is_set or
                    self.ifmtu.is_set or
                    self.ifoperstatus.is_set or
                    self.ifoutdiscards.is_set or
                    self.ifouterrors.is_set or
                    self.ifoutnucastpkts.is_set or
                    self.ifoutoctets.is_set or
                    self.ifoutqlen.is_set or
                    self.ifoutucastpkts.is_set or
                    self.ifphysaddress.is_set or
                    self.ifspecific.is_set or
                    self.ifspeed.is_set or
                    self.iftype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.ifadminstatus.yfilter != YFilter.not_set or
                    self.ifdescr.yfilter != YFilter.not_set or
                    self.ifindiscards.yfilter != YFilter.not_set or
                    self.ifinerrors.yfilter != YFilter.not_set or
                    self.ifinnucastpkts.yfilter != YFilter.not_set or
                    self.ifinoctets.yfilter != YFilter.not_set or
                    self.ifinucastpkts.yfilter != YFilter.not_set or
                    self.ifinunknownprotos.yfilter != YFilter.not_set or
                    self.iflastchange.yfilter != YFilter.not_set or
                    self.ifmtu.yfilter != YFilter.not_set or
                    self.ifoperstatus.yfilter != YFilter.not_set or
                    self.ifoutdiscards.yfilter != YFilter.not_set or
                    self.ifouterrors.yfilter != YFilter.not_set or
                    self.ifoutnucastpkts.yfilter != YFilter.not_set or
                    self.ifoutoctets.yfilter != YFilter.not_set or
                    self.ifoutqlen.yfilter != YFilter.not_set or
                    self.ifoutucastpkts.yfilter != YFilter.not_set or
                    self.ifphysaddress.yfilter != YFilter.not_set or
                    self.ifspecific.yfilter != YFilter.not_set or
                    self.ifspeed.yfilter != YFilter.not_set or
                    self.iftype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ifEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/ifTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.ifadminstatus.is_set or self.ifadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifadminstatus.get_name_leafdata())
                if (self.ifdescr.is_set or self.ifdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifdescr.get_name_leafdata())
                if (self.ifindiscards.is_set or self.ifindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindiscards.get_name_leafdata())
                if (self.ifinerrors.is_set or self.ifinerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinerrors.get_name_leafdata())
                if (self.ifinnucastpkts.is_set or self.ifinnucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinnucastpkts.get_name_leafdata())
                if (self.ifinoctets.is_set or self.ifinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinoctets.get_name_leafdata())
                if (self.ifinucastpkts.is_set or self.ifinucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinucastpkts.get_name_leafdata())
                if (self.ifinunknownprotos.is_set or self.ifinunknownprotos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifinunknownprotos.get_name_leafdata())
                if (self.iflastchange.is_set or self.iflastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iflastchange.get_name_leafdata())
                if (self.ifmtu.is_set or self.ifmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifmtu.get_name_leafdata())
                if (self.ifoperstatus.is_set or self.ifoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoperstatus.get_name_leafdata())
                if (self.ifoutdiscards.is_set or self.ifoutdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutdiscards.get_name_leafdata())
                if (self.ifouterrors.is_set or self.ifouterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifouterrors.get_name_leafdata())
                if (self.ifoutnucastpkts.is_set or self.ifoutnucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutnucastpkts.get_name_leafdata())
                if (self.ifoutoctets.is_set or self.ifoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutoctets.get_name_leafdata())
                if (self.ifoutqlen.is_set or self.ifoutqlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutqlen.get_name_leafdata())
                if (self.ifoutucastpkts.is_set or self.ifoutucastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifoutucastpkts.get_name_leafdata())
                if (self.ifphysaddress.is_set or self.ifphysaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifphysaddress.get_name_leafdata())
                if (self.ifspecific.is_set or self.ifspecific.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifspecific.get_name_leafdata())
                if (self.ifspeed.is_set or self.ifspeed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifspeed.get_name_leafdata())
                if (self.iftype.is_set or self.iftype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iftype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "ifAdminStatus" or name == "ifDescr" or name == "ifInDiscards" or name == "ifInErrors" or name == "ifInNUcastPkts" or name == "ifInOctets" or name == "ifInUcastPkts" or name == "ifInUnknownProtos" or name == "ifLastChange" or name == "ifMtu" or name == "ifOperStatus" or name == "ifOutDiscards" or name == "ifOutErrors" or name == "ifOutNUcastPkts" or name == "ifOutOctets" or name == "ifOutQLen" or name == "ifOutUcastPkts" or name == "ifPhysAddress" or name == "ifSpecific" or name == "ifSpeed" or name == "ifType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ifAdminStatus"):
                    self.ifadminstatus = value
                    self.ifadminstatus.value_namespace = name_space
                    self.ifadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ifDescr"):
                    self.ifdescr = value
                    self.ifdescr.value_namespace = name_space
                    self.ifdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInDiscards"):
                    self.ifindiscards = value
                    self.ifindiscards.value_namespace = name_space
                    self.ifindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInErrors"):
                    self.ifinerrors = value
                    self.ifinerrors.value_namespace = name_space
                    self.ifinerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInNUcastPkts"):
                    self.ifinnucastpkts = value
                    self.ifinnucastpkts.value_namespace = name_space
                    self.ifinnucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInOctets"):
                    self.ifinoctets = value
                    self.ifinoctets.value_namespace = name_space
                    self.ifinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInUcastPkts"):
                    self.ifinucastpkts = value
                    self.ifinucastpkts.value_namespace = name_space
                    self.ifinucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifInUnknownProtos"):
                    self.ifinunknownprotos = value
                    self.ifinunknownprotos.value_namespace = name_space
                    self.ifinunknownprotos.value_namespace_prefix = name_space_prefix
                if(value_path == "ifLastChange"):
                    self.iflastchange = value
                    self.iflastchange.value_namespace = name_space
                    self.iflastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "ifMtu"):
                    self.ifmtu = value
                    self.ifmtu.value_namespace = name_space
                    self.ifmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOperStatus"):
                    self.ifoperstatus = value
                    self.ifoperstatus.value_namespace = name_space
                    self.ifoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutDiscards"):
                    self.ifoutdiscards = value
                    self.ifoutdiscards.value_namespace = name_space
                    self.ifoutdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutErrors"):
                    self.ifouterrors = value
                    self.ifouterrors.value_namespace = name_space
                    self.ifouterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutNUcastPkts"):
                    self.ifoutnucastpkts = value
                    self.ifoutnucastpkts.value_namespace = name_space
                    self.ifoutnucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutOctets"):
                    self.ifoutoctets = value
                    self.ifoutoctets.value_namespace = name_space
                    self.ifoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutQLen"):
                    self.ifoutqlen = value
                    self.ifoutqlen.value_namespace = name_space
                    self.ifoutqlen.value_namespace_prefix = name_space_prefix
                if(value_path == "ifOutUcastPkts"):
                    self.ifoutucastpkts = value
                    self.ifoutucastpkts.value_namespace = name_space
                    self.ifoutucastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ifPhysAddress"):
                    self.ifphysaddress = value
                    self.ifphysaddress.value_namespace = name_space
                    self.ifphysaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ifSpecific"):
                    self.ifspecific = value
                    self.ifspecific.value_namespace = name_space
                    self.ifspecific.value_namespace_prefix = name_space_prefix
                if(value_path == "ifSpeed"):
                    self.ifspeed = value
                    self.ifspeed.value_namespace = name_space
                    self.ifspeed.value_namespace_prefix = name_space_prefix
                if(value_path == "ifType"):
                    self.iftype = value
                    self.iftype.value_namespace = name_space
                    self.iftype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ifTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ifEntry"):
                for c in self.ifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1213Mib.Iftable.Ifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Attable(Entity):
        """
        The Address Translation tables contain the
        NetworkAddress to `physical' address equivalences.
        Some interfaces do not use translation tables for
        determining address equivalences (e.g., DDN\-X.25
        has an algorithmic method); if all interfaces are
        of this type, then the Address Translation table
        is empty, i.e., has zero entries.
        
        .. attribute:: atentry
        
        	Each entry contains one NetworkAddress to `physical' address equivalence
        	**type**\: list of    :py:class:`Atentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Attable.Atentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Attable, self).__init__()

            self.yang_name = "atTable"
            self.yang_parent_name = "RFC1213-MIB"

            self.atentry = YList(self)

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
                        super(Rfc1213Mib.Attable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Attable, self).__setattr__(name, value)


        class Atentry(Entity):
            """
            Each entry contains one NetworkAddress to
            `physical' address equivalence.
            
            .. attribute:: atifindex  <key>
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: atifindex_2  <key>
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: atnetaddress  <key>
            
            	The NetworkAddress (e.g., the IP address) corresponding to the media\-dependent `physical' address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: atphysaddress
            
            	The media\-dependent `physical' address.  Setting this object to a null string (one of zero length) has the effect of invaliding the corresponding entry in the atTable object.  That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant atPhysAddress object
            	**type**\:  str
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Attable.Atentry, self).__init__()

                self.yang_name = "atEntry"
                self.yang_parent_name = "atTable"

                self.atifindex = YLeaf(YType.int32, "atIfIndex")

                self.atifindex_2 = YLeaf(YType.int32, "atIfIndex_2")

                self.atnetaddress = YLeaf(YType.str, "atNetAddress")

                self.atphysaddress = YLeaf(YType.str, "atPhysAddress")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("atifindex",
                                "atifindex_2",
                                "atnetaddress",
                                "atphysaddress") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1213Mib.Attable.Atentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Attable.Atentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.atifindex.is_set or
                    self.atifindex_2.is_set or
                    self.atnetaddress.is_set or
                    self.atphysaddress.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.atifindex.yfilter != YFilter.not_set or
                    self.atifindex_2.yfilter != YFilter.not_set or
                    self.atnetaddress.yfilter != YFilter.not_set or
                    self.atphysaddress.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "atEntry" + "[atIfIndex='" + self.atifindex.get() + "']" + "[atIfIndex_2='" + self.atifindex_2.get() + "']" + "[atNetAddress='" + self.atnetaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/atTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.atifindex.is_set or self.atifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atifindex.get_name_leafdata())
                if (self.atifindex_2.is_set or self.atifindex_2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atifindex_2.get_name_leafdata())
                if (self.atnetaddress.is_set or self.atnetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atnetaddress.get_name_leafdata())
                if (self.atphysaddress.is_set or self.atphysaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.atphysaddress.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "atIfIndex" or name == "atIfIndex_2" or name == "atNetAddress" or name == "atPhysAddress"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "atIfIndex"):
                    self.atifindex = value
                    self.atifindex.value_namespace = name_space
                    self.atifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "atIfIndex_2"):
                    self.atifindex_2 = value
                    self.atifindex_2.value_namespace = name_space
                    self.atifindex_2.value_namespace_prefix = name_space_prefix
                if(value_path == "atNetAddress"):
                    self.atnetaddress = value
                    self.atnetaddress.value_namespace = name_space
                    self.atnetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "atPhysAddress"):
                    self.atphysaddress = value
                    self.atphysaddress.value_namespace = name_space
                    self.atphysaddress.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.atentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.atentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "atTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "atEntry"):
                for c in self.atentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1213Mib.Attable.Atentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.atentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "atEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipaddrtable(Entity):
        """
        The table of addressing information relevant to
        this entity's IP addresses.
        
        .. attribute:: ipaddrentry
        
        	The addressing information for one of this entity's IP addresses
        	**type**\: list of    :py:class:`Ipaddrentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ipaddrtable.Ipaddrentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Ipaddrtable, self).__init__()

            self.yang_name = "ipAddrTable"
            self.yang_parent_name = "RFC1213-MIB"

            self.ipaddrentry = YList(self)

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
                        super(Rfc1213Mib.Ipaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Ipaddrtable, self).__setattr__(name, value)


        class Ipaddrentry(Entity):
            """
            The addressing information for one of this
            entity's IP addresses.
            
            .. attribute:: ipadentaddr  <key>
            
            	The IP address to which this entry's addressing information pertains
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipadentbcastaddr
            
            	The value of the least\-significant bit in the IP broadcast address used for sending datagrams on the (logical) interface associated with the IP address of this entry.  For example, when the Internet standard all\-ones broadcast address is used, the value will be 1.  This value applies to both the subnet and network broadcasts addresses used by the entity on this (logical) interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipadentifindex
            
            	The index value which uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipadentnetmask
            
            	The subnet mask associated with the IP address of this entry.  The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipadentreasmmaxsize
            
            	The size of the largest IP datagram which this entity can re\-assemble from incoming IP fragmented datagrams received on this interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Ipaddrtable.Ipaddrentry, self).__init__()

                self.yang_name = "ipAddrEntry"
                self.yang_parent_name = "ipAddrTable"

                self.ipadentaddr = YLeaf(YType.str, "ipAdEntAddr")

                self.ipadentbcastaddr = YLeaf(YType.int32, "ipAdEntBcastAddr")

                self.ipadentifindex = YLeaf(YType.int32, "ipAdEntIfIndex")

                self.ipadentnetmask = YLeaf(YType.str, "ipAdEntNetMask")

                self.ipadentreasmmaxsize = YLeaf(YType.int32, "ipAdEntReasmMaxSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipadentaddr",
                                "ipadentbcastaddr",
                                "ipadentifindex",
                                "ipadentnetmask",
                                "ipadentreasmmaxsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1213Mib.Ipaddrtable.Ipaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Ipaddrtable.Ipaddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipadentaddr.is_set or
                    self.ipadentbcastaddr.is_set or
                    self.ipadentifindex.is_set or
                    self.ipadentnetmask.is_set or
                    self.ipadentreasmmaxsize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipadentaddr.yfilter != YFilter.not_set or
                    self.ipadentbcastaddr.yfilter != YFilter.not_set or
                    self.ipadentifindex.yfilter != YFilter.not_set or
                    self.ipadentnetmask.yfilter != YFilter.not_set or
                    self.ipadentreasmmaxsize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipAddrEntry" + "[ipAdEntAddr='" + self.ipadentaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/ipAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipadentaddr.is_set or self.ipadentaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentaddr.get_name_leafdata())
                if (self.ipadentbcastaddr.is_set or self.ipadentbcastaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentbcastaddr.get_name_leafdata())
                if (self.ipadentifindex.is_set or self.ipadentifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentifindex.get_name_leafdata())
                if (self.ipadentnetmask.is_set or self.ipadentnetmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentnetmask.get_name_leafdata())
                if (self.ipadentreasmmaxsize.is_set or self.ipadentreasmmaxsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentreasmmaxsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipAdEntAddr" or name == "ipAdEntBcastAddr" or name == "ipAdEntIfIndex" or name == "ipAdEntNetMask" or name == "ipAdEntReasmMaxSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipAdEntAddr"):
                    self.ipadentaddr = value
                    self.ipadentaddr.value_namespace = name_space
                    self.ipadentaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntBcastAddr"):
                    self.ipadentbcastaddr = value
                    self.ipadentbcastaddr.value_namespace = name_space
                    self.ipadentbcastaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntIfIndex"):
                    self.ipadentifindex = value
                    self.ipadentifindex.value_namespace = name_space
                    self.ipadentifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntNetMask"):
                    self.ipadentnetmask = value
                    self.ipadentnetmask.value_namespace = name_space
                    self.ipadentnetmask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntReasmMaxSize"):
                    self.ipadentreasmmaxsize = value
                    self.ipadentreasmmaxsize.value_namespace = name_space
                    self.ipadentreasmmaxsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipAddrEntry"):
                for c in self.ipaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1213Mib.Ipaddrtable.Ipaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Iproutetable(Entity):
        """
        This entity's IP Routing table.
        
        .. attribute:: iprouteentry
        
        	A route to a particular destination
        	**type**\: list of    :py:class:`Iprouteentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iproutetable.Iprouteentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Iproutetable, self).__init__()

            self.yang_name = "ipRouteTable"
            self.yang_parent_name = "RFC1213-MIB"

            self.iprouteentry = YList(self)

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
                        super(Rfc1213Mib.Iproutetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Iproutetable, self).__setattr__(name, value)


        class Iprouteentry(Entity):
            """
            A route to a particular destination.
            
            .. attribute:: iproutedest  <key>
            
            	The destination IP address of this route.  An entry with a value of 0.0.0.0 is considered a default route.  Multiple routes to a single destination can appear in the table, but access to such multiple entries is dependent on the table\- access mechanisms defined by the network management protocol in use
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iprouteage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iprouteifindex
            
            	The index value which uniquely identifies the local interface through which the next hop of this route should be reached.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iprouteinfo
            
            	A reference to MIB definitions specific to the particular routing protocol which is responsible for this route, as determined by the value specified in the route's ipRouteProto value.  If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: iproutemask
            
            	Indicate the mask to be logical\-ANDed with the destination address before being compared to the value in the ipRouteDest field.  For those systems that do not support arbitrary subnet masks, an agent constructs the value of the ipRouteMask by determining whether the value of the correspondent ipRouteDest field belong to a class\-A, B, or C network, and then using one of\:       mask           network      255.0.0.0      class\-A      255.255.0.0    class\-B      255.255.255.0  class\-C  If the value of the ipRouteDest is 0.0.0.0 (a default route), then the mask value is also 0.0.0.0.  It should be noted that all IP routing subsystems implicitly use this mechanism
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iproutemetric1
            
            	The primary routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric2
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric3
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric4
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric5
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutenexthop
            
            	The IP address of the next hop of this route. (In the case of a route bound to an interface which is realized via a broadcast media, the value of this field is the agent's IP address on that interface.)
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iprouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols
            	**type**\:   :py:class:`Iprouteproto <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iproutetable.Iprouteentry.Iprouteproto>`
            
            .. attribute:: iproutetype
            
            	The type of route.  Note that the values direct(3) and indirect(4) refer to the notion of direct and indirect routing in the IP architecture.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipRouteTable object.  That is, it effectively disassociates the destination identified with said entry from the route identified with said entry.  It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipRouteType object
            	**type**\:   :py:class:`Iproutetype <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Iproutetable.Iprouteentry.Iproutetype>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Iproutetable.Iprouteentry, self).__init__()

                self.yang_name = "ipRouteEntry"
                self.yang_parent_name = "ipRouteTable"

                self.iproutedest = YLeaf(YType.str, "ipRouteDest")

                self.iprouteage = YLeaf(YType.int32, "ipRouteAge")

                self.iprouteifindex = YLeaf(YType.int32, "ipRouteIfIndex")

                self.iprouteinfo = YLeaf(YType.str, "ipRouteInfo")

                self.iproutemask = YLeaf(YType.str, "ipRouteMask")

                self.iproutemetric1 = YLeaf(YType.int32, "ipRouteMetric1")

                self.iproutemetric2 = YLeaf(YType.int32, "ipRouteMetric2")

                self.iproutemetric3 = YLeaf(YType.int32, "ipRouteMetric3")

                self.iproutemetric4 = YLeaf(YType.int32, "ipRouteMetric4")

                self.iproutemetric5 = YLeaf(YType.int32, "ipRouteMetric5")

                self.iproutenexthop = YLeaf(YType.str, "ipRouteNextHop")

                self.iprouteproto = YLeaf(YType.enumeration, "ipRouteProto")

                self.iproutetype = YLeaf(YType.enumeration, "ipRouteType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("iproutedest",
                                "iprouteage",
                                "iprouteifindex",
                                "iprouteinfo",
                                "iproutemask",
                                "iproutemetric1",
                                "iproutemetric2",
                                "iproutemetric3",
                                "iproutemetric4",
                                "iproutemetric5",
                                "iproutenexthop",
                                "iprouteproto",
                                "iproutetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1213Mib.Iproutetable.Iprouteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Iproutetable.Iprouteentry, self).__setattr__(name, value)

            class Iprouteproto(Enum):
                """
                Iprouteproto

                The routing mechanism via which this route was

                learned.  Inclusion of values for gateway routing

                protocols is not intended to imply that hosts

                should support those protocols.

                .. data:: other = 1

                .. data:: local = 2

                .. data:: netmgmt = 3

                .. data:: icmp = 4

                .. data:: egp = 5

                .. data:: ggp = 6

                .. data:: hello = 7

                .. data:: rip = 8

                .. data:: is_is = 9

                .. data:: es_is = 10

                .. data:: ciscoIgrp = 11

                .. data:: bbnSpfIgp = 12

                .. data:: ospf = 13

                .. data:: bgp = 14

                """

                other = Enum.YLeaf(1, "other")

                local = Enum.YLeaf(2, "local")

                netmgmt = Enum.YLeaf(3, "netmgmt")

                icmp = Enum.YLeaf(4, "icmp")

                egp = Enum.YLeaf(5, "egp")

                ggp = Enum.YLeaf(6, "ggp")

                hello = Enum.YLeaf(7, "hello")

                rip = Enum.YLeaf(8, "rip")

                is_is = Enum.YLeaf(9, "is-is")

                es_is = Enum.YLeaf(10, "es-is")

                ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

                bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

                ospf = Enum.YLeaf(13, "ospf")

                bgp = Enum.YLeaf(14, "bgp")


            class Iproutetype(Enum):
                """
                Iproutetype

                The type of route.  Note that the values

                direct(3) and indirect(4) refer to the notion of

                direct and indirect routing in the IP

                architecture.

                Setting this object to the value invalid(2) has

                the effect of invalidating the corresponding entry

                in the ipRouteTable object.  That is, it

                effectively disassociates the destination

                identified with said entry from the route

                identified with said entry.  It is an

                implementation\-specific matter as to whether the

                agent removes an invalidated entry from the table.

                Accordingly, management stations must be prepared

                to receive tabular information from agents that

                corresponds to entries not currently in use.

                Proper interpretation of such entries requires

                examination of the relevant ipRouteType object.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: direct = 3

                .. data:: indirect = 4

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                direct = Enum.YLeaf(3, "direct")

                indirect = Enum.YLeaf(4, "indirect")


            def has_data(self):
                return (
                    self.iproutedest.is_set or
                    self.iprouteage.is_set or
                    self.iprouteifindex.is_set or
                    self.iprouteinfo.is_set or
                    self.iproutemask.is_set or
                    self.iproutemetric1.is_set or
                    self.iproutemetric2.is_set or
                    self.iproutemetric3.is_set or
                    self.iproutemetric4.is_set or
                    self.iproutemetric5.is_set or
                    self.iproutenexthop.is_set or
                    self.iprouteproto.is_set or
                    self.iproutetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.iproutedest.yfilter != YFilter.not_set or
                    self.iprouteage.yfilter != YFilter.not_set or
                    self.iprouteifindex.yfilter != YFilter.not_set or
                    self.iprouteinfo.yfilter != YFilter.not_set or
                    self.iproutemask.yfilter != YFilter.not_set or
                    self.iproutemetric1.yfilter != YFilter.not_set or
                    self.iproutemetric2.yfilter != YFilter.not_set or
                    self.iproutemetric3.yfilter != YFilter.not_set or
                    self.iproutemetric4.yfilter != YFilter.not_set or
                    self.iproutemetric5.yfilter != YFilter.not_set or
                    self.iproutenexthop.yfilter != YFilter.not_set or
                    self.iprouteproto.yfilter != YFilter.not_set or
                    self.iproutetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipRouteEntry" + "[ipRouteDest='" + self.iproutedest.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/ipRouteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.iproutedest.is_set or self.iproutedest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutedest.get_name_leafdata())
                if (self.iprouteage.is_set or self.iprouteage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iprouteage.get_name_leafdata())
                if (self.iprouteifindex.is_set or self.iprouteifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iprouteifindex.get_name_leafdata())
                if (self.iprouteinfo.is_set or self.iprouteinfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iprouteinfo.get_name_leafdata())
                if (self.iproutemask.is_set or self.iproutemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutemask.get_name_leafdata())
                if (self.iproutemetric1.is_set or self.iproutemetric1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutemetric1.get_name_leafdata())
                if (self.iproutemetric2.is_set or self.iproutemetric2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutemetric2.get_name_leafdata())
                if (self.iproutemetric3.is_set or self.iproutemetric3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutemetric3.get_name_leafdata())
                if (self.iproutemetric4.is_set or self.iproutemetric4.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutemetric4.get_name_leafdata())
                if (self.iproutemetric5.is_set or self.iproutemetric5.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutemetric5.get_name_leafdata())
                if (self.iproutenexthop.is_set or self.iproutenexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutenexthop.get_name_leafdata())
                if (self.iprouteproto.is_set or self.iprouteproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iprouteproto.get_name_leafdata())
                if (self.iproutetype.is_set or self.iproutetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iproutetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipRouteDest" or name == "ipRouteAge" or name == "ipRouteIfIndex" or name == "ipRouteInfo" or name == "ipRouteMask" or name == "ipRouteMetric1" or name == "ipRouteMetric2" or name == "ipRouteMetric3" or name == "ipRouteMetric4" or name == "ipRouteMetric5" or name == "ipRouteNextHop" or name == "ipRouteProto" or name == "ipRouteType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipRouteDest"):
                    self.iproutedest = value
                    self.iproutedest.value_namespace = name_space
                    self.iproutedest.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteAge"):
                    self.iprouteage = value
                    self.iprouteage.value_namespace = name_space
                    self.iprouteage.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteIfIndex"):
                    self.iprouteifindex = value
                    self.iprouteifindex.value_namespace = name_space
                    self.iprouteifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteInfo"):
                    self.iprouteinfo = value
                    self.iprouteinfo.value_namespace = name_space
                    self.iprouteinfo.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteMask"):
                    self.iproutemask = value
                    self.iproutemask.value_namespace = name_space
                    self.iproutemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteMetric1"):
                    self.iproutemetric1 = value
                    self.iproutemetric1.value_namespace = name_space
                    self.iproutemetric1.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteMetric2"):
                    self.iproutemetric2 = value
                    self.iproutemetric2.value_namespace = name_space
                    self.iproutemetric2.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteMetric3"):
                    self.iproutemetric3 = value
                    self.iproutemetric3.value_namespace = name_space
                    self.iproutemetric3.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteMetric4"):
                    self.iproutemetric4 = value
                    self.iproutemetric4.value_namespace = name_space
                    self.iproutemetric4.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteMetric5"):
                    self.iproutemetric5 = value
                    self.iproutemetric5.value_namespace = name_space
                    self.iproutemetric5.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteNextHop"):
                    self.iproutenexthop = value
                    self.iproutenexthop.value_namespace = name_space
                    self.iproutenexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteProto"):
                    self.iprouteproto = value
                    self.iprouteproto.value_namespace = name_space
                    self.iprouteproto.value_namespace_prefix = name_space_prefix
                if(value_path == "ipRouteType"):
                    self.iproutetype = value
                    self.iproutetype.value_namespace = name_space
                    self.iproutetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.iprouteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.iprouteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipRouteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipRouteEntry"):
                for c in self.iprouteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1213Mib.Iproutetable.Iprouteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.iprouteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipRouteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipnettomediatable(Entity):
        """
        The IP Address Translation table used for mapping
        from IP addresses to physical addresses.
        
        .. attribute:: ipnettomediaentry
        
        	Each entry contains one IpAddress to `physical' address equivalence
        	**type**\: list of    :py:class:`Ipnettomediaentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ipnettomediatable.Ipnettomediaentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Ipnettomediatable, self).__init__()

            self.yang_name = "ipNetToMediaTable"
            self.yang_parent_name = "RFC1213-MIB"

            self.ipnettomediaentry = YList(self)

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
                        super(Rfc1213Mib.Ipnettomediatable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Ipnettomediatable, self).__setattr__(name, value)


        class Ipnettomediaentry(Entity):
            """
            Each entry contains one IpAddress to `physical'
            address equivalence.
            
            .. attribute:: ipnettomediaifindex  <key>
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipnettomedianetaddress  <key>
            
            	The IpAddress corresponding to the media\- dependent `physical' address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipnettomediaphysaddress
            
            	The media\-dependent `physical' address
            	**type**\:  str
            
            .. attribute:: ipnettomediatype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToMediaTable.  That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry. It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToMediaType object
            	**type**\:   :py:class:`Ipnettomediatype <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Ipnettomediatable.Ipnettomediaentry.Ipnettomediatype>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Ipnettomediatable.Ipnettomediaentry, self).__init__()

                self.yang_name = "ipNetToMediaEntry"
                self.yang_parent_name = "ipNetToMediaTable"

                self.ipnettomediaifindex = YLeaf(YType.int32, "ipNetToMediaIfIndex")

                self.ipnettomedianetaddress = YLeaf(YType.str, "ipNetToMediaNetAddress")

                self.ipnettomediaphysaddress = YLeaf(YType.str, "ipNetToMediaPhysAddress")

                self.ipnettomediatype = YLeaf(YType.enumeration, "ipNetToMediaType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipnettomediaifindex",
                                "ipnettomedianetaddress",
                                "ipnettomediaphysaddress",
                                "ipnettomediatype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1213Mib.Ipnettomediatable.Ipnettomediaentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Ipnettomediatable.Ipnettomediaentry, self).__setattr__(name, value)

            class Ipnettomediatype(Enum):
                """
                Ipnettomediatype

                The type of mapping.

                Setting this object to the value invalid(2) has

                the effect of invalidating the corresponding entry

                in the ipNetToMediaTable.  That is, it effectively

                disassociates the interface identified with said

                entry from the mapping identified with said entry.

                It is an implementation\-specific matter as to

                whether the agent removes an invalidated entry

                from the table.  Accordingly, management stations

                must be prepared to receive tabular information

                from agents that corresponds to entries not

                currently in use.  Proper interpretation of such

                entries requires examination of the relevant

                ipNetToMediaType object.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: dynamic = 3

                .. data:: static = 4

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                dynamic = Enum.YLeaf(3, "dynamic")

                static = Enum.YLeaf(4, "static")


            def has_data(self):
                return (
                    self.ipnettomediaifindex.is_set or
                    self.ipnettomedianetaddress.is_set or
                    self.ipnettomediaphysaddress.is_set or
                    self.ipnettomediatype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipnettomediaifindex.yfilter != YFilter.not_set or
                    self.ipnettomedianetaddress.yfilter != YFilter.not_set or
                    self.ipnettomediaphysaddress.yfilter != YFilter.not_set or
                    self.ipnettomediatype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipNetToMediaEntry" + "[ipNetToMediaIfIndex='" + self.ipnettomediaifindex.get() + "']" + "[ipNetToMediaNetAddress='" + self.ipnettomedianetaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/ipNetToMediaTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipnettomediaifindex.is_set or self.ipnettomediaifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomediaifindex.get_name_leafdata())
                if (self.ipnettomedianetaddress.is_set or self.ipnettomedianetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomedianetaddress.get_name_leafdata())
                if (self.ipnettomediaphysaddress.is_set or self.ipnettomediaphysaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomediaphysaddress.get_name_leafdata())
                if (self.ipnettomediatype.is_set or self.ipnettomediatype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomediatype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipNetToMediaIfIndex" or name == "ipNetToMediaNetAddress" or name == "ipNetToMediaPhysAddress" or name == "ipNetToMediaType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipNetToMediaIfIndex"):
                    self.ipnettomediaifindex = value
                    self.ipnettomediaifindex.value_namespace = name_space
                    self.ipnettomediaifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToMediaNetAddress"):
                    self.ipnettomedianetaddress = value
                    self.ipnettomedianetaddress.value_namespace = name_space
                    self.ipnettomedianetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToMediaPhysAddress"):
                    self.ipnettomediaphysaddress = value
                    self.ipnettomediaphysaddress.value_namespace = name_space
                    self.ipnettomediaphysaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToMediaType"):
                    self.ipnettomediatype = value
                    self.ipnettomediatype.value_namespace = name_space
                    self.ipnettomediatype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipnettomediaentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipnettomediaentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipNetToMediaTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipNetToMediaEntry"):
                for c in self.ipnettomediaentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1213Mib.Ipnettomediatable.Ipnettomediaentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipnettomediaentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipNetToMediaEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tcpconntable(Entity):
        """
        A table containing TCP connection\-specific
        information.
        
        .. attribute:: tcpconnentry
        
        	Information about a particular current TCP connection.  An object of this type is transient, in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of    :py:class:`Tcpconnentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Tcpconntable.Tcpconnentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Tcpconntable, self).__init__()

            self.yang_name = "tcpConnTable"
            self.yang_parent_name = "RFC1213-MIB"

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
                        super(Rfc1213Mib.Tcpconntable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Tcpconntable, self).__setattr__(name, value)


        class Tcpconnentry(Entity):
            """
            Information about a particular current TCP
            connection.  An object of this type is transient,
            in that it ceases to exist when (or soon after)
            the connection makes the transition to the CLOSED
            state.
            
            .. attribute:: tcpconnlocaladdress  <key>
            
            	The local IP address for this TCP connection.  In the case of a connection in the listen state which is willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnlocalport  <key>
            
            	The local port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnremaddress  <key>
            
            	The remote IP address for this TCP connection
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnremport  <key>
            
            	The remote port number for this TCP connection
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnstate
            
            	The state of this TCP connection.  The only value which may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then this has the effect of deleting the TCB (as defined in RFC 793) of the corresponding connection on the managed node, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note however that RST segments are not sent reliably)
            	**type**\:   :py:class:`Tcpconnstate <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Tcpconntable.Tcpconnentry.Tcpconnstate>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Tcpconntable.Tcpconnentry, self).__init__()

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
                            super(Rfc1213Mib.Tcpconntable.Tcpconnentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Tcpconntable.Tcpconnentry, self).__setattr__(name, value)

            class Tcpconnstate(Enum):
                """
                Tcpconnstate

                The state of this TCP connection.

                The only value which may be set by a management

                station is deleteTCB(12).  Accordingly, it is

                appropriate for an agent to return a `badValue'

                response if a management station attempts to set

                this object to any other value.

                If a management station sets this object to the

                value deleteTCB(12), then this has the effect of

                deleting the TCB (as defined in RFC 793) of the

                corresponding connection on the managed node,

                resulting in immediate termination of the

                connection.

                As an implementation\-specific option, a RST

                segment may be sent from the managed node to the

                other TCP endpoint (note however that RST segments

                are not sent reliably).

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
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/tcpConnTable/%s" % self.get_segment_path()
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
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
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
                c = Rfc1213Mib.Tcpconntable.Tcpconnentry()
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


    class Udptable(Entity):
        """
        A table containing UDP listener information.
        
        .. attribute:: udpentry
        
        	Information about a particular current UDP listener
        	**type**\: list of    :py:class:`Udpentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Udptable.Udpentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Udptable, self).__init__()

            self.yang_name = "udpTable"
            self.yang_parent_name = "RFC1213-MIB"

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
                        super(Rfc1213Mib.Udptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Udptable, self).__setattr__(name, value)


        class Udpentry(Entity):
            """
            Information about a particular current UDP
            listener.
            
            .. attribute:: udplocaladdress  <key>
            
            	The local IP address for this UDP listener.  In the case of a UDP listener which is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udplocalport  <key>
            
            	The local port number for this UDP listener
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Udptable.Udpentry, self).__init__()

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
                            super(Rfc1213Mib.Udptable.Udpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Udptable.Udpentry, self).__setattr__(name, value)

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
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/udpTable/%s" % self.get_segment_path()
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
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
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
                c = Rfc1213Mib.Udptable.Udpentry()
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


    class Egpneightable(Entity):
        """
        The EGP neighbor table.
        
        .. attribute:: egpneighentry
        
        	Information about this entity's relationship with a particular EGP neighbor
        	**type**\: list of    :py:class:`Egpneighentry <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Egpneightable.Egpneighentry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(Rfc1213Mib.Egpneightable, self).__init__()

            self.yang_name = "egpNeighTable"
            self.yang_parent_name = "RFC1213-MIB"

            self.egpneighentry = YList(self)

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
                        super(Rfc1213Mib.Egpneightable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rfc1213Mib.Egpneightable, self).__setattr__(name, value)


        class Egpneighentry(Entity):
            """
            Information about this entity's relationship with
            a particular EGP neighbor.
            
            .. attribute:: egpneighaddr  <key>
            
            	The IP address of this entry's EGP neighbor
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: egpneighas
            
            	The autonomous system of this EGP peer.  Zero should be specified if the autonomous system number of the neighbor is not yet known
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneigheventtrigger
            
            	A control variable used to trigger operator\- initiated Start and Stop events.  When read, this variable always returns the most recent value that egpNeighEventTrigger was set to.  If it has not been set since the last initialization of the network management subsystem on the node, it returns a value of `stop'.  When set, this variable causes a Start or Stop event on the specified neighbor, as specified on pages 8\-10 of RFC 904.  Briefly, a Start event causes an Idle peer to begin neighbor acquisition and a non\-Idle peer to reinitiate neighbor acquisition.  A stop event causes a non\-Idle peer to return to the Idle state until a Start event occurs, either via egpNeighEventTrigger or otherwise
            	**type**\:   :py:class:`Egpneigheventtrigger <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Egpneightable.Egpneighentry.Egpneigheventtrigger>`
            
            .. attribute:: egpneighinerrmsgs
            
            	The number of EGP\-defined error messages received from this EGP peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighinerrs
            
            	The number of EGP messages received from this EGP peer that proved to be in error (e.g., bad EGP checksum)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighinmsgs
            
            	The number of EGP messages received without error from this EGP peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighintervalhello
            
            	The interval between EGP Hello command retransmissions (in hundredths of a second).  This represents the t1 timer as defined in RFC 904
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighintervalpoll
            
            	The interval between EGP poll command retransmissions (in hundredths of a second).  This represents the t3 timer as defined in RFC 904
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighmode
            
            	The polling mode of this EGP entity, either passive or active
            	**type**\:   :py:class:`Egpneighmode <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Egpneightable.Egpneighentry.Egpneighmode>`
            
            .. attribute:: egpneighouterrmsgs
            
            	The number of EGP\-defined error messages sent to this EGP peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighouterrs
            
            	The number of locally generated EGP messages not sent to this EGP peer due to resource limitations within an EGP entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighoutmsgs
            
            	The number of locally generated EGP messages to this EGP peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighstate
            
            	The EGP state of the local system with respect to this entry's EGP neighbor.  Each EGP state is represented by a value that is one greater than the numerical value associated with said state in RFC 904
            	**type**\:   :py:class:`Egpneighstate <ydk.models.cisco_ios_xe.RFC1213_MIB.Rfc1213Mib.Egpneightable.Egpneighentry.Egpneighstate>`
            
            .. attribute:: egpneighstatedowns
            
            	The number of EGP state transitions from the UP state to any other state with this EGP peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighstateups
            
            	The number of EGP state transitions to the UP state with this EGP peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(Rfc1213Mib.Egpneightable.Egpneighentry, self).__init__()

                self.yang_name = "egpNeighEntry"
                self.yang_parent_name = "egpNeighTable"

                self.egpneighaddr = YLeaf(YType.str, "egpNeighAddr")

                self.egpneighas = YLeaf(YType.int32, "egpNeighAs")

                self.egpneigheventtrigger = YLeaf(YType.enumeration, "egpNeighEventTrigger")

                self.egpneighinerrmsgs = YLeaf(YType.uint32, "egpNeighInErrMsgs")

                self.egpneighinerrs = YLeaf(YType.uint32, "egpNeighInErrs")

                self.egpneighinmsgs = YLeaf(YType.uint32, "egpNeighInMsgs")

                self.egpneighintervalhello = YLeaf(YType.int32, "egpNeighIntervalHello")

                self.egpneighintervalpoll = YLeaf(YType.int32, "egpNeighIntervalPoll")

                self.egpneighmode = YLeaf(YType.enumeration, "egpNeighMode")

                self.egpneighouterrmsgs = YLeaf(YType.uint32, "egpNeighOutErrMsgs")

                self.egpneighouterrs = YLeaf(YType.uint32, "egpNeighOutErrs")

                self.egpneighoutmsgs = YLeaf(YType.uint32, "egpNeighOutMsgs")

                self.egpneighstate = YLeaf(YType.enumeration, "egpNeighState")

                self.egpneighstatedowns = YLeaf(YType.uint32, "egpNeighStateDowns")

                self.egpneighstateups = YLeaf(YType.uint32, "egpNeighStateUps")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("egpneighaddr",
                                "egpneighas",
                                "egpneigheventtrigger",
                                "egpneighinerrmsgs",
                                "egpneighinerrs",
                                "egpneighinmsgs",
                                "egpneighintervalhello",
                                "egpneighintervalpoll",
                                "egpneighmode",
                                "egpneighouterrmsgs",
                                "egpneighouterrs",
                                "egpneighoutmsgs",
                                "egpneighstate",
                                "egpneighstatedowns",
                                "egpneighstateups") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rfc1213Mib.Egpneightable.Egpneighentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rfc1213Mib.Egpneightable.Egpneighentry, self).__setattr__(name, value)

            class Egpneigheventtrigger(Enum):
                """
                Egpneigheventtrigger

                A control variable used to trigger operator\-

                initiated Start and Stop events.  When read, this

                variable always returns the most recent value that

                egpNeighEventTrigger was set to.  If it has not

                been set since the last initialization of the

                network management subsystem on the node, it

                returns a value of `stop'.

                When set, this variable causes a Start or Stop

                event on the specified neighbor, as specified on

                pages 8\-10 of RFC 904.  Briefly, a Start event

                causes an Idle peer to begin neighbor acquisition

                and a non\-Idle peer to reinitiate neighbor

                acquisition.  A stop event causes a non\-Idle peer

                to return to the Idle state until a Start event

                occurs, either via egpNeighEventTrigger or

                otherwise.

                .. data:: start = 1

                .. data:: stop = 2

                """

                start = Enum.YLeaf(1, "start")

                stop = Enum.YLeaf(2, "stop")


            class Egpneighmode(Enum):
                """
                Egpneighmode

                The polling mode of this EGP entity, either

                passive or active.

                .. data:: active = 1

                .. data:: passive = 2

                """

                active = Enum.YLeaf(1, "active")

                passive = Enum.YLeaf(2, "passive")


            class Egpneighstate(Enum):
                """
                Egpneighstate

                The EGP state of the local system with respect to

                this entry's EGP neighbor.  Each EGP state is

                represented by a value that is one greater than

                the numerical value associated with said state in

                RFC 904.

                .. data:: idle = 1

                .. data:: acquisition = 2

                .. data:: down = 3

                .. data:: up = 4

                .. data:: cease = 5

                """

                idle = Enum.YLeaf(1, "idle")

                acquisition = Enum.YLeaf(2, "acquisition")

                down = Enum.YLeaf(3, "down")

                up = Enum.YLeaf(4, "up")

                cease = Enum.YLeaf(5, "cease")


            def has_data(self):
                return (
                    self.egpneighaddr.is_set or
                    self.egpneighas.is_set or
                    self.egpneigheventtrigger.is_set or
                    self.egpneighinerrmsgs.is_set or
                    self.egpneighinerrs.is_set or
                    self.egpneighinmsgs.is_set or
                    self.egpneighintervalhello.is_set or
                    self.egpneighintervalpoll.is_set or
                    self.egpneighmode.is_set or
                    self.egpneighouterrmsgs.is_set or
                    self.egpneighouterrs.is_set or
                    self.egpneighoutmsgs.is_set or
                    self.egpneighstate.is_set or
                    self.egpneighstatedowns.is_set or
                    self.egpneighstateups.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.egpneighaddr.yfilter != YFilter.not_set or
                    self.egpneighas.yfilter != YFilter.not_set or
                    self.egpneigheventtrigger.yfilter != YFilter.not_set or
                    self.egpneighinerrmsgs.yfilter != YFilter.not_set or
                    self.egpneighinerrs.yfilter != YFilter.not_set or
                    self.egpneighinmsgs.yfilter != YFilter.not_set or
                    self.egpneighintervalhello.yfilter != YFilter.not_set or
                    self.egpneighintervalpoll.yfilter != YFilter.not_set or
                    self.egpneighmode.yfilter != YFilter.not_set or
                    self.egpneighouterrmsgs.yfilter != YFilter.not_set or
                    self.egpneighouterrs.yfilter != YFilter.not_set or
                    self.egpneighoutmsgs.yfilter != YFilter.not_set or
                    self.egpneighstate.yfilter != YFilter.not_set or
                    self.egpneighstatedowns.yfilter != YFilter.not_set or
                    self.egpneighstateups.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "egpNeighEntry" + "[egpNeighAddr='" + self.egpneighaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RFC1213-MIB:RFC1213-MIB/egpNeighTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.egpneighaddr.is_set or self.egpneighaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighaddr.get_name_leafdata())
                if (self.egpneighas.is_set or self.egpneighas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighas.get_name_leafdata())
                if (self.egpneigheventtrigger.is_set or self.egpneigheventtrigger.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneigheventtrigger.get_name_leafdata())
                if (self.egpneighinerrmsgs.is_set or self.egpneighinerrmsgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighinerrmsgs.get_name_leafdata())
                if (self.egpneighinerrs.is_set or self.egpneighinerrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighinerrs.get_name_leafdata())
                if (self.egpneighinmsgs.is_set or self.egpneighinmsgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighinmsgs.get_name_leafdata())
                if (self.egpneighintervalhello.is_set or self.egpneighintervalhello.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighintervalhello.get_name_leafdata())
                if (self.egpneighintervalpoll.is_set or self.egpneighintervalpoll.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighintervalpoll.get_name_leafdata())
                if (self.egpneighmode.is_set or self.egpneighmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighmode.get_name_leafdata())
                if (self.egpneighouterrmsgs.is_set or self.egpneighouterrmsgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighouterrmsgs.get_name_leafdata())
                if (self.egpneighouterrs.is_set or self.egpneighouterrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighouterrs.get_name_leafdata())
                if (self.egpneighoutmsgs.is_set or self.egpneighoutmsgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighoutmsgs.get_name_leafdata())
                if (self.egpneighstate.is_set or self.egpneighstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighstate.get_name_leafdata())
                if (self.egpneighstatedowns.is_set or self.egpneighstatedowns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighstatedowns.get_name_leafdata())
                if (self.egpneighstateups.is_set or self.egpneighstateups.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.egpneighstateups.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "egpNeighAddr" or name == "egpNeighAs" or name == "egpNeighEventTrigger" or name == "egpNeighInErrMsgs" or name == "egpNeighInErrs" or name == "egpNeighInMsgs" or name == "egpNeighIntervalHello" or name == "egpNeighIntervalPoll" or name == "egpNeighMode" or name == "egpNeighOutErrMsgs" or name == "egpNeighOutErrs" or name == "egpNeighOutMsgs" or name == "egpNeighState" or name == "egpNeighStateDowns" or name == "egpNeighStateUps"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "egpNeighAddr"):
                    self.egpneighaddr = value
                    self.egpneighaddr.value_namespace = name_space
                    self.egpneighaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighAs"):
                    self.egpneighas = value
                    self.egpneighas.value_namespace = name_space
                    self.egpneighas.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighEventTrigger"):
                    self.egpneigheventtrigger = value
                    self.egpneigheventtrigger.value_namespace = name_space
                    self.egpneigheventtrigger.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighInErrMsgs"):
                    self.egpneighinerrmsgs = value
                    self.egpneighinerrmsgs.value_namespace = name_space
                    self.egpneighinerrmsgs.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighInErrs"):
                    self.egpneighinerrs = value
                    self.egpneighinerrs.value_namespace = name_space
                    self.egpneighinerrs.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighInMsgs"):
                    self.egpneighinmsgs = value
                    self.egpneighinmsgs.value_namespace = name_space
                    self.egpneighinmsgs.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighIntervalHello"):
                    self.egpneighintervalhello = value
                    self.egpneighintervalhello.value_namespace = name_space
                    self.egpneighintervalhello.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighIntervalPoll"):
                    self.egpneighintervalpoll = value
                    self.egpneighintervalpoll.value_namespace = name_space
                    self.egpneighintervalpoll.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighMode"):
                    self.egpneighmode = value
                    self.egpneighmode.value_namespace = name_space
                    self.egpneighmode.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighOutErrMsgs"):
                    self.egpneighouterrmsgs = value
                    self.egpneighouterrmsgs.value_namespace = name_space
                    self.egpneighouterrmsgs.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighOutErrs"):
                    self.egpneighouterrs = value
                    self.egpneighouterrs.value_namespace = name_space
                    self.egpneighouterrs.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighOutMsgs"):
                    self.egpneighoutmsgs = value
                    self.egpneighoutmsgs.value_namespace = name_space
                    self.egpneighoutmsgs.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighState"):
                    self.egpneighstate = value
                    self.egpneighstate.value_namespace = name_space
                    self.egpneighstate.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighStateDowns"):
                    self.egpneighstatedowns = value
                    self.egpneighstatedowns.value_namespace = name_space
                    self.egpneighstatedowns.value_namespace_prefix = name_space_prefix
                if(value_path == "egpNeighStateUps"):
                    self.egpneighstateups = value
                    self.egpneighstateups.value_namespace = name_space
                    self.egpneighstateups.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.egpneighentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.egpneighentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "egpNeighTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RFC1213-MIB:RFC1213-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "egpNeighEntry"):
                for c in self.egpneighentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rfc1213Mib.Egpneightable.Egpneighentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.egpneighentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "egpNeighEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.attable is not None and self.attable.has_data()) or
            (self.egp is not None and self.egp.has_data()) or
            (self.egpneightable is not None and self.egpneightable.has_data()) or
            (self.icmp is not None and self.icmp.has_data()) or
            (self.iftable is not None and self.iftable.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.ip is not None and self.ip.has_data()) or
            (self.ipaddrtable is not None and self.ipaddrtable.has_data()) or
            (self.ipnettomediatable is not None and self.ipnettomediatable.has_data()) or
            (self.iproutetable is not None and self.iproutetable.has_data()) or
            (self.snmp is not None and self.snmp.has_data()) or
            (self.system is not None and self.system.has_data()) or
            (self.tcp is not None and self.tcp.has_data()) or
            (self.tcpconntable is not None and self.tcpconntable.has_data()) or
            (self.udp is not None and self.udp.has_data()) or
            (self.udptable is not None and self.udptable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.attable is not None and self.attable.has_operation()) or
            (self.egp is not None and self.egp.has_operation()) or
            (self.egpneightable is not None and self.egpneightable.has_operation()) or
            (self.icmp is not None and self.icmp.has_operation()) or
            (self.iftable is not None and self.iftable.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.ip is not None and self.ip.has_operation()) or
            (self.ipaddrtable is not None and self.ipaddrtable.has_operation()) or
            (self.ipnettomediatable is not None and self.ipnettomediatable.has_operation()) or
            (self.iproutetable is not None and self.iproutetable.has_operation()) or
            (self.snmp is not None and self.snmp.has_operation()) or
            (self.system is not None and self.system.has_operation()) or
            (self.tcp is not None and self.tcp.has_operation()) or
            (self.tcpconntable is not None and self.tcpconntable.has_operation()) or
            (self.udp is not None and self.udp.has_operation()) or
            (self.udptable is not None and self.udptable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "RFC1213-MIB:RFC1213-MIB" + path_buffer

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

        if (child_yang_name == "atTable"):
            if (self.attable is None):
                self.attable = Rfc1213Mib.Attable()
                self.attable.parent = self
                self._children_name_map["attable"] = "atTable"
            return self.attable

        if (child_yang_name == "egp"):
            if (self.egp is None):
                self.egp = Rfc1213Mib.Egp()
                self.egp.parent = self
                self._children_name_map["egp"] = "egp"
            return self.egp

        if (child_yang_name == "egpNeighTable"):
            if (self.egpneightable is None):
                self.egpneightable = Rfc1213Mib.Egpneightable()
                self.egpneightable.parent = self
                self._children_name_map["egpneightable"] = "egpNeighTable"
            return self.egpneightable

        if (child_yang_name == "icmp"):
            if (self.icmp is None):
                self.icmp = Rfc1213Mib.Icmp()
                self.icmp.parent = self
                self._children_name_map["icmp"] = "icmp"
            return self.icmp

        if (child_yang_name == "ifTable"):
            if (self.iftable is None):
                self.iftable = Rfc1213Mib.Iftable()
                self.iftable.parent = self
                self._children_name_map["iftable"] = "ifTable"
            return self.iftable

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Rfc1213Mib.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "ip"):
            if (self.ip is None):
                self.ip = Rfc1213Mib.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
            return self.ip

        if (child_yang_name == "ipAddrTable"):
            if (self.ipaddrtable is None):
                self.ipaddrtable = Rfc1213Mib.Ipaddrtable()
                self.ipaddrtable.parent = self
                self._children_name_map["ipaddrtable"] = "ipAddrTable"
            return self.ipaddrtable

        if (child_yang_name == "ipNetToMediaTable"):
            if (self.ipnettomediatable is None):
                self.ipnettomediatable = Rfc1213Mib.Ipnettomediatable()
                self.ipnettomediatable.parent = self
                self._children_name_map["ipnettomediatable"] = "ipNetToMediaTable"
            return self.ipnettomediatable

        if (child_yang_name == "ipRouteTable"):
            if (self.iproutetable is None):
                self.iproutetable = Rfc1213Mib.Iproutetable()
                self.iproutetable.parent = self
                self._children_name_map["iproutetable"] = "ipRouteTable"
            return self.iproutetable

        if (child_yang_name == "snmp"):
            if (self.snmp is None):
                self.snmp = Rfc1213Mib.Snmp()
                self.snmp.parent = self
                self._children_name_map["snmp"] = "snmp"
            return self.snmp

        if (child_yang_name == "system"):
            if (self.system is None):
                self.system = Rfc1213Mib.System()
                self.system.parent = self
                self._children_name_map["system"] = "system"
            return self.system

        if (child_yang_name == "tcp"):
            if (self.tcp is None):
                self.tcp = Rfc1213Mib.Tcp()
                self.tcp.parent = self
                self._children_name_map["tcp"] = "tcp"
            return self.tcp

        if (child_yang_name == "tcpConnTable"):
            if (self.tcpconntable is None):
                self.tcpconntable = Rfc1213Mib.Tcpconntable()
                self.tcpconntable.parent = self
                self._children_name_map["tcpconntable"] = "tcpConnTable"
            return self.tcpconntable

        if (child_yang_name == "udp"):
            if (self.udp is None):
                self.udp = Rfc1213Mib.Udp()
                self.udp.parent = self
                self._children_name_map["udp"] = "udp"
            return self.udp

        if (child_yang_name == "udpTable"):
            if (self.udptable is None):
                self.udptable = Rfc1213Mib.Udptable()
                self.udptable.parent = self
                self._children_name_map["udptable"] = "udpTable"
            return self.udptable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "atTable" or name == "egp" or name == "egpNeighTable" or name == "icmp" or name == "ifTable" or name == "interfaces" or name == "ip" or name == "ipAddrTable" or name == "ipNetToMediaTable" or name == "ipRouteTable" or name == "snmp" or name == "system" or name == "tcp" or name == "tcpConnTable" or name == "udp" or name == "udpTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rfc1213Mib()
        return self._top_entity

