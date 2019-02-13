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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOEIGRPMIB(Entity):
    """
    
    
    .. attribute:: ceigrpvpntable
    
    	This table contains information on those VPN's configured to run EIGRP.  The VPN creation on a router is independent of the routing protocol to be used over it.   A VPN is given a name and has a dedicated routing table associated with it.  This routing table is identified internally by a unique integer value
    	**type**\:  :py:class:`CEigrpVpnTable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpVpnTable>`
    
    	**config**\: False
    
    .. attribute:: ceigrptraffstatstable
    
    	Table of EIGRP traffic statistics and information associated with all EIGRP autonomous systems
    	**type**\:  :py:class:`CEigrpTraffStatsTable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTraffStatsTable>`
    
    	**config**\: False
    
    .. attribute:: ceigrptopotable
    
    	The table of EIGRP routes and their associated attributes for an Autonomous System (AS) configured in a VPN is called a topology table.  All route entries in the topology table will be indexed by IP network type, IP network number and network mask (prefix) size
    	**type**\:  :py:class:`CEigrpTopoTable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTopoTable>`
    
    	**config**\: False
    
    .. attribute:: ceigrppeertable
    
    	The table of established EIGRP peers (neighbors) in the selected autonomous system.   Peers are indexed by their unique internal handle id, as well as the AS number and VPN id.   The peer entry is removed from the table if the peer is declared down
    	**type**\:  :py:class:`CEigrpPeerTable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpPeerTable>`
    
    	**config**\: False
    
    .. attribute:: ceigrpinterfacetable
    
    	The table of interfaces over which EIGRP is running, and their associated statistics.   This table is independent of whether any peer adjacencies have been formed over the interfaces or not.   Interfaces running EIGRP are determined by whether their assigned IP addresses fall within configured EIGRP network statements
    	**type**\:  :py:class:`CEigrpInterfaceTable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpInterfaceTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-EIGRP-MIB'
    _revision = '2004-11-16'

    def __init__(self):
        super(CISCOEIGRPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-EIGRP-MIB"
        self.yang_parent_name = "CISCO-EIGRP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cEigrpVpnTable", ("ceigrpvpntable", CISCOEIGRPMIB.CEigrpVpnTable)), ("cEigrpTraffStatsTable", ("ceigrptraffstatstable", CISCOEIGRPMIB.CEigrpTraffStatsTable)), ("cEigrpTopoTable", ("ceigrptopotable", CISCOEIGRPMIB.CEigrpTopoTable)), ("cEigrpPeerTable", ("ceigrppeertable", CISCOEIGRPMIB.CEigrpPeerTable)), ("cEigrpInterfaceTable", ("ceigrpinterfacetable", CISCOEIGRPMIB.CEigrpInterfaceTable))])
        self._leafs = OrderedDict()

        self.ceigrpvpntable = CISCOEIGRPMIB.CEigrpVpnTable()
        self.ceigrpvpntable.parent = self
        self._children_name_map["ceigrpvpntable"] = "cEigrpVpnTable"

        self.ceigrptraffstatstable = CISCOEIGRPMIB.CEigrpTraffStatsTable()
        self.ceigrptraffstatstable.parent = self
        self._children_name_map["ceigrptraffstatstable"] = "cEigrpTraffStatsTable"

        self.ceigrptopotable = CISCOEIGRPMIB.CEigrpTopoTable()
        self.ceigrptopotable.parent = self
        self._children_name_map["ceigrptopotable"] = "cEigrpTopoTable"

        self.ceigrppeertable = CISCOEIGRPMIB.CEigrpPeerTable()
        self.ceigrppeertable.parent = self
        self._children_name_map["ceigrppeertable"] = "cEigrpPeerTable"

        self.ceigrpinterfacetable = CISCOEIGRPMIB.CEigrpInterfaceTable()
        self.ceigrpinterfacetable.parent = self
        self._children_name_map["ceigrpinterfacetable"] = "cEigrpInterfaceTable"
        self._segment_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOEIGRPMIB, [], name, value)


    class CEigrpVpnTable(Entity):
        """
        This table contains information on those VPN's configured
        to run EIGRP.  The VPN creation on a router is independent
        of the routing protocol to be used over it.   A VPN is
        given a name and has a dedicated routing table associated
        with it.  This routing table is identified internally
        by a unique integer value.
        
        .. attribute:: ceigrpvpnentry
        
        	Information relating to a single VPN which is configured to run EIGRP
        	**type**\: list of  		 :py:class:`CEigrpVpnEntry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CISCOEIGRPMIB.CEigrpVpnTable, self).__init__()

            self.yang_name = "cEigrpVpnTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cEigrpVpnEntry", ("ceigrpvpnentry", CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry))])
            self._leafs = OrderedDict()

            self.ceigrpvpnentry = YList(self)
            self._segment_path = lambda: "cEigrpVpnTable"
            self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOEIGRPMIB.CEigrpVpnTable, [], name, value)


        class CEigrpVpnEntry(Entity):
            """
            Information relating to a single VPN which is configured
            to run EIGRP.
            
            .. attribute:: ceigrpvpnid  (key)
            
            	The unique VPN identifier.  This is a unique integer relative to all other VPN's defined on the router.  It also identifies internally the routing table instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpvpnname
            
            	The name given to the VPN
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry, self).__init__()

                self.yang_name = "cEigrpVpnEntry"
                self.yang_parent_name = "cEigrpVpnTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceigrpvpnid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceigrpvpnid', (YLeaf(YType.uint32, 'cEigrpVpnId'), ['int'])),
                    ('ceigrpvpnname', (YLeaf(YType.str, 'cEigrpVpnName'), ['str'])),
                ])
                self.ceigrpvpnid = None
                self.ceigrpvpnname = None
                self._segment_path = lambda: "cEigrpVpnEntry" + "[cEigrpVpnId='" + str(self.ceigrpvpnid) + "']"
                self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpVpnTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry, ['ceigrpvpnid', 'ceigrpvpnname'], name, value)




    class CEigrpTraffStatsTable(Entity):
        """
        Table of EIGRP traffic statistics and information
        associated with all EIGRP autonomous systems.
        
        .. attribute:: ceigrptraffstatsentry
        
        	The set of statistics and information for a single EIGRP Autonomous System
        	**type**\: list of  		 :py:class:`CEigrpTraffStatsEntry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CISCOEIGRPMIB.CEigrpTraffStatsTable, self).__init__()

            self.yang_name = "cEigrpTraffStatsTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cEigrpTraffStatsEntry", ("ceigrptraffstatsentry", CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry))])
            self._leafs = OrderedDict()

            self.ceigrptraffstatsentry = YList(self)
            self._segment_path = lambda: "cEigrpTraffStatsTable"
            self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOEIGRPMIB.CEigrpTraffStatsTable, [], name, value)


        class CEigrpTraffStatsEntry(Entity):
            """
            The set of statistics and information for a single EIGRP
            Autonomous System.
            
            .. attribute:: ceigrpvpnid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrpasnumber  (key)
            
            	The Autonomous System number which is unique integer per VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpnbrcount
            
            	The total number of live EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured in the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrphellossent
            
            	The total number Hello packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrphellosrcvd
            
            	The total number Hello packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpupdatessent
            
            	The total number routing update packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpupdatesrcvd
            
            	The total number routing update packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpqueriessent
            
            	The total number alternate route query packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpqueriesrcvd
            
            	The total number alternate route query packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrprepliessent
            
            	The total number query reply packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrprepliesrcvd
            
            	The total number query reply packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpackssent
            
            	The total number packet acknowledgements that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpacksrcvd
            
            	The total number packet acknowledgements that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpinputqhighmark
            
            	The highest number of EIGRP packets in the input queue waiting to be processed internally addressed to this AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpinputqdrops
            
            	The number of EIGRP packets dropped from the input queue due to it being full within the AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpsiaqueriessent
            
            	The total number of Stuck\-In\-Active (SIA) query packets sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpsiaqueriesrcvd
            
            	The total number of Stuck\-In\-Active (SIA) query packets received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpasrouteridtype
            
            	The format of the router\-id configured or automatically selected for the EIGRP AS
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceigrpasrouterid
            
            	The router\-id configured or automatically selected for the EIGRP AS.   Each EIGRP routing process has a unique router\-id selected from each autonomous system configured. The format is governed by object cEigrpAsRouterIdType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceigrptoporoutes
            
            	The total number of EIGRP derived routes currently existing in the topology table for the AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpheadserial
            
            	Routes in a topology table for an AS are assigned serial numbers and are sequenced internally as they are inserted and deleted.   The serial number of the first route in that internal sequence is called the head serial number. Each AS has its own topology table, and its own serial number space, each of which begins with the value 1. A serial number of zero implies that there are no routes in the topology
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: ceigrpnextserial
            
            	The serial number that would be assigned to the next new or changed route in the topology table for the AS
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: ceigrpxmitpendreplies
            
            	When alternate route query packets are sent to adjacent EIGRP peers in an AS, replies are expected.   This object is the total number of outstanding replies expected to queries that have been sent to peers in the current AS. It remains at zero most of the time until an EIGRP route becomes active
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpxmitdummies
            
            	A dummy is a temporary internal entity used as a place holder in the topology table for an AS. They are not transmitted in routing updates.  This is the total number currently in existence associated with the AS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry, self).__init__()

                self.yang_name = "cEigrpTraffStatsEntry"
                self.yang_parent_name = "cEigrpTraffStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceigrpvpnid','ceigrpasnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceigrpvpnid', (YLeaf(YType.str, 'cEigrpVpnId'), ['int'])),
                    ('ceigrpasnumber', (YLeaf(YType.uint32, 'cEigrpAsNumber'), ['int'])),
                    ('ceigrpnbrcount', (YLeaf(YType.uint32, 'cEigrpNbrCount'), ['int'])),
                    ('ceigrphellossent', (YLeaf(YType.uint32, 'cEigrpHellosSent'), ['int'])),
                    ('ceigrphellosrcvd', (YLeaf(YType.uint32, 'cEigrpHellosRcvd'), ['int'])),
                    ('ceigrpupdatessent', (YLeaf(YType.uint32, 'cEigrpUpdatesSent'), ['int'])),
                    ('ceigrpupdatesrcvd', (YLeaf(YType.uint32, 'cEigrpUpdatesRcvd'), ['int'])),
                    ('ceigrpqueriessent', (YLeaf(YType.uint32, 'cEigrpQueriesSent'), ['int'])),
                    ('ceigrpqueriesrcvd', (YLeaf(YType.uint32, 'cEigrpQueriesRcvd'), ['int'])),
                    ('ceigrprepliessent', (YLeaf(YType.uint32, 'cEigrpRepliesSent'), ['int'])),
                    ('ceigrprepliesrcvd', (YLeaf(YType.uint32, 'cEigrpRepliesRcvd'), ['int'])),
                    ('ceigrpackssent', (YLeaf(YType.uint32, 'cEigrpAcksSent'), ['int'])),
                    ('ceigrpacksrcvd', (YLeaf(YType.uint32, 'cEigrpAcksRcvd'), ['int'])),
                    ('ceigrpinputqhighmark', (YLeaf(YType.uint32, 'cEigrpInputQHighMark'), ['int'])),
                    ('ceigrpinputqdrops', (YLeaf(YType.uint32, 'cEigrpInputQDrops'), ['int'])),
                    ('ceigrpsiaqueriessent', (YLeaf(YType.uint32, 'cEigrpSiaQueriesSent'), ['int'])),
                    ('ceigrpsiaqueriesrcvd', (YLeaf(YType.uint32, 'cEigrpSiaQueriesRcvd'), ['int'])),
                    ('ceigrpasrouteridtype', (YLeaf(YType.enumeration, 'cEigrpAsRouterIdType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceigrpasrouterid', (YLeaf(YType.str, 'cEigrpAsRouterId'), ['str'])),
                    ('ceigrptoporoutes', (YLeaf(YType.uint32, 'cEigrpTopoRoutes'), ['int'])),
                    ('ceigrpheadserial', (YLeaf(YType.uint64, 'cEigrpHeadSerial'), ['int'])),
                    ('ceigrpnextserial', (YLeaf(YType.uint64, 'cEigrpNextSerial'), ['int'])),
                    ('ceigrpxmitpendreplies', (YLeaf(YType.uint32, 'cEigrpXmitPendReplies'), ['int'])),
                    ('ceigrpxmitdummies', (YLeaf(YType.uint32, 'cEigrpXmitDummies'), ['int'])),
                ])
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ceigrpnbrcount = None
                self.ceigrphellossent = None
                self.ceigrphellosrcvd = None
                self.ceigrpupdatessent = None
                self.ceigrpupdatesrcvd = None
                self.ceigrpqueriessent = None
                self.ceigrpqueriesrcvd = None
                self.ceigrprepliessent = None
                self.ceigrprepliesrcvd = None
                self.ceigrpackssent = None
                self.ceigrpacksrcvd = None
                self.ceigrpinputqhighmark = None
                self.ceigrpinputqdrops = None
                self.ceigrpsiaqueriessent = None
                self.ceigrpsiaqueriesrcvd = None
                self.ceigrpasrouteridtype = None
                self.ceigrpasrouterid = None
                self.ceigrptoporoutes = None
                self.ceigrpheadserial = None
                self.ceigrpnextserial = None
                self.ceigrpxmitpendreplies = None
                self.ceigrpxmitdummies = None
                self._segment_path = lambda: "cEigrpTraffStatsEntry" + "[cEigrpVpnId='" + str(self.ceigrpvpnid) + "']" + "[cEigrpAsNumber='" + str(self.ceigrpasnumber) + "']"
                self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpTraffStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry, ['ceigrpvpnid', 'ceigrpasnumber', 'ceigrpnbrcount', 'ceigrphellossent', 'ceigrphellosrcvd', 'ceigrpupdatessent', 'ceigrpupdatesrcvd', 'ceigrpqueriessent', 'ceigrpqueriesrcvd', 'ceigrprepliessent', 'ceigrprepliesrcvd', 'ceigrpackssent', 'ceigrpacksrcvd', 'ceigrpinputqhighmark', 'ceigrpinputqdrops', 'ceigrpsiaqueriessent', 'ceigrpsiaqueriesrcvd', 'ceigrpasrouteridtype', 'ceigrpasrouterid', 'ceigrptoporoutes', 'ceigrpheadserial', 'ceigrpnextserial', 'ceigrpxmitpendreplies', 'ceigrpxmitdummies'], name, value)




    class CEigrpTopoTable(Entity):
        """
        The table of EIGRP routes and their associated
        attributes for an Autonomous System (AS) configured
        in a VPN is called a topology table.  All route entries in
        the topology table will be indexed by IP network type,
        IP network number and network mask (prefix) size.
        
        .. attribute:: ceigrptopoentry
        
        	The entry for a single EIGRP topology table in the given AS
        	**type**\: list of  		 :py:class:`CEigrpTopoEntry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTopoTable.CEigrpTopoEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CISCOEIGRPMIB.CEigrpTopoTable, self).__init__()

            self.yang_name = "cEigrpTopoTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cEigrpTopoEntry", ("ceigrptopoentry", CISCOEIGRPMIB.CEigrpTopoTable.CEigrpTopoEntry))])
            self._leafs = OrderedDict()

            self.ceigrptopoentry = YList(self)
            self._segment_path = lambda: "cEigrpTopoTable"
            self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOEIGRPMIB.CEigrpTopoTable, [], name, value)


        class CEigrpTopoEntry(Entity):
            """
            The entry for a single EIGRP topology table in the given
            AS.
            
            .. attribute:: ceigrpvpnid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrpasnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrpdestnettype  (key)
            
            	The format of the destination IP network number for a single route in the topology table in the AS specified in cEigrpDestNet
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceigrpdestnet  (key)
            
            	The destination IP network number for a single route in the topology table in the AS.  The format is governed by object cEigrpDestNetType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceigrpdestnetprefixlen  (key)
            
            	The prefix length associated with the destination IP network address for a single route in the topology table in the AS.  The format is governed by the object cEigrpDestNetType
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: ceigrpactive
            
            	A value of true(1) indicates the route to the destination network has failed and an active (query) search for an alternative path is in progress.  A value of false(2) indicates the route is stable (passive)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: ceigrpstuckinactive
            
            	A value of true(1) indicates that that this route which is in active state (cEigrpActive = true(1)) has not received any replies to queries for alternate paths, and a second EIGRP route query, called a stuck\-in\-active query, has now been sent
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: ceigrpdestsuccessors
            
            	A successor is the next routing hop for a path to the destination IP network number for a single route in the topology table in the AS.  There can be several potential successors if there are multiple paths to the destination.   This is the total number of successors for a topology entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpfdistance
            
            	The feasibility (best) distance is the minimum distance from this router to the destination IP network in this topology entry.  The feasibility distance is used in determining the best successor for a path to the destination network
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrprouteorigintype
            
            	This is a text string describing the internal origin of the EIGRP route represented by the topology entry
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ceigrprouteoriginaddrtype
            
            	The format of the IP address defined as the origin of this topology route entry
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceigrprouteoriginaddr
            
            	If the origin of the topology route entry is external to this router, then this object is the IP address of the router from which it originated.  The format  is governed by object cEigrpRouteOriginAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceigrpnexthopaddresstype
            
            	The format of the next hop IP address for the route represented by the topology entry
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceigrpnexthopaddress
            
            	This is the next hop IP address for the route represented by the topology entry.   The next hop is where network traffic will be routed to in order to reach the destination network for this topology entry.  The format is governed by cEigrpNextHopAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceigrpnexthopinterface
            
            	The interface through which the next hop IP address is reached to send network traffic to the destination network represented by the topology entry
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ceigrpdistance
            
            	The computed distance to the destination network entry from this router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpreportdistance
            
            	The computed distance to the destination network in the topology entry reported to this router by the originator of this route
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CISCOEIGRPMIB.CEigrpTopoTable.CEigrpTopoEntry, self).__init__()

                self.yang_name = "cEigrpTopoEntry"
                self.yang_parent_name = "cEigrpTopoTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceigrpvpnid','ceigrpasnumber','ceigrpdestnettype','ceigrpdestnet','ceigrpdestnetprefixlen']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceigrpvpnid', (YLeaf(YType.str, 'cEigrpVpnId'), ['int'])),
                    ('ceigrpasnumber', (YLeaf(YType.str, 'cEigrpAsNumber'), ['int'])),
                    ('ceigrpdestnettype', (YLeaf(YType.enumeration, 'cEigrpDestNetType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceigrpdestnet', (YLeaf(YType.str, 'cEigrpDestNet'), ['str'])),
                    ('ceigrpdestnetprefixlen', (YLeaf(YType.uint32, 'cEigrpDestNetPrefixLen'), ['int'])),
                    ('ceigrpactive', (YLeaf(YType.boolean, 'cEigrpActive'), ['bool'])),
                    ('ceigrpstuckinactive', (YLeaf(YType.boolean, 'cEigrpStuckInActive'), ['bool'])),
                    ('ceigrpdestsuccessors', (YLeaf(YType.uint32, 'cEigrpDestSuccessors'), ['int'])),
                    ('ceigrpfdistance', (YLeaf(YType.uint32, 'cEigrpFdistance'), ['int'])),
                    ('ceigrprouteorigintype', (YLeaf(YType.str, 'cEigrpRouteOriginType'), ['str'])),
                    ('ceigrprouteoriginaddrtype', (YLeaf(YType.enumeration, 'cEigrpRouteOriginAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceigrprouteoriginaddr', (YLeaf(YType.str, 'cEigrpRouteOriginAddr'), ['str'])),
                    ('ceigrpnexthopaddresstype', (YLeaf(YType.enumeration, 'cEigrpNextHopAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceigrpnexthopaddress', (YLeaf(YType.str, 'cEigrpNextHopAddress'), ['str'])),
                    ('ceigrpnexthopinterface', (YLeaf(YType.str, 'cEigrpNextHopInterface'), ['str'])),
                    ('ceigrpdistance', (YLeaf(YType.uint32, 'cEigrpDistance'), ['int'])),
                    ('ceigrpreportdistance', (YLeaf(YType.uint32, 'cEigrpReportDistance'), ['int'])),
                ])
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ceigrpdestnettype = None
                self.ceigrpdestnet = None
                self.ceigrpdestnetprefixlen = None
                self.ceigrpactive = None
                self.ceigrpstuckinactive = None
                self.ceigrpdestsuccessors = None
                self.ceigrpfdistance = None
                self.ceigrprouteorigintype = None
                self.ceigrprouteoriginaddrtype = None
                self.ceigrprouteoriginaddr = None
                self.ceigrpnexthopaddresstype = None
                self.ceigrpnexthopaddress = None
                self.ceigrpnexthopinterface = None
                self.ceigrpdistance = None
                self.ceigrpreportdistance = None
                self._segment_path = lambda: "cEigrpTopoEntry" + "[cEigrpVpnId='" + str(self.ceigrpvpnid) + "']" + "[cEigrpAsNumber='" + str(self.ceigrpasnumber) + "']" + "[cEigrpDestNetType='" + str(self.ceigrpdestnettype) + "']" + "[cEigrpDestNet='" + str(self.ceigrpdestnet) + "']" + "[cEigrpDestNetPrefixLen='" + str(self.ceigrpdestnetprefixlen) + "']"
                self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpTopoTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOEIGRPMIB.CEigrpTopoTable.CEigrpTopoEntry, ['ceigrpvpnid', 'ceigrpasnumber', 'ceigrpdestnettype', 'ceigrpdestnet', 'ceigrpdestnetprefixlen', 'ceigrpactive', 'ceigrpstuckinactive', 'ceigrpdestsuccessors', 'ceigrpfdistance', 'ceigrprouteorigintype', 'ceigrprouteoriginaddrtype', 'ceigrprouteoriginaddr', 'ceigrpnexthopaddresstype', 'ceigrpnexthopaddress', 'ceigrpnexthopinterface', 'ceigrpdistance', 'ceigrpreportdistance'], name, value)




    class CEigrpPeerTable(Entity):
        """
        The table of established EIGRP peers (neighbors) in the
        selected autonomous system.   Peers are indexed by their
        unique internal handle id, as well as the AS number and
        VPN id.   The peer entry is removed from the table if
        the peer is declared down.
        
        .. attribute:: ceigrppeerentry
        
        	Statistics and operational parameters for a single peer in the AS
        	**type**\: list of  		 :py:class:`CEigrpPeerEntry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpPeerTable.CEigrpPeerEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CISCOEIGRPMIB.CEigrpPeerTable, self).__init__()

            self.yang_name = "cEigrpPeerTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cEigrpPeerEntry", ("ceigrppeerentry", CISCOEIGRPMIB.CEigrpPeerTable.CEigrpPeerEntry))])
            self._leafs = OrderedDict()

            self.ceigrppeerentry = YList(self)
            self._segment_path = lambda: "cEigrpPeerTable"
            self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOEIGRPMIB.CEigrpPeerTable, [], name, value)


        class CEigrpPeerEntry(Entity):
            """
            Statistics and operational parameters for a single peer
            in the AS.
            
            .. attribute:: ceigrpvpnid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrpasnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrphandle  (key)
            
            	The unique internal identifier for the peer in the AS. This is a unique value among peer entries in a selected table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrppeeraddrtype
            
            	The format of the remote source IP address used by the peer to establish the EIGRP adjacency with this router
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceigrppeeraddr
            
            	The source IP address used by the peer to establish the EIGRP adjacency with this router.  The format is governed by object cEigrpPeerAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceigrppeerifindex
            
            	The ifIndex of the interface on this router through which this peer can be reached
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ceigrpholdtime
            
            	The count\-down timer indicating how much time must pass without receiving a hello packet from this EIGRP peer before this router declares the peer down. A peer declared as down is removed from the table and is no longer visible
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: ceigrpuptime
            
            	The elapsed time since the EIGRP adjacency was first established with the peer
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ceigrpsrtt
            
            	The computed smooth round trip time for packets to and from the peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrprto
            
            	The computed retransmission timeout for the peer. This value is computed over time as packets are sent to the peer and acknowledgements are received from it, and is the amount of time to wait before resending a packet from the retransmission queue to the peer when an expected acknowledgement has not been received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppktsenqueued
            
            	The number of any EIGRP packets currently enqueued waiting to be sent to this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrplastseq
            
            	All transmitted EIGRP packets have a sequence number assigned. This is the sequence number of the last EIGRP packet sent to this peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpversion
            
            	The EIGRP version information reported by the remote peer
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ceigrpretrans
            
            	The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpretries
            
            	The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CISCOEIGRPMIB.CEigrpPeerTable.CEigrpPeerEntry, self).__init__()

                self.yang_name = "cEigrpPeerEntry"
                self.yang_parent_name = "cEigrpPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceigrpvpnid','ceigrpasnumber','ceigrphandle']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceigrpvpnid', (YLeaf(YType.str, 'cEigrpVpnId'), ['int'])),
                    ('ceigrpasnumber', (YLeaf(YType.str, 'cEigrpAsNumber'), ['int'])),
                    ('ceigrphandle', (YLeaf(YType.uint32, 'cEigrpHandle'), ['int'])),
                    ('ceigrppeeraddrtype', (YLeaf(YType.enumeration, 'cEigrpPeerAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceigrppeeraddr', (YLeaf(YType.str, 'cEigrpPeerAddr'), ['str'])),
                    ('ceigrppeerifindex', (YLeaf(YType.int32, 'cEigrpPeerIfIndex'), ['int'])),
                    ('ceigrpholdtime', (YLeaf(YType.uint32, 'cEigrpHoldTime'), ['int'])),
                    ('ceigrpuptime', (YLeaf(YType.str, 'cEigrpUpTime'), ['str'])),
                    ('ceigrpsrtt', (YLeaf(YType.uint32, 'cEigrpSrtt'), ['int'])),
                    ('ceigrprto', (YLeaf(YType.uint32, 'cEigrpRto'), ['int'])),
                    ('ceigrppktsenqueued', (YLeaf(YType.uint32, 'cEigrpPktsEnqueued'), ['int'])),
                    ('ceigrplastseq', (YLeaf(YType.uint32, 'cEigrpLastSeq'), ['int'])),
                    ('ceigrpversion', (YLeaf(YType.str, 'cEigrpVersion'), ['str'])),
                    ('ceigrpretrans', (YLeaf(YType.uint32, 'cEigrpRetrans'), ['int'])),
                    ('ceigrpretries', (YLeaf(YType.uint32, 'cEigrpRetries'), ['int'])),
                ])
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ceigrphandle = None
                self.ceigrppeeraddrtype = None
                self.ceigrppeeraddr = None
                self.ceigrppeerifindex = None
                self.ceigrpholdtime = None
                self.ceigrpuptime = None
                self.ceigrpsrtt = None
                self.ceigrprto = None
                self.ceigrppktsenqueued = None
                self.ceigrplastseq = None
                self.ceigrpversion = None
                self.ceigrpretrans = None
                self.ceigrpretries = None
                self._segment_path = lambda: "cEigrpPeerEntry" + "[cEigrpVpnId='" + str(self.ceigrpvpnid) + "']" + "[cEigrpAsNumber='" + str(self.ceigrpasnumber) + "']" + "[cEigrpHandle='" + str(self.ceigrphandle) + "']"
                self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpPeerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOEIGRPMIB.CEigrpPeerTable.CEigrpPeerEntry, ['ceigrpvpnid', 'ceigrpasnumber', 'ceigrphandle', 'ceigrppeeraddrtype', 'ceigrppeeraddr', 'ceigrppeerifindex', 'ceigrpholdtime', 'ceigrpuptime', 'ceigrpsrtt', 'ceigrprto', 'ceigrppktsenqueued', 'ceigrplastseq', 'ceigrpversion', 'ceigrpretrans', 'ceigrpretries'], name, value)




    class CEigrpInterfaceTable(Entity):
        """
        The table of interfaces over which EIGRP is running, and
        their associated statistics.   This table is independent
        of whether any peer adjacencies have been formed over
        the interfaces or not.   Interfaces running EIGRP are
        determined by whether their assigned IP addresses fall
        within configured EIGRP network statements.
        
        .. attribute:: ceigrpinterfaceentry
        
        	Information for a single interface running EIGRP in the AS and VPN
        	**type**\: list of  		 :py:class:`CEigrpInterfaceEntry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpInterfaceTable.CEigrpInterfaceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CISCOEIGRPMIB.CEigrpInterfaceTable, self).__init__()

            self.yang_name = "cEigrpInterfaceTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cEigrpInterfaceEntry", ("ceigrpinterfaceentry", CISCOEIGRPMIB.CEigrpInterfaceTable.CEigrpInterfaceEntry))])
            self._leafs = OrderedDict()

            self.ceigrpinterfaceentry = YList(self)
            self._segment_path = lambda: "cEigrpInterfaceTable"
            self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOEIGRPMIB.CEigrpInterfaceTable, [], name, value)


        class CEigrpInterfaceEntry(Entity):
            """
            Information for a single interface running EIGRP in the
            AS and VPN.
            
            .. attribute:: ceigrpvpnid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpVpnTable.CEigrpVpnEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrpasnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpTraffStatsTable.CEigrpTraffStatsEntry>`
            
            	**config**\: False
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: ceigrppeercount
            
            	The number of EIGRP adjacencies currently formed with peers reached through this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpxmitreliableq
            
            	The number of EIGRP packets currently waiting in the reliable transport (acknowledgement\-required)  transmission queue to be sent to a peer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpxmitunreliableq
            
            	The number EIGRP of packets currently waiting in the unreliable transport (no acknowledgement required) transmission queue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpmeansrtt
            
            	The average of all the computed smooth round trip time values for a packet to and from all peers established on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppacingreliable
            
            	The configured time interval between EIGRP packet transmissions on the interface when the reliable transport method is used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppacingunreliable
            
            	The configured time interval between EIGRP packet transmissions on the interface when the unreliable transport method is used
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpmflowtimer
            
            	The configured multicast flow control timer value for this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppendingroutes
            
            	The number of queued EIGRP routing updates awaiting transmission on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrphellointerval
            
            	The configured time interval between Hello packet transmissions for this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: ceigrpxmitnextserial
            
            	The serial number of the next EIGRP packet that is to be queued for transmission on this interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: ceigrpumcasts
            
            	The total number of unreliable (no acknowledgement required) EIGRP multicast packets sent on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrprmcasts
            
            	The total number of reliable (acknowledgement required) EIGRP multicast packets sent on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpuucasts
            
            	The total number of unreliable (no acknowledgement required) EIGRP unicast packets sent on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrprucasts
            
            	The total number of reliable (acknowledgement required) unicast packets sent on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpmcastexcepts
            
            	The total number of EIGRP multicast exception transmissions that have occurred on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpcrpkts
            
            	The total number EIGRP Conditional\-Receive packets sent on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpackssuppressed
            
            	The total number of individual EIGRP acknowledgement packets that have been suppressed and combined in an already enqueued outbound reliable packet on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpretranssent
            
            	The total number EIGRP packet retransmissions sent on the interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpoosrvcd
            
            	The total number of out\-of\-sequence EIGRP packets received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceigrpauthmode
            
            	The EIGRP authentication mode of the interface. none  \:  no authentication enabled on the interface md5   \:  MD5 authentication enabled on the interface
            	**type**\:  :py:class:`CEigrpAuthMode <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CISCOEIGRPMIB.CEigrpInterfaceTable.CEigrpInterfaceEntry.CEigrpAuthMode>`
            
            	**config**\: False
            
            .. attribute:: ceigrpauthkeychain
            
            	The name of the authentication key\-chain configured on this interface.   The key\-chain is a reference to which set of secret keys are to be accessed in order to determine which secret key string to use.  The key chain name is not the secret key string password and can also be used in other routing protocols, such as RIP and ISIS
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CISCOEIGRPMIB.CEigrpInterfaceTable.CEigrpInterfaceEntry, self).__init__()

                self.yang_name = "cEigrpInterfaceEntry"
                self.yang_parent_name = "cEigrpInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceigrpvpnid','ceigrpasnumber','ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceigrpvpnid', (YLeaf(YType.str, 'cEigrpVpnId'), ['int'])),
                    ('ceigrpasnumber', (YLeaf(YType.str, 'cEigrpAsNumber'), ['int'])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('ceigrppeercount', (YLeaf(YType.uint32, 'cEigrpPeerCount'), ['int'])),
                    ('ceigrpxmitreliableq', (YLeaf(YType.uint32, 'cEigrpXmitReliableQ'), ['int'])),
                    ('ceigrpxmitunreliableq', (YLeaf(YType.uint32, 'cEigrpXmitUnreliableQ'), ['int'])),
                    ('ceigrpmeansrtt', (YLeaf(YType.uint32, 'cEigrpMeanSrtt'), ['int'])),
                    ('ceigrppacingreliable', (YLeaf(YType.uint32, 'cEigrpPacingReliable'), ['int'])),
                    ('ceigrppacingunreliable', (YLeaf(YType.uint32, 'cEigrpPacingUnreliable'), ['int'])),
                    ('ceigrpmflowtimer', (YLeaf(YType.uint32, 'cEigrpMFlowTimer'), ['int'])),
                    ('ceigrppendingroutes', (YLeaf(YType.uint32, 'cEigrpPendingRoutes'), ['int'])),
                    ('ceigrphellointerval', (YLeaf(YType.uint32, 'cEigrpHelloInterval'), ['int'])),
                    ('ceigrpxmitnextserial', (YLeaf(YType.uint64, 'cEigrpXmitNextSerial'), ['int'])),
                    ('ceigrpumcasts', (YLeaf(YType.uint32, 'cEigrpUMcasts'), ['int'])),
                    ('ceigrprmcasts', (YLeaf(YType.uint32, 'cEigrpRMcasts'), ['int'])),
                    ('ceigrpuucasts', (YLeaf(YType.uint32, 'cEigrpUUcasts'), ['int'])),
                    ('ceigrprucasts', (YLeaf(YType.uint32, 'cEigrpRUcasts'), ['int'])),
                    ('ceigrpmcastexcepts', (YLeaf(YType.uint32, 'cEigrpMcastExcepts'), ['int'])),
                    ('ceigrpcrpkts', (YLeaf(YType.uint32, 'cEigrpCRpkts'), ['int'])),
                    ('ceigrpackssuppressed', (YLeaf(YType.uint32, 'cEigrpAcksSuppressed'), ['int'])),
                    ('ceigrpretranssent', (YLeaf(YType.uint32, 'cEigrpRetransSent'), ['int'])),
                    ('ceigrpoosrvcd', (YLeaf(YType.uint32, 'cEigrpOOSrvcd'), ['int'])),
                    ('ceigrpauthmode', (YLeaf(YType.enumeration, 'cEigrpAuthMode'), [('ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB', 'CISCOEIGRPMIB', 'CEigrpInterfaceTable.CEigrpInterfaceEntry.CEigrpAuthMode')])),
                    ('ceigrpauthkeychain', (YLeaf(YType.str, 'cEigrpAuthKeyChain'), ['str'])),
                ])
                self.ceigrpvpnid = None
                self.ceigrpasnumber = None
                self.ifindex = None
                self.ceigrppeercount = None
                self.ceigrpxmitreliableq = None
                self.ceigrpxmitunreliableq = None
                self.ceigrpmeansrtt = None
                self.ceigrppacingreliable = None
                self.ceigrppacingunreliable = None
                self.ceigrpmflowtimer = None
                self.ceigrppendingroutes = None
                self.ceigrphellointerval = None
                self.ceigrpxmitnextserial = None
                self.ceigrpumcasts = None
                self.ceigrprmcasts = None
                self.ceigrpuucasts = None
                self.ceigrprucasts = None
                self.ceigrpmcastexcepts = None
                self.ceigrpcrpkts = None
                self.ceigrpackssuppressed = None
                self.ceigrpretranssent = None
                self.ceigrpoosrvcd = None
                self.ceigrpauthmode = None
                self.ceigrpauthkeychain = None
                self._segment_path = lambda: "cEigrpInterfaceEntry" + "[cEigrpVpnId='" + str(self.ceigrpvpnid) + "']" + "[cEigrpAsNumber='" + str(self.ceigrpasnumber) + "']" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpInterfaceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOEIGRPMIB.CEigrpInterfaceTable.CEigrpInterfaceEntry, ['ceigrpvpnid', 'ceigrpasnumber', 'ifindex', 'ceigrppeercount', 'ceigrpxmitreliableq', 'ceigrpxmitunreliableq', 'ceigrpmeansrtt', 'ceigrppacingreliable', 'ceigrppacingunreliable', 'ceigrpmflowtimer', 'ceigrppendingroutes', 'ceigrphellointerval', 'ceigrpxmitnextserial', 'ceigrpumcasts', 'ceigrprmcasts', 'ceigrpuucasts', 'ceigrprucasts', 'ceigrpmcastexcepts', 'ceigrpcrpkts', 'ceigrpackssuppressed', 'ceigrpretranssent', 'ceigrpoosrvcd', 'ceigrpauthmode', 'ceigrpauthkeychain'], name, value)

            class CEigrpAuthMode(Enum):
                """
                CEigrpAuthMode (Enum Class)

                The EIGRP authentication mode of the interface.

                none  \:  no authentication enabled on the interface

                md5   \:  MD5 authentication enabled on the interface

                .. data:: none = 1

                .. data:: md5 = 2

                """

                none = Enum.YLeaf(1, "none")

                md5 = Enum.YLeaf(2, "md5")




    def clone_ptr(self):
        self._top_entity = CISCOEIGRPMIB()
        return self._top_entity



