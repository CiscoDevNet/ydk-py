""" CISCO_IP_TAP_MIB 

This module manages Cisco's intercept feature for IP.

This MIB is used along with CISCO\-TAP2\-MIB to
intercept IP traffic. CISCO\-TAP2\-MIB along with
specific filter MIBs like this MIB replace 
CISCO\-TAP\-MIB.

To create an IP intercept, an entry citapStreamEntry 
is created which contains the filter details. An entry
cTap2StreamEntry of CISCO\-TAP2\-MIB is created, which is
the common stream information for all kinds of 
intercepts and type of the specific stream is set to
ip in this entry.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIPTAPMIB(Entity):
    """
    
    
    .. attribute:: citapstreamencodepacket
    
    	
    	**type**\:  :py:class:`CitapStreamEncodePacket <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CISCOIPTAPMIB.CitapStreamEncodePacket>`
    
    	**config**\: False
    
    .. attribute:: citapstreamtable
    
    	The Intercept Stream IP Table lists the IPv4 and IPv6 streams to be intercepted.  The same data stream may be required by multiple taps, and one might assume that often the intercepted stream is a small subset of the traffic that could be intercepted.   This essentially provides options for packet selection, only some of which might be used. For example, if all traffic to or from a given interface is to be intercepted, one would configure an entry which lists the interface, and wild\-card everything else.  If all traffic to or from a given IP Address is to be intercepted, one would configure two such entries listing the IP Address as source and destination respectively, and wild\-card everything else.  If a particular voice on a teleconference is to be intercepted, on the other hand, one would extract the multicast (destination) IP address, the source IP Address, the protocol (UDP), and the source and destination ports from the call control exchange and list all necessary information.   The first index indicates which Mediation Device the intercepted traffic will be diverted to. The second index permits multiple classifiers to be used together, such as having an IP address as source or destination. The value of the second index is that of the stream's counter entry in the  cTap2StreamTable.  Entries are added to this table via citapStreamStatus in  accordance with the RowStatus convention
    	**type**\:  :py:class:`CitapStreamTable <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CISCOIPTAPMIB.CitapStreamTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-IP-TAP-MIB'
    _revision = '2004-03-11'

    def __init__(self):
        super(CISCOIPTAPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IP-TAP-MIB"
        self.yang_parent_name = "CISCO-IP-TAP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("citapStreamEncodePacket", ("citapstreamencodepacket", CISCOIPTAPMIB.CitapStreamEncodePacket)), ("citapStreamTable", ("citapstreamtable", CISCOIPTAPMIB.CitapStreamTable))])
        self._leafs = OrderedDict()

        self.citapstreamencodepacket = CISCOIPTAPMIB.CitapStreamEncodePacket()
        self.citapstreamencodepacket.parent = self
        self._children_name_map["citapstreamencodepacket"] = "citapStreamEncodePacket"

        self.citapstreamtable = CISCOIPTAPMIB.CitapStreamTable()
        self.citapstreamtable.parent = self
        self._children_name_map["citapstreamtable"] = "citapStreamTable"
        self._segment_path = lambda: "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIPTAPMIB, [], name, value)


    class CitapStreamEncodePacket(Entity):
        """
        
        
        .. attribute:: citapstreamcapabilities
        
        	This object displays what types of intercept streams can be configured on this type of device. This may be dependent on hardware capabilities, software capabilities. The following fields may be supported\:     tapEnable\:   set if table entries with                  cTap2StreamInterceptEnable set to 'false'                  are used to pre\-screen packets for intercept;                  otherwise these entries are ignored.     interface\:   SNMP ifIndex Value may be used to select                  interception of all data crossing an                  interface or set of interfaces.     ipV4\:        IPv4 Address or prefix may be used to select                  traffic to be intercepted.     ipV6\:        IPv6 Address or prefix may be used to select                  traffic to be intercepted.     l4Port\:      TCP/UDP Ports may be used to select traffic                  to be intercepted.     dscp\:        DSCP (Differentiated Services Code Point) may                  be used to select traffic to be intercepted.     voip\:        packets belonging to a voice session may                  be intercepted using source IPv4 address and                  source UDP port
        	**type**\:  :py:class:`CitapStreamCapabilities <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CISCOIPTAPMIB.CitapStreamEncodePacket.CitapStreamCapabilities>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IP-TAP-MIB'
        _revision = '2004-03-11'

        def __init__(self):
            super(CISCOIPTAPMIB.CitapStreamEncodePacket, self).__init__()

            self.yang_name = "citapStreamEncodePacket"
            self.yang_parent_name = "CISCO-IP-TAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('citapstreamcapabilities', (YLeaf(YType.bits, 'citapStreamCapabilities'), ['Bits'])),
            ])
            self.citapstreamcapabilities = Bits()
            self._segment_path = lambda: "citapStreamEncodePacket"
            self._absolute_path = lambda: "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPTAPMIB.CitapStreamEncodePacket, ['citapstreamcapabilities'], name, value)



    class CitapStreamTable(Entity):
        """
        The Intercept Stream IP Table lists the IPv4 and IPv6 streams
        to be intercepted.  The same data stream may be required by
        multiple taps, and one might assume that often the intercepted
        stream is a small subset of the traffic that could be
        intercepted.
        
        
        This essentially provides options for packet selection, only
        some of which might be used. For example, if all traffic to or
        from a given interface is to be intercepted, one would
        configure an entry which lists the interface, and wild\-card
        everything else.  If all traffic to or from a given IP Address
        is to be intercepted, one would configure two such entries
        listing the IP Address as source and destination respectively,
        and wild\-card everything else.  If a particular voice on a
        teleconference is to be intercepted, on the other hand, one
        would extract the multicast (destination) IP address, the
        source IP Address, the protocol (UDP), and the source and
        destination ports from the call control exchange and list all
        necessary information.
        
        
        The first index indicates which Mediation Device the
        intercepted traffic will be diverted to. The second index
        permits multiple classifiers to be used together, such as
        having an IP address as source or destination. The value of the
        second index is that of the stream's counter entry in the 
        cTap2StreamTable.
        
        Entries are added to this table via citapStreamStatus in 
        accordance with the RowStatus convention.
        
        .. attribute:: citapstreamentry
        
        	A stream entry indicates a single data stream to be intercepted to a Mediation Device. Many selected data streams may go to the same application interface, and many application interfaces are supported
        	**type**\: list of  		 :py:class:`CitapStreamEntry <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CISCOIPTAPMIB.CitapStreamTable.CitapStreamEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IP-TAP-MIB'
        _revision = '2004-03-11'

        def __init__(self):
            super(CISCOIPTAPMIB.CitapStreamTable, self).__init__()

            self.yang_name = "citapStreamTable"
            self.yang_parent_name = "CISCO-IP-TAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("citapStreamEntry", ("citapstreamentry", CISCOIPTAPMIB.CitapStreamTable.CitapStreamEntry))])
            self._leafs = OrderedDict()

            self.citapstreamentry = YList(self)
            self._segment_path = lambda: "citapStreamTable"
            self._absolute_path = lambda: "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPTAPMIB.CitapStreamTable, [], name, value)


        class CitapStreamEntry(Entity):
            """
            A stream entry indicates a single data stream to be
            intercepted to a Mediation Device. Many selected data
            streams may go to the same application interface, and many
            application interfaces are supported.
            
            .. attribute:: ctap2mediationcontentid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ctap2mediationcontentid <ydk.models.cisco_ios_xe.CISCO_TAP2_MIB.CISCOTAP2MIB.CTap2MediationTable.CTap2MediationEntry>`
            
            	**config**\: False
            
            .. attribute:: ctap2streamindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ctap2streamindex <ydk.models.cisco_ios_xe.CISCO_TAP2_MIB.CISCOTAP2MIB.CTap2StreamTable.CTap2StreamEntry>`
            
            	**config**\: False
            
            .. attribute:: citapstreaminterface
            
            	The ifIndex value of the interface over which traffic to be intercepted is received or transmitted. The interface may be physical or virtual. If this is the only parameter specified, and it is other than \-2, \-1 or 0, all traffic on the selected interface will be chosen.   If the value is zero, matching traffic may be received or transmitted on any interface.  Additional selection parameters must be selected to limit the scope of traffic intercepted. This is most useful on non\-routing platforms or on intercepts placed elsewhere than a subscriber interface.   If the value is \-1, one or both of citapStreamDestinationAddress and citapStreamSourceAddress must be specified with prefix length greater than zero. Matching traffic on the interface pointed to by ipRouteIfIndex or ipCidrRouteIfIndex values associated with those values is intercepted, whichever is specified to be more focused than a default route.  If routing changes, either by operator action or by routing protocol events, the interface will change with it. This is primarily intended for use on subscriber interfaces and other places where routing is guaranteed to be symmetrical.   In both of these cases, it is possible to have the same packet selected for intersection on both its ingress and egress interface.  Nonetheless, only one instance of the packet is sent to the Mediation Device.   If the value is \-2, packets belonging to a Voice over IP (VoIP) session identified by citapStreamSourceAddress,  citapStreamSourceLen and citapStreamSourceL4PortMin may be  intercepted, as a specific voice session can be identified  with source IP address and udp port number. Other selection  parameters may be not considered, even if they are set by  the Mediation Device.   This value must be set when creating a stream entry, either to select an interface, to select all interfaces, or to select the interface that routing chooses. Some platforms may not implement the entire range of options
            	**type**\: int
            
            	**range:** \-2..2147483647
            
            	**config**\: False
            
            .. attribute:: citapstreamaddrtype
            
            	The type of address, used in packet selection
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: citapstreamdestinationaddress
            
            	The Destination address or prefix used in packet selection. This address will be of the type specified in citapStreamAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: citapstreamdestinationlength
            
            	The length of the Destination Prefix. A value of zero causes all addresses to match.  This prefix length will be consistent with the type specified in citapStreamAddrType
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: citapstreamsourceaddress
            
            	The Source Address used in packet selection. This address will be of the type specified in citapStreamAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: citapstreamsourcelength
            
            	The length of the Source Prefix. A value of zero causes all addresses to match. This prefix length will be consistent with the type specified in citapStreamAddrType
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: citapstreamtosbyte
            
            	The value of the TOS byte, when masked with citapStreamTosByteMask, of traffic to be intercepted.  If citapStreamTosByte&(~citapStreamTosByteMask)!=0, configuration is rejected
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: citapstreamtosbytemask
            
            	The value of the TOS byte in an IPv4 or IPv6 header is ANDed with citapStreamTosByteMask and compared with citapStreamTosByte.  If the values are equal, the comparison is equal. If the mask is zero and the TosByte value is zero, the result is to always accept
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: citapstreamflowid
            
            	The flow identifier in an IPv6 header. \-1 indicates that the Flow Id is unused
            	**type**\: int
            
            	**range:** \-1..1048575
            
            	**config**\: False
            
            .. attribute:: citapstreamprotocol
            
            	The IP protocol to match against the IPv4 protocol number or the IPv6 Next\- Header number in the packet. \-1 means 'any IP protocol'
            	**type**\: int
            
            	**range:** \-1..255
            
            	**config**\: False
            
            .. attribute:: citapstreamdestl4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match.  This value must be equal to or less than the value specified for this entry in citapStreamDestL4PortMax.   If both citapStreamDestL4PortMin and citapStreamDestL4PortMax are at their default values, the port number is effectively unused
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: citapstreamdestl4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in citapStreamDestL4PortMin.   If both citapStreamDestL4PortMin and citapStreamDestL4PortMax are at their default values, the port number is effectively unused
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: citapstreamsourcel4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match.  This value must be equal to or less than the value specified for this entry in citapStreamSourceL4PortMax.   If both citapStreamSourceL4PortMin and citapStreamSourceL4PortMax are at their default values, the port number is effectively unused
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: citapstreamsourcel4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in citapStreamSourceL4PortMin.   If both citapStreamSourceL4PortMin and citapStreamSourceL4PortMax are at their default values, the port number is effectively unused
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: citapstreamvrf
            
            	An ASCII string, which is the name of a Virtual Routing and Forwarding (VRF) table comprising the routing context of a Virtual Private Network. The interface or set of  interfaces on which the packet might be found should be  selected from the set of interfaces in the VRF table.  A string length of zero implies that global routing table be used for selection of interfaces on which the packet might be found
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: citapstreamstatus
            
            	The status of this conceptual row. This object manages creation, modification, and deletion of rows in this table. When any rows must be changed, citapStreamStatus must be first  set to 'notInService'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IP-TAP-MIB'
            _revision = '2004-03-11'

            def __init__(self):
                super(CISCOIPTAPMIB.CitapStreamTable.CitapStreamEntry, self).__init__()

                self.yang_name = "citapStreamEntry"
                self.yang_parent_name = "citapStreamTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ctap2mediationcontentid','ctap2streamindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ctap2mediationcontentid', (YLeaf(YType.str, 'cTap2MediationContentId'), ['int'])),
                    ('ctap2streamindex', (YLeaf(YType.str, 'cTap2StreamIndex'), ['int'])),
                    ('citapstreaminterface', (YLeaf(YType.int32, 'citapStreamInterface'), ['int'])),
                    ('citapstreamaddrtype', (YLeaf(YType.enumeration, 'citapStreamAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('citapstreamdestinationaddress', (YLeaf(YType.str, 'citapStreamDestinationAddress'), ['str'])),
                    ('citapstreamdestinationlength', (YLeaf(YType.uint32, 'citapStreamDestinationLength'), ['int'])),
                    ('citapstreamsourceaddress', (YLeaf(YType.str, 'citapStreamSourceAddress'), ['str'])),
                    ('citapstreamsourcelength', (YLeaf(YType.uint32, 'citapStreamSourceLength'), ['int'])),
                    ('citapstreamtosbyte', (YLeaf(YType.int32, 'citapStreamTosByte'), ['int'])),
                    ('citapstreamtosbytemask', (YLeaf(YType.int32, 'citapStreamTosByteMask'), ['int'])),
                    ('citapstreamflowid', (YLeaf(YType.int32, 'citapStreamFlowId'), ['int'])),
                    ('citapstreamprotocol', (YLeaf(YType.int32, 'citapStreamProtocol'), ['int'])),
                    ('citapstreamdestl4portmin', (YLeaf(YType.uint16, 'citapStreamDestL4PortMin'), ['int'])),
                    ('citapstreamdestl4portmax', (YLeaf(YType.uint16, 'citapStreamDestL4PortMax'), ['int'])),
                    ('citapstreamsourcel4portmin', (YLeaf(YType.uint16, 'citapStreamSourceL4PortMin'), ['int'])),
                    ('citapstreamsourcel4portmax', (YLeaf(YType.uint16, 'citapStreamSourceL4PortMax'), ['int'])),
                    ('citapstreamvrf', (YLeaf(YType.str, 'citapStreamVRF'), ['str'])),
                    ('citapstreamstatus', (YLeaf(YType.enumeration, 'citapStreamStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ctap2mediationcontentid = None
                self.ctap2streamindex = None
                self.citapstreaminterface = None
                self.citapstreamaddrtype = None
                self.citapstreamdestinationaddress = None
                self.citapstreamdestinationlength = None
                self.citapstreamsourceaddress = None
                self.citapstreamsourcelength = None
                self.citapstreamtosbyte = None
                self.citapstreamtosbytemask = None
                self.citapstreamflowid = None
                self.citapstreamprotocol = None
                self.citapstreamdestl4portmin = None
                self.citapstreamdestl4portmax = None
                self.citapstreamsourcel4portmin = None
                self.citapstreamsourcel4portmax = None
                self.citapstreamvrf = None
                self.citapstreamstatus = None
                self._segment_path = lambda: "citapStreamEntry" + "[cTap2MediationContentId='" + str(self.ctap2mediationcontentid) + "']" + "[cTap2StreamIndex='" + str(self.ctap2streamindex) + "']"
                self._absolute_path = lambda: "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/citapStreamTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPTAPMIB.CitapStreamTable.CitapStreamEntry, ['ctap2mediationcontentid', 'ctap2streamindex', 'citapstreaminterface', 'citapstreamaddrtype', 'citapstreamdestinationaddress', 'citapstreamdestinationlength', 'citapstreamsourceaddress', 'citapstreamsourcelength', 'citapstreamtosbyte', 'citapstreamtosbytemask', 'citapstreamflowid', 'citapstreamprotocol', 'citapstreamdestl4portmin', 'citapstreamdestl4portmax', 'citapstreamsourcel4portmin', 'citapstreamsourcel4portmax', 'citapstreamvrf', 'citapstreamstatus'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOIPTAPMIB()
        return self._top_entity



