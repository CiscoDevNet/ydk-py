""" IPMROUTE_STD_MIB 

The MIB module for management of IP Multicast routing, but
independent of the specific multicast routing protocol in
use.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpmrouteStdMib(Entity):
    """
    
    
    .. attribute:: ipmroute
    
    	
    	**type**\:   :py:class:`Ipmroute <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroute>`
    
    .. attribute:: ipmrouteboundarytable
    
    	The (conceptual) table listing the router's scoped multicast address boundaries
    	**type**\:   :py:class:`Ipmrouteboundarytable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmrouteboundarytable>`
    
    .. attribute:: ipmrouteinterfacetable
    
    	The (conceptual) table containing multicast routing information specific to interfaces
    	**type**\:   :py:class:`Ipmrouteinterfacetable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmrouteinterfacetable>`
    
    .. attribute:: ipmroutenexthoptable
    
    	The (conceptual) table containing information on the next\- hops on outgoing interfaces for routing IP multicast datagrams.  Each entry is one of a list of next\-hops on outgoing interfaces for particular sources sending to a particular multicast group address
    	**type**\:   :py:class:`Ipmroutenexthoptable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable>`
    
    .. attribute:: ipmroutescopenametable
    
    	The (conceptual) table listing the multicast scope names
    	**type**\:   :py:class:`Ipmroutescopenametable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutescopenametable>`
    
    .. attribute:: ipmroutetable
    
    	The (conceptual) table containing multicast routing information for IP datagrams sent by particular sources to the IP multicast groups known to this router
    	**type**\:   :py:class:`Ipmroutetable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable>`
    
    

    """

    _prefix = 'IPMROUTE-STD-MIB'
    _revision = '2000-09-22'

    def __init__(self):
        super(IpmrouteStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "IPMROUTE-STD-MIB"
        self.yang_parent_name = "IPMROUTE-STD-MIB"

        self.ipmroute = IpmrouteStdMib.Ipmroute()
        self.ipmroute.parent = self
        self._children_name_map["ipmroute"] = "ipMRoute"
        self._children_yang_names.add("ipMRoute")

        self.ipmrouteboundarytable = IpmrouteStdMib.Ipmrouteboundarytable()
        self.ipmrouteboundarytable.parent = self
        self._children_name_map["ipmrouteboundarytable"] = "ipMRouteBoundaryTable"
        self._children_yang_names.add("ipMRouteBoundaryTable")

        self.ipmrouteinterfacetable = IpmrouteStdMib.Ipmrouteinterfacetable()
        self.ipmrouteinterfacetable.parent = self
        self._children_name_map["ipmrouteinterfacetable"] = "ipMRouteInterfaceTable"
        self._children_yang_names.add("ipMRouteInterfaceTable")

        self.ipmroutenexthoptable = IpmrouteStdMib.Ipmroutenexthoptable()
        self.ipmroutenexthoptable.parent = self
        self._children_name_map["ipmroutenexthoptable"] = "ipMRouteNextHopTable"
        self._children_yang_names.add("ipMRouteNextHopTable")

        self.ipmroutescopenametable = IpmrouteStdMib.Ipmroutescopenametable()
        self.ipmroutescopenametable.parent = self
        self._children_name_map["ipmroutescopenametable"] = "ipMRouteScopeNameTable"
        self._children_yang_names.add("ipMRouteScopeNameTable")

        self.ipmroutetable = IpmrouteStdMib.Ipmroutetable()
        self.ipmroutetable.parent = self
        self._children_name_map["ipmroutetable"] = "ipMRouteTable"
        self._children_yang_names.add("ipMRouteTable")


    class Ipmroute(Entity):
        """
        
        
        .. attribute:: ipmrouteenable
        
        	The enabled status of IP Multicast routing on this router
        	**type**\:   :py:class:`Ipmrouteenable <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroute.Ipmrouteenable>`
        
        .. attribute:: ipmrouteentrycount
        
        	The number of rows in the ipMRouteTable.  This can be used to monitor the multicast routing table size
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IpmrouteStdMib.Ipmroute, self).__init__()

            self.yang_name = "ipMRoute"
            self.yang_parent_name = "IPMROUTE-STD-MIB"

            self.ipmrouteenable = YLeaf(YType.enumeration, "ipMRouteEnable")

            self.ipmrouteentrycount = YLeaf(YType.uint32, "ipMRouteEntryCount")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ipmrouteenable",
                            "ipmrouteentrycount") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpmrouteStdMib.Ipmroute, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpmrouteStdMib.Ipmroute, self).__setattr__(name, value)

        class Ipmrouteenable(Enum):
            """
            Ipmrouteenable

            The enabled status of IP Multicast routing on this router.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")


        def has_data(self):
            return (
                self.ipmrouteenable.is_set or
                self.ipmrouteentrycount.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ipmrouteenable.yfilter != YFilter.not_set or
                self.ipmrouteentrycount.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipMRoute" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ipmrouteenable.is_set or self.ipmrouteenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipmrouteenable.get_name_leafdata())
            if (self.ipmrouteentrycount.is_set or self.ipmrouteentrycount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipmrouteentrycount.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipMRouteEnable" or name == "ipMRouteEntryCount"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ipMRouteEnable"):
                self.ipmrouteenable = value
                self.ipmrouteenable.value_namespace = name_space
                self.ipmrouteenable.value_namespace_prefix = name_space_prefix
            if(value_path == "ipMRouteEntryCount"):
                self.ipmrouteentrycount = value
                self.ipmrouteentrycount.value_namespace = name_space
                self.ipmrouteentrycount.value_namespace_prefix = name_space_prefix


    class Ipmroutetable(Entity):
        """
        The (conceptual) table containing multicast routing
        information for IP datagrams sent by particular sources to
        the IP multicast groups known to this router.
        
        .. attribute:: ipmrouteentry
        
        	An entry (conceptual row) containing the multicast routing information for IP datagrams from a particular source and addressed to a particular IP multicast group address. Discontinuities in counters in this entry can be detected by observing the value of ipMRouteUpTime
        	**type**\: list of    :py:class:`Ipmrouteentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IpmrouteStdMib.Ipmroutetable, self).__init__()

            self.yang_name = "ipMRouteTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"

            self.ipmrouteentry = YList(self)

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
                        super(IpmrouteStdMib.Ipmroutetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpmrouteStdMib.Ipmroutetable, self).__setattr__(name, value)


        class Ipmrouteentry(Entity):
            """
            An entry (conceptual row) containing the multicast routing
            information for IP datagrams from a particular source and
            addressed to a particular IP multicast group address.
            Discontinuities in counters in this entry can be detected by
            observing the value of ipMRouteUpTime.
            
            .. attribute:: ipmroutegroup  <key>
            
            	The IP multicast group address for which this entry contains multicast routing information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutesource  <key>
            
            	The network address which when combined with the corresponding value of ipMRouteSourceMask identifies the sources for which this entry contains multicast routing information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutesourcemask  <key>
            
            	The network mask which when combined with the corresponding value of ipMRouteSource identifies the sources for which this entry contains multicast routing information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmroutebps
            
            	Bits per second forwarded by this router.  This is the sum of all forwarded bits during a 1 second interval.  At the end of each second the field is cleared. This object has been superseded by ciscoIpMRouteBps2 (which is the 64\-bit version of this object)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: ciscoipmroutebps2
            
            	Bits per second forwarded by this router. This is the sum of all forwarded bits during a 1 second interval. At the end of each second the field is cleared
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteconnectedflag
            
            	Boolean, indicating whether there is a directly connected member for a group attached to the router
            	**type**\:  bool
            
            .. attribute:: ciscoipmroutedifferentinifpkts
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address, which were not received from the interface indicated by ipMRouteInIfIndex. This object is a 64\-bit version of ipMRouteDifferentInIfPackets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteinlimit
            
            	Incoming interface's limit for rate limiting data traffic, in Kbps. Replaced by ciscoIpMRouteInLimit2
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Kbits/second
            
            	**status**\: obsolete
            
            .. attribute:: ciscoipmrouteinlimit2
            
            	Incoming interface's limit for rate limiting data traffic, in Kbps
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Kbits/second
            
            .. attribute:: ciscoipmroutejoinflag
            
            	Boolean, indicates whether this route is created due to SPT threshold
            	**type**\:  bool
            
            .. attribute:: ciscoipmroutelastused
            
            	How long has it been since the last multicast packet was fastswitched
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmroutelocalflag
            
            	Boolean, indicating whether local system is a member of a group on any interface
            	**type**\:  bool
            
            .. attribute:: ciscoipmroutemetric
            
            	Metric \- The best metric heard from Assert messages. This object has been replaced by ciscoIpMRouteMetric2 in order to correctly represent a 32\-bit unsigned metric value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ciscoipmroutemetric2
            
            	Metric \- The best metric heard from Assert messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmroutemetricpreference
            
            	Metric Preference \- The best metric preference heard from Assert messages
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoipmroutemsdpflag
            
            	Boolean, indicates whether this route is learned via MSDP
            	**type**\:  bool
            
            .. attribute:: ciscoipmrouteoctets
            
            	The number of octets contained in IP datagrams which were received from these sources and addressed to this multicast group address, and which were forwarded by this router. This object is a 64\-bit version of ipMRouteOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmroutepkts
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address. This object is a 64\-bit version of ipMRoutePkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteproxyjoinflag
            
            	Boolean, indicates whether to send join for this entry
            	**type**\:  bool
            
            .. attribute:: ciscoipmroutepruneflag
            
            	Boolean, indicates whether this route is pruned. A pruned route is one that has an empty outgoing interface list or all interfaces are in Pruned state. A multicast packet that matches a pruned route doesn't get forwarded
            	**type**\:  bool
            
            .. attribute:: ciscoipmrouteregisterflag
            
            	Boolean, indicates whether to send registers for the entry. A first hop router directly connected to a multicast source host, as well as a border router on the boundary of two domains running different multicast routing protocols, encapsulates packets to be sent on the shared tree. This is done until the RP sends Joins back to this router
            	**type**\:  bool
            
            .. attribute:: ciscoipmrouterpflag
            
            	Boolean, indicating whether there is a Prune state for this source along the shared tree
            	**type**\:  bool
            
            .. attribute:: ciscoipmroutesparseflag
            
            	Boolean, indicating PIM multicast routing protocol sparse\-mode (versus dense\-mode).  In sparse\-mode, packets are forwarded only out interfaces that have been joined. In dense\-mode, they are forwarded out all interfaces that have not been pruned
            	**type**\:  bool
            
            .. attribute:: ciscoipmroutesptflag
            
            	Boolean, indicating whether data is being received on the SPT tree, ie the Shortest Path Tree
            	**type**\:  bool
            
            .. attribute:: ipmroutedifferentinifpackets
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address, which were dropped because they were not received on the interface indicated by ipMRouteInIfIndex.  Packets which are not subject to an incoming interface check (e.g., using CBT) are not counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  The value 0 indicates that the entry is not subject to aging
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutehcoctets
            
            	The number of octets contained in IP datagrams which were received from these sources and addressed to this multicast group address, and which were forwarded by this router. This object is a 64\-bit version of ipMRouteOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipmrouteinifindex
            
            	The value of ifIndex for the interface on which IP datagrams sent by these sources to this multicast address are received.  A value of 0 indicates that datagrams are not subject to an incoming interface check, but may be accepted on multiple interfaces (e.g., in CBT)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ipmrouteoctets
            
            	The number of octets contained in IP datagrams which were received from these sources and addressed to this multicast group address, and which were forwarded by this router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutepkts
            
            	The number of packets which this router has received from these sources and addressed to this multicast group address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteprotocol
            
            	The multicast routing protocol via which this multicast forwarding entry was learned
            	**type**\:   :py:class:`Ianaipmrouteprotocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.Ianaipmrouteprotocol>`
            
            .. attribute:: ipmroutertaddress
            
            	The address portion of the route used to find the upstream or parent interface for this multicast forwarding entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutertmask
            
            	The mask associated with the route used to find the upstream or parent interface for this multicast forwarding entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutertproto
            
            	The routing mechanism via which the route used to find the upstream or parent interface for this multicast forwarding entry was learned.  Inclusion of values for routing protocols is not intended to imply that those protocols need be supported
            	**type**\:   :py:class:`Ianaiprouteprotocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.Ianaiprouteprotocol>`
            
            .. attribute:: ipmrouterttype
            
            	The reason the given route was placed in the (logical) multicast Routing Information Base (RIB).  A value of unicast means that the route would normally be placed only in the unicast RIB, but was placed in the multicast RIB (instead or in addition) due to local configuration, such as when running PIM over RIP.  A value of multicast means that      the route was explicitly added to the multicast RIB by the routing protocol, such as DVMRP or Multiprotocol BGP
            	**type**\:   :py:class:`Ipmrouterttype <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry.Ipmrouterttype>`
            
            .. attribute:: ipmrouteupstreamneighbor
            
            	The address of the upstream neighbor (e.g., RPF neighbor) from which IP datagrams from these sources to this multicast address are received, or 0.0.0.0 if the upstream neighbor is unknown (e.g., in CBT)
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteuptime
            
            	The time since the multicast routing information represented by this entry was learned by the router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IpmrouteStdMib.Ipmroutetable.Ipmrouteentry, self).__init__()

                self.yang_name = "ipMRouteEntry"
                self.yang_parent_name = "ipMRouteTable"

                self.ipmroutegroup = YLeaf(YType.str, "ipMRouteGroup")

                self.ipmroutesource = YLeaf(YType.str, "ipMRouteSource")

                self.ipmroutesourcemask = YLeaf(YType.str, "ipMRouteSourceMask")

                self.ciscoipmroutebps = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteBps")

                self.ciscoipmroutebps2 = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteBps2")

                self.ciscoipmrouteconnectedflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteConnectedFlag")

                self.ciscoipmroutedifferentinifpkts = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteDifferentInIfPkts")

                self.ciscoipmrouteinlimit = YLeaf(YType.int32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteInLimit")

                self.ciscoipmrouteinlimit2 = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteInLimit2")

                self.ciscoipmroutejoinflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteJoinFlag")

                self.ciscoipmroutelastused = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteLastUsed")

                self.ciscoipmroutelocalflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteLocalFlag")

                self.ciscoipmroutemetric = YLeaf(YType.int32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteMetric")

                self.ciscoipmroutemetric2 = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteMetric2")

                self.ciscoipmroutemetricpreference = YLeaf(YType.int32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteMetricPreference")

                self.ciscoipmroutemsdpflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteMsdpFlag")

                self.ciscoipmrouteoctets = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteOctets")

                self.ciscoipmroutepkts = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRoutePkts")

                self.ciscoipmrouteproxyjoinflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteProxyJoinFlag")

                self.ciscoipmroutepruneflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRoutePruneFlag")

                self.ciscoipmrouteregisterflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteRegisterFlag")

                self.ciscoipmrouterpflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteRpFlag")

                self.ciscoipmroutesparseflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteSparseFlag")

                self.ciscoipmroutesptflag = YLeaf(YType.boolean, "CISCO-IPMROUTE-MIB:ciscoIpMRouteSptFlag")

                self.ipmroutedifferentinifpackets = YLeaf(YType.uint32, "ipMRouteDifferentInIfPackets")

                self.ipmrouteexpirytime = YLeaf(YType.uint32, "ipMRouteExpiryTime")

                self.ipmroutehcoctets = YLeaf(YType.uint64, "ipMRouteHCOctets")

                self.ipmrouteinifindex = YLeaf(YType.int32, "ipMRouteInIfIndex")

                self.ipmrouteoctets = YLeaf(YType.uint32, "ipMRouteOctets")

                self.ipmroutepkts = YLeaf(YType.uint32, "ipMRoutePkts")

                self.ipmrouteprotocol = YLeaf(YType.enumeration, "ipMRouteProtocol")

                self.ipmroutertaddress = YLeaf(YType.str, "ipMRouteRtAddress")

                self.ipmroutertmask = YLeaf(YType.str, "ipMRouteRtMask")

                self.ipmroutertproto = YLeaf(YType.enumeration, "ipMRouteRtProto")

                self.ipmrouterttype = YLeaf(YType.enumeration, "ipMRouteRtType")

                self.ipmrouteupstreamneighbor = YLeaf(YType.str, "ipMRouteUpstreamNeighbor")

                self.ipmrouteuptime = YLeaf(YType.uint32, "ipMRouteUpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmroutegroup",
                                "ipmroutesource",
                                "ipmroutesourcemask",
                                "ciscoipmroutebps",
                                "ciscoipmroutebps2",
                                "ciscoipmrouteconnectedflag",
                                "ciscoipmroutedifferentinifpkts",
                                "ciscoipmrouteinlimit",
                                "ciscoipmrouteinlimit2",
                                "ciscoipmroutejoinflag",
                                "ciscoipmroutelastused",
                                "ciscoipmroutelocalflag",
                                "ciscoipmroutemetric",
                                "ciscoipmroutemetric2",
                                "ciscoipmroutemetricpreference",
                                "ciscoipmroutemsdpflag",
                                "ciscoipmrouteoctets",
                                "ciscoipmroutepkts",
                                "ciscoipmrouteproxyjoinflag",
                                "ciscoipmroutepruneflag",
                                "ciscoipmrouteregisterflag",
                                "ciscoipmrouterpflag",
                                "ciscoipmroutesparseflag",
                                "ciscoipmroutesptflag",
                                "ipmroutedifferentinifpackets",
                                "ipmrouteexpirytime",
                                "ipmroutehcoctets",
                                "ipmrouteinifindex",
                                "ipmrouteoctets",
                                "ipmroutepkts",
                                "ipmrouteprotocol",
                                "ipmroutertaddress",
                                "ipmroutertmask",
                                "ipmroutertproto",
                                "ipmrouterttype",
                                "ipmrouteupstreamneighbor",
                                "ipmrouteuptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpmrouteStdMib.Ipmroutetable.Ipmrouteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpmrouteStdMib.Ipmroutetable.Ipmrouteentry, self).__setattr__(name, value)

            class Ipmrouterttype(Enum):
                """
                Ipmrouterttype

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


            def has_data(self):
                return (
                    self.ipmroutegroup.is_set or
                    self.ipmroutesource.is_set or
                    self.ipmroutesourcemask.is_set or
                    self.ciscoipmroutebps.is_set or
                    self.ciscoipmroutebps2.is_set or
                    self.ciscoipmrouteconnectedflag.is_set or
                    self.ciscoipmroutedifferentinifpkts.is_set or
                    self.ciscoipmrouteinlimit.is_set or
                    self.ciscoipmrouteinlimit2.is_set or
                    self.ciscoipmroutejoinflag.is_set or
                    self.ciscoipmroutelastused.is_set or
                    self.ciscoipmroutelocalflag.is_set or
                    self.ciscoipmroutemetric.is_set or
                    self.ciscoipmroutemetric2.is_set or
                    self.ciscoipmroutemetricpreference.is_set or
                    self.ciscoipmroutemsdpflag.is_set or
                    self.ciscoipmrouteoctets.is_set or
                    self.ciscoipmroutepkts.is_set or
                    self.ciscoipmrouteproxyjoinflag.is_set or
                    self.ciscoipmroutepruneflag.is_set or
                    self.ciscoipmrouteregisterflag.is_set or
                    self.ciscoipmrouterpflag.is_set or
                    self.ciscoipmroutesparseflag.is_set or
                    self.ciscoipmroutesptflag.is_set or
                    self.ipmroutedifferentinifpackets.is_set or
                    self.ipmrouteexpirytime.is_set or
                    self.ipmroutehcoctets.is_set or
                    self.ipmrouteinifindex.is_set or
                    self.ipmrouteoctets.is_set or
                    self.ipmroutepkts.is_set or
                    self.ipmrouteprotocol.is_set or
                    self.ipmroutertaddress.is_set or
                    self.ipmroutertmask.is_set or
                    self.ipmroutertproto.is_set or
                    self.ipmrouterttype.is_set or
                    self.ipmrouteupstreamneighbor.is_set or
                    self.ipmrouteuptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmroutegroup.yfilter != YFilter.not_set or
                    self.ipmroutesource.yfilter != YFilter.not_set or
                    self.ipmroutesourcemask.yfilter != YFilter.not_set or
                    self.ciscoipmroutebps.yfilter != YFilter.not_set or
                    self.ciscoipmroutebps2.yfilter != YFilter.not_set or
                    self.ciscoipmrouteconnectedflag.yfilter != YFilter.not_set or
                    self.ciscoipmroutedifferentinifpkts.yfilter != YFilter.not_set or
                    self.ciscoipmrouteinlimit.yfilter != YFilter.not_set or
                    self.ciscoipmrouteinlimit2.yfilter != YFilter.not_set or
                    self.ciscoipmroutejoinflag.yfilter != YFilter.not_set or
                    self.ciscoipmroutelastused.yfilter != YFilter.not_set or
                    self.ciscoipmroutelocalflag.yfilter != YFilter.not_set or
                    self.ciscoipmroutemetric.yfilter != YFilter.not_set or
                    self.ciscoipmroutemetric2.yfilter != YFilter.not_set or
                    self.ciscoipmroutemetricpreference.yfilter != YFilter.not_set or
                    self.ciscoipmroutemsdpflag.yfilter != YFilter.not_set or
                    self.ciscoipmrouteoctets.yfilter != YFilter.not_set or
                    self.ciscoipmroutepkts.yfilter != YFilter.not_set or
                    self.ciscoipmrouteproxyjoinflag.yfilter != YFilter.not_set or
                    self.ciscoipmroutepruneflag.yfilter != YFilter.not_set or
                    self.ciscoipmrouteregisterflag.yfilter != YFilter.not_set or
                    self.ciscoipmrouterpflag.yfilter != YFilter.not_set or
                    self.ciscoipmroutesparseflag.yfilter != YFilter.not_set or
                    self.ciscoipmroutesptflag.yfilter != YFilter.not_set or
                    self.ipmroutedifferentinifpackets.yfilter != YFilter.not_set or
                    self.ipmrouteexpirytime.yfilter != YFilter.not_set or
                    self.ipmroutehcoctets.yfilter != YFilter.not_set or
                    self.ipmrouteinifindex.yfilter != YFilter.not_set or
                    self.ipmrouteoctets.yfilter != YFilter.not_set or
                    self.ipmroutepkts.yfilter != YFilter.not_set or
                    self.ipmrouteprotocol.yfilter != YFilter.not_set or
                    self.ipmroutertaddress.yfilter != YFilter.not_set or
                    self.ipmroutertmask.yfilter != YFilter.not_set or
                    self.ipmroutertproto.yfilter != YFilter.not_set or
                    self.ipmrouterttype.yfilter != YFilter.not_set or
                    self.ipmrouteupstreamneighbor.yfilter != YFilter.not_set or
                    self.ipmrouteuptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipMRouteEntry" + "[ipMRouteGroup='" + self.ipmroutegroup.get() + "']" + "[ipMRouteSource='" + self.ipmroutesource.get() + "']" + "[ipMRouteSourceMask='" + self.ipmroutesourcemask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmroutegroup.is_set or self.ipmroutegroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutegroup.get_name_leafdata())
                if (self.ipmroutesource.is_set or self.ipmroutesource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutesource.get_name_leafdata())
                if (self.ipmroutesourcemask.is_set or self.ipmroutesourcemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutesourcemask.get_name_leafdata())
                if (self.ciscoipmroutebps.is_set or self.ciscoipmroutebps.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutebps.get_name_leafdata())
                if (self.ciscoipmroutebps2.is_set or self.ciscoipmroutebps2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutebps2.get_name_leafdata())
                if (self.ciscoipmrouteconnectedflag.is_set or self.ciscoipmrouteconnectedflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteconnectedflag.get_name_leafdata())
                if (self.ciscoipmroutedifferentinifpkts.is_set or self.ciscoipmroutedifferentinifpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutedifferentinifpkts.get_name_leafdata())
                if (self.ciscoipmrouteinlimit.is_set or self.ciscoipmrouteinlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteinlimit.get_name_leafdata())
                if (self.ciscoipmrouteinlimit2.is_set or self.ciscoipmrouteinlimit2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteinlimit2.get_name_leafdata())
                if (self.ciscoipmroutejoinflag.is_set or self.ciscoipmroutejoinflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutejoinflag.get_name_leafdata())
                if (self.ciscoipmroutelastused.is_set or self.ciscoipmroutelastused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutelastused.get_name_leafdata())
                if (self.ciscoipmroutelocalflag.is_set or self.ciscoipmroutelocalflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutelocalflag.get_name_leafdata())
                if (self.ciscoipmroutemetric.is_set or self.ciscoipmroutemetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutemetric.get_name_leafdata())
                if (self.ciscoipmroutemetric2.is_set or self.ciscoipmroutemetric2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutemetric2.get_name_leafdata())
                if (self.ciscoipmroutemetricpreference.is_set or self.ciscoipmroutemetricpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutemetricpreference.get_name_leafdata())
                if (self.ciscoipmroutemsdpflag.is_set or self.ciscoipmroutemsdpflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutemsdpflag.get_name_leafdata())
                if (self.ciscoipmrouteoctets.is_set or self.ciscoipmrouteoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteoctets.get_name_leafdata())
                if (self.ciscoipmroutepkts.is_set or self.ciscoipmroutepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutepkts.get_name_leafdata())
                if (self.ciscoipmrouteproxyjoinflag.is_set or self.ciscoipmrouteproxyjoinflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteproxyjoinflag.get_name_leafdata())
                if (self.ciscoipmroutepruneflag.is_set or self.ciscoipmroutepruneflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutepruneflag.get_name_leafdata())
                if (self.ciscoipmrouteregisterflag.is_set or self.ciscoipmrouteregisterflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteregisterflag.get_name_leafdata())
                if (self.ciscoipmrouterpflag.is_set or self.ciscoipmrouterpflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouterpflag.get_name_leafdata())
                if (self.ciscoipmroutesparseflag.is_set or self.ciscoipmroutesparseflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutesparseflag.get_name_leafdata())
                if (self.ciscoipmroutesptflag.is_set or self.ciscoipmroutesptflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutesptflag.get_name_leafdata())
                if (self.ipmroutedifferentinifpackets.is_set or self.ipmroutedifferentinifpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutedifferentinifpackets.get_name_leafdata())
                if (self.ipmrouteexpirytime.is_set or self.ipmrouteexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteexpirytime.get_name_leafdata())
                if (self.ipmroutehcoctets.is_set or self.ipmroutehcoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutehcoctets.get_name_leafdata())
                if (self.ipmrouteinifindex.is_set or self.ipmrouteinifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinifindex.get_name_leafdata())
                if (self.ipmrouteoctets.is_set or self.ipmrouteoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteoctets.get_name_leafdata())
                if (self.ipmroutepkts.is_set or self.ipmroutepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutepkts.get_name_leafdata())
                if (self.ipmrouteprotocol.is_set or self.ipmrouteprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteprotocol.get_name_leafdata())
                if (self.ipmroutertaddress.is_set or self.ipmroutertaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutertaddress.get_name_leafdata())
                if (self.ipmroutertmask.is_set or self.ipmroutertmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutertmask.get_name_leafdata())
                if (self.ipmroutertproto.is_set or self.ipmroutertproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutertproto.get_name_leafdata())
                if (self.ipmrouterttype.is_set or self.ipmrouterttype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouterttype.get_name_leafdata())
                if (self.ipmrouteupstreamneighbor.is_set or self.ipmrouteupstreamneighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteupstreamneighbor.get_name_leafdata())
                if (self.ipmrouteuptime.is_set or self.ipmrouteuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteuptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteGroup" or name == "ipMRouteSource" or name == "ipMRouteSourceMask" or name == "ciscoIpMRouteBps" or name == "ciscoIpMRouteBps2" or name == "ciscoIpMRouteConnectedFlag" or name == "ciscoIpMRouteDifferentInIfPkts" or name == "ciscoIpMRouteInLimit" or name == "ciscoIpMRouteInLimit2" or name == "ciscoIpMRouteJoinFlag" or name == "ciscoIpMRouteLastUsed" or name == "ciscoIpMRouteLocalFlag" or name == "ciscoIpMRouteMetric" or name == "ciscoIpMRouteMetric2" or name == "ciscoIpMRouteMetricPreference" or name == "ciscoIpMRouteMsdpFlag" or name == "ciscoIpMRouteOctets" or name == "ciscoIpMRoutePkts" or name == "ciscoIpMRouteProxyJoinFlag" or name == "ciscoIpMRoutePruneFlag" or name == "ciscoIpMRouteRegisterFlag" or name == "ciscoIpMRouteRpFlag" or name == "ciscoIpMRouteSparseFlag" or name == "ciscoIpMRouteSptFlag" or name == "ipMRouteDifferentInIfPackets" or name == "ipMRouteExpiryTime" or name == "ipMRouteHCOctets" or name == "ipMRouteInIfIndex" or name == "ipMRouteOctets" or name == "ipMRoutePkts" or name == "ipMRouteProtocol" or name == "ipMRouteRtAddress" or name == "ipMRouteRtMask" or name == "ipMRouteRtProto" or name == "ipMRouteRtType" or name == "ipMRouteUpstreamNeighbor" or name == "ipMRouteUpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteGroup"):
                    self.ipmroutegroup = value
                    self.ipmroutegroup.value_namespace = name_space
                    self.ipmroutegroup.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteSource"):
                    self.ipmroutesource = value
                    self.ipmroutesource.value_namespace = name_space
                    self.ipmroutesource.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteSourceMask"):
                    self.ipmroutesourcemask = value
                    self.ipmroutesourcemask.value_namespace = name_space
                    self.ipmroutesourcemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteBps"):
                    self.ciscoipmroutebps = value
                    self.ciscoipmroutebps.value_namespace = name_space
                    self.ciscoipmroutebps.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteBps2"):
                    self.ciscoipmroutebps2 = value
                    self.ciscoipmroutebps2.value_namespace = name_space
                    self.ciscoipmroutebps2.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteConnectedFlag"):
                    self.ciscoipmrouteconnectedflag = value
                    self.ciscoipmrouteconnectedflag.value_namespace = name_space
                    self.ciscoipmrouteconnectedflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteDifferentInIfPkts"):
                    self.ciscoipmroutedifferentinifpkts = value
                    self.ciscoipmroutedifferentinifpkts.value_namespace = name_space
                    self.ciscoipmroutedifferentinifpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteInLimit"):
                    self.ciscoipmrouteinlimit = value
                    self.ciscoipmrouteinlimit.value_namespace = name_space
                    self.ciscoipmrouteinlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteInLimit2"):
                    self.ciscoipmrouteinlimit2 = value
                    self.ciscoipmrouteinlimit2.value_namespace = name_space
                    self.ciscoipmrouteinlimit2.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteJoinFlag"):
                    self.ciscoipmroutejoinflag = value
                    self.ciscoipmroutejoinflag.value_namespace = name_space
                    self.ciscoipmroutejoinflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteLastUsed"):
                    self.ciscoipmroutelastused = value
                    self.ciscoipmroutelastused.value_namespace = name_space
                    self.ciscoipmroutelastused.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteLocalFlag"):
                    self.ciscoipmroutelocalflag = value
                    self.ciscoipmroutelocalflag.value_namespace = name_space
                    self.ciscoipmroutelocalflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteMetric"):
                    self.ciscoipmroutemetric = value
                    self.ciscoipmroutemetric.value_namespace = name_space
                    self.ciscoipmroutemetric.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteMetric2"):
                    self.ciscoipmroutemetric2 = value
                    self.ciscoipmroutemetric2.value_namespace = name_space
                    self.ciscoipmroutemetric2.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteMetricPreference"):
                    self.ciscoipmroutemetricpreference = value
                    self.ciscoipmroutemetricpreference.value_namespace = name_space
                    self.ciscoipmroutemetricpreference.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteMsdpFlag"):
                    self.ciscoipmroutemsdpflag = value
                    self.ciscoipmroutemsdpflag.value_namespace = name_space
                    self.ciscoipmroutemsdpflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteOctets"):
                    self.ciscoipmrouteoctets = value
                    self.ciscoipmrouteoctets.value_namespace = name_space
                    self.ciscoipmrouteoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRoutePkts"):
                    self.ciscoipmroutepkts = value
                    self.ciscoipmroutepkts.value_namespace = name_space
                    self.ciscoipmroutepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteProxyJoinFlag"):
                    self.ciscoipmrouteproxyjoinflag = value
                    self.ciscoipmrouteproxyjoinflag.value_namespace = name_space
                    self.ciscoipmrouteproxyjoinflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRoutePruneFlag"):
                    self.ciscoipmroutepruneflag = value
                    self.ciscoipmroutepruneflag.value_namespace = name_space
                    self.ciscoipmroutepruneflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteRegisterFlag"):
                    self.ciscoipmrouteregisterflag = value
                    self.ciscoipmrouteregisterflag.value_namespace = name_space
                    self.ciscoipmrouteregisterflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteRpFlag"):
                    self.ciscoipmrouterpflag = value
                    self.ciscoipmrouterpflag.value_namespace = name_space
                    self.ciscoipmrouterpflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteSparseFlag"):
                    self.ciscoipmroutesparseflag = value
                    self.ciscoipmroutesparseflag.value_namespace = name_space
                    self.ciscoipmroutesparseflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteSptFlag"):
                    self.ciscoipmroutesptflag = value
                    self.ciscoipmroutesptflag.value_namespace = name_space
                    self.ciscoipmroutesptflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteDifferentInIfPackets"):
                    self.ipmroutedifferentinifpackets = value
                    self.ipmroutedifferentinifpackets.value_namespace = name_space
                    self.ipmroutedifferentinifpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteExpiryTime"):
                    self.ipmrouteexpirytime = value
                    self.ipmrouteexpirytime.value_namespace = name_space
                    self.ipmrouteexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteHCOctets"):
                    self.ipmroutehcoctets = value
                    self.ipmroutehcoctets.value_namespace = name_space
                    self.ipmroutehcoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInIfIndex"):
                    self.ipmrouteinifindex = value
                    self.ipmrouteinifindex.value_namespace = name_space
                    self.ipmrouteinifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteOctets"):
                    self.ipmrouteoctets = value
                    self.ipmrouteoctets.value_namespace = name_space
                    self.ipmrouteoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRoutePkts"):
                    self.ipmroutepkts = value
                    self.ipmroutepkts.value_namespace = name_space
                    self.ipmroutepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteProtocol"):
                    self.ipmrouteprotocol = value
                    self.ipmrouteprotocol.value_namespace = name_space
                    self.ipmrouteprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteRtAddress"):
                    self.ipmroutertaddress = value
                    self.ipmroutertaddress.value_namespace = name_space
                    self.ipmroutertaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteRtMask"):
                    self.ipmroutertmask = value
                    self.ipmroutertmask.value_namespace = name_space
                    self.ipmroutertmask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteRtProto"):
                    self.ipmroutertproto = value
                    self.ipmroutertproto.value_namespace = name_space
                    self.ipmroutertproto.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteRtType"):
                    self.ipmrouterttype = value
                    self.ipmrouterttype.value_namespace = name_space
                    self.ipmrouterttype.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteUpstreamNeighbor"):
                    self.ipmrouteupstreamneighbor = value
                    self.ipmrouteupstreamneighbor.value_namespace = name_space
                    self.ipmrouteupstreamneighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteUpTime"):
                    self.ipmrouteuptime = value
                    self.ipmrouteuptime.value_namespace = name_space
                    self.ipmrouteuptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipmrouteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipmrouteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipMRouteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipMRouteEntry"):
                for c in self.ipmrouteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpmrouteStdMib.Ipmroutetable.Ipmrouteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipmrouteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipMRouteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipmroutenexthoptable(Entity):
        """
        The (conceptual) table containing information on the next\-
        hops on outgoing interfaces for routing IP multicast
        datagrams.  Each entry is one of a list of next\-hops on
        outgoing interfaces for particular sources sending to a
        particular multicast group address.
        
        .. attribute:: ipmroutenexthopentry
        
        	An entry (conceptual row) in the list of next\-hops on outgoing interfaces to which IP multicast datagrams from particular sources to a IP multicast group address are routed.  Discontinuities in counters in this entry can be detected by observing the value of ipMRouteUpTime
        	**type**\: list of    :py:class:`Ipmroutenexthopentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IpmrouteStdMib.Ipmroutenexthoptable, self).__init__()

            self.yang_name = "ipMRouteNextHopTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"

            self.ipmroutenexthopentry = YList(self)

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
                        super(IpmrouteStdMib.Ipmroutenexthoptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpmrouteStdMib.Ipmroutenexthoptable, self).__setattr__(name, value)


        class Ipmroutenexthopentry(Entity):
            """
            An entry (conceptual row) in the list of next\-hops on
            outgoing interfaces to which IP multicast datagrams from
            particular sources to a IP multicast group address are
            routed.  Discontinuities in counters in this entry can be
            detected by observing the value of ipMRouteUpTime.
            
            .. attribute:: ipmroutenexthopgroup  <key>
            
            	The IP multicast group for which this entry specifies a next\-hop on an outgoing interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopsource  <key>
            
            	The network address which when combined with the corresponding value of ipMRouteNextHopSourceMask identifies the sources for which this entry specifies a next\-hop on an outgoing interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopsourcemask  <key>
            
            	The network mask which when combined with the corresponding value of ipMRouteNextHopSource identifies the sources for which this entry specifies a next\-hop on an outgoing interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopifindex  <key>
            
            	The ifIndex value of the interface for the outgoing interface for this next\-hop
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipmroutenexthopaddress  <key>
            
            	The address of the next\-hop specific to this entry.  For most interfaces, this is identical to ipMRouteNextHopGroup. NBMA interfaces, however, may have multiple next\-hop addresses out a single outgoing interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmroutenexthopmachdr
            
            	The data link mac address header for a multicast datagram. Used by IP multicast fastswitching
            	**type**\:  str
            
            .. attribute:: ciscoipmroutenexthopoutlimit
            
            	An outgoing interface's limit for rate limiting data traffic, in Kbps
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: Kbits/second
            
            .. attribute:: ciscoipmroutenexthoppkts
            
            	The number of packets which have been forwarded using this route. This object is a 64\-bit version of ipMRouteNextHopPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipmroutenexthopclosestmemberhops
            
            	The minimum number of hops between this router and any member of this IP multicast group reached via this next\-hop on this outgoing interface.  Any IP multicast datagrams for the group which have a TTL less than this number of hops will not be forwarded to this next\-hop
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipmroutenexthopexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  If ipMRouteNextHopState is pruned(1), the remaining time until the prune expires and the state reverts to forwarding(2).  Otherwise, the remaining time until this entry is removed from the table.  The time remaining may be copied from ipMRouteExpiryTime if the protocol in use for this entry does not specify next\-hop timers.  The value 0      indicates that the entry is not subject to aging
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutenexthoppkts
            
            	The number of packets which have been forwarded using this route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmroutenexthopprotocol
            
            	The routing mechanism via which this next\-hop was learned
            	**type**\:   :py:class:`Ianaipmrouteprotocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.Ianaipmrouteprotocol>`
            
            .. attribute:: ipmroutenexthopstate
            
            	An indication of whether the outgoing interface and next\- hop represented by this entry is currently being used to forward IP datagrams.  The value 'forwarding' indicates it is currently being used; the value 'pruned' indicates it is not
            	**type**\:   :py:class:`Ipmroutenexthopstate <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry.Ipmroutenexthopstate>`
            
            .. attribute:: ipmroutenexthopuptime
            
            	The time since the multicast routing information represented by this entry was learned by the router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry, self).__init__()

                self.yang_name = "ipMRouteNextHopEntry"
                self.yang_parent_name = "ipMRouteNextHopTable"

                self.ipmroutenexthopgroup = YLeaf(YType.str, "ipMRouteNextHopGroup")

                self.ipmroutenexthopsource = YLeaf(YType.str, "ipMRouteNextHopSource")

                self.ipmroutenexthopsourcemask = YLeaf(YType.str, "ipMRouteNextHopSourceMask")

                self.ipmroutenexthopifindex = YLeaf(YType.int32, "ipMRouteNextHopIfIndex")

                self.ipmroutenexthopaddress = YLeaf(YType.str, "ipMRouteNextHopAddress")

                self.ciscoipmroutenexthopmachdr = YLeaf(YType.str, "CISCO-IPMROUTE-MIB:ciscoIpMRouteNextHopMacHdr")

                self.ciscoipmroutenexthopoutlimit = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteNextHopOutLimit")

                self.ciscoipmroutenexthoppkts = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteNextHopPkts")

                self.ipmroutenexthopclosestmemberhops = YLeaf(YType.int32, "ipMRouteNextHopClosestMemberHops")

                self.ipmroutenexthopexpirytime = YLeaf(YType.uint32, "ipMRouteNextHopExpiryTime")

                self.ipmroutenexthoppkts = YLeaf(YType.uint32, "ipMRouteNextHopPkts")

                self.ipmroutenexthopprotocol = YLeaf(YType.enumeration, "ipMRouteNextHopProtocol")

                self.ipmroutenexthopstate = YLeaf(YType.enumeration, "ipMRouteNextHopState")

                self.ipmroutenexthopuptime = YLeaf(YType.uint32, "ipMRouteNextHopUpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmroutenexthopgroup",
                                "ipmroutenexthopsource",
                                "ipmroutenexthopsourcemask",
                                "ipmroutenexthopifindex",
                                "ipmroutenexthopaddress",
                                "ciscoipmroutenexthopmachdr",
                                "ciscoipmroutenexthopoutlimit",
                                "ciscoipmroutenexthoppkts",
                                "ipmroutenexthopclosestmemberhops",
                                "ipmroutenexthopexpirytime",
                                "ipmroutenexthoppkts",
                                "ipmroutenexthopprotocol",
                                "ipmroutenexthopstate",
                                "ipmroutenexthopuptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry, self).__setattr__(name, value)

            class Ipmroutenexthopstate(Enum):
                """
                Ipmroutenexthopstate

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


            def has_data(self):
                return (
                    self.ipmroutenexthopgroup.is_set or
                    self.ipmroutenexthopsource.is_set or
                    self.ipmroutenexthopsourcemask.is_set or
                    self.ipmroutenexthopifindex.is_set or
                    self.ipmroutenexthopaddress.is_set or
                    self.ciscoipmroutenexthopmachdr.is_set or
                    self.ciscoipmroutenexthopoutlimit.is_set or
                    self.ciscoipmroutenexthoppkts.is_set or
                    self.ipmroutenexthopclosestmemberhops.is_set or
                    self.ipmroutenexthopexpirytime.is_set or
                    self.ipmroutenexthoppkts.is_set or
                    self.ipmroutenexthopprotocol.is_set or
                    self.ipmroutenexthopstate.is_set or
                    self.ipmroutenexthopuptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmroutenexthopgroup.yfilter != YFilter.not_set or
                    self.ipmroutenexthopsource.yfilter != YFilter.not_set or
                    self.ipmroutenexthopsourcemask.yfilter != YFilter.not_set or
                    self.ipmroutenexthopifindex.yfilter != YFilter.not_set or
                    self.ipmroutenexthopaddress.yfilter != YFilter.not_set or
                    self.ciscoipmroutenexthopmachdr.yfilter != YFilter.not_set or
                    self.ciscoipmroutenexthopoutlimit.yfilter != YFilter.not_set or
                    self.ciscoipmroutenexthoppkts.yfilter != YFilter.not_set or
                    self.ipmroutenexthopclosestmemberhops.yfilter != YFilter.not_set or
                    self.ipmroutenexthopexpirytime.yfilter != YFilter.not_set or
                    self.ipmroutenexthoppkts.yfilter != YFilter.not_set or
                    self.ipmroutenexthopprotocol.yfilter != YFilter.not_set or
                    self.ipmroutenexthopstate.yfilter != YFilter.not_set or
                    self.ipmroutenexthopuptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipMRouteNextHopEntry" + "[ipMRouteNextHopGroup='" + self.ipmroutenexthopgroup.get() + "']" + "[ipMRouteNextHopSource='" + self.ipmroutenexthopsource.get() + "']" + "[ipMRouteNextHopSourceMask='" + self.ipmroutenexthopsourcemask.get() + "']" + "[ipMRouteNextHopIfIndex='" + self.ipmroutenexthopifindex.get() + "']" + "[ipMRouteNextHopAddress='" + self.ipmroutenexthopaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteNextHopTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmroutenexthopgroup.is_set or self.ipmroutenexthopgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopgroup.get_name_leafdata())
                if (self.ipmroutenexthopsource.is_set or self.ipmroutenexthopsource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopsource.get_name_leafdata())
                if (self.ipmroutenexthopsourcemask.is_set or self.ipmroutenexthopsourcemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopsourcemask.get_name_leafdata())
                if (self.ipmroutenexthopifindex.is_set or self.ipmroutenexthopifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopifindex.get_name_leafdata())
                if (self.ipmroutenexthopaddress.is_set or self.ipmroutenexthopaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopaddress.get_name_leafdata())
                if (self.ciscoipmroutenexthopmachdr.is_set or self.ciscoipmroutenexthopmachdr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutenexthopmachdr.get_name_leafdata())
                if (self.ciscoipmroutenexthopoutlimit.is_set or self.ciscoipmroutenexthopoutlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutenexthopoutlimit.get_name_leafdata())
                if (self.ciscoipmroutenexthoppkts.is_set or self.ciscoipmroutenexthoppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmroutenexthoppkts.get_name_leafdata())
                if (self.ipmroutenexthopclosestmemberhops.is_set or self.ipmroutenexthopclosestmemberhops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopclosestmemberhops.get_name_leafdata())
                if (self.ipmroutenexthopexpirytime.is_set or self.ipmroutenexthopexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopexpirytime.get_name_leafdata())
                if (self.ipmroutenexthoppkts.is_set or self.ipmroutenexthoppkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthoppkts.get_name_leafdata())
                if (self.ipmroutenexthopprotocol.is_set or self.ipmroutenexthopprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopprotocol.get_name_leafdata())
                if (self.ipmroutenexthopstate.is_set or self.ipmroutenexthopstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopstate.get_name_leafdata())
                if (self.ipmroutenexthopuptime.is_set or self.ipmroutenexthopuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopuptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteNextHopGroup" or name == "ipMRouteNextHopSource" or name == "ipMRouteNextHopSourceMask" or name == "ipMRouteNextHopIfIndex" or name == "ipMRouteNextHopAddress" or name == "ciscoIpMRouteNextHopMacHdr" or name == "ciscoIpMRouteNextHopOutLimit" or name == "ciscoIpMRouteNextHopPkts" or name == "ipMRouteNextHopClosestMemberHops" or name == "ipMRouteNextHopExpiryTime" or name == "ipMRouteNextHopPkts" or name == "ipMRouteNextHopProtocol" or name == "ipMRouteNextHopState" or name == "ipMRouteNextHopUpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteNextHopGroup"):
                    self.ipmroutenexthopgroup = value
                    self.ipmroutenexthopgroup.value_namespace = name_space
                    self.ipmroutenexthopgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopSource"):
                    self.ipmroutenexthopsource = value
                    self.ipmroutenexthopsource.value_namespace = name_space
                    self.ipmroutenexthopsource.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopSourceMask"):
                    self.ipmroutenexthopsourcemask = value
                    self.ipmroutenexthopsourcemask.value_namespace = name_space
                    self.ipmroutenexthopsourcemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopIfIndex"):
                    self.ipmroutenexthopifindex = value
                    self.ipmroutenexthopifindex.value_namespace = name_space
                    self.ipmroutenexthopifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopAddress"):
                    self.ipmroutenexthopaddress = value
                    self.ipmroutenexthopaddress.value_namespace = name_space
                    self.ipmroutenexthopaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteNextHopMacHdr"):
                    self.ciscoipmroutenexthopmachdr = value
                    self.ciscoipmroutenexthopmachdr.value_namespace = name_space
                    self.ciscoipmroutenexthopmachdr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteNextHopOutLimit"):
                    self.ciscoipmroutenexthopoutlimit = value
                    self.ciscoipmroutenexthopoutlimit.value_namespace = name_space
                    self.ciscoipmroutenexthopoutlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteNextHopPkts"):
                    self.ciscoipmroutenexthoppkts = value
                    self.ciscoipmroutenexthoppkts.value_namespace = name_space
                    self.ciscoipmroutenexthoppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopClosestMemberHops"):
                    self.ipmroutenexthopclosestmemberhops = value
                    self.ipmroutenexthopclosestmemberhops.value_namespace = name_space
                    self.ipmroutenexthopclosestmemberhops.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopExpiryTime"):
                    self.ipmroutenexthopexpirytime = value
                    self.ipmroutenexthopexpirytime.value_namespace = name_space
                    self.ipmroutenexthopexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopPkts"):
                    self.ipmroutenexthoppkts = value
                    self.ipmroutenexthoppkts.value_namespace = name_space
                    self.ipmroutenexthoppkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopProtocol"):
                    self.ipmroutenexthopprotocol = value
                    self.ipmroutenexthopprotocol.value_namespace = name_space
                    self.ipmroutenexthopprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopState"):
                    self.ipmroutenexthopstate = value
                    self.ipmroutenexthopstate.value_namespace = name_space
                    self.ipmroutenexthopstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopUpTime"):
                    self.ipmroutenexthopuptime = value
                    self.ipmroutenexthopuptime.value_namespace = name_space
                    self.ipmroutenexthopuptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipmroutenexthopentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipmroutenexthopentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipMRouteNextHopTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipMRouteNextHopEntry"):
                for c in self.ipmroutenexthopentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipmroutenexthopentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipMRouteNextHopEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipmrouteinterfacetable(Entity):
        """
        The (conceptual) table containing multicast routing
        information specific to interfaces.
        
        .. attribute:: ipmrouteinterfaceentry
        
        	An entry (conceptual row) containing the multicast routing information for a particular interface
        	**type**\: list of    :py:class:`Ipmrouteinterfaceentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IpmrouteStdMib.Ipmrouteinterfacetable, self).__init__()

            self.yang_name = "ipMRouteInterfaceTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"

            self.ipmrouteinterfaceentry = YList(self)

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
                        super(IpmrouteStdMib.Ipmrouteinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpmrouteStdMib.Ipmrouteinterfacetable, self).__setattr__(name, value)


        class Ipmrouteinterfaceentry(Entity):
            """
            An entry (conceptual row) containing the multicast routing
            information for a particular interface.
            
            .. attribute:: ipmrouteinterfaceifindex  <key>
            
            	The ifIndex value of the interface for which this entry contains information
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscoipmrouteifhcinmcastpkts
            
            	The number of multicast packets that have arrived on the interface. This object is a 64\-bit version of ciscoIpMRouteIfInMcastPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifhcoutmcastpkts
            
            	The number of multicast packets that have been sent on the interface. This object is a 64\-bit version of ciscoIpMRouteIfOutMcastPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifinmcastoctets
            
            	The number of octets of multicast packets that have arrived on the interface. This object is a 64\-bit version of ipMRouteInterfaceInMcastOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifinmcastpkts
            
            	The number of multicast packets that have arrived on the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteifoutmcastoctets
            
            	The number of octets of multicast packets that have been sent on the interface. This object is a 64\-bit version of ipMRouteInterfaceOutMcastOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoipmrouteifoutmcastpkts
            
            	The number of multicast packets that have been sent on the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteinterfacehcinmcastoctets
            
            	The number of octets of multicast packets that have arrived on the interface, including framing characters.  This object is a 64\-bit version of ipMRouteInterfaceInMcastOctets.  It is similar to ifHCInOctets in the Interfaces MIB, except that only multicast packets are counted
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipmrouteinterfacehcoutmcastoctets
            
            	The number of octets of multicast packets that have been      sent on the interface.  This object is a 64\-bit version of ipMRouteInterfaceOutMcastOctets
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipmrouteinterfaceinmcastoctets
            
            	The number of octets of multicast packets that have arrived on the interface, including framing characters.  This object is similar to ifInOctets in the Interfaces MIB, except that only multicast packets are counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteinterfaceoutmcastoctets
            
            	The number of octets of multicast packets that have been sent on the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipmrouteinterfaceprotocol
            
            	The routing protocol running on this interface
            	**type**\:   :py:class:`Ianaipmrouteprotocol <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.Ianaipmrouteprotocol>`
            
            .. attribute:: ipmrouteinterfaceratelimit
            
            	The rate\-limit, in kilobits per second, of forwarded multicast traffic on the interface.  A rate\-limit of 0 indicates that no rate limiting is done
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipmrouteinterfacettl
            
            	The datagram TTL threshold for the interface. Any IP multicast datagrams with a TTL less than this threshold will not be forwarded out the interface. The default value of 0 means all multicast packets are forwarded out the interface
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry, self).__init__()

                self.yang_name = "ipMRouteInterfaceEntry"
                self.yang_parent_name = "ipMRouteInterfaceTable"

                self.ipmrouteinterfaceifindex = YLeaf(YType.int32, "ipMRouteInterfaceIfIndex")

                self.ciscoipmrouteifhcinmcastpkts = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteIfHCInMcastPkts")

                self.ciscoipmrouteifhcoutmcastpkts = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteIfHCOutMcastPkts")

                self.ciscoipmrouteifinmcastoctets = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteIfInMcastOctets")

                self.ciscoipmrouteifinmcastpkts = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteIfInMcastPkts")

                self.ciscoipmrouteifoutmcastoctets = YLeaf(YType.uint64, "CISCO-IPMROUTE-MIB:ciscoIpMRouteIfOutMcastOctets")

                self.ciscoipmrouteifoutmcastpkts = YLeaf(YType.uint32, "CISCO-IPMROUTE-MIB:ciscoIpMRouteIfOutMcastPkts")

                self.ipmrouteinterfacehcinmcastoctets = YLeaf(YType.uint64, "ipMRouteInterfaceHCInMcastOctets")

                self.ipmrouteinterfacehcoutmcastoctets = YLeaf(YType.uint64, "ipMRouteInterfaceHCOutMcastOctets")

                self.ipmrouteinterfaceinmcastoctets = YLeaf(YType.uint32, "ipMRouteInterfaceInMcastOctets")

                self.ipmrouteinterfaceoutmcastoctets = YLeaf(YType.uint32, "ipMRouteInterfaceOutMcastOctets")

                self.ipmrouteinterfaceprotocol = YLeaf(YType.enumeration, "ipMRouteInterfaceProtocol")

                self.ipmrouteinterfaceratelimit = YLeaf(YType.int32, "ipMRouteInterfaceRateLimit")

                self.ipmrouteinterfacettl = YLeaf(YType.int32, "ipMRouteInterfaceTtl")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmrouteinterfaceifindex",
                                "ciscoipmrouteifhcinmcastpkts",
                                "ciscoipmrouteifhcoutmcastpkts",
                                "ciscoipmrouteifinmcastoctets",
                                "ciscoipmrouteifinmcastpkts",
                                "ciscoipmrouteifoutmcastoctets",
                                "ciscoipmrouteifoutmcastpkts",
                                "ipmrouteinterfacehcinmcastoctets",
                                "ipmrouteinterfacehcoutmcastoctets",
                                "ipmrouteinterfaceinmcastoctets",
                                "ipmrouteinterfaceoutmcastoctets",
                                "ipmrouteinterfaceprotocol",
                                "ipmrouteinterfaceratelimit",
                                "ipmrouteinterfacettl") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipmrouteinterfaceifindex.is_set or
                    self.ciscoipmrouteifhcinmcastpkts.is_set or
                    self.ciscoipmrouteifhcoutmcastpkts.is_set or
                    self.ciscoipmrouteifinmcastoctets.is_set or
                    self.ciscoipmrouteifinmcastpkts.is_set or
                    self.ciscoipmrouteifoutmcastoctets.is_set or
                    self.ciscoipmrouteifoutmcastpkts.is_set or
                    self.ipmrouteinterfacehcinmcastoctets.is_set or
                    self.ipmrouteinterfacehcoutmcastoctets.is_set or
                    self.ipmrouteinterfaceinmcastoctets.is_set or
                    self.ipmrouteinterfaceoutmcastoctets.is_set or
                    self.ipmrouteinterfaceprotocol.is_set or
                    self.ipmrouteinterfaceratelimit.is_set or
                    self.ipmrouteinterfacettl.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmrouteinterfaceifindex.yfilter != YFilter.not_set or
                    self.ciscoipmrouteifhcinmcastpkts.yfilter != YFilter.not_set or
                    self.ciscoipmrouteifhcoutmcastpkts.yfilter != YFilter.not_set or
                    self.ciscoipmrouteifinmcastoctets.yfilter != YFilter.not_set or
                    self.ciscoipmrouteifinmcastpkts.yfilter != YFilter.not_set or
                    self.ciscoipmrouteifoutmcastoctets.yfilter != YFilter.not_set or
                    self.ciscoipmrouteifoutmcastpkts.yfilter != YFilter.not_set or
                    self.ipmrouteinterfacehcinmcastoctets.yfilter != YFilter.not_set or
                    self.ipmrouteinterfacehcoutmcastoctets.yfilter != YFilter.not_set or
                    self.ipmrouteinterfaceinmcastoctets.yfilter != YFilter.not_set or
                    self.ipmrouteinterfaceoutmcastoctets.yfilter != YFilter.not_set or
                    self.ipmrouteinterfaceprotocol.yfilter != YFilter.not_set or
                    self.ipmrouteinterfaceratelimit.yfilter != YFilter.not_set or
                    self.ipmrouteinterfacettl.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipMRouteInterfaceEntry" + "[ipMRouteInterfaceIfIndex='" + self.ipmrouteinterfaceifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmrouteinterfaceifindex.is_set or self.ipmrouteinterfaceifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfaceifindex.get_name_leafdata())
                if (self.ciscoipmrouteifhcinmcastpkts.is_set or self.ciscoipmrouteifhcinmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteifhcinmcastpkts.get_name_leafdata())
                if (self.ciscoipmrouteifhcoutmcastpkts.is_set or self.ciscoipmrouteifhcoutmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteifhcoutmcastpkts.get_name_leafdata())
                if (self.ciscoipmrouteifinmcastoctets.is_set or self.ciscoipmrouteifinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteifinmcastoctets.get_name_leafdata())
                if (self.ciscoipmrouteifinmcastpkts.is_set or self.ciscoipmrouteifinmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteifinmcastpkts.get_name_leafdata())
                if (self.ciscoipmrouteifoutmcastoctets.is_set or self.ciscoipmrouteifoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteifoutmcastoctets.get_name_leafdata())
                if (self.ciscoipmrouteifoutmcastpkts.is_set or self.ciscoipmrouteifoutmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoipmrouteifoutmcastpkts.get_name_leafdata())
                if (self.ipmrouteinterfacehcinmcastoctets.is_set or self.ipmrouteinterfacehcinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfacehcinmcastoctets.get_name_leafdata())
                if (self.ipmrouteinterfacehcoutmcastoctets.is_set or self.ipmrouteinterfacehcoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfacehcoutmcastoctets.get_name_leafdata())
                if (self.ipmrouteinterfaceinmcastoctets.is_set or self.ipmrouteinterfaceinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfaceinmcastoctets.get_name_leafdata())
                if (self.ipmrouteinterfaceoutmcastoctets.is_set or self.ipmrouteinterfaceoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfaceoutmcastoctets.get_name_leafdata())
                if (self.ipmrouteinterfaceprotocol.is_set or self.ipmrouteinterfaceprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfaceprotocol.get_name_leafdata())
                if (self.ipmrouteinterfaceratelimit.is_set or self.ipmrouteinterfaceratelimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfaceratelimit.get_name_leafdata())
                if (self.ipmrouteinterfacettl.is_set or self.ipmrouteinterfacettl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteinterfacettl.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteInterfaceIfIndex" or name == "ciscoIpMRouteIfHCInMcastPkts" or name == "ciscoIpMRouteIfHCOutMcastPkts" or name == "ciscoIpMRouteIfInMcastOctets" or name == "ciscoIpMRouteIfInMcastPkts" or name == "ciscoIpMRouteIfOutMcastOctets" or name == "ciscoIpMRouteIfOutMcastPkts" or name == "ipMRouteInterfaceHCInMcastOctets" or name == "ipMRouteInterfaceHCOutMcastOctets" or name == "ipMRouteInterfaceInMcastOctets" or name == "ipMRouteInterfaceOutMcastOctets" or name == "ipMRouteInterfaceProtocol" or name == "ipMRouteInterfaceRateLimit" or name == "ipMRouteInterfaceTtl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteInterfaceIfIndex"):
                    self.ipmrouteinterfaceifindex = value
                    self.ipmrouteinterfaceifindex.value_namespace = name_space
                    self.ipmrouteinterfaceifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteIfHCInMcastPkts"):
                    self.ciscoipmrouteifhcinmcastpkts = value
                    self.ciscoipmrouteifhcinmcastpkts.value_namespace = name_space
                    self.ciscoipmrouteifhcinmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteIfHCOutMcastPkts"):
                    self.ciscoipmrouteifhcoutmcastpkts = value
                    self.ciscoipmrouteifhcoutmcastpkts.value_namespace = name_space
                    self.ciscoipmrouteifhcoutmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteIfInMcastOctets"):
                    self.ciscoipmrouteifinmcastoctets = value
                    self.ciscoipmrouteifinmcastoctets.value_namespace = name_space
                    self.ciscoipmrouteifinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteIfInMcastPkts"):
                    self.ciscoipmrouteifinmcastpkts = value
                    self.ciscoipmrouteifinmcastpkts.value_namespace = name_space
                    self.ciscoipmrouteifinmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteIfOutMcastOctets"):
                    self.ciscoipmrouteifoutmcastoctets = value
                    self.ciscoipmrouteifoutmcastoctets.value_namespace = name_space
                    self.ciscoipmrouteifoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoIpMRouteIfOutMcastPkts"):
                    self.ciscoipmrouteifoutmcastpkts = value
                    self.ciscoipmrouteifoutmcastpkts.value_namespace = name_space
                    self.ciscoipmrouteifoutmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceHCInMcastOctets"):
                    self.ipmrouteinterfacehcinmcastoctets = value
                    self.ipmrouteinterfacehcinmcastoctets.value_namespace = name_space
                    self.ipmrouteinterfacehcinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceHCOutMcastOctets"):
                    self.ipmrouteinterfacehcoutmcastoctets = value
                    self.ipmrouteinterfacehcoutmcastoctets.value_namespace = name_space
                    self.ipmrouteinterfacehcoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceInMcastOctets"):
                    self.ipmrouteinterfaceinmcastoctets = value
                    self.ipmrouteinterfaceinmcastoctets.value_namespace = name_space
                    self.ipmrouteinterfaceinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceOutMcastOctets"):
                    self.ipmrouteinterfaceoutmcastoctets = value
                    self.ipmrouteinterfaceoutmcastoctets.value_namespace = name_space
                    self.ipmrouteinterfaceoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceProtocol"):
                    self.ipmrouteinterfaceprotocol = value
                    self.ipmrouteinterfaceprotocol.value_namespace = name_space
                    self.ipmrouteinterfaceprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceRateLimit"):
                    self.ipmrouteinterfaceratelimit = value
                    self.ipmrouteinterfaceratelimit.value_namespace = name_space
                    self.ipmrouteinterfaceratelimit.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteInterfaceTtl"):
                    self.ipmrouteinterfacettl = value
                    self.ipmrouteinterfacettl.value_namespace = name_space
                    self.ipmrouteinterfacettl.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipmrouteinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipmrouteinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipMRouteInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipMRouteInterfaceEntry"):
                for c in self.ipmrouteinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipmrouteinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipMRouteInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipmrouteboundarytable(Entity):
        """
        The (conceptual) table listing the router's scoped
        multicast address boundaries.
        
        .. attribute:: ipmrouteboundaryentry
        
        	An entry (conceptual row) in the ipMRouteBoundaryTable representing a scoped boundary
        	**type**\: list of    :py:class:`Ipmrouteboundaryentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IpmrouteStdMib.Ipmrouteboundarytable, self).__init__()

            self.yang_name = "ipMRouteBoundaryTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"

            self.ipmrouteboundaryentry = YList(self)

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
                        super(IpmrouteStdMib.Ipmrouteboundarytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpmrouteStdMib.Ipmrouteboundarytable, self).__setattr__(name, value)


        class Ipmrouteboundaryentry(Entity):
            """
            An entry (conceptual row) in the ipMRouteBoundaryTable
            representing a scoped boundary.
            
            .. attribute:: ipmrouteboundaryifindex  <key>
            
            	The IfIndex value for the interface to which this boundary applies.  Packets with a destination address in the associated address/mask range will not be forwarded out this interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipmrouteboundaryaddress  <key>
            
            	The group address which when combined with the corresponding value of ipMRouteBoundaryAddressMask identifies the group range for which the scoped boundary exists.  Scoped addresses must come from the range 239.x.x.x as specified in RFC 2365
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteboundaryaddressmask  <key>
            
            	The group address mask which when combined with the corresponding value of ipMRouteBoundaryAddress identifies the group range for which the scoped boundary exists
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmrouteboundarystatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry, self).__init__()

                self.yang_name = "ipMRouteBoundaryEntry"
                self.yang_parent_name = "ipMRouteBoundaryTable"

                self.ipmrouteboundaryifindex = YLeaf(YType.int32, "ipMRouteBoundaryIfIndex")

                self.ipmrouteboundaryaddress = YLeaf(YType.str, "ipMRouteBoundaryAddress")

                self.ipmrouteboundaryaddressmask = YLeaf(YType.str, "ipMRouteBoundaryAddressMask")

                self.ipmrouteboundarystatus = YLeaf(YType.enumeration, "ipMRouteBoundaryStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmrouteboundaryifindex",
                                "ipmrouteboundaryaddress",
                                "ipmrouteboundaryaddressmask",
                                "ipmrouteboundarystatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipmrouteboundaryifindex.is_set or
                    self.ipmrouteboundaryaddress.is_set or
                    self.ipmrouteboundaryaddressmask.is_set or
                    self.ipmrouteboundarystatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmrouteboundaryifindex.yfilter != YFilter.not_set or
                    self.ipmrouteboundaryaddress.yfilter != YFilter.not_set or
                    self.ipmrouteboundaryaddressmask.yfilter != YFilter.not_set or
                    self.ipmrouteboundarystatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipMRouteBoundaryEntry" + "[ipMRouteBoundaryIfIndex='" + self.ipmrouteboundaryifindex.get() + "']" + "[ipMRouteBoundaryAddress='" + self.ipmrouteboundaryaddress.get() + "']" + "[ipMRouteBoundaryAddressMask='" + self.ipmrouteboundaryaddressmask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteBoundaryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmrouteboundaryifindex.is_set or self.ipmrouteboundaryifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteboundaryifindex.get_name_leafdata())
                if (self.ipmrouteboundaryaddress.is_set or self.ipmrouteboundaryaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteboundaryaddress.get_name_leafdata())
                if (self.ipmrouteboundaryaddressmask.is_set or self.ipmrouteboundaryaddressmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteboundaryaddressmask.get_name_leafdata())
                if (self.ipmrouteboundarystatus.is_set or self.ipmrouteboundarystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmrouteboundarystatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteBoundaryIfIndex" or name == "ipMRouteBoundaryAddress" or name == "ipMRouteBoundaryAddressMask" or name == "ipMRouteBoundaryStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteBoundaryIfIndex"):
                    self.ipmrouteboundaryifindex = value
                    self.ipmrouteboundaryifindex.value_namespace = name_space
                    self.ipmrouteboundaryifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteBoundaryAddress"):
                    self.ipmrouteboundaryaddress = value
                    self.ipmrouteboundaryaddress.value_namespace = name_space
                    self.ipmrouteboundaryaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteBoundaryAddressMask"):
                    self.ipmrouteboundaryaddressmask = value
                    self.ipmrouteboundaryaddressmask.value_namespace = name_space
                    self.ipmrouteboundaryaddressmask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteBoundaryStatus"):
                    self.ipmrouteboundarystatus = value
                    self.ipmrouteboundarystatus.value_namespace = name_space
                    self.ipmrouteboundarystatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipmrouteboundaryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipmrouteboundaryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipMRouteBoundaryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipMRouteBoundaryEntry"):
                for c in self.ipmrouteboundaryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipmrouteboundaryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipMRouteBoundaryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipmroutescopenametable(Entity):
        """
        The (conceptual) table listing the multicast scope names.
        
        .. attribute:: ipmroutescopenameentry
        
        	An entry (conceptual row) in the ipMRouteScopeNameTable representing a multicast scope name
        	**type**\: list of    :py:class:`Ipmroutescopenameentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            super(IpmrouteStdMib.Ipmroutescopenametable, self).__init__()

            self.yang_name = "ipMRouteScopeNameTable"
            self.yang_parent_name = "IPMROUTE-STD-MIB"

            self.ipmroutescopenameentry = YList(self)

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
                        super(IpmrouteStdMib.Ipmroutescopenametable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpmrouteStdMib.Ipmroutescopenametable, self).__setattr__(name, value)


        class Ipmroutescopenameentry(Entity):
            """
            An entry (conceptual row) in the ipMRouteScopeNameTable
            representing a multicast scope name.
            
            .. attribute:: ipmroutescopenameaddress  <key>
            
            	The group address which when combined with the corresponding value of ipMRouteScopeNameAddressMask identifies the group range associated with the multicast scope.  Scoped addresses must come from the range 239.x.x.x
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutescopenameaddressmask  <key>
            
            	The group address mask which when combined with the corresponding value of ipMRouteScopeNameAddress identifies the group range associated with the multicast scope
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutescopenamelanguage  <key>
            
            	The RFC 1766\-style language tag associated with the scope name
            	**type**\:  str
            
            .. attribute:: ipmroutescopenamedefault
            
            	If true, indicates a preference that the name in the following language should be used by applications if no name is available in a desired language
            	**type**\:  bool
            
            .. attribute:: ipmroutescopenamestatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ipmroutescopenamestring
            
            	The textual name associated with the multicast scope.  The value of this object should be suitable for displaying to end\-users, such as when allocating a multicast address in this scope.  When no name is specified, the default value of this object should be the string 239.x.x.x/y with x and y replaced appropriately to describe the address and mask length associated with the scope
            	**type**\:  str
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                super(IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry, self).__init__()

                self.yang_name = "ipMRouteScopeNameEntry"
                self.yang_parent_name = "ipMRouteScopeNameTable"

                self.ipmroutescopenameaddress = YLeaf(YType.str, "ipMRouteScopeNameAddress")

                self.ipmroutescopenameaddressmask = YLeaf(YType.str, "ipMRouteScopeNameAddressMask")

                self.ipmroutescopenamelanguage = YLeaf(YType.str, "ipMRouteScopeNameLanguage")

                self.ipmroutescopenamedefault = YLeaf(YType.boolean, "ipMRouteScopeNameDefault")

                self.ipmroutescopenamestatus = YLeaf(YType.enumeration, "ipMRouteScopeNameStatus")

                self.ipmroutescopenamestring = YLeaf(YType.str, "ipMRouteScopeNameString")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmroutescopenameaddress",
                                "ipmroutescopenameaddressmask",
                                "ipmroutescopenamelanguage",
                                "ipmroutescopenamedefault",
                                "ipmroutescopenamestatus",
                                "ipmroutescopenamestring") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipmroutescopenameaddress.is_set or
                    self.ipmroutescopenameaddressmask.is_set or
                    self.ipmroutescopenamelanguage.is_set or
                    self.ipmroutescopenamedefault.is_set or
                    self.ipmroutescopenamestatus.is_set or
                    self.ipmroutescopenamestring.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmroutescopenameaddress.yfilter != YFilter.not_set or
                    self.ipmroutescopenameaddressmask.yfilter != YFilter.not_set or
                    self.ipmroutescopenamelanguage.yfilter != YFilter.not_set or
                    self.ipmroutescopenamedefault.yfilter != YFilter.not_set or
                    self.ipmroutescopenamestatus.yfilter != YFilter.not_set or
                    self.ipmroutescopenamestring.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipMRouteScopeNameEntry" + "[ipMRouteScopeNameAddress='" + self.ipmroutescopenameaddress.get() + "']" + "[ipMRouteScopeNameAddressMask='" + self.ipmroutescopenameaddressmask.get() + "']" + "[ipMRouteScopeNameLanguage='" + self.ipmroutescopenamelanguage.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/ipMRouteScopeNameTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmroutescopenameaddress.is_set or self.ipmroutescopenameaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutescopenameaddress.get_name_leafdata())
                if (self.ipmroutescopenameaddressmask.is_set or self.ipmroutescopenameaddressmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutescopenameaddressmask.get_name_leafdata())
                if (self.ipmroutescopenamelanguage.is_set or self.ipmroutescopenamelanguage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutescopenamelanguage.get_name_leafdata())
                if (self.ipmroutescopenamedefault.is_set or self.ipmroutescopenamedefault.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutescopenamedefault.get_name_leafdata())
                if (self.ipmroutescopenamestatus.is_set or self.ipmroutescopenamestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutescopenamestatus.get_name_leafdata())
                if (self.ipmroutescopenamestring.is_set or self.ipmroutescopenamestring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutescopenamestring.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteScopeNameAddress" or name == "ipMRouteScopeNameAddressMask" or name == "ipMRouteScopeNameLanguage" or name == "ipMRouteScopeNameDefault" or name == "ipMRouteScopeNameStatus" or name == "ipMRouteScopeNameString"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteScopeNameAddress"):
                    self.ipmroutescopenameaddress = value
                    self.ipmroutescopenameaddress.value_namespace = name_space
                    self.ipmroutescopenameaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteScopeNameAddressMask"):
                    self.ipmroutescopenameaddressmask = value
                    self.ipmroutescopenameaddressmask.value_namespace = name_space
                    self.ipmroutescopenameaddressmask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteScopeNameLanguage"):
                    self.ipmroutescopenamelanguage = value
                    self.ipmroutescopenamelanguage.value_namespace = name_space
                    self.ipmroutescopenamelanguage.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteScopeNameDefault"):
                    self.ipmroutescopenamedefault = value
                    self.ipmroutescopenamedefault.value_namespace = name_space
                    self.ipmroutescopenamedefault.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteScopeNameStatus"):
                    self.ipmroutescopenamestatus = value
                    self.ipmroutescopenamestatus.value_namespace = name_space
                    self.ipmroutescopenamestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteScopeNameString"):
                    self.ipmroutescopenamestring = value
                    self.ipmroutescopenamestring.value_namespace = name_space
                    self.ipmroutescopenamestring.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipmroutescopenameentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipmroutescopenameentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipMRouteScopeNameTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipMRouteScopeNameEntry"):
                for c in self.ipmroutescopenameentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipmroutescopenameentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipMRouteScopeNameEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ipmroute is not None and self.ipmroute.has_data()) or
            (self.ipmrouteboundarytable is not None and self.ipmrouteboundarytable.has_data()) or
            (self.ipmrouteinterfacetable is not None and self.ipmrouteinterfacetable.has_data()) or
            (self.ipmroutenexthoptable is not None and self.ipmroutenexthoptable.has_data()) or
            (self.ipmroutescopenametable is not None and self.ipmroutescopenametable.has_data()) or
            (self.ipmroutetable is not None and self.ipmroutetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ipmroute is not None and self.ipmroute.has_operation()) or
            (self.ipmrouteboundarytable is not None and self.ipmrouteboundarytable.has_operation()) or
            (self.ipmrouteinterfacetable is not None and self.ipmrouteinterfacetable.has_operation()) or
            (self.ipmroutenexthoptable is not None and self.ipmroutenexthoptable.has_operation()) or
            (self.ipmroutescopenametable is not None and self.ipmroutescopenametable.has_operation()) or
            (self.ipmroutetable is not None and self.ipmroutetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "IPMROUTE-STD-MIB:IPMROUTE-STD-MIB" + path_buffer

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

        if (child_yang_name == "ipMRoute"):
            if (self.ipmroute is None):
                self.ipmroute = IpmrouteStdMib.Ipmroute()
                self.ipmroute.parent = self
                self._children_name_map["ipmroute"] = "ipMRoute"
            return self.ipmroute

        if (child_yang_name == "ipMRouteBoundaryTable"):
            if (self.ipmrouteboundarytable is None):
                self.ipmrouteboundarytable = IpmrouteStdMib.Ipmrouteboundarytable()
                self.ipmrouteboundarytable.parent = self
                self._children_name_map["ipmrouteboundarytable"] = "ipMRouteBoundaryTable"
            return self.ipmrouteboundarytable

        if (child_yang_name == "ipMRouteInterfaceTable"):
            if (self.ipmrouteinterfacetable is None):
                self.ipmrouteinterfacetable = IpmrouteStdMib.Ipmrouteinterfacetable()
                self.ipmrouteinterfacetable.parent = self
                self._children_name_map["ipmrouteinterfacetable"] = "ipMRouteInterfaceTable"
            return self.ipmrouteinterfacetable

        if (child_yang_name == "ipMRouteNextHopTable"):
            if (self.ipmroutenexthoptable is None):
                self.ipmroutenexthoptable = IpmrouteStdMib.Ipmroutenexthoptable()
                self.ipmroutenexthoptable.parent = self
                self._children_name_map["ipmroutenexthoptable"] = "ipMRouteNextHopTable"
            return self.ipmroutenexthoptable

        if (child_yang_name == "ipMRouteScopeNameTable"):
            if (self.ipmroutescopenametable is None):
                self.ipmroutescopenametable = IpmrouteStdMib.Ipmroutescopenametable()
                self.ipmroutescopenametable.parent = self
                self._children_name_map["ipmroutescopenametable"] = "ipMRouteScopeNameTable"
            return self.ipmroutescopenametable

        if (child_yang_name == "ipMRouteTable"):
            if (self.ipmroutetable is None):
                self.ipmroutetable = IpmrouteStdMib.Ipmroutetable()
                self.ipmroutetable.parent = self
                self._children_name_map["ipmroutetable"] = "ipMRouteTable"
            return self.ipmroutetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ipMRoute" or name == "ipMRouteBoundaryTable" or name == "ipMRouteInterfaceTable" or name == "ipMRouteNextHopTable" or name == "ipMRouteScopeNameTable" or name == "ipMRouteTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpmrouteStdMib()
        return self._top_entity

