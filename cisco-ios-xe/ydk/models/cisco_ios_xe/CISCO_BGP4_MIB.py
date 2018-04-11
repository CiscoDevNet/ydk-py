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
    
    	
    	**type**\:  :py:class:`Cbgpglobal <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgpglobal>`
    
    .. attribute:: cbgproutetable
    
    	This table contains information about routes to destination networks from all BGP4 peers.  Since  BGP4 can carry routes for multiple Network Layer  protocols, this table has the Address Family  Identifier(AFI) of the Network Layer protocol as the  first index. Further for a given AFI, routes carried by BGP4 are distinguished based on Subsequent Address  Family Identifiers(SAFI).  Hence that is used as the second index.  Conceptually there is a separate Loc\-RIB maintained by the BGP speaker for each combination of  AFI and SAFI supported by it
    	**type**\:  :py:class:`Cbgproutetable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgproutetable>`
    
    .. attribute:: cbgppeercapstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are  received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability  is received, this table is updated with a new  entry. When an existing capability is not received  during the latest connection establishment, the  corresponding entry is deleted from the table
    	**type**\:  :py:class:`Cbgppeercapstable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeercapstable>`
    
    .. attribute:: cbgppeeraddrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP  connection establishment. When a new supported  address family is known, this table is updated  with a new entry. When an address family is not  supported any more, corresponding entry is deleted  from the table
    	**type**\:  :py:class:`Cbgppeeraddrfamilytable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeeraddrfamilytable>`
    
    .. attribute:: cbgppeeraddrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer.  Supported address families of a peer are known  during BGP connection establishment. When a new  supported address family is known, this table  is updated with a new entry. When an address  family is not supported any more, corresponding  entry is deleted from the table
    	**type**\:  :py:class:`Cbgppeeraddrfamilyprefixtable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable>`
    
    .. attribute:: cbgppeer2table
    
    	BGP peer table.  This table contains, one entry per BGP peer, information about the connections with BGP peers
    	**type**\:  :py:class:`Cbgppeer2Table <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table>`
    
    .. attribute:: cbgppeer2capstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability is received, this table is updated with a new entry. When an existing capability is not received during the latest connection establishment, the corresponding entry is deleted from the table
    	**type**\:  :py:class:`Cbgppeer2Capstable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Capstable>`
    
    .. attribute:: cbgppeer2addrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\:  :py:class:`Cbgppeer2Addrfamilytable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Addrfamilytable>`
    
    .. attribute:: cbgppeer2addrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\:  :py:class:`Cbgppeer2Addrfamilyprefixtable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable>`
    
    

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
        self._child_container_classes = OrderedDict([("cbgpGlobal", ("cbgpglobal", CISCOBGP4MIB.Cbgpglobal)), ("cbgpRouteTable", ("cbgproutetable", CISCOBGP4MIB.Cbgproutetable)), ("cbgpPeerCapsTable", ("cbgppeercapstable", CISCOBGP4MIB.Cbgppeercapstable)), ("cbgpPeerAddrFamilyTable", ("cbgppeeraddrfamilytable", CISCOBGP4MIB.Cbgppeeraddrfamilytable)), ("cbgpPeerAddrFamilyPrefixTable", ("cbgppeeraddrfamilyprefixtable", CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable)), ("cbgpPeer2Table", ("cbgppeer2table", CISCOBGP4MIB.Cbgppeer2Table)), ("cbgpPeer2CapsTable", ("cbgppeer2capstable", CISCOBGP4MIB.Cbgppeer2Capstable)), ("cbgpPeer2AddrFamilyTable", ("cbgppeer2addrfamilytable", CISCOBGP4MIB.Cbgppeer2Addrfamilytable)), ("cbgpPeer2AddrFamilyPrefixTable", ("cbgppeer2addrfamilyprefixtable", CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cbgpglobal = CISCOBGP4MIB.Cbgpglobal()
        self.cbgpglobal.parent = self
        self._children_name_map["cbgpglobal"] = "cbgpGlobal"
        self._children_yang_names.add("cbgpGlobal")

        self.cbgproutetable = CISCOBGP4MIB.Cbgproutetable()
        self.cbgproutetable.parent = self
        self._children_name_map["cbgproutetable"] = "cbgpRouteTable"
        self._children_yang_names.add("cbgpRouteTable")

        self.cbgppeercapstable = CISCOBGP4MIB.Cbgppeercapstable()
        self.cbgppeercapstable.parent = self
        self._children_name_map["cbgppeercapstable"] = "cbgpPeerCapsTable"
        self._children_yang_names.add("cbgpPeerCapsTable")

        self.cbgppeeraddrfamilytable = CISCOBGP4MIB.Cbgppeeraddrfamilytable()
        self.cbgppeeraddrfamilytable.parent = self
        self._children_name_map["cbgppeeraddrfamilytable"] = "cbgpPeerAddrFamilyTable"
        self._children_yang_names.add("cbgpPeerAddrFamilyTable")

        self.cbgppeeraddrfamilyprefixtable = CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable()
        self.cbgppeeraddrfamilyprefixtable.parent = self
        self._children_name_map["cbgppeeraddrfamilyprefixtable"] = "cbgpPeerAddrFamilyPrefixTable"
        self._children_yang_names.add("cbgpPeerAddrFamilyPrefixTable")

        self.cbgppeer2table = CISCOBGP4MIB.Cbgppeer2Table()
        self.cbgppeer2table.parent = self
        self._children_name_map["cbgppeer2table"] = "cbgpPeer2Table"
        self._children_yang_names.add("cbgpPeer2Table")

        self.cbgppeer2capstable = CISCOBGP4MIB.Cbgppeer2Capstable()
        self.cbgppeer2capstable.parent = self
        self._children_name_map["cbgppeer2capstable"] = "cbgpPeer2CapsTable"
        self._children_yang_names.add("cbgpPeer2CapsTable")

        self.cbgppeer2addrfamilytable = CISCOBGP4MIB.Cbgppeer2Addrfamilytable()
        self.cbgppeer2addrfamilytable.parent = self
        self._children_name_map["cbgppeer2addrfamilytable"] = "cbgpPeer2AddrFamilyTable"
        self._children_yang_names.add("cbgpPeer2AddrFamilyTable")

        self.cbgppeer2addrfamilyprefixtable = CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable()
        self.cbgppeer2addrfamilyprefixtable.parent = self
        self._children_name_map["cbgppeer2addrfamilyprefixtable"] = "cbgpPeer2AddrFamilyPrefixTable"
        self._children_yang_names.add("cbgpPeer2AddrFamilyPrefixTable")
        self._segment_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB"


    class Cbgpglobal(Entity):
        """
        
        
        .. attribute:: cbgpnotifsenable
        
        	Indicates whether the specific notifications are enabled.  If notifsEnable(0) bit is set to 1, then the notifications defined in ciscoBgp4NotificationsGroup1 are enabled;  If notifsPeer2Enable(1) bit is set to 1, then the notifications defined in ciscoBgp4Peer2NotificationsGroup are enabled
        	**type**\:  :py:class:`Cbgpnotifsenable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgpglobal.Cbgpnotifsenable>`
        
        .. attribute:: cbgplocalas
        
        	The local autonomous system (AS) number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgpglobal, self).__init__()

            self.yang_name = "cbgpGlobal"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cbgpnotifsenable', YLeaf(YType.bits, 'cbgpNotifsEnable')),
                ('cbgplocalas', YLeaf(YType.uint32, 'cbgpLocalAs')),
            ])
            self.cbgpnotifsenable = Bits()
            self.cbgplocalas = None
            self._segment_path = lambda: "cbgpGlobal"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgpglobal, ['cbgpnotifsenable', 'cbgplocalas'], name, value)


    class Cbgproutetable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgprouteentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgproutetable.Cbgprouteentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgproutetable, self).__init__()

            self.yang_name = "cbgpRouteTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpRouteEntry", ("cbgprouteentry", CISCOBGP4MIB.Cbgproutetable.Cbgprouteentry))])
            self._leafs = OrderedDict()

            self.cbgprouteentry = YList(self)
            self._segment_path = lambda: "cbgpRouteTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgproutetable, [], name, value)


        class Cbgprouteentry(Entity):
            """
            Information about a path to a network received from
            a peer.
            
            .. attribute:: cbgprouteafi  (key)
            
            	Represents Address Family Identifier(AFI) of the Network Layer protocol associated with the route. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgproutesafi  (key)
            
            	Represents Subsequent Address Family Identifier(SAFI) of the route. It gives additional information about the type of the route. An implementation is only  required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            .. attribute:: cbgproutepeertype  (key)
            
            	Represents the type of Network Layer address stored in cbgpRoutePeer. An implementation is only required to support IPv4 address type(Value \- 1)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgproutepeer  (key)
            
            	The Network Layer address of the peer where the route information was learned. An implementation is only  required to support an IPv4 peer
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteaddrprefix  (key)
            
            	A Network Address prefix in the Network Layer Reachability Information field of BGP UPDATE message. This object is a Network Address containing the prefix with length specified by cbgpRouteAddrPrefixLen. Any bits beyond the length specified by cbgpRouteAddrPrefixLen are zeroed
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteaddrprefixlen  (key)
            
            	Length in bits of the Network Address prefix in the Network Layer Reachability Information field
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cbgprouteorigin
            
            	The ultimate origin of the route information
            	**type**\:  :py:class:`Cbgprouteorigin <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgproutetable.Cbgprouteentry.Cbgprouteorigin>`
            
            .. attribute:: cbgprouteaspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.  The type is a 1\-octet field which has two possible values\: 1  AS\_SET\: unordered set of ASs a route in the            UPDATE message has traversed 2  AS\_SEQUENCE\: ordered set of ASs a route in the                UPDATE message has traversed.  The length is a 1\-octet field containing the number of ASs in the value field.  The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm\:  first\-byte\-of\-pair = ASNumber / 256; second\-byte\-of\-pair = ASNumber & 255;
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgproutenexthop
            
            	The Network Layer address of the border router that should be used for the destination network
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgproutemedpresent
            
            	Indicates the presence/absence of MULTI\_EXIT\_DISC attribute for the route
            	**type**\: bool
            
            .. attribute:: cbgproutemultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  The value of this object is irrelevant if the value of of cbgpRouteMedPresent is false(2)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgproutelocalprefpresent
            
            	Indicates the presence/absence of LOCAL\_PREF attribute for the route
            	**type**\: bool
            
            .. attribute:: cbgproutelocalpref
            
            	The degree of preference calculated by the local BGP4 speaker for the route. The value of this object is  irrelevant if the value of cbgpRouteLocalPrefPresent  is false(2)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgprouteatomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:  :py:class:`Cbgprouteatomicaggregate <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgproutetable.Cbgprouteentry.Cbgprouteatomicaggregate>`
            
            .. attribute:: cbgprouteaggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the  absence of this attribute
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbgprouteaggregatoraddrtype
            
            	Represents the type of Network Layer address stored in cbgpRouteAggregatorAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgprouteaggregatoraddr
            
            	The Network Layer address of the last BGP4 speaker that performed route aggregation.  A value of all zeros indicates the absence of this attribute
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgproutebest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\: bool
            
            .. attribute:: cbgprouteunknownattr
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object.    Each path attribute is a triple <attribute type, attribute length, attribute value> of variable length. Attribute Type is a two\-octet field that consists of the Attribute Flags octet followed by the Attribute Type Code octet.  If the Extended Length bit of the  Attribute Flags octet is set to 0, the third octet of  the Path Attribute contains the length of the attribute data in octets.  If the Extended Length bit  of the Attribute Flags octet is set to 1, then the third and the fourth octets of the path attribute  contain the length of the attribute data in octets. The remaining octets of the Path Attribute represent  the attribute value and are interpreted according to  the Attribute Flags and the Attribute Type Code
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgproutetable.Cbgprouteentry, self).__init__()

                self.yang_name = "cbgpRouteEntry"
                self.yang_parent_name = "cbgpRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgprouteafi','cbgproutesafi','cbgproutepeertype','cbgproutepeer','cbgprouteaddrprefix','cbgprouteaddrprefixlen']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgprouteafi', YLeaf(YType.enumeration, 'cbgpRouteAfi')),
                    ('cbgproutesafi', YLeaf(YType.enumeration, 'cbgpRouteSafi')),
                    ('cbgproutepeertype', YLeaf(YType.enumeration, 'cbgpRoutePeerType')),
                    ('cbgproutepeer', YLeaf(YType.str, 'cbgpRoutePeer')),
                    ('cbgprouteaddrprefix', YLeaf(YType.str, 'cbgpRouteAddrPrefix')),
                    ('cbgprouteaddrprefixlen', YLeaf(YType.uint32, 'cbgpRouteAddrPrefixLen')),
                    ('cbgprouteorigin', YLeaf(YType.enumeration, 'cbgpRouteOrigin')),
                    ('cbgprouteaspathsegment', YLeaf(YType.str, 'cbgpRouteASPathSegment')),
                    ('cbgproutenexthop', YLeaf(YType.str, 'cbgpRouteNextHop')),
                    ('cbgproutemedpresent', YLeaf(YType.boolean, 'cbgpRouteMedPresent')),
                    ('cbgproutemultiexitdisc', YLeaf(YType.uint32, 'cbgpRouteMultiExitDisc')),
                    ('cbgproutelocalprefpresent', YLeaf(YType.boolean, 'cbgpRouteLocalPrefPresent')),
                    ('cbgproutelocalpref', YLeaf(YType.uint32, 'cbgpRouteLocalPref')),
                    ('cbgprouteatomicaggregate', YLeaf(YType.enumeration, 'cbgpRouteAtomicAggregate')),
                    ('cbgprouteaggregatoras', YLeaf(YType.uint32, 'cbgpRouteAggregatorAS')),
                    ('cbgprouteaggregatoraddrtype', YLeaf(YType.enumeration, 'cbgpRouteAggregatorAddrType')),
                    ('cbgprouteaggregatoraddr', YLeaf(YType.str, 'cbgpRouteAggregatorAddr')),
                    ('cbgproutebest', YLeaf(YType.boolean, 'cbgpRouteBest')),
                    ('cbgprouteunknownattr', YLeaf(YType.str, 'cbgpRouteUnknownAttr')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgproutetable.Cbgprouteentry, ['cbgprouteafi', 'cbgproutesafi', 'cbgproutepeertype', 'cbgproutepeer', 'cbgprouteaddrprefix', 'cbgprouteaddrprefixlen', 'cbgprouteorigin', 'cbgprouteaspathsegment', 'cbgproutenexthop', 'cbgproutemedpresent', 'cbgproutemultiexitdisc', 'cbgproutelocalprefpresent', 'cbgproutelocalpref', 'cbgprouteatomicaggregate', 'cbgprouteaggregatoras', 'cbgprouteaggregatoraddrtype', 'cbgprouteaggregatoraddr', 'cbgproutebest', 'cbgprouteunknownattr'], name, value)

            class Cbgprouteatomicaggregate(Enum):
                """
                Cbgprouteatomicaggregate (Enum Class)

                Whether or not the local system has selected a less

                specific route without selecting a more specific

                route.

                .. data:: lessSpecificRouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRouteNotSelected = Enum.YLeaf(1, "lessSpecificRouteNotSelected")

                lessSpecificRouteSelected = Enum.YLeaf(2, "lessSpecificRouteSelected")


            class Cbgprouteorigin(Enum):
                """
                Cbgprouteorigin (Enum Class)

                The ultimate origin of the route information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")



    class Cbgppeercapstable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgppeercapsentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeercapstable.Cbgppeercapsentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeercapstable, self).__init__()

            self.yang_name = "cbgpPeerCapsTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeerCapsEntry", ("cbgppeercapsentry", CISCOBGP4MIB.Cbgppeercapstable.Cbgppeercapsentry))])
            self._leafs = OrderedDict()

            self.cbgppeercapsentry = YList(self)
            self._segment_path = lambda: "cbgpPeerCapsTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeercapstable, [], name, value)


        class Cbgppeercapsentry(Entity):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a 
            capability is received multiple times with different
            values during a BGP connection establishment, 
            corresponding entries are differentiated with indices.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeercapcode  (key)
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:  :py:class:`Cbgppeercapcode <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeercapstable.Cbgppeercapsentry.Cbgppeercapcode>`
            
            .. attribute:: cbgppeercapindex  (key)
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: cbgppeercapvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeercapstable.Cbgppeercapsentry, self).__init__()

                self.yang_name = "cbgpPeerCapsEntry"
                self.yang_parent_name = "cbgpPeerCapsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr','cbgppeercapcode','cbgppeercapindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', YLeaf(YType.str, 'bgpPeerRemoteAddr')),
                    ('cbgppeercapcode', YLeaf(YType.enumeration, 'cbgpPeerCapCode')),
                    ('cbgppeercapindex', YLeaf(YType.uint32, 'cbgpPeerCapIndex')),
                    ('cbgppeercapvalue', YLeaf(YType.str, 'cbgpPeerCapValue')),
                ])
                self.bgppeerremoteaddr = None
                self.cbgppeercapcode = None
                self.cbgppeercapindex = None
                self.cbgppeercapvalue = None
                self._segment_path = lambda: "cbgpPeerCapsEntry" + "[bgpPeerRemoteAddr='" + str(self.bgppeerremoteaddr) + "']" + "[cbgpPeerCapCode='" + str(self.cbgppeercapcode) + "']" + "[cbgpPeerCapIndex='" + str(self.cbgppeercapindex) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerCapsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeercapstable.Cbgppeercapsentry, ['bgppeerremoteaddr', 'cbgppeercapcode', 'cbgppeercapindex', 'cbgppeercapvalue'], name, value)

            class Cbgppeercapcode(Enum):
                """
                Cbgppeercapcode (Enum Class)

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



    class Cbgppeeraddrfamilytable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgppeeraddrfamilyentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeeraddrfamilytable, self).__init__()

            self.yang_name = "cbgpPeerAddrFamilyTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeerAddrFamilyEntry", ("cbgppeeraddrfamilyentry", CISCOBGP4MIB.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry))])
            self._leafs = OrderedDict()

            self.cbgppeeraddrfamilyentry = YList(self)
            self._segment_path = lambda: "cbgpPeerAddrFamilyTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeeraddrfamilytable, [], name, value)


        class Cbgppeeraddrfamilyentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeeraddrfamilyafi  (key)
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and  VPNv4 (Value \- 1) address families
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeeraddrfamilysafi  (key)
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value  \- 1) and VPNv4( Value \- 128) address families
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            .. attribute:: cbgppeeraddrfamilyname
            
            	Implementation specific Address Family name
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry, self).__init__()

                self.yang_name = "cbgpPeerAddrFamilyEntry"
                self.yang_parent_name = "cbgpPeerAddrFamilyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr','cbgppeeraddrfamilyafi','cbgppeeraddrfamilysafi']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', YLeaf(YType.str, 'bgpPeerRemoteAddr')),
                    ('cbgppeeraddrfamilyafi', YLeaf(YType.enumeration, 'cbgpPeerAddrFamilyAfi')),
                    ('cbgppeeraddrfamilysafi', YLeaf(YType.enumeration, 'cbgpPeerAddrFamilySafi')),
                    ('cbgppeeraddrfamilyname', YLeaf(YType.str, 'cbgpPeerAddrFamilyName')),
                ])
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeraddrfamilyname = None
                self._segment_path = lambda: "cbgpPeerAddrFamilyEntry" + "[bgpPeerRemoteAddr='" + str(self.bgppeerremoteaddr) + "']" + "[cbgpPeerAddrFamilyAfi='" + str(self.cbgppeeraddrfamilyafi) + "']" + "[cbgpPeerAddrFamilySafi='" + str(self.cbgppeeraddrfamilysafi) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerAddrFamilyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry, ['bgppeerremoteaddr', 'cbgppeeraddrfamilyafi', 'cbgppeeraddrfamilysafi', 'cbgppeeraddrfamilyname'], name, value)


    class Cbgppeeraddrfamilyprefixtable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgppeeraddrfamilyprefixentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable, self).__init__()

            self.yang_name = "cbgpPeerAddrFamilyPrefixTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeerAddrFamilyPrefixEntry", ("cbgppeeraddrfamilyprefixentry", CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry))])
            self._leafs = OrderedDict()

            self.cbgppeeraddrfamilyprefixentry = YList(self)
            self._segment_path = lambda: "cbgpPeerAddrFamilyPrefixTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable, [], name, value)


        class Cbgppeeraddrfamilyprefixentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated 
            with route prefixes belonging to an address family.
            
            .. attribute:: bgppeerremoteaddr  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.BGP4MIB.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeeraddrfamilyafi  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeeraddrfamilysafi  (key)
            
            	
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            .. attribute:: cbgppeeracceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerdeniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this  connection is denied. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerprefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbgppeerprefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or  corresponding SNMP notification is generated
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeerprefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeeradvertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeersuppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is  initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerwithdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry, self).__init__()

                self.yang_name = "cbgpPeerAddrFamilyPrefixEntry"
                self.yang_parent_name = "cbgpPeerAddrFamilyPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bgppeerremoteaddr','cbgppeeraddrfamilyafi','cbgppeeraddrfamilysafi']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bgppeerremoteaddr', YLeaf(YType.str, 'bgpPeerRemoteAddr')),
                    ('cbgppeeraddrfamilyafi', YLeaf(YType.enumeration, 'cbgpPeerAddrFamilyAfi')),
                    ('cbgppeeraddrfamilysafi', YLeaf(YType.enumeration, 'cbgpPeerAddrFamilySafi')),
                    ('cbgppeeracceptedprefixes', YLeaf(YType.uint32, 'cbgpPeerAcceptedPrefixes')),
                    ('cbgppeerdeniedprefixes', YLeaf(YType.uint32, 'cbgpPeerDeniedPrefixes')),
                    ('cbgppeerprefixadminlimit', YLeaf(YType.uint32, 'cbgpPeerPrefixAdminLimit')),
                    ('cbgppeerprefixthreshold', YLeaf(YType.uint32, 'cbgpPeerPrefixThreshold')),
                    ('cbgppeerprefixclearthreshold', YLeaf(YType.uint32, 'cbgpPeerPrefixClearThreshold')),
                    ('cbgppeeradvertisedprefixes', YLeaf(YType.uint32, 'cbgpPeerAdvertisedPrefixes')),
                    ('cbgppeersuppressedprefixes', YLeaf(YType.uint32, 'cbgpPeerSuppressedPrefixes')),
                    ('cbgppeerwithdrawnprefixes', YLeaf(YType.uint32, 'cbgpPeerWithdrawnPrefixes')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry, ['bgppeerremoteaddr', 'cbgppeeraddrfamilyafi', 'cbgppeeraddrfamilysafi', 'cbgppeeracceptedprefixes', 'cbgppeerdeniedprefixes', 'cbgppeerprefixadminlimit', 'cbgppeerprefixthreshold', 'cbgppeerprefixclearthreshold', 'cbgppeeradvertisedprefixes', 'cbgppeersuppressedprefixes', 'cbgppeerwithdrawnprefixes'], name, value)


    class Cbgppeer2Table(Entity):
        """
        BGP peer table.  This table contains,
        one entry per BGP peer, information about
        the connections with BGP peers.
        
        .. attribute:: cbgppeer2entry
        
        	Entry containing information about the connection with a BGP peer
        	**type**\: list of  		 :py:class:`Cbgppeer2Entry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeer2Table, self).__init__()

            self.yang_name = "cbgpPeer2Table"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeer2Entry", ("cbgppeer2entry", CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry))])
            self._leafs = OrderedDict()

            self.cbgppeer2entry = YList(self)
            self._segment_path = lambda: "cbgpPeer2Table"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Table, [], name, value)


        class Cbgppeer2Entry(Entity):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: cbgppeer2type  (key)
            
            	Represents the type of Peer address stored in cbgpPeer2Entry
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	The remote IP address of this entry's BGP peer
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgppeer2state
            
            	The BGP peer connection state
            	**type**\:  :py:class:`Cbgppeer2State <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2State>`
            
            .. attribute:: cbgppeer2adminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Manual Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Manual Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:  :py:class:`Cbgppeer2Adminstatus <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2Adminstatus>`
            
            .. attribute:: cbgppeer2negotiatedversion
            
            	The negotiated version of BGP running between the two peers.  This entry MUST be zero (0) unless the cbgpPeer2State is in the openconfirm or the established state.  Note that legal values for this object are between 0 and 255
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cbgppeer2localaddr
            
            	The local IP address of this entry's BGP connection
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cbgppeer2localport
            
            	The local port for the TCP connection between the BGP peers
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbgppeer2localas
            
            	The local AS number for this session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2localidentifier
            
            	The BGP Identifier of this entry's BGP peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeer2remoteport
            
            	The remote port for the TCP connection between the BGP peers.  Note that the objects cbgpPeer2LocalAddr, cbgpPeer2LocalPort, cbgpPeer2RemoteAddr, and cbgpPeer2RemotePort provide the appropriate reference to the standard MIB TCP connection table
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cbgppeer2remoteas
            
            	The remote autonomous system number received in the BGP OPEN message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2remoteidentifier
            
            	The BGP Identifier of this entry's BGP peer. This entry MUST be 0.0.0.0 unless the cbgpPeer2State is in the openconfirm or the established state
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeer2inupdates
            
            	The number of BGP UPDATE messages received on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2outupdates
            
            	The number of BGP UPDATE messages transmitted on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2intotalmessages
            
            	The total number of messages received from the remote peer on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2outtotalmessages
            
            	The total number of messages transmitted to the remote peer on this connection
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2lasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\: str
            
            	**length:** 2
            
            .. attribute:: cbgppeer2fsmestablishedtransitions
            
            	The total number of times the BGP FSM transitioned into the established state for this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2fsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the established state or how long since this peer was last in the established state.  It is set to zero when a new peer is configured or when the router is booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2connectretryinterval
            
            	Time interval (in seconds) for the ConnectRetry timer.  The suggested value for this timer is 120 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2holdtime
            
            	Time interval (in seconds) for the Hold Timer established with the peer.  The value of this object is calculated by this BGP speaker, using the smaller of the values in cbgpPeer2HoldTimeConfigured and the Hold Time received in the OPEN message.  This value must be at least three seconds if it is not zero (0).  If the Hold Timer has not been established with the peer this object MUST have a value of zero (0).  If the cbgpPeer2HoldTimeConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\: int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2keepalive
            
            	Time interval (in seconds) for the KeepAlive timer established with the peer.  The value of this object is calculated by this BGP speaker such that, when compared with cbgpPeer2HoldTime, it has the same proportion that cbgpPeer2KeepAliveConfigured has, compared with cbgpPeer2HoldTimeConfigured.  If the KeepAlive timer has not been established with the peer, this object MUST have a value of zero (0).  If the of cbgpPeer2KeepAliveConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\: int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2holdtimeconfigured
            
            	Time interval (in seconds) for the Hold Time configured for this BGP speaker with this peer.  This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (cbgpPeer2HoldTime) with the peer. This value must not be less than three seconds if it is not zero (0).  If it is zero (0), the Hold Time is NOT to be established with the peer.  The suggested value for this timer is 90 seconds
            	**type**\: int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2keepaliveconfigured
            
            	Time interval (in seconds) for the KeepAlive timer configured for this BGP speaker with this peer.  The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in cbgpPeer2HoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by cbgpPeer2KeepAlive.  A reasonable maximum value for this timer would be one third of that of cbgpPeer2HoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established.  The suggested value for this timer is 30 seconds
            	**type**\: int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2minasoriginationinterval
            
            	Time interval (in seconds) for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2minrouteadvertisementinterval
            
            	Time interval (in seconds) for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds for EBGP connections and 5 seconds for IBGP connections
            	**type**\: int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2inupdateelapsedtime
            
            	Elapsed time (in seconds) since the last BGP UPDATE message was received from the peer. Each time cbgpPeer2InUpdates is incremented, the value of this object is set to zero (0)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2lasterrortxt
            
            	Implementation specific error description for bgpPeerLastErrorReceived
            	**type**\: str
            
            .. attribute:: cbgppeer2prevstate
            
            	The BGP peer connection previous state
            	**type**\:  :py:class:`Cbgppeer2Prevstate <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2Prevstate>`
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry, self).__init__()

                self.yang_name = "cbgpPeer2Entry"
                self.yang_parent_name = "cbgpPeer2Table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', YLeaf(YType.enumeration, 'cbgpPeer2Type')),
                    ('cbgppeer2remoteaddr', YLeaf(YType.str, 'cbgpPeer2RemoteAddr')),
                    ('cbgppeer2state', YLeaf(YType.enumeration, 'cbgpPeer2State')),
                    ('cbgppeer2adminstatus', YLeaf(YType.enumeration, 'cbgpPeer2AdminStatus')),
                    ('cbgppeer2negotiatedversion', YLeaf(YType.int32, 'cbgpPeer2NegotiatedVersion')),
                    ('cbgppeer2localaddr', YLeaf(YType.str, 'cbgpPeer2LocalAddr')),
                    ('cbgppeer2localport', YLeaf(YType.uint16, 'cbgpPeer2LocalPort')),
                    ('cbgppeer2localas', YLeaf(YType.uint32, 'cbgpPeer2LocalAs')),
                    ('cbgppeer2localidentifier', YLeaf(YType.str, 'cbgpPeer2LocalIdentifier')),
                    ('cbgppeer2remoteport', YLeaf(YType.uint16, 'cbgpPeer2RemotePort')),
                    ('cbgppeer2remoteas', YLeaf(YType.uint32, 'cbgpPeer2RemoteAs')),
                    ('cbgppeer2remoteidentifier', YLeaf(YType.str, 'cbgpPeer2RemoteIdentifier')),
                    ('cbgppeer2inupdates', YLeaf(YType.uint32, 'cbgpPeer2InUpdates')),
                    ('cbgppeer2outupdates', YLeaf(YType.uint32, 'cbgpPeer2OutUpdates')),
                    ('cbgppeer2intotalmessages', YLeaf(YType.uint32, 'cbgpPeer2InTotalMessages')),
                    ('cbgppeer2outtotalmessages', YLeaf(YType.uint32, 'cbgpPeer2OutTotalMessages')),
                    ('cbgppeer2lasterror', YLeaf(YType.str, 'cbgpPeer2LastError')),
                    ('cbgppeer2fsmestablishedtransitions', YLeaf(YType.uint32, 'cbgpPeer2FsmEstablishedTransitions')),
                    ('cbgppeer2fsmestablishedtime', YLeaf(YType.uint32, 'cbgpPeer2FsmEstablishedTime')),
                    ('cbgppeer2connectretryinterval', YLeaf(YType.int32, 'cbgpPeer2ConnectRetryInterval')),
                    ('cbgppeer2holdtime', YLeaf(YType.int32, 'cbgpPeer2HoldTime')),
                    ('cbgppeer2keepalive', YLeaf(YType.int32, 'cbgpPeer2KeepAlive')),
                    ('cbgppeer2holdtimeconfigured', YLeaf(YType.int32, 'cbgpPeer2HoldTimeConfigured')),
                    ('cbgppeer2keepaliveconfigured', YLeaf(YType.int32, 'cbgpPeer2KeepAliveConfigured')),
                    ('cbgppeer2minasoriginationinterval', YLeaf(YType.int32, 'cbgpPeer2MinASOriginationInterval')),
                    ('cbgppeer2minrouteadvertisementinterval', YLeaf(YType.int32, 'cbgpPeer2MinRouteAdvertisementInterval')),
                    ('cbgppeer2inupdateelapsedtime', YLeaf(YType.uint32, 'cbgpPeer2InUpdateElapsedTime')),
                    ('cbgppeer2lasterrortxt', YLeaf(YType.str, 'cbgpPeer2LastErrorTxt')),
                    ('cbgppeer2prevstate', YLeaf(YType.enumeration, 'cbgpPeer2PrevState')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2state', 'cbgppeer2adminstatus', 'cbgppeer2negotiatedversion', 'cbgppeer2localaddr', 'cbgppeer2localport', 'cbgppeer2localas', 'cbgppeer2localidentifier', 'cbgppeer2remoteport', 'cbgppeer2remoteas', 'cbgppeer2remoteidentifier', 'cbgppeer2inupdates', 'cbgppeer2outupdates', 'cbgppeer2intotalmessages', 'cbgppeer2outtotalmessages', 'cbgppeer2lasterror', 'cbgppeer2fsmestablishedtransitions', 'cbgppeer2fsmestablishedtime', 'cbgppeer2connectretryinterval', 'cbgppeer2holdtime', 'cbgppeer2keepalive', 'cbgppeer2holdtimeconfigured', 'cbgppeer2keepaliveconfigured', 'cbgppeer2minasoriginationinterval', 'cbgppeer2minrouteadvertisementinterval', 'cbgppeer2inupdateelapsedtime', 'cbgppeer2lasterrortxt', 'cbgppeer2prevstate'], name, value)

            class Cbgppeer2Adminstatus(Enum):
                """
                Cbgppeer2Adminstatus (Enum Class)

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


            class Cbgppeer2Prevstate(Enum):
                """
                Cbgppeer2Prevstate (Enum Class)

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


            class Cbgppeer2State(Enum):
                """
                Cbgppeer2State (Enum Class)

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



    class Cbgppeer2Capstable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgppeer2Capsentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Capstable.Cbgppeer2Capsentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeer2Capstable, self).__init__()

            self.yang_name = "cbgpPeer2CapsTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeer2CapsEntry", ("cbgppeer2capsentry", CISCOBGP4MIB.Cbgppeer2Capstable.Cbgppeer2Capsentry))])
            self._leafs = OrderedDict()

            self.cbgppeer2capsentry = YList(self)
            self._segment_path = lambda: "cbgpPeer2CapsTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Capstable, [], name, value)


        class Cbgppeer2Capsentry(Entity):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a
            capability is received multiple times with different
            values during a BGP connection establishment,
            corresponding entries are differentiated with indices.
            
            .. attribute:: cbgppeer2type  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2capcode  (key)
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:  :py:class:`Cbgppeer2Capcode <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Capstable.Cbgppeer2Capsentry.Cbgppeer2Capcode>`
            
            .. attribute:: cbgppeer2capindex  (key)
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: cbgppeer2capvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  4\-Byte AS Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Additional Paths       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Send/Receive (8 bits)            \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeer2Capstable.Cbgppeer2Capsentry, self).__init__()

                self.yang_name = "cbgpPeer2CapsEntry"
                self.yang_parent_name = "cbgpPeer2CapsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr','cbgppeer2capcode','cbgppeer2capindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', YLeaf(YType.enumeration, 'cbgpPeer2Type')),
                    ('cbgppeer2remoteaddr', YLeaf(YType.str, 'cbgpPeer2RemoteAddr')),
                    ('cbgppeer2capcode', YLeaf(YType.enumeration, 'cbgpPeer2CapCode')),
                    ('cbgppeer2capindex', YLeaf(YType.uint32, 'cbgpPeer2CapIndex')),
                    ('cbgppeer2capvalue', YLeaf(YType.str, 'cbgpPeer2CapValue')),
                ])
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2capcode = None
                self.cbgppeer2capindex = None
                self.cbgppeer2capvalue = None
                self._segment_path = lambda: "cbgpPeer2CapsEntry" + "[cbgpPeer2Type='" + str(self.cbgppeer2type) + "']" + "[cbgpPeer2RemoteAddr='" + str(self.cbgppeer2remoteaddr) + "']" + "[cbgpPeer2CapCode='" + str(self.cbgppeer2capcode) + "']" + "[cbgpPeer2CapIndex='" + str(self.cbgppeer2capindex) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2CapsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Capstable.Cbgppeer2Capsentry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2capcode', 'cbgppeer2capindex', 'cbgppeer2capvalue'], name, value)

            class Cbgppeer2Capcode(Enum):
                """
                Cbgppeer2Capcode (Enum Class)

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



    class Cbgppeer2Addrfamilytable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgppeer2Addrfamilyentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeer2Addrfamilytable, self).__init__()

            self.yang_name = "cbgpPeer2AddrFamilyTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeer2AddrFamilyEntry", ("cbgppeer2addrfamilyentry", CISCOBGP4MIB.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry))])
            self._leafs = OrderedDict()

            self.cbgppeer2addrfamilyentry = YList(self)
            self._segment_path = lambda: "cbgpPeer2AddrFamilyTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Addrfamilytable, [], name, value)


        class Cbgppeer2Addrfamilyentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: cbgppeer2type  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2addrfamilyafi  (key)
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeer2addrfamilysafi  (key)
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            .. attribute:: cbgppeer2addrfamilyname
            
            	Implementation specific Address Family name
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry, self).__init__()

                self.yang_name = "cbgpPeer2AddrFamilyEntry"
                self.yang_parent_name = "cbgpPeer2AddrFamilyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr','cbgppeer2addrfamilyafi','cbgppeer2addrfamilysafi']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', YLeaf(YType.enumeration, 'cbgpPeer2Type')),
                    ('cbgppeer2remoteaddr', YLeaf(YType.str, 'cbgpPeer2RemoteAddr')),
                    ('cbgppeer2addrfamilyafi', YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilyAfi')),
                    ('cbgppeer2addrfamilysafi', YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilySafi')),
                    ('cbgppeer2addrfamilyname', YLeaf(YType.str, 'cbgpPeer2AddrFamilyName')),
                ])
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2addrfamilyname = None
                self._segment_path = lambda: "cbgpPeer2AddrFamilyEntry" + "[cbgpPeer2Type='" + str(self.cbgppeer2type) + "']" + "[cbgpPeer2RemoteAddr='" + str(self.cbgppeer2remoteaddr) + "']" + "[cbgpPeer2AddrFamilyAfi='" + str(self.cbgppeer2addrfamilyafi) + "']" + "[cbgpPeer2AddrFamilySafi='" + str(self.cbgppeer2addrfamilysafi) + "']"
                self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2AddrFamilyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2addrfamilyafi', 'cbgppeer2addrfamilysafi', 'cbgppeer2addrfamilyname'], name, value)


    class Cbgppeer2Addrfamilyprefixtable(Entity):
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
        	**type**\: list of  		 :py:class:`Cbgppeer2Addrfamilyprefixentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable, self).__init__()

            self.yang_name = "cbgpPeer2AddrFamilyPrefixTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cbgpPeer2AddrFamilyPrefixEntry", ("cbgppeer2addrfamilyprefixentry", CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry))])
            self._leafs = OrderedDict()

            self.cbgppeer2addrfamilyprefixentry = YList(self)
            self._segment_path = lambda: "cbgpPeer2AddrFamilyPrefixTable"
            self._absolute_path = lambda: "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable, [], name, value)


        class Cbgppeer2Addrfamilyprefixentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated
            with route prefixes belonging to an address family.
            
            .. attribute:: cbgppeer2type  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeer2remoteaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CISCOBGP4MIB.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2addrfamilyafi  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cbgppeer2addrfamilysafi  (key)
            
            	
            	**type**\:  :py:class:`CbgpSafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpSafi>`
            
            .. attribute:: cbgppeer2acceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2deniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this connection is denied. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2prefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbgppeer2prefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or corresponding SNMP notification is generated
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: percent
            
            .. attribute:: cbgppeer2prefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\: int
            
            	**range:** 1..100
            
            	**units**\: percent
            
            .. attribute:: cbgppeer2advertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2suppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2withdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry, self).__init__()

                self.yang_name = "cbgpPeer2AddrFamilyPrefixEntry"
                self.yang_parent_name = "cbgpPeer2AddrFamilyPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cbgppeer2type','cbgppeer2remoteaddr','cbgppeer2addrfamilyafi','cbgppeer2addrfamilysafi']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cbgppeer2type', YLeaf(YType.enumeration, 'cbgpPeer2Type')),
                    ('cbgppeer2remoteaddr', YLeaf(YType.str, 'cbgpPeer2RemoteAddr')),
                    ('cbgppeer2addrfamilyafi', YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilyAfi')),
                    ('cbgppeer2addrfamilysafi', YLeaf(YType.enumeration, 'cbgpPeer2AddrFamilySafi')),
                    ('cbgppeer2acceptedprefixes', YLeaf(YType.uint32, 'cbgpPeer2AcceptedPrefixes')),
                    ('cbgppeer2deniedprefixes', YLeaf(YType.uint32, 'cbgpPeer2DeniedPrefixes')),
                    ('cbgppeer2prefixadminlimit', YLeaf(YType.uint32, 'cbgpPeer2PrefixAdminLimit')),
                    ('cbgppeer2prefixthreshold', YLeaf(YType.uint32, 'cbgpPeer2PrefixThreshold')),
                    ('cbgppeer2prefixclearthreshold', YLeaf(YType.uint32, 'cbgpPeer2PrefixClearThreshold')),
                    ('cbgppeer2advertisedprefixes', YLeaf(YType.uint32, 'cbgpPeer2AdvertisedPrefixes')),
                    ('cbgppeer2suppressedprefixes', YLeaf(YType.uint32, 'cbgpPeer2SuppressedPrefixes')),
                    ('cbgppeer2withdrawnprefixes', YLeaf(YType.uint32, 'cbgpPeer2WithdrawnPrefixes')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOBGP4MIB.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry, ['cbgppeer2type', 'cbgppeer2remoteaddr', 'cbgppeer2addrfamilyafi', 'cbgppeer2addrfamilysafi', 'cbgppeer2acceptedprefixes', 'cbgppeer2deniedprefixes', 'cbgppeer2prefixadminlimit', 'cbgppeer2prefixthreshold', 'cbgppeer2prefixclearthreshold', 'cbgppeer2advertisedprefixes', 'cbgppeer2suppressedprefixes', 'cbgppeer2withdrawnprefixes'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOBGP4MIB()
        return self._top_entity

