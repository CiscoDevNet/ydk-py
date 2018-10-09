""" RFC1213_MIB 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class RFC1213MIB(Entity):
    """
    
    
    .. attribute:: system
    
    	
    	**type**\:  :py:class:`System <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.System>`
    
    .. attribute:: interfaces
    
    	
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Interfaces>`
    
    .. attribute:: ip
    
    	
    	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Ip>`
    
    .. attribute:: icmp
    
    	
    	**type**\:  :py:class:`Icmp <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Icmp>`
    
    .. attribute:: tcp
    
    	
    	**type**\:  :py:class:`Tcp <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Tcp>`
    
    .. attribute:: udp
    
    	
    	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Udp>`
    
    .. attribute:: egp
    
    	
    	**type**\:  :py:class:`Egp <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Egp>`
    
    .. attribute:: snmp
    
    	
    	**type**\:  :py:class:`Snmp <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Snmp>`
    
    .. attribute:: iftable
    
    	A list of interface entries.  The number of entries is given by the value of ifNumber
    	**type**\:  :py:class:`IfTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IfTable>`
    
    .. attribute:: attable
    
    	The Address Translation tables contain the NetworkAddress to `physical' address equivalences. Some interfaces do not use translation tables for determining address equivalences (e.g., DDN\-X.25 has an algorithmic method); if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries
    	**type**\:  :py:class:`AtTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.AtTable>`
    
    	**status**\: obsolete
    
    .. attribute:: ipaddrtable
    
    	The table of addressing information relevant to this entity's IP addresses
    	**type**\:  :py:class:`IpAddrTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpAddrTable>`
    
    .. attribute:: iproutetable
    
    	This entity's IP Routing table
    	**type**\:  :py:class:`IpRouteTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpRouteTable>`
    
    .. attribute:: ipnettomediatable
    
    	The IP Address Translation table used for mapping from IP addresses to physical addresses
    	**type**\:  :py:class:`IpNetToMediaTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpNetToMediaTable>`
    
    .. attribute:: tcpconntable
    
    	A table containing TCP connection\-specific information
    	**type**\:  :py:class:`TcpConnTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.TcpConnTable>`
    
    .. attribute:: udptable
    
    	A table containing UDP listener information
    	**type**\:  :py:class:`UdpTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.UdpTable>`
    
    .. attribute:: egpneightable
    
    	The EGP neighbor table
    	**type**\:  :py:class:`EgpNeighTable <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.EgpNeighTable>`
    
    

    """

    _prefix = 'RFC1213-MIB'

    def __init__(self):
        super(RFC1213MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "RFC1213-MIB"
        self.yang_parent_name = "RFC1213-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("system", ("system", RFC1213MIB.System)), ("interfaces", ("interfaces", RFC1213MIB.Interfaces)), ("ip", ("ip", RFC1213MIB.Ip)), ("icmp", ("icmp", RFC1213MIB.Icmp)), ("tcp", ("tcp", RFC1213MIB.Tcp)), ("udp", ("udp", RFC1213MIB.Udp)), ("egp", ("egp", RFC1213MIB.Egp)), ("snmp", ("snmp", RFC1213MIB.Snmp)), ("ifTable", ("iftable", RFC1213MIB.IfTable)), ("atTable", ("attable", RFC1213MIB.AtTable)), ("ipAddrTable", ("ipaddrtable", RFC1213MIB.IpAddrTable)), ("ipRouteTable", ("iproutetable", RFC1213MIB.IpRouteTable)), ("ipNetToMediaTable", ("ipnettomediatable", RFC1213MIB.IpNetToMediaTable)), ("tcpConnTable", ("tcpconntable", RFC1213MIB.TcpConnTable)), ("udpTable", ("udptable", RFC1213MIB.UdpTable)), ("egpNeighTable", ("egpneightable", RFC1213MIB.EgpNeighTable))])
        self._leafs = OrderedDict()

        self.system = RFC1213MIB.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"

        self.interfaces = RFC1213MIB.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.ip = RFC1213MIB.Ip()
        self.ip.parent = self
        self._children_name_map["ip"] = "ip"

        self.icmp = RFC1213MIB.Icmp()
        self.icmp.parent = self
        self._children_name_map["icmp"] = "icmp"

        self.tcp = RFC1213MIB.Tcp()
        self.tcp.parent = self
        self._children_name_map["tcp"] = "tcp"

        self.udp = RFC1213MIB.Udp()
        self.udp.parent = self
        self._children_name_map["udp"] = "udp"

        self.egp = RFC1213MIB.Egp()
        self.egp.parent = self
        self._children_name_map["egp"] = "egp"

        self.snmp = RFC1213MIB.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"

        self.iftable = RFC1213MIB.IfTable()
        self.iftable.parent = self
        self._children_name_map["iftable"] = "ifTable"

        self.attable = RFC1213MIB.AtTable()
        self.attable.parent = self
        self._children_name_map["attable"] = "atTable"

        self.ipaddrtable = RFC1213MIB.IpAddrTable()
        self.ipaddrtable.parent = self
        self._children_name_map["ipaddrtable"] = "ipAddrTable"

        self.iproutetable = RFC1213MIB.IpRouteTable()
        self.iproutetable.parent = self
        self._children_name_map["iproutetable"] = "ipRouteTable"

        self.ipnettomediatable = RFC1213MIB.IpNetToMediaTable()
        self.ipnettomediatable.parent = self
        self._children_name_map["ipnettomediatable"] = "ipNetToMediaTable"

        self.tcpconntable = RFC1213MIB.TcpConnTable()
        self.tcpconntable.parent = self
        self._children_name_map["tcpconntable"] = "tcpConnTable"

        self.udptable = RFC1213MIB.UdpTable()
        self.udptable.parent = self
        self._children_name_map["udptable"] = "udpTable"

        self.egpneightable = RFC1213MIB.EgpNeighTable()
        self.egpneightable.parent = self
        self._children_name_map["egpneightable"] = "egpNeighTable"
        self._segment_path = lambda: "RFC1213-MIB:RFC1213-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RFC1213MIB, [], name, value)


    class System(Entity):
        """
        
        
        .. attribute:: sysdescr
        
        	A textual description of the entity.  This value should include the full name and version identification of the system's hardware type, software operating\-system, and networking software.  It is mandatory that this only contain printable ASCII characters
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysobjectid
        
        	The vendor's authoritative identification of the network management subsystem contained in the entity.  This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed.  For example, if vendor `Flintstones, Inc.' was assigned the subtree 1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'
        	**type**\: str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        .. attribute:: sysuptime
        
        	The time (in hundredths of a second) since the network management portion of the system was last re\-initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: syscontact
        
        	The textual identification of the contact person for this managed node, together with information on how to contact this person
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysname
        
        	An administratively\-assigned name for this managed node.  By convention, this is the node's fully\-qualified domain name
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: syslocation
        
        	The physical location of this node (e.g., `telephone closet, 3rd floor')
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysservices
        
        	A value which indicates the set of services that this entity primarily offers.  The value is a sum.  This sum initially takes the value zero, Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L \- 1) is added to the sum.  For example, a node which performs primarily routing functions would have a value of 4 (2^(3\-1)).  In contrast, a node which is a host offering application services would have a value of 72 (2^(4\-1) + 2^(7\-1)).  Note that in the context of the Internet suite of protocols, values should be calculated accordingly\:       layer  functionality          1  physical (e.g., repeaters)          2  datalink/subnetwork (e.g., bridges)          3  internet (e.g., IP gateways)          4  end\-to\-end  (e.g., IP hosts)          7  applications (e.g., mail relays)  For systems including OSI protocols, layers 5 and 6 may also be counted
        	**type**\: int
        
        	**range:** 0..127
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sysdescr', (YLeaf(YType.str, 'sysDescr'), ['str'])),
                ('sysobjectid', (YLeaf(YType.str, 'sysObjectID'), ['str'])),
                ('sysuptime', (YLeaf(YType.uint32, 'sysUpTime'), ['int'])),
                ('syscontact', (YLeaf(YType.str, 'sysContact'), ['str'])),
                ('sysname', (YLeaf(YType.str, 'sysName'), ['str'])),
                ('syslocation', (YLeaf(YType.str, 'sysLocation'), ['str'])),
                ('sysservices', (YLeaf(YType.int32, 'sysServices'), ['int'])),
            ])
            self.sysdescr = None
            self.sysobjectid = None
            self.sysuptime = None
            self.syscontact = None
            self.sysname = None
            self.syslocation = None
            self.sysservices = None
            self._segment_path = lambda: "system"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.System, [u'sysdescr', u'sysobjectid', u'sysuptime', u'syscontact', u'sysname', u'syslocation', u'sysservices'], name, value)


    class Interfaces(Entity):
        """
        
        
        .. attribute:: ifnumber
        
        	The number of network interfaces (regardless of their current state) present on this system
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifnumber', (YLeaf(YType.int32, 'ifNumber'), ['int'])),
            ])
            self.ifnumber = None
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Interfaces, [u'ifnumber'], name, value)


    class Ip(Entity):
        """
        
        
        .. attribute:: ipforwarding
        
        	The indication of whether this entity is acting as an IP gateway in respect to the forwarding of datagrams received by, but not addressed to, this entity.  IP gateways forward datagrams.  IP hosts do not (except those source\-routed via the host).  Note that for some managed nodes, this object may take on only a subset of the values possible. Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to change this object to an inappropriate value
        	**type**\:  :py:class:`IpForwarding <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Ip.IpForwarding>`
        
        .. attribute:: ipdefaultttl
        
        	The default value inserted into the Time\-To\-Live field of the IP header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer protocol
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ipinreceives
        
        	The total number of input datagrams received from interfaces, including those received in error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinhdrerrors
        
        	The number of input datagrams discarded due to errors in their IP headers, including bad checksums, version number mismatch, other format errors, time\-to\-live exceeded, errors discovered in processing their IP options, etc
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinaddrerrors
        
        	The number of input datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E).  For entities which are not IP Gateways and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipforwdatagrams
        
        	The number of input datagrams for which this entity was not their final IP destination, as a result of which an attempt was made to find a route to forward them to that final destination. In entities which do not act as IP Gateways, this counter will include only those packets which were Source\-Routed via this entity, and the Source\- Route option processing was successful
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipinunknownprotos
        
        	The number of locally\-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipindiscards
        
        	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipindelivers
        
        	The total number of input datagrams successfully delivered to IP user\-protocols (including ICMP)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutrequests
        
        	The total number of IP datagrams which local IP user\-protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipForwDatagrams
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutdiscards
        
        	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipoutnoroutes
        
        	The number of IP datagrams discarded because no route could be found to transmit them to their destination.  Note that this counter includes any packets counted in ipForwDatagrams which meet this `no\-route' criterion.  Note that this includes any datagrams which a host cannot route because all of its default gateways are down
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmtimeout
        
        	The maximum number of seconds which received fragments are held while they are awaiting reassembly at this entity
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: ipreasmreqds
        
        	The number of IP fragments received which needed to be reassembled at this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmoks
        
        	The number of IP datagrams successfully re\- assembled
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipreasmfails
        
        	The number of failures detected by the IP re\- assembly algorithm (for whatever reason\: timed out, errors, etc).  Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragoks
        
        	The number of IP datagrams that have been successfully fragmented at this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragfails
        
        	The number of IP datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipfragcreates
        
        	The number of IP datagram fragments that have been generated as a result of fragmentation at this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: iproutingdiscards
        
        	The number of routing entries which were chosen to be discarded even though they are valid.  One possible reason for discarding such an entry could be to free\-up buffer space for other routing entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Ip, self).__init__()

            self.yang_name = "ip"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ipforwarding', (YLeaf(YType.enumeration, 'ipForwarding'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'Ip.IpForwarding')])),
                ('ipdefaultttl', (YLeaf(YType.int32, 'ipDefaultTTL'), ['int'])),
                ('ipinreceives', (YLeaf(YType.uint32, 'ipInReceives'), ['int'])),
                ('ipinhdrerrors', (YLeaf(YType.uint32, 'ipInHdrErrors'), ['int'])),
                ('ipinaddrerrors', (YLeaf(YType.uint32, 'ipInAddrErrors'), ['int'])),
                ('ipforwdatagrams', (YLeaf(YType.uint32, 'ipForwDatagrams'), ['int'])),
                ('ipinunknownprotos', (YLeaf(YType.uint32, 'ipInUnknownProtos'), ['int'])),
                ('ipindiscards', (YLeaf(YType.uint32, 'ipInDiscards'), ['int'])),
                ('ipindelivers', (YLeaf(YType.uint32, 'ipInDelivers'), ['int'])),
                ('ipoutrequests', (YLeaf(YType.uint32, 'ipOutRequests'), ['int'])),
                ('ipoutdiscards', (YLeaf(YType.uint32, 'ipOutDiscards'), ['int'])),
                ('ipoutnoroutes', (YLeaf(YType.uint32, 'ipOutNoRoutes'), ['int'])),
                ('ipreasmtimeout', (YLeaf(YType.int32, 'ipReasmTimeout'), ['int'])),
                ('ipreasmreqds', (YLeaf(YType.uint32, 'ipReasmReqds'), ['int'])),
                ('ipreasmoks', (YLeaf(YType.uint32, 'ipReasmOKs'), ['int'])),
                ('ipreasmfails', (YLeaf(YType.uint32, 'ipReasmFails'), ['int'])),
                ('ipfragoks', (YLeaf(YType.uint32, 'ipFragOKs'), ['int'])),
                ('ipfragfails', (YLeaf(YType.uint32, 'ipFragFails'), ['int'])),
                ('ipfragcreates', (YLeaf(YType.uint32, 'ipFragCreates'), ['int'])),
                ('iproutingdiscards', (YLeaf(YType.uint32, 'ipRoutingDiscards'), ['int'])),
            ])
            self.ipforwarding = None
            self.ipdefaultttl = None
            self.ipinreceives = None
            self.ipinhdrerrors = None
            self.ipinaddrerrors = None
            self.ipforwdatagrams = None
            self.ipinunknownprotos = None
            self.ipindiscards = None
            self.ipindelivers = None
            self.ipoutrequests = None
            self.ipoutdiscards = None
            self.ipoutnoroutes = None
            self.ipreasmtimeout = None
            self.ipreasmreqds = None
            self.ipreasmoks = None
            self.ipreasmfails = None
            self.ipfragoks = None
            self.ipfragfails = None
            self.ipfragcreates = None
            self.iproutingdiscards = None
            self._segment_path = lambda: "ip"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Ip, [u'ipforwarding', u'ipdefaultttl', u'ipinreceives', u'ipinhdrerrors', u'ipinaddrerrors', u'ipforwdatagrams', u'ipinunknownprotos', u'ipindiscards', u'ipindelivers', u'ipoutrequests', u'ipoutdiscards', u'ipoutnoroutes', u'ipreasmtimeout', u'ipreasmreqds', u'ipreasmoks', u'ipreasmfails', u'ipfragoks', u'ipfragfails', u'ipfragcreates', u'iproutingdiscards'], name, value)

        class IpForwarding(Enum):
            """
            IpForwarding (Enum Class)

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



    class Icmp(Entity):
        """
        
        
        .. attribute:: icmpinmsgs
        
        	The total number of ICMP messages which the entity received.  Note that this counter includes all those counted by icmpInErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinerrors
        
        	The number of ICMP messages which the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpindestunreachs
        
        	The number of ICMP Destination Unreachable messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimeexcds
        
        	The number of ICMP Time Exceeded messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinparmprobs
        
        	The number of ICMP Parameter Problem messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinsrcquenchs
        
        	The number of ICMP Source Quench messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinredirects
        
        	The number of ICMP Redirect messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinechos
        
        	The number of ICMP Echo (request) messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinechoreps
        
        	The number of ICMP Echo Reply messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimestamps
        
        	The number of ICMP Timestamp (request) messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpintimestampreps
        
        	The number of ICMP Timestamp Reply messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinaddrmasks
        
        	The number of ICMP Address Mask Request messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpinaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutmsgs
        
        	The total number of ICMP messages which this entity attempted to send.  Note that this counter includes all those counted by icmpOutErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouterrors
        
        	The number of ICMP messages which this entity did not send due to problems discovered within ICMP such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer such as the inability of IP to route the resultant datagram.  In some implementations there may be no types of error which contribute to this counter's value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutdestunreachs
        
        	The number of ICMP Destination Unreachable messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimeexcds
        
        	The number of ICMP Time Exceeded messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutparmprobs
        
        	The number of ICMP Parameter Problem messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutsrcquenchs
        
        	The number of ICMP Source Quench messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutredirects
        
        	The number of ICMP Redirect messages sent.  For a host, this object will always be zero, since hosts do not send redirects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutechos
        
        	The number of ICMP Echo (request) messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutechoreps
        
        	The number of ICMP Echo Reply messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimestamps
        
        	The number of ICMP Timestamp (request) messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpouttimestampreps
        
        	The number of ICMP Timestamp Reply messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutaddrmasks
        
        	The number of ICMP Address Mask Request messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: icmpoutaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Icmp, self).__init__()

            self.yang_name = "icmp"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('icmpinmsgs', (YLeaf(YType.uint32, 'icmpInMsgs'), ['int'])),
                ('icmpinerrors', (YLeaf(YType.uint32, 'icmpInErrors'), ['int'])),
                ('icmpindestunreachs', (YLeaf(YType.uint32, 'icmpInDestUnreachs'), ['int'])),
                ('icmpintimeexcds', (YLeaf(YType.uint32, 'icmpInTimeExcds'), ['int'])),
                ('icmpinparmprobs', (YLeaf(YType.uint32, 'icmpInParmProbs'), ['int'])),
                ('icmpinsrcquenchs', (YLeaf(YType.uint32, 'icmpInSrcQuenchs'), ['int'])),
                ('icmpinredirects', (YLeaf(YType.uint32, 'icmpInRedirects'), ['int'])),
                ('icmpinechos', (YLeaf(YType.uint32, 'icmpInEchos'), ['int'])),
                ('icmpinechoreps', (YLeaf(YType.uint32, 'icmpInEchoReps'), ['int'])),
                ('icmpintimestamps', (YLeaf(YType.uint32, 'icmpInTimestamps'), ['int'])),
                ('icmpintimestampreps', (YLeaf(YType.uint32, 'icmpInTimestampReps'), ['int'])),
                ('icmpinaddrmasks', (YLeaf(YType.uint32, 'icmpInAddrMasks'), ['int'])),
                ('icmpinaddrmaskreps', (YLeaf(YType.uint32, 'icmpInAddrMaskReps'), ['int'])),
                ('icmpoutmsgs', (YLeaf(YType.uint32, 'icmpOutMsgs'), ['int'])),
                ('icmpouterrors', (YLeaf(YType.uint32, 'icmpOutErrors'), ['int'])),
                ('icmpoutdestunreachs', (YLeaf(YType.uint32, 'icmpOutDestUnreachs'), ['int'])),
                ('icmpouttimeexcds', (YLeaf(YType.uint32, 'icmpOutTimeExcds'), ['int'])),
                ('icmpoutparmprobs', (YLeaf(YType.uint32, 'icmpOutParmProbs'), ['int'])),
                ('icmpoutsrcquenchs', (YLeaf(YType.uint32, 'icmpOutSrcQuenchs'), ['int'])),
                ('icmpoutredirects', (YLeaf(YType.uint32, 'icmpOutRedirects'), ['int'])),
                ('icmpoutechos', (YLeaf(YType.uint32, 'icmpOutEchos'), ['int'])),
                ('icmpoutechoreps', (YLeaf(YType.uint32, 'icmpOutEchoReps'), ['int'])),
                ('icmpouttimestamps', (YLeaf(YType.uint32, 'icmpOutTimestamps'), ['int'])),
                ('icmpouttimestampreps', (YLeaf(YType.uint32, 'icmpOutTimestampReps'), ['int'])),
                ('icmpoutaddrmasks', (YLeaf(YType.uint32, 'icmpOutAddrMasks'), ['int'])),
                ('icmpoutaddrmaskreps', (YLeaf(YType.uint32, 'icmpOutAddrMaskReps'), ['int'])),
            ])
            self.icmpinmsgs = None
            self.icmpinerrors = None
            self.icmpindestunreachs = None
            self.icmpintimeexcds = None
            self.icmpinparmprobs = None
            self.icmpinsrcquenchs = None
            self.icmpinredirects = None
            self.icmpinechos = None
            self.icmpinechoreps = None
            self.icmpintimestamps = None
            self.icmpintimestampreps = None
            self.icmpinaddrmasks = None
            self.icmpinaddrmaskreps = None
            self.icmpoutmsgs = None
            self.icmpouterrors = None
            self.icmpoutdestunreachs = None
            self.icmpouttimeexcds = None
            self.icmpoutparmprobs = None
            self.icmpoutsrcquenchs = None
            self.icmpoutredirects = None
            self.icmpoutechos = None
            self.icmpoutechoreps = None
            self.icmpouttimestamps = None
            self.icmpouttimestampreps = None
            self.icmpoutaddrmasks = None
            self.icmpoutaddrmaskreps = None
            self._segment_path = lambda: "icmp"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Icmp, [u'icmpinmsgs', u'icmpinerrors', u'icmpindestunreachs', u'icmpintimeexcds', u'icmpinparmprobs', u'icmpinsrcquenchs', u'icmpinredirects', u'icmpinechos', u'icmpinechoreps', u'icmpintimestamps', u'icmpintimestampreps', u'icmpinaddrmasks', u'icmpinaddrmaskreps', u'icmpoutmsgs', u'icmpouterrors', u'icmpoutdestunreachs', u'icmpouttimeexcds', u'icmpoutparmprobs', u'icmpoutsrcquenchs', u'icmpoutredirects', u'icmpoutechos', u'icmpoutechoreps', u'icmpouttimestamps', u'icmpouttimestampreps', u'icmpoutaddrmasks', u'icmpoutaddrmaskreps'], name, value)


    class Tcp(Entity):
        """
        
        
        .. attribute:: tcprtoalgorithm
        
        	The algorithm used to determine the timeout value used for retransmitting unacknowledged octets
        	**type**\:  :py:class:`TcpRtoAlgorithm <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Tcp.TcpRtoAlgorithm>`
        
        .. attribute:: tcprtomin
        
        	The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds.  More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout.  In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the LBOUND quantity described in RFC 793
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcprtomax
        
        	The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds.  More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout.  In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the UBOUND quantity described in RFC 793
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcpmaxconn
        
        	The limit on the total number of TCP connections the entity can support.  In entities where the maximum number of connections is dynamic, this object should contain the value \-1
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: tcpactiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-SENT state from the CLOSED state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcppassiveopens
        
        	The number of times TCP connections have made a direct transition to the SYN\-RCVD state from the LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpattemptfails
        
        	The number of times TCP connections have made a direct transition to the CLOSED state from either the SYN\-SENT state or the SYN\-RCVD state, plus the number of times TCP connections have made a direct transition to the LISTEN state from the SYN\-RCVD state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpestabresets
        
        	The number of times TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE\-WAIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpcurrestab
        
        	The number of TCP connections for which the current state is either ESTABLISHED or CLOSE\- WAIT
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinsegs
        
        	The total number of segments received, including those received in error.  This count includes segments received on currently established connections
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutsegs
        
        	The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpretranssegs
        
        	The total number of segments retransmitted \- that is, the number of TCP segments transmitted containing one or more previously transmitted octets
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpinerrs
        
        	The total number of segments received in error (e.g., bad TCP checksums)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcpoutrsts
        
        	The number of TCP segments sent containing the RST flag
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Tcp, self).__init__()

            self.yang_name = "tcp"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('tcprtoalgorithm', (YLeaf(YType.enumeration, 'tcpRtoAlgorithm'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'Tcp.TcpRtoAlgorithm')])),
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
            self._segment_path = lambda: "tcp"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Tcp, [u'tcprtoalgorithm', u'tcprtomin', u'tcprtomax', u'tcpmaxconn', u'tcpactiveopens', u'tcppassiveopens', u'tcpattemptfails', u'tcpestabresets', u'tcpcurrestab', u'tcpinsegs', u'tcpoutsegs', u'tcpretranssegs', u'tcpinerrs', u'tcpoutrsts'], name, value)

        class TcpRtoAlgorithm(Enum):
            """
            TcpRtoAlgorithm (Enum Class)

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



    class Udp(Entity):
        """
        
        
        .. attribute:: udpindatagrams
        
        	The total number of UDP datagrams delivered to UDP users
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpnoports
        
        	The total number of received UDP datagrams for which there was no application at the destination port
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpinerrors
        
        	The number of received UDP datagrams that could not be delivered for reasons other than the lack of an application at the destination port
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: udpoutdatagrams
        
        	The total number of UDP datagrams sent from this entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Udp, self).__init__()

            self.yang_name = "udp"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('udpindatagrams', (YLeaf(YType.uint32, 'udpInDatagrams'), ['int'])),
                ('udpnoports', (YLeaf(YType.uint32, 'udpNoPorts'), ['int'])),
                ('udpinerrors', (YLeaf(YType.uint32, 'udpInErrors'), ['int'])),
                ('udpoutdatagrams', (YLeaf(YType.uint32, 'udpOutDatagrams'), ['int'])),
            ])
            self.udpindatagrams = None
            self.udpnoports = None
            self.udpinerrors = None
            self.udpoutdatagrams = None
            self._segment_path = lambda: "udp"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Udp, [u'udpindatagrams', u'udpnoports', u'udpinerrors', u'udpoutdatagrams'], name, value)


    class Egp(Entity):
        """
        
        
        .. attribute:: egpinmsgs
        
        	The number of EGP messages received without error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpinerrors
        
        	The number of EGP messages received that proved to be in error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpoutmsgs
        
        	The total number of locally generated EGP messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpouterrors
        
        	The number of locally generated EGP messages not sent due to resource limitations within an EGP entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: egpas
        
        	The autonomous system number of this EGP entity
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Egp, self).__init__()

            self.yang_name = "egp"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('egpinmsgs', (YLeaf(YType.uint32, 'egpInMsgs'), ['int'])),
                ('egpinerrors', (YLeaf(YType.uint32, 'egpInErrors'), ['int'])),
                ('egpoutmsgs', (YLeaf(YType.uint32, 'egpOutMsgs'), ['int'])),
                ('egpouterrors', (YLeaf(YType.uint32, 'egpOutErrors'), ['int'])),
                ('egpas', (YLeaf(YType.int32, 'egpAs'), ['int'])),
            ])
            self.egpinmsgs = None
            self.egpinerrors = None
            self.egpoutmsgs = None
            self.egpouterrors = None
            self.egpas = None
            self._segment_path = lambda: "egp"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Egp, [u'egpinmsgs', u'egpinerrors', u'egpoutmsgs', u'egpouterrors', u'egpas'], name, value)


    class Snmp(Entity):
        """
        
        
        .. attribute:: snmpinpkts
        
        	The total number of Messages delivered to the SNMP entity from the transport service
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutpkts
        
        	The total number of SNMP Messages which were passed from the SNMP protocol entity to the transport service
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadversions
        
        	The total number of SNMP Messages which were delivered to the SNMP protocol entity and were for an unsupported SNMP version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunitynames
        
        	The total number of SNMP Messages delivered to the SNMP protocol entity which used a SNMP community name not known to said entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunityuses
        
        	The total number of SNMP Messages delivered to the SNMP protocol entity which represented an SNMP operation which was not allowed by the SNMP community named in the Message
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinasnparseerrs
        
        	The total number of ASN.1 or BER errors encountered by the SNMP protocol entity when decoding received SNMP Messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintoobigs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `tooBig'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinnosuchnames
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `noSuchName'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadvalues
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `badValue'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinreadonlys
        
        	The total number valid SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `readOnly'.  It should be noted that it is a protocol error to generate an SNMP PDU which contains the value `readOnly' in the error\-status field, as such this object is provided as a means of detecting incorrect implementations of the SNMP
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingenerrs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field is `genErr'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintotalreqvars
        
        	The total number of MIB objects which have been retrieved successfully by the SNMP protocol entity as the result of receiving valid SNMP Get\-Request and Get\-Next PDUs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintotalsetvars
        
        	The total number of MIB objects which have been altered successfully by the SNMP protocol entity as the result of receiving valid SNMP Set\-Request PDUs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintraps
        
        	The total number of SNMP Trap PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpouttoobigs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `tooBig.'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutnosuchnames
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status is `noSuchName'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutbadvalues
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `badValue'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgenerrs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field is `genErr'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutgetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpouttraps
        
        	The total number of SNMP Trap PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpenableauthentraps
        
        	Indicates whether the SNMP agent process is permitted to generate authentication\-failure traps.  The value of this object overrides any configuration information; as such, it provides a means whereby all authentication\-failure traps may be disabled.  Note that it is strongly recommended that this object be stored in non\-volatile memory so that it remains constant between re\-initializations of the network management system
        	**type**\:  :py:class:`SnmpEnableAuthenTraps <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.Snmp.SnmpEnableAuthenTraps>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpinpkts', (YLeaf(YType.uint32, 'snmpInPkts'), ['int'])),
                ('snmpoutpkts', (YLeaf(YType.uint32, 'snmpOutPkts'), ['int'])),
                ('snmpinbadversions', (YLeaf(YType.uint32, 'snmpInBadVersions'), ['int'])),
                ('snmpinbadcommunitynames', (YLeaf(YType.uint32, 'snmpInBadCommunityNames'), ['int'])),
                ('snmpinbadcommunityuses', (YLeaf(YType.uint32, 'snmpInBadCommunityUses'), ['int'])),
                ('snmpinasnparseerrs', (YLeaf(YType.uint32, 'snmpInASNParseErrs'), ['int'])),
                ('snmpintoobigs', (YLeaf(YType.uint32, 'snmpInTooBigs'), ['int'])),
                ('snmpinnosuchnames', (YLeaf(YType.uint32, 'snmpInNoSuchNames'), ['int'])),
                ('snmpinbadvalues', (YLeaf(YType.uint32, 'snmpInBadValues'), ['int'])),
                ('snmpinreadonlys', (YLeaf(YType.uint32, 'snmpInReadOnlys'), ['int'])),
                ('snmpingenerrs', (YLeaf(YType.uint32, 'snmpInGenErrs'), ['int'])),
                ('snmpintotalreqvars', (YLeaf(YType.uint32, 'snmpInTotalReqVars'), ['int'])),
                ('snmpintotalsetvars', (YLeaf(YType.uint32, 'snmpInTotalSetVars'), ['int'])),
                ('snmpingetrequests', (YLeaf(YType.uint32, 'snmpInGetRequests'), ['int'])),
                ('snmpingetnexts', (YLeaf(YType.uint32, 'snmpInGetNexts'), ['int'])),
                ('snmpinsetrequests', (YLeaf(YType.uint32, 'snmpInSetRequests'), ['int'])),
                ('snmpingetresponses', (YLeaf(YType.uint32, 'snmpInGetResponses'), ['int'])),
                ('snmpintraps', (YLeaf(YType.uint32, 'snmpInTraps'), ['int'])),
                ('snmpouttoobigs', (YLeaf(YType.uint32, 'snmpOutTooBigs'), ['int'])),
                ('snmpoutnosuchnames', (YLeaf(YType.uint32, 'snmpOutNoSuchNames'), ['int'])),
                ('snmpoutbadvalues', (YLeaf(YType.uint32, 'snmpOutBadValues'), ['int'])),
                ('snmpoutgenerrs', (YLeaf(YType.uint32, 'snmpOutGenErrs'), ['int'])),
                ('snmpoutgetrequests', (YLeaf(YType.uint32, 'snmpOutGetRequests'), ['int'])),
                ('snmpoutgetnexts', (YLeaf(YType.uint32, 'snmpOutGetNexts'), ['int'])),
                ('snmpoutsetrequests', (YLeaf(YType.uint32, 'snmpOutSetRequests'), ['int'])),
                ('snmpoutgetresponses', (YLeaf(YType.uint32, 'snmpOutGetResponses'), ['int'])),
                ('snmpouttraps', (YLeaf(YType.uint32, 'snmpOutTraps'), ['int'])),
                ('snmpenableauthentraps', (YLeaf(YType.enumeration, 'snmpEnableAuthenTraps'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'Snmp.SnmpEnableAuthenTraps')])),
            ])
            self.snmpinpkts = None
            self.snmpoutpkts = None
            self.snmpinbadversions = None
            self.snmpinbadcommunitynames = None
            self.snmpinbadcommunityuses = None
            self.snmpinasnparseerrs = None
            self.snmpintoobigs = None
            self.snmpinnosuchnames = None
            self.snmpinbadvalues = None
            self.snmpinreadonlys = None
            self.snmpingenerrs = None
            self.snmpintotalreqvars = None
            self.snmpintotalsetvars = None
            self.snmpingetrequests = None
            self.snmpingetnexts = None
            self.snmpinsetrequests = None
            self.snmpingetresponses = None
            self.snmpintraps = None
            self.snmpouttoobigs = None
            self.snmpoutnosuchnames = None
            self.snmpoutbadvalues = None
            self.snmpoutgenerrs = None
            self.snmpoutgetrequests = None
            self.snmpoutgetnexts = None
            self.snmpoutsetrequests = None
            self.snmpoutgetresponses = None
            self.snmpouttraps = None
            self.snmpenableauthentraps = None
            self._segment_path = lambda: "snmp"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.Snmp, [u'snmpinpkts', u'snmpoutpkts', u'snmpinbadversions', u'snmpinbadcommunitynames', u'snmpinbadcommunityuses', u'snmpinasnparseerrs', u'snmpintoobigs', u'snmpinnosuchnames', u'snmpinbadvalues', u'snmpinreadonlys', u'snmpingenerrs', u'snmpintotalreqvars', u'snmpintotalsetvars', u'snmpingetrequests', u'snmpingetnexts', u'snmpinsetrequests', u'snmpingetresponses', u'snmpintraps', u'snmpouttoobigs', u'snmpoutnosuchnames', u'snmpoutbadvalues', u'snmpoutgenerrs', u'snmpoutgetrequests', u'snmpoutgetnexts', u'snmpoutsetrequests', u'snmpoutgetresponses', u'snmpouttraps', u'snmpenableauthentraps'], name, value)

        class SnmpEnableAuthenTraps(Enum):
            """
            SnmpEnableAuthenTraps (Enum Class)

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



    class IfTable(Entity):
        """
        A list of interface entries.  The number of
        entries is given by the value of ifNumber.
        
        .. attribute:: ifentry
        
        	An interface entry containing objects at the subnetwork layer and below for a particular interface
        	**type**\: list of  		 :py:class:`IfEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.IfTable, self).__init__()

            self.yang_name = "ifTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ifEntry", ("ifentry", RFC1213MIB.IfTable.IfEntry))])
            self._leafs = OrderedDict()

            self.ifentry = YList(self)
            self._segment_path = lambda: "ifTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.IfTable, [], name, value)


        class IfEntry(Entity):
            """
            An interface entry containing objects at the
            subnetwork layer and below for a particular
            interface.
            
            .. attribute:: ifindex  (key)
            
            	A unique value for each interface.  Its value ranges between 1 and the value of ifNumber.  The value for each interface must remain constant at least from one re\-initialization of the entity's network management system to the next re\- initialization
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifdescr
            
            	A textual string containing information about the interface.  This string should include the name of the manufacturer, the product name and the version of the hardware interface
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: iftype
            
            	The type of interface.  Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention
            	**type**\:  :py:class:`IANAifType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAifType>`
            
            .. attribute:: ifmtu
            
            	The size of the largest datagram which can be sent/received on the interface, specified in octets.  For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifspeed
            
            	An estimate of the interface's current bandwidth in bits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifphysaddress
            
            	The interface's address at the protocol layer immediately `below' the network layer in the protocol stack.  For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length
            	**type**\: str
            
            .. attribute:: ifadminstatus
            
            	The desired state of the interface.  The testing(3) state indicates that no operational packets can be passed
            	**type**\:  :py:class:`IfAdminStatus <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry.IfAdminStatus>`
            
            .. attribute:: ifoperstatus
            
            	The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed
            	**type**\:  :py:class:`IfOperStatus <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry.IfOperStatus>`
            
            .. attribute:: iflastchange
            
            	The value of sysUpTime at the time the interface entered its current operational state.  If the current state was entered prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinoctets
            
            	The total number of octets received on the interface, including framing characters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinucastpkts
            
            	The number of subnetwork\-unicast packets delivered to a higher\-layer protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinnucastpkts
            
            	The number of non\-unicast (i.e., subnetwork\- broadcast or subnetwork\-multicast) packets delivered to a higher\-layer protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifindiscards
            
            	The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinerrors
            
            	The number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinunknownprotos
            
            	The number of packets received via the interface which were discarded because of an unknown or unsupported protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted to a subnetwork\-unicast address, including those that were discarded or not sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutnucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted to a non\- unicast (i.e., a subnetwork\-broadcast or subnetwork\-multicast) address, including those that were discarded or not sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutdiscards
            
            	The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifouterrors
            
            	The number of outbound packets that could not be transmitted because of errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutqlen
            
            	The length of the output packet queue (in packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifspecific
            
            	A reference to MIB definitions specific to the particular media being used to realize the interface.  For example, if the interface is realized by an ethernet, then the value of this object refers to a document defining objects specific to ethernet.  If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.IfTable.IfEntry, self).__init__()

                self.yang_name = "ifEntry"
                self.yang_parent_name = "ifTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.int32, 'ifIndex'), ['int'])),
                    ('ifdescr', (YLeaf(YType.str, 'ifDescr'), ['str'])),
                    ('iftype', (YLeaf(YType.enumeration, 'ifType'), [('ydk.models.cisco_ios_xe.IANAifType_MIB', 'IANAifType', '')])),
                    ('ifmtu', (YLeaf(YType.int32, 'ifMtu'), ['int'])),
                    ('ifspeed', (YLeaf(YType.uint32, 'ifSpeed'), ['int'])),
                    ('ifphysaddress', (YLeaf(YType.str, 'ifPhysAddress'), ['str'])),
                    ('ifadminstatus', (YLeaf(YType.enumeration, 'ifAdminStatus'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'IfTable.IfEntry.IfAdminStatus')])),
                    ('ifoperstatus', (YLeaf(YType.enumeration, 'ifOperStatus'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'IfTable.IfEntry.IfOperStatus')])),
                    ('iflastchange', (YLeaf(YType.uint32, 'ifLastChange'), ['int'])),
                    ('ifinoctets', (YLeaf(YType.uint32, 'ifInOctets'), ['int'])),
                    ('ifinucastpkts', (YLeaf(YType.uint32, 'ifInUcastPkts'), ['int'])),
                    ('ifinnucastpkts', (YLeaf(YType.uint32, 'ifInNUcastPkts'), ['int'])),
                    ('ifindiscards', (YLeaf(YType.uint32, 'ifInDiscards'), ['int'])),
                    ('ifinerrors', (YLeaf(YType.uint32, 'ifInErrors'), ['int'])),
                    ('ifinunknownprotos', (YLeaf(YType.uint32, 'ifInUnknownProtos'), ['int'])),
                    ('ifoutoctets', (YLeaf(YType.uint32, 'ifOutOctets'), ['int'])),
                    ('ifoutucastpkts', (YLeaf(YType.uint32, 'ifOutUcastPkts'), ['int'])),
                    ('ifoutnucastpkts', (YLeaf(YType.uint32, 'ifOutNUcastPkts'), ['int'])),
                    ('ifoutdiscards', (YLeaf(YType.uint32, 'ifOutDiscards'), ['int'])),
                    ('ifouterrors', (YLeaf(YType.uint32, 'ifOutErrors'), ['int'])),
                    ('ifoutqlen', (YLeaf(YType.uint32, 'ifOutQLen'), ['int'])),
                    ('ifspecific', (YLeaf(YType.str, 'ifSpecific'), ['str'])),
                ])
                self.ifindex = None
                self.ifdescr = None
                self.iftype = None
                self.ifmtu = None
                self.ifspeed = None
                self.ifphysaddress = None
                self.ifadminstatus = None
                self.ifoperstatus = None
                self.iflastchange = None
                self.ifinoctets = None
                self.ifinucastpkts = None
                self.ifinnucastpkts = None
                self.ifindiscards = None
                self.ifinerrors = None
                self.ifinunknownprotos = None
                self.ifoutoctets = None
                self.ifoutucastpkts = None
                self.ifoutnucastpkts = None
                self.ifoutdiscards = None
                self.ifouterrors = None
                self.ifoutqlen = None
                self.ifspecific = None
                self._segment_path = lambda: "ifEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/ifTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.IfTable.IfEntry, [u'ifindex', u'ifdescr', u'iftype', u'ifmtu', u'ifspeed', u'ifphysaddress', u'ifadminstatus', u'ifoperstatus', u'iflastchange', u'ifinoctets', u'ifinucastpkts', u'ifinnucastpkts', u'ifindiscards', u'ifinerrors', u'ifinunknownprotos', u'ifoutoctets', u'ifoutucastpkts', u'ifoutnucastpkts', u'ifoutdiscards', u'ifouterrors', u'ifoutqlen', u'ifspecific'], name, value)

            class IfAdminStatus(Enum):
                """
                IfAdminStatus (Enum Class)

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


            class IfOperStatus(Enum):
                """
                IfOperStatus (Enum Class)

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



    class AtTable(Entity):
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
        	**type**\: list of  		 :py:class:`AtEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.AtTable.AtEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.AtTable, self).__init__()

            self.yang_name = "atTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("atEntry", ("atentry", RFC1213MIB.AtTable.AtEntry))])
            self._leafs = OrderedDict()

            self.atentry = YList(self)
            self._segment_path = lambda: "atTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.AtTable, [], name, value)


        class AtEntry(Entity):
            """
            Each entry contains one NetworkAddress to
            `physical' address equivalence.
            
            .. attribute:: atifindex  (key)
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: atifindex_2  (key)
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: atnetaddress  (key)
            
            	The NetworkAddress (e.g., the IP address) corresponding to the media\-dependent `physical' address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: atphysaddress
            
            	The media\-dependent `physical' address.  Setting this object to a null string (one of zero length) has the effect of invaliding the corresponding entry in the atTable object.  That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant atPhysAddress object
            	**type**\: str
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.AtTable.AtEntry, self).__init__()

                self.yang_name = "atEntry"
                self.yang_parent_name = "atTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['atifindex','atifindex_2','atnetaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('atifindex', (YLeaf(YType.int32, 'atIfIndex'), ['int'])),
                    ('atifindex_2', (YLeaf(YType.int32, 'atIfIndex_2'), ['int'])),
                    ('atnetaddress', (YLeaf(YType.str, 'atNetAddress'), ['str'])),
                    ('atphysaddress', (YLeaf(YType.str, 'atPhysAddress'), ['str'])),
                ])
                self.atifindex = None
                self.atifindex_2 = None
                self.atnetaddress = None
                self.atphysaddress = None
                self._segment_path = lambda: "atEntry" + "[atIfIndex='" + str(self.atifindex) + "']" + "[atIfIndex_2='" + str(self.atifindex_2) + "']" + "[atNetAddress='" + str(self.atnetaddress) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/atTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.AtTable.AtEntry, [u'atifindex', u'atifindex_2', u'atnetaddress', u'atphysaddress'], name, value)


    class IpAddrTable(Entity):
        """
        The table of addressing information relevant to
        this entity's IP addresses.
        
        .. attribute:: ipaddrentry
        
        	The addressing information for one of this entity's IP addresses
        	**type**\: list of  		 :py:class:`IpAddrEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpAddrTable.IpAddrEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.IpAddrTable, self).__init__()

            self.yang_name = "ipAddrTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipAddrEntry", ("ipaddrentry", RFC1213MIB.IpAddrTable.IpAddrEntry))])
            self._leafs = OrderedDict()

            self.ipaddrentry = YList(self)
            self._segment_path = lambda: "ipAddrTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.IpAddrTable, [], name, value)


        class IpAddrEntry(Entity):
            """
            The addressing information for one of this
            entity's IP addresses.
            
            .. attribute:: ipadentaddr  (key)
            
            	The IP address to which this entry's addressing information pertains
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipadentifindex
            
            	The index value which uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipadentnetmask
            
            	The subnet mask associated with the IP address of this entry.  The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipadentbcastaddr
            
            	The value of the least\-significant bit in the IP broadcast address used for sending datagrams on the (logical) interface associated with the IP address of this entry.  For example, when the Internet standard all\-ones broadcast address is used, the value will be 1.  This value applies to both the subnet and network broadcasts addresses used by the entity on this (logical) interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipadentreasmmaxsize
            
            	The size of the largest IP datagram which this entity can re\-assemble from incoming IP fragmented datagrams received on this interface
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.IpAddrTable.IpAddrEntry, self).__init__()

                self.yang_name = "ipAddrEntry"
                self.yang_parent_name = "ipAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipadentaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipadentaddr', (YLeaf(YType.str, 'ipAdEntAddr'), ['str'])),
                    ('ipadentifindex', (YLeaf(YType.int32, 'ipAdEntIfIndex'), ['int'])),
                    ('ipadentnetmask', (YLeaf(YType.str, 'ipAdEntNetMask'), ['str'])),
                    ('ipadentbcastaddr', (YLeaf(YType.int32, 'ipAdEntBcastAddr'), ['int'])),
                    ('ipadentreasmmaxsize', (YLeaf(YType.int32, 'ipAdEntReasmMaxSize'), ['int'])),
                ])
                self.ipadentaddr = None
                self.ipadentifindex = None
                self.ipadentnetmask = None
                self.ipadentbcastaddr = None
                self.ipadentreasmmaxsize = None
                self._segment_path = lambda: "ipAddrEntry" + "[ipAdEntAddr='" + str(self.ipadentaddr) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/ipAddrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.IpAddrTable.IpAddrEntry, [u'ipadentaddr', u'ipadentifindex', u'ipadentnetmask', u'ipadentbcastaddr', u'ipadentreasmmaxsize'], name, value)


    class IpRouteTable(Entity):
        """
        This entity's IP Routing table.
        
        .. attribute:: iprouteentry
        
        	A route to a particular destination
        	**type**\: list of  		 :py:class:`IpRouteEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpRouteTable.IpRouteEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.IpRouteTable, self).__init__()

            self.yang_name = "ipRouteTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipRouteEntry", ("iprouteentry", RFC1213MIB.IpRouteTable.IpRouteEntry))])
            self._leafs = OrderedDict()

            self.iprouteentry = YList(self)
            self._segment_path = lambda: "ipRouteTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.IpRouteTable, [], name, value)


        class IpRouteEntry(Entity):
            """
            A route to a particular destination.
            
            .. attribute:: iproutedest  (key)
            
            	The destination IP address of this route.  An entry with a value of 0.0.0.0 is considered a default route.  Multiple routes to a single destination can appear in the table, but access to such multiple entries is dependent on the table\- access mechanisms defined by the network management protocol in use
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iprouteifindex
            
            	The index value which uniquely identifies the local interface through which the next hop of this route should be reached.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric1
            
            	The primary routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric2
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric3
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemetric4
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutenexthop
            
            	The IP address of the next hop of this route. (In the case of a route bound to an interface which is realized via a broadcast media, the value of this field is the agent's IP address on that interface.)
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iproutetype
            
            	The type of route.  Note that the values direct(3) and indirect(4) refer to the notion of direct and indirect routing in the IP architecture.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipRouteTable object.  That is, it effectively disassociates the destination identified with said entry from the route identified with said entry.  It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant ipRouteType object
            	**type**\:  :py:class:`IpRouteType <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteType>`
            
            .. attribute:: iprouteproto
            
            	The routing mechanism via which this route was learned.  Inclusion of values for gateway routing protocols is not intended to imply that hosts should support those protocols
            	**type**\:  :py:class:`IpRouteProto <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpRouteTable.IpRouteEntry.IpRouteProto>`
            
            .. attribute:: iprouteage
            
            	The number of seconds since this route was last updated or otherwise determined to be correct. Note that no semantics of `too old' can be implied except through knowledge of the routing protocol by which the route was learned
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iproutemask
            
            	Indicate the mask to be logical\-ANDed with the destination address before being compared to the value in the ipRouteDest field.  For those systems that do not support arbitrary subnet masks, an agent constructs the value of the ipRouteMask by determining whether the value of the correspondent ipRouteDest field belong to a class\-A, B, or C network, and then using one of\:       mask           network      255.0.0.0      class\-A      255.255.0.0    class\-B      255.255.255.0  class\-C  If the value of the ipRouteDest is 0.0.0.0 (a default route), then the mask value is also 0.0.0.0.  It should be noted that all IP routing subsystems implicitly use this mechanism
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: iproutemetric5
            
            	An alternate routing metric for this route.  The semantics of this metric are determined by the routing\-protocol specified in the route's ipRouteProto value.  If this metric is not used, its value should be set to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: iprouteinfo
            
            	A reference to MIB definitions specific to the particular routing protocol which is responsible for this route, as determined by the value specified in the route's ipRouteProto value.  If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntactically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.IpRouteTable.IpRouteEntry, self).__init__()

                self.yang_name = "ipRouteEntry"
                self.yang_parent_name = "ipRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['iproutedest']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('iproutedest', (YLeaf(YType.str, 'ipRouteDest'), ['str'])),
                    ('iprouteifindex', (YLeaf(YType.int32, 'ipRouteIfIndex'), ['int'])),
                    ('iproutemetric1', (YLeaf(YType.int32, 'ipRouteMetric1'), ['int'])),
                    ('iproutemetric2', (YLeaf(YType.int32, 'ipRouteMetric2'), ['int'])),
                    ('iproutemetric3', (YLeaf(YType.int32, 'ipRouteMetric3'), ['int'])),
                    ('iproutemetric4', (YLeaf(YType.int32, 'ipRouteMetric4'), ['int'])),
                    ('iproutenexthop', (YLeaf(YType.str, 'ipRouteNextHop'), ['str'])),
                    ('iproutetype', (YLeaf(YType.enumeration, 'ipRouteType'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'IpRouteTable.IpRouteEntry.IpRouteType')])),
                    ('iprouteproto', (YLeaf(YType.enumeration, 'ipRouteProto'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'IpRouteTable.IpRouteEntry.IpRouteProto')])),
                    ('iprouteage', (YLeaf(YType.int32, 'ipRouteAge'), ['int'])),
                    ('iproutemask', (YLeaf(YType.str, 'ipRouteMask'), ['str'])),
                    ('iproutemetric5', (YLeaf(YType.int32, 'ipRouteMetric5'), ['int'])),
                    ('iprouteinfo', (YLeaf(YType.str, 'ipRouteInfo'), ['str'])),
                ])
                self.iproutedest = None
                self.iprouteifindex = None
                self.iproutemetric1 = None
                self.iproutemetric2 = None
                self.iproutemetric3 = None
                self.iproutemetric4 = None
                self.iproutenexthop = None
                self.iproutetype = None
                self.iprouteproto = None
                self.iprouteage = None
                self.iproutemask = None
                self.iproutemetric5 = None
                self.iprouteinfo = None
                self._segment_path = lambda: "ipRouteEntry" + "[ipRouteDest='" + str(self.iproutedest) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/ipRouteTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.IpRouteTable.IpRouteEntry, [u'iproutedest', u'iprouteifindex', u'iproutemetric1', u'iproutemetric2', u'iproutemetric3', u'iproutemetric4', u'iproutenexthop', u'iproutetype', u'iprouteproto', u'iprouteage', u'iproutemask', u'iproutemetric5', u'iprouteinfo'], name, value)

            class IpRouteProto(Enum):
                """
                IpRouteProto (Enum Class)

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


            class IpRouteType(Enum):
                """
                IpRouteType (Enum Class)

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



    class IpNetToMediaTable(Entity):
        """
        The IP Address Translation table used for mapping
        from IP addresses to physical addresses.
        
        .. attribute:: ipnettomediaentry
        
        	Each entry contains one IpAddress to `physical' address equivalence
        	**type**\: list of  		 :py:class:`IpNetToMediaEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.IpNetToMediaTable, self).__init__()

            self.yang_name = "ipNetToMediaTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipNetToMediaEntry", ("ipnettomediaentry", RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry))])
            self._leafs = OrderedDict()

            self.ipnettomediaentry = YList(self)
            self._segment_path = lambda: "ipNetToMediaTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.IpNetToMediaTable, [], name, value)


        class IpNetToMediaEntry(Entity):
            """
            Each entry contains one IpAddress to `physical'
            address equivalence.
            
            .. attribute:: ipnettomediaifindex  (key)
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipnettomedianetaddress  (key)
            
            	The IpAddress corresponding to the media\- dependent `physical' address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipnettomediaphysaddress
            
            	The media\-dependent `physical' address
            	**type**\: str
            
            .. attribute:: ipnettomediatype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToMediaTable.  That is, it effectively disassociates the interface identified with said entry from the mapping identified with said entry. It is an implementation\-specific matter as to whether the agent removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToMediaType object
            	**type**\:  :py:class:`IpNetToMediaType <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry.IpNetToMediaType>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry, self).__init__()

                self.yang_name = "ipNetToMediaEntry"
                self.yang_parent_name = "ipNetToMediaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipnettomediaifindex','ipnettomedianetaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipnettomediaifindex', (YLeaf(YType.int32, 'ipNetToMediaIfIndex'), ['int'])),
                    ('ipnettomedianetaddress', (YLeaf(YType.str, 'ipNetToMediaNetAddress'), ['str'])),
                    ('ipnettomediaphysaddress', (YLeaf(YType.str, 'ipNetToMediaPhysAddress'), ['str'])),
                    ('ipnettomediatype', (YLeaf(YType.enumeration, 'ipNetToMediaType'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'IpNetToMediaTable.IpNetToMediaEntry.IpNetToMediaType')])),
                ])
                self.ipnettomediaifindex = None
                self.ipnettomedianetaddress = None
                self.ipnettomediaphysaddress = None
                self.ipnettomediatype = None
                self._segment_path = lambda: "ipNetToMediaEntry" + "[ipNetToMediaIfIndex='" + str(self.ipnettomediaifindex) + "']" + "[ipNetToMediaNetAddress='" + str(self.ipnettomedianetaddress) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/ipNetToMediaTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.IpNetToMediaTable.IpNetToMediaEntry, [u'ipnettomediaifindex', u'ipnettomedianetaddress', u'ipnettomediaphysaddress', u'ipnettomediatype'], name, value)

            class IpNetToMediaType(Enum):
                """
                IpNetToMediaType (Enum Class)

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



    class TcpConnTable(Entity):
        """
        A table containing TCP connection\-specific
        information.
        
        .. attribute:: tcpconnentry
        
        	Information about a particular current TCP connection.  An object of this type is transient, in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state
        	**type**\: list of  		 :py:class:`TcpConnEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.TcpConnTable.TcpConnEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.TcpConnTable, self).__init__()

            self.yang_name = "tcpConnTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tcpConnEntry", ("tcpconnentry", RFC1213MIB.TcpConnTable.TcpConnEntry))])
            self._leafs = OrderedDict()

            self.tcpconnentry = YList(self)
            self._segment_path = lambda: "tcpConnTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.TcpConnTable, [], name, value)


        class TcpConnEntry(Entity):
            """
            Information about a particular current TCP
            connection.  An object of this type is transient,
            in that it ceases to exist when (or soon after)
            the connection makes the transition to the CLOSED
            state.
            
            .. attribute:: tcpconnlocaladdress  (key)
            
            	The local IP address for this TCP connection.  In the case of a connection in the listen state which is willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnlocalport  (key)
            
            	The local port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnremaddress  (key)
            
            	The remote IP address for this TCP connection
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tcpconnremport  (key)
            
            	The remote port number for this TCP connection
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: tcpconnstate
            
            	The state of this TCP connection.  The only value which may be set by a management station is deleteTCB(12).  Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value.  If a management station sets this object to the value deleteTCB(12), then this has the effect of deleting the TCB (as defined in RFC 793) of the corresponding connection on the managed node, resulting in immediate termination of the connection.  As an implementation\-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note however that RST segments are not sent reliably)
            	**type**\:  :py:class:`TcpConnState <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.TcpConnTable.TcpConnEntry.TcpConnState>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.TcpConnTable.TcpConnEntry, self).__init__()

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
                    ('tcpconnstate', (YLeaf(YType.enumeration, 'tcpConnState'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'TcpConnTable.TcpConnEntry.TcpConnState')])),
                ])
                self.tcpconnlocaladdress = None
                self.tcpconnlocalport = None
                self.tcpconnremaddress = None
                self.tcpconnremport = None
                self.tcpconnstate = None
                self._segment_path = lambda: "tcpConnEntry" + "[tcpConnLocalAddress='" + str(self.tcpconnlocaladdress) + "']" + "[tcpConnLocalPort='" + str(self.tcpconnlocalport) + "']" + "[tcpConnRemAddress='" + str(self.tcpconnremaddress) + "']" + "[tcpConnRemPort='" + str(self.tcpconnremport) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/tcpConnTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.TcpConnTable.TcpConnEntry, [u'tcpconnlocaladdress', u'tcpconnlocalport', u'tcpconnremaddress', u'tcpconnremport', u'tcpconnstate'], name, value)

            class TcpConnState(Enum):
                """
                TcpConnState (Enum Class)

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



    class UdpTable(Entity):
        """
        A table containing UDP listener information.
        
        .. attribute:: udpentry
        
        	Information about a particular current UDP listener
        	**type**\: list of  		 :py:class:`UdpEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.UdpTable.UdpEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.UdpTable, self).__init__()

            self.yang_name = "udpTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("udpEntry", ("udpentry", RFC1213MIB.UdpTable.UdpEntry))])
            self._leafs = OrderedDict()

            self.udpentry = YList(self)
            self._segment_path = lambda: "udpTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.UdpTable, [], name, value)


        class UdpEntry(Entity):
            """
            Information about a particular current UDP
            listener.
            
            .. attribute:: udplocaladdress  (key)
            
            	The local IP address for this UDP listener.  In the case of a UDP listener which is willing to accept datagrams for any IP interface associated with the node, the value 0.0.0.0 is used
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: udplocalport  (key)
            
            	The local port number for this UDP listener
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.UdpTable.UdpEntry, self).__init__()

                self.yang_name = "udpEntry"
                self.yang_parent_name = "udpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['udplocaladdress','udplocalport']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('udplocaladdress', (YLeaf(YType.str, 'udpLocalAddress'), ['str'])),
                    ('udplocalport', (YLeaf(YType.int32, 'udpLocalPort'), ['int'])),
                ])
                self.udplocaladdress = None
                self.udplocalport = None
                self._segment_path = lambda: "udpEntry" + "[udpLocalAddress='" + str(self.udplocaladdress) + "']" + "[udpLocalPort='" + str(self.udplocalport) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/udpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.UdpTable.UdpEntry, [u'udplocaladdress', u'udplocalport'], name, value)


    class EgpNeighTable(Entity):
        """
        The EGP neighbor table.
        
        .. attribute:: egpneighentry
        
        	Information about this entity's relationship with a particular EGP neighbor
        	**type**\: list of  		 :py:class:`EgpNeighEntry <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry>`
        
        

        """

        _prefix = 'RFC1213-MIB'

        def __init__(self):
            super(RFC1213MIB.EgpNeighTable, self).__init__()

            self.yang_name = "egpNeighTable"
            self.yang_parent_name = "RFC1213-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("egpNeighEntry", ("egpneighentry", RFC1213MIB.EgpNeighTable.EgpNeighEntry))])
            self._leafs = OrderedDict()

            self.egpneighentry = YList(self)
            self._segment_path = lambda: "egpNeighTable"
            self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RFC1213MIB.EgpNeighTable, [], name, value)


        class EgpNeighEntry(Entity):
            """
            Information about this entity's relationship with
            a particular EGP neighbor.
            
            .. attribute:: egpneighaddr  (key)
            
            	The IP address of this entry's EGP neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: egpneighstate
            
            	The EGP state of the local system with respect to this entry's EGP neighbor.  Each EGP state is represented by a value that is one greater than the numerical value associated with said state in RFC 904
            	**type**\:  :py:class:`EgpNeighState <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighState>`
            
            .. attribute:: egpneighas
            
            	The autonomous system of this EGP peer.  Zero should be specified if the autonomous system number of the neighbor is not yet known
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighinmsgs
            
            	The number of EGP messages received without error from this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighinerrs
            
            	The number of EGP messages received from this EGP peer that proved to be in error (e.g., bad EGP checksum)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighoutmsgs
            
            	The number of locally generated EGP messages to this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighouterrs
            
            	The number of locally generated EGP messages not sent to this EGP peer due to resource limitations within an EGP entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighinerrmsgs
            
            	The number of EGP\-defined error messages received from this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighouterrmsgs
            
            	The number of EGP\-defined error messages sent to this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighstateups
            
            	The number of EGP state transitions to the UP state with this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighstatedowns
            
            	The number of EGP state transitions from the UP state to any other state with this EGP peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: egpneighintervalhello
            
            	The interval between EGP Hello command retransmissions (in hundredths of a second).  This represents the t1 timer as defined in RFC 904
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighintervalpoll
            
            	The interval between EGP poll command retransmissions (in hundredths of a second).  This represents the t3 timer as defined in RFC 904
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: egpneighmode
            
            	The polling mode of this EGP entity, either passive or active
            	**type**\:  :py:class:`EgpNeighMode <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighMode>`
            
            .. attribute:: egpneigheventtrigger
            
            	A control variable used to trigger operator\- initiated Start and Stop events.  When read, this variable always returns the most recent value that egpNeighEventTrigger was set to.  If it has not been set since the last initialization of the network management subsystem on the node, it returns a value of `stop'.  When set, this variable causes a Start or Stop event on the specified neighbor, as specified on pages 8\-10 of RFC 904.  Briefly, a Start event causes an Idle peer to begin neighbor acquisition and a non\-Idle peer to reinitiate neighbor acquisition.  A stop event causes a non\-Idle peer to return to the Idle state until a Start event occurs, either via egpNeighEventTrigger or otherwise
            	**type**\:  :py:class:`EgpNeighEventTrigger <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.EgpNeighTable.EgpNeighEntry.EgpNeighEventTrigger>`
            
            

            """

            _prefix = 'RFC1213-MIB'

            def __init__(self):
                super(RFC1213MIB.EgpNeighTable.EgpNeighEntry, self).__init__()

                self.yang_name = "egpNeighEntry"
                self.yang_parent_name = "egpNeighTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['egpneighaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('egpneighaddr', (YLeaf(YType.str, 'egpNeighAddr'), ['str'])),
                    ('egpneighstate', (YLeaf(YType.enumeration, 'egpNeighState'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'EgpNeighTable.EgpNeighEntry.EgpNeighState')])),
                    ('egpneighas', (YLeaf(YType.int32, 'egpNeighAs'), ['int'])),
                    ('egpneighinmsgs', (YLeaf(YType.uint32, 'egpNeighInMsgs'), ['int'])),
                    ('egpneighinerrs', (YLeaf(YType.uint32, 'egpNeighInErrs'), ['int'])),
                    ('egpneighoutmsgs', (YLeaf(YType.uint32, 'egpNeighOutMsgs'), ['int'])),
                    ('egpneighouterrs', (YLeaf(YType.uint32, 'egpNeighOutErrs'), ['int'])),
                    ('egpneighinerrmsgs', (YLeaf(YType.uint32, 'egpNeighInErrMsgs'), ['int'])),
                    ('egpneighouterrmsgs', (YLeaf(YType.uint32, 'egpNeighOutErrMsgs'), ['int'])),
                    ('egpneighstateups', (YLeaf(YType.uint32, 'egpNeighStateUps'), ['int'])),
                    ('egpneighstatedowns', (YLeaf(YType.uint32, 'egpNeighStateDowns'), ['int'])),
                    ('egpneighintervalhello', (YLeaf(YType.int32, 'egpNeighIntervalHello'), ['int'])),
                    ('egpneighintervalpoll', (YLeaf(YType.int32, 'egpNeighIntervalPoll'), ['int'])),
                    ('egpneighmode', (YLeaf(YType.enumeration, 'egpNeighMode'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'EgpNeighTable.EgpNeighEntry.EgpNeighMode')])),
                    ('egpneigheventtrigger', (YLeaf(YType.enumeration, 'egpNeighEventTrigger'), [('ydk.models.cisco_ios_xe.RFC1213_MIB', 'RFC1213MIB', 'EgpNeighTable.EgpNeighEntry.EgpNeighEventTrigger')])),
                ])
                self.egpneighaddr = None
                self.egpneighstate = None
                self.egpneighas = None
                self.egpneighinmsgs = None
                self.egpneighinerrs = None
                self.egpneighoutmsgs = None
                self.egpneighouterrs = None
                self.egpneighinerrmsgs = None
                self.egpneighouterrmsgs = None
                self.egpneighstateups = None
                self.egpneighstatedowns = None
                self.egpneighintervalhello = None
                self.egpneighintervalpoll = None
                self.egpneighmode = None
                self.egpneigheventtrigger = None
                self._segment_path = lambda: "egpNeighEntry" + "[egpNeighAddr='" + str(self.egpneighaddr) + "']"
                self._absolute_path = lambda: "RFC1213-MIB:RFC1213-MIB/egpNeighTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RFC1213MIB.EgpNeighTable.EgpNeighEntry, [u'egpneighaddr', u'egpneighstate', u'egpneighas', u'egpneighinmsgs', u'egpneighinerrs', u'egpneighoutmsgs', u'egpneighouterrs', u'egpneighinerrmsgs', u'egpneighouterrmsgs', u'egpneighstateups', u'egpneighstatedowns', u'egpneighintervalhello', u'egpneighintervalpoll', u'egpneighmode', u'egpneigheventtrigger'], name, value)

            class EgpNeighEventTrigger(Enum):
                """
                EgpNeighEventTrigger (Enum Class)

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


            class EgpNeighMode(Enum):
                """
                EgpNeighMode (Enum Class)

                The polling mode of this EGP entity, either

                passive or active.

                .. data:: active = 1

                .. data:: passive = 2

                """

                active = Enum.YLeaf(1, "active")

                passive = Enum.YLeaf(2, "passive")


            class EgpNeighState(Enum):
                """
                EgpNeighState (Enum Class)

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


    def clone_ptr(self):
        self._top_entity = RFC1213MIB()
        return self._top_entity

