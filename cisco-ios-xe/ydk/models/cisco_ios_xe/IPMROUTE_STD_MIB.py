""" IPMROUTE_STD_MIB 

The MIB module for management of IP Multicast routing, but
independent of the specific multicast routing protocol in
use.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IPMROUTESTDMIB(Entity):
    """
    
    
    .. attribute:: ipmroute
    
    	
    	**type**\:  :py:class:`Ipmroute <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroute>`
    
    .. attribute:: ipmroutetable
    
    	The (conceptual) table containing multicast routing information for IP datagrams sent by particular sources to the IP multicast groups known to this router
    	**type**\:  :py:class:`Ipmroutetable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutetable>`
    
    .. attribute:: ipmroutenexthoptable
    
    	The (conceptual) table containing information on the next\- hops on outgoing interfaces for routing IP multicast datagrams.  Each entry is one of a list of next\-hops on outgoing interfaces for particular sources sending to a particular multicast group address
    	**type**\:  :py:class:`Ipmroutenexthoptable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutenexthoptable>`
    
    .. attribute:: ipmrouteinterfacetable
    
    	The (conceptual) table containing multicast routing information specific to interfaces
    	**type**\:  :py:class:`Ipmrouteinterfacetable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmrouteinterfacetable>`
    
    .. attribute:: ipmrouteboundarytable
    
    	The (conceptual) table listing the router's scoped multicast address boundaries
    	**type**\:  :py:class:`Ipmrouteboundarytable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmrouteboundarytable>`
    
    .. attribute:: ipmroutescopenametable
    
    	The (conceptual) table listing the multicast scope names
    	**type**\:  :py:class:`Ipmroutescopenametable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutescopenametable>`
    
    

    """

    _prefix = 'IPMROUTE-STD-MIB'
    _revision = '2000-09-22'

    def __init__(self):
        super(IPMROUTESTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "IPMROUTE-STD-MIB"
        self.yang_parent_name = "IPMROUTE-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ipMRoute", ("ipmroute", IPMROUTESTDMIB.Ipmroute)), ("ipMRouteTable", ("ipmroutetable", IPMROUTESTDMIB.Ipmroutetable)), ("ipMRouteNextHopTable", ("ipmroutenexthoptable", IPMROUTESTDMIB.Ipmroutenexthoptable)), ("ipMRouteInterfaceTable", ("ipmrouteinterfacetable", IPMROUTESTDMIB.Ipmrouteinterfacetable)), ("ipMRouteBoundaryTable", ("ipmrouteboundarytable", IPMROUTESTDMIB.Ipmrouteboundarytable)), ("ipMRouteScopeNameTable", ("ipmroutescopenametable", IPMROUTESTDMIB.Ipmroutescopenametable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ipmroute = IPMROUTESTDMIB.Ipmroute()
        self.ipmroute.parent = self
        self._children_name_map["ipmroute"] = "ipMRoute"
        self._children_yang_names.add("ipMRoute")

        self.ipmroutetable = IPMROUTESTDMIB.Ipmroutetable()
        self.ipmroutetable.parent = self
        self._children_name_map["ipmroutetable"] = "ipMRouteTable"
        self._children_yang_names.add("ipMRouteTable")

        self.ipmroutenexthoptable = IPMROUTESTDMIB.Ipmroutenexthoptable()
        self.ipmroutenexthoptable.parent = self
        self._children_name_map["ipmroutenexthoptable"] = "ipMRouteNextHopTable"
        self._children_yang_names.add("ipMRouteNextHopTable")

        self.ipmrouteinterfacetable = IPMROUTESTDMIB.Ipmrouteinterfacetable()
        self.ipmrouteinterfacetable.parent = self
        self._children_name_map["ipmrouteinterfacetable"] = "ipMRouteInterfaceTable"
        self._children_yang_names.add("ipMRouteInterfaceTable")

        self.ipmrouteboundarytable = IPMROUTESTDMIB.Ipmrouteboundarytable()
        self.ipmrouteboundarytable.parent = self
        self._children_name_map["ipmrouteboundarytable"] = "ipMRouteBoundaryTable"
        self._children_yang_names.add("ipMRouteBoundaryTable")

        self.ipmroutescopenametable = IPMROUTESTDMIB.Ipmroutescopenametable()
        self.ipmroutescopenametable.parent = self
        self._children_name_map["ipmroutescopenametable"] = "ipMRouteScopeNameTable"
        self._children_yang_names.add("ipMRouteScopeNameTable")
        self._segment_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB"


    class Ipmroute(Entity):
        """
        
        
        .. attribute:: ipmrouteenable
        
        	The enabled status of IP Multicast routing on this router
        	**type**\:  :py:class:`Ipmrouteenable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroute.Ipmrouteenable>`
        
        .. attribute:: ipmrouteentrycount
        
        	The number of rows in the ipMRouteTable.  This can be used to monitor the multicast routing table size
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IPMROUTESTDMIB.Ipmroute, self).__init__()

            self.yang_name = "ipMRoute"
            self.yang_parent_name = "IPMROUTE-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ipmrouteenable', YLeaf(YType.enumeration, 'ipMRouteEnable')),
                ('ipmrouteentrycount', YLeaf(YType.uint32, 'ipMRouteEntryCount')),
            ])
            self.ipmrouteenable = None
            self.ipmrouteentrycount = None
            self._segment_path = lambda: "ipMRoute"
            self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMROUTESTDMIB.Ipmroute, ['ipmrouteenable', 'ipmrouteentrycount'], name, value)

        class Ipmrouteenable(Enum):
            """
            Ipmrouteenable (Enum Class)

            The enabled status of IP Multicast routing on this router.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")



    class Ipmroutetable(Entity):
        """
        The (conceptual) table containing multicast routing
        information for IP datagrams sent by particular sources to
        the IP multicast groups known to this router.
        
        .. attribute:: ipmrouteentry
        
        	An entry (conceptual row) containing the multicast routing information for IP datagrams from a particular source and addressed to a particular IP multicast group address. Discontinuities in counters in this entry can be detected by observing the value of ipMRouteUpTime
        	**type**\: list of  		 :py:class:`Ipmrouteentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutetable.Ipmrouteentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IPMROUTESTDMIB.Ipmroutetable, self).__init__()

            self.yang_name = "ipMRouteTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipMRouteEntry", ("ipmrouteentry", IPMROUTESTDMIB.Ipmroutetable.Ipmrouteentry))])
            self._leafs = OrderedDict()

            self.ipmrouteentry = YList(self)
            self._segment_path = lambda: "ipMRouteTable"
            self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMROUTESTDMIB.Ipmroutetable, [], name, value)


        class Ipmrouteentry(Entity):
            """
            An entry (conceptual row) containing the multicast routing
            information for IP datagrams from a particular source and
            addressed to a particular IP multicast group address.
            Discontinuities in counters in this entry can be detected by
            observing the value of ipMRouteUpTime.
            
            .. attribute:: ipmroutegroup  (key)
            
            	The IP multicast group address for which this entry contains multicast routing information
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutesource  (key)
            
            	The network address which when combined with the corresponding value of ipMRouteSourceMask identifies the sources for which this entry contains multicast routing information
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutesourcemask  (key)
            
            	The network mask which when combined with the corresponding value of ipMRouteSource identifies the sources for which this entry contains multicast routing information
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteupstreamneighbor
            
            	The address of the upstream neighbor (e.g., RPF neighbor) from which IP datagrams from these sources to this multicast address are received, or 0.0.0.0 if the upstream neighbor is unknown (e.g., in CBT)
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteinifindex
            
            	The value of ifIndex for the interface on which IP datagrams sent by these sources to this multicast address are received.  A value of 0 indicates that datagrams are not subject to an incoming interface check, but may be accepted on multiple interfaces (e.g., in CBT)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ipmrouteuptime
            
            	The time since the multicast routing information represented by this entry was learned by the router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  The value 0 indicates that the entry is not subject to aging
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutepkts
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutedifferentinifpackets
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address, which were dropped because they were not received on the interface indicated by ipMRouteInIfIndex.  Packets which are not subject to an incoming interface check (e.g., using CBT) are not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteoctets
            
            	The number of octets contained in IP datagrams which were received from these sources and addressed to this multicast group address, and which were forwarded by this router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteprotocol
            
            	The multicast routing protocol via which this multicast forwarding entry was learned
            	**type**\:  :py:class:`IANAipMRouteProtocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IANAipMRouteProtocol>`
            
            .. attribute:: ipmroutertproto
            
            	The routing mechanism via which the route used to find the upstream or parent interface for this multicast forwarding entry was learned.  Inclusion of values for routing protocols is not intended to imply that those protocols need be supported
            	**type**\:  :py:class:`IANAipRouteProtocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IANAipRouteProtocol>`
            
            .. attribute:: ipmroutertaddress
            
            	The address portion of the route used to find the upstream or parent interface for this multicast forwarding entry
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutertmask
            
            	The mask associated with the route used to find the upstream or parent interface for this multicast forwarding entry
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouterttype
            
            	The reason the given route was placed in the (logical) multicast Routing Information Base (RIB).  A value of unicast means that the route would normally be placed only in the unicast RIB, but was placed in the multicast RIB (instead or in addition) due to local configuration, such as when running PIM over RIP.  A value of multicast means that      the route was explicitly added to the multicast RIB by the routing protocol, such as DVMRP or Multiprotocol BGP
            	**type**\:  :py:class:`Ipmrouterttype <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutetable.Ipmrouteentry.Ipmrouterttype>`
            
            .. attribute:: ipmroutehcoctets
            
            	The number of octets contained in IP datagrams which were received from these sources and addressed to this multicast group address, and which were forwarded by this router. This object is a 64\-bit version of ipMRouteOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmroutepruneflag
            
            	Boolean, indicates whether this route is pruned. A pruned route is one that has an empty outgoing interface list or all interfaces are in Pruned state. A multicast packet that matches a pruned route doesn't get forwarded
            	**type**\: bool
            
            .. attribute:: ciscoipmroutesparseflag
            
            	Boolean, indicating PIM multicast routing protocol sparse\-mode (versus dense\-mode).  In sparse\-mode, packets are forwarded only out interfaces that have been joined. In dense\-mode, they are forwarded out all interfaces that have not been pruned
            	**type**\: bool
            
            .. attribute:: ciscoipmrouteconnectedflag
            
            	Boolean, indicating whether there is a directly connected member for a group attached to the router
            	**type**\: bool
            
            .. attribute:: ciscoipmroutelocalflag
            
            	Boolean, indicating whether local system is a member of a group on any interface
            	**type**\: bool
            
            .. attribute:: ciscoipmrouteregisterflag
            
            	Boolean, indicates whether to send registers for the entry. A first hop router directly connected to a multicast source host, as well as a border router on the boundary of two domains running different multicast routing protocols, encapsulates packets to be sent on the shared tree. This is done until the RP sends Joins back to this router
            	**type**\: bool
            
            .. attribute:: ciscoipmrouterpflag
            
            	Boolean, indicating whether there is a Prune state for this source along the shared tree
            	**type**\: bool
            
            .. attribute:: ciscoipmroutesptflag
            
            	Boolean, indicating whether data is being received on the SPT tree, ie the Shortest Path Tree
            	**type**\: bool
            
            .. attribute:: ciscoipmroutebps
            
            	Bits per second forwarded by this router.  This is the sum of all forwarded bits during a 1 second interval.  At the end of each second the field is cleared. This object has been superseded by ciscoIpMRouteBps2 (which is the 64\-bit version of this object)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ciscoipmroutemetric
            
            	Metric \- The best metric heard from Assert messages. This object has been replaced by ciscoIpMRouteMetric2 in order to correctly represent a 32\-bit unsigned metric value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ciscoipmroutemetricpreference
            
            	Metric Preference \- The best metric preference heard from Assert messages
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoipmrouteinlimit
            
            	Incoming interface's limit for rate limiting data traffic, in Kbps. Replaced by ciscoIpMRouteInLimit2
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: Kbits/second
            
            	**status**\: obsolete
            
            .. attribute:: ciscoipmroutelastused
            
            	How long has it been since the last multicast packet was fastswitched
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteinlimit2
            
            	Incoming interface's limit for rate limiting data traffic, in Kbps
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Kbits/second
            
            .. attribute:: ciscoipmroutejoinflag
            
            	Boolean, indicates whether this route is created due to SPT threshold
            	**type**\: bool
            
            .. attribute:: ciscoipmroutemsdpflag
            
            	Boolean, indicates whether this route is learned via MSDP
            	**type**\: bool
            
            .. attribute:: ciscoipmrouteproxyjoinflag
            
            	Boolean, indicates whether to send join for this entry
            	**type**\: bool
            
            .. attribute:: ciscoipmroutepkts
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address. This object is a 64\-bit version of ipMRoutePkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmroutedifferentinifpkts
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address, which were not received from the interface indicated by ipMRouteInIfIndex. This object is a 64\-bit version of ipMRouteDifferentInIfPackets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteoctets
            
            	The number of octets contained in IP datagrams which were received from these sources and addressed to this multicast group address, and which were forwarded by this router. This object is a 64\-bit version of ipMRouteOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmroutebps2
            
            	Bits per second forwarded by this router. This is the sum of all forwarded bits during a 1 second interval. At the end of each second the field is cleared
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmroutemetric2
            
            	Metric \- The best metric heard from Assert messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IPMROUTESTDMIB.Ipmroutetable.Ipmrouteentry, self).__init__()

                self.yang_name = "ipMRouteEntry"
                self.yang_parent_name = "ipMRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmroutegroup','ipmroutesource','ipmroutesourcemask']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmroutegroup', YLeaf(YType.str, 'ipMRouteGroup')),
                    ('ipmroutesource', YLeaf(YType.str, 'ipMRouteSource')),
                    ('ipmroutesourcemask', YLeaf(YType.str, 'ipMRouteSourceMask')),
                    ('ipmrouteupstreamneighbor', YLeaf(YType.str, 'ipMRouteUpstreamNeighbor')),
                    ('ipmrouteinifindex', YLeaf(YType.int32, 'ipMRouteInIfIndex')),
                    ('ipmrouteuptime', YLeaf(YType.uint32, 'ipMRouteUpTime')),
                    ('ipmrouteexpirytime', YLeaf(YType.uint32, 'ipMRouteExpiryTime')),
                    ('ipmroutepkts', YLeaf(YType.uint32, 'ipMRoutePkts')),
                    ('ipmroutedifferentinifpackets', YLeaf(YType.uint32, 'ipMRouteDifferentInIfPackets')),
                    ('ipmrouteoctets', YLeaf(YType.uint32, 'ipMRouteOctets')),
                    ('ipmrouteprotocol', YLeaf(YType.enumeration, 'ipMRouteProtocol')),
                    ('ipmroutertproto', YLeaf(YType.enumeration, 'ipMRouteRtProto')),
                    ('ipmroutertaddress', YLeaf(YType.str, 'ipMRouteRtAddress')),
                    ('ipmroutertmask', YLeaf(YType.str, 'ipMRouteRtMask')),
                    ('ipmrouterttype', YLeaf(YType.enumeration, 'ipMRouteRtType')),
                    ('ipmroutehcoctets', YLeaf(YType.uint64, 'ipMRouteHCOctets')),
                    ('ciscoipmroutepruneflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRoutePruneFlag')),
                    ('ciscoipmroutesparseflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteSparseFlag')),
                    ('ciscoipmrouteconnectedflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteConnectedFlag')),
                    ('ciscoipmroutelocalflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteLocalFlag')),
                    ('ciscoipmrouteregisterflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteRegisterFlag')),
                    ('ciscoipmrouterpflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteRpFlag')),
                    ('ciscoipmroutesptflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteSptFlag')),
                    ('ciscoipmroutebps', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteBps')),
                    ('ciscoipmroutemetric', YLeaf(YType.int32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteMetric')),
                    ('ciscoipmroutemetricpreference', YLeaf(YType.int32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteMetricPreference')),
                    ('ciscoipmrouteinlimit', YLeaf(YType.int32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteInLimit')),
                    ('ciscoipmroutelastused', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteLastUsed')),
                    ('ciscoipmrouteinlimit2', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteInLimit2')),
                    ('ciscoipmroutejoinflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteJoinFlag')),
                    ('ciscoipmroutemsdpflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteMsdpFlag')),
                    ('ciscoipmrouteproxyjoinflag', YLeaf(YType.boolean, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteProxyJoinFlag')),
                    ('ciscoipmroutepkts', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRoutePkts')),
                    ('ciscoipmroutedifferentinifpkts', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteDifferentInIfPkts')),
                    ('ciscoipmrouteoctets', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteOctets')),
                    ('ciscoipmroutebps2', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteBps2')),
                    ('ciscoipmroutemetric2', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteMetric2')),
                ])
                self.ipmroutegroup = None
                self.ipmroutesource = None
                self.ipmroutesourcemask = None
                self.ipmrouteupstreamneighbor = None
                self.ipmrouteinifindex = None
                self.ipmrouteuptime = None
                self.ipmrouteexpirytime = None
                self.ipmroutepkts = None
                self.ipmroutedifferentinifpackets = None
                self.ipmrouteoctets = None
                self.ipmrouteprotocol = None
                self.ipmroutertproto = None
                self.ipmroutertaddress = None
                self.ipmroutertmask = None
                self.ipmrouterttype = None
                self.ipmroutehcoctets = None
                self.ciscoipmroutepruneflag = None
                self.ciscoipmroutesparseflag = None
                self.ciscoipmrouteconnectedflag = None
                self.ciscoipmroutelocalflag = None
                self.ciscoipmrouteregisterflag = None
                self.ciscoipmrouterpflag = None
                self.ciscoipmroutesptflag = None
                self.ciscoipmroutebps = None
                self.ciscoipmroutemetric = None
                self.ciscoipmroutemetricpreference = None
                self.ciscoipmrouteinlimit = None
                self.ciscoipmroutelastused = None
                self.ciscoipmrouteinlimit2 = None
                self.ciscoipmroutejoinflag = None
                self.ciscoipmroutemsdpflag = None
                self.ciscoipmrouteproxyjoinflag = None
                self.ciscoipmroutepkts = None
                self.ciscoipmroutedifferentinifpkts = None
                self.ciscoipmrouteoctets = None
                self.ciscoipmroutebps2 = None
                self.ciscoipmroutemetric2 = None
                self._segment_path = lambda: "ipMRouteEntry" + "[ipMRouteGroup='" + str(self.ipmroutegroup) + "']" + "[ipMRouteSource='" + str(self.ipmroutesource) + "']" + "[ipMRouteSourceMask='" + str(self.ipmroutesourcemask) + "']"
                self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMROUTESTDMIB.Ipmroutetable.Ipmrouteentry, ['ipmroutegroup', 'ipmroutesource', 'ipmroutesourcemask', 'ipmrouteupstreamneighbor', 'ipmrouteinifindex', 'ipmrouteuptime', 'ipmrouteexpirytime', 'ipmroutepkts', 'ipmroutedifferentinifpackets', 'ipmrouteoctets', 'ipmrouteprotocol', 'ipmroutertproto', 'ipmroutertaddress', 'ipmroutertmask', 'ipmrouterttype', 'ipmroutehcoctets', 'ciscoipmroutepruneflag', 'ciscoipmroutesparseflag', 'ciscoipmrouteconnectedflag', 'ciscoipmroutelocalflag', 'ciscoipmrouteregisterflag', 'ciscoipmrouterpflag', 'ciscoipmroutesptflag', 'ciscoipmroutebps', 'ciscoipmroutemetric', 'ciscoipmroutemetricpreference', 'ciscoipmrouteinlimit', 'ciscoipmroutelastused', 'ciscoipmrouteinlimit2', 'ciscoipmroutejoinflag', 'ciscoipmroutemsdpflag', 'ciscoipmrouteproxyjoinflag', 'ciscoipmroutepkts', 'ciscoipmroutedifferentinifpkts', 'ciscoipmrouteoctets', 'ciscoipmroutebps2', 'ciscoipmroutemetric2'], name, value)

            class Ipmrouterttype(Enum):
                """
                Ipmrouterttype (Enum Class)

                The reason the given route was placed in the (logical)

                multicast Routing Information Base (RIB).  A value of

                unicast means that the route would normally be placed only

                in the unicast RIB, but was placed in the multicast RIB

                (instead or in addition) due to local configuration, such as

                when running PIM over RIP.  A value of multicast means that

                the route was explicitly added to the multicast RIB by the

                routing protocol, such as DVMRP or Multiprotocol BGP.

                .. data:: unicast = 1

                .. data:: multicast = 2

                """

                unicast = Enum.YLeaf(1, "unicast")

                multicast = Enum.YLeaf(2, "multicast")



    class Ipmroutenexthoptable(Entity):
        """
        The (conceptual) table containing information on the next\-
        hops on outgoing interfaces for routing IP multicast
        datagrams.  Each entry is one of a list of next\-hops on
        outgoing interfaces for particular sources sending to a
        particular multicast group address.
        
        .. attribute:: ipmroutenexthopentry
        
        	An entry (conceptual row) in the list of next\-hops on outgoing interfaces to which IP multicast datagrams from particular sources to a IP multicast group address are routed.  Discontinuities in counters in this entry can be detected by observing the value of ipMRouteUpTime
        	**type**\: list of  		 :py:class:`Ipmroutenexthopentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutenexthoptable.Ipmroutenexthopentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IPMROUTESTDMIB.Ipmroutenexthoptable, self).__init__()

            self.yang_name = "ipMRouteNextHopTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipMRouteNextHopEntry", ("ipmroutenexthopentry", IPMROUTESTDMIB.Ipmroutenexthoptable.Ipmroutenexthopentry))])
            self._leafs = OrderedDict()

            self.ipmroutenexthopentry = YList(self)
            self._segment_path = lambda: "ipMRouteNextHopTable"
            self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMROUTESTDMIB.Ipmroutenexthoptable, [], name, value)


        class Ipmroutenexthopentry(Entity):
            """
            An entry (conceptual row) in the list of next\-hops on
            outgoing interfaces to which IP multicast datagrams from
            particular sources to a IP multicast group address are
            routed.  Discontinuities in counters in this entry can be
            detected by observing the value of ipMRouteUpTime.
            
            .. attribute:: ipmroutenexthopgroup  (key)
            
            	The IP multicast group for which this entry specifies a next\-hop on an outgoing interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopsource  (key)
            
            	The network address which when combined with the corresponding value of ipMRouteNextHopSourceMask identifies the sources for which this entry specifies a next\-hop on an outgoing interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopsourcemask  (key)
            
            	The network mask which when combined with the corresponding value of ipMRouteNextHopSource identifies the sources for which this entry specifies a next\-hop on an outgoing interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopifindex  (key)
            
            	The ifIndex value of the interface for the outgoing interface for this next\-hop
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipmroutenexthopaddress  (key)
            
            	The address of the next\-hop specific to this entry.  For most interfaces, this is identical to ipMRouteNextHopGroup. NBMA interfaces, however, may have multiple next\-hop addresses out a single outgoing interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopstate
            
            	An indication of whether the outgoing interface and next\- hop represented by this entry is currently being used to forward IP datagrams.  The value 'forwarding' indicates it is currently being used; the value 'pruned' indicates it is not
            	**type**\:  :py:class:`Ipmroutenexthopstate <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutenexthoptable.Ipmroutenexthopentry.Ipmroutenexthopstate>`
            
            .. attribute:: ipmroutenexthopuptime
            
            	The time since the multicast routing information represented by this entry was learned by the router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutenexthopexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  If ipMRouteNextHopState is pruned(1), the remaining time until the prune expires and the state reverts to forwarding(2).  Otherwise, the remaining time until this entry is removed from the table.  The time remaining may be copied from ipMRouteExpiryTime if the protocol in use for this entry does not specify next\-hop timers.  The value 0      indicates that the entry is not subject to aging
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutenexthopclosestmemberhops
            
            	The minimum number of hops between this router and any member of this IP multicast group reached via this next\-hop on this outgoing interface.  Any IP multicast datagrams for the group which have a TTL less than this number of hops will not be forwarded to this next\-hop
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipmroutenexthopprotocol
            
            	The routing mechanism via which this next\-hop was learned
            	**type**\:  :py:class:`IANAipMRouteProtocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IANAipMRouteProtocol>`
            
            .. attribute:: ipmroutenexthoppkts
            
            	The number of packets which have been forwarded using this route
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmroutenexthopoutlimit
            
            	An outgoing interface's limit for rate limiting data traffic, in Kbps
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: Kbits/second
            
            .. attribute:: ciscoipmroutenexthopmachdr
            
            	The data link mac address header for a multicast datagram. Used by IP multicast fastswitching
            	**type**\: str
            
            .. attribute:: ciscoipmroutenexthoppkts
            
            	The number of packets which have been forwarded using this route. This object is a 64\-bit version of ipMRouteNextHopPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IPMROUTESTDMIB.Ipmroutenexthoptable.Ipmroutenexthopentry, self).__init__()

                self.yang_name = "ipMRouteNextHopEntry"
                self.yang_parent_name = "ipMRouteNextHopTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmroutenexthopgroup','ipmroutenexthopsource','ipmroutenexthopsourcemask','ipmroutenexthopifindex','ipmroutenexthopaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmroutenexthopgroup', YLeaf(YType.str, 'ipMRouteNextHopGroup')),
                    ('ipmroutenexthopsource', YLeaf(YType.str, 'ipMRouteNextHopSource')),
                    ('ipmroutenexthopsourcemask', YLeaf(YType.str, 'ipMRouteNextHopSourceMask')),
                    ('ipmroutenexthopifindex', YLeaf(YType.int32, 'ipMRouteNextHopIfIndex')),
                    ('ipmroutenexthopaddress', YLeaf(YType.str, 'ipMRouteNextHopAddress')),
                    ('ipmroutenexthopstate', YLeaf(YType.enumeration, 'ipMRouteNextHopState')),
                    ('ipmroutenexthopuptime', YLeaf(YType.uint32, 'ipMRouteNextHopUpTime')),
                    ('ipmroutenexthopexpirytime', YLeaf(YType.uint32, 'ipMRouteNextHopExpiryTime')),
                    ('ipmroutenexthopclosestmemberhops', YLeaf(YType.int32, 'ipMRouteNextHopClosestMemberHops')),
                    ('ipmroutenexthopprotocol', YLeaf(YType.enumeration, 'ipMRouteNextHopProtocol')),
                    ('ipmroutenexthoppkts', YLeaf(YType.uint32, 'ipMRouteNextHopPkts')),
                    ('ciscoipmroutenexthopoutlimit', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteNextHopOutLimit')),
                    ('ciscoipmroutenexthopmachdr', YLeaf(YType.str, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteNextHopMacHdr')),
                    ('ciscoipmroutenexthoppkts', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteNextHopPkts')),
                ])
                self.ipmroutenexthopgroup = None
                self.ipmroutenexthopsource = None
                self.ipmroutenexthopsourcemask = None
                self.ipmroutenexthopifindex = None
                self.ipmroutenexthopaddress = None
                self.ipmroutenexthopstate = None
                self.ipmroutenexthopuptime = None
                self.ipmroutenexthopexpirytime = None
                self.ipmroutenexthopclosestmemberhops = None
                self.ipmroutenexthopprotocol = None
                self.ipmroutenexthoppkts = None
                self.ciscoipmroutenexthopoutlimit = None
                self.ciscoipmroutenexthopmachdr = None
                self.ciscoipmroutenexthoppkts = None
                self._segment_path = lambda: "ipMRouteNextHopEntry" + "[ipMRouteNextHopGroup='" + str(self.ipmroutenexthopgroup) + "']" + "[ipMRouteNextHopSource='" + str(self.ipmroutenexthopsource) + "']" + "[ipMRouteNextHopSourceMask='" + str(self.ipmroutenexthopsourcemask) + "']" + "[ipMRouteNextHopIfIndex='" + str(self.ipmroutenexthopifindex) + "']" + "[ipMRouteNextHopAddress='" + str(self.ipmroutenexthopaddress) + "']"
                self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteNextHopTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMROUTESTDMIB.Ipmroutenexthoptable.Ipmroutenexthopentry, ['ipmroutenexthopgroup', 'ipmroutenexthopsource', 'ipmroutenexthopsourcemask', 'ipmroutenexthopifindex', 'ipmroutenexthopaddress', 'ipmroutenexthopstate', 'ipmroutenexthopuptime', 'ipmroutenexthopexpirytime', 'ipmroutenexthopclosestmemberhops', 'ipmroutenexthopprotocol', 'ipmroutenexthoppkts', 'ciscoipmroutenexthopoutlimit', 'ciscoipmroutenexthopmachdr', 'ciscoipmroutenexthoppkts'], name, value)

            class Ipmroutenexthopstate(Enum):
                """
                Ipmroutenexthopstate (Enum Class)

                An indication of whether the outgoing interface and next\-

                hop represented by this entry is currently being used to

                forward IP datagrams.  The value 'forwarding' indicates it

                is currently being used; the value 'pruned' indicates it is

                not.

                .. data:: pruned = 1

                .. data:: forwarding = 2

                """

                pruned = Enum.YLeaf(1, "pruned")

                forwarding = Enum.YLeaf(2, "forwarding")



    class Ipmrouteinterfacetable(Entity):
        """
        The (conceptual) table containing multicast routing
        information specific to interfaces.
        
        .. attribute:: ipmrouteinterfaceentry
        
        	An entry (conceptual row) containing the multicast routing information for a particular interface
        	**type**\: list of  		 :py:class:`Ipmrouteinterfaceentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmrouteinterfacetable.Ipmrouteinterfaceentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IPMROUTESTDMIB.Ipmrouteinterfacetable, self).__init__()

            self.yang_name = "ipMRouteInterfaceTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipMRouteInterfaceEntry", ("ipmrouteinterfaceentry", IPMROUTESTDMIB.Ipmrouteinterfacetable.Ipmrouteinterfaceentry))])
            self._leafs = OrderedDict()

            self.ipmrouteinterfaceentry = YList(self)
            self._segment_path = lambda: "ipMRouteInterfaceTable"
            self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMROUTESTDMIB.Ipmrouteinterfacetable, [], name, value)


        class Ipmrouteinterfaceentry(Entity):
            """
            An entry (conceptual row) containing the multicast routing
            information for a particular interface.
            
            .. attribute:: ipmrouteinterfaceifindex  (key)
            
            	The ifIndex value of the interface for which this entry contains information
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipmrouteinterfacettl
            
            	The datagram TTL threshold for the interface. Any IP multicast datagrams with a TTL less than this threshold will not be forwarded out the interface. The default value of 0 means all multicast packets are forwarded out the interface
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ipmrouteinterfaceprotocol
            
            	The routing protocol running on this interface
            	**type**\:  :py:class:`IANAipMRouteProtocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IANAipMRouteProtocol>`
            
            .. attribute:: ipmrouteinterfaceratelimit
            
            	The rate\-limit, in kilobits per second, of forwarded multicast traffic on the interface.  A rate\-limit of 0 indicates that no rate limiting is done
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipmrouteinterfaceinmcastoctets
            
            	The number of octets of multicast packets that have arrived on the interface, including framing characters.  This object is similar to ifInOctets in the Interfaces MIB, except that only multicast packets are counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteinterfaceoutmcastoctets
            
            	The number of octets of multicast packets that have been sent on the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteinterfacehcinmcastoctets
            
            	The number of octets of multicast packets that have arrived on the interface, including framing characters.  This object is a 64\-bit version of ipMRouteInterfaceInMcastOctets.  It is similar to ifHCInOctets in the Interfaces MIB, except that only multicast packets are counted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipmrouteinterfacehcoutmcastoctets
            
            	The number of octets of multicast packets that have been      sent on the interface.  This object is a 64\-bit version of ipMRouteInterfaceOutMcastOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifinmcastoctets
            
            	The number of octets of multicast packets that have arrived on the interface. This object is a 64\-bit version of ipMRouteInterfaceInMcastOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifoutmcastoctets
            
            	The number of octets of multicast packets that have been sent on the interface. This object is a 64\-bit version of ipMRouteInterfaceOutMcastOctets
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifinmcastpkts
            
            	The number of multicast packets that have arrived on the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteifhcinmcastpkts
            
            	The number of multicast packets that have arrived on the interface. This object is a 64\-bit version of ciscoIpMRouteIfInMcastPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifoutmcastpkts
            
            	The number of multicast packets that have been sent on the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteifhcoutmcastpkts
            
            	The number of multicast packets that have been sent on the interface. This object is a 64\-bit version of ciscoIpMRouteIfOutMcastPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IPMROUTESTDMIB.Ipmrouteinterfacetable.Ipmrouteinterfaceentry, self).__init__()

                self.yang_name = "ipMRouteInterfaceEntry"
                self.yang_parent_name = "ipMRouteInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmrouteinterfaceifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmrouteinterfaceifindex', YLeaf(YType.int32, 'ipMRouteInterfaceIfIndex')),
                    ('ipmrouteinterfacettl', YLeaf(YType.int32, 'ipMRouteInterfaceTtl')),
                    ('ipmrouteinterfaceprotocol', YLeaf(YType.enumeration, 'ipMRouteInterfaceProtocol')),
                    ('ipmrouteinterfaceratelimit', YLeaf(YType.int32, 'ipMRouteInterfaceRateLimit')),
                    ('ipmrouteinterfaceinmcastoctets', YLeaf(YType.uint32, 'ipMRouteInterfaceInMcastOctets')),
                    ('ipmrouteinterfaceoutmcastoctets', YLeaf(YType.uint32, 'ipMRouteInterfaceOutMcastOctets')),
                    ('ipmrouteinterfacehcinmcastoctets', YLeaf(YType.uint64, 'ipMRouteInterfaceHCInMcastOctets')),
                    ('ipmrouteinterfacehcoutmcastoctets', YLeaf(YType.uint64, 'ipMRouteInterfaceHCOutMcastOctets')),
                    ('ciscoipmrouteifinmcastoctets', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteIfInMcastOctets')),
                    ('ciscoipmrouteifoutmcastoctets', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteIfOutMcastOctets')),
                    ('ciscoipmrouteifinmcastpkts', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteIfInMcastPkts')),
                    ('ciscoipmrouteifhcinmcastpkts', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteIfHCInMcastPkts')),
                    ('ciscoipmrouteifoutmcastpkts', YLeaf(YType.uint32, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteIfOutMcastPkts')),
                    ('ciscoipmrouteifhcoutmcastpkts', YLeaf(YType.uint64, 'CISCO-IPMROUTE-MIB:ciscoIpMRouteIfHCOutMcastPkts')),
                ])
                self.ipmrouteinterfaceifindex = None
                self.ipmrouteinterfacettl = None
                self.ipmrouteinterfaceprotocol = None
                self.ipmrouteinterfaceratelimit = None
                self.ipmrouteinterfaceinmcastoctets = None
                self.ipmrouteinterfaceoutmcastoctets = None
                self.ipmrouteinterfacehcinmcastoctets = None
                self.ipmrouteinterfacehcoutmcastoctets = None
                self.ciscoipmrouteifinmcastoctets = None
                self.ciscoipmrouteifoutmcastoctets = None
                self.ciscoipmrouteifinmcastpkts = None
                self.ciscoipmrouteifhcinmcastpkts = None
                self.ciscoipmrouteifoutmcastpkts = None
                self.ciscoipmrouteifhcoutmcastpkts = None
                self._segment_path = lambda: "ipMRouteInterfaceEntry" + "[ipMRouteInterfaceIfIndex='" + str(self.ipmrouteinterfaceifindex) + "']"
                self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMROUTESTDMIB.Ipmrouteinterfacetable.Ipmrouteinterfaceentry, ['ipmrouteinterfaceifindex', 'ipmrouteinterfacettl', 'ipmrouteinterfaceprotocol', 'ipmrouteinterfaceratelimit', 'ipmrouteinterfaceinmcastoctets', 'ipmrouteinterfaceoutmcastoctets', 'ipmrouteinterfacehcinmcastoctets', 'ipmrouteinterfacehcoutmcastoctets', 'ciscoipmrouteifinmcastoctets', 'ciscoipmrouteifoutmcastoctets', 'ciscoipmrouteifinmcastpkts', 'ciscoipmrouteifhcinmcastpkts', 'ciscoipmrouteifoutmcastpkts', 'ciscoipmrouteifhcoutmcastpkts'], name, value)


    class Ipmrouteboundarytable(Entity):
        """
        The (conceptual) table listing the router's scoped
        multicast address boundaries.
        
        .. attribute:: ipmrouteboundaryentry
        
        	An entry (conceptual row) in the ipMRouteBoundaryTable representing a scoped boundary
        	**type**\: list of  		 :py:class:`Ipmrouteboundaryentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmrouteboundarytable.Ipmrouteboundaryentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IPMROUTESTDMIB.Ipmrouteboundarytable, self).__init__()

            self.yang_name = "ipMRouteBoundaryTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipMRouteBoundaryEntry", ("ipmrouteboundaryentry", IPMROUTESTDMIB.Ipmrouteboundarytable.Ipmrouteboundaryentry))])
            self._leafs = OrderedDict()

            self.ipmrouteboundaryentry = YList(self)
            self._segment_path = lambda: "ipMRouteBoundaryTable"
            self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMROUTESTDMIB.Ipmrouteboundarytable, [], name, value)


        class Ipmrouteboundaryentry(Entity):
            """
            An entry (conceptual row) in the ipMRouteBoundaryTable
            representing a scoped boundary.
            
            .. attribute:: ipmrouteboundaryifindex  (key)
            
            	The IfIndex value for the interface to which this boundary applies.  Packets with a destination address in the associated address/mask range will not be forwarded out this interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipmrouteboundaryaddress  (key)
            
            	The group address which when combined with the corresponding value of ipMRouteBoundaryAddressMask identifies the group range for which the scoped boundary exists.  Scoped addresses must come from the range 239.x.x.x as specified in RFC 2365
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteboundaryaddressmask  (key)
            
            	The group address mask which when combined with the corresponding value of ipMRouteBoundaryAddress identifies the group range for which the scoped boundary exists
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteboundarystatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IPMROUTESTDMIB.Ipmrouteboundarytable.Ipmrouteboundaryentry, self).__init__()

                self.yang_name = "ipMRouteBoundaryEntry"
                self.yang_parent_name = "ipMRouteBoundaryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmrouteboundaryifindex','ipmrouteboundaryaddress','ipmrouteboundaryaddressmask']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmrouteboundaryifindex', YLeaf(YType.int32, 'ipMRouteBoundaryIfIndex')),
                    ('ipmrouteboundaryaddress', YLeaf(YType.str, 'ipMRouteBoundaryAddress')),
                    ('ipmrouteboundaryaddressmask', YLeaf(YType.str, 'ipMRouteBoundaryAddressMask')),
                    ('ipmrouteboundarystatus', YLeaf(YType.enumeration, 'ipMRouteBoundaryStatus')),
                ])
                self.ipmrouteboundaryifindex = None
                self.ipmrouteboundaryaddress = None
                self.ipmrouteboundaryaddressmask = None
                self.ipmrouteboundarystatus = None
                self._segment_path = lambda: "ipMRouteBoundaryEntry" + "[ipMRouteBoundaryIfIndex='" + str(self.ipmrouteboundaryifindex) + "']" + "[ipMRouteBoundaryAddress='" + str(self.ipmrouteboundaryaddress) + "']" + "[ipMRouteBoundaryAddressMask='" + str(self.ipmrouteboundaryaddressmask) + "']"
                self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteBoundaryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMROUTESTDMIB.Ipmrouteboundarytable.Ipmrouteboundaryentry, ['ipmrouteboundaryifindex', 'ipmrouteboundaryaddress', 'ipmrouteboundaryaddressmask', 'ipmrouteboundarystatus'], name, value)


    class Ipmroutescopenametable(Entity):
        """
        The (conceptual) table listing the multicast scope names.
        
        .. attribute:: ipmroutescopenameentry
        
        	An entry (conceptual row) in the ipMRouteScopeNameTable representing a multicast scope name
        	**type**\: list of  		 :py:class:`Ipmroutescopenameentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.Ipmroutescopenametable.Ipmroutescopenameentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IPMROUTESTDMIB.Ipmroutescopenametable, self).__init__()

            self.yang_name = "ipMRouteScopeNameTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipMRouteScopeNameEntry", ("ipmroutescopenameentry", IPMROUTESTDMIB.Ipmroutescopenametable.Ipmroutescopenameentry))])
            self._leafs = OrderedDict()

            self.ipmroutescopenameentry = YList(self)
            self._segment_path = lambda: "ipMRouteScopeNameTable"
            self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMROUTESTDMIB.Ipmroutescopenametable, [], name, value)


        class Ipmroutescopenameentry(Entity):
            """
            An entry (conceptual row) in the ipMRouteScopeNameTable
            representing a multicast scope name.
            
            .. attribute:: ipmroutescopenameaddress  (key)
            
            	The group address which when combined with the corresponding value of ipMRouteScopeNameAddressMask identifies the group range associated with the multicast scope.  Scoped addresses must come from the range 239.x.x.x
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutescopenameaddressmask  (key)
            
            	The group address mask which when combined with the corresponding value of ipMRouteScopeNameAddress identifies the group range associated with the multicast scope
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutescopenamelanguage  (key)
            
            	The RFC 1766\-style language tag associated with the scope name
            	**type**\: str
            
            .. attribute:: ipmroutescopenamestring
            
            	The textual name associated with the multicast scope.  The value of this object should be suitable for displaying to end\-users, such as when allocating a multicast address in this scope.  When no name is specified, the default value of this object should be the string 239.x.x.x/y with x and y replaced appropriately to describe the address and mask length associated with the scope
            	**type**\: str
            
            .. attribute:: ipmroutescopenamedefault
            
            	If true, indicates a preference that the name in the following language should be used by applications if no name is available in a desired language
            	**type**\: bool
            
            .. attribute:: ipmroutescopenamestatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IPMROUTESTDMIB.Ipmroutescopenametable.Ipmroutescopenameentry, self).__init__()

                self.yang_name = "ipMRouteScopeNameEntry"
                self.yang_parent_name = "ipMRouteScopeNameTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmroutescopenameaddress','ipmroutescopenameaddressmask','ipmroutescopenamelanguage']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmroutescopenameaddress', YLeaf(YType.str, 'ipMRouteScopeNameAddress')),
                    ('ipmroutescopenameaddressmask', YLeaf(YType.str, 'ipMRouteScopeNameAddressMask')),
                    ('ipmroutescopenamelanguage', YLeaf(YType.str, 'ipMRouteScopeNameLanguage')),
                    ('ipmroutescopenamestring', YLeaf(YType.str, 'ipMRouteScopeNameString')),
                    ('ipmroutescopenamedefault', YLeaf(YType.boolean, 'ipMRouteScopeNameDefault')),
                    ('ipmroutescopenamestatus', YLeaf(YType.enumeration, 'ipMRouteScopeNameStatus')),
                ])
                self.ipmroutescopenameaddress = None
                self.ipmroutescopenameaddressmask = None
                self.ipmroutescopenamelanguage = None
                self.ipmroutescopenamestring = None
                self.ipmroutescopenamedefault = None
                self.ipmroutescopenamestatus = None
                self._segment_path = lambda: "ipMRouteScopeNameEntry" + "[ipMRouteScopeNameAddress='" + str(self.ipmroutescopenameaddress) + "']" + "[ipMRouteScopeNameAddressMask='" + str(self.ipmroutescopenameaddressmask) + "']" + "[ipMRouteScopeNameLanguage='" + str(self.ipmroutescopenamelanguage) + "']"
                self._absolute_path = lambda: "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteScopeNameTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMROUTESTDMIB.Ipmroutescopenametable.Ipmroutescopenameentry, ['ipmroutescopenameaddress', 'ipmroutescopenameaddressmask', 'ipmroutescopenamelanguage', 'ipmroutescopenamestring', 'ipmroutescopenamedefault', 'ipmroutescopenamestatus'], name, value)

    def clone_ptr(self):
        self._top_entity = IPMROUTESTDMIB()
        return self._top_entity

