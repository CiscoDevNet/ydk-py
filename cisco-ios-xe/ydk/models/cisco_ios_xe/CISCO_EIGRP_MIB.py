""" CISCO_EIGRP_MIB 

Enhanced Interior Gateway Protocol (EIGRP) is a Cisco
proprietary distance vector routing protocol.   It is based on
the Diffusing Update Algorithm (DUAL), which is a method of
finding loop\-free paths through a network.   Directly
connected routers running EIGRP form neighbor adjacencies in
order to propagate best\-path and alternate\-path routing
information for configured and learned routes.

The tables defined within the MIB are closely aligned with how
the router command\-line interface for EIGRP displays
information on EIGRP configurations, i.e., the topology table
contains objects associated with the EIGRP topology commands,
and the peer table contains objects associated withe EIGRP
neighbor commands, etc.

There are five main tables within this mib\:

   EIGRP VPN table
      Contains information regarding which virtual private
      networks (VPN) are configured with EIGRP.

   EIGRP traffic statistics table
      Contains counter & statistcs regarding specific types of
      EIGRP packets sent and related collective information
      per VPN and per autonomous system (AS).

   EIGRP topology table
      Contains information regarding EIGRP routes received in
      updates and originated locally.   EIGRP sends and
      receives routing updates from adjacent routers running
      EIGRP with which it formed a peer relationship.

   EIGRP peer (neighbor) table
      Contains information about neighbor EIGRP routers with
      which peer adjacencies have been established.   EIGRP
      uses a Hello protocol to form neighbor relationships
      with directly connected routers also running EIGRP.

   EIGRP interfaces table
      Contains information and statistics on each of the
      interfaces on the router over which EIGRP has been
      configured to run.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoEigrpMib(object):
    """
    
    
    .. attribute:: ceigrpinterfacetable
    
    	The table of interfaces over which EIGRP is running, and their associated statistics.   This table is independent of whether any peer adjacencies have been formed over the interfaces or not.   Interfaces running EIGRP are determined by whether their assigned IP addresses fall within configured EIGRP network statements
    	**type**\:   :py:class:`Ceigrpinterfacetable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpinterfacetable>`
    
    .. attribute:: ceigrppeertable
    
    	The table of established EIGRP peers (neighbors) in the selected autonomous system.   Peers are indexed by their unique internal handle id, as well as the AS number and VPN id.   The peer entry is removed from the table if the peer is declared down
    	**type**\:   :py:class:`Ceigrppeertable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrppeertable>`
    
    .. attribute:: ceigrptopotable
    
    	The table of EIGRP routes and their associated attributes for an Autonomous System (AS) configured in a VPN is called a topology table.  All route entries in the topology table will be indexed by IP network type, IP network number and network mask (prefix) size
    	**type**\:   :py:class:`Ceigrptopotable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptopotable>`
    
    .. attribute:: ceigrptraffstatstable
    
    	Table of EIGRP traffic statistics and information associated with all EIGRP autonomous systems
    	**type**\:   :py:class:`Ceigrptraffstatstable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable>`
    
    .. attribute:: ceigrpvpntable
    
    	This table contains information on those VPN's configured to run EIGRP.  The VPN creation on a router is independent of the routing protocol to be used over it.   A VPN is given a name and has a dedicated routing table associated with it.  This routing table is identified internally by a unique integer value
    	**type**\:   :py:class:`Ceigrpvpntable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable>`
    
    

    """

    _prefix = 'CISCO-EIGRP-MIB'
    _revision = '2004-11-16'

    def __init__(self):
        self.ceigrpinterfacetable = CiscoEigrpMib.Ceigrpinterfacetable()
        self.ceigrpinterfacetable.parent = self
        self.ceigrppeertable = CiscoEigrpMib.Ceigrppeertable()
        self.ceigrppeertable.parent = self
        self.ceigrptopotable = CiscoEigrpMib.Ceigrptopotable()
        self.ceigrptopotable.parent = self
        self.ceigrptraffstatstable = CiscoEigrpMib.Ceigrptraffstatstable()
        self.ceigrptraffstatstable.parent = self
        self.ceigrpvpntable = CiscoEigrpMib.Ceigrpvpntable()
        self.ceigrpvpntable.parent = self


    class Ceigrpvpntable(object):
        """
        This table contains information on those VPN's configured
        to run EIGRP.  The VPN creation on a router is independent
        of the routing protocol to be used over it.   A VPN is
        given a name and has a dedicated routing table associated
        with it.  This routing table is identified internally
        by a unique integer value.
        
        .. attribute:: ceigrpvpnentry
        
        	Information relating to a single VPN which is configured to run EIGRP
        	**type**\: list of    :py:class:`Ceigrpvpnentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            self.parent = None
            self.ceigrpvpnentry = YList()
            self.ceigrpvpnentry.parent = self
            self.ceigrpvpnentry.name = 'ceigrpvpnentry'


        class Ceigrpvpnentry(object):
            """
            Information relating to a single VPN which is configured
            to run EIGRP.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	The unique VPN identifier.  This is a unique integer relative to all other VPN's defined on the router.  It also identifies internally the routing table instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpvpnname
            
            	The name given to the VPN
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                self.parent = None
                self.ceigrpvpnid = None
                self.ceigrpvpnname = None

            @property
            def _common_path(self):
                if self.ceigrpvpnid is None:
                    raise YPYModelError('Key property ceigrpvpnid is None')

                return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpVpnTable/CISCO-EIGRP-MIB:cEigrpVpnEntry[CISCO-EIGRP-MIB:cEigrpVpnId = ' + str(self.ceigrpvpnid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ceigrpvpnid is not None:
                    return True

                if self.ceigrpvpnname is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
                return meta._meta_table['CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpVpnTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceigrpvpnentry is not None:
                for child_ref in self.ceigrpvpnentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
            return meta._meta_table['CiscoEigrpMib.Ceigrpvpntable']['meta_info']


    class Ceigrptraffstatstable(object):
        """
        Table of EIGRP traffic statistics and information
        associated with all EIGRP autonomous systems.
        
        .. attribute:: ceigrptraffstatsentry
        
        	The set of statistics and information for a single EIGRP Autonomous System
        	**type**\: list of    :py:class:`Ceigrptraffstatsentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            self.parent = None
            self.ceigrptraffstatsentry = YList()
            self.ceigrptraffstatsentry.parent = self
            self.ceigrptraffstatsentry.name = 'ceigrptraffstatsentry'


        class Ceigrptraffstatsentry(object):
            """
            The set of statistics and information for a single EIGRP
            Autonomous System.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	The Autonomous System number which is unique integer per VPN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpacksrcvd
            
            	The total number packet acknowledgements that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpackssent
            
            	The total number packet acknowledgements that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpasrouterid
            
            	The router\-id configured or automatically selected for the EIGRP AS.   Each EIGRP routing process has a unique router\-id selected from each autonomous system configured. The format is governed by object cEigrpAsRouterIdType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrpasrouteridtype
            
            	The format of the router\-id configured or automatically selected for the EIGRP AS
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ceigrpheadserial
            
            	Routes in a topology table for an AS are assigned serial numbers and are sequenced internally as they are inserted and deleted.   The serial number of the first route in that internal sequence is called the head serial number. Each AS has its own topology table, and its own serial number space, each of which begins with the value 1. A serial number of zero implies that there are no routes in the topology
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceigrphellosrcvd
            
            	The total number Hello packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrphellossent
            
            	The total number Hello packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpinputqdrops
            
            	The number of EIGRP packets dropped from the input queue due to it being full within the AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpinputqhighmark
            
            	The highest number of EIGRP packets in the input queue waiting to be processed internally addressed to this AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpnbrcount
            
            	The total number of live EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured in the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpnextserial
            
            	The serial number that would be assigned to the next new or changed route in the topology table for the AS
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceigrpqueriesrcvd
            
            	The total number alternate route query packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpqueriessent
            
            	The total number alternate route query packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprepliesrcvd
            
            	The total number query reply packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprepliessent
            
            	The total number query reply packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpsiaqueriesrcvd
            
            	The total number of Stuck\-In\-Active (SIA) query packets received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpsiaqueriessent
            
            	The total number of Stuck\-In\-Active (SIA) query packets sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrptoporoutes
            
            	The total number of EIGRP derived routes currently existing in the topology table for the AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpupdatesrcvd
            
            	The total number routing update packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpupdatessent
            
            	The total number routing update packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitdummies
            
            	A dummy is a temporary internal entity used as a place holder in the topology table for an AS. They are not transmitted in routing updates.  This is the total number currently in existence associated with the AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitpendreplies
            
            	When alternate route query packets are sent to adjacent EIGRP peers in an AS, replies are expected.   This object is the total number of outstanding replies expected to queries that have been sent to peers in the current AS. It remains at zero most of the time until an EIGRP route becomes active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                self.parent = None
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ceigrpacksrcvd = None
                self.ceigrpackssent = None
                self.ceigrpasrouterid = None
                self.ceigrpasrouteridtype = None
                self.ceigrpheadserial = None
                self.ceigrphellosrcvd = None
                self.ceigrphellossent = None
                self.ceigrpinputqdrops = None
                self.ceigrpinputqhighmark = None
                self.ceigrpnbrcount = None
                self.ceigrpnextserial = None
                self.ceigrpqueriesrcvd = None
                self.ceigrpqueriessent = None
                self.ceigrprepliesrcvd = None
                self.ceigrprepliessent = None
                self.ceigrpsiaqueriesrcvd = None
                self.ceigrpsiaqueriessent = None
                self.ceigrptoporoutes = None
                self.ceigrpupdatesrcvd = None
                self.ceigrpupdatessent = None
                self.ceigrpxmitdummies = None
                self.ceigrpxmitpendreplies = None

            @property
            def _common_path(self):
                if self.ceigrpvpnid is None:
                    raise YPYModelError('Key property ceigrpvpnid is None')
                if self.ceigrpasnumber is None:
                    raise YPYModelError('Key property ceigrpasnumber is None')

                return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpTraffStatsTable/CISCO-EIGRP-MIB:cEigrpTraffStatsEntry[CISCO-EIGRP-MIB:cEigrpVpnId = ' + str(self.ceigrpvpnid) + '][CISCO-EIGRP-MIB:cEigrpAsNumber = ' + str(self.ceigrpasnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ceigrpvpnid is not None:
                    return True

                if self.ceigrpasnumber is not None:
                    return True

                if self.ceigrpacksrcvd is not None:
                    return True

                if self.ceigrpackssent is not None:
                    return True

                if self.ceigrpasrouterid is not None:
                    return True

                if self.ceigrpasrouteridtype is not None:
                    return True

                if self.ceigrpheadserial is not None:
                    return True

                if self.ceigrphellosrcvd is not None:
                    return True

                if self.ceigrphellossent is not None:
                    return True

                if self.ceigrpinputqdrops is not None:
                    return True

                if self.ceigrpinputqhighmark is not None:
                    return True

                if self.ceigrpnbrcount is not None:
                    return True

                if self.ceigrpnextserial is not None:
                    return True

                if self.ceigrpqueriesrcvd is not None:
                    return True

                if self.ceigrpqueriessent is not None:
                    return True

                if self.ceigrprepliesrcvd is not None:
                    return True

                if self.ceigrprepliessent is not None:
                    return True

                if self.ceigrpsiaqueriesrcvd is not None:
                    return True

                if self.ceigrpsiaqueriessent is not None:
                    return True

                if self.ceigrptoporoutes is not None:
                    return True

                if self.ceigrpupdatesrcvd is not None:
                    return True

                if self.ceigrpupdatessent is not None:
                    return True

                if self.ceigrpxmitdummies is not None:
                    return True

                if self.ceigrpxmitpendreplies is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
                return meta._meta_table['CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpTraffStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceigrptraffstatsentry is not None:
                for child_ref in self.ceigrptraffstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
            return meta._meta_table['CiscoEigrpMib.Ceigrptraffstatstable']['meta_info']


    class Ceigrptopotable(object):
        """
        The table of EIGRP routes and their associated
        attributes for an Autonomous System (AS) configured
        in a VPN is called a topology table.  All route entries in
        the topology table will be indexed by IP network type,
        IP network number and network mask (prefix) size.
        
        .. attribute:: ceigrptopoentry
        
        	The entry for a single EIGRP topology table in the given AS
        	**type**\: list of    :py:class:`Ceigrptopoentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            self.parent = None
            self.ceigrptopoentry = YList()
            self.ceigrptopoentry.parent = self
            self.ceigrptopoentry.name = 'ceigrptopoentry'


        class Ceigrptopoentry(object):
            """
            The entry for a single EIGRP topology table in the given
            AS.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
            
            .. attribute:: ceigrpdestnettype  <key>
            
            	The format of the destination IP network number for a single route in the topology table in the AS specified in cEigrpDestNet
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ceigrpdestnet  <key>
            
            	The destination IP network number for a single route in the topology table in the AS.  The format is governed by object cEigrpDestNetType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrpdestnetprefixlen  <key>
            
            	The prefix length associated with the destination IP network address for a single route in the topology table in the AS.  The format is governed by the object cEigrpDestNetType
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: ceigrpactive
            
            	A value of true(1) indicates the route to the destination network has failed and an active (query) search for an alternative path is in progress.  A value of false(2) indicates the route is stable (passive)
            	**type**\:  bool
            
            .. attribute:: ceigrpdestsuccessors
            
            	A successor is the next routing hop for a path to the destination IP network number for a single route in the topology table in the AS.  There can be several potential successors if there are multiple paths to the destination.   This is the total number of successors for a topology entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpdistance
            
            	The computed distance to the destination network entry from this router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpfdistance
            
            	The feasibility (best) distance is the minimum distance from this router to the destination IP network in this topology entry.  The feasibility distance is used in determining the best successor for a path to the destination network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpnexthopaddress
            
            	This is the next hop IP address for the route represented by the topology entry.   The next hop is where network traffic will be routed to in order to reach the destination network for this topology entry.  The format is governed by cEigrpNextHopAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrpnexthopaddresstype
            
            	The format of the next hop IP address for the route represented by the topology entry
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ceigrpnexthopinterface
            
            	The interface through which the next hop IP address is reached to send network traffic to the destination network represented by the topology entry
            	**type**\:  str
            
            .. attribute:: ceigrpreportdistance
            
            	The computed distance to the destination network in the topology entry reported to this router by the originator of this route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprouteoriginaddr
            
            	If the origin of the topology route entry is external to this router, then this object is the IP address of the router from which it originated.  The format  is governed by object cEigrpRouteOriginAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrprouteoriginaddrtype
            
            	The format of the IP address defined as the origin of this topology route entry
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ceigrprouteorigintype
            
            	This is a text string describing the internal origin of the EIGRP route represented by the topology entry
            	**type**\:  str
            
            .. attribute:: ceigrpstuckinactive
            
            	A value of true(1) indicates that that this route which is in active state (cEigrpActive = true(1)) has not received any replies to queries for alternate paths, and a second EIGRP route query, called a stuck\-in\-active query, has now been sent
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                self.parent = None
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ceigrpdestnettype = None
                self.ceigrpdestnet = None
                self.ceigrpdestnetprefixlen = None
                self.ceigrpactive = None
                self.ceigrpdestsuccessors = None
                self.ceigrpdistance = None
                self.ceigrpfdistance = None
                self.ceigrpnexthopaddress = None
                self.ceigrpnexthopaddresstype = None
                self.ceigrpnexthopinterface = None
                self.ceigrpreportdistance = None
                self.ceigrprouteoriginaddr = None
                self.ceigrprouteoriginaddrtype = None
                self.ceigrprouteorigintype = None
                self.ceigrpstuckinactive = None

            @property
            def _common_path(self):
                if self.ceigrpvpnid is None:
                    raise YPYModelError('Key property ceigrpvpnid is None')
                if self.ceigrpasnumber is None:
                    raise YPYModelError('Key property ceigrpasnumber is None')
                if self.ceigrpdestnettype is None:
                    raise YPYModelError('Key property ceigrpdestnettype is None')
                if self.ceigrpdestnet is None:
                    raise YPYModelError('Key property ceigrpdestnet is None')
                if self.ceigrpdestnetprefixlen is None:
                    raise YPYModelError('Key property ceigrpdestnetprefixlen is None')

                return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpTopoTable/CISCO-EIGRP-MIB:cEigrpTopoEntry[CISCO-EIGRP-MIB:cEigrpVpnId = ' + str(self.ceigrpvpnid) + '][CISCO-EIGRP-MIB:cEigrpAsNumber = ' + str(self.ceigrpasnumber) + '][CISCO-EIGRP-MIB:cEigrpDestNetType = ' + str(self.ceigrpdestnettype) + '][CISCO-EIGRP-MIB:cEigrpDestNet = ' + str(self.ceigrpdestnet) + '][CISCO-EIGRP-MIB:cEigrpDestNetPrefixLen = ' + str(self.ceigrpdestnetprefixlen) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ceigrpvpnid is not None:
                    return True

                if self.ceigrpasnumber is not None:
                    return True

                if self.ceigrpdestnettype is not None:
                    return True

                if self.ceigrpdestnet is not None:
                    return True

                if self.ceigrpdestnetprefixlen is not None:
                    return True

                if self.ceigrpactive is not None:
                    return True

                if self.ceigrpdestsuccessors is not None:
                    return True

                if self.ceigrpdistance is not None:
                    return True

                if self.ceigrpfdistance is not None:
                    return True

                if self.ceigrpnexthopaddress is not None:
                    return True

                if self.ceigrpnexthopaddresstype is not None:
                    return True

                if self.ceigrpnexthopinterface is not None:
                    return True

                if self.ceigrpreportdistance is not None:
                    return True

                if self.ceigrprouteoriginaddr is not None:
                    return True

                if self.ceigrprouteoriginaddrtype is not None:
                    return True

                if self.ceigrprouteorigintype is not None:
                    return True

                if self.ceigrpstuckinactive is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
                return meta._meta_table['CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpTopoTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceigrptopoentry is not None:
                for child_ref in self.ceigrptopoentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
            return meta._meta_table['CiscoEigrpMib.Ceigrptopotable']['meta_info']


    class Ceigrppeertable(object):
        """
        The table of established EIGRP peers (neighbors) in the
        selected autonomous system.   Peers are indexed by their
        unique internal handle id, as well as the AS number and
        VPN id.   The peer entry is removed from the table if
        the peer is declared down.
        
        .. attribute:: ceigrppeerentry
        
        	Statistics and operational parameters for a single peer in the AS
        	**type**\: list of    :py:class:`Ceigrppeerentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            self.parent = None
            self.ceigrppeerentry = YList()
            self.ceigrppeerentry.parent = self
            self.ceigrppeerentry.name = 'ceigrppeerentry'


        class Ceigrppeerentry(object):
            """
            Statistics and operational parameters for a single peer
            in the AS.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
            
            .. attribute:: ceigrphandle  <key>
            
            	The unique internal identifier for the peer in the AS. This is a unique value among peer entries in a selected table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpholdtime
            
            	The count\-down timer indicating how much time must pass without receiving a hello packet from this EIGRP peer before this router declares the peer down. A peer declared as down is removed from the table and is no longer visible
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ceigrplastseq
            
            	All transmitted EIGRP packets have a sequence number assigned. This is the sequence number of the last EIGRP packet sent to this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrppeeraddr
            
            	The source IP address used by the peer to establish the EIGRP adjacency with this router.  The format is governed by object cEigrpPeerAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrppeeraddrtype
            
            	The format of the remote source IP address used by the peer to establish the EIGRP adjacency with this router
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: ceigrppeerifindex
            
            	The ifIndex of the interface on this router through which this peer can be reached
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ceigrppktsenqueued
            
            	The number of any EIGRP packets currently enqueued waiting to be sent to this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpretrans
            
            	The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpretries
            
            	The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprto
            
            	The computed retransmission timeout for the peer. This value is computed over time as packets are sent to the peer and acknowledgements are received from it, and is the amount of time to wait before resending a packet from the retransmission queue to the peer when an expected acknowledgement has not been received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpsrtt
            
            	The computed smooth round trip time for packets to and from the peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpuptime
            
            	The elapsed time since the EIGRP adjacency was first established with the peer
            	**type**\:  str
            
            .. attribute:: ceigrpversion
            
            	The EIGRP version information reported by the remote peer
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                self.parent = None
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ceigrphandle = None
                self.ceigrpholdtime = None
                self.ceigrplastseq = None
                self.ceigrppeeraddr = None
                self.ceigrppeeraddrtype = None
                self.ceigrppeerifindex = None
                self.ceigrppktsenqueued = None
                self.ceigrpretrans = None
                self.ceigrpretries = None
                self.ceigrprto = None
                self.ceigrpsrtt = None
                self.ceigrpuptime = None
                self.ceigrpversion = None

            @property
            def _common_path(self):
                if self.ceigrpvpnid is None:
                    raise YPYModelError('Key property ceigrpvpnid is None')
                if self.ceigrpasnumber is None:
                    raise YPYModelError('Key property ceigrpasnumber is None')
                if self.ceigrphandle is None:
                    raise YPYModelError('Key property ceigrphandle is None')

                return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpPeerTable/CISCO-EIGRP-MIB:cEigrpPeerEntry[CISCO-EIGRP-MIB:cEigrpVpnId = ' + str(self.ceigrpvpnid) + '][CISCO-EIGRP-MIB:cEigrpAsNumber = ' + str(self.ceigrpasnumber) + '][CISCO-EIGRP-MIB:cEigrpHandle = ' + str(self.ceigrphandle) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ceigrpvpnid is not None:
                    return True

                if self.ceigrpasnumber is not None:
                    return True

                if self.ceigrphandle is not None:
                    return True

                if self.ceigrpholdtime is not None:
                    return True

                if self.ceigrplastseq is not None:
                    return True

                if self.ceigrppeeraddr is not None:
                    return True

                if self.ceigrppeeraddrtype is not None:
                    return True

                if self.ceigrppeerifindex is not None:
                    return True

                if self.ceigrppktsenqueued is not None:
                    return True

                if self.ceigrpretrans is not None:
                    return True

                if self.ceigrpretries is not None:
                    return True

                if self.ceigrprto is not None:
                    return True

                if self.ceigrpsrtt is not None:
                    return True

                if self.ceigrpuptime is not None:
                    return True

                if self.ceigrpversion is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
                return meta._meta_table['CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceigrppeerentry is not None:
                for child_ref in self.ceigrppeerentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
            return meta._meta_table['CiscoEigrpMib.Ceigrppeertable']['meta_info']


    class Ceigrpinterfacetable(object):
        """
        The table of interfaces over which EIGRP is running, and
        their associated statistics.   This table is independent
        of whether any peer adjacencies have been formed over
        the interfaces or not.   Interfaces running EIGRP are
        determined by whether their assigned IP addresses fall
        within configured EIGRP network statements.
        
        .. attribute:: ceigrpinterfaceentry
        
        	Information for a single interface running EIGRP in the AS and VPN
        	**type**\: list of    :py:class:`Ceigrpinterfaceentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            self.parent = None
            self.ceigrpinterfaceentry = YList()
            self.ceigrpinterfaceentry.parent = self
            self.ceigrpinterfaceentry.name = 'ceigrpinterfaceentry'


        class Ceigrpinterfaceentry(object):
            """
            Information for a single interface running EIGRP in the
            AS and VPN.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: ceigrpackssuppressed
            
            	The total number of individual EIGRP acknowledgement packets that have been suppressed and combined in an already enqueued outbound reliable packet on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpauthkeychain
            
            	The name of the authentication key\-chain configured on this interface.   The key\-chain is a reference to which set of secret keys are to be accessed in order to determine which secret key string to use.  The key chain name is not the secret key string password and can also be used in other routing protocols, such as RIP and ISIS
            	**type**\:  str
            
            .. attribute:: ceigrpauthmode
            
            	The EIGRP authentication mode of the interface. none  \:  no authentication enabled on the interface md5   \:  MD5 authentication enabled on the interface
            	**type**\:   :py:class:`CeigrpauthmodeEnum <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry.CeigrpauthmodeEnum>`
            
            .. attribute:: ceigrpcrpkts
            
            	The total number EIGRP Conditional\-Receive packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrphellointerval
            
            	The configured time interval between Hello packet transmissions for this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ceigrpmcastexcepts
            
            	The total number of EIGRP multicast exception transmissions that have occurred on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpmeansrtt
            
            	The average of all the computed smooth round trip time values for a packet to and from all peers established on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpmflowtimer
            
            	The configured multicast flow control timer value for this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpoosrvcd
            
            	The total number of out\-of\-sequence EIGRP packets received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrppacingreliable
            
            	The configured time interval between EIGRP packet transmissions on the interface when the reliable transport method is used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppacingunreliable
            
            	The configured time interval between EIGRP packet transmissions on the interface when the unreliable transport method is used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppeercount
            
            	The number of EIGRP adjacencies currently formed with peers reached through this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrppendingroutes
            
            	The number of queued EIGRP routing updates awaiting transmission on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpretranssent
            
            	The total number EIGRP packet retransmissions sent on the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprmcasts
            
            	The total number of reliable (acknowledgement required) EIGRP multicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprucasts
            
            	The total number of reliable (acknowledgement required) unicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpumcasts
            
            	The total number of unreliable (no acknowledgement required) EIGRP multicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpuucasts
            
            	The total number of unreliable (no acknowledgement required) EIGRP unicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitnextserial
            
            	The serial number of the next EIGRP packet that is to be queued for transmission on this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceigrpxmitreliableq
            
            	The number of EIGRP packets currently waiting in the reliable transport (acknowledgement\-required)  transmission queue to be sent to a peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitunreliableq
            
            	The number EIGRP of packets currently waiting in the unreliable transport (no acknowledgement required) transmission queue
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                self.parent = None
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ifindex = None
                self.ceigrpackssuppressed = None
                self.ceigrpauthkeychain = None
                self.ceigrpauthmode = None
                self.ceigrpcrpkts = None
                self.ceigrphellointerval = None
                self.ceigrpmcastexcepts = None
                self.ceigrpmeansrtt = None
                self.ceigrpmflowtimer = None
                self.ceigrpoosrvcd = None
                self.ceigrppacingreliable = None
                self.ceigrppacingunreliable = None
                self.ceigrppeercount = None
                self.ceigrppendingroutes = None
                self.ceigrpretranssent = None
                self.ceigrprmcasts = None
                self.ceigrprucasts = None
                self.ceigrpumcasts = None
                self.ceigrpuucasts = None
                self.ceigrpxmitnextserial = None
                self.ceigrpxmitreliableq = None
                self.ceigrpxmitunreliableq = None

            class CeigrpauthmodeEnum(Enum):
                """
                CeigrpauthmodeEnum

                The EIGRP authentication mode of the interface.

                none  \:  no authentication enabled on the interface

                md5   \:  MD5 authentication enabled on the interface

                .. data:: none = 1

                .. data:: md5 = 2

                """

                none = 1

                md5 = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
                    return meta._meta_table['CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry.CeigrpauthmodeEnum']


            @property
            def _common_path(self):
                if self.ceigrpvpnid is None:
                    raise YPYModelError('Key property ceigrpvpnid is None')
                if self.ceigrpasnumber is None:
                    raise YPYModelError('Key property ceigrpasnumber is None')
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpInterfaceTable/CISCO-EIGRP-MIB:cEigrpInterfaceEntry[CISCO-EIGRP-MIB:cEigrpVpnId = ' + str(self.ceigrpvpnid) + '][CISCO-EIGRP-MIB:cEigrpAsNumber = ' + str(self.ceigrpasnumber) + '][CISCO-EIGRP-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ceigrpvpnid is not None:
                    return True

                if self.ceigrpasnumber is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.ceigrpackssuppressed is not None:
                    return True

                if self.ceigrpauthkeychain is not None:
                    return True

                if self.ceigrpauthmode is not None:
                    return True

                if self.ceigrpcrpkts is not None:
                    return True

                if self.ceigrphellointerval is not None:
                    return True

                if self.ceigrpmcastexcepts is not None:
                    return True

                if self.ceigrpmeansrtt is not None:
                    return True

                if self.ceigrpmflowtimer is not None:
                    return True

                if self.ceigrpoosrvcd is not None:
                    return True

                if self.ceigrppacingreliable is not None:
                    return True

                if self.ceigrppacingunreliable is not None:
                    return True

                if self.ceigrppeercount is not None:
                    return True

                if self.ceigrppendingroutes is not None:
                    return True

                if self.ceigrpretranssent is not None:
                    return True

                if self.ceigrprmcasts is not None:
                    return True

                if self.ceigrprucasts is not None:
                    return True

                if self.ceigrpumcasts is not None:
                    return True

                if self.ceigrpuucasts is not None:
                    return True

                if self.ceigrpxmitnextserial is not None:
                    return True

                if self.ceigrpxmitreliableq is not None:
                    return True

                if self.ceigrpxmitunreliableq is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
                return meta._meta_table['CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/CISCO-EIGRP-MIB:cEigrpInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceigrpinterfaceentry is not None:
                for child_ref in self.ceigrpinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
            return meta._meta_table['CiscoEigrpMib.Ceigrpinterfacetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-EIGRP-MIB:CISCO-EIGRP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ceigrpinterfacetable is not None and self.ceigrpinterfacetable._has_data():
            return True

        if self.ceigrppeertable is not None and self.ceigrppeertable._has_data():
            return True

        if self.ceigrptopotable is not None and self.ceigrptopotable._has_data():
            return True

        if self.ceigrptraffstatstable is not None and self.ceigrptraffstatstable._has_data():
            return True

        if self.ceigrpvpntable is not None and self.ceigrpvpntable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_EIGRP_MIB as meta
        return meta._meta_table['CiscoEigrpMib']['meta_info']


