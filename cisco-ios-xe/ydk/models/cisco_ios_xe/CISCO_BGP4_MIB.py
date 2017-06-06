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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CbgpsafiEnum(Enum):
    """
    CbgpsafiEnum

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

    unicast = 1

    multicast = 2

    unicastAndMulticast = 3

    vpn = 128


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
        return meta._meta_table['CbgpsafiEnum']



class CiscoBgp4Mib(object):
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
        self.cbgpglobal = CiscoBgp4Mib.Cbgpglobal()
        self.cbgpglobal.parent = self
        self.cbgppeer2addrfamilyprefixtable = CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable()
        self.cbgppeer2addrfamilyprefixtable.parent = self
        self.cbgppeer2addrfamilytable = CiscoBgp4Mib.Cbgppeer2Addrfamilytable()
        self.cbgppeer2addrfamilytable.parent = self
        self.cbgppeer2capstable = CiscoBgp4Mib.Cbgppeer2Capstable()
        self.cbgppeer2capstable.parent = self
        self.cbgppeer2table = CiscoBgp4Mib.Cbgppeer2Table()
        self.cbgppeer2table.parent = self
        self.cbgppeeraddrfamilyprefixtable = CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable()
        self.cbgppeeraddrfamilyprefixtable.parent = self
        self.cbgppeeraddrfamilytable = CiscoBgp4Mib.Cbgppeeraddrfamilytable()
        self.cbgppeeraddrfamilytable.parent = self
        self.cbgppeercapstable = CiscoBgp4Mib.Cbgppeercapstable()
        self.cbgppeercapstable.parent = self
        self.cbgproutetable = CiscoBgp4Mib.Cbgproutetable()
        self.cbgproutetable.parent = self


    class Cbgpglobal(object):
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
            self.parent = None
            self.cbgplocalas = None
            self.cbgpnotifsenable = CiscoBgp4Mib.Cbgpglobal.Cbgpnotifsenable()

        class Cbgpnotifsenable(FixedBitsDict):
            """
            Cbgpnotifsenable

            Indicates whether the specific notifications are
            enabled. 
            If notifsEnable(0) bit is set to 1,
            then the notifications defined in
            ciscoBgp4NotificationsGroup1 are enabled; 
            If notifsPeer2Enable(1) bit is set to 1,
            then the notifications defined in
            ciscoBgp4Peer2NotificationsGroup are enabled.
            Keys are:- notifsEnable , notifsPeer2Enable

            """

            def __init__(self):
                self._dictionary = { 
                    'notifsEnable':False,
                    'notifsPeer2Enable':False,
                }
                self._pos_map = { 
                    'notifsEnable':0,
                    'notifsPeer2Enable':1,
                }

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpGlobal'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgplocalas is not None:
                return True

            if self.cbgpnotifsenable is not None:
                if self.cbgpnotifsenable._has_data():
                    return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgpglobal']['meta_info']


    class Cbgproutetable(object):
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
            self.parent = None
            self.cbgprouteentry = YList()
            self.cbgprouteentry.parent = self
            self.cbgprouteentry.name = 'cbgprouteentry'


        class Cbgprouteentry(object):
            """
            Information about a path to a network received from
            a peer.
            
            .. attribute:: cbgprouteafi  <key>
            
            	Represents Address Family Identifier(AFI) of the Network Layer protocol associated with the route. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgproutesafi  <key>
            
            	Represents Subsequent Address Family Identifier(SAFI) of the route. It gives additional information about the type of the route. An implementation is only  required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:   :py:class:`CbgpsafiEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpsafiEnum>`
            
            .. attribute:: cbgproutepeertype  <key>
            
            	Represents the type of Network Layer address stored in cbgpRoutePeer. An implementation is only required to support IPv4 address type(Value \- 1)
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`CbgprouteatomicaggregateEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteatomicaggregateEnum>`
            
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
            	**type**\:   :py:class:`CbgprouteoriginEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteoriginEnum>`
            
            .. attribute:: cbgprouteunknownattr
            
            	One or more path attributes not understood by this BGP4 speaker.  Size zero (0) indicates the absence of such attribute(s).  Octets beyond the maximum size, if any, are not recorded by this object.    Each path attribute is a triple <attribute type, attribute length, attribute value> of variable length. Attribute Type is a two\-octet field that consists of the Attribute Flags octet followed by the Attribute Type Code octet.  If the Extended Length bit of the  Attribute Flags octet is set to 0, the third octet of  the Path Attribute contains the length of the attribute data in octets.  If the Extended Length bit  of the Attribute Flags octet is set to 1, then the third and the fourth octets of the path attribute  contain the length of the attribute data in octets. The remaining octets of the Path Attribute represent  the attribute value and are interpreted according to  the Attribute Flags and the Attribute Type Code
            	**type**\:  str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgprouteafi = None
                self.cbgproutesafi = None
                self.cbgproutepeertype = None
                self.cbgproutepeer = None
                self.cbgprouteaddrprefix = None
                self.cbgprouteaddrprefixlen = None
                self.cbgprouteaggregatoraddr = None
                self.cbgprouteaggregatoraddrtype = None
                self.cbgprouteaggregatoras = None
                self.cbgprouteaspathsegment = None
                self.cbgprouteatomicaggregate = None
                self.cbgproutebest = None
                self.cbgproutelocalpref = None
                self.cbgproutelocalprefpresent = None
                self.cbgproutemedpresent = None
                self.cbgproutemultiexitdisc = None
                self.cbgproutenexthop = None
                self.cbgprouteorigin = None
                self.cbgprouteunknownattr = None

            class CbgprouteatomicaggregateEnum(Enum):
                """
                CbgprouteatomicaggregateEnum

                Whether or not the local system has selected a less

                specific route without selecting a more specific

                route.

                .. data:: lessSpecificRouteNotSelected = 1

                .. data:: lessSpecificRouteSelected = 2

                """

                lessSpecificRouteNotSelected = 1

                lessSpecificRouteSelected = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteatomicaggregateEnum']


            class CbgprouteoriginEnum(Enum):
                """
                CbgprouteoriginEnum

                The ultimate origin of the route information.

                .. data:: igp = 1

                .. data:: egp = 2

                .. data:: incomplete = 3

                """

                igp = 1

                egp = 2

                incomplete = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry.CbgprouteoriginEnum']


            @property
            def _common_path(self):
                if self.cbgprouteafi is None:
                    raise YPYModelError('Key property cbgprouteafi is None')
                if self.cbgproutesafi is None:
                    raise YPYModelError('Key property cbgproutesafi is None')
                if self.cbgproutepeertype is None:
                    raise YPYModelError('Key property cbgproutepeertype is None')
                if self.cbgproutepeer is None:
                    raise YPYModelError('Key property cbgproutepeer is None')
                if self.cbgprouteaddrprefix is None:
                    raise YPYModelError('Key property cbgprouteaddrprefix is None')
                if self.cbgprouteaddrprefixlen is None:
                    raise YPYModelError('Key property cbgprouteaddrprefixlen is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpRouteTable/CISCO-BGP4-MIB:cbgpRouteEntry[CISCO-BGP4-MIB:cbgpRouteAfi = ' + str(self.cbgprouteafi) + '][CISCO-BGP4-MIB:cbgpRouteSafi = ' + str(self.cbgproutesafi) + '][CISCO-BGP4-MIB:cbgpRoutePeerType = ' + str(self.cbgproutepeertype) + '][CISCO-BGP4-MIB:cbgpRoutePeer = ' + str(self.cbgproutepeer) + '][CISCO-BGP4-MIB:cbgpRouteAddrPrefix = ' + str(self.cbgprouteaddrprefix) + '][CISCO-BGP4-MIB:cbgpRouteAddrPrefixLen = ' + str(self.cbgprouteaddrprefixlen) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbgprouteafi is not None:
                    return True

                if self.cbgproutesafi is not None:
                    return True

                if self.cbgproutepeertype is not None:
                    return True

                if self.cbgproutepeer is not None:
                    return True

                if self.cbgprouteaddrprefix is not None:
                    return True

                if self.cbgprouteaddrprefixlen is not None:
                    return True

                if self.cbgprouteaggregatoraddr is not None:
                    return True

                if self.cbgprouteaggregatoraddrtype is not None:
                    return True

                if self.cbgprouteaggregatoras is not None:
                    return True

                if self.cbgprouteaspathsegment is not None:
                    return True

                if self.cbgprouteatomicaggregate is not None:
                    return True

                if self.cbgproutebest is not None:
                    return True

                if self.cbgproutelocalpref is not None:
                    return True

                if self.cbgproutelocalprefpresent is not None:
                    return True

                if self.cbgproutemedpresent is not None:
                    return True

                if self.cbgproutemultiexitdisc is not None:
                    return True

                if self.cbgproutenexthop is not None:
                    return True

                if self.cbgprouteorigin is not None:
                    return True

                if self.cbgprouteunknownattr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgproutetable.Cbgprouteentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgprouteentry is not None:
                for child_ref in self.cbgprouteentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgproutetable']['meta_info']


    class Cbgppeercapstable(object):
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
            self.parent = None
            self.cbgppeercapsentry = YList()
            self.cbgppeercapsentry.parent = self
            self.cbgppeercapsentry.name = 'cbgppeercapsentry'


        class Cbgppeercapsentry(object):
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
            	**type**\:   :py:class:`CbgppeercapcodeEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry.CbgppeercapcodeEnum>`
            
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
                self.parent = None
                self.bgppeerremoteaddr = None
                self.cbgppeercapcode = None
                self.cbgppeercapindex = None
                self.cbgppeercapvalue = None

            class CbgppeercapcodeEnum(Enum):
                """
                CbgppeercapcodeEnum

                The BGP Capability Advertisement Capability Code.

                .. data:: multiProtocol = 1

                .. data:: routeRefresh = 2

                .. data:: gracefulRestart = 64

                .. data:: routeRefreshOld = 128

                """

                multiProtocol = 1

                routeRefresh = 2

                gracefulRestart = 64

                routeRefreshOld = 128


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry.CbgppeercapcodeEnum']


            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYModelError('Key property bgppeerremoteaddr is None')
                if self.cbgppeercapcode is None:
                    raise YPYModelError('Key property cbgppeercapcode is None')
                if self.cbgppeercapindex is None:
                    raise YPYModelError('Key property cbgppeercapindex is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerCapsTable/CISCO-BGP4-MIB:cbgpPeerCapsEntry[CISCO-BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + '][CISCO-BGP4-MIB:cbgpPeerCapCode = ' + str(self.cbgppeercapcode) + '][CISCO-BGP4-MIB:cbgpPeerCapIndex = ' + str(self.cbgppeercapindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.cbgppeercapcode is not None:
                    return True

                if self.cbgppeercapindex is not None:
                    return True

                if self.cbgppeercapvalue is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeercapstable.Cbgppeercapsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerCapsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeercapsentry is not None:
                for child_ref in self.cbgppeercapsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeercapstable']['meta_info']


    class Cbgppeeraddrfamilytable(object):
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
            self.parent = None
            self.cbgppeeraddrfamilyentry = YList()
            self.cbgppeeraddrfamilyentry.parent = self
            self.cbgppeeraddrfamilyentry.name = 'cbgppeeraddrfamilyentry'


        class Cbgppeeraddrfamilyentry(object):
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeeraddrfamilysafi  <key>
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value  \- 1) and VPNv4( Value \- 128) address families
            	**type**\:   :py:class:`CbgpsafiEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpsafiEnum>`
            
            .. attribute:: cbgppeeraddrfamilyname
            
            	Implementation specific Address Family name
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeraddrfamilyname = None

            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYModelError('Key property bgppeerremoteaddr is None')
                if self.cbgppeeraddrfamilyafi is None:
                    raise YPYModelError('Key property cbgppeeraddrfamilyafi is None')
                if self.cbgppeeraddrfamilysafi is None:
                    raise YPYModelError('Key property cbgppeeraddrfamilysafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyTable/CISCO-BGP4-MIB:cbgpPeerAddrFamilyEntry[CISCO-BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilyAfi = ' + str(self.cbgppeeraddrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilySafi = ' + str(self.cbgppeeraddrfamilysafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.cbgppeeraddrfamilyafi is not None:
                    return True

                if self.cbgppeeraddrfamilysafi is not None:
                    return True

                if self.cbgppeeraddrfamilyname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilytable.Cbgppeeraddrfamilyentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeeraddrfamilyentry is not None:
                for child_ref in self.cbgppeeraddrfamilyentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilytable']['meta_info']


    class Cbgppeeraddrfamilyprefixtable(object):
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
            self.parent = None
            self.cbgppeeraddrfamilyprefixentry = YList()
            self.cbgppeeraddrfamilyprefixentry.parent = self
            self.cbgppeeraddrfamilyprefixentry.name = 'cbgppeeraddrfamilyprefixentry'


        class Cbgppeeraddrfamilyprefixentry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated 
            with route prefixes belonging to an address family.
            
            .. attribute:: bgppeerremoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`bgppeerremoteaddr <ydk.models.cisco_ios_xe.BGP4_MIB.Bgp4Mib.Bgppeertable.Bgppeerentry>`
            
            .. attribute:: cbgppeeraddrfamilyafi  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeeraddrfamilysafi  <key>
            
            	
            	**type**\:   :py:class:`CbgpsafiEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpsafiEnum>`
            
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
                self.parent = None
                self.bgppeerremoteaddr = None
                self.cbgppeeraddrfamilyafi = None
                self.cbgppeeraddrfamilysafi = None
                self.cbgppeeracceptedprefixes = None
                self.cbgppeeradvertisedprefixes = None
                self.cbgppeerdeniedprefixes = None
                self.cbgppeerprefixadminlimit = None
                self.cbgppeerprefixclearthreshold = None
                self.cbgppeerprefixthreshold = None
                self.cbgppeersuppressedprefixes = None
                self.cbgppeerwithdrawnprefixes = None

            @property
            def _common_path(self):
                if self.bgppeerremoteaddr is None:
                    raise YPYModelError('Key property bgppeerremoteaddr is None')
                if self.cbgppeeraddrfamilyafi is None:
                    raise YPYModelError('Key property cbgppeeraddrfamilyafi is None')
                if self.cbgppeeraddrfamilysafi is None:
                    raise YPYModelError('Key property cbgppeeraddrfamilysafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyPrefixTable/CISCO-BGP4-MIB:cbgpPeerAddrFamilyPrefixEntry[CISCO-BGP4-MIB:bgpPeerRemoteAddr = ' + str(self.bgppeerremoteaddr) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilyAfi = ' + str(self.cbgppeeraddrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeerAddrFamilySafi = ' + str(self.cbgppeeraddrfamilysafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgppeerremoteaddr is not None:
                    return True

                if self.cbgppeeraddrfamilyafi is not None:
                    return True

                if self.cbgppeeraddrfamilysafi is not None:
                    return True

                if self.cbgppeeracceptedprefixes is not None:
                    return True

                if self.cbgppeeradvertisedprefixes is not None:
                    return True

                if self.cbgppeerdeniedprefixes is not None:
                    return True

                if self.cbgppeerprefixadminlimit is not None:
                    return True

                if self.cbgppeerprefixclearthreshold is not None:
                    return True

                if self.cbgppeerprefixthreshold is not None:
                    return True

                if self.cbgppeersuppressedprefixes is not None:
                    return True

                if self.cbgppeerwithdrawnprefixes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable.Cbgppeeraddrfamilyprefixentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeerAddrFamilyPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeeraddrfamilyprefixentry is not None:
                for child_ref in self.cbgppeeraddrfamilyprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeeraddrfamilyprefixtable']['meta_info']


    class Cbgppeer2Table(object):
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
            self.parent = None
            self.cbgppeer2entry = YList()
            self.cbgppeer2entry.parent = self
            self.cbgppeer2entry.name = 'cbgppeer2entry'


        class Cbgppeer2Entry(object):
            """
            Entry containing information about the
            connection with a BGP peer.
            
            .. attribute:: cbgppeer2type  <key>
            
            	Represents the type of Peer address stored in cbgpPeer2Entry
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	The remote IP address of this entry's BGP peer
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cbgppeer2adminstatus
            
            	The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Manual Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Manual Stop Event to be generated. This parameter can be used to restart BGP peer connections.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:   :py:class:`Cbgppeer2AdminstatusEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2AdminstatusEnum>`
            
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
            	**type**\:   :py:class:`Cbgppeer2PrevstateEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2PrevstateEnum>`
            
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
            	**type**\:   :py:class:`Cbgppeer2StateEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2StateEnum>`
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2adminstatus = None
                self.cbgppeer2connectretryinterval = None
                self.cbgppeer2fsmestablishedtime = None
                self.cbgppeer2fsmestablishedtransitions = None
                self.cbgppeer2holdtime = None
                self.cbgppeer2holdtimeconfigured = None
                self.cbgppeer2intotalmessages = None
                self.cbgppeer2inupdateelapsedtime = None
                self.cbgppeer2inupdates = None
                self.cbgppeer2keepalive = None
                self.cbgppeer2keepaliveconfigured = None
                self.cbgppeer2lasterror = None
                self.cbgppeer2lasterrortxt = None
                self.cbgppeer2localaddr = None
                self.cbgppeer2localas = None
                self.cbgppeer2localidentifier = None
                self.cbgppeer2localport = None
                self.cbgppeer2minasoriginationinterval = None
                self.cbgppeer2minrouteadvertisementinterval = None
                self.cbgppeer2negotiatedversion = None
                self.cbgppeer2outtotalmessages = None
                self.cbgppeer2outupdates = None
                self.cbgppeer2prevstate = None
                self.cbgppeer2remoteas = None
                self.cbgppeer2remoteidentifier = None
                self.cbgppeer2remoteport = None
                self.cbgppeer2state = None

            class Cbgppeer2AdminstatusEnum(Enum):
                """
                Cbgppeer2AdminstatusEnum

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

                stop = 1

                start = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2AdminstatusEnum']


            class Cbgppeer2PrevstateEnum(Enum):
                """
                Cbgppeer2PrevstateEnum

                The BGP peer connection previous state.

                .. data:: none = 0

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                none = 0

                idle = 1

                connect = 2

                active = 3

                opensent = 4

                openconfirm = 5

                established = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2PrevstateEnum']


            class Cbgppeer2StateEnum(Enum):
                """
                Cbgppeer2StateEnum

                The BGP peer connection state.

                .. data:: idle = 1

                .. data:: connect = 2

                .. data:: active = 3

                .. data:: opensent = 4

                .. data:: openconfirm = 5

                .. data:: established = 6

                """

                idle = 1

                connect = 2

                active = 3

                opensent = 4

                openconfirm = 5

                established = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry.Cbgppeer2StateEnum']


            @property
            def _common_path(self):
                if self.cbgppeer2type is None:
                    raise YPYModelError('Key property cbgppeer2type is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYModelError('Key property cbgppeer2remoteaddr is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2Table/CISCO-BGP4-MIB:cbgpPeer2Entry[CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2adminstatus is not None:
                    return True

                if self.cbgppeer2connectretryinterval is not None:
                    return True

                if self.cbgppeer2fsmestablishedtime is not None:
                    return True

                if self.cbgppeer2fsmestablishedtransitions is not None:
                    return True

                if self.cbgppeer2holdtime is not None:
                    return True

                if self.cbgppeer2holdtimeconfigured is not None:
                    return True

                if self.cbgppeer2intotalmessages is not None:
                    return True

                if self.cbgppeer2inupdateelapsedtime is not None:
                    return True

                if self.cbgppeer2inupdates is not None:
                    return True

                if self.cbgppeer2keepalive is not None:
                    return True

                if self.cbgppeer2keepaliveconfigured is not None:
                    return True

                if self.cbgppeer2lasterror is not None:
                    return True

                if self.cbgppeer2lasterrortxt is not None:
                    return True

                if self.cbgppeer2localaddr is not None:
                    return True

                if self.cbgppeer2localas is not None:
                    return True

                if self.cbgppeer2localidentifier is not None:
                    return True

                if self.cbgppeer2localport is not None:
                    return True

                if self.cbgppeer2minasoriginationinterval is not None:
                    return True

                if self.cbgppeer2minrouteadvertisementinterval is not None:
                    return True

                if self.cbgppeer2negotiatedversion is not None:
                    return True

                if self.cbgppeer2outtotalmessages is not None:
                    return True

                if self.cbgppeer2outupdates is not None:
                    return True

                if self.cbgppeer2prevstate is not None:
                    return True

                if self.cbgppeer2remoteas is not None:
                    return True

                if self.cbgppeer2remoteidentifier is not None:
                    return True

                if self.cbgppeer2remoteport is not None:
                    return True

                if self.cbgppeer2state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2Table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeer2entry is not None:
                for child_ref in self.cbgppeer2entry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Table']['meta_info']


    class Cbgppeer2Capstable(object):
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
            self.parent = None
            self.cbgppeer2capsentry = YList()
            self.cbgppeer2capsentry.parent = self
            self.cbgppeer2capsentry.name = 'cbgppeer2capsentry'


        class Cbgppeer2Capsentry(object):
            """
            Each entry represents a capability received from a
            peer with a particular code and an index. When a
            capability is received multiple times with different
            values during a BGP connection establishment,
            corresponding entries are differentiated with indices.
            
            .. attribute:: cbgppeer2type  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2capcode  <key>
            
            	The BGP Capability Advertisement Capability Code
            	**type**\:   :py:class:`Cbgppeer2CapcodeEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry.Cbgppeer2CapcodeEnum>`
            
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
                self.parent = None
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2capcode = None
                self.cbgppeer2capindex = None
                self.cbgppeer2capvalue = None

            class Cbgppeer2CapcodeEnum(Enum):
                """
                Cbgppeer2CapcodeEnum

                The BGP Capability Advertisement Capability Code.

                .. data:: multiProtocol = 1

                .. data:: routeRefresh = 2

                .. data:: gracefulRestart = 64

                .. data:: fourByteAs = 65

                .. data:: addPath = 69

                .. data:: routeRefreshOld = 128

                """

                multiProtocol = 1

                routeRefresh = 2

                gracefulRestart = 64

                fourByteAs = 65

                addPath = 69

                routeRefreshOld = 128


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                    return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry.Cbgppeer2CapcodeEnum']


            @property
            def _common_path(self):
                if self.cbgppeer2type is None:
                    raise YPYModelError('Key property cbgppeer2type is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYModelError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2capcode is None:
                    raise YPYModelError('Key property cbgppeer2capcode is None')
                if self.cbgppeer2capindex is None:
                    raise YPYModelError('Key property cbgppeer2capindex is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2CapsTable/CISCO-BGP4-MIB:cbgpPeer2CapsEntry[CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2CapCode = ' + str(self.cbgppeer2capcode) + '][CISCO-BGP4-MIB:cbgpPeer2CapIndex = ' + str(self.cbgppeer2capindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2capcode is not None:
                    return True

                if self.cbgppeer2capindex is not None:
                    return True

                if self.cbgppeer2capvalue is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Capstable.Cbgppeer2Capsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2CapsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeer2capsentry is not None:
                for child_ref in self.cbgppeer2capsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Capstable']['meta_info']


    class Cbgppeer2Addrfamilytable(object):
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
            self.parent = None
            self.cbgppeer2addrfamilyentry = YList()
            self.cbgppeer2addrfamilyentry.parent = self
            self.cbgppeer2addrfamilyentry.name = 'cbgppeer2addrfamilyentry'


        class Cbgppeer2Addrfamilyentry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains names associated with
            an address family.
            
            .. attribute:: cbgppeer2type  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2addrfamilyafi  <key>
            
            	The AFI index of the entry. An implementation is only required to support IPv4 unicast and VPNv4 (Value \- 1) address families
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeer2addrfamilysafi  <key>
            
            	The SAFI index of the entry. An implementation is only required to support IPv4 unicast(Value \- 1) and VPNv4( Value \- 128) address families
            	**type**\:   :py:class:`CbgpsafiEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpsafiEnum>`
            
            .. attribute:: cbgppeer2addrfamilyname
            
            	Implementation specific Address Family name
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-BGP4-MIB'
            _revision = '2010-09-30'

            def __init__(self):
                self.parent = None
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2addrfamilyname = None

            @property
            def _common_path(self):
                if self.cbgppeer2type is None:
                    raise YPYModelError('Key property cbgppeer2type is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYModelError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2addrfamilyafi is None:
                    raise YPYModelError('Key property cbgppeer2addrfamilyafi is None')
                if self.cbgppeer2addrfamilysafi is None:
                    raise YPYModelError('Key property cbgppeer2addrfamilysafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyTable/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyEntry[CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2AddrFamilyAfi = ' + str(self.cbgppeer2addrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeer2AddrFamilySafi = ' + str(self.cbgppeer2addrfamilysafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2addrfamilyafi is not None:
                    return True

                if self.cbgppeer2addrfamilysafi is not None:
                    return True

                if self.cbgppeer2addrfamilyname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilytable.Cbgppeer2Addrfamilyentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeer2addrfamilyentry is not None:
                for child_ref in self.cbgppeer2addrfamilyentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilytable']['meta_info']


    class Cbgppeer2Addrfamilyprefixtable(object):
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
            self.parent = None
            self.cbgppeer2addrfamilyprefixentry = YList()
            self.cbgppeer2addrfamilyprefixentry.parent = self
            self.cbgppeer2addrfamilyprefixentry.name = 'cbgppeer2addrfamilyprefixentry'


        class Cbgppeer2Addrfamilyprefixentry(object):
            """
            An entry is identified by an AFI/SAFI pair and
            peer address. It contains information associated
            with route prefixes belonging to an address family.
            
            .. attribute:: cbgppeer2type  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeer2remoteaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cbgppeer2remoteaddr <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CiscoBgp4Mib.Cbgppeer2Table.Cbgppeer2Entry>`
            
            .. attribute:: cbgppeer2addrfamilyafi  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cbgppeer2addrfamilysafi  <key>
            
            	
            	**type**\:   :py:class:`CbgpsafiEnum <ydk.models.cisco_ios_xe.CISCO_BGP4_MIB.CbgpsafiEnum>`
            
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
                self.parent = None
                self.cbgppeer2type = None
                self.cbgppeer2remoteaddr = None
                self.cbgppeer2addrfamilyafi = None
                self.cbgppeer2addrfamilysafi = None
                self.cbgppeer2acceptedprefixes = None
                self.cbgppeer2advertisedprefixes = None
                self.cbgppeer2deniedprefixes = None
                self.cbgppeer2prefixadminlimit = None
                self.cbgppeer2prefixclearthreshold = None
                self.cbgppeer2prefixthreshold = None
                self.cbgppeer2suppressedprefixes = None
                self.cbgppeer2withdrawnprefixes = None

            @property
            def _common_path(self):
                if self.cbgppeer2type is None:
                    raise YPYModelError('Key property cbgppeer2type is None')
                if self.cbgppeer2remoteaddr is None:
                    raise YPYModelError('Key property cbgppeer2remoteaddr is None')
                if self.cbgppeer2addrfamilyafi is None:
                    raise YPYModelError('Key property cbgppeer2addrfamilyafi is None')
                if self.cbgppeer2addrfamilysafi is None:
                    raise YPYModelError('Key property cbgppeer2addrfamilysafi is None')

                return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyPrefixTable/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyPrefixEntry[CISCO-BGP4-MIB:cbgpPeer2Type = ' + str(self.cbgppeer2type) + '][CISCO-BGP4-MIB:cbgpPeer2RemoteAddr = ' + str(self.cbgppeer2remoteaddr) + '][CISCO-BGP4-MIB:cbgpPeer2AddrFamilyAfi = ' + str(self.cbgppeer2addrfamilyafi) + '][CISCO-BGP4-MIB:cbgpPeer2AddrFamilySafi = ' + str(self.cbgppeer2addrfamilysafi) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cbgppeer2type is not None:
                    return True

                if self.cbgppeer2remoteaddr is not None:
                    return True

                if self.cbgppeer2addrfamilyafi is not None:
                    return True

                if self.cbgppeer2addrfamilysafi is not None:
                    return True

                if self.cbgppeer2acceptedprefixes is not None:
                    return True

                if self.cbgppeer2advertisedprefixes is not None:
                    return True

                if self.cbgppeer2deniedprefixes is not None:
                    return True

                if self.cbgppeer2prefixadminlimit is not None:
                    return True

                if self.cbgppeer2prefixclearthreshold is not None:
                    return True

                if self.cbgppeer2prefixthreshold is not None:
                    return True

                if self.cbgppeer2suppressedprefixes is not None:
                    return True

                if self.cbgppeer2withdrawnprefixes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
                return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable.Cbgppeer2Addrfamilyprefixentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB/CISCO-BGP4-MIB:cbgpPeer2AddrFamilyPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cbgppeer2addrfamilyprefixentry is not None:
                for child_ref in self.cbgppeer2addrfamilyprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
            return meta._meta_table['CiscoBgp4Mib.Cbgppeer2Addrfamilyprefixtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-BGP4-MIB:CISCO-BGP4-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cbgpglobal is not None and self.cbgpglobal._has_data():
            return True

        if self.cbgppeer2addrfamilyprefixtable is not None and self.cbgppeer2addrfamilyprefixtable._has_data():
            return True

        if self.cbgppeer2addrfamilytable is not None and self.cbgppeer2addrfamilytable._has_data():
            return True

        if self.cbgppeer2capstable is not None and self.cbgppeer2capstable._has_data():
            return True

        if self.cbgppeer2table is not None and self.cbgppeer2table._has_data():
            return True

        if self.cbgppeeraddrfamilyprefixtable is not None and self.cbgppeeraddrfamilyprefixtable._has_data():
            return True

        if self.cbgppeeraddrfamilytable is not None and self.cbgppeeraddrfamilytable._has_data():
            return True

        if self.cbgppeercapstable is not None and self.cbgppeercapstable._has_data():
            return True

        if self.cbgproutetable is not None and self.cbgproutetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_BGP4_MIB as meta
        return meta._meta_table['CiscoBgp4Mib']['meta_info']


