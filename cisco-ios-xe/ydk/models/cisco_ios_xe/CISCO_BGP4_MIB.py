""" CISCO_BGP4_MIB 

An extension to the IETF BGP4 MIB module defined in
RFC 1657.

Following is the terminology associated with Border
Gateway Protocol(BGP).

UPDATE message
    UPDATE messages are used to transfer routing 
    information between BGP peers. An UPDATE message 
    is used to advertise a single feasible route to a
    peer, or to withdraw multiple unfeasible routes 
    from service.                 

Adj\-RIBs\-In 
   The Adj\-RIBs\-In store routing information that has
   been learned from inbound UPDATE messages. Their 
   contents represent routes that are available as an 
   input to the Decision Process.

Loc\-RIB(BGP table) 
   The Loc\-RIB contains the local routing information
   that the BGP speaker has selected by applying its 
   local policies to the routing information contained 
   in its Adj\-RIBs\-In.

Adj\-RIBs\-Out 
   The Adj\-RIBs\-Out store the information that the
   local BGP speaker has selected for advertisement to 
   its peers. The routing information stored in the 
   Adj\-RIBs\-Out will be carried in the local BGP 
   speaker's UPDATE messages and advertised to its
   peers.

Path Attributes
   A variable length sequence of path attributes is 
   present in every UPDATE. Each path attribute is a 
   triple <attribute type, attribute length, 
   attribute value> of variable length. 

Network Layer Reachability Information(NLRI)
   A variable length field present in UPDATE messages
   which contains a list of Network Layer address 
   prefixes. 

Address Family Identifier(AFI) 
   Primary identifier to indicate the type of the 
   Network Layer Reachability Information(NLRI) being 
   carried.

Subsequent Address Family Identifier(SAFI) 
   Secondary identifier to indicate the type of the 
   Network Layer Reachability Information(NLRI) being 
   carried.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CbgpSafi(Enum):
    """
    CbgpSafi (Enum Class)

    Subsequent Address Family Identifier(SAFI) is used

    by BGP speaker to indicate the type of the the Network

    Layer Reachability Information(NLRI) being carried. 

    RFC\-2858 has defined the following values for SAFI.

    1 \- Network Layer Reachability Information used for 

        unicast forwarding

    2 \- Network Layer Reachability Information used for 

        multicast forwarding

    3 \- Network Layer Reachability Information used for 

        both unicast and multicast forwarding. 

    SAFI values 128 through 255 are for private use.

    .. data:: unicast = 1

    .. data:: multicast = 2

    .. data:: unicastAndMulticast = 3

    .. data:: vpn = 128

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    unicastAndMulticast = Enum.YLeaf(3, "unicastAndMulticast")

    vpn = Enum.YLeaf(128, "vpn")



