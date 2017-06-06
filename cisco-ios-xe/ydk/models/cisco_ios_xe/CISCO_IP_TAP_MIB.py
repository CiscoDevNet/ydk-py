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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIpTapMib(object):
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
        self.citapstreamencodepacket = CiscoIpTapMib.Citapstreamencodepacket()
        self.citapstreamencodepacket.parent = self
        self.citapstreamtable = CiscoIpTapMib.Citapstreamtable()
        self.citapstreamtable.parent = self


    class Citapstreamencodepacket(object):
        """
        
        
        .. attribute:: citapstreamcapabilities
        
        	This object displays what types of intercept streams can be configured on this type of device. This may be dependent on hardware capabilities, software capabilities. The following fields may be supported\:     tapEnable\:   set if table entries with                  cTap2StreamInterceptEnable set to 'false'                  are used to pre\-screen packets for intercept;                  otherwise these entries are ignored.     interface\:   SNMP ifIndex Value may be used to select                  interception of all data crossing an                  interface or set of interfaces.     ipV4\:        IPv4 Address or prefix may be used to select                  traffic to be intercepted.     ipV6\:        IPv6 Address or prefix may be used to select                  traffic to be intercepted.     l4Port\:      TCP/UDP Ports may be used to select traffic                  to be intercepted.     dscp\:        DSCP (Differentiated Services Code Point) may                  be used to select traffic to be intercepted.     voip\:        packets belonging to a voice session may                  be intercepted using source IPv4 address and                  source UDP port
        	**type**\:   :py:class:`Citapstreamcapabilities <ydk.models.cisco_ios_xe.CISCO_IP_TAP_MIB.CiscoIpTapMib.Citapstreamencodepacket.Citapstreamcapabilities>`
        
        

        """

        _prefix = 'CISCO-IP-TAP-MIB'
        _revision = '2004-03-11'

        def __init__(self):
            self.parent = None
            self.citapstreamcapabilities = CiscoIpTapMib.Citapstreamencodepacket.Citapstreamcapabilities()

        class Citapstreamcapabilities(FixedBitsDict):
            """
            Citapstreamcapabilities

            This object displays what types of intercept streams can be
            configured on this type of device. This may be dependent on
            hardware capabilities, software capabilities. The following
            fields may be supported\:
                tapEnable\:   set if table entries with
                             cTap2StreamInterceptEnable set to 'false'
                             are used to pre\-screen packets for intercept;
                             otherwise these entries are ignored.
                interface\:   SNMP ifIndex Value may be used to select
                             interception of all data crossing an
                             interface or set of interfaces.
                ipV4\:        IPv4 Address or prefix may be used to select
                             traffic to be intercepted.
                ipV6\:        IPv6 Address or prefix may be used to select
                             traffic to be intercepted.
                l4Port\:      TCP/UDP Ports may be used to select traffic
                             to be intercepted.
                dscp\:        DSCP (Differentiated Services Code Point) may
                             be used to select traffic to be intercepted.
                voip\:        packets belonging to a voice session may
                             be intercepted using source IPv4 address and
                             source UDP port.
            Keys are:- ipV4 , dscp , ipV6 , tapEnable , interface , voip , l4Port

            """

            def __init__(self):
                self._dictionary = { 
                    'ipV4':False,
                    'dscp':False,
                    'ipV6':False,
                    'tapEnable':False,
                    'interface':False,
                    'voip':False,
                    'l4Port':False,
                }
                self._pos_map = { 
                    'ipV4':2,
                    'dscp':5,
                    'ipV6':3,
                    'tapEnable':0,
                    'interface':1,
                    'voip':6,
                    'l4Port':4,
                }

        @property
        def _common_path(self):

            return '/CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/CISCO-IP-TAP-MIB:citapStreamEncodePacket'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.citapstreamcapabilities is not None:
                if self.citapstreamcapabilities._has_data():
                    return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IP_TAP_MIB as meta
            return meta._meta_table['CiscoIpTapMib.Citapstreamencodepacket']['meta_info']


    class Citapstreamtable(object):
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
            self.parent = None
            self.citapstreamentry = YList()
            self.citapstreamentry.parent = self
            self.citapstreamentry.name = 'citapstreamentry'


        class Citapstreamentry(object):
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
                self.parent = None
                self.ctap2mediationcontentid = None
                self.ctap2streamindex = None
                self.citapstreamaddrtype = None
                self.citapstreamdestinationaddress = None
                self.citapstreamdestinationlength = None
                self.citapstreamdestl4portmax = None
                self.citapstreamdestl4portmin = None
                self.citapstreamflowid = None
                self.citapstreaminterface = None
                self.citapstreamprotocol = None
                self.citapstreamsourceaddress = None
                self.citapstreamsourcel4portmax = None
                self.citapstreamsourcel4portmin = None
                self.citapstreamsourcelength = None
                self.citapstreamstatus = None
                self.citapstreamtosbyte = None
                self.citapstreamtosbytemask = None
                self.citapstreamvrf = None

            @property
            def _common_path(self):
                if self.ctap2mediationcontentid is None:
                    raise YPYModelError('Key property ctap2mediationcontentid is None')
                if self.ctap2streamindex is None:
                    raise YPYModelError('Key property ctap2streamindex is None')

                return '/CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/CISCO-IP-TAP-MIB:citapStreamTable/CISCO-IP-TAP-MIB:citapStreamEntry[CISCO-IP-TAP-MIB:cTap2MediationContentId = ' + str(self.ctap2mediationcontentid) + '][CISCO-IP-TAP-MIB:cTap2StreamIndex = ' + str(self.ctap2streamindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ctap2mediationcontentid is not None:
                    return True

                if self.ctap2streamindex is not None:
                    return True

                if self.citapstreamaddrtype is not None:
                    return True

                if self.citapstreamdestinationaddress is not None:
                    return True

                if self.citapstreamdestinationlength is not None:
                    return True

                if self.citapstreamdestl4portmax is not None:
                    return True

                if self.citapstreamdestl4portmin is not None:
                    return True

                if self.citapstreamflowid is not None:
                    return True

                if self.citapstreaminterface is not None:
                    return True

                if self.citapstreamprotocol is not None:
                    return True

                if self.citapstreamsourceaddress is not None:
                    return True

                if self.citapstreamsourcel4portmax is not None:
                    return True

                if self.citapstreamsourcel4portmin is not None:
                    return True

                if self.citapstreamsourcelength is not None:
                    return True

                if self.citapstreamstatus is not None:
                    return True

                if self.citapstreamtosbyte is not None:
                    return True

                if self.citapstreamtosbytemask is not None:
                    return True

                if self.citapstreamvrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IP_TAP_MIB as meta
                return meta._meta_table['CiscoIpTapMib.Citapstreamtable.Citapstreamentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB/CISCO-IP-TAP-MIB:citapStreamTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.citapstreamentry is not None:
                for child_ref in self.citapstreamentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IP_TAP_MIB as meta
            return meta._meta_table['CiscoIpTapMib.Citapstreamtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IP-TAP-MIB:CISCO-IP-TAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.citapstreamencodepacket is not None and self.citapstreamencodepacket._has_data():
            return True

        if self.citapstreamtable is not None and self.citapstreamtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IP_TAP_MIB as meta
        return meta._meta_table['CiscoIpTapMib']['meta_info']


