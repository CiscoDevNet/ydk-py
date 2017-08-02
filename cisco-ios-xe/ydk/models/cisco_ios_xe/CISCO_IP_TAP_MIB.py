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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpTapMib(Entity):
    """
    
    
    .. attribute:: citapstreamencodepacket
    
    	
    	**type**\:   :py:class:`Citapstreamencodepacket <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CiscoIpTapMib.Citapstreamencodepacket>`
    
    .. attribute:: citapstreamtable
    
    	The Intercept Stream IP Table lists the IPv4 and IPv6 streams to be intercepted.  The same data stream may be required by multiple taps, and one might assume that often the intercepted stream is a small subset of the traffic that could be intercepted.   This essentially provides options for packet selection, only some of which might be used. For example, if all traffic to or from a given interface is to be intercepted, one would configure an entry which lists the interface, and wild\-card everything else.  If all traffic to or from a given IP Address is to be intercepted, one would configure two such entries listing the IP Address as source and destination respectively, and wild\-card everything else.  If a particular voice on a teleconference is to be intercepted, on the other hand, one would extract the multicast (destination) IP address, the source IP Address, the protocol (UDP), and the source and destination ports from the call control exchange and list all necessary information.   The first index indicates which Mediation Device the intercepted traffic will be diverted to. The second index permits multiple classifiers to be used together, such as having an IP address as source or destination. The value of the second index is that of the stream's counter entry in the  cTap2StreamTable.  Entries are added to this table via citapStreamStatus in  accordance with the RowStatus convention
    	**type**\:   :py:class:`Citapstreamtable <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CiscoIpTapMib.Citapstreamtable>`
    
    

    """

    _prefix = 'CISCO-IP-TAP-MIB'
    _revision = '2004-03-11'

    def __init__(self):
        super(CiscoIpTapMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IP-TAP-MIB"
        self.yang_parent_name = "CISCO-IP-TAP-MIB"

        self.citapstreamencodepacket = CiscoIpTapMib.Citapstreamencodepacket()
        self.citapstreamencodepacket.parent = self
        self._children_name_map["citapstreamencodepacket"] = "citapStreamEncodePacket"
        self._children_yang_names.add("citapStreamEncodePacket")

        self.citapstreamtable = CiscoIpTapMib.Citapstreamtable()
        self.citapstreamtable.parent = self
        self._children_name_map["citapstreamtable"] = "citapStreamTable"
        self._children_yang_names.add("citapStreamTable")


    class Citapstreamencodepacket(Entity):
        """
        
        
        .. attribute:: citapstreamcapabilities
        
        	This object displays what types of intercept streams can be configured on this type of device. This may be dependent on hardware capabilities, software capabilities. The following fields may be supported\:     tapEnable\:   set if table entries with                  cTap2StreamInterceptEnable set to 'false'                  are used to pre\-screen packets for intercept;                  otherwise these entries are ignored.     interface\:   SNMP ifIndex Value may be used to select                  interception of all data crossing an                  interface or set of interfaces.     ipV4\:        IPv4 Address or prefix may be used to select                  traffic to be intercepted.     ipV6\:        IPv6 Address or prefix may be used to select                  traffic to be intercepted.     l4Port\:      TCP/UDP Ports may be used to select traffic                  to be intercepted.     dscp\:        DSCP (Differentiated Services Code Point) may                  be used to select traffic to be intercepted.     voip\:        packets belonging to a voice session may                  be intercepted using source IPv4 address and                  source UDP port
        	**type**\:   :py:class:`Citapstreamcapabilities <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CiscoIpTapMib.Citapstreamencodepacket.Citapstreamcapabilities>`
        
        

        """

        _prefix = 'CISCO-IP-TAP-MIB'
        _revision = '2004-03-11'

        def __init__(self):
            super(CiscoIpTapMib.Citapstreamencodepacket, self).__init__()

            self.yang_name = "citapStreamEncodePacket"
            self.yang_parent_name = "CISCO-IP-TAP-MIB"

            self.citapstreamcapabilities = YLeaf(YType.bits, "citapStreamCapabilities")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("citapstreamcapabilities") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpTapMib.Citapstreamencodepacket, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpTapMib.Citapstreamencodepacket, self).__setattr__(name, value)

        def has_data(self):
            return self.citapstreamcapabilities.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.citapstreamcapabilities.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "citapStreamEncodePacket" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.citapstreamcapabilities.is_set or self.citapstreamcapabilities.yfilter != YFilter.not_set):
                leaf_name_data.append(self.citapstreamcapabilities.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "citapStreamCapabilities"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "citapStreamCapabilities"):
                self.citapstreamcapabilities[value] = True


    class Citapstreamtable(Entity):
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
        	**type**\: list of    :py:class:`Citapstreamentry <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CiscoIpTapMib.Citapstreamtable.Citapstreamentry>`
        
        

        """

        _prefix = 'CISCO-IP-TAP-MIB'
        _revision = '2004-03-11'

        def __init__(self):
            super(CiscoIpTapMib.Citapstreamtable, self).__init__()

            self.yang_name = "citapStreamTable"
            self.yang_parent_name = "CISCO-IP-TAP-MIB"

            self.citapstreamentry = YList(self)

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
                        super(CiscoIpTapMib.Citapstreamtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpTapMib.Citapstreamtable, self).__setattr__(name, value)


        class Citapstreamentry(Entity):
            """
            A stream entry indicates a single data stream to be
            intercepted to a Mediation Device. Many selected data
            streams may go to the same application interface, and many
            application interfaces are supported.
            
            .. attribute:: ctap2mediationcontentid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ctap2mediationcontentid <ydk.models.cisco_ios_xe.CISCO_TAP2_MIB.CiscoTap2Mib.Ctap2Mediationtable.Ctap2Mediationentry>`
            
            .. attribute:: ctap2streamindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ctap2streamindex <ydk.models.cisco_ios_xe.CISCO_TAP2_MIB.CiscoTap2Mib.Ctap2Streamtable.Ctap2Streamentry>`
            
            .. attribute:: citapstreamaddrtype
            
            	The type of address, used in packet selection
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: citapstreamdestinationaddress
            
            	The Destination address or prefix used in packet selection. This address will be of the type specified in citapStreamAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: citapstreamdestinationlength
            
            	The length of the Destination Prefix. A value of zero causes all addresses to match.  This prefix length will be consistent with the type specified in citapStreamAddrType
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: citapstreamdestl4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in citapStreamDestL4PortMin.   If both citapStreamDestL4PortMin and citapStreamDestL4PortMax are at their default values, the port number is effectively unused
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: citapstreamdestl4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match.  This value must be equal to or less than the value specified for this entry in citapStreamDestL4PortMax.   If both citapStreamDestL4PortMin and citapStreamDestL4PortMax are at their default values, the port number is effectively unused
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: citapstreamflowid
            
            	The flow identifier in an IPv6 header. \-1 indicates that the Flow Id is unused
            	**type**\:  int
            
            	**range:** \-1..1048575
            
            .. attribute:: citapstreaminterface
            
            	The ifIndex value of the interface over which traffic to be intercepted is received or transmitted. The interface may be physical or virtual. If this is the only parameter specified, and it is other than \-2, \-1 or 0, all traffic on the selected interface will be chosen.   If the value is zero, matching traffic may be received or transmitted on any interface.  Additional selection parameters must be selected to limit the scope of traffic intercepted. This is most useful on non\-routing platforms or on intercepts placed elsewhere than a subscriber interface.   If the value is \-1, one or both of citapStreamDestinationAddress and citapStreamSourceAddress must be specified with prefix length greater than zero. Matching traffic on the interface pointed to by ipRouteIfIndex or ipCidrRouteIfIndex values associated with those values is intercepted, whichever is specified to be more focused than a default route.  If routing changes, either by operator action or by routing protocol events, the interface will change with it. This is primarily intended for use on subscriber interfaces and other places where routing is guaranteed to be symmetrical.   In both of these cases, it is possible to have the same packet selected for intersection on both its ingress and egress interface.  Nonetheless, only one instance of the packet is sent to the Mediation Device.   If the value is \-2, packets belonging to a Voice over IP (VoIP) session identified by citapStreamSourceAddress,  citapStreamSourceLen and citapStreamSourceL4PortMin may be  intercepted, as a specific voice session can be identified  with source IP address and udp port number. Other selection  parameters may be not considered, even if they are set by  the Mediation Device.   This value must be set when creating a stream entry, either to select an interface, to select all interfaces, or to select the interface that routing chooses. Some platforms may not implement the entire range of options
            	**type**\:  int
            
            	**range:** \-2..2147483647
            
            .. attribute:: citapstreamprotocol
            
            	The IP protocol to match against the IPv4 protocol number or the IPv6 Next\- Header number in the packet. \-1 means 'any IP protocol'
            	**type**\:  int
            
            	**range:** \-1..255
            
            .. attribute:: citapstreamsourceaddress
            
            	The Source Address used in packet selection. This address will be of the type specified in citapStreamAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: citapstreamsourcel4portmax
            
            	The maximum value that the layer\-4 destination port number in the packet must have in order to match this classifier entry. This value must be equal to or greater than the value specified for this entry in citapStreamSourceL4PortMin.   If both citapStreamSourceL4PortMin and citapStreamSourceL4PortMax are at their default values, the port number is effectively unused
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: citapstreamsourcel4portmin
            
            	The minimum value that the layer\-4 destination port number in the packet must have in order to match.  This value must be equal to or less than the value specified for this entry in citapStreamSourceL4PortMax.   If both citapStreamSourceL4PortMin and citapStreamSourceL4PortMax are at their default values, the port number is effectively unused
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: citapstreamsourcelength
            
            	The length of the Source Prefix. A value of zero causes all addresses to match. This prefix length will be consistent with the type specified in citapStreamAddrType
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: citapstreamstatus
            
            	The status of this conceptual row. This object manages creation, modification, and deletion of rows in this table. When any rows must be changed, citapStreamStatus must be first  set to 'notInService'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: citapstreamtosbyte
            
            	The value of the TOS byte, when masked with citapStreamTosByteMask, of traffic to be intercepted.  If citapStreamTosByte&(~citapStreamTosByteMask)!=0, configuration is rejected
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: citapstreamtosbytemask
            
            	The value of the TOS byte in an IPv4 or IPv6 header is ANDed with citapStreamTosByteMask and compared with citapStreamTosByte.  If the values are equal, the comparison is equal. If the mask is zero and the TosByte value is zero, the result is to always accept
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: citapstreamvrf
            
            	An ASCII string, which is the name of a Virtual Routing and Forwarding (VRF) table comprising the routing context of a Virtual Private Network. The interface or set of  interfaces on which the packet might be found should be  selected from the set of interfaces in the VRF table.  A string length of zero implies that global routing table be used for selection of interfaces on which the packet might be found
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-IP-TAP-MIB'
            _revision = '2004-03-11'

            def __init__(self):
                super(CiscoIpTapMib.Citapstreamtable.Citapstreamentry, self).__init__()

                self.yang_name = "citapStreamEntry"
                self.yang_parent_name = "citapStreamTable"

                self.ctap2mediationcontentid = YLeaf(YType.str, "cTap2MediationContentId")

                self.ctap2streamindex = YLeaf(YType.str, "cTap2StreamIndex")

                self.citapstreamaddrtype = YLeaf(YType.enumeration, "citapStreamAddrType")

                self.citapstreamdestinationaddress = YLeaf(YType.str, "citapStreamDestinationAddress")

                self.citapstreamdestinationlength = YLeaf(YType.uint32, "citapStreamDestinationLength")

                self.citapstreamdestl4portmax = YLeaf(YType.uint16, "citapStreamDestL4PortMax")

                self.citapstreamdestl4portmin = YLeaf(YType.uint16, "citapStreamDestL4PortMin")

                self.citapstreamflowid = YLeaf(YType.int32, "citapStreamFlowId")

                self.citapstreaminterface = YLeaf(YType.int32, "citapStreamInterface")

                self.citapstreamprotocol = YLeaf(YType.int32, "citapStreamProtocol")

                self.citapstreamsourceaddress = YLeaf(YType.str, "citapStreamSourceAddress")

                self.citapstreamsourcel4portmax = YLeaf(YType.uint16, "citapStreamSourceL4PortMax")

                self.citapstreamsourcel4portmin = YLeaf(YType.uint16, "citapStreamSourceL4PortMin")

                self.citapstreamsourcelength = YLeaf(YType.uint32, "citapStreamSourceLength")

                self.citapstreamstatus = YLeaf(YType.enumeration, "citapStreamStatus")

                self.citapstreamtosbyte = YLeaf(YType.int32, "citapStreamTosByte")

                self.citapstreamtosbytemask = YLeaf(YType.int32, "citapStreamTosByteMask")

                self.citapstreamvrf = YLeaf(YType.str, "citapStreamVRF")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ctap2mediationcontentid",
                                "ctap2streamindex",
                                "citapstreamaddrtype",
                                "citapstreamdestinationaddress",
                                "citapstreamdestinationlength",
                                "citapstreamdestl4portmax",
                                "citapstreamdestl4portmin",
                                "citapstreamflowid",
                                "citapstreaminterface",
                                "citapstreamprotocol",
                                "citapstreamsourceaddress",
                                "citapstreamsourcel4portmax",
                                "citapstreamsourcel4portmin",
                                "citapstreamsourcelength",
                                "citapstreamstatus",
                                "citapstreamtosbyte",
                                "citapstreamtosbytemask",
                                "citapstreamvrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpTapMib.Citapstreamtable.Citapstreamentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpTapMib.Citapstreamtable.Citapstreamentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ctap2mediationcontentid.is_set or
                    self.ctap2streamindex.is_set or
                    self.citapstreamaddrtype.is_set or
                    self.citapstreamdestinationaddress.is_set or
                    self.citapstreamdestinationlength.is_set or
                    self.citapstreamdestl4portmax.is_set or
                    self.citapstreamdestl4portmin.is_set or
                    self.citapstreamflowid.is_set or
                    self.citapstreaminterface.is_set or
                    self.citapstreamprotocol.is_set or
                    self.citapstreamsourceaddress.is_set or
                    self.citapstreamsourcel4portmax.is_set or
                    self.citapstreamsourcel4portmin.is_set or
                    self.citapstreamsourcelength.is_set or
                    self.citapstreamstatus.is_set or
                    self.citapstreamtosbyte.is_set or
                    self.citapstreamtosbytemask.is_set or
                    self.citapstreamvrf.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ctap2mediationcontentid.yfilter != YFilter.not_set or
                    self.ctap2streamindex.yfilter != YFilter.not_set or
                    self.citapstreamaddrtype.yfilter != YFilter.not_set or
                    self.citapstreamdestinationaddress.yfilter != YFilter.not_set or
                    self.citapstreamdestinationlength.yfilter != YFilter.not_set or
                    self.citapstreamdestl4portmax.yfilter != YFilter.not_set or
                    self.citapstreamdestl4portmin.yfilter != YFilter.not_set or
                    self.citapstreamflowid.yfilter != YFilter.not_set or
                    self.citapstreaminterface.yfilter != YFilter.not_set or
                    self.citapstreamprotocol.yfilter != YFilter.not_set or
                    self.citapstreamsourceaddress.yfilter != YFilter.not_set or
                    self.citapstreamsourcel4portmax.yfilter != YFilter.not_set or
                    self.citapstreamsourcel4portmin.yfilter != YFilter.not_set or
                    self.citapstreamsourcelength.yfilter != YFilter.not_set or
                    self.citapstreamstatus.yfilter != YFilter.not_set or
                    self.citapstreamtosbyte.yfilter != YFilter.not_set or
                    self.citapstreamtosbytemask.yfilter != YFilter.not_set or
                    self.citapstreamvrf.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "citapStreamEntry" + "[cTap2MediationContentId='" + self.ctap2mediationcontentid.get() + "']" + "[cTap2StreamIndex='" + self.ctap2streamindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/citapStreamTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ctap2mediationcontentid.is_set or self.ctap2mediationcontentid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ctap2mediationcontentid.get_name_leafdata())
                if (self.ctap2streamindex.is_set or self.ctap2streamindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ctap2streamindex.get_name_leafdata())
                if (self.citapstreamaddrtype.is_set or self.citapstreamaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamaddrtype.get_name_leafdata())
                if (self.citapstreamdestinationaddress.is_set or self.citapstreamdestinationaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamdestinationaddress.get_name_leafdata())
                if (self.citapstreamdestinationlength.is_set or self.citapstreamdestinationlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamdestinationlength.get_name_leafdata())
                if (self.citapstreamdestl4portmax.is_set or self.citapstreamdestl4portmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamdestl4portmax.get_name_leafdata())
                if (self.citapstreamdestl4portmin.is_set or self.citapstreamdestl4portmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamdestl4portmin.get_name_leafdata())
                if (self.citapstreamflowid.is_set or self.citapstreamflowid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamflowid.get_name_leafdata())
                if (self.citapstreaminterface.is_set or self.citapstreaminterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreaminterface.get_name_leafdata())
                if (self.citapstreamprotocol.is_set or self.citapstreamprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamprotocol.get_name_leafdata())
                if (self.citapstreamsourceaddress.is_set or self.citapstreamsourceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamsourceaddress.get_name_leafdata())
                if (self.citapstreamsourcel4portmax.is_set or self.citapstreamsourcel4portmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamsourcel4portmax.get_name_leafdata())
                if (self.citapstreamsourcel4portmin.is_set or self.citapstreamsourcel4portmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamsourcel4portmin.get_name_leafdata())
                if (self.citapstreamsourcelength.is_set or self.citapstreamsourcelength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamsourcelength.get_name_leafdata())
                if (self.citapstreamstatus.is_set or self.citapstreamstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamstatus.get_name_leafdata())
                if (self.citapstreamtosbyte.is_set or self.citapstreamtosbyte.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamtosbyte.get_name_leafdata())
                if (self.citapstreamtosbytemask.is_set or self.citapstreamtosbytemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamtosbytemask.get_name_leafdata())
                if (self.citapstreamvrf.is_set or self.citapstreamvrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.citapstreamvrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cTap2MediationContentId" or name == "cTap2StreamIndex" or name == "citapStreamAddrType" or name == "citapStreamDestinationAddress" or name == "citapStreamDestinationLength" or name == "citapStreamDestL4PortMax" or name == "citapStreamDestL4PortMin" or name == "citapStreamFlowId" or name == "citapStreamInterface" or name == "citapStreamProtocol" or name == "citapStreamSourceAddress" or name == "citapStreamSourceL4PortMax" or name == "citapStreamSourceL4PortMin" or name == "citapStreamSourceLength" or name == "citapStreamStatus" or name == "citapStreamTosByte" or name == "citapStreamTosByteMask" or name == "citapStreamVRF"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cTap2MediationContentId"):
                    self.ctap2mediationcontentid = value
                    self.ctap2mediationcontentid.value_namespace = name_space
                    self.ctap2mediationcontentid.value_namespace_prefix = name_space_prefix
                if(value_path == "cTap2StreamIndex"):
                    self.ctap2streamindex = value
                    self.ctap2streamindex.value_namespace = name_space
                    self.ctap2streamindex.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamAddrType"):
                    self.citapstreamaddrtype = value
                    self.citapstreamaddrtype.value_namespace = name_space
                    self.citapstreamaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamDestinationAddress"):
                    self.citapstreamdestinationaddress = value
                    self.citapstreamdestinationaddress.value_namespace = name_space
                    self.citapstreamdestinationaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamDestinationLength"):
                    self.citapstreamdestinationlength = value
                    self.citapstreamdestinationlength.value_namespace = name_space
                    self.citapstreamdestinationlength.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamDestL4PortMax"):
                    self.citapstreamdestl4portmax = value
                    self.citapstreamdestl4portmax.value_namespace = name_space
                    self.citapstreamdestl4portmax.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamDestL4PortMin"):
                    self.citapstreamdestl4portmin = value
                    self.citapstreamdestl4portmin.value_namespace = name_space
                    self.citapstreamdestl4portmin.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamFlowId"):
                    self.citapstreamflowid = value
                    self.citapstreamflowid.value_namespace = name_space
                    self.citapstreamflowid.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamInterface"):
                    self.citapstreaminterface = value
                    self.citapstreaminterface.value_namespace = name_space
                    self.citapstreaminterface.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamProtocol"):
                    self.citapstreamprotocol = value
                    self.citapstreamprotocol.value_namespace = name_space
                    self.citapstreamprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamSourceAddress"):
                    self.citapstreamsourceaddress = value
                    self.citapstreamsourceaddress.value_namespace = name_space
                    self.citapstreamsourceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamSourceL4PortMax"):
                    self.citapstreamsourcel4portmax = value
                    self.citapstreamsourcel4portmax.value_namespace = name_space
                    self.citapstreamsourcel4portmax.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamSourceL4PortMin"):
                    self.citapstreamsourcel4portmin = value
                    self.citapstreamsourcel4portmin.value_namespace = name_space
                    self.citapstreamsourcel4portmin.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamSourceLength"):
                    self.citapstreamsourcelength = value
                    self.citapstreamsourcelength.value_namespace = name_space
                    self.citapstreamsourcelength.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamStatus"):
                    self.citapstreamstatus = value
                    self.citapstreamstatus.value_namespace = name_space
                    self.citapstreamstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamTosByte"):
                    self.citapstreamtosbyte = value
                    self.citapstreamtosbyte.value_namespace = name_space
                    self.citapstreamtosbyte.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamTosByteMask"):
                    self.citapstreamtosbytemask = value
                    self.citapstreamtosbytemask.value_namespace = name_space
                    self.citapstreamtosbytemask.value_namespace_prefix = name_space_prefix
                if(value_path == "citapStreamVRF"):
                    self.citapstreamvrf = value
                    self.citapstreamvrf.value_namespace = name_space
                    self.citapstreamvrf.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.citapstreamentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.citapstreamentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "citapStreamTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "citapStreamEntry"):
                for c in self.citapstreamentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpTapMib.Citapstreamtable.Citapstreamentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.citapstreamentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "citapStreamEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.citapstreamencodepacket is not None and self.citapstreamencodepacket.has_data()) or
            (self.citapstreamtable is not None and self.citapstreamtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.citapstreamencodepacket is not None and self.citapstreamencodepacket.has_operation()) or
            (self.citapstreamtable is not None and self.citapstreamtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB" + path_buffer

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

        if (child_yang_name == "citapStreamEncodePacket"):
            if (self.citapstreamencodepacket is None):
                self.citapstreamencodepacket = CiscoIpTapMib.Citapstreamencodepacket()
                self.citapstreamencodepacket.parent = self
                self._children_name_map["citapstreamencodepacket"] = "citapStreamEncodePacket"
            return self.citapstreamencodepacket

        if (child_yang_name == "citapStreamTable"):
            if (self.citapstreamtable is None):
                self.citapstreamtable = CiscoIpTapMib.Citapstreamtable()
                self.citapstreamtable.parent = self
                self._children_name_map["citapstreamtable"] = "citapStreamTable"
            return self.citapstreamtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "citapStreamEncodePacket" or name == "citapStreamTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpTapMib()
        return self._top_entity

