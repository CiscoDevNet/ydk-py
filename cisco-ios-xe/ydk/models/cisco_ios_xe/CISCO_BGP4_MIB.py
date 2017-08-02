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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cbgpsafi(Enum):
    """
    Cbgpsafi

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



class CiscoBgp4Mib(Entity):
    """
    
    
    .. attribute:: cbgpglobal
    
    	
    	**type**\:   :py:class:`Cbgpglobal <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgpglobal>`
    
    .. attribute:: cbgppeer2addrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\:   :py:class:`Cbgppeer2Addrfamilyprefixtable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable>`
    
    .. attribute:: cbgppeer2addrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP connection establishment. When a new supported address family is known, this table is updated with a new entry. When an address family is not supported any more, corresponding entry is deleted from the table
    	**type**\:   :py:class:`Cbgppeer2Addrfamilytable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Addrfamilytable>`
    
    .. attribute:: cbgppeer2capstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability is received, this table is updated with a new entry. When an existing capability is not received during the latest connection establishment, the corresponding entry is deleted from the table
    	**type**\:   :py:class:`Cbgppeer2Capstable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Capstable>`
    
    .. attribute:: cbgppeer2table
    
    	BGP peer table.  This table contains, one entry per BGP peer, information about the connections with BGP peers
    	**type**\:   :py:class:`Cbgppeer2Table <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table>`
    
    .. attribute:: cbgppeeraddrfamilyprefixtable
    
    	This table contains prefix related information related to address families supported by a peer.  Supported address families of a peer are known  during BGP connection establishment. When a new  supported address family is known, this table  is updated with a new entry. When an address  family is not supported any more, corresponding  entry is deleted from the table
    	**type**\:   :py:class:`Cbgppeeraddrfamilyprefixtable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable>`
    
    .. attribute:: cbgppeeraddrfamilytable
    
    	This table contains information related to address families supported by a peer. Supported address families of a peer are known during BGP  connection establishment. When a new supported  address family is known, this table is updated  with a new entry. When an address family is not  supported any more, corresponding entry is deleted  from the table
    	**type**\:   :py:class:`Cbgppeeraddrfamilytable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeeraddrfamilytable>`
    
    .. attribute:: cbgppeercapstable
    
    	This table contains the capabilities that are supported by a peer. Capabilities of a peer are  received during BGP connection establishment. Values corresponding to each received capability are stored in this table. When a new capability  is received, this table is updated with a new  entry. When an existing capability is not received  during the latest connection establishment, the  corresponding entry is deleted from the table
    	**type**\:   :py:class:`Cbgppeercapstable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeercapstable>`
    
    .. attribute:: cbgproutetable
    
    	This table contains information about routes to destination networks from all BGP4 peers.  Since  BGP4 can carry routes for multiple Network Layer  protocols, this table has the Address Family  Identifier(AFI) of the Network Layer protocol as the  first index. Further for a given AFI, routes carried by BGP4 are distinguished based on Subsequent Address  Family Identifiers(SAFI).  Hence that is used as the second index.  Conceptually there is a separate Loc\-RIB maintained by the BGP speaker for each combination of  AFI and SAFI supported by it
    	**type**\:   :py:class:`Cbgproutetable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgproutetable>`
    
    

    """

    _prefix = 'CISCO-BGP4-MIB'
    _revision = '2010-09-30'

    def __init__(self):
        super(CiscoBgp4Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-BGP4-MIB"
        self.yang_parent_name = "CISCO-BGP4-MIB"

        self.cbgpglobal = CiscoBgp4Mib.Cbgpglobal()
        self.cbgpglobal.parent = self
        self._children_name_map["cbgpglobal"] = "cbgpGlobal"
        self._children_yang_names.add("cbgpGlobal")

        self.cbgppeer2addrfamilyprefixtable = CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable()
        self.cbgppeer2addrfamilyprefixtable.parent = self
        self._children_name_map["cbgppeer2addrfamilyprefixtable"] = "cbgpPeer2AddrFamilyPrefixTable"
        self._children_yang_names.add("cbgpPeer2AddrFamilyPrefixTable")

        self.cbgppeer2addrfamilytable = CiscoBgp4Mib.Cbgppeer2Addrfamilytable()
        self.cbgppeer2addrfamilytable.parent = self
        self._children_name_map["cbgppeer2addrfamilytable"] = "cbgpPeer2AddrFamilyTable"
        self._children_yang_names.add("cbgpPeer2AddrFamilyTable")

        self.cbgppeer2capstable = CiscoBgp4Mib.Cbgppeer2Capstable()
        self.cbgppeer2capstable.parent = self
        self._children_name_map["cbgppeer2capstable"] = "cbgpPeer2CapsTable"
        self._children_yang_names.add("cbgpPeer2CapsTable")

        self.cbgppeer2table = CiscoBgp4Mib.Cbgppeer2Table()
        self.cbgppeer2table.parent = self
        self._children_name_map["cbgppeer2table"] = "cbgpPeer2Table"
        self._children_yang_names.add("cbgpPeer2Table")

        self.cbgppeeraddrfamilyprefixtable = CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable()
        self.cbgppeeraddrfamilyprefixtable.parent = self
        self._children_name_map["cbgppeeraddrfamilyprefixtable"] = "cbgpPeerAddrFamilyPrefixTable"
        self._children_yang_names.add("cbgpPeerAddrFamilyPrefixTable")

        self.cbgppeeraddrfamilytable = CiscoBgp4Mib.Cbgppeeraddrfamilytable()
        self.cbgppeeraddrfamilytable.parent = self
        self._children_name_map["cbgppeeraddrfamilytable"] = "cbgpPeerAddrFamilyTable"
        self._children_yang_names.add("cbgpPeerAddrFamilyTable")

        self.cbgppeercapstable = CiscoBgp4Mib.Cbgppeercapstable()
        self.cbgppeercapstable.parent = self
        self._children_name_map["cbgppeercapstable"] = "cbgpPeerCapsTable"
        self._children_yang_names.add("cbgpPeerCapsTable")

        self.cbgproutetable = CiscoBgp4Mib.Cbgproutetable()
        self.cbgproutetable.parent = self
        self._children_name_map["cbgproutetable"] = "cbgpRouteTable"
        self._children_yang_names.add("cbgpRouteTable")


    class Cbgpglobal(Entity):
        """
        
        
        .. attribute:: cbgplocalas
        
        	The local autonomous system (AS) number
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cbgpnotifsenable
        
        	Indicates whether the specific notifications are enabled.  If notifsEnable(0) bit is set to 1, then the notifications defined in ciscoBgp4NotificationsGroup1 are enabled;  If notifsPeer2Enable(1) bit is set to 1, then the notifications defined in ciscoBgp4Peer2NotificationsGroup are enabled
        	**type**\:   :py:class:`Cbgpnotifsenable <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgpglobal.Cbgpnotifsenable>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgpglobal, self).__init__()

            self.yang_name = "cbgpGlobal"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgplocalas = YLeaf(YType.uint32, "cbgpLocalAs")

            self.cbgpnotifsenable = YLeaf(YType.bits, "cbgpNotifsEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cbgplocalas",
                            "cbgpnotifsenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoBgp4Mib.Cbgpglobal, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgpglobal, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cbgplocalas.is_set or
                self.cbgpnotifsenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cbgplocalas.yfilter != YFilter.not_set or
                self.cbgpnotifsenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpGlobal" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cbgplocalas.is_set or self.cbgplocalas.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbgplocalas.get_name_leafdata())
            if (self.cbgpnotifsenable.is_set or self.cbgpnotifsenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cbgpnotifsenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpLocalAs" or name == "cbgpNotifsEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cbgpLocalAs"):
                self.cbgplocalas = value
                self.cbgplocalas.value_namespace = name_space
                self.cbgplocalas.value_namespace_prefix = name_space_prefix
            if(value_path == "cbgpNotifsEnable"):
                self.cbgpnotifsenable[value] = True


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
        	**type**\: list of    :py:class:`Cbgprouteentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgproutetable, self).__init__()

            self.yang_name = "cbgpRouteTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgprouteentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgproutetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgproutetable, self).__setattr__(name, value)


        class Cbgprouteentry(Entity):
            """
            Information about a path to a network received from
            a peer.
            
            .. attribute:: cbgprouteafi  <key>
            
            	Represents Address Family Identifier(AFI) of the Network Layer protocol associated with the route. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgproutesafi  <key>
            
            	Represents Subsequent Address Family Identifier(SAFI) of the route. It gives additional information about the type of the route. An implementation is only  required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:   :py:class:`Cbgpsafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.Cbgpsafi>`
            
            .. attribute:: cbgproutepeertype  <key>
            
            	Represents the type of Network Layer address stored in cbgpRoutePeer. An implementation is only required to support IPv4 address type(Value \- 1)
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgproutepeer  <key>
            
            	The Network Layer address of the peer where the route information was learned. An implementation is only  required to support an IPv4 peer
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteaddrprefix  <key>
            
            	A Network Address prefix in the Network Layer Reachability Information field of BGP UPDATE message. This object is a Network Address containing the prefix with length specified by cbgpRouteAddrPrefixLen. Any bits beyond the length specified by cbgpRouteAddrPrefixLen are zeroed
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteaddrprefixlen  <key>
            
            	Length in bits of the Network Address prefix in the Network Layer Reachability Information field
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: cbgprouteaggregatoraddr
            
            	The Network Layer address of the last BGP4 speaker that performed route aggregation.  A value of all zeros indicates the absence of this attribute
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteaggregatoraddrtype
            
            	Represents the type of Network Layer address stored in cbgpRouteAggregatorAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgprouteaggregatoras
            
            	The AS number of the last BGP4 speaker that performed route aggregation.  A value of zero (0) indicates the  absence of this attribute
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cbgprouteaspathsegment
            
            	The sequence of AS path segments.  Each AS path segment is represented by a triple <type, length, value>.  The type is a 1\-octet field which has two possible values\: 1  AS\_SET\: unordered set of ASs a route in the            UPDATE message has traversed 2  AS\_SEQUENCE\: ordered set of ASs a route in the                UPDATE message has traversed.  The length is a 1\-octet field containing the number of ASs in the value field.  The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm\:  first\-byte\-of\-pair = ASNumber / 256; second\-byte\-of\-pair = ASNumber & 255;
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteatomicaggregate
            
            	Whether or not the local system has selected a less specific route without selecting a more specific route
            	**type**\:   :py:class:`Cbgprouteatomicaggregate <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.Cbgprouteatomicaggregate>`
            
            .. attribute:: cbgproutebest
            
            	An indication of whether or not this route was chosen as the best BGP4 route
            	**type**\:  bool
            
            .. attribute:: cbgproutelocalpref
            
            	The degree of preference calculated by the local BGP4 speaker for the route. The value of this object is  irrelevant if the value of cbgpRouteLocalPrefPresent  is false(2)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgproutelocalprefpresent
            
            	Indicates the presence/absence of LOCAL\_PREF attribute for the route
            	**type**\:  bool
            
            .. attribute:: cbgproutemedpresent
            
            	Indicates the presence/absence of MULTI\_EXIT\_DISC attribute for the route
            	**type**\:  bool
            
            .. attribute:: cbgproutemultiexitdisc
            
            	This metric is used to discriminate between multiple exit points to an adjacent autonomous system.  The value of this object is irrelevant if the value of of cbgpRouteMedPresent is false(2)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgproutenexthop
            
            	The Network Layer address of the border router that should be used for the destination network
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgprouteorigin
            
            	The ultimate origin of the route information
            	**type**\:   :py:class:`Cbgprouteorigin <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.Cbgprouteorigin>`
            
            .. attribute:: cbgprouteunknownattr
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object.    Each path attribute is a triple <attribute type, attribute length, attribute value> of variable length. Attribute Type is a two\-octet field that consists of the Attribute Flags octet followed by the Attribute Type Code octet.  If the Extended Length bit of the  Attribute Flags octet is set to 0, the third octet of  the Path Attribute contains the length of the attribute data in octets.  If the Extended Length bit  of the Attribute Flags octet is set to 1, then the third and the fourth octets of the path attribute  contain the length of the attribute data in octets. The remaining octets of the Path Attribute represent  the attribute value and are interpreted according to  the Attribute Flags and the Attribute Type Code
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry, self).__init__()

                self.yang_name = "cbgpRouteEntry"
                self.yang_parent_name = "cbgpRouteTable"

                self.cbgprouteafi = YLeaf(YType.enumeration, "cbgpRouteAfi")

                self.cbgproutesafi = YLeaf(YType.enumeration, "cbgpRouteSafi")

                self.cbgproutepeertype = YLeaf(YType.enumeration, "cbgpRoutePeerType")

                self.cbgproutepeer = YLeaf(YType.str, "cbgpRoutePeer")

                self.cbgprouteaddrprefix = YLeaf(YType.str, "cbgpRouteAddrPrefix")

                self.cbgprouteaddrprefixlen = YLeaf(YType.uint32, "cbgpRouteAddrPrefixLen")

                self.cbgprouteaggregatoraddr = YLeaf(YType.str, "cbgpRouteAggregatorAddr")

                self.cbgprouteaggregatoraddrtype = YLeaf(YType.enumeration, "cbgpRouteAggregatorAddrType")

                self.cbgprouteaggregatoras = YLeaf(YType.uint32, "cbgpRouteAggregatorAS")

                self.cbgprouteaspathsegment = YLeaf(YType.str, "cbgpRouteASPathSegment")

                self.cbgprouteatomicaggregate = YLeaf(YType.enumeration, "cbgpRouteAtomicAggregate")

                self.cbgproutebest = YLeaf(YType.boolean, "cbgpRouteBest")

                self.cbgproutelocalpref = YLeaf(YType.uint32, "cbgpRouteLocalPref")

                self.cbgproutelocalprefpresent = YLeaf(YType.boolean, "cbgpRouteLocalPrefPresent")

                self.cbgproutemedpresent = YLeaf(YType.boolean, "cbgpRouteMedPresent")

                self.cbgproutemultiexitdisc = YLeaf(YType.uint32, "cbgpRouteMultiExitDisc")

                self.cbgproutenexthop = YLeaf(YType.str, "cbgpRouteNextHop")

                self.cbgprouteorigin = YLeaf(YType.enumeration, "cbgpRouteOrigin")

                self.cbgprouteunknownattr = YLeaf(YType.str, "cbgpRouteUnknownAttr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbgprouteafi",
                                "cbgproutesafi",
                                "cbgproutepeertype",
                                "cbgproutepeer",
                                "cbgprouteaddrprefix",
                                "cbgprouteaddrprefixlen",
                                "cbgprouteaggregatoraddr",
                                "cbgprouteaggregatoraddrtype",
                                "cbgprouteaggregatoras",
                                "cbgprouteaspathsegment",
                                "cbgprouteatomicaggregate",
                                "cbgproutebest",
                                "cbgproutelocalpref",
                                "cbgproutelocalprefpresent",
                                "cbgproutemedpresent",
                                "cbgproutemultiexitdisc",
                                "cbgproutenexthop",
                                "cbgprouteorigin",
                                "cbgprouteunknownattr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry, self).__setattr__(name, value)

            class Cbgprouteatomicaggregate(Enum):
                """
                Cbgprouteatomicaggregate

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
                Cbgprouteorigin

                The ultimate origin of the route information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = Enum.YLeaf(1, "igp")

                egp = Enum.YLeaf(2, "egp")

                incomplete = Enum.YLeaf(3, "incomplete")


            def has_data(self):
                return (
                    self.cbgprouteafi.is_set or
                    self.cbgproutesafi.is_set or
                    self.cbgproutepeertype.is_set or
                    self.cbgproutepeer.is_set or
                    self.cbgprouteaddrprefix.is_set or
                    self.cbgprouteaddrprefixlen.is_set or
                    self.cbgprouteaggregatoraddr.is_set or
                    self.cbgprouteaggregatoraddrtype.is_set or
                    self.cbgprouteaggregatoras.is_set or
                    self.cbgprouteaspathsegment.is_set or
                    self.cbgprouteatomicaggregate.is_set or
                    self.cbgproutebest.is_set or
                    self.cbgproutelocalpref.is_set or
                    self.cbgproutelocalprefpresent.is_set or
                    self.cbgproutemedpresent.is_set or
                    self.cbgproutemultiexitdisc.is_set or
                    self.cbgproutenexthop.is_set or
                    self.cbgprouteorigin.is_set or
                    self.cbgprouteunknownattr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbgprouteafi.yfilter != YFilter.not_set or
                    self.cbgproutesafi.yfilter != YFilter.not_set or
                    self.cbgproutepeertype.yfilter != YFilter.not_set or
                    self.cbgproutepeer.yfilter != YFilter.not_set or
                    self.cbgprouteaddrprefix.yfilter != YFilter.not_set or
                    self.cbgprouteaddrprefixlen.yfilter != YFilter.not_set or
                    self.cbgprouteaggregatoraddr.yfilter != YFilter.not_set or
                    self.cbgprouteaggregatoraddrtype.yfilter != YFilter.not_set or
                    self.cbgprouteaggregatoras.yfilter != YFilter.not_set or
                    self.cbgprouteaspathsegment.yfilter != YFilter.not_set or
                    self.cbgprouteatomicaggregate.yfilter != YFilter.not_set or
                    self.cbgproutebest.yfilter != YFilter.not_set or
                    self.cbgproutelocalpref.yfilter != YFilter.not_set or
                    self.cbgproutelocalprefpresent.yfilter != YFilter.not_set or
                    self.cbgproutemedpresent.yfilter != YFilter.not_set or
                    self.cbgproutemultiexitdisc.yfilter != YFilter.not_set or
                    self.cbgproutenexthop.yfilter != YFilter.not_set or
                    self.cbgprouteorigin.yfilter != YFilter.not_set or
                    self.cbgprouteunknownattr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpRouteEntry" + "[cbgpRouteAfi='" + self.cbgprouteafi.get() + "']" + "[cbgpRouteSafi='" + self.cbgproutesafi.get() + "']" + "[cbgpRoutePeerType='" + self.cbgproutepeertype.get() + "']" + "[cbgpRoutePeer='" + self.cbgproutepeer.get() + "']" + "[cbgpRouteAddrPrefix='" + self.cbgprouteaddrprefix.get() + "']" + "[cbgpRouteAddrPrefixLen='" + self.cbgprouteaddrprefixlen.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpRouteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbgprouteafi.is_set or self.cbgprouteafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteafi.get_name_leafdata())
                if (self.cbgproutesafi.is_set or self.cbgproutesafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutesafi.get_name_leafdata())
                if (self.cbgproutepeertype.is_set or self.cbgproutepeertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutepeertype.get_name_leafdata())
                if (self.cbgproutepeer.is_set or self.cbgproutepeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutepeer.get_name_leafdata())
                if (self.cbgprouteaddrprefix.is_set or self.cbgprouteaddrprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteaddrprefix.get_name_leafdata())
                if (self.cbgprouteaddrprefixlen.is_set or self.cbgprouteaddrprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteaddrprefixlen.get_name_leafdata())
                if (self.cbgprouteaggregatoraddr.is_set or self.cbgprouteaggregatoraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteaggregatoraddr.get_name_leafdata())
                if (self.cbgprouteaggregatoraddrtype.is_set or self.cbgprouteaggregatoraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteaggregatoraddrtype.get_name_leafdata())
                if (self.cbgprouteaggregatoras.is_set or self.cbgprouteaggregatoras.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteaggregatoras.get_name_leafdata())
                if (self.cbgprouteaspathsegment.is_set or self.cbgprouteaspathsegment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteaspathsegment.get_name_leafdata())
                if (self.cbgprouteatomicaggregate.is_set or self.cbgprouteatomicaggregate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteatomicaggregate.get_name_leafdata())
                if (self.cbgproutebest.is_set or self.cbgproutebest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutebest.get_name_leafdata())
                if (self.cbgproutelocalpref.is_set or self.cbgproutelocalpref.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutelocalpref.get_name_leafdata())
                if (self.cbgproutelocalprefpresent.is_set or self.cbgproutelocalprefpresent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutelocalprefpresent.get_name_leafdata())
                if (self.cbgproutemedpresent.is_set or self.cbgproutemedpresent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutemedpresent.get_name_leafdata())
                if (self.cbgproutemultiexitdisc.is_set or self.cbgproutemultiexitdisc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutemultiexitdisc.get_name_leafdata())
                if (self.cbgproutenexthop.is_set or self.cbgproutenexthop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgproutenexthop.get_name_leafdata())
                if (self.cbgprouteorigin.is_set or self.cbgprouteorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteorigin.get_name_leafdata())
                if (self.cbgprouteunknownattr.is_set or self.cbgprouteunknownattr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgprouteunknownattr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbgpRouteAfi" or name == "cbgpRouteSafi" or name == "cbgpRoutePeerType" or name == "cbgpRoutePeer" or name == "cbgpRouteAddrPrefix" or name == "cbgpRouteAddrPrefixLen" or name == "cbgpRouteAggregatorAddr" or name == "cbgpRouteAggregatorAddrType" or name == "cbgpRouteAggregatorAS" or name == "cbgpRouteASPathSegment" or name == "cbgpRouteAtomicAggregate" or name == "cbgpRouteBest" or name == "cbgpRouteLocalPref" or name == "cbgpRouteLocalPrefPresent" or name == "cbgpRouteMedPresent" or name == "cbgpRouteMultiExitDisc" or name == "cbgpRouteNextHop" or name == "cbgpRouteOrigin" or name == "cbgpRouteUnknownAttr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbgpRouteAfi"):
                    self.cbgprouteafi = value
                    self.cbgprouteafi.value_namespace = name_space
                    self.cbgprouteafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteSafi"):
                    self.cbgproutesafi = value
                    self.cbgproutesafi.value_namespace = name_space
                    self.cbgproutesafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRoutePeerType"):
                    self.cbgproutepeertype = value
                    self.cbgproutepeertype.value_namespace = name_space
                    self.cbgproutepeertype.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRoutePeer"):
                    self.cbgproutepeer = value
                    self.cbgproutepeer.value_namespace = name_space
                    self.cbgproutepeer.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteAddrPrefix"):
                    self.cbgprouteaddrprefix = value
                    self.cbgprouteaddrprefix.value_namespace = name_space
                    self.cbgprouteaddrprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteAddrPrefixLen"):
                    self.cbgprouteaddrprefixlen = value
                    self.cbgprouteaddrprefixlen.value_namespace = name_space
                    self.cbgprouteaddrprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteAggregatorAddr"):
                    self.cbgprouteaggregatoraddr = value
                    self.cbgprouteaggregatoraddr.value_namespace = name_space
                    self.cbgprouteaggregatoraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteAggregatorAddrType"):
                    self.cbgprouteaggregatoraddrtype = value
                    self.cbgprouteaggregatoraddrtype.value_namespace = name_space
                    self.cbgprouteaggregatoraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteAggregatorAS"):
                    self.cbgprouteaggregatoras = value
                    self.cbgprouteaggregatoras.value_namespace = name_space
                    self.cbgprouteaggregatoras.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteASPathSegment"):
                    self.cbgprouteaspathsegment = value
                    self.cbgprouteaspathsegment.value_namespace = name_space
                    self.cbgprouteaspathsegment.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteAtomicAggregate"):
                    self.cbgprouteatomicaggregate = value
                    self.cbgprouteatomicaggregate.value_namespace = name_space
                    self.cbgprouteatomicaggregate.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteBest"):
                    self.cbgproutebest = value
                    self.cbgproutebest.value_namespace = name_space
                    self.cbgproutebest.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteLocalPref"):
                    self.cbgproutelocalpref = value
                    self.cbgproutelocalpref.value_namespace = name_space
                    self.cbgproutelocalpref.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteLocalPrefPresent"):
                    self.cbgproutelocalprefpresent = value
                    self.cbgproutelocalprefpresent.value_namespace = name_space
                    self.cbgproutelocalprefpresent.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteMedPresent"):
                    self.cbgproutemedpresent = value
                    self.cbgproutemedpresent.value_namespace = name_space
                    self.cbgproutemedpresent.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteMultiExitDisc"):
                    self.cbgproutemultiexitdisc = value
                    self.cbgproutemultiexitdisc.value_namespace = name_space
                    self.cbgproutemultiexitdisc.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteNextHop"):
                    self.cbgproutenexthop = value
                    self.cbgproutenexthop.value_namespace = name_space
                    self.cbgproutenexthop.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteOrigin"):
                    self.cbgprouteorigin = value
                    self.cbgprouteorigin.value_namespace = name_space
                    self.cbgprouteorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpRouteUnknownAttr"):
                    self.cbgprouteunknownattr = value
                    self.cbgprouteunknownattr.value_namespace = name_space
                    self.cbgprouteunknownattr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgprouteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgprouteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpRouteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpRouteEntry"):
                for c in self.cbgprouteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgprouteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpRouteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cbgppeercapsentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeercapstable, self).__init__()

            self.yang_name = "cbgpPeerCapsTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeercapsentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeercapstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeercapstable, self).__setattr__(name, value)


        class Cbgppeercapsentry(Entity):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a 
            capability is received multiple times with different
            values during a BGP connection establishment, 
            corresponding entries are differentiated with indices.
            
            .. attribute:: bgppeerremoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeercapcode  <key>
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:   :py:class:`Cbgppeercapcode <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry.Cbgppeercapcode>`
            
            .. attribute:: cbgppeercapindex  <key>
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: cbgppeercapvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry, self).__init__()

                self.yang_name = "cbgpPeerCapsEntry"
                self.yang_parent_name = "cbgpPeerCapsTable"

                self.bgppeerremoteaddr = YLeaf(YType.str, "bgpPeerRemoteAddr")

                self.cbgppeercapcode = YLeaf(YType.enumeration, "cbgpPeerCapCode")

                self.cbgppeercapindex = YLeaf(YType.uint32, "cbgpPeerCapIndex")

                self.cbgppeercapvalue = YLeaf(YType.str, "cbgpPeerCapValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bgppeerremoteaddr",
                                "cbgppeercapcode",
                                "cbgppeercapindex",
                                "cbgppeercapvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry, self).__setattr__(name, value)

            class Cbgppeercapcode(Enum):
                """
                Cbgppeercapcode

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


            def has_data(self):
                return (
                    self.bgppeerremoteaddr.is_set or
                    self.cbgppeercapcode.is_set or
                    self.cbgppeercapindex.is_set or
                    self.cbgppeercapvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bgppeerremoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeercapcode.yfilter != YFilter.not_set or
                    self.cbgppeercapindex.yfilter != YFilter.not_set or
                    self.cbgppeercapvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeerCapsEntry" + "[bgpPeerRemoteAddr='" + self.bgppeerremoteaddr.get() + "']" + "[cbgpPeerCapCode='" + self.cbgppeercapcode.get() + "']" + "[cbgpPeerCapIndex='" + self.cbgppeercapindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerCapsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bgppeerremoteaddr.is_set or self.bgppeerremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerremoteaddr.get_name_leafdata())
                if (self.cbgppeercapcode.is_set or self.cbgppeercapcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeercapcode.get_name_leafdata())
                if (self.cbgppeercapindex.is_set or self.cbgppeercapindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeercapindex.get_name_leafdata())
                if (self.cbgppeercapvalue.is_set or self.cbgppeercapvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeercapvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgpPeerRemoteAddr" or name == "cbgpPeerCapCode" or name == "cbgpPeerCapIndex" or name == "cbgpPeerCapValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bgpPeerRemoteAddr"):
                    self.bgppeerremoteaddr = value
                    self.bgppeerremoteaddr.value_namespace = name_space
                    self.bgppeerremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerCapCode"):
                    self.cbgppeercapcode = value
                    self.cbgppeercapcode.value_namespace = name_space
                    self.cbgppeercapcode.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerCapIndex"):
                    self.cbgppeercapindex = value
                    self.cbgppeercapindex.value_namespace = name_space
                    self.cbgppeercapindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerCapValue"):
                    self.cbgppeercapvalue = value
                    self.cbgppeercapvalue.value_namespace = name_space
                    self.cbgppeercapvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeercapsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeercapsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeerCapsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeerCapsEntry"):
                for c in self.cbgppeercapsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeercapsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeerCapsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cbgppeeraddrfamilyentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeeraddrfamilytable, self).__init__()

            self.yang_name = "cbgpPeerAddrFamilyTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeeraddrfamilyentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeeraddrfamilytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeeraddrfamilytable, self).__setattr__(name, value)


        class Cbgppeeraddrfamilyentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: bgppeerremoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeeraddrfamilyafi  <key>
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and  VPNv4 (Value \- 1) address families
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeeraddrfamilysafi  <key>
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value  \- 1) and VPNv4( Value \- 128) address families
            	**type**\:   :py:class:`Cbgpsafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.Cbgpsafi>`
            
            .. attribute:: cbgppeeraddrfamilyname
            
            	Implementation specific Address Family name
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry, self).__init__()

                self.yang_name = "cbgpPeerAddrFamilyEntry"
                self.yang_parent_name = "cbgpPeerAddrFamilyTable"

                self.bgppeerremoteaddr = YLeaf(YType.str, "bgpPeerRemoteAddr")

                self.cbgppeeraddrfamilyafi = YLeaf(YType.enumeration, "cbgpPeerAddrFamilyAfi")

                self.cbgppeeraddrfamilysafi = YLeaf(YType.enumeration, "cbgpPeerAddrFamilySafi")

                self.cbgppeeraddrfamilyname = YLeaf(YType.str, "cbgpPeerAddrFamilyName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bgppeerremoteaddr",
                                "cbgppeeraddrfamilyafi",
                                "cbgppeeraddrfamilysafi",
                                "cbgppeeraddrfamilyname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.bgppeerremoteaddr.is_set or
                    self.cbgppeeraddrfamilyafi.is_set or
                    self.cbgppeeraddrfamilysafi.is_set or
                    self.cbgppeeraddrfamilyname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bgppeerremoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeeraddrfamilyafi.yfilter != YFilter.not_set or
                    self.cbgppeeraddrfamilysafi.yfilter != YFilter.not_set or
                    self.cbgppeeraddrfamilyname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeerAddrFamilyEntry" + "[bgpPeerRemoteAddr='" + self.bgppeerremoteaddr.get() + "']" + "[cbgpPeerAddrFamilyAfi='" + self.cbgppeeraddrfamilyafi.get() + "']" + "[cbgpPeerAddrFamilySafi='" + self.cbgppeeraddrfamilysafi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerAddrFamilyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bgppeerremoteaddr.is_set or self.bgppeerremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerremoteaddr.get_name_leafdata())
                if (self.cbgppeeraddrfamilyafi.is_set or self.cbgppeeraddrfamilyafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeraddrfamilyafi.get_name_leafdata())
                if (self.cbgppeeraddrfamilysafi.is_set or self.cbgppeeraddrfamilysafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeraddrfamilysafi.get_name_leafdata())
                if (self.cbgppeeraddrfamilyname.is_set or self.cbgppeeraddrfamilyname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeraddrfamilyname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgpPeerRemoteAddr" or name == "cbgpPeerAddrFamilyAfi" or name == "cbgpPeerAddrFamilySafi" or name == "cbgpPeerAddrFamilyName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bgpPeerRemoteAddr"):
                    self.bgppeerremoteaddr = value
                    self.bgppeerremoteaddr.value_namespace = name_space
                    self.bgppeerremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAddrFamilyAfi"):
                    self.cbgppeeraddrfamilyafi = value
                    self.cbgppeeraddrfamilyafi.value_namespace = name_space
                    self.cbgppeeraddrfamilyafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAddrFamilySafi"):
                    self.cbgppeeraddrfamilysafi = value
                    self.cbgppeeraddrfamilysafi.value_namespace = name_space
                    self.cbgppeeraddrfamilysafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAddrFamilyName"):
                    self.cbgppeeraddrfamilyname = value
                    self.cbgppeeraddrfamilyname.value_namespace = name_space
                    self.cbgppeeraddrfamilyname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeeraddrfamilyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeeraddrfamilyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeerAddrFamilyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeerAddrFamilyEntry"):
                for c in self.cbgppeeraddrfamilyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeeraddrfamilyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeerAddrFamilyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cbgppeeraddrfamilyprefixentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable, self).__init__()

            self.yang_name = "cbgpPeerAddrFamilyPrefixTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeeraddrfamilyprefixentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable, self).__setattr__(name, value)


        class Cbgppeeraddrfamilyprefixentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated 
            with route prefixes belonging to an address family.
            
            .. attribute:: bgppeerremoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeeraddrfamilyafi  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeeraddrfamilysafi  <key>
            
            	
            	**type**\:   :py:class:`Cbgpsafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.Cbgpsafi>`
            
            .. attribute:: cbgppeeracceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeeradvertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerdeniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this  connection is denied. It is initialized to zero when  the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerprefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbgppeerprefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\:  int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeerprefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or  corresponding SNMP notification is generated
            	**type**\:  int
            
            	**range:** 1..100
            
            .. attribute:: cbgppeersuppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is  initialized to zero when the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeerwithdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry, self).__init__()

                self.yang_name = "cbgpPeerAddrFamilyPrefixEntry"
                self.yang_parent_name = "cbgpPeerAddrFamilyPrefixTable"

                self.bgppeerremoteaddr = YLeaf(YType.str, "bgpPeerRemoteAddr")

                self.cbgppeeraddrfamilyafi = YLeaf(YType.enumeration, "cbgpPeerAddrFamilyAfi")

                self.cbgppeeraddrfamilysafi = YLeaf(YType.enumeration, "cbgpPeerAddrFamilySafi")

                self.cbgppeeracceptedprefixes = YLeaf(YType.uint32, "cbgpPeerAcceptedPrefixes")

                self.cbgppeeradvertisedprefixes = YLeaf(YType.uint32, "cbgpPeerAdvertisedPrefixes")

                self.cbgppeerdeniedprefixes = YLeaf(YType.uint32, "cbgpPeerDeniedPrefixes")

                self.cbgppeerprefixadminlimit = YLeaf(YType.uint32, "cbgpPeerPrefixAdminLimit")

                self.cbgppeerprefixclearthreshold = YLeaf(YType.uint32, "cbgpPeerPrefixClearThreshold")

                self.cbgppeerprefixthreshold = YLeaf(YType.uint32, "cbgpPeerPrefixThreshold")

                self.cbgppeersuppressedprefixes = YLeaf(YType.uint32, "cbgpPeerSuppressedPrefixes")

                self.cbgppeerwithdrawnprefixes = YLeaf(YType.uint32, "cbgpPeerWithdrawnPrefixes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bgppeerremoteaddr",
                                "cbgppeeraddrfamilyafi",
                                "cbgppeeraddrfamilysafi",
                                "cbgppeeracceptedprefixes",
                                "cbgppeeradvertisedprefixes",
                                "cbgppeerdeniedprefixes",
                                "cbgppeerprefixadminlimit",
                                "cbgppeerprefixclearthreshold",
                                "cbgppeerprefixthreshold",
                                "cbgppeersuppressedprefixes",
                                "cbgppeerwithdrawnprefixes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.bgppeerremoteaddr.is_set or
                    self.cbgppeeraddrfamilyafi.is_set or
                    self.cbgppeeraddrfamilysafi.is_set or
                    self.cbgppeeracceptedprefixes.is_set or
                    self.cbgppeeradvertisedprefixes.is_set or
                    self.cbgppeerdeniedprefixes.is_set or
                    self.cbgppeerprefixadminlimit.is_set or
                    self.cbgppeerprefixclearthreshold.is_set or
                    self.cbgppeerprefixthreshold.is_set or
                    self.cbgppeersuppressedprefixes.is_set or
                    self.cbgppeerwithdrawnprefixes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bgppeerremoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeeraddrfamilyafi.yfilter != YFilter.not_set or
                    self.cbgppeeraddrfamilysafi.yfilter != YFilter.not_set or
                    self.cbgppeeracceptedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeeradvertisedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeerdeniedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeerprefixadminlimit.yfilter != YFilter.not_set or
                    self.cbgppeerprefixclearthreshold.yfilter != YFilter.not_set or
                    self.cbgppeerprefixthreshold.yfilter != YFilter.not_set or
                    self.cbgppeersuppressedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeerwithdrawnprefixes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeerAddrFamilyPrefixEntry" + "[bgpPeerRemoteAddr='" + self.bgppeerremoteaddr.get() + "']" + "[cbgpPeerAddrFamilyAfi='" + self.cbgppeeraddrfamilyafi.get() + "']" + "[cbgpPeerAddrFamilySafi='" + self.cbgppeeraddrfamilysafi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeerAddrFamilyPrefixTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bgppeerremoteaddr.is_set or self.bgppeerremoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgppeerremoteaddr.get_name_leafdata())
                if (self.cbgppeeraddrfamilyafi.is_set or self.cbgppeeraddrfamilyafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeraddrfamilyafi.get_name_leafdata())
                if (self.cbgppeeraddrfamilysafi.is_set or self.cbgppeeraddrfamilysafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeraddrfamilysafi.get_name_leafdata())
                if (self.cbgppeeracceptedprefixes.is_set or self.cbgppeeracceptedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeracceptedprefixes.get_name_leafdata())
                if (self.cbgppeeradvertisedprefixes.is_set or self.cbgppeeradvertisedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeeradvertisedprefixes.get_name_leafdata())
                if (self.cbgppeerdeniedprefixes.is_set or self.cbgppeerdeniedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerdeniedprefixes.get_name_leafdata())
                if (self.cbgppeerprefixadminlimit.is_set or self.cbgppeerprefixadminlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixadminlimit.get_name_leafdata())
                if (self.cbgppeerprefixclearthreshold.is_set or self.cbgppeerprefixclearthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixclearthreshold.get_name_leafdata())
                if (self.cbgppeerprefixthreshold.is_set or self.cbgppeerprefixthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerprefixthreshold.get_name_leafdata())
                if (self.cbgppeersuppressedprefixes.is_set or self.cbgppeersuppressedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeersuppressedprefixes.get_name_leafdata())
                if (self.cbgppeerwithdrawnprefixes.is_set or self.cbgppeerwithdrawnprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeerwithdrawnprefixes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgpPeerRemoteAddr" or name == "cbgpPeerAddrFamilyAfi" or name == "cbgpPeerAddrFamilySafi" or name == "cbgpPeerAcceptedPrefixes" or name == "cbgpPeerAdvertisedPrefixes" or name == "cbgpPeerDeniedPrefixes" or name == "cbgpPeerPrefixAdminLimit" or name == "cbgpPeerPrefixClearThreshold" or name == "cbgpPeerPrefixThreshold" or name == "cbgpPeerSuppressedPrefixes" or name == "cbgpPeerWithdrawnPrefixes"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bgpPeerRemoteAddr"):
                    self.bgppeerremoteaddr = value
                    self.bgppeerremoteaddr.value_namespace = name_space
                    self.bgppeerremoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAddrFamilyAfi"):
                    self.cbgppeeraddrfamilyafi = value
                    self.cbgppeeraddrfamilyafi.value_namespace = name_space
                    self.cbgppeeraddrfamilyafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAddrFamilySafi"):
                    self.cbgppeeraddrfamilysafi = value
                    self.cbgppeeraddrfamilysafi.value_namespace = name_space
                    self.cbgppeeraddrfamilysafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAcceptedPrefixes"):
                    self.cbgppeeracceptedprefixes = value
                    self.cbgppeeracceptedprefixes.value_namespace = name_space
                    self.cbgppeeracceptedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerAdvertisedPrefixes"):
                    self.cbgppeeradvertisedprefixes = value
                    self.cbgppeeradvertisedprefixes.value_namespace = name_space
                    self.cbgppeeradvertisedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerDeniedPrefixes"):
                    self.cbgppeerdeniedprefixes = value
                    self.cbgppeerdeniedprefixes.value_namespace = name_space
                    self.cbgppeerdeniedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixAdminLimit"):
                    self.cbgppeerprefixadminlimit = value
                    self.cbgppeerprefixadminlimit.value_namespace = name_space
                    self.cbgppeerprefixadminlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixClearThreshold"):
                    self.cbgppeerprefixclearthreshold = value
                    self.cbgppeerprefixclearthreshold.value_namespace = name_space
                    self.cbgppeerprefixclearthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerPrefixThreshold"):
                    self.cbgppeerprefixthreshold = value
                    self.cbgppeerprefixthreshold.value_namespace = name_space
                    self.cbgppeerprefixthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerSuppressedPrefixes"):
                    self.cbgppeersuppressedprefixes = value
                    self.cbgppeersuppressedprefixes.value_namespace = name_space
                    self.cbgppeersuppressedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeerWithdrawnPrefixes"):
                    self.cbgppeerwithdrawnprefixes = value
                    self.cbgppeerwithdrawnprefixes.value_namespace = name_space
                    self.cbgppeerwithdrawnprefixes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeeraddrfamilyprefixentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeeraddrfamilyprefixentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeerAddrFamilyPrefixTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeerAddrFamilyPrefixEntry"):
                for c in self.cbgppeeraddrfamilyprefixentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeeraddrfamilyprefixentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeerAddrFamilyPrefixEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cbgppeer2Table(Entity):
        """
        BGP peer table.  This table contains,
        one entry per BGP peer, information about
        the connections with BGP peers.
        
        .. attribute:: cbgppeer2entry
        
        	Entry containing information about the connection with a BGP peer
        	**type**\: list of    :py:class:`Cbgppeer2Entry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeer2Table, self).__init__()

            self.yang_name = "cbgpPeer2Table"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeer2entry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeer2Table, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeer2Table, self).__setattr__(name, value)


        class Cbgppeer2Entry(Entity):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: cbgppeer2type  <key>
            
            	Represents the type of Peer address stored in cbgpPeer2Entry
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	The remote IP address of this entry's BGP peer
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgppeer2adminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Manual Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Manual Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:   :py:class:`Cbgppeer2Adminstatus <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2Adminstatus>`
            
            .. attribute:: cbgppeer2connectretryinterval
            
            	Time interval (in seconds) for the ConnectRetry timer.  The suggested value for this timer is 120 seconds
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2fsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the established state or how long since this peer was last in the established state.  It is set to zero when a new peer is configured or when the router is booted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2fsmestablishedtransitions
            
            	The total number of times the BGP FSM transitioned into the established state for this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2holdtime
            
            	Time interval (in seconds) for the Hold Timer established with the peer.  The value of this object is calculated by this BGP speaker, using the smaller of the values in cbgpPeer2HoldTimeConfigured and the Hold Time received in the OPEN message.  This value must be at least three seconds if it is not zero (0).  If the Hold Timer has not been established with the peer this object MUST have a value of zero (0).  If the cbgpPeer2HoldTimeConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\:  int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2holdtimeconfigured
            
            	Time interval (in seconds) for the Hold Time configured for this BGP speaker with this peer.  This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (cbgpPeer2HoldTime) with the peer. This value must not be less than three seconds if it is not zero (0).  If it is zero (0), the Hold Time is NOT to be established with the peer.  The suggested value for this timer is 90 seconds
            	**type**\:  int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2intotalmessages
            
            	The total number of messages received from the remote peer on this connection
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2inupdateelapsedtime
            
            	Elapsed time (in seconds) since the last BGP UPDATE message was received from the peer. Each time cbgpPeer2InUpdates is incremented, the value of this object is set to zero (0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2inupdates
            
            	The number of BGP UPDATE messages received on this connection
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2keepalive
            
            	Time interval (in seconds) for the KeepAlive timer established with the peer.  The value of this object is calculated by this BGP speaker such that, when compared with cbgpPeer2HoldTime, it has the same proportion that cbgpPeer2KeepAliveConfigured has, compared with cbgpPeer2HoldTimeConfigured.  If the KeepAlive timer has not been established with the peer, this object MUST have a value of zero (0).  If the of cbgpPeer2KeepAliveConfigured object has a value of (0), then this object MUST have a value of (0)
            	**type**\:  int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2keepaliveconfigured
            
            	Time interval (in seconds) for the KeepAlive timer configured for this BGP speaker with this peer.  The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in cbgpPeer2HoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by cbgpPeer2KeepAlive.  A reasonable maximum value for this timer would be one third of that of cbgpPeer2HoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established.  The suggested value for this timer is 30 seconds
            	**type**\:  int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2lasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\:  str
            
            	**length:** 2
            
            .. attribute:: cbgppeer2lasterrortxt
            
            	Implementation specific error description for bgpPeerLastErrorReceived
            	**type**\:  str
            
            .. attribute:: cbgppeer2localaddr
            
            	The local IP address of this entry's BGP connection
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgppeer2localas
            
            	The local AS number for this session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2localidentifier
            
            	The BGP Identifier of this entry's BGP peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeer2localport
            
            	The local port for the TCP connection between the BGP peers
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cbgppeer2minasoriginationinterval
            
            	Time interval (in seconds) for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2minrouteadvertisementinterval
            
            	Time interval (in seconds) for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds for EBGP connections and 5 seconds for IBGP connections
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: cbgppeer2negotiatedversion
            
            	The negotiated version of BGP running between the two peers.  This entry MUST be zero (0) unless the cbgpPeer2State is in the openconfirm or the established state.  Note that legal values for this object are between 0 and 255
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cbgppeer2outtotalmessages
            
            	The total number of messages transmitted to the remote peer on this connection
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2outupdates
            
            	The number of BGP UPDATE messages transmitted on this connection
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2prevstate
            
            	The BGP peer connection previous state
            	**type**\:   :py:class:`Cbgppeer2Prevstate <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2Prevstate>`
            
            .. attribute:: cbgppeer2remoteas
            
            	The remote autonomous system number received in the BGP OPEN message
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2remoteidentifier
            
            	The BGP Identifier of this entry's BGP peer. This entry MUST be 0.0.0.0 unless the cbgpPeer2State is in the openconfirm or the established state
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cbgppeer2remoteport
            
            	The remote port for the TCP connection between the BGP peers.  Note that the objects cbgpPeer2LocalAddr, cbgpPeer2LocalPort, cbgpPeer2RemoteAddr, and cbgpPeer2RemotePort provide the appropriate reference to the standard MIB TCP connection table
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cbgppeer2state
            
            	The BGP peer connection state
            	**type**\:   :py:class:`Cbgppeer2State <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2State>`
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry, self).__init__()

                self.yang_name = "cbgpPeer2Entry"
                self.yang_parent_name = "cbgpPeer2Table"

                self.cbgppeer2type = YLeaf(YType.enumeration, "cbgpPeer2Type")

                self.cbgppeer2remoteaddr = YLeaf(YType.str, "cbgpPeer2RemoteAddr")

                self.cbgppeer2adminstatus = YLeaf(YType.enumeration, "cbgpPeer2AdminStatus")

                self.cbgppeer2connectretryinterval = YLeaf(YType.int32, "cbgpPeer2ConnectRetryInterval")

                self.cbgppeer2fsmestablishedtime = YLeaf(YType.uint32, "cbgpPeer2FsmEstablishedTime")

                self.cbgppeer2fsmestablishedtransitions = YLeaf(YType.uint32, "cbgpPeer2FsmEstablishedTransitions")

                self.cbgppeer2holdtime = YLeaf(YType.int32, "cbgpPeer2HoldTime")

                self.cbgppeer2holdtimeconfigured = YLeaf(YType.int32, "cbgpPeer2HoldTimeConfigured")

                self.cbgppeer2intotalmessages = YLeaf(YType.uint32, "cbgpPeer2InTotalMessages")

                self.cbgppeer2inupdateelapsedtime = YLeaf(YType.uint32, "cbgpPeer2InUpdateElapsedTime")

                self.cbgppeer2inupdates = YLeaf(YType.uint32, "cbgpPeer2InUpdates")

                self.cbgppeer2keepalive = YLeaf(YType.int32, "cbgpPeer2KeepAlive")

                self.cbgppeer2keepaliveconfigured = YLeaf(YType.int32, "cbgpPeer2KeepAliveConfigured")

                self.cbgppeer2lasterror = YLeaf(YType.str, "cbgpPeer2LastError")

                self.cbgppeer2lasterrortxt = YLeaf(YType.str, "cbgpPeer2LastErrorTxt")

                self.cbgppeer2localaddr = YLeaf(YType.str, "cbgpPeer2LocalAddr")

                self.cbgppeer2localas = YLeaf(YType.uint32, "cbgpPeer2LocalAs")

                self.cbgppeer2localidentifier = YLeaf(YType.str, "cbgpPeer2LocalIdentifier")

                self.cbgppeer2localport = YLeaf(YType.uint16, "cbgpPeer2LocalPort")

                self.cbgppeer2minasoriginationinterval = YLeaf(YType.int32, "cbgpPeer2MinASOriginationInterval")

                self.cbgppeer2minrouteadvertisementinterval = YLeaf(YType.int32, "cbgpPeer2MinRouteAdvertisementInterval")

                self.cbgppeer2negotiatedversion = YLeaf(YType.int32, "cbgpPeer2NegotiatedVersion")

                self.cbgppeer2outtotalmessages = YLeaf(YType.uint32, "cbgpPeer2OutTotalMessages")

                self.cbgppeer2outupdates = YLeaf(YType.uint32, "cbgpPeer2OutUpdates")

                self.cbgppeer2prevstate = YLeaf(YType.enumeration, "cbgpPeer2PrevState")

                self.cbgppeer2remoteas = YLeaf(YType.uint32, "cbgpPeer2RemoteAs")

                self.cbgppeer2remoteidentifier = YLeaf(YType.str, "cbgpPeer2RemoteIdentifier")

                self.cbgppeer2remoteport = YLeaf(YType.uint16, "cbgpPeer2RemotePort")

                self.cbgppeer2state = YLeaf(YType.enumeration, "cbgpPeer2State")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbgppeer2type",
                                "cbgppeer2remoteaddr",
                                "cbgppeer2adminstatus",
                                "cbgppeer2connectretryinterval",
                                "cbgppeer2fsmestablishedtime",
                                "cbgppeer2fsmestablishedtransitions",
                                "cbgppeer2holdtime",
                                "cbgppeer2holdtimeconfigured",
                                "cbgppeer2intotalmessages",
                                "cbgppeer2inupdateelapsedtime",
                                "cbgppeer2inupdates",
                                "cbgppeer2keepalive",
                                "cbgppeer2keepaliveconfigured",
                                "cbgppeer2lasterror",
                                "cbgppeer2lasterrortxt",
                                "cbgppeer2localaddr",
                                "cbgppeer2localas",
                                "cbgppeer2localidentifier",
                                "cbgppeer2localport",
                                "cbgppeer2minasoriginationinterval",
                                "cbgppeer2minrouteadvertisementinterval",
                                "cbgppeer2negotiatedversion",
                                "cbgppeer2outtotalmessages",
                                "cbgppeer2outupdates",
                                "cbgppeer2prevstate",
                                "cbgppeer2remoteas",
                                "cbgppeer2remoteidentifier",
                                "cbgppeer2remoteport",
                                "cbgppeer2state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry, self).__setattr__(name, value)

            class Cbgppeer2Adminstatus(Enum):
                """
                Cbgppeer2Adminstatus

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
                Cbgppeer2Prevstate

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
                Cbgppeer2State

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


            def has_data(self):
                return (
                    self.cbgppeer2type.is_set or
                    self.cbgppeer2remoteaddr.is_set or
                    self.cbgppeer2adminstatus.is_set or
                    self.cbgppeer2connectretryinterval.is_set or
                    self.cbgppeer2fsmestablishedtime.is_set or
                    self.cbgppeer2fsmestablishedtransitions.is_set or
                    self.cbgppeer2holdtime.is_set or
                    self.cbgppeer2holdtimeconfigured.is_set or
                    self.cbgppeer2intotalmessages.is_set or
                    self.cbgppeer2inupdateelapsedtime.is_set or
                    self.cbgppeer2inupdates.is_set or
                    self.cbgppeer2keepalive.is_set or
                    self.cbgppeer2keepaliveconfigured.is_set or
                    self.cbgppeer2lasterror.is_set or
                    self.cbgppeer2lasterrortxt.is_set or
                    self.cbgppeer2localaddr.is_set or
                    self.cbgppeer2localas.is_set or
                    self.cbgppeer2localidentifier.is_set or
                    self.cbgppeer2localport.is_set or
                    self.cbgppeer2minasoriginationinterval.is_set or
                    self.cbgppeer2minrouteadvertisementinterval.is_set or
                    self.cbgppeer2negotiatedversion.is_set or
                    self.cbgppeer2outtotalmessages.is_set or
                    self.cbgppeer2outupdates.is_set or
                    self.cbgppeer2prevstate.is_set or
                    self.cbgppeer2remoteas.is_set or
                    self.cbgppeer2remoteidentifier.is_set or
                    self.cbgppeer2remoteport.is_set or
                    self.cbgppeer2state.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbgppeer2type.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeer2adminstatus.yfilter != YFilter.not_set or
                    self.cbgppeer2connectretryinterval.yfilter != YFilter.not_set or
                    self.cbgppeer2fsmestablishedtime.yfilter != YFilter.not_set or
                    self.cbgppeer2fsmestablishedtransitions.yfilter != YFilter.not_set or
                    self.cbgppeer2holdtime.yfilter != YFilter.not_set or
                    self.cbgppeer2holdtimeconfigured.yfilter != YFilter.not_set or
                    self.cbgppeer2intotalmessages.yfilter != YFilter.not_set or
                    self.cbgppeer2inupdateelapsedtime.yfilter != YFilter.not_set or
                    self.cbgppeer2inupdates.yfilter != YFilter.not_set or
                    self.cbgppeer2keepalive.yfilter != YFilter.not_set or
                    self.cbgppeer2keepaliveconfigured.yfilter != YFilter.not_set or
                    self.cbgppeer2lasterror.yfilter != YFilter.not_set or
                    self.cbgppeer2lasterrortxt.yfilter != YFilter.not_set or
                    self.cbgppeer2localaddr.yfilter != YFilter.not_set or
                    self.cbgppeer2localas.yfilter != YFilter.not_set or
                    self.cbgppeer2localidentifier.yfilter != YFilter.not_set or
                    self.cbgppeer2localport.yfilter != YFilter.not_set or
                    self.cbgppeer2minasoriginationinterval.yfilter != YFilter.not_set or
                    self.cbgppeer2minrouteadvertisementinterval.yfilter != YFilter.not_set or
                    self.cbgppeer2negotiatedversion.yfilter != YFilter.not_set or
                    self.cbgppeer2outtotalmessages.yfilter != YFilter.not_set or
                    self.cbgppeer2outupdates.yfilter != YFilter.not_set or
                    self.cbgppeer2prevstate.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteas.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteidentifier.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteport.yfilter != YFilter.not_set or
                    self.cbgppeer2state.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeer2Entry" + "[cbgpPeer2Type='" + self.cbgppeer2type.get() + "']" + "[cbgpPeer2RemoteAddr='" + self.cbgppeer2remoteaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2Table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbgppeer2type.is_set or self.cbgppeer2type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2type.get_name_leafdata())
                if (self.cbgppeer2remoteaddr.is_set or self.cbgppeer2remoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteaddr.get_name_leafdata())
                if (self.cbgppeer2adminstatus.is_set or self.cbgppeer2adminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2adminstatus.get_name_leafdata())
                if (self.cbgppeer2connectretryinterval.is_set or self.cbgppeer2connectretryinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2connectretryinterval.get_name_leafdata())
                if (self.cbgppeer2fsmestablishedtime.is_set or self.cbgppeer2fsmestablishedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2fsmestablishedtime.get_name_leafdata())
                if (self.cbgppeer2fsmestablishedtransitions.is_set or self.cbgppeer2fsmestablishedtransitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2fsmestablishedtransitions.get_name_leafdata())
                if (self.cbgppeer2holdtime.is_set or self.cbgppeer2holdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2holdtime.get_name_leafdata())
                if (self.cbgppeer2holdtimeconfigured.is_set or self.cbgppeer2holdtimeconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2holdtimeconfigured.get_name_leafdata())
                if (self.cbgppeer2intotalmessages.is_set or self.cbgppeer2intotalmessages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2intotalmessages.get_name_leafdata())
                if (self.cbgppeer2inupdateelapsedtime.is_set or self.cbgppeer2inupdateelapsedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2inupdateelapsedtime.get_name_leafdata())
                if (self.cbgppeer2inupdates.is_set or self.cbgppeer2inupdates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2inupdates.get_name_leafdata())
                if (self.cbgppeer2keepalive.is_set or self.cbgppeer2keepalive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2keepalive.get_name_leafdata())
                if (self.cbgppeer2keepaliveconfigured.is_set or self.cbgppeer2keepaliveconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2keepaliveconfigured.get_name_leafdata())
                if (self.cbgppeer2lasterror.is_set or self.cbgppeer2lasterror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2lasterror.get_name_leafdata())
                if (self.cbgppeer2lasterrortxt.is_set or self.cbgppeer2lasterrortxt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2lasterrortxt.get_name_leafdata())
                if (self.cbgppeer2localaddr.is_set or self.cbgppeer2localaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2localaddr.get_name_leafdata())
                if (self.cbgppeer2localas.is_set or self.cbgppeer2localas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2localas.get_name_leafdata())
                if (self.cbgppeer2localidentifier.is_set or self.cbgppeer2localidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2localidentifier.get_name_leafdata())
                if (self.cbgppeer2localport.is_set or self.cbgppeer2localport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2localport.get_name_leafdata())
                if (self.cbgppeer2minasoriginationinterval.is_set or self.cbgppeer2minasoriginationinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2minasoriginationinterval.get_name_leafdata())
                if (self.cbgppeer2minrouteadvertisementinterval.is_set or self.cbgppeer2minrouteadvertisementinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2minrouteadvertisementinterval.get_name_leafdata())
                if (self.cbgppeer2negotiatedversion.is_set or self.cbgppeer2negotiatedversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2negotiatedversion.get_name_leafdata())
                if (self.cbgppeer2outtotalmessages.is_set or self.cbgppeer2outtotalmessages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2outtotalmessages.get_name_leafdata())
                if (self.cbgppeer2outupdates.is_set or self.cbgppeer2outupdates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2outupdates.get_name_leafdata())
                if (self.cbgppeer2prevstate.is_set or self.cbgppeer2prevstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2prevstate.get_name_leafdata())
                if (self.cbgppeer2remoteas.is_set or self.cbgppeer2remoteas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteas.get_name_leafdata())
                if (self.cbgppeer2remoteidentifier.is_set or self.cbgppeer2remoteidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteidentifier.get_name_leafdata())
                if (self.cbgppeer2remoteport.is_set or self.cbgppeer2remoteport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteport.get_name_leafdata())
                if (self.cbgppeer2state.is_set or self.cbgppeer2state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2state.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbgpPeer2Type" or name == "cbgpPeer2RemoteAddr" or name == "cbgpPeer2AdminStatus" or name == "cbgpPeer2ConnectRetryInterval" or name == "cbgpPeer2FsmEstablishedTime" or name == "cbgpPeer2FsmEstablishedTransitions" or name == "cbgpPeer2HoldTime" or name == "cbgpPeer2HoldTimeConfigured" or name == "cbgpPeer2InTotalMessages" or name == "cbgpPeer2InUpdateElapsedTime" or name == "cbgpPeer2InUpdates" or name == "cbgpPeer2KeepAlive" or name == "cbgpPeer2KeepAliveConfigured" or name == "cbgpPeer2LastError" or name == "cbgpPeer2LastErrorTxt" or name == "cbgpPeer2LocalAddr" or name == "cbgpPeer2LocalAs" or name == "cbgpPeer2LocalIdentifier" or name == "cbgpPeer2LocalPort" or name == "cbgpPeer2MinASOriginationInterval" or name == "cbgpPeer2MinRouteAdvertisementInterval" or name == "cbgpPeer2NegotiatedVersion" or name == "cbgpPeer2OutTotalMessages" or name == "cbgpPeer2OutUpdates" or name == "cbgpPeer2PrevState" or name == "cbgpPeer2RemoteAs" or name == "cbgpPeer2RemoteIdentifier" or name == "cbgpPeer2RemotePort" or name == "cbgpPeer2State"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbgpPeer2Type"):
                    self.cbgppeer2type = value
                    self.cbgppeer2type.value_namespace = name_space
                    self.cbgppeer2type.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemoteAddr"):
                    self.cbgppeer2remoteaddr = value
                    self.cbgppeer2remoteaddr.value_namespace = name_space
                    self.cbgppeer2remoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AdminStatus"):
                    self.cbgppeer2adminstatus = value
                    self.cbgppeer2adminstatus.value_namespace = name_space
                    self.cbgppeer2adminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2ConnectRetryInterval"):
                    self.cbgppeer2connectretryinterval = value
                    self.cbgppeer2connectretryinterval.value_namespace = name_space
                    self.cbgppeer2connectretryinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2FsmEstablishedTime"):
                    self.cbgppeer2fsmestablishedtime = value
                    self.cbgppeer2fsmestablishedtime.value_namespace = name_space
                    self.cbgppeer2fsmestablishedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2FsmEstablishedTransitions"):
                    self.cbgppeer2fsmestablishedtransitions = value
                    self.cbgppeer2fsmestablishedtransitions.value_namespace = name_space
                    self.cbgppeer2fsmestablishedtransitions.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2HoldTime"):
                    self.cbgppeer2holdtime = value
                    self.cbgppeer2holdtime.value_namespace = name_space
                    self.cbgppeer2holdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2HoldTimeConfigured"):
                    self.cbgppeer2holdtimeconfigured = value
                    self.cbgppeer2holdtimeconfigured.value_namespace = name_space
                    self.cbgppeer2holdtimeconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2InTotalMessages"):
                    self.cbgppeer2intotalmessages = value
                    self.cbgppeer2intotalmessages.value_namespace = name_space
                    self.cbgppeer2intotalmessages.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2InUpdateElapsedTime"):
                    self.cbgppeer2inupdateelapsedtime = value
                    self.cbgppeer2inupdateelapsedtime.value_namespace = name_space
                    self.cbgppeer2inupdateelapsedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2InUpdates"):
                    self.cbgppeer2inupdates = value
                    self.cbgppeer2inupdates.value_namespace = name_space
                    self.cbgppeer2inupdates.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2KeepAlive"):
                    self.cbgppeer2keepalive = value
                    self.cbgppeer2keepalive.value_namespace = name_space
                    self.cbgppeer2keepalive.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2KeepAliveConfigured"):
                    self.cbgppeer2keepaliveconfigured = value
                    self.cbgppeer2keepaliveconfigured.value_namespace = name_space
                    self.cbgppeer2keepaliveconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2LastError"):
                    self.cbgppeer2lasterror = value
                    self.cbgppeer2lasterror.value_namespace = name_space
                    self.cbgppeer2lasterror.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2LastErrorTxt"):
                    self.cbgppeer2lasterrortxt = value
                    self.cbgppeer2lasterrortxt.value_namespace = name_space
                    self.cbgppeer2lasterrortxt.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2LocalAddr"):
                    self.cbgppeer2localaddr = value
                    self.cbgppeer2localaddr.value_namespace = name_space
                    self.cbgppeer2localaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2LocalAs"):
                    self.cbgppeer2localas = value
                    self.cbgppeer2localas.value_namespace = name_space
                    self.cbgppeer2localas.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2LocalIdentifier"):
                    self.cbgppeer2localidentifier = value
                    self.cbgppeer2localidentifier.value_namespace = name_space
                    self.cbgppeer2localidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2LocalPort"):
                    self.cbgppeer2localport = value
                    self.cbgppeer2localport.value_namespace = name_space
                    self.cbgppeer2localport.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2MinASOriginationInterval"):
                    self.cbgppeer2minasoriginationinterval = value
                    self.cbgppeer2minasoriginationinterval.value_namespace = name_space
                    self.cbgppeer2minasoriginationinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2MinRouteAdvertisementInterval"):
                    self.cbgppeer2minrouteadvertisementinterval = value
                    self.cbgppeer2minrouteadvertisementinterval.value_namespace = name_space
                    self.cbgppeer2minrouteadvertisementinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2NegotiatedVersion"):
                    self.cbgppeer2negotiatedversion = value
                    self.cbgppeer2negotiatedversion.value_namespace = name_space
                    self.cbgppeer2negotiatedversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2OutTotalMessages"):
                    self.cbgppeer2outtotalmessages = value
                    self.cbgppeer2outtotalmessages.value_namespace = name_space
                    self.cbgppeer2outtotalmessages.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2OutUpdates"):
                    self.cbgppeer2outupdates = value
                    self.cbgppeer2outupdates.value_namespace = name_space
                    self.cbgppeer2outupdates.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2PrevState"):
                    self.cbgppeer2prevstate = value
                    self.cbgppeer2prevstate.value_namespace = name_space
                    self.cbgppeer2prevstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemoteAs"):
                    self.cbgppeer2remoteas = value
                    self.cbgppeer2remoteas.value_namespace = name_space
                    self.cbgppeer2remoteas.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemoteIdentifier"):
                    self.cbgppeer2remoteidentifier = value
                    self.cbgppeer2remoteidentifier.value_namespace = name_space
                    self.cbgppeer2remoteidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemotePort"):
                    self.cbgppeer2remoteport = value
                    self.cbgppeer2remoteport.value_namespace = name_space
                    self.cbgppeer2remoteport.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2State"):
                    self.cbgppeer2state = value
                    self.cbgppeer2state.value_namespace = name_space
                    self.cbgppeer2state.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeer2entry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeer2entry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeer2Table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeer2Entry"):
                for c in self.cbgppeer2entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeer2entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeer2Entry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cbgppeer2Capsentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeer2Capstable, self).__init__()

            self.yang_name = "cbgpPeer2CapsTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeer2capsentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeer2Capstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeer2Capstable, self).__setattr__(name, value)


        class Cbgppeer2Capsentry(Entity):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a
            capability is received multiple times with different
            values during a BGP connection establishment,
            corresponding entries are differentiated with indices.
            
            .. attribute:: cbgppeer2type  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2capcode  <key>
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:   :py:class:`Cbgppeer2Capcode <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry.Cbgppeer2Capcode>`
            
            .. attribute:: cbgppeer2capindex  <key>
            
            	Multiple instances of a given capability may be sent by a BGP speaker.  This variable is used to index them
            	**type**\:  int
            
            	**range:** 1..128
            
            .. attribute:: cbgppeer2capvalue
            
            	The value of the announced capability. This MIB object value is organized as given below,     Capability \: Route Refresh Capability                  4\-Byte AS Capability                  Null string     Capability \: Multiprotocol Extensions       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Graceful Restart       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Flags (4 bits)           \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Restart Time in seconds (12 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| ...                              \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Flags for Address Family (8 bits)\|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     Capability \: Additional Paths       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| AFI(16 bits)                     \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| SAFI (8 bits)                    \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \| Send/Receive (8 bits)            \|       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry, self).__init__()

                self.yang_name = "cbgpPeer2CapsEntry"
                self.yang_parent_name = "cbgpPeer2CapsTable"

                self.cbgppeer2type = YLeaf(YType.enumeration, "cbgpPeer2Type")

                self.cbgppeer2remoteaddr = YLeaf(YType.str, "cbgpPeer2RemoteAddr")

                self.cbgppeer2capcode = YLeaf(YType.enumeration, "cbgpPeer2CapCode")

                self.cbgppeer2capindex = YLeaf(YType.uint32, "cbgpPeer2CapIndex")

                self.cbgppeer2capvalue = YLeaf(YType.str, "cbgpPeer2CapValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbgppeer2type",
                                "cbgppeer2remoteaddr",
                                "cbgppeer2capcode",
                                "cbgppeer2capindex",
                                "cbgppeer2capvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry, self).__setattr__(name, value)

            class Cbgppeer2Capcode(Enum):
                """
                Cbgppeer2Capcode

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


            def has_data(self):
                return (
                    self.cbgppeer2type.is_set or
                    self.cbgppeer2remoteaddr.is_set or
                    self.cbgppeer2capcode.is_set or
                    self.cbgppeer2capindex.is_set or
                    self.cbgppeer2capvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbgppeer2type.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeer2capcode.yfilter != YFilter.not_set or
                    self.cbgppeer2capindex.yfilter != YFilter.not_set or
                    self.cbgppeer2capvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeer2CapsEntry" + "[cbgpPeer2Type='" + self.cbgppeer2type.get() + "']" + "[cbgpPeer2RemoteAddr='" + self.cbgppeer2remoteaddr.get() + "']" + "[cbgpPeer2CapCode='" + self.cbgppeer2capcode.get() + "']" + "[cbgpPeer2CapIndex='" + self.cbgppeer2capindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2CapsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbgppeer2type.is_set or self.cbgppeer2type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2type.get_name_leafdata())
                if (self.cbgppeer2remoteaddr.is_set or self.cbgppeer2remoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteaddr.get_name_leafdata())
                if (self.cbgppeer2capcode.is_set or self.cbgppeer2capcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2capcode.get_name_leafdata())
                if (self.cbgppeer2capindex.is_set or self.cbgppeer2capindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2capindex.get_name_leafdata())
                if (self.cbgppeer2capvalue.is_set or self.cbgppeer2capvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2capvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbgpPeer2Type" or name == "cbgpPeer2RemoteAddr" or name == "cbgpPeer2CapCode" or name == "cbgpPeer2CapIndex" or name == "cbgpPeer2CapValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbgpPeer2Type"):
                    self.cbgppeer2type = value
                    self.cbgppeer2type.value_namespace = name_space
                    self.cbgppeer2type.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemoteAddr"):
                    self.cbgppeer2remoteaddr = value
                    self.cbgppeer2remoteaddr.value_namespace = name_space
                    self.cbgppeer2remoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2CapCode"):
                    self.cbgppeer2capcode = value
                    self.cbgppeer2capcode.value_namespace = name_space
                    self.cbgppeer2capcode.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2CapIndex"):
                    self.cbgppeer2capindex = value
                    self.cbgppeer2capindex.value_namespace = name_space
                    self.cbgppeer2capindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2CapValue"):
                    self.cbgppeer2capvalue = value
                    self.cbgppeer2capvalue.value_namespace = name_space
                    self.cbgppeer2capvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeer2capsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeer2capsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeer2CapsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeer2CapsEntry"):
                for c in self.cbgppeer2capsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeer2capsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeer2CapsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cbgppeer2Addrfamilyentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeer2Addrfamilytable, self).__init__()

            self.yang_name = "cbgpPeer2AddrFamilyTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeer2addrfamilyentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeer2Addrfamilytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeer2Addrfamilytable, self).__setattr__(name, value)


        class Cbgppeer2Addrfamilyentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: cbgppeer2type  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2addrfamilyafi  <key>
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeer2addrfamilysafi  <key>
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:   :py:class:`Cbgpsafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.Cbgpsafi>`
            
            .. attribute:: cbgppeer2addrfamilyname
            
            	Implementation specific Address Family name
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry, self).__init__()

                self.yang_name = "cbgpPeer2AddrFamilyEntry"
                self.yang_parent_name = "cbgpPeer2AddrFamilyTable"

                self.cbgppeer2type = YLeaf(YType.enumeration, "cbgpPeer2Type")

                self.cbgppeer2remoteaddr = YLeaf(YType.str, "cbgpPeer2RemoteAddr")

                self.cbgppeer2addrfamilyafi = YLeaf(YType.enumeration, "cbgpPeer2AddrFamilyAfi")

                self.cbgppeer2addrfamilysafi = YLeaf(YType.enumeration, "cbgpPeer2AddrFamilySafi")

                self.cbgppeer2addrfamilyname = YLeaf(YType.str, "cbgpPeer2AddrFamilyName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbgppeer2type",
                                "cbgppeer2remoteaddr",
                                "cbgppeer2addrfamilyafi",
                                "cbgppeer2addrfamilysafi",
                                "cbgppeer2addrfamilyname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cbgppeer2type.is_set or
                    self.cbgppeer2remoteaddr.is_set or
                    self.cbgppeer2addrfamilyafi.is_set or
                    self.cbgppeer2addrfamilysafi.is_set or
                    self.cbgppeer2addrfamilyname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbgppeer2type.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeer2addrfamilyafi.yfilter != YFilter.not_set or
                    self.cbgppeer2addrfamilysafi.yfilter != YFilter.not_set or
                    self.cbgppeer2addrfamilyname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeer2AddrFamilyEntry" + "[cbgpPeer2Type='" + self.cbgppeer2type.get() + "']" + "[cbgpPeer2RemoteAddr='" + self.cbgppeer2remoteaddr.get() + "']" + "[cbgpPeer2AddrFamilyAfi='" + self.cbgppeer2addrfamilyafi.get() + "']" + "[cbgpPeer2AddrFamilySafi='" + self.cbgppeer2addrfamilysafi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2AddrFamilyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbgppeer2type.is_set or self.cbgppeer2type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2type.get_name_leafdata())
                if (self.cbgppeer2remoteaddr.is_set or self.cbgppeer2remoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteaddr.get_name_leafdata())
                if (self.cbgppeer2addrfamilyafi.is_set or self.cbgppeer2addrfamilyafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2addrfamilyafi.get_name_leafdata())
                if (self.cbgppeer2addrfamilysafi.is_set or self.cbgppeer2addrfamilysafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2addrfamilysafi.get_name_leafdata())
                if (self.cbgppeer2addrfamilyname.is_set or self.cbgppeer2addrfamilyname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2addrfamilyname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbgpPeer2Type" or name == "cbgpPeer2RemoteAddr" or name == "cbgpPeer2AddrFamilyAfi" or name == "cbgpPeer2AddrFamilySafi" or name == "cbgpPeer2AddrFamilyName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbgpPeer2Type"):
                    self.cbgppeer2type = value
                    self.cbgppeer2type.value_namespace = name_space
                    self.cbgppeer2type.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemoteAddr"):
                    self.cbgppeer2remoteaddr = value
                    self.cbgppeer2remoteaddr.value_namespace = name_space
                    self.cbgppeer2remoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AddrFamilyAfi"):
                    self.cbgppeer2addrfamilyafi = value
                    self.cbgppeer2addrfamilyafi.value_namespace = name_space
                    self.cbgppeer2addrfamilyafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AddrFamilySafi"):
                    self.cbgppeer2addrfamilysafi = value
                    self.cbgppeer2addrfamilysafi.value_namespace = name_space
                    self.cbgppeer2addrfamilysafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AddrFamilyName"):
                    self.cbgppeer2addrfamilyname = value
                    self.cbgppeer2addrfamilyname.value_namespace = name_space
                    self.cbgppeer2addrfamilyname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeer2addrfamilyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeer2addrfamilyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeer2AddrFamilyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeer2AddrFamilyEntry"):
                for c in self.cbgppeer2addrfamilyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeer2addrfamilyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeer2AddrFamilyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cbgppeer2Addrfamilyprefixentry <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry>`
        
        

        """

        _prefix = 'CISCO-BGP4-MIB'
        _revision = '2010-09-30'

        def __init__(self):
            super(CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable, self).__init__()

            self.yang_name = "cbgpPeer2AddrFamilyPrefixTable"
            self.yang_parent_name = "CISCO-BGP4-MIB"

            self.cbgppeer2addrfamilyprefixentry = YList(self)

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
                        super(CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable, self).__setattr__(name, value)


        class Cbgppeer2Addrfamilyprefixentry(Entity):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated
            with route prefixes belonging to an address family.
            
            .. attribute:: cbgppeer2type  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2addrfamilyafi  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cbgppeer2addrfamilysafi  <key>
            
            	
            	**type**\:   :py:class:`Cbgpsafi <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.Cbgpsafi>`
            
            .. attribute:: cbgppeer2acceptedprefixes
            
            	Number of accepted route prefixes on this connection, which belong to an address family
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2advertisedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is advertised on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2deniedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, received on this connection is denied. It is initialized to zero when the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2prefixadminlimit
            
            	Max number of route prefixes accepted for an address family on this connection
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cbgppeer2prefixclearthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which SNMP clear notification is generated if prefix threshold notification is already generated
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: percent
            
            .. attribute:: cbgppeer2prefixthreshold
            
            	Prefix threshold value (%) for an address family on this connection at which warning message stating the prefix count is crossed the threshold or corresponding SNMP notification is generated
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: percent
            
            .. attribute:: cbgppeer2suppressedprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family is suppressed from being sent on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cbgppeer2withdrawnprefixes
            
            	This counter is incremented when a route prefix, which belongs to an address family, is withdrawn on this connection. It is initialized to zero when the connection is undergone a hard reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                super(CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry, self).__init__()

                self.yang_name = "cbgpPeer2AddrFamilyPrefixEntry"
                self.yang_parent_name = "cbgpPeer2AddrFamilyPrefixTable"

                self.cbgppeer2type = YLeaf(YType.enumeration, "cbgpPeer2Type")

                self.cbgppeer2remoteaddr = YLeaf(YType.str, "cbgpPeer2RemoteAddr")

                self.cbgppeer2addrfamilyafi = YLeaf(YType.enumeration, "cbgpPeer2AddrFamilyAfi")

                self.cbgppeer2addrfamilysafi = YLeaf(YType.enumeration, "cbgpPeer2AddrFamilySafi")

                self.cbgppeer2acceptedprefixes = YLeaf(YType.uint32, "cbgpPeer2AcceptedPrefixes")

                self.cbgppeer2advertisedprefixes = YLeaf(YType.uint32, "cbgpPeer2AdvertisedPrefixes")

                self.cbgppeer2deniedprefixes = YLeaf(YType.uint32, "cbgpPeer2DeniedPrefixes")

                self.cbgppeer2prefixadminlimit = YLeaf(YType.uint32, "cbgpPeer2PrefixAdminLimit")

                self.cbgppeer2prefixclearthreshold = YLeaf(YType.uint32, "cbgpPeer2PrefixClearThreshold")

                self.cbgppeer2prefixthreshold = YLeaf(YType.uint32, "cbgpPeer2PrefixThreshold")

                self.cbgppeer2suppressedprefixes = YLeaf(YType.uint32, "cbgpPeer2SuppressedPrefixes")

                self.cbgppeer2withdrawnprefixes = YLeaf(YType.uint32, "cbgpPeer2WithdrawnPrefixes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cbgppeer2type",
                                "cbgppeer2remoteaddr",
                                "cbgppeer2addrfamilyafi",
                                "cbgppeer2addrfamilysafi",
                                "cbgppeer2acceptedprefixes",
                                "cbgppeer2advertisedprefixes",
                                "cbgppeer2deniedprefixes",
                                "cbgppeer2prefixadminlimit",
                                "cbgppeer2prefixclearthreshold",
                                "cbgppeer2prefixthreshold",
                                "cbgppeer2suppressedprefixes",
                                "cbgppeer2withdrawnprefixes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cbgppeer2type.is_set or
                    self.cbgppeer2remoteaddr.is_set or
                    self.cbgppeer2addrfamilyafi.is_set or
                    self.cbgppeer2addrfamilysafi.is_set or
                    self.cbgppeer2acceptedprefixes.is_set or
                    self.cbgppeer2advertisedprefixes.is_set or
                    self.cbgppeer2deniedprefixes.is_set or
                    self.cbgppeer2prefixadminlimit.is_set or
                    self.cbgppeer2prefixclearthreshold.is_set or
                    self.cbgppeer2prefixthreshold.is_set or
                    self.cbgppeer2suppressedprefixes.is_set or
                    self.cbgppeer2withdrawnprefixes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cbgppeer2type.yfilter != YFilter.not_set or
                    self.cbgppeer2remoteaddr.yfilter != YFilter.not_set or
                    self.cbgppeer2addrfamilyafi.yfilter != YFilter.not_set or
                    self.cbgppeer2addrfamilysafi.yfilter != YFilter.not_set or
                    self.cbgppeer2acceptedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeer2advertisedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeer2deniedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeer2prefixadminlimit.yfilter != YFilter.not_set or
                    self.cbgppeer2prefixclearthreshold.yfilter != YFilter.not_set or
                    self.cbgppeer2prefixthreshold.yfilter != YFilter.not_set or
                    self.cbgppeer2suppressedprefixes.yfilter != YFilter.not_set or
                    self.cbgppeer2withdrawnprefixes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cbgpPeer2AddrFamilyPrefixEntry" + "[cbgpPeer2Type='" + self.cbgppeer2type.get() + "']" + "[cbgpPeer2RemoteAddr='" + self.cbgppeer2remoteaddr.get() + "']" + "[cbgpPeer2AddrFamilyAfi='" + self.cbgppeer2addrfamilyafi.get() + "']" + "[cbgpPeer2AddrFamilySafi='" + self.cbgppeer2addrfamilysafi.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/cbgpPeer2AddrFamilyPrefixTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cbgppeer2type.is_set or self.cbgppeer2type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2type.get_name_leafdata())
                if (self.cbgppeer2remoteaddr.is_set or self.cbgppeer2remoteaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2remoteaddr.get_name_leafdata())
                if (self.cbgppeer2addrfamilyafi.is_set or self.cbgppeer2addrfamilyafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2addrfamilyafi.get_name_leafdata())
                if (self.cbgppeer2addrfamilysafi.is_set or self.cbgppeer2addrfamilysafi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2addrfamilysafi.get_name_leafdata())
                if (self.cbgppeer2acceptedprefixes.is_set or self.cbgppeer2acceptedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2acceptedprefixes.get_name_leafdata())
                if (self.cbgppeer2advertisedprefixes.is_set or self.cbgppeer2advertisedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2advertisedprefixes.get_name_leafdata())
                if (self.cbgppeer2deniedprefixes.is_set or self.cbgppeer2deniedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2deniedprefixes.get_name_leafdata())
                if (self.cbgppeer2prefixadminlimit.is_set or self.cbgppeer2prefixadminlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2prefixadminlimit.get_name_leafdata())
                if (self.cbgppeer2prefixclearthreshold.is_set or self.cbgppeer2prefixclearthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2prefixclearthreshold.get_name_leafdata())
                if (self.cbgppeer2prefixthreshold.is_set or self.cbgppeer2prefixthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2prefixthreshold.get_name_leafdata())
                if (self.cbgppeer2suppressedprefixes.is_set or self.cbgppeer2suppressedprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2suppressedprefixes.get_name_leafdata())
                if (self.cbgppeer2withdrawnprefixes.is_set or self.cbgppeer2withdrawnprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cbgppeer2withdrawnprefixes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cbgpPeer2Type" or name == "cbgpPeer2RemoteAddr" or name == "cbgpPeer2AddrFamilyAfi" or name == "cbgpPeer2AddrFamilySafi" or name == "cbgpPeer2AcceptedPrefixes" or name == "cbgpPeer2AdvertisedPrefixes" or name == "cbgpPeer2DeniedPrefixes" or name == "cbgpPeer2PrefixAdminLimit" or name == "cbgpPeer2PrefixClearThreshold" or name == "cbgpPeer2PrefixThreshold" or name == "cbgpPeer2SuppressedPrefixes" or name == "cbgpPeer2WithdrawnPrefixes"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cbgpPeer2Type"):
                    self.cbgppeer2type = value
                    self.cbgppeer2type.value_namespace = name_space
                    self.cbgppeer2type.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2RemoteAddr"):
                    self.cbgppeer2remoteaddr = value
                    self.cbgppeer2remoteaddr.value_namespace = name_space
                    self.cbgppeer2remoteaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AddrFamilyAfi"):
                    self.cbgppeer2addrfamilyafi = value
                    self.cbgppeer2addrfamilyafi.value_namespace = name_space
                    self.cbgppeer2addrfamilyafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AddrFamilySafi"):
                    self.cbgppeer2addrfamilysafi = value
                    self.cbgppeer2addrfamilysafi.value_namespace = name_space
                    self.cbgppeer2addrfamilysafi.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AcceptedPrefixes"):
                    self.cbgppeer2acceptedprefixes = value
                    self.cbgppeer2acceptedprefixes.value_namespace = name_space
                    self.cbgppeer2acceptedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2AdvertisedPrefixes"):
                    self.cbgppeer2advertisedprefixes = value
                    self.cbgppeer2advertisedprefixes.value_namespace = name_space
                    self.cbgppeer2advertisedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2DeniedPrefixes"):
                    self.cbgppeer2deniedprefixes = value
                    self.cbgppeer2deniedprefixes.value_namespace = name_space
                    self.cbgppeer2deniedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2PrefixAdminLimit"):
                    self.cbgppeer2prefixadminlimit = value
                    self.cbgppeer2prefixadminlimit.value_namespace = name_space
                    self.cbgppeer2prefixadminlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2PrefixClearThreshold"):
                    self.cbgppeer2prefixclearthreshold = value
                    self.cbgppeer2prefixclearthreshold.value_namespace = name_space
                    self.cbgppeer2prefixclearthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2PrefixThreshold"):
                    self.cbgppeer2prefixthreshold = value
                    self.cbgppeer2prefixthreshold.value_namespace = name_space
                    self.cbgppeer2prefixthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2SuppressedPrefixes"):
                    self.cbgppeer2suppressedprefixes = value
                    self.cbgppeer2suppressedprefixes.value_namespace = name_space
                    self.cbgppeer2suppressedprefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "cbgpPeer2WithdrawnPrefixes"):
                    self.cbgppeer2withdrawnprefixes = value
                    self.cbgppeer2withdrawnprefixes.value_namespace = name_space
                    self.cbgppeer2withdrawnprefixes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cbgppeer2addrfamilyprefixentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cbgppeer2addrfamilyprefixentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cbgpPeer2AddrFamilyPrefixTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cbgpPeer2AddrFamilyPrefixEntry"):
                for c in self.cbgppeer2addrfamilyprefixentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cbgppeer2addrfamilyprefixentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cbgpPeer2AddrFamilyPrefixEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cbgpglobal is not None and self.cbgpglobal.has_data()) or
            (self.cbgppeer2addrfamilyprefixtable is not None and self.cbgppeer2addrfamilyprefixtable.has_data()) or
            (self.cbgppeer2addrfamilytable is not None and self.cbgppeer2addrfamilytable.has_data()) or
            (self.cbgppeer2capstable is not None and self.cbgppeer2capstable.has_data()) or
            (self.cbgppeer2table is not None and self.cbgppeer2table.has_data()) or
            (self.cbgppeeraddrfamilyprefixtable is not None and self.cbgppeeraddrfamilyprefixtable.has_data()) or
            (self.cbgppeeraddrfamilytable is not None and self.cbgppeeraddrfamilytable.has_data()) or
            (self.cbgppeercapstable is not None and self.cbgppeercapstable.has_data()) or
            (self.cbgproutetable is not None and self.cbgproutetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cbgpglobal is not None and self.cbgpglobal.has_operation()) or
            (self.cbgppeer2addrfamilyprefixtable is not None and self.cbgppeer2addrfamilyprefixtable.has_operation()) or
            (self.cbgppeer2addrfamilytable is not None and self.cbgppeer2addrfamilytable.has_operation()) or
            (self.cbgppeer2capstable is not None and self.cbgppeer2capstable.has_operation()) or
            (self.cbgppeer2table is not None and self.cbgppeer2table.has_operation()) or
            (self.cbgppeeraddrfamilyprefixtable is not None and self.cbgppeeraddrfamilyprefixtable.has_operation()) or
            (self.cbgppeeraddrfamilytable is not None and self.cbgppeeraddrfamilytable.has_operation()) or
            (self.cbgppeercapstable is not None and self.cbgppeercapstable.has_operation()) or
            (self.cbgproutetable is not None and self.cbgproutetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-BGP4-MIB:CISCO-BGP4-MIB" + path_buffer

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

        if (child_yang_name == "cbgpGlobal"):
            if (self.cbgpglobal is None):
                self.cbgpglobal = CiscoBgp4Mib.Cbgpglobal()
                self.cbgpglobal.parent = self
                self._children_name_map["cbgpglobal"] = "cbgpGlobal"
            return self.cbgpglobal

        if (child_yang_name == "cbgpPeer2AddrFamilyPrefixTable"):
            if (self.cbgppeer2addrfamilyprefixtable is None):
                self.cbgppeer2addrfamilyprefixtable = CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable()
                self.cbgppeer2addrfamilyprefixtable.parent = self
                self._children_name_map["cbgppeer2addrfamilyprefixtable"] = "cbgpPeer2AddrFamilyPrefixTable"
            return self.cbgppeer2addrfamilyprefixtable

        if (child_yang_name == "cbgpPeer2AddrFamilyTable"):
            if (self.cbgppeer2addrfamilytable is None):
                self.cbgppeer2addrfamilytable = CiscoBgp4Mib.Cbgppeer2Addrfamilytable()
                self.cbgppeer2addrfamilytable.parent = self
                self._children_name_map["cbgppeer2addrfamilytable"] = "cbgpPeer2AddrFamilyTable"
            return self.cbgppeer2addrfamilytable

        if (child_yang_name == "cbgpPeer2CapsTable"):
            if (self.cbgppeer2capstable is None):
                self.cbgppeer2capstable = CiscoBgp4Mib.Cbgppeer2Capstable()
                self.cbgppeer2capstable.parent = self
                self._children_name_map["cbgppeer2capstable"] = "cbgpPeer2CapsTable"
            return self.cbgppeer2capstable

        if (child_yang_name == "cbgpPeer2Table"):
            if (self.cbgppeer2table is None):
                self.cbgppeer2table = CiscoBgp4Mib.Cbgppeer2Table()
                self.cbgppeer2table.parent = self
                self._children_name_map["cbgppeer2table"] = "cbgpPeer2Table"
            return self.cbgppeer2table

        if (child_yang_name == "cbgpPeerAddrFamilyPrefixTable"):
            if (self.cbgppeeraddrfamilyprefixtable is None):
                self.cbgppeeraddrfamilyprefixtable = CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable()
                self.cbgppeeraddrfamilyprefixtable.parent = self
                self._children_name_map["cbgppeeraddrfamilyprefixtable"] = "cbgpPeerAddrFamilyPrefixTable"
            return self.cbgppeeraddrfamilyprefixtable

        if (child_yang_name == "cbgpPeerAddrFamilyTable"):
            if (self.cbgppeeraddrfamilytable is None):
                self.cbgppeeraddrfamilytable = CiscoBgp4Mib.Cbgppeeraddrfamilytable()
                self.cbgppeeraddrfamilytable.parent = self
                self._children_name_map["cbgppeeraddrfamilytable"] = "cbgpPeerAddrFamilyTable"
            return self.cbgppeeraddrfamilytable

        if (child_yang_name == "cbgpPeerCapsTable"):
            if (self.cbgppeercapstable is None):
                self.cbgppeercapstable = CiscoBgp4Mib.Cbgppeercapstable()
                self.cbgppeercapstable.parent = self
                self._children_name_map["cbgppeercapstable"] = "cbgpPeerCapsTable"
            return self.cbgppeercapstable

        if (child_yang_name == "cbgpRouteTable"):
            if (self.cbgproutetable is None):
                self.cbgproutetable = CiscoBgp4Mib.Cbgproutetable()
                self.cbgproutetable.parent = self
                self._children_name_map["cbgproutetable"] = "cbgpRouteTable"
            return self.cbgproutetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cbgpGlobal" or name == "cbgpPeer2AddrFamilyPrefixTable" or name == "cbgpPeer2AddrFamilyTable" or name == "cbgpPeer2CapsTable" or name == "cbgpPeer2Table" or name == "cbgpPeerAddrFamilyPrefixTable" or name == "cbgpPeerAddrFamilyTable" or name == "cbgpPeerCapsTable" or name == "cbgpRouteTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoBgp4Mib()
        return self._top_entity

