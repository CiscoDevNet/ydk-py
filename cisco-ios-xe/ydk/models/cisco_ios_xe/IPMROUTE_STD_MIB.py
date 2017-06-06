""" IPMROUTE_STD_MIB 

The MIB module for management of IP Multicast routing, but
independent of the specific multicast routing protocol in
use.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IpmrouteStdMib(object):
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
        self.ipmroute = IpmrouteStdMib.Ipmroute()
        self.ipmroute.parent = self
        self.ipmrouteboundarytable = IpmrouteStdMib.Ipmrouteboundarytable()
        self.ipmrouteboundarytable.parent = self
        self.ipmrouteinterfacetable = IpmrouteStdMib.Ipmrouteinterfacetable()
        self.ipmrouteinterfacetable.parent = self
        self.ipmroutenexthoptable = IpmrouteStdMib.Ipmroutenexthoptable()
        self.ipmroutenexthoptable.parent = self
        self.ipmroutescopenametable = IpmrouteStdMib.Ipmroutescopenametable()
        self.ipmroutescopenametable.parent = self
        self.ipmroutetable = IpmrouteStdMib.Ipmroutetable()
        self.ipmroutetable.parent = self


    class Ipmroute(object):
        """
        
        
        .. attribute:: ipmrouteenable
        
        	The enabled status of IP Multicast routing on this router
        	**type**\:   :py:class:`IpmrouteenableEnum <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroute.IpmrouteenableEnum>`
        
        .. attribute:: ipmrouteentrycount
        
        	The number of rows in the ipMRouteTable.  This can be used to monitor the multicast routing table size
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            self.parent = None
            self.ipmrouteenable = None
            self.ipmrouteentrycount = None

        class IpmrouteenableEnum(Enum):
            """
            IpmrouteenableEnum

            The enabled status of IP Multicast routing on this router.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                return meta._meta_table['IpmrouteStdMib.Ipmroute.IpmrouteenableEnum']


        @property
        def _common_path(self):

            return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRoute'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipmrouteenable is not None:
                return True

            if self.ipmrouteentrycount is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
            return meta._meta_table['IpmrouteStdMib.Ipmroute']['meta_info']


    class Ipmroutetable(object):
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
            self.parent = None
            self.ipmrouteentry = YList()
            self.ipmrouteentry.parent = self
            self.ipmrouteentry.name = 'ipmrouteentry'


        class Ipmrouteentry(object):
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
            	**type**\:   :py:class:`IanaipmrouteprotocolEnum <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IanaipmrouteprotocolEnum>`
            
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
            	**type**\:   :py:class:`IanaiprouteprotocolEnum <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IanaiprouteprotocolEnum>`
            
            .. attribute:: ipmrouterttype
            
            	The reason the given route was placed in the (logical) multicast Routing Information Base (RIB).  A value of unicast means that the route would normally be placed only in the unicast RIB, but was placed in the multicast RIB (instead or in addition) due to local configuration, such as when running PIM over RIP.  A value of multicast means that      the route was explicitly added to the multicast RIB by the routing protocol, such as DVMRP or Multiprotocol BGP
            	**type**\:   :py:class:`IpmrouterttypeEnum <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry.IpmrouterttypeEnum>`
            
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
                self.parent = None
                self.ipmroutegroup = None
                self.ipmroutesource = None
                self.ipmroutesourcemask = None
                self.ciscoipmroutebps = None
                self.ciscoipmroutebps2 = None
                self.ciscoipmrouteconnectedflag = None
                self.ciscoipmroutedifferentinifpkts = None
                self.ciscoipmrouteinlimit = None
                self.ciscoipmrouteinlimit2 = None
                self.ciscoipmroutejoinflag = None
                self.ciscoipmroutelastused = None
                self.ciscoipmroutelocalflag = None
                self.ciscoipmroutemetric = None
                self.ciscoipmroutemetric2 = None
                self.ciscoipmroutemetricpreference = None
                self.ciscoipmroutemsdpflag = None
                self.ciscoipmrouteoctets = None
                self.ciscoipmroutepkts = None
                self.ciscoipmrouteproxyjoinflag = None
                self.ciscoipmroutepruneflag = None
                self.ciscoipmrouteregisterflag = None
                self.ciscoipmrouterpflag = None
                self.ciscoipmroutesparseflag = None
                self.ciscoipmroutesptflag = None
                self.ipmroutedifferentinifpackets = None
                self.ipmrouteexpirytime = None
                self.ipmroutehcoctets = None
                self.ipmrouteinifindex = None
                self.ipmrouteoctets = None
                self.ipmroutepkts = None
                self.ipmrouteprotocol = None
                self.ipmroutertaddress = None
                self.ipmroutertmask = None
                self.ipmroutertproto = None
                self.ipmrouterttype = None
                self.ipmrouteupstreamneighbor = None
                self.ipmrouteuptime = None

            class IpmrouterttypeEnum(Enum):
                """
                IpmrouterttypeEnum

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

                unicast = 1

                multicast = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                    return meta._meta_table['IpmrouteStdMib.Ipmroutetable.Ipmrouteentry.IpmrouterttypeEnum']


            @property
            def _common_path(self):
                if self.ipmroutegroup is None:
                    raise YPYModelError('Key property ipmroutegroup is None')
                if self.ipmroutesource is None:
                    raise YPYModelError('Key property ipmroutesource is None')
                if self.ipmroutesourcemask is None:
                    raise YPYModelError('Key property ipmroutesourcemask is None')

                return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteTable/IPMROUTE-STD-MIB:ipMRouteEntry[IPMROUTE-STD-MIB:ipMRouteGroup = ' + str(self.ipmroutegroup) + '][IPMROUTE-STD-MIB:ipMRouteSource = ' + str(self.ipmroutesource) + '][IPMROUTE-STD-MIB:ipMRouteSourceMask = ' + str(self.ipmroutesourcemask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipmroutegroup is not None:
                    return True

                if self.ipmroutesource is not None:
                    return True

                if self.ipmroutesourcemask is not None:
                    return True

                if self.ciscoipmroutebps is not None:
                    return True

                if self.ciscoipmroutebps2 is not None:
                    return True

                if self.ciscoipmrouteconnectedflag is not None:
                    return True

                if self.ciscoipmroutedifferentinifpkts is not None:
                    return True

                if self.ciscoipmrouteinlimit is not None:
                    return True

                if self.ciscoipmrouteinlimit2 is not None:
                    return True

                if self.ciscoipmroutejoinflag is not None:
                    return True

                if self.ciscoipmroutelastused is not None:
                    return True

                if self.ciscoipmroutelocalflag is not None:
                    return True

                if self.ciscoipmroutemetric is not None:
                    return True

                if self.ciscoipmroutemetric2 is not None:
                    return True

                if self.ciscoipmroutemetricpreference is not None:
                    return True

                if self.ciscoipmroutemsdpflag is not None:
                    return True

                if self.ciscoipmrouteoctets is not None:
                    return True

                if self.ciscoipmroutepkts is not None:
                    return True

                if self.ciscoipmrouteproxyjoinflag is not None:
                    return True

                if self.ciscoipmroutepruneflag is not None:
                    return True

                if self.ciscoipmrouteregisterflag is not None:
                    return True

                if self.ciscoipmrouterpflag is not None:
                    return True

                if self.ciscoipmroutesparseflag is not None:
                    return True

                if self.ciscoipmroutesptflag is not None:
                    return True

                if self.ipmroutedifferentinifpackets is not None:
                    return True

                if self.ipmrouteexpirytime is not None:
                    return True

                if self.ipmroutehcoctets is not None:
                    return True

                if self.ipmrouteinifindex is not None:
                    return True

                if self.ipmrouteoctets is not None:
                    return True

                if self.ipmroutepkts is not None:
                    return True

                if self.ipmrouteprotocol is not None:
                    return True

                if self.ipmroutertaddress is not None:
                    return True

                if self.ipmroutertmask is not None:
                    return True

                if self.ipmroutertproto is not None:
                    return True

                if self.ipmrouterttype is not None:
                    return True

                if self.ipmrouteupstreamneighbor is not None:
                    return True

                if self.ipmrouteuptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                return meta._meta_table['IpmrouteStdMib.Ipmroutetable.Ipmrouteentry']['meta_info']

        @property
        def _common_path(self):

            return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipmrouteentry is not None:
                for child_ref in self.ipmrouteentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
            return meta._meta_table['IpmrouteStdMib.Ipmroutetable']['meta_info']


    class Ipmroutenexthoptable(object):
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
            self.parent = None
            self.ipmroutenexthopentry = YList()
            self.ipmroutenexthopentry.parent = self
            self.ipmroutenexthopentry.name = 'ipmroutenexthopentry'


        class Ipmroutenexthopentry(object):
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
            	**type**\:   :py:class:`IanaipmrouteprotocolEnum <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IanaipmrouteprotocolEnum>`
            
            .. attribute:: ipmroutenexthopstate
            
            	An indication of whether the outgoing interface and next\- hop represented by this entry is currently being used to forward IP datagrams.  The value 'forwarding' indicates it is currently being used; the value 'pruned' indicates it is not
            	**type**\:   :py:class:`IpmroutenexthopstateEnum <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry.IpmroutenexthopstateEnum>`
            
            .. attribute:: ipmroutenexthopuptime
            
            	The time since the multicast routing information represented by this entry was learned by the router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                self.parent = None
                self.ipmroutenexthopgroup = None
                self.ipmroutenexthopsource = None
                self.ipmroutenexthopsourcemask = None
                self.ipmroutenexthopifindex = None
                self.ipmroutenexthopaddress = None
                self.ciscoipmroutenexthopmachdr = None
                self.ciscoipmroutenexthopoutlimit = None
                self.ciscoipmroutenexthoppkts = None
                self.ipmroutenexthopclosestmemberhops = None
                self.ipmroutenexthopexpirytime = None
                self.ipmroutenexthoppkts = None
                self.ipmroutenexthopprotocol = None
                self.ipmroutenexthopstate = None
                self.ipmroutenexthopuptime = None

            class IpmroutenexthopstateEnum(Enum):
                """
                IpmroutenexthopstateEnum

                An indication of whether the outgoing interface and next\-

                hop represented by this entry is currently being used to

                forward IP datagrams.  The value 'forwarding' indicates it

                is currently being used; the value 'pruned' indicates it is

                not.

                .. data:: pruned = 1

                .. data:: forwarding = 2

                """

                pruned = 1

                forwarding = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                    return meta._meta_table['IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry.IpmroutenexthopstateEnum']


            @property
            def _common_path(self):
                if self.ipmroutenexthopgroup is None:
                    raise YPYModelError('Key property ipmroutenexthopgroup is None')
                if self.ipmroutenexthopsource is None:
                    raise YPYModelError('Key property ipmroutenexthopsource is None')
                if self.ipmroutenexthopsourcemask is None:
                    raise YPYModelError('Key property ipmroutenexthopsourcemask is None')
                if self.ipmroutenexthopifindex is None:
                    raise YPYModelError('Key property ipmroutenexthopifindex is None')
                if self.ipmroutenexthopaddress is None:
                    raise YPYModelError('Key property ipmroutenexthopaddress is None')

                return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteNextHopTable/IPMROUTE-STD-MIB:ipMRouteNextHopEntry[IPMROUTE-STD-MIB:ipMRouteNextHopGroup = ' + str(self.ipmroutenexthopgroup) + '][IPMROUTE-STD-MIB:ipMRouteNextHopSource = ' + str(self.ipmroutenexthopsource) + '][IPMROUTE-STD-MIB:ipMRouteNextHopSourceMask = ' + str(self.ipmroutenexthopsourcemask) + '][IPMROUTE-STD-MIB:ipMRouteNextHopIfIndex = ' + str(self.ipmroutenexthopifindex) + '][IPMROUTE-STD-MIB:ipMRouteNextHopAddress = ' + str(self.ipmroutenexthopaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipmroutenexthopgroup is not None:
                    return True

                if self.ipmroutenexthopsource is not None:
                    return True

                if self.ipmroutenexthopsourcemask is not None:
                    return True

                if self.ipmroutenexthopifindex is not None:
                    return True

                if self.ipmroutenexthopaddress is not None:
                    return True

                if self.ciscoipmroutenexthopmachdr is not None:
                    return True

                if self.ciscoipmroutenexthopoutlimit is not None:
                    return True

                if self.ciscoipmroutenexthoppkts is not None:
                    return True

                if self.ipmroutenexthopclosestmemberhops is not None:
                    return True

                if self.ipmroutenexthopexpirytime is not None:
                    return True

                if self.ipmroutenexthoppkts is not None:
                    return True

                if self.ipmroutenexthopprotocol is not None:
                    return True

                if self.ipmroutenexthopstate is not None:
                    return True

                if self.ipmroutenexthopuptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                return meta._meta_table['IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry']['meta_info']

        @property
        def _common_path(self):

            return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteNextHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipmroutenexthopentry is not None:
                for child_ref in self.ipmroutenexthopentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
            return meta._meta_table['IpmrouteStdMib.Ipmroutenexthoptable']['meta_info']


    class Ipmrouteinterfacetable(object):
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
            self.parent = None
            self.ipmrouteinterfaceentry = YList()
            self.ipmrouteinterfaceentry.parent = self
            self.ipmrouteinterfaceentry.name = 'ipmrouteinterfaceentry'


        class Ipmrouteinterfaceentry(object):
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
            	**type**\:   :py:class:`IanaipmrouteprotocolEnum <ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB.IanaipmrouteprotocolEnum>`
            
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
                self.parent = None
                self.ipmrouteinterfaceifindex = None
                self.ciscoipmrouteifhcinmcastpkts = None
                self.ciscoipmrouteifhcoutmcastpkts = None
                self.ciscoipmrouteifinmcastoctets = None
                self.ciscoipmrouteifinmcastpkts = None
                self.ciscoipmrouteifoutmcastoctets = None
                self.ciscoipmrouteifoutmcastpkts = None
                self.ipmrouteinterfacehcinmcastoctets = None
                self.ipmrouteinterfacehcoutmcastoctets = None
                self.ipmrouteinterfaceinmcastoctets = None
                self.ipmrouteinterfaceoutmcastoctets = None
                self.ipmrouteinterfaceprotocol = None
                self.ipmrouteinterfaceratelimit = None
                self.ipmrouteinterfacettl = None

            @property
            def _common_path(self):
                if self.ipmrouteinterfaceifindex is None:
                    raise YPYModelError('Key property ipmrouteinterfaceifindex is None')

                return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteInterfaceTable/IPMROUTE-STD-MIB:ipMRouteInterfaceEntry[IPMROUTE-STD-MIB:ipMRouteInterfaceIfIndex = ' + str(self.ipmrouteinterfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipmrouteinterfaceifindex is not None:
                    return True

                if self.ciscoipmrouteifhcinmcastpkts is not None:
                    return True

                if self.ciscoipmrouteifhcoutmcastpkts is not None:
                    return True

                if self.ciscoipmrouteifinmcastoctets is not None:
                    return True

                if self.ciscoipmrouteifinmcastpkts is not None:
                    return True

                if self.ciscoipmrouteifoutmcastoctets is not None:
                    return True

                if self.ciscoipmrouteifoutmcastpkts is not None:
                    return True

                if self.ipmrouteinterfacehcinmcastoctets is not None:
                    return True

                if self.ipmrouteinterfacehcoutmcastoctets is not None:
                    return True

                if self.ipmrouteinterfaceinmcastoctets is not None:
                    return True

                if self.ipmrouteinterfaceoutmcastoctets is not None:
                    return True

                if self.ipmrouteinterfaceprotocol is not None:
                    return True

                if self.ipmrouteinterfaceratelimit is not None:
                    return True

                if self.ipmrouteinterfacettl is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                return meta._meta_table['IpmrouteStdMib.Ipmrouteinterfacetable.Ipmrouteinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipmrouteinterfaceentry is not None:
                for child_ref in self.ipmrouteinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
            return meta._meta_table['IpmrouteStdMib.Ipmrouteinterfacetable']['meta_info']


    class Ipmrouteboundarytable(object):
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
            self.parent = None
            self.ipmrouteboundaryentry = YList()
            self.ipmrouteboundaryentry.parent = self
            self.ipmrouteboundaryentry.name = 'ipmrouteboundaryentry'


        class Ipmrouteboundaryentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                self.parent = None
                self.ipmrouteboundaryifindex = None
                self.ipmrouteboundaryaddress = None
                self.ipmrouteboundaryaddressmask = None
                self.ipmrouteboundarystatus = None

            @property
            def _common_path(self):
                if self.ipmrouteboundaryifindex is None:
                    raise YPYModelError('Key property ipmrouteboundaryifindex is None')
                if self.ipmrouteboundaryaddress is None:
                    raise YPYModelError('Key property ipmrouteboundaryaddress is None')
                if self.ipmrouteboundaryaddressmask is None:
                    raise YPYModelError('Key property ipmrouteboundaryaddressmask is None')

                return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteBoundaryTable/IPMROUTE-STD-MIB:ipMRouteBoundaryEntry[IPMROUTE-STD-MIB:ipMRouteBoundaryIfIndex = ' + str(self.ipmrouteboundaryifindex) + '][IPMROUTE-STD-MIB:ipMRouteBoundaryAddress = ' + str(self.ipmrouteboundaryaddress) + '][IPMROUTE-STD-MIB:ipMRouteBoundaryAddressMask = ' + str(self.ipmrouteboundaryaddressmask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipmrouteboundaryifindex is not None:
                    return True

                if self.ipmrouteboundaryaddress is not None:
                    return True

                if self.ipmrouteboundaryaddressmask is not None:
                    return True

                if self.ipmrouteboundarystatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                return meta._meta_table['IpmrouteStdMib.Ipmrouteboundarytable.Ipmrouteboundaryentry']['meta_info']

        @property
        def _common_path(self):

            return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteBoundaryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipmrouteboundaryentry is not None:
                for child_ref in self.ipmrouteboundaryentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
            return meta._meta_table['IpmrouteStdMib.Ipmrouteboundarytable']['meta_info']


    class Ipmroutescopenametable(object):
        """
        The (conceptual) table listing the multicast scope names.
        
        .. attribute:: ipmroutescopenameentry
        
        	An entry (conceptual row) in the ipMRouteScopeNameTable representing a multicast scope name
        	**type**\: list of    :py:class:`Ipmroutescopenameentry <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry>`
        
        

        """

        _prefix = 'IPMROUTE-STD-MIB'
        _revision = '2000-09-22'

        def __init__(self):
            self.parent = None
            self.ipmroutescopenameentry = YList()
            self.ipmroutescopenameentry.parent = self
            self.ipmroutescopenameentry.name = 'ipmroutescopenameentry'


        class Ipmroutescopenameentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ipmroutescopenamestring
            
            	The textual name associated with the multicast scope.  The value of this object should be suitable for displaying to end\-users, such as when allocating a multicast address in this scope.  When no name is specified, the default value of this object should be the string 239.x.x.x/y with x and y replaced appropriately to describe the address and mask length associated with the scope
            	**type**\:  str
            
            

            """

            _prefix = 'IPMROUTE-STD-MIB'
            _revision = '2000-09-22'

            def __init__(self):
                self.parent = None
                self.ipmroutescopenameaddress = None
                self.ipmroutescopenameaddressmask = None
                self.ipmroutescopenamelanguage = None
                self.ipmroutescopenamedefault = None
                self.ipmroutescopenamestatus = None
                self.ipmroutescopenamestring = None

            @property
            def _common_path(self):
                if self.ipmroutescopenameaddress is None:
                    raise YPYModelError('Key property ipmroutescopenameaddress is None')
                if self.ipmroutescopenameaddressmask is None:
                    raise YPYModelError('Key property ipmroutescopenameaddressmask is None')
                if self.ipmroutescopenamelanguage is None:
                    raise YPYModelError('Key property ipmroutescopenamelanguage is None')

                return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteScopeNameTable/IPMROUTE-STD-MIB:ipMRouteScopeNameEntry[IPMROUTE-STD-MIB:ipMRouteScopeNameAddress = ' + str(self.ipmroutescopenameaddress) + '][IPMROUTE-STD-MIB:ipMRouteScopeNameAddressMask = ' + str(self.ipmroutescopenameaddressmask) + '][IPMROUTE-STD-MIB:ipMRouteScopeNameLanguage = ' + str(self.ipmroutescopenamelanguage) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipmroutescopenameaddress is not None:
                    return True

                if self.ipmroutescopenameaddressmask is not None:
                    return True

                if self.ipmroutescopenamelanguage is not None:
                    return True

                if self.ipmroutescopenamedefault is not None:
                    return True

                if self.ipmroutescopenamestatus is not None:
                    return True

                if self.ipmroutescopenamestring is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
                return meta._meta_table['IpmrouteStdMib.Ipmroutescopenametable.Ipmroutescopenameentry']['meta_info']

        @property
        def _common_path(self):

            return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB/IPMROUTE-STD-MIB:ipMRouteScopeNameTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipmroutescopenameentry is not None:
                for child_ref in self.ipmroutescopenameentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
            return meta._meta_table['IpmrouteStdMib.Ipmroutescopenametable']['meta_info']

    @property
    def _common_path(self):

        return '/IPMROUTE-STD-MIB:IPMROUTE-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ipmroute is not None and self.ipmroute._has_data():
            return True

        if self.ipmrouteboundarytable is not None and self.ipmrouteboundarytable._has_data():
            return True

        if self.ipmrouteinterfacetable is not None and self.ipmrouteinterfacetable._has_data():
            return True

        if self.ipmroutenexthoptable is not None and self.ipmroutenexthoptable._has_data():
            return True

        if self.ipmroutescopenametable is not None and self.ipmroutescopenametable._has_data():
            return True

        if self.ipmroutetable is not None and self.ipmroutetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IPMROUTE_STD_MIB as meta
        return meta._meta_table['IpmrouteStdMib']['meta_info']