class CISCOBGP4MIB(Entity):
    """
    
    
    .. attribute:: cbgpglobal
    
    	
    	**type**\:  :py:class:`CbgpGlobal <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpGlobal>`
    
    	**config**\: False
    
    .. attribute:: cbgproutetable
    
    	This table contains information about routes to destination networks from all BGP4 peers.  Since  BGP4 can carry routes for multiple Network Layer  protocols, this table has the Address Family  Identifier(AFI) of the Network Layer protocol as the  first index. Further for a given AFI, routes carried by BGP4 are distinguished based on Subsequent Address  Family Identifiers(SAFI).  Hence that is used as the second index.  Conceptually there is a separate Loc\-RIB maintained by the BGP speaker for each combination of  AFI and SAFI supported by it
    	**type**\:  :py:class:`CbgpRouteTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable>`
    
    	**config**\: False
    
    .. attribute:: cbgppeercapstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are  received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability  is received, this table is updated with a new  entry. When an existing capability is not received  during the latest connection establishment, the  corresponding entry is deleted from the table
    	**type**\:  :py:class:`CbgpPeerCapsTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerCapsTable>`
    
    	**config**\: False
    
    .. attribute:: cbgppeeraddrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP  connection establishment. When a new supported  address family is known, this table is updated  with a new entry. When an address family is not  supported any more, corresponding entry is deleted  from the table
    	**type**\:  :py:class:`CbgpPeerAddrFamilyTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyTable>`
    
    	**config**\: False
    
    .. attribute:: cbgppeeraddrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer.  Supported address families of a peer are known  during BGP connection establishment. When a new  supported address family is known, this table  is updated with a new entry. When an address  family is not supported any more, corresponding  entry is deleted from the table
    	**type**\:  :py:class:`CbgpPeerAddrFamilyPrefixTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable>`
    
    	**config**\: False
    
    .. attribute:: cbgppeer2table
    
    	BGP peer table.  This table contains, one entry per BGP peer, information about the connections with BGP peers
    	**type**\:  :py:class:`CbgpPeer2Table <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table>`
    
    	**config**\: False
    
    .. attribute:: cbgppeer2capstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability is received, this table is updated with a new entry. When an existing capability is not received during the latest connection establishment, the corresponding entry is deleted from the table
    	**type**\:  :py:class:`CbgpPeer2CapsTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2CapsTable>`
    
    	**config**\: False
    
    .. attribute:: cbgppeer2addrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\:  :py:class:`CbgpPeer2AddrFamilyTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyTable>`
    
    	**config**\: False
    
    .. attribute:: cbgppeer2addrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\:  :py:class:`CbgpPeer2AddrFamilyPrefixTable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-BGP4-MIB'
    _revision = '2010-09-30'

    def __init__(self):
        super(CISCOBGP4MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-BGP4-MIB"
        self.yang_parent_name = "CISCO-BGP4-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cbgpGlobal", ("cbgpglobal", CISCOBGP4MIB.CbgpGlobal)), ("cbgpRouteTable", ("cbgproutetable", CISCOBGP4MIB.CbgpRouteTable)), ("cbgpPeerCapsTable", ("cbgppeercapstable", CISCOBGP4MIB.CbgpPeerCapsTable)), ("cbgpPeerAddrFamilyTable", ("cbgppeeraddrfamilytable", CISCOBGP4MIB.CbgpPeerAddrFamilyTable)), ("cbgpPeerAddrFamilyPrefixTable", ("cbgppeeraddrfamilyprefixtable", CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable)), ("cbgpPeer2Table", ("cbgppeer2table", CISCOBGP4MIB.CbgpPeer2Table)), ("cbgpPeer2CapsTable", ("cbgppeer2capstable", CISCOBGP4MIB.CbgpPeer2CapsTable)), ("cbgpPeer2AddrFamilyTable", ("cbgppeer2addrfamilytable", CISCOBGP4MIB.CbgpPeer2AddrFamilyTable)), ("cbgpPeer2AddrFamilyPrefixTable", ("cbgppeer2addrfamilyprefixtable", CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable))])
        self._leafs = OrderedDict()

        self.cbgpglobal = CISCOBGP4MIB.CbgpGlobal()
        self.cbgpglobal.parent = self
        self._children_name_map["cbgpglobal"] = "cbgpGlobal"

        self.cbgproutetable = CISCOBGP4MIB.CbgpRouteTable()
        self.cbgproutetable.parent = self
        self._children_name_map["cbgproutetable"] = "cbgpRouteTable"

        self.cbgppeercapstable = CISCOBGP4MIB.CbgpPeerCapsTable()
        self.cbgppeercapstable.parent = self
        self._children_name_map["cbgppeercapstable"] = "cbgpPeerCapsTable"

        self.cbgppeeraddrfamilytable = CISCOBGP4MIB.CbgpPeerAddrFamilyTable()
        self.cbgppeeraddrfamilytable.parent = self
        self._children_name_map["cbgppeeraddrfamilytable"] = "cbgpPeerAddrFamilyTable"

        self.cbgppeeraddrfamilyprefixtable = CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable()
        self.cbgppeeraddrfamilyprefixtable.parent = self
        self._children_name_map["cbgppeeraddrfamilyprefixtable"] = "cbgpPeerAddrFamilyPrefixTable"

        self.cbgppeer2table = CISCOBGP4MIB.CbgpPeer2Table()
        self.cbgppeer2table.parent = self
        self._children_name_map["cbgppeer2table"] = "cbgpPeer2Table"

        self.cbgppeer2capstable = CISCOBGP4MIB.CbgpPeer2CapsTable()
        self.cbgppeer2capstable.parent = self
        self._children_name_map["cbgppeer2capstable"] = "cbgpPeer2CapsTable"

        self.cbgppeer2addrfamilytable = CISCOBGP4MIB.CbgpPeer2AddrFamilyTable()
        self.cbgppeer2addrfamilytable.parent = self
        self._children_name_map["cbgppeer2addrfamilytable"] = "cbgpPeer2AddrFamilyTable"

        self.cbgppeer2addrfamilyprefixtable = CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable()
        self.cbgppeer2addrfamilyprefixtable.parent = self
        self._children_name_map["cbgppeer2addrfamilyprefixtable"] = "cbgpPeer2AddrFamilyPrefixTable"
        self._segment_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOBGP4MIB, [], name, value)


    class CbgpGlobal(Entity):
        """
        
        
        .. attribute:: cbgpnotifsenable
        
        	Indicates whether the specific notifications are enabled.  If notifsEnable(0) bit is set to 1, then the notifications defined in ciscoBgp4NotificationsGroup1 are enabled;  If notifsPeer2Enable(1) bit is set to 1, then the notifications defined in ciscoBgp4Peer2NotificationsGroup are enabled
        	**type**\:  :py:class:`CbgpNotifsEnable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpGlobal.CbgpNotifsEnable>`
        
        	**config**\: False
        
        .. attribute:: cbgplocalas
        
        	The local autonomous system (AS) number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpGlobal, self).__init__()

            self.yang_name = "cbgpGlobal"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cbgpnotifsenable', (YLeaf(YType.bits, 'cbgpNotifsEnable'), ['Bits'])),
                ('cbgplocalas', (YLeaf(YType.uint32, 'cbgpLocalAs'), ['int'])),
            ])
            self.cbgpnotifsenable = Bits()
            self.cbgplocalas = None
            self._segment_path = lambda: "cbgpGlobal"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpGlobal, ['cbgpnotifsenable', 'cbgplocalas'], name, value)



    class CbgpRouteTable(Entity):
        """
        This table contains information about routes to
        destination networks from all BGP4 peers.  Since 
        BGP4 can carry routes for multiple Network Layer 
        protocols, this table has the Address Family 
        Identifier(AFI) of the Network Layer protocol as the 
        first index. Further for a given AFI, routes carried
        by BGP4 are distinguished based on Subsequent Address 
        Family Identifiers(SAFI).  Hence that is used as the
        second index.  Conceptually there is a separate Loc\-RIB
        maintained by the BGP speaker for each combination of 
        AFI and SAFI supported by it.
        
        .. attribute:: cbgprouteentry
        
        	Information about a path to a network received from a peer
        	**type**\: list of  		 :py:class:`CbgpRouteEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpRouteTable, self).__init__()

            self.yang_name = "cbgpRouteTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpRouteEntry", ("cbgprouteentry", CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry))])
            self._leafs = OrderedDict()

            self.cbgprouteentry = YList(self)
            self._segment_path = lambda: "cbgpRouteTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpRouteTable, [], name, value)


        class CbgpRouteEntry(Entity):
            """
            Information about a path to a network received from
            a peer.
            
            .. attribute:: cbgprouteafi  (key)
            
            	Represents Address Family Identifier(AFI) of the Network Layer protocol associated with the route. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgproutesafi  (key)
            
            	Represents Subsequent Address Family Identifier(SAFI) of the route. It gives additional information about the type of the route. An implementation is only  required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            	**config**\: False
            
            .. attribute:: cbgproutepeertype  (key)
            
            	Represents the type of Network Layer address stored in cbgpRoutePeer. An implementation is only required to support IPv4 address type(Value \- 1)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgproutepeer  (key)
            
            	The Network Layer address of the peer where the route information was learned. An implementation is only  required to support an IPv4 peer
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgprouteaddrprefix  (key)
            
            	A Network Address prefix in the Network Layer Reachability Information field of BGP UPDATE message. This object is a Network Address containing the prefix with length specified by cbgpRouteAddrPrefixLen. Any bits beyond the length specified by cbgpRouteAddrPrefixLen are zeroed
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgprouteaddrprefixlen  (key)
            
            	Length in bits of the Network Address prefix in the Network Layer Reachability Information field
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: cbgprouteorigin
            
            	The ultimate origin of the route information
            	**type**\:  :py:class:`CbgpRouteOrigin <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry.CbgpRouteOrigin>`
            
            	**config**\: False
            
            .. attribute:: cbgprouteaspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.  The type is a 1\-octet field which has two possible values\: 1  AS\_SET\: unordered set of ASs a route in the            UPDATE message has traversed 2  AS\_SEQUENCE\: ordered set of ASs a route in the                UPDATE message has traversed.  The length is a 1\-octet field containing the number of ASs in the value field.  The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm\:  first\-byte\-of\-pair = ASNumber / 256; second\-byte\-of\-pair = ASNumber & 255;
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgproutenexthop
            
            	The Network Layer address of the border router that should be used for the destination network
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgproutemedpresent
            
            	Indicates the presence/absence of MULTI\_EXIT\_DISC attribute for the route
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cbgproutemultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  The value of this object is irrelevant if the value of of cbgpRouteMedPresent is false(2)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgproutelocalprefpresent
            
            	Indicates the presence/absence of LOCAL\_PREF attribute for the route
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cbgproutelocalpref
            
            	The degree of preference calculated by the local BGP4 speaker for the route. The value of this object is  irrelevant if the value of cbgpRouteLocalPrefPresent  is false(2)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgprouteatomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:  :py:class:`CbgpRouteAtomicAggregate <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry.CbgpRouteAtomicAggregate>`
            
            	**config**\: False
            
            .. attribute:: cbgprouteaggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the  absence of this attribute
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cbgprouteaggregatoraddrtype
            
            	Represents the type of Network Layer address stored in cbgpRouteAggregatorAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgprouteaggregatoraddr
            
            	The Network Layer address of the last BGP4 speaker that performed route aggregation.  A value of all zeros indicates the absence of this attribute
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgproutebest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cbgprouteunknownattr
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object.    Each path attribute is a triple <attribute type, attribute length, attribute value> of variable length. Attribute Type is a two\-octet field that consists of the Attribute Flags octet followed by the Attribute Type Code octet.  If the Extended Length bit of the  Attribute Flags octet is set to 0, the third octet of  the Path Attribute contains the length of the attribute data in octets.  If the Extended Length bit  of the Attribute Flags octet is set to 1, then the third and the fourth octets of the path attribute  contain the length of the attribute data in octets. The remaining octets of the Path Attribute represent  the attribute value and are interpreted according to  the Attribute Flags and the Attribute Type Code
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry, self).__init__()

                self.yang_name = "cbgpRouteEntry"
                self.yang_parent_name = "cbgpRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgprouteafi','cbgproutesafi','cbgproutepeertype','cbgproutepeer','cbgprouteaddrprefix','cbgprouteaddrprefixlen']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgprouteafi', (YLeaf(YType.enumeration, 'cbgpRouteAfi'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgproutesafi', (YLeaf(YType.enumeration, 'cbgpRouteSafi'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpSafi', '')])),
                    ('cbgproutepeertype', (YLeaf(YType.enumeration, 'cbgpRoutePeerType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgproutepeer', (YLeaf(YType.str, 'cbgpRoutePeer'), ['str'])),
                    ('cbgprouteaddrprefix', (YLeaf(YType.str, 'cbgpRouteAddrPrefix'), ['str'])),
                    ('cbgprouteaddrprefixlen', (YLeaf(YType.uint32, 'cbgpRouteAddrPrefixLen'), ['int'])),
                    ('cbgprouteorigin', (YLeaf(YType.enumeration, 'cbgpRouteOrigin'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpRouteTable.CbgpRouteEntry.CbgpRouteOrigin')])),
                    ('cbgprouteaspathsegment', (YLeaf(YType.str, 'cbgpRouteASPathSegment'), ['str'])),
                    ('cbgproutenexthop', (YLeaf(YType.str, 'cbgpRouteNextHop'), ['str'])),
                    ('cbgproutemedpresent', (YLeaf(YType.boolean, 'cbgpRouteMedPresent'), ['bool'])),
                    ('cbgproutemultiexitdisc', (YLeaf(YType.uint32, 'cbgpRouteMultiExitDisc'), ['int'])),
                    ('cbgproutelocalprefpresent', (YLeaf(YType.boolean, 'cbgpRouteLocalPrefPresent'), ['bool'])),
                    ('cbgproutelocalpref', (YLeaf(YType.uint32, 'cbgpRouteLocalPref'), ['int'])),
                    ('cbgprouteatomicaggregate', (YLeaf(YType.enumeration, 'cbgpRouteAtomicAggregate'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpRouteTable.CbgpRouteEntry.CbgpRouteAtomicAggregate')])),
                    ('cbgprouteaggregatoras', (YLeaf(YType.uint32, 'cbgpRouteAggregatorAS'), ['int'])),
                    ('cbgprouteaggregatoraddrtype', (YLeaf(YType.enumeration, 'cbgpRouteAggregatorAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgprouteaggregatoraddr', (YLeaf(YType.str, 'cbgpRouteAggregatorAddr'), ['str'])),
                    ('cbgproutebest', (YLeaf(YType.boolean, 'cbgpRouteBest'), ['bool'])),
                    ('cbgprouteunknownattr', (YLeaf(YType.str, 'cbgpRouteUnknownAttr'), ['str'])),
                ])
                self.cbgprouteafi = None
                self.cbgproutesafi = None
                self.cbgproutepeertype = None
                self.cbgproutepeer = None
                self.cbgprouteaddrprefix = None
                self.cbgprouteaddrprefixlen = None
                self.cbgprouteorigin = None
                self.cbgprouteaspathsegment = None
                self.cbgproutenexthop = None
                self.cbgproutemedpresent = None
                self.cbgproutemultiexitdisc = None
                self.cbgproutelocalprefpresent = None
                self.cbgproutelocalpref = None
                self.cbgprouteatomicaggregate = None
                self.cbgprouteaggregatoras = None
                self.cbgprouteaggregatoraddrtype = None
                self.cbgprouteaggregatoraddr = None
                self.cbgproutebest = None
                self.cbgprouteunknownattr = None
                self._segment_path = lambda: "cbgpRouteEntry" + "[cbgpRouteAfi='" + str(self.cbgprouteafi) + "']" + "[cbgpRouteSafi='" + str(self.cbgproutesafi) + "']" + "[cbgpRoutePeerType='" + str(self.cbgproutepeertype) + "']" + "[cbgpRoutePeer='" + str(self.cbgproutepeer) + "']" + "[cbgpRouteAddrPrefix='" + str(self.cbgprouteaddrprefix) + "']" + "[cbgpRouteAddrPrefixLen='" + str(self.cbgprouteaddrprefixlen) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpRouteTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpRouteTable.CbgpRouteEntry, ['cbgprouteafi', 'cbgproutesafi', 'cbgproutepeertype', 'cbgproutepeer', 'cbgprouteaddrprefix', 'cbgprouteaddrprefixlen', 'cbgprouteorigin', 'cbgprouteaspathsegment', 'cbgproutenexthop', 'cbgproutemedpresent', 'cbgproutemultiexitdisc', 'cbgproutelocalprefpresent', 'cbgproutelocalpref', 'cbgprouteatomicaggregate', 'cbgprouteaggregatoras', 'cbgprouteaggregatoraddrtype', 'cbgprouteaggregatoraddr', 'cbgproutebest', 'cbgprouteunknownattr'], name, value)

            class CbgpRouteAtomicAggregate(Enum):
                """
                CbgpRouteAtomicAggregate (Enum Class)

                Whether or not the local system has selected a less

                specific route without selecting a more specific

                route.

                .. data:: lessSpecificRouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRouteNotSelected = Enum.YLeaf(1, "lessSpecificRouteNotSelected")

                lessSpecificRouteSelected = Enum.YLeaf(2, "lessSpecificRouteSelected")


            class CbgpRouteOrigin(Enum):
                """
                CbgpRouteOrigin (Enum Class)

                The ultimate origin of the route information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")





    class CbgpPeerCapsTable(Entity):
        """
        This table contains the capabilities that are
        supported by a peer. Capabilities of a peer are 
        received during BGP connection establishment.
        Values corresponding to each received capability
        are stored in this table. When a new capability 
        is received, this table is updated with a new 
        entry. When an existing capability is not received 
        during the latest connection establishment, the 
        corresponding entry is deleted from the table.
        
        .. attribute:: cbgppeercapsentry
        
        	Each entry represents a capability received from a peer with a particular code and an index. When a  capability is received multiple times with different values during a BGP connection establishment,  corresponding entries are differentiated with indices
        	**type**\: list of  		 :py:class:`CbgpPeerCapsEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeerCapsTable, self).__init__()

            self.yang_name = "cbgpPeerCapsTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeerCapsEntry", ("cbgppeercapsentry", CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry))])
            self._leafs = OrderedDict()

            self.cbgppeercapsentry = YList(self)
            self._segment_path = lambda: "cbgpPeerCapsTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeerCapsTable, [], name, value)


        class CbgpPeerCapsEntry(Entity):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a 
            capability is received multiple times with different
            values during a BGP connection establishment, 
            corresponding entries are differentiated with indices.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.BgpPeerTable.BgpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: cbgppeercapcode  (key)
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:  :py:class:`CbgpPeerCapCode <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry.CbgpPeerCapCode>`
            
            	**config**\: False
            
            .. attribute:: cbgppeercapindex  (key)
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\: int
            
            	**range:** 1..128
            
            	**config**\: False
            
            .. attribute:: cbgppeercapvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry, self).__init__()

                self.yang_name = "cbgpPeerCapsEntry"
                self.yang_parent_name = "cbgpPeerCapsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr','cbgppeercapcode','cbgppeercapindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', (YLeaf(YType.str, 'bgpPeerRemoteAddr'), ['str'])),
                    ('cbgppeercapcode', (YLeaf(YType.enumeration, 'cbgpPeerCapCode'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpPeerCapsTable.CbgpPeerCapsEntry.CbgpPeerCapCode')])),
                    ('cbgppeercapindex', (YLeaf(YType.uint32, 'cbgpPeerCapIndex'), ['int'])),
                    ('cbgppeercapvalue', (YLeaf(YType.str, 'cbgpPeerCapValue'), ['str'])),
                ])
                self.bgppeerremoteaddr = None
                self.cbgppeercapcode = None
                self.cbgppeercapindex = None
                self.cbgppeercapvalue = None
                self._segment_path = lambda: "cbgpPeerCapsEntry" + "[bgpPeerRemoteAddr='" + str(self.bgppeerremoteaddr) + "']" + "[cbgpPeerCapCode='" + str(self.cbgppeercapcode) + "']" + "[cbgpPeerCapIndex='" + str(self.cbgppeercapindex) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerCapsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeerCapsTable.CbgpPeerCapsEntry, ['bgppeerremoteaddr', 'cbgppeercapcode', 'cbgppeercapindex', 'cbgppeercapvalue'], name, value)

            class CbgpPeerCapCode(Enum):
                """
                CbgpPeerCapCode (Enum Class)

                The BGP Capability Advertisement Capability Code.

                .. data:: multiProtocol = 1

                .. data:: routeRefresh = 2

                .. data:: gracefulRestart = 64

                .. data:: routeRefreshOld = 128

                """

                multiProtocol = Enum.YLeaf(1, "multiProtocol")

                routeRefresh = Enum.YLeaf(2, "routeRefresh")

                gracefulRestart = Enum.YLeaf(64, "gracefulRestart")

                routeRefreshOld = Enum.YLeaf(128, "routeRefreshOld")





    class CbgpPeerAddrFamilyTable(Entity):
        """
        This table contains information related to
        address families supported by a peer. Supported
        address families of a peer are known during BGP 
        connection establishment. When a new supported 
        address family is known, this table is updated 
        with a new entry. When an address family is not 
        supported any more, corresponding entry is deleted 
        from the table.
        
        .. attribute:: cbgppeeraddrfamilyentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains names associated with an address family
        	**type**\: list of  		 :py:class:`CbgpPeerAddrFamilyEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyTable.CbgpPeerAddrFamilyEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeerAddrFamilyTable, self).__init__()

            self.yang_name = "cbgpPeerAddrFamilyTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeerAddrFamilyEntry", ("cbgppeeraddrfamilyentry", CISCOBGP4MIB.CbgpPeerAddrFamilyTable.CbgpPeerAddrFamilyEntry))])
            self._leafs = OrderedDict()

            self.cbgppeeraddrfamilyentry = YList(self)
            self._segment_path = lambda: "cbgpPeerAddrFamilyTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeerAddrFamilyTable, [], name, value)


        class CbgpPeerAddrFamilyEntry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.BgpPeerTable.BgpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: cbgppeeraddrfamilyafi  (key)
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and  VPNv4 (Value \- 1) address families
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeeraddrfamilysafi  (key)
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value  \- 1) and VPNv4( Value \- 128) address families
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            	**config**\: False
            
            .. attribute:: cbgppeeraddrfamilyname
            
            	Implementation specific Address Family name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeerAddrFamilyTable.CbgpPeerAddrFamilyEntry, self).__init__()

                self.yang_name = "cbgpPeerAddrFamilyEntry"
                self.yang_parent_name = "cbgpPeerAddrFamilyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr','cbgppeeraddrfamilyafi','cbgppeeraddrfamilysafi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', (YLeaf(YType.str, 'bgpPeerRemoteAddr'), ['str'])),
                    ('cbgppeeraddrfamilyafi', (YLeaf(YType.enumeration, 'cbgpPeerAddrFamilyAfi'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeeraddrfamilysafi', (YLeaf(YType.enumeration, 'cbgpPeerAddrFamilySafi'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpSafi', '')])),
                    ('cbgppeeraddrfamilyname', (YLeaf(YType.str, 'cbgpPeerAddrFamilyName'), ['str'])),
                ])
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeraddrfamilyname = None
                self._segment_path = lambda: "cbgpPeerAddrFamilyEntry" + "[bgpPeerRemoteAddr='" + str(self.bgppeerremoteaddr) + "']" + "[cbgpPeerAddrFamilyAfi='" + str(self.cbgppeeraddrfamilyafi) + "']" + "[cbgpPeerAddrFamilySafi='" + str(self.cbgppeeraddrfamilysafi) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerAddrFamilyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeerAddrFamilyTable.CbgpPeerAddrFamilyEntry, ['bgppeerremoteaddr', 'cbgppeeraddrfamilyafi', 'cbgppeeraddrfamilysafi', 'cbgppeeraddrfamilyname'], name, value)




    class CbgpPeerAddrFamilyPrefixTable(Entity):
        """
        This table contains prefix related information
        related to address families supported by a peer. 
        Supported address families of a peer are known 
        during BGP connection establishment. When a new 
        supported address family is known, this table 
        is updated with a new entry. When an address 
        family is not supported any more, corresponding 
        entry is deleted from the table.
        
        .. attribute:: cbgppeeraddrfamilyprefixentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains information associated  with route prefixes belonging to an address family
        	**type**\: list of  		 :py:class:`CbgpPeerAddrFamilyPrefixEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable.CbgpPeerAddrFamilyPrefixEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable, self).__init__()

            self.yang_name = "cbgpPeerAddrFamilyPrefixTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeerAddrFamilyPrefixEntry", ("cbgppeeraddrfamilyprefixentry", CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable.CbgpPeerAddrFamilyPrefixEntry))])
            self._leafs = OrderedDict()

            self.cbgppeeraddrfamilyprefixentry = YList(self)
            self._segment_path = lambda: "cbgpPeerAddrFamilyPrefixTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable, [], name, value)


        class CbgpPeerAddrFamilyPrefixEntry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated 
            with route prefixes belonging to an address family.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.BgpPeerTable.BgpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: cbgppeeraddrfamilyafi  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeeraddrfamilysafi  (key)
            
            	
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            	**config**\: False
            
            .. attribute:: cbgppeeracceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeerdeniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this  connection is denied. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeerprefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeerprefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or  corresponding SNMP notification is generated
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: cbgppeerprefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: cbgppeeradvertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeersuppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is  initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeerwithdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable.CbgpPeerAddrFamilyPrefixEntry, self).__init__()

                self.yang_name = "cbgpPeerAddrFamilyPrefixEntry"
                self.yang_parent_name = "cbgpPeerAddrFamilyPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr','cbgppeeraddrfamilyafi','cbgppeeraddrfamilysafi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', (YLeaf(YType.str, 'bgpPeerRemoteAddr'), ['str'])),
                    ('cbgppeeraddrfamilyafi', (YLeaf(YType.enumeration, 'cbgpPeerAddrFamilyAfi'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeeraddrfamilysafi', (YLeaf(YType.enumeration, 'cbgpPeerAddrFamilySafi'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpSafi', '')])),
                    ('cbgppeeracceptedprefixes', (YLeaf(YType.uint32, 'cbgpPeerAcceptedPrefixes'), ['int'])),
                    ('cbgppeerdeniedprefixes', (YLeaf(YType.uint32, 'cbgpPeerDeniedPrefixes'), ['int'])),
                    ('cbgppeerprefixadminlimit', (YLeaf(YType.uint32, 'cbgpPeerPrefixAdminLimit'), ['int'])),
                    ('cbgppeerprefixthreshold', (YLeaf(YType.uint32, 'cbgpPeerPrefixThreshold'), ['int'])),
                    ('cbgppeerprefixclearthreshold', (YLeaf(YType.uint32, 'cbgpPeerPrefixClearThreshold'), ['int'])),
                    ('cbgppeeradvertisedprefixes', (YLeaf(YType.uint32, 'cbgpPeerAdvertisedPrefixes'), ['int'])),
                    ('cbgppeersuppressedprefixes', (YLeaf(YType.uint32, 'cbgpPeerSuppressedPrefixes'), ['int'])),
                    ('cbgppeerwithdrawnprefixes', (YLeaf(YType.uint32, 'cbgpPeerWithdrawnPrefixes'), ['int'])),
                ])
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeracceptedprefixes = None
                self.cbgppeerdeniedprefixes = None
                self.cbgppeerprefixadminlimit = None
                self.cbgppeerprefixthreshold = None
                self.cbgppeerprefixclearthreshold = None
                self.cbgppeeradvertisedprefixes = None
                self.cbgppeersuppressedprefixes = None
                self.cbgppeerwithdrawnprefixes = None
                self._segment_path = lambda: "cbgpPeerAddrFamilyPrefixEntry" + "[bgpPeerRemoteAddr='" + str(self.bgppeerremoteaddr) + "']" + "[cbgpPeerAddrFamilyAfi='" + str(self.cbgppeeraddrfamilyafi) + "']" + "[cbgpPeerAddrFamilySafi='" + str(self.cbgppeeraddrfamilysafi) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerAddrFamilyPrefixTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeerAddrFamilyPrefixTable.CbgpPeerAddrFamilyPrefixEntry, ['bgppeerremoteaddr', 'cbgppeeraddrfamilyafi', 'cbgppeeraddrfamilysafi', 'cbgppeeracceptedprefixes', 'cbgppeerdeniedprefixes', 'cbgppeerprefixadminlimit', 'cbgppeerprefixthreshold', 'cbgppeerprefixclearthreshold', 'cbgppeeradvertisedprefixes', 'cbgppeersuppressedprefixes', 'cbgppeerwithdrawnprefixes'], name, value)




    class CbgpPeer2Table(Entity):
        """
        BGP peer table.  This table contains,
        one entry per BGP peer, information about
        the connections with BGP peers.
        
        .. attribute:: cbgppeer2entry
        
        	Entry containing information about the connection with a BGP peer
        	**type**\: list of  		 :py:class:`CbgpPeer2Entry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeer2Table, self).__init__()

            self.yang_name = "cbgpPeer2Table"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeer2Entry", ("cbgppeer2entry", CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry))])
            self._leafs = OrderedDict()

            self.cbgppeer2entry = YList(self)
            self._segment_path = lambda: "cbgpPeer2Table"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeer2Table, [], name, value)


        class CbgpPeer2Entry(Entity):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: cbgppeer2type  (key)
            
            	Represents the type of Peer address stored in cbgpPeer2Entry
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	The remote IP address of this entry's BGP peer
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgppeer2state
            
            	The BGP peer connection state
            	**type**\:  :py:class:`CbgpPeer2State <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2State>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2adminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Manual Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Manual Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:  :py:class:`CbgpPeer2AdminStatus <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2AdminStatus>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2negotiatedversion
            
            	The negotiated version of BGP running between the two peers.  This entry MUST be zero (0) unless the cbgpPeer2State is in the openconfirm or the established state.  Note that legal values for this object are between 0 and 255
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cbgppeer2localaddr
            
            	The local IP address of this entry's BGP connection
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cbgppeer2localport
            
            	The local port for the TCP connection between the BGP peers
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cbgppeer2localas
            
            	The local AS number for this session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2localidentifier
            
            	The BGP Identifier of this entry's BGP peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteport
            
            	The remote port for the TCP connection between the BGP peers.  Note that the objects cbgpPeer2LocalAddr, cbgpPeer2LocalPort, cbgpPeer2RemoteAddr, and cbgpPeer2RemotePort provide the appropriate reference to the standard MIB TCP connection table
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteas
            
            	The remote autonomous system number received in the BGP OPEN message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteidentifier
            
            	The BGP Identifier of this entry's BGP peer. This entry MUST be 0.0.0.0 unless the cbgpPeer2State is in the openconfirm or the established state
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: cbgppeer2inupdates
            
            	The number of BGP UPDATE messages received on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2outupdates
            
            	The number of BGP UPDATE messages transmitted on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2intotalmessages
            
            	The total number of messages received from the remote peer on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2outtotalmessages
            
            	The total number of messages transmitted to the remote peer on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2lasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\: str
            
            	**length:** 2..2
            
            	**config**\: False
            
            .. attribute:: cbgppeer2fsmestablishedtransitions
            
            	The total number of times the BGP FSM transitioned into the established state for this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2fsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the established state or how long since this peer was last in the established state.  It is set to zero when a new peer is configured or when the router is booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2connectretryinterval
            
            	Time interval (in seconds) for the ConnectRetry timer.  The suggested value for this timer is 120 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2holdtime
            
            	Time interval (in seconds) for the Hold Timer established with the peer.  The value of this object is calculated by this BGP speaker, using the smaller of the values in cbgpPeer2HoldTimeConfigured and the Hold Time received in the OPEN message.  This value must be at least three seconds if it is not zero (0).  If the Hold Timer has not been established with the peer this object MUST have a value of zero (0).  If the cbgpPeer2HoldTimeConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\: int
            
            	**range:** 0..0 \| 3..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2keepalive
            
            	Time interval (in seconds) for the KeepAlive timer established with the peer.  The value of this object is calculated by this BGP speaker such that, when compared with cbgpPeer2HoldTime, it has the same proportion that cbgpPeer2KeepAliveConfigured has, compared with cbgpPeer2HoldTimeConfigured.  If the KeepAlive timer has not been established with the peer, this object MUST have a value of zero (0).  If the of cbgpPeer2KeepAliveConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\: int
            
            	**range:** 0..21845
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2holdtimeconfigured
            
            	Time interval (in seconds) for the Hold Time configured for this BGP speaker with this peer.  This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (cbgpPeer2HoldTime) with the peer. This value must not be less than three seconds if it is not zero (0).  If it is zero (0), the Hold Time is NOT to be established with the peer.  The suggested value for this timer is 90 seconds
            	**type**\: int
            
            	**range:** 0..0 \| 3..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2keepaliveconfigured
            
            	Time interval (in seconds) for the KeepAlive timer configured for this BGP speaker with this peer.  The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in cbgpPeer2HoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by cbgpPeer2KeepAlive.  A reasonable maximum value for this timer would be one third of that of cbgpPeer2HoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established.  The suggested value for this timer is 30 seconds
            	**type**\: int
            
            	**range:** 0..21845
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2minasoriginationinterval
            
            	Time interval (in seconds) for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2minrouteadvertisementinterval
            
            	Time interval (in seconds) for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds for EBGP connections and 5 seconds for IBGP connections
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2inupdateelapsedtime
            
            	Elapsed time (in seconds) since the last BGP UPDATE message was received from the peer. Each time cbgpPeer2InUpdates is incremented, the value of this object is set to zero (0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2lasterrortxt
            
            	Implementation specific error description for bgpPeerLastErrorReceived
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cbgppeer2prevstate
            
            	The BGP peer connection previous state
            	**type**\:  :py:class:`CbgpPeer2PrevState <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2PrevState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry, self).__init__()

                self.yang_name = "cbgpPeer2Entry"
                self.yang_parent_name = "cbgpPeer2Table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', (YLeaf(YType.enumeration, 'cbgpPeer2Type'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeer2remoteaddr', (YLeaf(YType.str, 'cbgpPeer2RemoteAddr'), ['str'])),
                    ('cbgppeer2state', (YLeaf(YType.enumeration, 'cbgpPeer2State'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2State')])),
                    ('cbgppeer2adminstatus', (YLeaf(YType.enumeration, 'cbgpPeer2AdminStatus'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2AdminStatus')])),
                    ('cbgppeer2negotiatedversion', (YLeaf(YType.int32, 'cbgpPeer2NegotiatedVersion'), ['int'])),
                    ('cbgppeer2localaddr', (YLeaf(YType.str, 'cbgpPeer2LocalAddr'), ['str'])),
                    ('cbgppeer2localport', (YLeaf(YType.uint16, 'cbgpPeer2LocalPort'), ['int'])),
                    ('cbgppeer2localas', (YLeaf(YType.uint32, 'cbgpPeer2LocalAs'), ['int'])),
                    ('cbgppeer2localidentifier', (YLeaf(YType.str, 'cbgpPeer2LocalIdentifier'), ['str'])),
                    ('cbgppeer2remoteport', (YLeaf(YType.uint16, 'cbgpPeer2RemotePort'), ['int'])),
                    ('cbgppeer2remoteas', (YLeaf(YType.uint32, 'cbgpPeer2RemoteAs'), ['int'])),
                    ('cbgppeer2remoteidentifier', (YLeaf(YType.str, 'cbgpPeer2RemoteIdentifier'), ['str'])),
                    ('cbgppeer2inupdates', (YLeaf(YType.uint32, 'cbgpPeer2InUpdates'), ['int'])),
                    ('cbgppeer2outupdates', (YLeaf(YType.uint32, 'cbgpPeer2OutUpdates'), ['int'])),
                    ('cbgppeer2intotalmessages', (YLeaf(YType.uint32, 'cbgpPeer2InTotalMessages'), ['int'])),
                    ('cbgppeer2outtotalmessages', (YLeaf(YType.uint32, 'cbgpPeer2OutTotalMessages'), ['int'])),
                    ('cbgppeer2lasterror', (YLeaf(YType.str, 'cbgpPeer2LastError'), ['str'])),
                    ('cbgppeer2fsmestablishedtransitions', (YLeaf(YType.uint32, 'cbgpPeer2FsmEstablishedTransitions'), ['int'])),
                    ('cbgppeer2fsmestablishedtime', (YLeaf(YType.uint32, 'cbgpPeer2FsmEstablishedTime'), ['int'])),
                    ('cbgppeer2connectretryinterval', (YLeaf(YType.int32, 'cbgpPeer2ConnectRetryInterval'), ['int'])),
                    ('cbgppeer2holdtime', (YLeaf(YType.int32, 'cbgpPeer2HoldTime'), ['int'])),
                    ('cbgppeer2keepalive', (YLeaf(YType.int32, 'cbgpPeer2KeepAlive'), ['int'])),
                    ('cbgppeer2holdtimeconfigured', (YLeaf(YType.int32, 'cbgpPeer2HoldTimeConfigured'), ['int'])),
                    ('cbgppeer2keepaliveconfigured', (YLeaf(YType.int32, 'cbgpPeer2KeepAliveConfigured'), ['int'])),
                    ('cbgppeer2minasoriginationinterval', (YLeaf(YType.int32, 'cbgpPeer2MinASOriginationInterval'), ['int'])),
                    ('cbgppeer2minrouteadvertisementinterval', (YLeaf(YType.int32, 'cbgpPeer2MinRouteAdvertisementInterval'), ['int'])),
                    ('cbgppeer2inupdateelapsedtime', (YLeaf(YType.uint32, 'cbgpPeer2InUpdateElapsedTime'), ['int'])),
                    ('cbgppeer2lasterrortxt', (YLeaf(YType.str, 'cbgpPeer2LastErrorTxt'), ['str'])),
                    ('cbgppeer2prevstate', (YLeaf(YType.enumeration, 'cbgpPeer2PrevState'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpPeer2Table.CbgpPeer2Entry.CbgpPeer2PrevState')])),
                ])
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2state = None
                self.cbgppeer2adminstatus = None
                self.cbgppeer2negotiatedversion = None
                self.cbgppeer2localaddr = None
                self.cbgppeer2localport = None
                self.cbgppeer2localas = None
                self.cbgppeer2localidentifier = None
                self.cbgppeer2remoteport = None
                self.cbgppeer2remoteas = None
                self.cbgppeer2remoteidentifier = None
                self.cbgppeer2inupdates = None
                self.cbgppeer2outupdates = None
                self.cbgppeer2intotalmessages = None
                self.cbgppeer2outtotalmessages = None
                self.cbgppeer2lasterror = None
                self.cbgppeer2fsmestablishedtransitions = None
                self.cbgppeer2fsmestablishedtime = None
                self.cbgppeer2connectretryinterval = None
                self.cbgppeer2holdtime = None
                self.cbgppeer2keepalive = None
                self.cbgppeer2holdtimeconfigured = None
                self.cbgppeer2keepaliveconfigured = None
                self.cbgppeer2minasoriginationinterval = None
                self.cbgppeer2minrouteadvertisementinterval = None
                self.cbgppeer2inupdateelapsedtime = None
                self.cbgppeer2lasterrortxt = None
                self.cbgppeer2prevstate = None
                self._segment_path = lambda: "cbgpPeer2Entry" + "[cbgpPeer2Type='" + str(self.cbgppeer2type) + "']" + "[cbgpPeer2RemoteAddr='" + str(self.cbgppeer2remoteaddr) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2Table/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2state', 'cbgppeer2adminstatus', 'cbgppeer2negotiatedversion', 'cbgppeer2localaddr', 'cbgppeer2localport', 'cbgppeer2localas', 'cbgppeer2localidentifier', 'cbgppeer2remoteport', 'cbgppeer2remoteas', 'cbgppeer2remoteidentifier', 'cbgppeer2inupdates', 'cbgppeer2outupdates', 'cbgppeer2intotalmessages', 'cbgppeer2outtotalmessages', 'cbgppeer2lasterror', 'cbgppeer2fsmestablishedtransitions', 'cbgppeer2fsmestablishedtime', 'cbgppeer2connectretryinterval', 'cbgppeer2holdtime', 'cbgppeer2keepalive', 'cbgppeer2holdtimeconfigured', 'cbgppeer2keepaliveconfigured', 'cbgppeer2minasoriginationinterval', 'cbgppeer2minrouteadvertisementinterval', 'cbgppeer2inupdateelapsedtime', 'cbgppeer2lasterrortxt', 'cbgppeer2prevstate'], name, value)

            class CbgpPeer2AdminStatus(Enum):
                """
                CbgpPeer2AdminStatus (Enum Class)

                The desired state of the BGP connection.

                A transition from 'stop' to 'start' will cause

                the BGP Manual Start Event to be generated.

                A transition from 'start' to 'stop' will cause

                the BGP Manual Stop Event to be generated.

                This parameter can be used to restart BGP peer

                connections.  Care should be used in providing

                write access to this object without adequate

                authentication.

                .. data:: stop = 1

                .. data:: start = 2

                """

                stop = Enum.YLeaf(1, "stop")

                start = Enum.YLeaf(2, "start")


            class CbgpPeer2PrevState(Enum):
                """
                CbgpPeer2PrevState (Enum Class)

                The BGP peer connection previous state.

                .. data:: none = 0

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                none = Enum.YLeaf(0, "none")

                idle = Enum.YLeaf(1, "idle")

                connect = Enum.YLeaf(2, "connect")

                active = Enum.YLeaf(3, "active")

                opensent = Enum.YLeaf(4, "opensent")

                openconfirm = Enum.YLeaf(5, "openconfirm")

                established = Enum.YLeaf(6, "established")


            class CbgpPeer2State(Enum):
                """
                CbgpPeer2State (Enum Class)

                The BGP peer connection state.

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                idle = Enum.YLeaf(1, "idle")

                connect = Enum.YLeaf(2, "connect")

                active = Enum.YLeaf(3, "active")

                opensent = Enum.YLeaf(4, "opensent")

                openconfirm = Enum.YLeaf(5, "openconfirm")

                established = Enum.YLeaf(6, "established")





    class CbgpPeer2CapsTable(Entity):
        """
        This table contains the capabilities that are
        supported by a peer. Capabilities of a peer are
        received during BGP connection establishment.
        Values corresponding to each received capability
        are stored in this table. When a new capability
        is received, this table is updated with a new
        entry. When an existing capability is not received
        during the latest connection establishment, the
        corresponding entry is deleted from the table.
        
        .. attribute:: cbgppeer2capsentry
        
        	Each entry represents a capability received from a peer with a particular code and an index. When a capability is received multiple times with different values during a BGP connection establishment, corresponding entries are differentiated with indices
        	**type**\: list of  		 :py:class:`CbgpPeer2CapsEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeer2CapsTable, self).__init__()

            self.yang_name = "cbgpPeer2CapsTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeer2CapsEntry", ("cbgppeer2capsentry", CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry))])
            self._leafs = OrderedDict()

            self.cbgppeer2capsentry = YList(self)
            self._segment_path = lambda: "cbgpPeer2CapsTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeer2CapsTable, [], name, value)


        class CbgpPeer2CapsEntry(Entity):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a
            capability is received multiple times with different
            values during a BGP connection establishment,
            corresponding entries are differentiated with indices.
            
            .. attribute:: cbgppeer2type  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2capcode  (key)
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:  :py:class:`CbgpPeer2CapCode <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry.CbgpPeer2CapCode>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2capindex  (key)
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\: int
            
            	**range:** 1..128
            
            	**config**\: False
            
            .. attribute:: cbgppeer2capvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  4\-Byte AS Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Additional Paths       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Send/Receive (8 bits)            \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry, self).__init__()

                self.yang_name = "cbgpPeer2CapsEntry"
                self.yang_parent_name = "cbgpPeer2CapsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr','cbgppeer2capcode','cbgppeer2capindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', (YLeaf(YType.enumeration, 'cbgpPeer2Type'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeer2remoteaddr', (YLeaf(YType.str, 'cbgpPeer2RemoteAddr'), ['str'])),
                    ('cbgppeer2capcode', (YLeaf(YType.enumeration, 'cbgpPeer2CapCode'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CISCOBGP4MIB', 'CbgpPeer2CapsTable.CbgpPeer2CapsEntry.CbgpPeer2CapCode')])),
                    ('cbgppeer2capindex', (YLeaf(YType.uint32, 'cbgpPeer2CapIndex'), ['int'])),
                    ('cbgppeer2capvalue', (YLeaf(YType.str, 'cbgpPeer2CapValue'), ['str'])),
                ])
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2capcode = None
                self.cbgppeer2capindex = None
                self.cbgppeer2capvalue = None
                self._segment_path = lambda: "cbgpPeer2CapsEntry" + "[cbgpPeer2Type='" + str(self.cbgppeer2type) + "']" + "[cbgpPeer2RemoteAddr='" + str(self.cbgppeer2remoteaddr) + "']" + "[cbgpPeer2CapCode='" + str(self.cbgppeer2capcode) + "']" + "[cbgpPeer2CapIndex='" + str(self.cbgppeer2capindex) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2CapsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeer2CapsTable.CbgpPeer2CapsEntry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2capcode', 'cbgppeer2capindex', 'cbgppeer2capvalue'], name, value)

            class CbgpPeer2CapCode(Enum):
                """
                CbgpPeer2CapCode (Enum Class)

                The BGP Capability Advertisement Capability Code.

                .. data:: multiProtocol = 1

                .. data:: routeRefresh = 2

                .. data:: gracefulRestart = 64

                .. data:: fourByteAs = 65

                .. data:: addPath = 69

                .. data:: routeRefreshOld = 128

                """

                multiProtocol = Enum.YLeaf(1, "multiProtocol")

                routeRefresh = Enum.YLeaf(2, "routeRefresh")

                gracefulRestart = Enum.YLeaf(64, "gracefulRestart")

                fourByteAs = Enum.YLeaf(65, "fourByteAs")

                addPath = Enum.YLeaf(69, "addPath")

                routeRefreshOld = Enum.YLeaf(128, "routeRefreshOld")





    class CbgpPeer2AddrFamilyTable(Entity):
        """
        This table contains information related to
        address families supported by a peer. Supported
        address families of a peer are known during BGP
        connection establishment. When a new supported
        address family is known, this table is updated
        with a new entry. When an address family is not
        supported any more, corresponding entry is deleted
        from the table.
        
        .. attribute:: cbgppeer2addrfamilyentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains names associated with an address family
        	**type**\: list of  		 :py:class:`CbgpPeer2AddrFamilyEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyTable.CbgpPeer2AddrFamilyEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeer2AddrFamilyTable, self).__init__()

            self.yang_name = "cbgpPeer2AddrFamilyTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeer2AddrFamilyEntry", ("cbgppeer2addrfamilyentry", CISCOBGP4MIB.CbgpPeer2AddrFamilyTable.CbgpPeer2AddrFamilyEntry))])
            self._leafs = OrderedDict()

            self.cbgppeer2addrfamilyentry = YList(self)
            self._segment_path = lambda: "cbgpPeer2AddrFamilyTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeer2AddrFamilyTable, [], name, value)


        class CbgpPeer2AddrFamilyEntry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: cbgppeer2type  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2addrfamilyafi  (key)
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2addrfamilysafi  (key)
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2addrfamilyname
            
            	Implementation specific Address Family name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeer2AddrFamilyTable.CbgpPeer2AddrFamilyEntry, self).__init__()

                self.yang_name = "cbgpPeer2AddrFamilyEntry"
                self.yang_parent_name = "cbgpPeer2AddrFamilyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr','cbgppeer2addrfamilyafi','cbgppeer2addrfamilysafi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', (YLeaf(YType.enumeration, 'cbgpPeer2Type'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeer2remoteaddr', (YLeaf(YType.str, 'cbgpPeer2RemoteAddr'), ['str'])),
                    ('cbgppeer2addrfamilyafi', (YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilyAfi'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeer2addrfamilysafi', (YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilySafi'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpSafi', '')])),
                    ('cbgppeer2addrfamilyname', (YLeaf(YType.str, 'cbgpPeer2AddrFamilyName'), ['str'])),
                ])
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2addrfamilyname = None
                self._segment_path = lambda: "cbgpPeer2AddrFamilyEntry" + "[cbgpPeer2Type='" + str(self.cbgppeer2type) + "']" + "[cbgpPeer2RemoteAddr='" + str(self.cbgppeer2remoteaddr) + "']" + "[cbgpPeer2AddrFamilyAfi='" + str(self.cbgppeer2addrfamilyafi) + "']" + "[cbgpPeer2AddrFamilySafi='" + str(self.cbgppeer2addrfamilysafi) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2AddrFamilyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeer2AddrFamilyTable.CbgpPeer2AddrFamilyEntry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2addrfamilyafi', 'cbgppeer2addrfamilysafi', 'cbgppeer2addrfamilyname'], name, value)




    class CbgpPeer2AddrFamilyPrefixTable(Entity):
        """
        This table contains prefix related information
        related to address families supported by a peer.
        Supported address families of a peer are known
        during BGP connection establishment. When a new
        supported address family is known, this table
        is updated with a new entry. When an address
        family is not supported any more, corresponding
        entry is deleted from the table.
        
        .. attribute:: cbgppeer2addrfamilyprefixentry
        
        	An entry is identified by an AFI/SAFI pair and peer address. It contains information associated with route prefixes belonging to an address family
        	**type**\: list of  		 :py:class:`CbgpPeer2AddrFamilyPrefixEntry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable.CbgpPeer2AddrFamilyPrefixEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable, self).__init__()

            self.yang_name = "cbgpPeer2AddrFamilyPrefixTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cbgpPeer2AddrFamilyPrefixEntry", ("cbgppeer2addrfamilyprefixentry", CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable.CbgpPeer2AddrFamilyPrefixEntry))])
            self._leafs = OrderedDict()

            self.cbgppeer2addrfamilyprefixentry = YList(self)
            self._segment_path = lambda: "cbgpPeer2AddrFamilyPrefixTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable, [], name, value)


        class CbgpPeer2AddrFamilyPrefixEntry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated
            with route prefixes belonging to an address family.
            
            .. attribute:: cbgppeer2type  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.CbgpPeer2Table.CbgpPeer2Entry>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2addrfamilyafi  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2addrfamilysafi  (key)
            
            	
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            	**config**\: False
            
            .. attribute:: cbgppeer2acceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2deniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this connection is denied. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2prefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2prefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or corresponding SNMP notification is generated
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cbgppeer2prefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cbgppeer2advertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2suppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cbgppeer2withdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable.CbgpPeer2AddrFamilyPrefixEntry, self).__init__()

                self.yang_name = "cbgpPeer2AddrFamilyPrefixEntry"
                self.yang_parent_name = "cbgpPeer2AddrFamilyPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr','cbgppeer2addrfamilyafi','cbgppeer2addrfamilysafi']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', (YLeaf(YType.enumeration, 'cbgpPeer2Type'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeer2remoteaddr', (YLeaf(YType.str, 'cbgpPeer2RemoteAddr'), ['str'])),
                    ('cbgppeer2addrfamilyafi', (YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilyAfi'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cbgppeer2addrfamilysafi', (YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilySafi'), [('ydk.models.cisco_ios_xe.CISCO_BGP4_MIB', 'CbgpSafi', '')])),
                    ('cbgppeer2acceptedprefixes', (YLeaf(YType.uint32, 'cbgpPeer2AcceptedPrefixes'), ['int'])),
                    ('cbgppeer2deniedprefixes', (YLeaf(YType.uint32, 'cbgpPeer2DeniedPrefixes'), ['int'])),
                    ('cbgppeer2prefixadminlimit', (YLeaf(YType.uint32, 'cbgpPeer2PrefixAdminLimit'), ['int'])),
                    ('cbgppeer2prefixthreshold', (YLeaf(YType.uint32, 'cbgpPeer2PrefixThreshold'), ['int'])),
                    ('cbgppeer2prefixclearthreshold', (YLeaf(YType.uint32, 'cbgpPeer2PrefixClearThreshold'), ['int'])),
                    ('cbgppeer2advertisedprefixes', (YLeaf(YType.uint32, 'cbgpPeer2AdvertisedPrefixes'), ['int'])),
                    ('cbgppeer2suppressedprefixes', (YLeaf(YType.uint32, 'cbgpPeer2SuppressedPrefixes'), ['int'])),
                    ('cbgppeer2withdrawnprefixes', (YLeaf(YType.uint32, 'cbgpPeer2WithdrawnPrefixes'), ['int'])),
                ])
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2acceptedprefixes = None
                self.cbgppeer2deniedprefixes = None
                self.cbgppeer2prefixadminlimit = None
                self.cbgppeer2prefixthreshold = None
                self.cbgppeer2prefixclearthreshold = None
                self.cbgppeer2advertisedprefixes = None
                self.cbgppeer2suppressedprefixes = None
                self.cbgppeer2withdrawnprefixes = None
                self._segment_path = lambda: "cbgpPeer2AddrFamilyPrefixEntry" + "[cbgpPeer2Type='" + str(self.cbgppeer2type) + "']" + "[cbgpPeer2RemoteAddr='" + str(self.cbgppeer2remoteaddr) + "']" + "[cbgpPeer2AddrFamilyAfi='" + str(self.cbgppeer2addrfamilyafi) + "']" + "[cbgpPeer2AddrFamilySafi='" + str(self.cbgppeer2addrfamilysafi) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2AddrFamilyPrefixTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.CbgpPeer2AddrFamilyPrefixTable.CbgpPeer2AddrFamilyPrefixEntry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2addrfamilyafi', 'cbgppeer2addrfamilysafi', 'cbgppeer2acceptedprefixes', 'cbgppeer2deniedprefixes', 'cbgppeer2prefixadminlimit', 'cbgppeer2prefixthreshold', 'cbgppeer2prefixclearthreshold', 'cbgppeer2advertisedprefixes', 'cbgppeer2suppressedprefixes', 'cbgppeer2withdrawnprefixes'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOBGP4MIB()
        return self._top_entity



