""" IF_MIB 

The MIB module to describe generic objects for network
interface sub\-layers.  This MIB is an updated version of
MIB\-II's ifTable, and incorporates the extensions defined in
RFC 1229.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class IFMIB(Entity):
    """
    
    
    .. attribute:: interfaces
    
    	
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Interfaces>`
    
    .. attribute:: ifmibobjects
    
    	
    	**type**\:  :py:class:`IfMIBObjects <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfMIBObjects>`
    
    .. attribute:: iftable
    
    	A list of interface entries.  The number of entries is given by the value of ifNumber
    	**type**\:  :py:class:`IfTable <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable>`
    
    .. attribute:: ifstacktable
    
    	The table containing information on the relationships between the multiple sub\-layers of network interfaces.  In particular, it contains information on which sub\-layers run 'on top of' which other sub\-layers, where each sub\-layer corresponds to a conceptual row in the ifTable.  For example, when the sub\-layer with ifIndex value x runs over the sub\-layer with ifIndex value y, then this table contains\:    ifStackStatus.x.y=active  For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I.  For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer.  (If I is not involved in multiplexing, then these are the only two rows associated with I.)  For example, two rows exist even for an interface which has no others stacked on top or below it\:    ifStackStatus.0.x=active   ifStackStatus.x.0=active 
    	**type**\:  :py:class:`IfStackTable <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfStackTable>`
    
    .. attribute:: ifrcvaddresstable
    
    	This table contains an entry for each address (broadcast, multicast, or uni\-cast) for which the system will receive packets/frames on a particular interface, except as follows\:  \- for an interface operating in promiscuous mode, entries are only required for those addresses for which the system would receive frames were it not operating in promiscuous mode.  \- for 802.5 functional addresses, only one entry is required, for the address which has the functional address bit ANDed with the bit mask of all functional addresses for which the interface will accept frames.  A system is normally able to use any unicast address which corresponds to an entry in this table as a source address
    	**type**\:  :py:class:`IfRcvAddressTable <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfRcvAddressTable>`
    
    

    """

    _prefix = 'IF-MIB'
    _revision = '2000-06-14'

    def __init__(self):
        super(IFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "IF-MIB"
        self.yang_parent_name = "IF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", IFMIB.Interfaces)), ("ifMIBObjects", ("ifmibobjects", IFMIB.IfMIBObjects)), ("ifTable", ("iftable", IFMIB.IfTable)), ("ifStackTable", ("ifstacktable", IFMIB.IfStackTable)), ("ifRcvAddressTable", ("ifrcvaddresstable", IFMIB.IfRcvAddressTable))])
        self._leafs = OrderedDict()

        self.interfaces = IFMIB.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.ifmibobjects = IFMIB.IfMIBObjects()
        self.ifmibobjects.parent = self
        self._children_name_map["ifmibobjects"] = "ifMIBObjects"

        self.iftable = IFMIB.IfTable()
        self.iftable.parent = self
        self._children_name_map["iftable"] = "ifTable"

        self.ifstacktable = IFMIB.IfStackTable()
        self.ifstacktable.parent = self
        self._children_name_map["ifstacktable"] = "ifStackTable"

        self.ifrcvaddresstable = IFMIB.IfRcvAddressTable()
        self.ifrcvaddresstable.parent = self
        self._children_name_map["ifrcvaddresstable"] = "ifRcvAddressTable"
        self._segment_path = lambda: "IF-MIB:IF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IFMIB, [], name, value)


    class Interfaces(Entity):
        """
        
        
        .. attribute:: ifnumber
        
        	The number of network interfaces (regardless of their current state) present on this system
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IFMIB.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifnumber', (YLeaf(YType.int32, 'ifNumber'), ['int'])),
            ])
            self.ifnumber = None
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "IF-MIB:IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IFMIB.Interfaces, [u'ifnumber'], name, value)


    class IfMIBObjects(Entity):
        """
        
        
        .. attribute:: iftablelastchange
        
        	The value of sysUpTime at the time of the last creation or deletion of an entry in the ifTable.  If the number of entries has been unchanged since the last re\-initialization of the local network management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ifstacklastchange
        
        	The value of sysUpTime at the time of the last change of the (whole) interface stack.  A change of the interface stack is defined to be any creation, deletion, or change in value of any instance of ifStackStatus.  If the interface stack has been unchanged since the last re\-initialization of the local network management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IFMIB.IfMIBObjects, self).__init__()

            self.yang_name = "ifMIBObjects"
            self.yang_parent_name = "IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('iftablelastchange', (YLeaf(YType.uint32, 'ifTableLastChange'), ['int'])),
                ('ifstacklastchange', (YLeaf(YType.uint32, 'ifStackLastChange'), ['int'])),
            ])
            self.iftablelastchange = None
            self.ifstacklastchange = None
            self._segment_path = lambda: "ifMIBObjects"
            self._absolute_path = lambda: "IF-MIB:IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IFMIB.IfMIBObjects, [u'iftablelastchange', u'ifstacklastchange'], name, value)


    class IfTable(Entity):
        """
        A list of interface entries.  The number of entries is
        given by the value of ifNumber.
        
        .. attribute:: ifentry
        
        	An entry containing management information applicable to a particular interface
        	**type**\: list of  		 :py:class:`IfEntry <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IFMIB.IfTable, self).__init__()

            self.yang_name = "ifTable"
            self.yang_parent_name = "IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ifEntry", ("ifentry", IFMIB.IfTable.IfEntry))])
            self._leafs = OrderedDict()

            self.ifentry = YList(self)
            self._segment_path = lambda: "ifTable"
            self._absolute_path = lambda: "IF-MIB:IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IFMIB.IfTable, [], name, value)


        class IfEntry(Entity):
            """
            An entry containing management information applicable to a
            particular interface.
            
            .. attribute:: ifindex  (key)
            
            	A unique value, greater than zero, for each interface.  It is recommended that values are assigned contiguously starting from 1.  The value for each interface sub\-layer must remain constant at least from one re\-initialization of the entity's network management system to the next re\- initialization
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifdescr
            
            	A textual string containing information about the interface.  This string should include the name of the manufacturer, the product name and the version of the interface hardware/software
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: iftype
            
            	The type of interface.  Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA), through updating the syntax of the IANAifType textual convention
            	**type**\:  :py:class:`IANAifType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAifType>`
            
            .. attribute:: ifmtu
            
            	The size of the largest packet which can be sent/received on the interface, specified in octets.  For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ifspeed
            
            	An estimate of the interface's current bandwidth in bits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  If the bandwidth of the interface is greater than the maximum value reportable by this object then this object should report its maximum value (4,294,967,295) and ifHighSpeed must be used to report the interace's speed.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifphysaddress
            
            	The interface's address at its protocol sub\-layer.  For example, for an 802.x interface, this object normally contains a MAC address.  The interface's media\-specific MIB must define the bit and byte ordering and the format of the value of this object.  For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: ifadminstatus
            
            	The desired state of the interface.  The testing(3) state indicates that no operational packets can be passed.  When a managed system initializes, all interfaces start with ifAdminStatus in the down(2) state.  As a result of either explicit management action or per configuration information retained by the managed system, ifAdminStatus is then changed to either the up(1) or testing(3) states (or remains in the down(2) state)
            	**type**\:  :py:class:`IfAdminStatus <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry.IfAdminStatus>`
            
            .. attribute:: ifoperstatus
            
            	The current operational state of the interface.  The testing(3) state indicates that no operational packets can be passed.  If ifAdminStatus is down(2) then ifOperStatus should be down(2).  If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic; it should change to dormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection); it should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state; it should remain in the notPresent(6) state if the interface has missing (typically, hardware) components
            	**type**\:  :py:class:`IfOperStatus <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry.IfOperStatus>`
            
            .. attribute:: iflastchange
            
            	The value of sysUpTime at the time the interface entered its current operational state.  If the current state was entered prior to the last re\-initialization of the local network management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinoctets
            
            	The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinnucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.  This object is deprecated in favour of ifInMulticastPkts and ifInBroadcastPkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifindiscards
            
            	The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinerrors
            
            	For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinunknownprotos
            
            	For packet\-oriented interfaces, the number of packets received via the interface which were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing the number of transmission units received via the interface which were discarded because of an unknown or unsupported protocol.  For any interface that does not support protocol multiplexing, this counter will always be 0.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutnucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.  This object is deprecated in favour of ifOutMulticastPkts and ifOutBroadcastPkts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifoutdiscards
            
            	The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifouterrors
            
            	For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutqlen
            
            	The length of the output packet queue (in packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ifspecific
            
            	A reference to MIB definitions specific to the particular media being used to realize the interface.  It is recommended that this value point to an instance of a MIB object in the media\-specific MIB, i.e., that this object have the semantics associated with the InstancePointer textual convention defined in RFC 2579.  In fact, it is recommended that the media\-specific MIB specify what value ifSpecific should/can take for values of ifType.  If no MIB definitions specific to the particular media are available, the value should be set to the OBJECT IDENTIFIER { 0 0 }
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: ifname
            
            	The textual name of the interface.  The value of this object should be the name of the interface as assigned by the local device and should be suitable for use in commands entered at the device's `console'.  This might be a text name, such as `le0' or a simple port number, such as `1', depending on the interface naming syntax of the device.  If several entries in the ifTable together represent a single interface as named by the device, then each will have the same value of ifName.  Note that for an agent which responds to SNMP queries concerning an interface on some other (proxied) device, then the value of ifName for such an interface is the proxied device's local name for it.  If there is no local name, or this object is otherwise not applicable, then this object contains a zero\-length string
            	**type**\: str
            
            .. attribute:: ifinmulticastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast address at this sub\-layer.  For a MAC layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifinbroadcastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutmulticastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifoutbroadcastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifhcinoctets
            
            	The total number of octets received on the interface, including framing characters.  This object is a 64\-bit version of ifInOctets.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinucastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were not addressed to a multicast or broadcast address at this sub\-layer.  This object is a 64\-bit version of ifInUcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinmulticastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a multicast address at this sub\-layer.  For a MAC layer protocol, this includes both Group and Functional addresses.  This object is a 64\-bit version of ifInMulticastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcinbroadcastpkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, which were addressed to a broadcast address at this sub\-layer.  This object is a 64\-bit version of ifInBroadcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutoctets
            
            	The total number of octets transmitted out of the interface, including framing characters.  This object is a 64\-bit version of ifOutOctets.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutucastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  This object is a 64\-bit version of ifOutUcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutmulticastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC layer protocol, this includes both Group and Functional addresses.  This object is a 64\-bit version of ifOutMulticastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ifhcoutbroadcastpkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and which were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  This object is a 64\-bit version of ifOutBroadcastPkts.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: iflinkupdowntrapenable
            
            	Indicates whether linkUp/linkDown traps should be generated for this interface.  By default, this object should have the value enabled(1) for interfaces which do not operate on 'top' of any other interface (as defined in the ifStackTable), and disabled(2) otherwise
            	**type**\:  :py:class:`IfLinkUpDownTrapEnable <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry.IfLinkUpDownTrapEnable>`
            
            .. attribute:: ifhighspeed
            
            	An estimate of the interface's current bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n\-500,000' to `n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub\-layer which has no concept of bandwidth, this object should be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifpromiscuousmode
            
            	This object has a value of false(2) if this interface only accepts packets/frames that are addressed to this station. This object has a value of true(1) when the station accepts all packets/frames transmitted on the media.  The value true(1) is only legal on certain types of media.  If legal, setting this object to a value of true(1) may require the interface to be reset before becoming effective.  The value of ifPromiscuousMode does not affect the reception of broadcast and multicast packets/frames by the interface
            	**type**\: bool
            
            .. attribute:: ifconnectorpresent
            
            	This object has the value 'true(1)' if the interface sublayer has a physical connector and the value 'false(2)' otherwise
            	**type**\: bool
            
            .. attribute:: ifalias
            
            	This object is an 'alias' name for the interface as specified by a network manager, and provides a non\-volatile 'handle' for the interface.  On the first instantiation of an interface, the value of ifAlias associated with that interface is the zero\-length string.  As and when a value is written into an instance of ifAlias through a network management set operation, then the agent must retain the supplied value in the ifAlias instance associated with the same interface for as long as that interface remains instantiated, including across all re\- initializations/reboots of the network management system, including those which result in a change of the interface's ifIndex value.  An example of the value which a network manager might store in this object for a WAN interface is the (Telco's) circuit number/identifier of the interface.  Some agents may support write\-access only for interfaces having particular values of ifType.  An agent which supports write access to this object is required to keep the value in non\-volatile storage, but it may limit the length of new values depending on how much storage is already occupied by the current values for other interfaces
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ifcounterdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this interface of any Counter32 or Counter64 object contained in the ifTable or ifXTable.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: iftestid
            
            	This object identifies the current invocation of the interface's test
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ifteststatus
            
            	This object indicates whether or not some manager currently has the necessary 'ownership' required to invoke a test on this interface.  A write to this object is only successful when it changes its value from 'notInUse(1)' to 'inUse(2)'. After completion of a test, the agent resets the value back to 'notInUse(1)'
            	**type**\:  :py:class:`IfTestStatus <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry.IfTestStatus>`
            
            	**status**\: deprecated
            
            .. attribute:: iftesttype
            
            	A control variable used to start and stop operator\- initiated interface tests.  Most OBJECT IDENTIFIER values assigned to tests are defined elsewhere, in association with specific types of interface.  However, this document assigns a value for a full\-duplex loopback test, and defines the special meanings of the subject identifier\:      noTest  OBJECT IDENTIFIER \:\:= { 0 0 }  When the value noTest is written to this object, no action is taken unless a test is in progress, in which case the test is aborted.  Writing any other value to this object is only valid when no test is currently in progress, in which case the indicated test is initiated.  When read, this object always returns the most recent value that ifTestType was set to.  If it has not been set since the last initialization of the network management subsystem on the agent, a value of noTest is returned
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: iftestresult
            
            	This object contains the result of the most recently requested test, or the value none(1) if no tests have been requested since the last reset.  Note that this facility provides no provision for saving the results of one test when starting another, as could be required if used by multiple managers concurrently
            	**type**\:  :py:class:`IfTestResult <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry.IfTestResult>`
            
            	**status**\: deprecated
            
            .. attribute:: iftestcode
            
            	This object contains a code which contains more specific information on the test result, for example an error\-code after a failed test.  Error codes and other values this object may take are specific to the type of interface and/or test.  The value may have the semantics of either the AutonomousType or InstancePointer textual conventions as defined in RFC 2579.  The identifier\:      testCodeUnknown  OBJECT IDENTIFIER \:\:= { 0 0 }  is defined for use if no additional result code is available
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: iftestowner
            
            	The entity which currently has the 'ownership' required to invoke a test on this interface
            	**type**\: str
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                super(IFMIB.IfTable.IfEntry, self).__init__()

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
                    ('ifadminstatus', (YLeaf(YType.enumeration, 'ifAdminStatus'), [('ydk.models.cisco_ios_xe.IF_MIB', 'IFMIB', 'IfTable.IfEntry.IfAdminStatus')])),
                    ('ifoperstatus', (YLeaf(YType.enumeration, 'ifOperStatus'), [('ydk.models.cisco_ios_xe.IF_MIB', 'IFMIB', 'IfTable.IfEntry.IfOperStatus')])),
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
                    ('ifname', (YLeaf(YType.str, 'ifName'), ['str'])),
                    ('ifinmulticastpkts', (YLeaf(YType.uint32, 'ifInMulticastPkts'), ['int'])),
                    ('ifinbroadcastpkts', (YLeaf(YType.uint32, 'ifInBroadcastPkts'), ['int'])),
                    ('ifoutmulticastpkts', (YLeaf(YType.uint32, 'ifOutMulticastPkts'), ['int'])),
                    ('ifoutbroadcastpkts', (YLeaf(YType.uint32, 'ifOutBroadcastPkts'), ['int'])),
                    ('ifhcinoctets', (YLeaf(YType.uint64, 'ifHCInOctets'), ['int'])),
                    ('ifhcinucastpkts', (YLeaf(YType.uint64, 'ifHCInUcastPkts'), ['int'])),
                    ('ifhcinmulticastpkts', (YLeaf(YType.uint64, 'ifHCInMulticastPkts'), ['int'])),
                    ('ifhcinbroadcastpkts', (YLeaf(YType.uint64, 'ifHCInBroadcastPkts'), ['int'])),
                    ('ifhcoutoctets', (YLeaf(YType.uint64, 'ifHCOutOctets'), ['int'])),
                    ('ifhcoutucastpkts', (YLeaf(YType.uint64, 'ifHCOutUcastPkts'), ['int'])),
                    ('ifhcoutmulticastpkts', (YLeaf(YType.uint64, 'ifHCOutMulticastPkts'), ['int'])),
                    ('ifhcoutbroadcastpkts', (YLeaf(YType.uint64, 'ifHCOutBroadcastPkts'), ['int'])),
                    ('iflinkupdowntrapenable', (YLeaf(YType.enumeration, 'ifLinkUpDownTrapEnable'), [('ydk.models.cisco_ios_xe.IF_MIB', 'IFMIB', 'IfTable.IfEntry.IfLinkUpDownTrapEnable')])),
                    ('ifhighspeed', (YLeaf(YType.uint32, 'ifHighSpeed'), ['int'])),
                    ('ifpromiscuousmode', (YLeaf(YType.boolean, 'ifPromiscuousMode'), ['bool'])),
                    ('ifconnectorpresent', (YLeaf(YType.boolean, 'ifConnectorPresent'), ['bool'])),
                    ('ifalias', (YLeaf(YType.str, 'ifAlias'), ['str'])),
                    ('ifcounterdiscontinuitytime', (YLeaf(YType.uint32, 'ifCounterDiscontinuityTime'), ['int'])),
                    ('iftestid', (YLeaf(YType.int32, 'ifTestId'), ['int'])),
                    ('ifteststatus', (YLeaf(YType.enumeration, 'ifTestStatus'), [('ydk.models.cisco_ios_xe.IF_MIB', 'IFMIB', 'IfTable.IfEntry.IfTestStatus')])),
                    ('iftesttype', (YLeaf(YType.str, 'ifTestType'), ['str'])),
                    ('iftestresult', (YLeaf(YType.enumeration, 'ifTestResult'), [('ydk.models.cisco_ios_xe.IF_MIB', 'IFMIB', 'IfTable.IfEntry.IfTestResult')])),
                    ('iftestcode', (YLeaf(YType.str, 'ifTestCode'), ['str'])),
                    ('iftestowner', (YLeaf(YType.str, 'ifTestOwner'), ['str'])),
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
                self.ifname = None
                self.ifinmulticastpkts = None
                self.ifinbroadcastpkts = None
                self.ifoutmulticastpkts = None
                self.ifoutbroadcastpkts = None
                self.ifhcinoctets = None
                self.ifhcinucastpkts = None
                self.ifhcinmulticastpkts = None
                self.ifhcinbroadcastpkts = None
                self.ifhcoutoctets = None
                self.ifhcoutucastpkts = None
                self.ifhcoutmulticastpkts = None
                self.ifhcoutbroadcastpkts = None
                self.iflinkupdowntrapenable = None
                self.ifhighspeed = None
                self.ifpromiscuousmode = None
                self.ifconnectorpresent = None
                self.ifalias = None
                self.ifcounterdiscontinuitytime = None
                self.iftestid = None
                self.ifteststatus = None
                self.iftesttype = None
                self.iftestresult = None
                self.iftestcode = None
                self.iftestowner = None
                self._segment_path = lambda: "ifEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "IF-MIB:IF-MIB/ifTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IFMIB.IfTable.IfEntry, [u'ifindex', u'ifdescr', u'iftype', u'ifmtu', u'ifspeed', u'ifphysaddress', u'ifadminstatus', u'ifoperstatus', u'iflastchange', u'ifinoctets', u'ifinucastpkts', u'ifinnucastpkts', u'ifindiscards', u'ifinerrors', u'ifinunknownprotos', u'ifoutoctets', u'ifoutucastpkts', u'ifoutnucastpkts', u'ifoutdiscards', u'ifouterrors', u'ifoutqlen', u'ifspecific', u'ifname', u'ifinmulticastpkts', u'ifinbroadcastpkts', u'ifoutmulticastpkts', u'ifoutbroadcastpkts', u'ifhcinoctets', u'ifhcinucastpkts', u'ifhcinmulticastpkts', u'ifhcinbroadcastpkts', u'ifhcoutoctets', u'ifhcoutucastpkts', u'ifhcoutmulticastpkts', u'ifhcoutbroadcastpkts', u'iflinkupdowntrapenable', u'ifhighspeed', u'ifpromiscuousmode', u'ifconnectorpresent', u'ifalias', u'ifcounterdiscontinuitytime', u'iftestid', u'ifteststatus', u'iftesttype', u'iftestresult', u'iftestcode', u'iftestowner'], name, value)

            class IfAdminStatus(Enum):
                """
                IfAdminStatus (Enum Class)

                The desired state of the interface.  The testing(3) state

                indicates that no operational packets can be passed.  When a

                managed system initializes, all interfaces start with

                ifAdminStatus in the down(2) state.  As a result of either

                explicit management action or per configuration information

                retained by the managed system, ifAdminStatus is then

                changed to either the up(1) or testing(3) states (or remains

                in the down(2) state).

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class IfLinkUpDownTrapEnable(Enum):
                """
                IfLinkUpDownTrapEnable (Enum Class)

                Indicates whether linkUp/linkDown traps should be generated

                for this interface.

                By default, this object should have the value enabled(1) for

                interfaces which do not operate on 'top' of any other

                interface (as defined in the ifStackTable), and disabled(2)

                otherwise.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class IfOperStatus(Enum):
                """
                IfOperStatus (Enum Class)

                The current operational state of the interface.  The

                testing(3) state indicates that no operational packets can

                be passed.  If ifAdminStatus is down(2) then ifOperStatus

                should be down(2).  If ifAdminStatus is changed to up(1)

                then ifOperStatus should change to up(1) if the interface is

                ready to transmit and receive network traffic; it should

                change to dormant(5) if the interface is waiting for

                external actions (such as a serial line waiting for an

                incoming connection); it should remain in the down(2) state

                if and only if there is a fault that prevents it from going

                to the up(1) state; it should remain in the notPresent(6)

                state if the interface has missing (typically, hardware)

                components.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")

                unknown = Enum.YLeaf(4, "unknown")

                dormant = Enum.YLeaf(5, "dormant")

                notPresent = Enum.YLeaf(6, "notPresent")

                lowerLayerDown = Enum.YLeaf(7, "lowerLayerDown")


            class IfTestResult(Enum):
                """
                IfTestResult (Enum Class)

                This object contains the result of the most recently

                requested test, or the value none(1) if no tests have been

                requested since the last reset.  Note that this facility

                provides no provision for saving the results of one test

                when starting another, as could be required if used by

                multiple managers concurrently.

                .. data:: none = 1

                .. data:: success = 2

                .. data:: inProgress = 3

                .. data:: notSupported = 4

                .. data:: unAbleToRun = 5

                .. data:: aborted = 6

                .. data:: failed = 7

                """

                none = Enum.YLeaf(1, "none")

                success = Enum.YLeaf(2, "success")

                inProgress = Enum.YLeaf(3, "inProgress")

                notSupported = Enum.YLeaf(4, "notSupported")

                unAbleToRun = Enum.YLeaf(5, "unAbleToRun")

                aborted = Enum.YLeaf(6, "aborted")

                failed = Enum.YLeaf(7, "failed")


            class IfTestStatus(Enum):
                """
                IfTestStatus (Enum Class)

                This object indicates whether or not some manager currently

                has the necessary 'ownership' required to invoke a test on

                this interface.  A write to this object is only successful

                when it changes its value from 'notInUse(1)' to 'inUse(2)'.

                After completion of a test, the agent resets the value back

                to 'notInUse(1)'.

                .. data:: notInUse = 1

                .. data:: inUse = 2

                """

                notInUse = Enum.YLeaf(1, "notInUse")

                inUse = Enum.YLeaf(2, "inUse")



    class IfStackTable(Entity):
        """
        The table containing information on the relationships
        between the multiple sub\-layers of network interfaces.  In
        particular, it contains information on which sub\-layers run
        'on top of' which other sub\-layers, where each sub\-layer
        corresponds to a conceptual row in the ifTable.  For
        example, when the sub\-layer with ifIndex value x runs over
        the sub\-layer with ifIndex value y, then this table
        contains\:
        
          ifStackStatus.x.y=active
        
        For each ifIndex value, I, which identifies an active
        interface, there are always at least two instantiated rows
        in this table associated with I.  For one of these rows, I
        is the value of ifStackHigherLayer; for the other, I is the
        value of ifStackLowerLayer.  (If I is not involved in
        multiplexing, then these are the only two rows associated
        with I.)
        
        For example, two rows exist even for an interface which has
        no others stacked on top or below it\:
        
          ifStackStatus.0.x=active
          ifStackStatus.x.0=active 
        
        .. attribute:: ifstackentry
        
        	Information on a particular relationship between two sub\- layers, specifying that one sub\-layer runs on 'top' of the other sub\-layer.  Each sub\-layer corresponds to a conceptual row in the ifTable
        	**type**\: list of  		 :py:class:`IfStackEntry <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfStackTable.IfStackEntry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IFMIB.IfStackTable, self).__init__()

            self.yang_name = "ifStackTable"
            self.yang_parent_name = "IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ifStackEntry", ("ifstackentry", IFMIB.IfStackTable.IfStackEntry))])
            self._leafs = OrderedDict()

            self.ifstackentry = YList(self)
            self._segment_path = lambda: "ifStackTable"
            self._absolute_path = lambda: "IF-MIB:IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IFMIB.IfStackTable, [], name, value)


        class IfStackEntry(Entity):
            """
            Information on a particular relationship between two sub\-
            layers, specifying that one sub\-layer runs on 'top' of the
            other sub\-layer.  Each sub\-layer corresponds to a conceptual
            row in the ifTable.
            
            .. attribute:: ifstackhigherlayer  (key)
            
            	The value of ifIndex corresponding to the higher sub\-layer of the relationship, i.e., the sub\-layer which runs on 'top' of the sub\-layer identified by the corresponding instance of ifStackLowerLayer.  If there is no higher sub\-layer (below the internetwork layer), then this object has the value 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ifstacklowerlayer  (key)
            
            	The value of ifIndex corresponding to the lower sub\-layer of the relationship, i.e., the sub\-layer which runs 'below' the sub\-layer identified by the corresponding instance of ifStackHigherLayer.  If there is no lower sub\-layer, then this object has the value 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ifstackstatus
            
            	The status of the relationship between two sub\-layers.  Changing the value of this object from 'active' to 'notInService' or 'destroy' will likely have consequences up and down the interface stack.  Thus, write access to this object is likely to be inappropriate for some types of interfaces, and many implementations will choose not to support write\-access for any type of interface
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                super(IFMIB.IfStackTable.IfStackEntry, self).__init__()

                self.yang_name = "ifStackEntry"
                self.yang_parent_name = "ifStackTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifstackhigherlayer','ifstacklowerlayer']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifstackhigherlayer', (YLeaf(YType.int32, 'ifStackHigherLayer'), ['int'])),
                    ('ifstacklowerlayer', (YLeaf(YType.int32, 'ifStackLowerLayer'), ['int'])),
                    ('ifstackstatus', (YLeaf(YType.enumeration, 'ifStackStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifstackhigherlayer = None
                self.ifstacklowerlayer = None
                self.ifstackstatus = None
                self._segment_path = lambda: "ifStackEntry" + "[ifStackHigherLayer='" + str(self.ifstackhigherlayer) + "']" + "[ifStackLowerLayer='" + str(self.ifstacklowerlayer) + "']"
                self._absolute_path = lambda: "IF-MIB:IF-MIB/ifStackTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IFMIB.IfStackTable.IfStackEntry, [u'ifstackhigherlayer', u'ifstacklowerlayer', u'ifstackstatus'], name, value)


    class IfRcvAddressTable(Entity):
        """
        This table contains an entry for each address (broadcast,
        multicast, or uni\-cast) for which the system will receive
        packets/frames on a particular interface, except as follows\:
        
        \- for an interface operating in promiscuous mode, entries
        are only required for those addresses for which the system
        would receive frames were it not operating in promiscuous
        mode.
        
        \- for 802.5 functional addresses, only one entry is
        required, for the address which has the functional address
        bit ANDed with the bit mask of all functional addresses for
        which the interface will accept frames.
        
        A system is normally able to use any unicast address which
        corresponds to an entry in this table as a source address.
        
        .. attribute:: ifrcvaddressentry
        
        	A list of objects identifying an address for which the system will accept packets/frames on the particular interface identified by the index value ifIndex
        	**type**\: list of  		 :py:class:`IfRcvAddressEntry <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfRcvAddressTable.IfRcvAddressEntry>`
        
        

        """

        _prefix = 'IF-MIB'
        _revision = '2000-06-14'

        def __init__(self):
            super(IFMIB.IfRcvAddressTable, self).__init__()

            self.yang_name = "ifRcvAddressTable"
            self.yang_parent_name = "IF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ifRcvAddressEntry", ("ifrcvaddressentry", IFMIB.IfRcvAddressTable.IfRcvAddressEntry))])
            self._leafs = OrderedDict()

            self.ifrcvaddressentry = YList(self)
            self._segment_path = lambda: "ifRcvAddressTable"
            self._absolute_path = lambda: "IF-MIB:IF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IFMIB.IfRcvAddressTable, [], name, value)


        class IfRcvAddressEntry(Entity):
            """
            A list of objects identifying an address for which the
            system will accept packets/frames on the particular
            interface identified by the index value ifIndex.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: ifrcvaddressaddress  (key)
            
            	An address for which the system will accept packets/frames on this entry's interface
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: ifrcvaddressstatus
            
            	This object is used to create and delete rows in the ifRcvAddressTable
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ifrcvaddresstype
            
            	This object has the value nonVolatile(3) for those entries in the table which are valid and will not be deleted by the next restart of the managed system.  Entries having the value volatile(2) are valid and exist, but have not been saved, so that will not exist after the next restart of the managed system.  Entries having the value other(1) are valid and exist but are not classified as to whether they will continue to exist after the next restart
            	**type**\:  :py:class:`IfRcvAddressType <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfRcvAddressTable.IfRcvAddressEntry.IfRcvAddressType>`
            
            

            """

            _prefix = 'IF-MIB'
            _revision = '2000-06-14'

            def __init__(self):
                super(IFMIB.IfRcvAddressTable.IfRcvAddressEntry, self).__init__()

                self.yang_name = "ifRcvAddressEntry"
                self.yang_parent_name = "ifRcvAddressTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','ifrcvaddressaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('ifrcvaddressaddress', (YLeaf(YType.str, 'ifRcvAddressAddress'), ['str'])),
                    ('ifrcvaddressstatus', (YLeaf(YType.enumeration, 'ifRcvAddressStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ifrcvaddresstype', (YLeaf(YType.enumeration, 'ifRcvAddressType'), [('ydk.models.cisco_ios_xe.IF_MIB', 'IFMIB', 'IfRcvAddressTable.IfRcvAddressEntry.IfRcvAddressType')])),
                ])
                self.ifindex = None
                self.ifrcvaddressaddress = None
                self.ifrcvaddressstatus = None
                self.ifrcvaddresstype = None
                self._segment_path = lambda: "ifRcvAddressEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[ifRcvAddressAddress='" + str(self.ifrcvaddressaddress) + "']"
                self._absolute_path = lambda: "IF-MIB:IF-MIB/ifRcvAddressTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IFMIB.IfRcvAddressTable.IfRcvAddressEntry, [u'ifindex', u'ifrcvaddressaddress', u'ifrcvaddressstatus', u'ifrcvaddresstype'], name, value)

            class IfRcvAddressType(Enum):
                """
                IfRcvAddressType (Enum Class)

                This object has the value nonVolatile(3) for those entries

                in the table which are valid and will not be deleted by the

                next restart of the managed system.  Entries having the

                value volatile(2) are valid and exist, but have not been

                saved, so that will not exist after the next restart of the

                managed system.  Entries having the value other(1) are valid

                and exist but are not classified as to whether they will

                continue to exist after the next restart.

                .. data:: other = 1

                .. data:: volatile = 2

                .. data:: nonVolatile = 3

                """

                other = Enum.YLeaf(1, "other")

                volatile = Enum.YLeaf(2, "volatile")

                nonVolatile = Enum.YLeaf(3, "nonVolatile")


    def clone_ptr(self):
        self._top_entity = IFMIB()
        return self._top_entity

