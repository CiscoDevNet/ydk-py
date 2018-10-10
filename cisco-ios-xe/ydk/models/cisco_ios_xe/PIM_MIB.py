""" PIM_MIB 

The MIB module for management of PIM routers.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PIMMIB(Entity):
    """
    
    
    .. attribute:: pim
    
    	
    	**type**\:  :py:class:`Pim <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.Pim>`
    
    .. attribute:: piminterfacetable
    
    	The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table
    	**type**\:  :py:class:`PimInterfaceTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimInterfaceTable>`
    
    .. attribute:: pimneighbortable
    
    	The (conceptual) table listing the router's PIM neighbors
    	**type**\:  :py:class:`PimNeighborTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimNeighborTable>`
    
    .. attribute:: pimipmroutetable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteTable defined in the IP Multicast MIB
    	**type**\:  :py:class:`PimIpMRouteTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimIpMRouteTable>`
    
    .. attribute:: pimrptable
    
    	The (conceptual) table listing PIM version 1 information for the Rendezvous Points (RPs) for IP multicast groups. This table is deprecated since its function is replaced by the pimRPSetTable for PIM version 2
    	**type**\:  :py:class:`PimRPTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimRPTable>`
    
    	**status**\: deprecated
    
    .. attribute:: pimrpsettable
    
    	The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate\-RP\-Advertisements.  When the local router is not the BSR, this information is obtained from received RP\-Set messages
    	**type**\:  :py:class:`PimRPSetTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimRPSetTable>`
    
    .. attribute:: pimipmroutenexthoptable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteNextHopTable defined in the IP Multicast MIB
    	**type**\:  :py:class:`PimIpMRouteNextHopTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimIpMRouteNextHopTable>`
    
    .. attribute:: pimcandidaterptable
    
    	The (conceptual) table listing the IP multicast groups for which the local router is to advertise itself as a Candidate\-RP when the value of pimComponentCRPHoldTime is non\-zero.  If this table is empty, then the local router      will advertise itself as a Candidate\-RP for all groups (providing the value of pimComponentCRPHoldTime is non\- zero)
    	**type**\:  :py:class:`PimCandidateRPTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimCandidateRPTable>`
    
    .. attribute:: pimcomponenttable
    
    	The (conceptual) table containing objects specific to a PIM domain.  One row exists for each domain to which the router is connected.  A PIM\-SM domain is defined as an area of the network over which Bootstrap messages are forwarded. Typically, a PIM\-SM router will be a member of exactly one domain.  This table also supports, however, routers which may form a border between two PIM\-SM domains and do not forward Bootstrap messages between them
    	**type**\:  :py:class:`PimComponentTable <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimComponentTable>`
    
    

    """

    _prefix = 'PIM-MIB'
    _revision = '2000-09-28'

    def __init__(self):
        super(PIMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "PIM-MIB"
        self.yang_parent_name = "PIM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("pim", ("pim", PIMMIB.Pim)), ("pimInterfaceTable", ("piminterfacetable", PIMMIB.PimInterfaceTable)), ("pimNeighborTable", ("pimneighbortable", PIMMIB.PimNeighborTable)), ("pimIpMRouteTable", ("pimipmroutetable", PIMMIB.PimIpMRouteTable)), ("pimRPTable", ("pimrptable", PIMMIB.PimRPTable)), ("pimRPSetTable", ("pimrpsettable", PIMMIB.PimRPSetTable)), ("pimIpMRouteNextHopTable", ("pimipmroutenexthoptable", PIMMIB.PimIpMRouteNextHopTable)), ("pimCandidateRPTable", ("pimcandidaterptable", PIMMIB.PimCandidateRPTable)), ("pimComponentTable", ("pimcomponenttable", PIMMIB.PimComponentTable))])
        self._leafs = OrderedDict()

        self.pim = PIMMIB.Pim()
        self.pim.parent = self
        self._children_name_map["pim"] = "pim"

        self.piminterfacetable = PIMMIB.PimInterfaceTable()
        self.piminterfacetable.parent = self
        self._children_name_map["piminterfacetable"] = "pimInterfaceTable"

        self.pimneighbortable = PIMMIB.PimNeighborTable()
        self.pimneighbortable.parent = self
        self._children_name_map["pimneighbortable"] = "pimNeighborTable"

        self.pimipmroutetable = PIMMIB.PimIpMRouteTable()
        self.pimipmroutetable.parent = self
        self._children_name_map["pimipmroutetable"] = "pimIpMRouteTable"

        self.pimrptable = PIMMIB.PimRPTable()
        self.pimrptable.parent = self
        self._children_name_map["pimrptable"] = "pimRPTable"

        self.pimrpsettable = PIMMIB.PimRPSetTable()
        self.pimrpsettable.parent = self
        self._children_name_map["pimrpsettable"] = "pimRPSetTable"

        self.pimipmroutenexthoptable = PIMMIB.PimIpMRouteNextHopTable()
        self.pimipmroutenexthoptable.parent = self
        self._children_name_map["pimipmroutenexthoptable"] = "pimIpMRouteNextHopTable"

        self.pimcandidaterptable = PIMMIB.PimCandidateRPTable()
        self.pimcandidaterptable.parent = self
        self._children_name_map["pimcandidaterptable"] = "pimCandidateRPTable"

        self.pimcomponenttable = PIMMIB.PimComponentTable()
        self.pimcomponenttable.parent = self
        self._children_name_map["pimcomponenttable"] = "pimComponentTable"
        self._segment_path = lambda: "PIM-MIB:PIM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PIMMIB, [], name, value)


    class Pim(Entity):
        """
        
        
        .. attribute:: pimjoinpruneinterval
        
        	The default interval at which periodic PIM\-SM Join/Prune messages are to be sent
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.Pim, self).__init__()

            self.yang_name = "pim"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('pimjoinpruneinterval', (YLeaf(YType.int32, 'pimJoinPruneInterval'), ['int'])),
            ])
            self.pimjoinpruneinterval = None
            self._segment_path = lambda: "pim"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.Pim, [u'pimjoinpruneinterval'], name, value)


    class PimInterfaceTable(Entity):
        """
        The (conceptual) table listing the router's PIM interfaces.
        IGMP and PIM are enabled on all interfaces listed in this
        table.
        
        .. attribute:: piminterfaceentry
        
        	An entry (conceptual row) in the pimInterfaceTable
        	**type**\: list of  		 :py:class:`PimInterfaceEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimInterfaceTable.PimInterfaceEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimInterfaceTable, self).__init__()

            self.yang_name = "pimInterfaceTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimInterfaceEntry", ("piminterfaceentry", PIMMIB.PimInterfaceTable.PimInterfaceEntry))])
            self._leafs = OrderedDict()

            self.piminterfaceentry = YList(self)
            self._segment_path = lambda: "pimInterfaceTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimInterfaceTable, [], name, value)


        class PimInterfaceEntry(Entity):
            """
            An entry (conceptual row) in the pimInterfaceTable.
            
            .. attribute:: piminterfaceifindex  (key)
            
            	The ifIndex value of this PIM interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: piminterfaceaddress
            
            	The IP address of the PIM interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacenetmask
            
            	The network mask for the IP address of the PIM interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacemode
            
            	The configured mode of this PIM interface.  A value of sparseDense is only valid for PIMv1
            	**type**\:  :py:class:`PimInterfaceMode <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimInterfaceTable.PimInterfaceEntry.PimInterfaceMode>`
            
            .. attribute:: piminterfacedr
            
            	The Designated Router on this PIM interface.  For point\-to\- point interfaces, this object has the value 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacehellointerval
            
            	The frequency at which PIM Hello messages are transmitted on this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: piminterfacestatus
            
            	The status of this entry.  Creating the entry enables PIM on the interface; destroying the entry disables PIM on the interface
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: piminterfacejoinpruneinterval
            
            	The frequency at which PIM Join/Prune messages are transmitted on this PIM interface.  The default value of this object is the pimJoinPruneInterval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: piminterfacecbsrpreference
            
            	The preference value for the local interface as a candidate bootstrap router.  The value of \-1 is used to indicate that the local interface is not a candidate BSR interface
            	**type**\: int
            
            	**range:** \-1..255
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimInterfaceTable.PimInterfaceEntry, self).__init__()

                self.yang_name = "pimInterfaceEntry"
                self.yang_parent_name = "pimInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['piminterfaceifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('piminterfaceifindex', (YLeaf(YType.int32, 'pimInterfaceIfIndex'), ['int'])),
                    ('piminterfaceaddress', (YLeaf(YType.str, 'pimInterfaceAddress'), ['str'])),
                    ('piminterfacenetmask', (YLeaf(YType.str, 'pimInterfaceNetMask'), ['str'])),
                    ('piminterfacemode', (YLeaf(YType.enumeration, 'pimInterfaceMode'), [('ydk.models.cisco_ios_xe.PIM_MIB', 'PIMMIB', 'PimInterfaceTable.PimInterfaceEntry.PimInterfaceMode')])),
                    ('piminterfacedr', (YLeaf(YType.str, 'pimInterfaceDR'), ['str'])),
                    ('piminterfacehellointerval', (YLeaf(YType.int32, 'pimInterfaceHelloInterval'), ['int'])),
                    ('piminterfacestatus', (YLeaf(YType.enumeration, 'pimInterfaceStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('piminterfacejoinpruneinterval', (YLeaf(YType.int32, 'pimInterfaceJoinPruneInterval'), ['int'])),
                    ('piminterfacecbsrpreference', (YLeaf(YType.int32, 'pimInterfaceCBSRPreference'), ['int'])),
                ])
                self.piminterfaceifindex = None
                self.piminterfaceaddress = None
                self.piminterfacenetmask = None
                self.piminterfacemode = None
                self.piminterfacedr = None
                self.piminterfacehellointerval = None
                self.piminterfacestatus = None
                self.piminterfacejoinpruneinterval = None
                self.piminterfacecbsrpreference = None
                self._segment_path = lambda: "pimInterfaceEntry" + "[pimInterfaceIfIndex='" + str(self.piminterfaceifindex) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimInterfaceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimInterfaceTable.PimInterfaceEntry, [u'piminterfaceifindex', u'piminterfaceaddress', u'piminterfacenetmask', u'piminterfacemode', u'piminterfacedr', u'piminterfacehellointerval', u'piminterfacestatus', u'piminterfacejoinpruneinterval', u'piminterfacecbsrpreference'], name, value)

            class PimInterfaceMode(Enum):
                """
                PimInterfaceMode (Enum Class)

                The configured mode of this PIM interface.  A value of

                sparseDense is only valid for PIMv1.

                .. data:: dense = 1

                .. data:: sparse = 2

                .. data:: sparseDense = 3

                """

                dense = Enum.YLeaf(1, "dense")

                sparse = Enum.YLeaf(2, "sparse")

                sparseDense = Enum.YLeaf(3, "sparseDense")



    class PimNeighborTable(Entity):
        """
        The (conceptual) table listing the router's PIM neighbors.
        
        .. attribute:: pimneighborentry
        
        	An entry (conceptual row) in the pimNeighborTable
        	**type**\: list of  		 :py:class:`PimNeighborEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimNeighborTable.PimNeighborEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimNeighborTable, self).__init__()

            self.yang_name = "pimNeighborTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimNeighborEntry", ("pimneighborentry", PIMMIB.PimNeighborTable.PimNeighborEntry))])
            self._leafs = OrderedDict()

            self.pimneighborentry = YList(self)
            self._segment_path = lambda: "pimNeighborTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimNeighborTable, [], name, value)


        class PimNeighborEntry(Entity):
            """
            An entry (conceptual row) in the pimNeighborTable.
            
            .. attribute:: pimneighboraddress  (key)
            
            	The IP address of the PIM neighbor for which this entry contains information
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimneighborifindex
            
            	The value of ifIndex for the interface used to reach this PIM neighbor
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: pimneighboruptime
            
            	The time since this PIM neighbor (last) became a neighbor of the local router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimneighborexpirytime
            
            	The minimum time remaining before this PIM neighbor will be aged out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimneighbormode
            
            	The active PIM mode of this neighbor.  This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface
            	**type**\:  :py:class:`PimNeighborMode <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimNeighborTable.PimNeighborEntry.PimNeighborMode>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimNeighborTable.PimNeighborEntry, self).__init__()

                self.yang_name = "pimNeighborEntry"
                self.yang_parent_name = "pimNeighborTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pimneighboraddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pimneighboraddress', (YLeaf(YType.str, 'pimNeighborAddress'), ['str'])),
                    ('pimneighborifindex', (YLeaf(YType.int32, 'pimNeighborIfIndex'), ['int'])),
                    ('pimneighboruptime', (YLeaf(YType.uint32, 'pimNeighborUpTime'), ['int'])),
                    ('pimneighborexpirytime', (YLeaf(YType.uint32, 'pimNeighborExpiryTime'), ['int'])),
                    ('pimneighbormode', (YLeaf(YType.enumeration, 'pimNeighborMode'), [('ydk.models.cisco_ios_xe.PIM_MIB', 'PIMMIB', 'PimNeighborTable.PimNeighborEntry.PimNeighborMode')])),
                ])
                self.pimneighboraddress = None
                self.pimneighborifindex = None
                self.pimneighboruptime = None
                self.pimneighborexpirytime = None
                self.pimneighbormode = None
                self._segment_path = lambda: "pimNeighborEntry" + "[pimNeighborAddress='" + str(self.pimneighboraddress) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimNeighborTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimNeighborTable.PimNeighborEntry, [u'pimneighboraddress', u'pimneighborifindex', u'pimneighboruptime', u'pimneighborexpirytime', u'pimneighbormode'], name, value)

            class PimNeighborMode(Enum):
                """
                PimNeighborMode (Enum Class)

                The active PIM mode of this neighbor.  This object is

                deprecated for PIMv2 routers since all neighbors on the

                interface must be either dense or sparse as determined by

                the protocol running on the interface.

                .. data:: dense = 1

                .. data:: sparse = 2

                """

                dense = Enum.YLeaf(1, "dense")

                sparse = Enum.YLeaf(2, "sparse")



    class PimIpMRouteTable(Entity):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteTable defined in the IP
        Multicast MIB.
        
        .. attribute:: pimipmrouteentry
        
        	An entry (conceptual row) in the pimIpMRouteTable.  There is one entry per entry in the ipMRouteTable whose incoming interface is running PIM
        	**type**\: list of  		 :py:class:`PimIpMRouteEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimIpMRouteTable.PimIpMRouteEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimIpMRouteTable, self).__init__()

            self.yang_name = "pimIpMRouteTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimIpMRouteEntry", ("pimipmrouteentry", PIMMIB.PimIpMRouteTable.PimIpMRouteEntry))])
            self._leafs = OrderedDict()

            self.pimipmrouteentry = YList(self)
            self._segment_path = lambda: "pimIpMRouteTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimIpMRouteTable, [], name, value)


        class PimIpMRouteEntry(Entity):
            """
            An entry (conceptual row) in the pimIpMRouteTable.  There
            is one entry per entry in the ipMRouteTable whose incoming
            interface is running PIM.
            
            .. attribute:: ipmroutegroup  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutegroup <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteTable.IpMRouteEntry>`
            
            .. attribute:: ipmroutesource  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutesource <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteTable.IpMRouteEntry>`
            
            .. attribute:: ipmroutesourcemask  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutesourcemask <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteTable.IpMRouteEntry>`
            
            .. attribute:: pimipmrouteupstreamasserttimer
            
            	The time remaining before the router changes its upstream neighbor back to its RPF neighbor.  This timer is called the Assert timer in the PIM Sparse and Dense mode specification.      A value of 0 indicates that no Assert has changed the upstream neighbor away from the RPF neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimipmrouteassertmetric
            
            	The metric advertised by the assert winner on the upstream interface, or 0 if no such assert is in received
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertmetricpref
            
            	The preference advertised by the assert winner on the upstream interface, or 0 if no such assert is in effect
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertrptbit
            
            	The value of the RPT\-bit advertised by the assert winner on the upstream interface, or false if no such assert is in effect
            	**type**\: bool
            
            .. attribute:: pimipmrouteflags
            
            	This object describes PIM\-specific flags related to a multicast state entry.  See the PIM Sparse Mode specification for the meaning of the RPT and SPT bits
            	**type**\: str
            
            	**length:** 1
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimIpMRouteTable.PimIpMRouteEntry, self).__init__()

                self.yang_name = "pimIpMRouteEntry"
                self.yang_parent_name = "pimIpMRouteTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmroutegroup','ipmroutesource','ipmroutesourcemask']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmroutegroup', (YLeaf(YType.str, 'ipMRouteGroup'), ['str'])),
                    ('ipmroutesource', (YLeaf(YType.str, 'ipMRouteSource'), ['str'])),
                    ('ipmroutesourcemask', (YLeaf(YType.str, 'ipMRouteSourceMask'), ['str'])),
                    ('pimipmrouteupstreamasserttimer', (YLeaf(YType.uint32, 'pimIpMRouteUpstreamAssertTimer'), ['int'])),
                    ('pimipmrouteassertmetric', (YLeaf(YType.int32, 'pimIpMRouteAssertMetric'), ['int'])),
                    ('pimipmrouteassertmetricpref', (YLeaf(YType.int32, 'pimIpMRouteAssertMetricPref'), ['int'])),
                    ('pimipmrouteassertrptbit', (YLeaf(YType.boolean, 'pimIpMRouteAssertRPTBit'), ['bool'])),
                    ('pimipmrouteflags', (YLeaf(YType.str, 'pimIpMRouteFlags'), ['str'])),
                ])
                self.ipmroutegroup = None
                self.ipmroutesource = None
                self.ipmroutesourcemask = None
                self.pimipmrouteupstreamasserttimer = None
                self.pimipmrouteassertmetric = None
                self.pimipmrouteassertmetricpref = None
                self.pimipmrouteassertrptbit = None
                self.pimipmrouteflags = None
                self._segment_path = lambda: "pimIpMRouteEntry" + "[ipMRouteGroup='" + str(self.ipmroutegroup) + "']" + "[ipMRouteSource='" + str(self.ipmroutesource) + "']" + "[ipMRouteSourceMask='" + str(self.ipmroutesourcemask) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimIpMRouteTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimIpMRouteTable.PimIpMRouteEntry, [u'ipmroutegroup', u'ipmroutesource', u'ipmroutesourcemask', u'pimipmrouteupstreamasserttimer', u'pimipmrouteassertmetric', u'pimipmrouteassertmetricpref', u'pimipmrouteassertrptbit', u'pimipmrouteflags'], name, value)


    class PimRPTable(Entity):
        """
        The (conceptual) table listing PIM version 1 information
        for the Rendezvous Points (RPs) for IP multicast groups.
        This table is deprecated since its function is replaced by
        the pimRPSetTable for PIM version 2.
        
        .. attribute:: pimrpentry
        
        	An entry (conceptual row) in the pimRPTable.  There is one entry per RP address for each IP multicast group
        	**type**\: list of  		 :py:class:`PimRPEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimRPTable.PimRPEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimRPTable, self).__init__()

            self.yang_name = "pimRPTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimRPEntry", ("pimrpentry", PIMMIB.PimRPTable.PimRPEntry))])
            self._leafs = OrderedDict()

            self.pimrpentry = YList(self)
            self._segment_path = lambda: "pimRPTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimRPTable, [], name, value)


        class PimRPEntry(Entity):
            """
            An entry (conceptual row) in the pimRPTable.  There is one
            entry per RP address for each IP multicast group.
            
            .. attribute:: pimrpgroupaddress  (key)
            
            	The IP multicast group address for which this entry contains information about an RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: pimrpaddress  (key)
            
            	The unicast address of the RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: pimrpstate
            
            	The state of the RP
            	**type**\:  :py:class:`PimRPState <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimRPTable.PimRPEntry.PimRPState>`
            
            	**status**\: deprecated
            
            .. attribute:: pimrpstatetimer
            
            	The minimum time remaining before the next state change. When pimRPState is up, this is the minimum time which must expire until it can be declared down.  When pimRPState is down, this is the time until it will be declared up (in order to retry)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: pimrplastchange
            
            	The value of sysUpTime at the time when the corresponding instance of pimRPState last changed its value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: pimrprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimRPTable.PimRPEntry, self).__init__()

                self.yang_name = "pimRPEntry"
                self.yang_parent_name = "pimRPTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pimrpgroupaddress','pimrpaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pimrpgroupaddress', (YLeaf(YType.str, 'pimRPGroupAddress'), ['str'])),
                    ('pimrpaddress', (YLeaf(YType.str, 'pimRPAddress'), ['str'])),
                    ('pimrpstate', (YLeaf(YType.enumeration, 'pimRPState'), [('ydk.models.cisco_ios_xe.PIM_MIB', 'PIMMIB', 'PimRPTable.PimRPEntry.PimRPState')])),
                    ('pimrpstatetimer', (YLeaf(YType.uint32, 'pimRPStateTimer'), ['int'])),
                    ('pimrplastchange', (YLeaf(YType.uint32, 'pimRPLastChange'), ['int'])),
                    ('pimrprowstatus', (YLeaf(YType.enumeration, 'pimRPRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.pimrpgroupaddress = None
                self.pimrpaddress = None
                self.pimrpstate = None
                self.pimrpstatetimer = None
                self.pimrplastchange = None
                self.pimrprowstatus = None
                self._segment_path = lambda: "pimRPEntry" + "[pimRPGroupAddress='" + str(self.pimrpgroupaddress) + "']" + "[pimRPAddress='" + str(self.pimrpaddress) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimRPTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimRPTable.PimRPEntry, [u'pimrpgroupaddress', u'pimrpaddress', u'pimrpstate', u'pimrpstatetimer', u'pimrplastchange', u'pimrprowstatus'], name, value)

            class PimRPState(Enum):
                """
                PimRPState (Enum Class)

                The state of the RP.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")



    class PimRPSetTable(Entity):
        """
        The (conceptual) table listing PIM information for
        candidate Rendezvous Points (RPs) for IP multicast groups.
        When the local router is the BSR, this information is
        obtained from received Candidate\-RP\-Advertisements.  When
        the local router is not the BSR, this information is
        obtained from received RP\-Set messages.
        
        .. attribute:: pimrpsetentry
        
        	An entry (conceptual row) in the pimRPSetTable
        	**type**\: list of  		 :py:class:`PimRPSetEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimRPSetTable.PimRPSetEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimRPSetTable, self).__init__()

            self.yang_name = "pimRPSetTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimRPSetEntry", ("pimrpsetentry", PIMMIB.PimRPSetTable.PimRPSetEntry))])
            self._leafs = OrderedDict()

            self.pimrpsetentry = YList(self)
            self._segment_path = lambda: "pimRPSetTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimRPSetTable, [], name, value)


        class PimRPSetEntry(Entity):
            """
            An entry (conceptual row) in the pimRPSetTable.
            
            .. attribute:: pimrpsetcomponent  (key)
            
            	 A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: pimrpsetgroupaddress  (key)
            
            	The IP multicast group address which, when combined with pimRPSetGroupMask, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetgroupmask  (key)
            
            	The multicast group address mask which, when combined with pimRPSetGroupAddress, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetaddress  (key)
            
            	The IP address of the Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetholdtime
            
            	The holdtime of a Candidate\-RP.  If the local router is not the BSR, this value is 0
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: seconds
            
            .. attribute:: pimrpsetexpirytime
            
            	The minimum time remaining before the Candidate\-RP will be declared down.  If the local router is not the BSR, this value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimRPSetTable.PimRPSetEntry, self).__init__()

                self.yang_name = "pimRPSetEntry"
                self.yang_parent_name = "pimRPSetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pimrpsetcomponent','pimrpsetgroupaddress','pimrpsetgroupmask','pimrpsetaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pimrpsetcomponent', (YLeaf(YType.int32, 'pimRPSetComponent'), ['int'])),
                    ('pimrpsetgroupaddress', (YLeaf(YType.str, 'pimRPSetGroupAddress'), ['str'])),
                    ('pimrpsetgroupmask', (YLeaf(YType.str, 'pimRPSetGroupMask'), ['str'])),
                    ('pimrpsetaddress', (YLeaf(YType.str, 'pimRPSetAddress'), ['str'])),
                    ('pimrpsetholdtime', (YLeaf(YType.int32, 'pimRPSetHoldTime'), ['int'])),
                    ('pimrpsetexpirytime', (YLeaf(YType.uint32, 'pimRPSetExpiryTime'), ['int'])),
                ])
                self.pimrpsetcomponent = None
                self.pimrpsetgroupaddress = None
                self.pimrpsetgroupmask = None
                self.pimrpsetaddress = None
                self.pimrpsetholdtime = None
                self.pimrpsetexpirytime = None
                self._segment_path = lambda: "pimRPSetEntry" + "[pimRPSetComponent='" + str(self.pimrpsetcomponent) + "']" + "[pimRPSetGroupAddress='" + str(self.pimrpsetgroupaddress) + "']" + "[pimRPSetGroupMask='" + str(self.pimrpsetgroupmask) + "']" + "[pimRPSetAddress='" + str(self.pimrpsetaddress) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimRPSetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimRPSetTable.PimRPSetEntry, [u'pimrpsetcomponent', u'pimrpsetgroupaddress', u'pimrpsetgroupmask', u'pimrpsetaddress', u'pimrpsetholdtime', u'pimrpsetexpirytime'], name, value)


    class PimIpMRouteNextHopTable(Entity):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteNextHopTable defined in
        the IP Multicast MIB.
        
        .. attribute:: pimipmroutenexthopentry
        
        	An entry (conceptual row) in the pimIpMRouteNextHopTable. There is one entry per entry in the ipMRouteNextHopTable whose interface is running PIM and whose ipMRouteNextHopState is pruned(1)
        	**type**\: list of  		 :py:class:`PimIpMRouteNextHopEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimIpMRouteNextHopTable, self).__init__()

            self.yang_name = "pimIpMRouteNextHopTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimIpMRouteNextHopEntry", ("pimipmroutenexthopentry", PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry))])
            self._leafs = OrderedDict()

            self.pimipmroutenexthopentry = YList(self)
            self._segment_path = lambda: "pimIpMRouteNextHopTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimIpMRouteNextHopTable, [], name, value)


        class PimIpMRouteNextHopEntry(Entity):
            """
            An entry (conceptual row) in the pimIpMRouteNextHopTable.
            There is one entry per entry in the ipMRouteNextHopTable
            whose interface is running PIM and whose
            ipMRouteNextHopState is pruned(1).
            
            .. attribute:: ipmroutenexthopgroup  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopgroup <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteNextHopTable.IpMRouteNextHopEntry>`
            
            .. attribute:: ipmroutenexthopsource  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopsource <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteNextHopTable.IpMRouteNextHopEntry>`
            
            .. attribute:: ipmroutenexthopsourcemask  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopsourcemask <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteNextHopTable.IpMRouteNextHopEntry>`
            
            .. attribute:: ipmroutenexthopifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ipmroutenexthopifindex <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteNextHopTable.IpMRouteNextHopEntry>`
            
            .. attribute:: ipmroutenexthopaddress  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopaddress <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IPMROUTESTDMIB.IpMRouteNextHopTable.IpMRouteNextHopEntry>`
            
            .. attribute:: pimipmroutenexthopprunereason
            
            	This object indicates why the downstream interface was pruned, whether in response to a PIM prune message or due to PIM Assert processing
            	**type**\:  :py:class:`PimIpMRouteNextHopPruneReason <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry.PimIpMRouteNextHopPruneReason>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry, self).__init__()

                self.yang_name = "pimIpMRouteNextHopEntry"
                self.yang_parent_name = "pimIpMRouteNextHopTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipmroutenexthopgroup','ipmroutenexthopsource','ipmroutenexthopsourcemask','ipmroutenexthopifindex','ipmroutenexthopaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipmroutenexthopgroup', (YLeaf(YType.str, 'ipMRouteNextHopGroup'), ['str'])),
                    ('ipmroutenexthopsource', (YLeaf(YType.str, 'ipMRouteNextHopSource'), ['str'])),
                    ('ipmroutenexthopsourcemask', (YLeaf(YType.str, 'ipMRouteNextHopSourceMask'), ['str'])),
                    ('ipmroutenexthopifindex', (YLeaf(YType.str, 'ipMRouteNextHopIfIndex'), ['int'])),
                    ('ipmroutenexthopaddress', (YLeaf(YType.str, 'ipMRouteNextHopAddress'), ['str'])),
                    ('pimipmroutenexthopprunereason', (YLeaf(YType.enumeration, 'pimIpMRouteNextHopPruneReason'), [('ydk.models.cisco_ios_xe.PIM_MIB', 'PIMMIB', 'PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry.PimIpMRouteNextHopPruneReason')])),
                ])
                self.ipmroutenexthopgroup = None
                self.ipmroutenexthopsource = None
                self.ipmroutenexthopsourcemask = None
                self.ipmroutenexthopifindex = None
                self.ipmroutenexthopaddress = None
                self.pimipmroutenexthopprunereason = None
                self._segment_path = lambda: "pimIpMRouteNextHopEntry" + "[ipMRouteNextHopGroup='" + str(self.ipmroutenexthopgroup) + "']" + "[ipMRouteNextHopSource='" + str(self.ipmroutenexthopsource) + "']" + "[ipMRouteNextHopSourceMask='" + str(self.ipmroutenexthopsourcemask) + "']" + "[ipMRouteNextHopIfIndex='" + str(self.ipmroutenexthopifindex) + "']" + "[ipMRouteNextHopAddress='" + str(self.ipmroutenexthopaddress) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimIpMRouteNextHopTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry, [u'ipmroutenexthopgroup', u'ipmroutenexthopsource', u'ipmroutenexthopsourcemask', u'ipmroutenexthopifindex', u'ipmroutenexthopaddress', u'pimipmroutenexthopprunereason'], name, value)

            class PimIpMRouteNextHopPruneReason(Enum):
                """
                PimIpMRouteNextHopPruneReason (Enum Class)

                This object indicates why the downstream interface was

                pruned, whether in response to a PIM prune message or due to

                PIM Assert processing.

                .. data:: other = 1

                .. data:: prune = 2

                .. data:: assert_ = 3

                """

                other = Enum.YLeaf(1, "other")

                prune = Enum.YLeaf(2, "prune")

                assert_ = Enum.YLeaf(3, "assert")



    class PimCandidateRPTable(Entity):
        """
        The (conceptual) table listing the IP multicast groups for
        which the local router is to advertise itself as a
        Candidate\-RP when the value of pimComponentCRPHoldTime is
        non\-zero.  If this table is empty, then the local router
        
        
        
        
        
        will advertise itself as a Candidate\-RP for all groups
        (providing the value of pimComponentCRPHoldTime is non\-
        zero).
        
        .. attribute:: pimcandidaterpentry
        
        	An entry (conceptual row) in the pimCandidateRPTable
        	**type**\: list of  		 :py:class:`PimCandidateRPEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimCandidateRPTable.PimCandidateRPEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimCandidateRPTable, self).__init__()

            self.yang_name = "pimCandidateRPTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimCandidateRPEntry", ("pimcandidaterpentry", PIMMIB.PimCandidateRPTable.PimCandidateRPEntry))])
            self._leafs = OrderedDict()

            self.pimcandidaterpentry = YList(self)
            self._segment_path = lambda: "pimCandidateRPTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimCandidateRPTable, [], name, value)


        class PimCandidateRPEntry(Entity):
            """
            An entry (conceptual row) in the pimCandidateRPTable.
            
            .. attribute:: pimcandidaterpgroupaddress  (key)
            
            	The IP multicast group address which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpgroupmask  (key)
            
            	The multicast group address mask which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpaddress
            
            	The (unicast) address of the interface which will be      advertised as a Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimCandidateRPTable.PimCandidateRPEntry, self).__init__()

                self.yang_name = "pimCandidateRPEntry"
                self.yang_parent_name = "pimCandidateRPTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pimcandidaterpgroupaddress','pimcandidaterpgroupmask']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pimcandidaterpgroupaddress', (YLeaf(YType.str, 'pimCandidateRPGroupAddress'), ['str'])),
                    ('pimcandidaterpgroupmask', (YLeaf(YType.str, 'pimCandidateRPGroupMask'), ['str'])),
                    ('pimcandidaterpaddress', (YLeaf(YType.str, 'pimCandidateRPAddress'), ['str'])),
                    ('pimcandidaterprowstatus', (YLeaf(YType.enumeration, 'pimCandidateRPRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.pimcandidaterpgroupaddress = None
                self.pimcandidaterpgroupmask = None
                self.pimcandidaterpaddress = None
                self.pimcandidaterprowstatus = None
                self._segment_path = lambda: "pimCandidateRPEntry" + "[pimCandidateRPGroupAddress='" + str(self.pimcandidaterpgroupaddress) + "']" + "[pimCandidateRPGroupMask='" + str(self.pimcandidaterpgroupmask) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimCandidateRPTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimCandidateRPTable.PimCandidateRPEntry, [u'pimcandidaterpgroupaddress', u'pimcandidaterpgroupmask', u'pimcandidaterpaddress', u'pimcandidaterprowstatus'], name, value)


    class PimComponentTable(Entity):
        """
        The (conceptual) table containing objects specific to a PIM
        domain.  One row exists for each domain to which the router
        is connected.  A PIM\-SM domain is defined as an area of the
        network over which Bootstrap messages are forwarded.
        Typically, a PIM\-SM router will be a member of exactly one
        domain.  This table also supports, however, routers which
        may form a border between two PIM\-SM domains and do not
        forward Bootstrap messages between them.
        
        .. attribute:: pimcomponententry
        
        	An entry (conceptual row) in the pimComponentTable
        	**type**\: list of  		 :py:class:`PimComponentEntry <ydk.models.cisco_ios_xe.PIM_MIB.PIMMIB.PimComponentTable.PimComponentEntry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PIMMIB.PimComponentTable, self).__init__()

            self.yang_name = "pimComponentTable"
            self.yang_parent_name = "PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pimComponentEntry", ("pimcomponententry", PIMMIB.PimComponentTable.PimComponentEntry))])
            self._leafs = OrderedDict()

            self.pimcomponententry = YList(self)
            self._segment_path = lambda: "pimComponentTable"
            self._absolute_path = lambda: "PIM-MIB:PIM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PIMMIB.PimComponentTable, [], name, value)


        class PimComponentEntry(Entity):
            """
            An entry (conceptual row) in the pimComponentTable.
            
            .. attribute:: pimcomponentindex  (key)
            
            	A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value.  Routers that only support membership in a single PIM\-SM domain should use a pimComponentIndex value of 1
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: pimcomponentbsraddress
            
            	The IP address of the bootstrap router (BSR) for the local PIM region
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcomponentbsrexpirytime
            
            	The minimum time remaining before the bootstrap router in the local domain will be declared down.  For candidate BSRs, this is the time until the component sends an RP\-Set message.  For other routers, this is the time until it may accept an RP\-Set message from a lower candidate BSR
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimcomponentcrpholdtime
            
            	The holdtime of the component when it is a candidate RP in the local domain.  The value of 0 is used to indicate that the local system is not a Candidate\-RP
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: seconds
            
            .. attribute:: pimcomponentstatus
            
            	The status of this entry.  Creating the entry creates another protocol instance; destroying the entry disables a protocol instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PIMMIB.PimComponentTable.PimComponentEntry, self).__init__()

                self.yang_name = "pimComponentEntry"
                self.yang_parent_name = "pimComponentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pimcomponentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pimcomponentindex', (YLeaf(YType.int32, 'pimComponentIndex'), ['int'])),
                    ('pimcomponentbsraddress', (YLeaf(YType.str, 'pimComponentBSRAddress'), ['str'])),
                    ('pimcomponentbsrexpirytime', (YLeaf(YType.uint32, 'pimComponentBSRExpiryTime'), ['int'])),
                    ('pimcomponentcrpholdtime', (YLeaf(YType.int32, 'pimComponentCRPHoldTime'), ['int'])),
                    ('pimcomponentstatus', (YLeaf(YType.enumeration, 'pimComponentStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.pimcomponentindex = None
                self.pimcomponentbsraddress = None
                self.pimcomponentbsrexpirytime = None
                self.pimcomponentcrpholdtime = None
                self.pimcomponentstatus = None
                self._segment_path = lambda: "pimComponentEntry" + "[pimComponentIndex='" + str(self.pimcomponentindex) + "']"
                self._absolute_path = lambda: "PIM-MIB:PIM-MIB/pimComponentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PIMMIB.PimComponentTable.PimComponentEntry, [u'pimcomponentindex', u'pimcomponentbsraddress', u'pimcomponentbsrexpirytime', u'pimcomponentcrpholdtime', u'pimcomponentstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = PIMMIB()
        return self._top_entity

