""" TOKEN_RING_RMON_MIB 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EntryStatus(Enum):
    """
    EntryStatus (Enum Class)

    .. data:: valid = 1

    .. data:: createRequest = 2

    .. data:: underCreation = 3

    .. data:: invalid = 4

    """

    valid = Enum.YLeaf(1, "valid")

    createRequest = Enum.YLeaf(2, "createRequest")

    underCreation = Enum.YLeaf(3, "underCreation")

    invalid = Enum.YLeaf(4, "invalid")



class TOKENRINGRMONMIB(Entity):
    """
    
    
    .. attribute:: tokenringmlstatstable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\:  :py:class:`TokenRingMLStatsTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLStatsTable>`
    
    	**config**\: False
    
    .. attribute:: tokenringpstatstable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\:  :py:class:`TokenRingPStatsTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPStatsTable>`
    
    	**config**\: False
    
    .. attribute:: tokenringmlhistorytable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\:  :py:class:`TokenRingMLHistoryTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLHistoryTable>`
    
    	**config**\: False
    
    .. attribute:: tokenringphistorytable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\:  :py:class:`TokenRingPHistoryTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPHistoryTable>`
    
    	**config**\: False
    
    .. attribute:: ringstationcontroltable
    
    	A list of ringStation table control entries
    	**type**\:  :py:class:`RingStationControlTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationControlTable>`
    
    	**config**\: False
    
    .. attribute:: ringstationtable
    
    	A list of ring station entries.  An entry will exist for each station that is now or has      previously been detected as physically present on this ring
    	**type**\:  :py:class:`RingStationTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationTable>`
    
    	**config**\: False
    
    .. attribute:: ringstationordertable
    
    	A list of ring station entries for stations in the ring poll, ordered by their ring\-order
    	**type**\:  :py:class:`RingStationOrderTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationOrderTable>`
    
    	**config**\: False
    
    .. attribute:: ringstationconfigcontroltable
    
    	A list of ring station configuration control entries
    	**type**\:  :py:class:`RingStationConfigControlTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable>`
    
    	**config**\: False
    
    .. attribute:: ringstationconfigtable
    
    	A list of configuration entries for stations on a ring monitored by this probe
    	**type**\:  :py:class:`RingStationConfigTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigTable>`
    
    	**config**\: False
    
    .. attribute:: sourceroutingstatstable
    
    	A list of source routing statistics entries
    	**type**\:  :py:class:`SourceRoutingStatsTable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.SourceRoutingStatsTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'TOKEN-RING-RMON-MIB'

    def __init__(self):
        super(TOKENRINGRMONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "TOKEN-RING-RMON-MIB"
        self.yang_parent_name = "TOKEN-RING-RMON-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("tokenRingMLStatsTable", ("tokenringmlstatstable", TOKENRINGRMONMIB.TokenRingMLStatsTable)), ("tokenRingPStatsTable", ("tokenringpstatstable", TOKENRINGRMONMIB.TokenRingPStatsTable)), ("tokenRingMLHistoryTable", ("tokenringmlhistorytable", TOKENRINGRMONMIB.TokenRingMLHistoryTable)), ("tokenRingPHistoryTable", ("tokenringphistorytable", TOKENRINGRMONMIB.TokenRingPHistoryTable)), ("ringStationControlTable", ("ringstationcontroltable", TOKENRINGRMONMIB.RingStationControlTable)), ("ringStationTable", ("ringstationtable", TOKENRINGRMONMIB.RingStationTable)), ("ringStationOrderTable", ("ringstationordertable", TOKENRINGRMONMIB.RingStationOrderTable)), ("ringStationConfigControlTable", ("ringstationconfigcontroltable", TOKENRINGRMONMIB.RingStationConfigControlTable)), ("ringStationConfigTable", ("ringstationconfigtable", TOKENRINGRMONMIB.RingStationConfigTable)), ("sourceRoutingStatsTable", ("sourceroutingstatstable", TOKENRINGRMONMIB.SourceRoutingStatsTable))])
        self._leafs = OrderedDict()

        self.tokenringmlstatstable = TOKENRINGRMONMIB.TokenRingMLStatsTable()
        self.tokenringmlstatstable.parent = self
        self._children_name_map["tokenringmlstatstable"] = "tokenRingMLStatsTable"

        self.tokenringpstatstable = TOKENRINGRMONMIB.TokenRingPStatsTable()
        self.tokenringpstatstable.parent = self
        self._children_name_map["tokenringpstatstable"] = "tokenRingPStatsTable"

        self.tokenringmlhistorytable = TOKENRINGRMONMIB.TokenRingMLHistoryTable()
        self.tokenringmlhistorytable.parent = self
        self._children_name_map["tokenringmlhistorytable"] = "tokenRingMLHistoryTable"

        self.tokenringphistorytable = TOKENRINGRMONMIB.TokenRingPHistoryTable()
        self.tokenringphistorytable.parent = self
        self._children_name_map["tokenringphistorytable"] = "tokenRingPHistoryTable"

        self.ringstationcontroltable = TOKENRINGRMONMIB.RingStationControlTable()
        self.ringstationcontroltable.parent = self
        self._children_name_map["ringstationcontroltable"] = "ringStationControlTable"

        self.ringstationtable = TOKENRINGRMONMIB.RingStationTable()
        self.ringstationtable.parent = self
        self._children_name_map["ringstationtable"] = "ringStationTable"

        self.ringstationordertable = TOKENRINGRMONMIB.RingStationOrderTable()
        self.ringstationordertable.parent = self
        self._children_name_map["ringstationordertable"] = "ringStationOrderTable"

        self.ringstationconfigcontroltable = TOKENRINGRMONMIB.RingStationConfigControlTable()
        self.ringstationconfigcontroltable.parent = self
        self._children_name_map["ringstationconfigcontroltable"] = "ringStationConfigControlTable"

        self.ringstationconfigtable = TOKENRINGRMONMIB.RingStationConfigTable()
        self.ringstationconfigtable.parent = self
        self._children_name_map["ringstationconfigtable"] = "ringStationConfigTable"

        self.sourceroutingstatstable = TOKENRINGRMONMIB.SourceRoutingStatsTable()
        self.sourceroutingstatstable.parent = self
        self._children_name_map["sourceroutingstatstable"] = "sourceRoutingStatsTable"
        self._segment_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TOKENRINGRMONMIB, [], name, value)


    class TokenRingMLStatsTable(Entity):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlstatsentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`TokenRingMLStatsEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLStatsTable.TokenRingMLStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.TokenRingMLStatsTable, self).__init__()

            self.yang_name = "tokenRingMLStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tokenRingMLStatsEntry", ("tokenringmlstatsentry", TOKENRINGRMONMIB.TokenRingMLStatsTable.TokenRingMLStatsEntry))])
            self._leafs = OrderedDict()

            self.tokenringmlstatsentry = YList(self)
            self._segment_path = lambda: "tokenRingMLStatsTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.TokenRingMLStatsTable, [], name, value)


        class TokenRingMLStatsEntry(Entity):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlstatsindex  (key)
            
            	The value of this object uniquely identifies this tokenRingMLStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsdatasource
            
            	This object identifies the source of the data that this tokenRingMLStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all error reports on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingMLStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingPStatsDropEvents
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsmacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsmacpkts
            
            	The total number of MAC packets (excluding packets that were not good frames) received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsringpurgeevents
            
            	The total number of times that the ring enters the ring purge state from normal ring state.  The ring purge state that comes in response to the claim token or beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsringpurgepkts
            
            	The total number of ring purge MAC packets detected by probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsbeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState,      beaconSetRecoveryModeState, or beaconRingSignalLossState) from a non\-beaconing state.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsbeacontime
            
            	The total amount of time that the ring has been in the beaconing state
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsbeaconpkts
            
            	The total number of beacon MAC packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state.  The claim token state that comes in response to a beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsnaunchanges
            
            	The total number of NAUN changes detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatslineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsbursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsacerrors
            
            	The total number of AC (Address Copied)  errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatslostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatscongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatstokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatssofterrorreports
            
            	The total number of soft error report frames detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsringpollevents
            
            	The total number of ring poll events detected by the probe (i.e. the number of ring polls initiated by the active monitor that were detected)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsstatus
            
            	The status of this tokenRingMLStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.TokenRingMLStatsTable.TokenRingMLStatsEntry, self).__init__()

                self.yang_name = "tokenRingMLStatsEntry"
                self.yang_parent_name = "tokenRingMLStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringmlstatsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringmlstatsindex', (YLeaf(YType.int32, 'tokenRingMLStatsIndex'), ['int'])),
                    ('tokenringmlstatsdatasource', (YLeaf(YType.str, 'tokenRingMLStatsDataSource'), ['str'])),
                    ('tokenringmlstatsdropevents', (YLeaf(YType.uint32, 'tokenRingMLStatsDropEvents'), ['int'])),
                    ('tokenringmlstatsmacoctets', (YLeaf(YType.uint32, 'tokenRingMLStatsMacOctets'), ['int'])),
                    ('tokenringmlstatsmacpkts', (YLeaf(YType.uint32, 'tokenRingMLStatsMacPkts'), ['int'])),
                    ('tokenringmlstatsringpurgeevents', (YLeaf(YType.uint32, 'tokenRingMLStatsRingPurgeEvents'), ['int'])),
                    ('tokenringmlstatsringpurgepkts', (YLeaf(YType.uint32, 'tokenRingMLStatsRingPurgePkts'), ['int'])),
                    ('tokenringmlstatsbeaconevents', (YLeaf(YType.uint32, 'tokenRingMLStatsBeaconEvents'), ['int'])),
                    ('tokenringmlstatsbeacontime', (YLeaf(YType.int32, 'tokenRingMLStatsBeaconTime'), ['int'])),
                    ('tokenringmlstatsbeaconpkts', (YLeaf(YType.uint32, 'tokenRingMLStatsBeaconPkts'), ['int'])),
                    ('tokenringmlstatsclaimtokenevents', (YLeaf(YType.uint32, 'tokenRingMLStatsClaimTokenEvents'), ['int'])),
                    ('tokenringmlstatsclaimtokenpkts', (YLeaf(YType.uint32, 'tokenRingMLStatsClaimTokenPkts'), ['int'])),
                    ('tokenringmlstatsnaunchanges', (YLeaf(YType.uint32, 'tokenRingMLStatsNAUNChanges'), ['int'])),
                    ('tokenringmlstatslineerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsLineErrors'), ['int'])),
                    ('tokenringmlstatsinternalerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsInternalErrors'), ['int'])),
                    ('tokenringmlstatsbursterrors', (YLeaf(YType.uint32, 'tokenRingMLStatsBurstErrors'), ['int'])),
                    ('tokenringmlstatsacerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsACErrors'), ['int'])),
                    ('tokenringmlstatsaborterrors', (YLeaf(YType.uint32, 'tokenRingMLStatsAbortErrors'), ['int'])),
                    ('tokenringmlstatslostframeerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsLostFrameErrors'), ['int'])),
                    ('tokenringmlstatscongestionerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsCongestionErrors'), ['int'])),
                    ('tokenringmlstatsframecopiederrors', (YLeaf(YType.uint32, 'tokenRingMLStatsFrameCopiedErrors'), ['int'])),
                    ('tokenringmlstatsfrequencyerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsFrequencyErrors'), ['int'])),
                    ('tokenringmlstatstokenerrors', (YLeaf(YType.uint32, 'tokenRingMLStatsTokenErrors'), ['int'])),
                    ('tokenringmlstatssofterrorreports', (YLeaf(YType.uint32, 'tokenRingMLStatsSoftErrorReports'), ['int'])),
                    ('tokenringmlstatsringpollevents', (YLeaf(YType.uint32, 'tokenRingMLStatsRingPollEvents'), ['int'])),
                    ('tokenringmlstatsowner', (YLeaf(YType.str, 'tokenRingMLStatsOwner'), ['str'])),
                    ('tokenringmlstatsstatus', (YLeaf(YType.enumeration, 'tokenRingMLStatsStatus'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntryStatus', '')])),
                    ('tokenringmlstatsdroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:tokenRingMLStatsDroppedFrames'), ['int'])),
                    ('tokenringmlstatscreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:tokenRingMLStatsCreateTime'), ['int'])),
                ])
                self.tokenringmlstatsindex = None
                self.tokenringmlstatsdatasource = None
                self.tokenringmlstatsdropevents = None
                self.tokenringmlstatsmacoctets = None
                self.tokenringmlstatsmacpkts = None
                self.tokenringmlstatsringpurgeevents = None
                self.tokenringmlstatsringpurgepkts = None
                self.tokenringmlstatsbeaconevents = None
                self.tokenringmlstatsbeacontime = None
                self.tokenringmlstatsbeaconpkts = None
                self.tokenringmlstatsclaimtokenevents = None
                self.tokenringmlstatsclaimtokenpkts = None
                self.tokenringmlstatsnaunchanges = None
                self.tokenringmlstatslineerrors = None
                self.tokenringmlstatsinternalerrors = None
                self.tokenringmlstatsbursterrors = None
                self.tokenringmlstatsacerrors = None
                self.tokenringmlstatsaborterrors = None
                self.tokenringmlstatslostframeerrors = None
                self.tokenringmlstatscongestionerrors = None
                self.tokenringmlstatsframecopiederrors = None
                self.tokenringmlstatsfrequencyerrors = None
                self.tokenringmlstatstokenerrors = None
                self.tokenringmlstatssofterrorreports = None
                self.tokenringmlstatsringpollevents = None
                self.tokenringmlstatsowner = None
                self.tokenringmlstatsstatus = None
                self.tokenringmlstatsdroppedframes = None
                self.tokenringmlstatscreatetime = None
                self._segment_path = lambda: "tokenRingMLStatsEntry" + "[tokenRingMLStatsIndex='" + str(self.tokenringmlstatsindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingMLStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.TokenRingMLStatsTable.TokenRingMLStatsEntry, ['tokenringmlstatsindex', 'tokenringmlstatsdatasource', 'tokenringmlstatsdropevents', 'tokenringmlstatsmacoctets', 'tokenringmlstatsmacpkts', 'tokenringmlstatsringpurgeevents', 'tokenringmlstatsringpurgepkts', 'tokenringmlstatsbeaconevents', 'tokenringmlstatsbeacontime', 'tokenringmlstatsbeaconpkts', 'tokenringmlstatsclaimtokenevents', 'tokenringmlstatsclaimtokenpkts', 'tokenringmlstatsnaunchanges', 'tokenringmlstatslineerrors', 'tokenringmlstatsinternalerrors', 'tokenringmlstatsbursterrors', 'tokenringmlstatsacerrors', 'tokenringmlstatsaborterrors', 'tokenringmlstatslostframeerrors', 'tokenringmlstatscongestionerrors', 'tokenringmlstatsframecopiederrors', 'tokenringmlstatsfrequencyerrors', 'tokenringmlstatstokenerrors', 'tokenringmlstatssofterrorreports', 'tokenringmlstatsringpollevents', 'tokenringmlstatsowner', 'tokenringmlstatsstatus', 'tokenringmlstatsdroppedframes', 'tokenringmlstatscreatetime'], name, value)




    class TokenRingPStatsTable(Entity):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringpstatsentry
        
        	A collection of promiscuous statistics kept for non\-MAC packets on a particular Token Ring interface
        	**type**\: list of  		 :py:class:`TokenRingPStatsEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPStatsTable.TokenRingPStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.TokenRingPStatsTable, self).__init__()

            self.yang_name = "tokenRingPStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tokenRingPStatsEntry", ("tokenringpstatsentry", TOKENRINGRMONMIB.TokenRingPStatsTable.TokenRingPStatsEntry))])
            self._leafs = OrderedDict()

            self.tokenringpstatsentry = YList(self)
            self._segment_path = lambda: "tokenRingPStatsTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.TokenRingPStatsTable, [], name, value)


        class TokenRingPStatsEntry(Entity):
            """
            A collection of promiscuous statistics kept for
            non\-MAC packets on a particular Token Ring
            interface.
            
            .. attribute:: tokenringpstatsindex  (key)
            
            	The value of this object uniquely identifies this tokenRingPStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatasource
            
            	This object identifies the source of the data that this tokenRingPStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all non\-MAC packets on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingPStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingMLStatsDropEvents
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts
            
            	The total number of non\-MAC packets in good frames.  received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatabroadcastpkts
            
            	The total number of good non\-MAC frames received that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatamulticastpkts
            
            	The total number of good non\-MAC frames received that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts18to63octets
            
            	The total number of good non\-MAC frames received that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts64to127octets
            
            	The total number of good non\-MAC frames received that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts128to255octets
            
            	The total number of good non\-MAC frames received that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts256to511octets
            
            	The total number of good non\-MAC frames received that were between 256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts512to1023octets
            
            	The total number of good non\-MAC frames received that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsstatus
            
            	The status of this tokenRingPStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: tokenringpstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringpstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.TokenRingPStatsTable.TokenRingPStatsEntry, self).__init__()

                self.yang_name = "tokenRingPStatsEntry"
                self.yang_parent_name = "tokenRingPStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringpstatsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringpstatsindex', (YLeaf(YType.int32, 'tokenRingPStatsIndex'), ['int'])),
                    ('tokenringpstatsdatasource', (YLeaf(YType.str, 'tokenRingPStatsDataSource'), ['str'])),
                    ('tokenringpstatsdropevents', (YLeaf(YType.uint32, 'tokenRingPStatsDropEvents'), ['int'])),
                    ('tokenringpstatsdataoctets', (YLeaf(YType.uint32, 'tokenRingPStatsDataOctets'), ['int'])),
                    ('tokenringpstatsdatapkts', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts'), ['int'])),
                    ('tokenringpstatsdatabroadcastpkts', (YLeaf(YType.uint32, 'tokenRingPStatsDataBroadcastPkts'), ['int'])),
                    ('tokenringpstatsdatamulticastpkts', (YLeaf(YType.uint32, 'tokenRingPStatsDataMulticastPkts'), ['int'])),
                    ('tokenringpstatsdatapkts18to63octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts18to63Octets'), ['int'])),
                    ('tokenringpstatsdatapkts64to127octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts64to127Octets'), ['int'])),
                    ('tokenringpstatsdatapkts128to255octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts128to255Octets'), ['int'])),
                    ('tokenringpstatsdatapkts256to511octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts256to511Octets'), ['int'])),
                    ('tokenringpstatsdatapkts512to1023octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts512to1023Octets'), ['int'])),
                    ('tokenringpstatsdatapkts1024to2047octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts1024to2047Octets'), ['int'])),
                    ('tokenringpstatsdatapkts2048to4095octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts2048to4095Octets'), ['int'])),
                    ('tokenringpstatsdatapkts4096to8191octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts4096to8191Octets'), ['int'])),
                    ('tokenringpstatsdatapkts8192to18000octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPkts8192to18000Octets'), ['int'])),
                    ('tokenringpstatsdatapktsgreaterthan18000octets', (YLeaf(YType.uint32, 'tokenRingPStatsDataPktsGreaterThan18000Octets'), ['int'])),
                    ('tokenringpstatsowner', (YLeaf(YType.str, 'tokenRingPStatsOwner'), ['str'])),
                    ('tokenringpstatsstatus', (YLeaf(YType.enumeration, 'tokenRingPStatsStatus'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntryStatus', '')])),
                    ('tokenringpstatsdroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:tokenRingPStatsDroppedFrames'), ['int'])),
                    ('tokenringpstatscreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:tokenRingPStatsCreateTime'), ['int'])),
                ])
                self.tokenringpstatsindex = None
                self.tokenringpstatsdatasource = None
                self.tokenringpstatsdropevents = None
                self.tokenringpstatsdataoctets = None
                self.tokenringpstatsdatapkts = None
                self.tokenringpstatsdatabroadcastpkts = None
                self.tokenringpstatsdatamulticastpkts = None
                self.tokenringpstatsdatapkts18to63octets = None
                self.tokenringpstatsdatapkts64to127octets = None
                self.tokenringpstatsdatapkts128to255octets = None
                self.tokenringpstatsdatapkts256to511octets = None
                self.tokenringpstatsdatapkts512to1023octets = None
                self.tokenringpstatsdatapkts1024to2047octets = None
                self.tokenringpstatsdatapkts2048to4095octets = None
                self.tokenringpstatsdatapkts4096to8191octets = None
                self.tokenringpstatsdatapkts8192to18000octets = None
                self.tokenringpstatsdatapktsgreaterthan18000octets = None
                self.tokenringpstatsowner = None
                self.tokenringpstatsstatus = None
                self.tokenringpstatsdroppedframes = None
                self.tokenringpstatscreatetime = None
                self._segment_path = lambda: "tokenRingPStatsEntry" + "[tokenRingPStatsIndex='" + str(self.tokenringpstatsindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingPStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.TokenRingPStatsTable.TokenRingPStatsEntry, ['tokenringpstatsindex', 'tokenringpstatsdatasource', 'tokenringpstatsdropevents', 'tokenringpstatsdataoctets', 'tokenringpstatsdatapkts', 'tokenringpstatsdatabroadcastpkts', 'tokenringpstatsdatamulticastpkts', 'tokenringpstatsdatapkts18to63octets', 'tokenringpstatsdatapkts64to127octets', 'tokenringpstatsdatapkts128to255octets', 'tokenringpstatsdatapkts256to511octets', 'tokenringpstatsdatapkts512to1023octets', 'tokenringpstatsdatapkts1024to2047octets', 'tokenringpstatsdatapkts2048to4095octets', 'tokenringpstatsdatapkts4096to8191octets', 'tokenringpstatsdatapkts8192to18000octets', 'tokenringpstatsdatapktsgreaterthan18000octets', 'tokenringpstatsowner', 'tokenringpstatsstatus', 'tokenringpstatsdroppedframes', 'tokenringpstatscreatetime'], name, value)




    class TokenRingMLHistoryTable(Entity):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlhistoryentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`TokenRingMLHistoryEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLHistoryTable.TokenRingMLHistoryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.TokenRingMLHistoryTable, self).__init__()

            self.yang_name = "tokenRingMLHistoryTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tokenRingMLHistoryEntry", ("tokenringmlhistoryentry", TOKENRINGRMONMIB.TokenRingMLHistoryTable.TokenRingMLHistoryEntry))])
            self._leafs = OrderedDict()

            self.tokenringmlhistoryentry = YList(self)
            self._segment_path = lambda: "tokenRingMLHistoryTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.TokenRingMLHistoryTable, [], name, value)


        class TokenRingMLHistoryEntry(Entity):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlhistoryindex  (key)
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorysampleindex  (key)
            
            	An index that uniquely identifies the particular Mac\-Layer sample this entry represents among all Mac\-Layer samples associated with the same historyControlEntry.  This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorydropevents
            
            	The total number of events in which packets were      dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorymacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network during this sampling interval (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorymacpkts
            
            	The total number of MAC packets (excluding those that were not good frames) received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryringpurgeevents
            
            	The total number of times that the ring entered the ring purge state from normal ring state during this sampling interval.  The ring purge state that comes from the claim token or beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryringpurgepkts
            
            	The total number of Ring Purge MAC packets detected by the probe during this sampling      interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorybeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState, beaconSetRecoveryModeState, or beaconRingSignalLossState) during this sampling interval.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorybeacontime
            
            	The amount of time that the ring has been in the beaconing state during this sampling interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorybeaconpkts
            
            	The total number of beacon MAC packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state during this sampling interval. The claim token state that comes from the beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorynaunchanges
            
            	The total number of NAUN changes detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorylineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorybursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorylostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorycongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorytokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistorysofterrorreports
            
            	The total number of soft error report frames detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryringpollevents
            
            	The total number of ring poll events detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringmlhistoryactivestations
            
            	The maximum number of active stations on the ring detected by the probe during this sampling      interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.TokenRingMLHistoryTable.TokenRingMLHistoryEntry, self).__init__()

                self.yang_name = "tokenRingMLHistoryEntry"
                self.yang_parent_name = "tokenRingMLHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringmlhistoryindex','tokenringmlhistorysampleindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringmlhistoryindex', (YLeaf(YType.int32, 'tokenRingMLHistoryIndex'), ['int'])),
                    ('tokenringmlhistorysampleindex', (YLeaf(YType.int32, 'tokenRingMLHistorySampleIndex'), ['int'])),
                    ('tokenringmlhistoryintervalstart', (YLeaf(YType.uint32, 'tokenRingMLHistoryIntervalStart'), ['int'])),
                    ('tokenringmlhistorydropevents', (YLeaf(YType.uint32, 'tokenRingMLHistoryDropEvents'), ['int'])),
                    ('tokenringmlhistorymacoctets', (YLeaf(YType.uint32, 'tokenRingMLHistoryMacOctets'), ['int'])),
                    ('tokenringmlhistorymacpkts', (YLeaf(YType.uint32, 'tokenRingMLHistoryMacPkts'), ['int'])),
                    ('tokenringmlhistoryringpurgeevents', (YLeaf(YType.uint32, 'tokenRingMLHistoryRingPurgeEvents'), ['int'])),
                    ('tokenringmlhistoryringpurgepkts', (YLeaf(YType.uint32, 'tokenRingMLHistoryRingPurgePkts'), ['int'])),
                    ('tokenringmlhistorybeaconevents', (YLeaf(YType.uint32, 'tokenRingMLHistoryBeaconEvents'), ['int'])),
                    ('tokenringmlhistorybeacontime', (YLeaf(YType.int32, 'tokenRingMLHistoryBeaconTime'), ['int'])),
                    ('tokenringmlhistorybeaconpkts', (YLeaf(YType.uint32, 'tokenRingMLHistoryBeaconPkts'), ['int'])),
                    ('tokenringmlhistoryclaimtokenevents', (YLeaf(YType.uint32, 'tokenRingMLHistoryClaimTokenEvents'), ['int'])),
                    ('tokenringmlhistoryclaimtokenpkts', (YLeaf(YType.uint32, 'tokenRingMLHistoryClaimTokenPkts'), ['int'])),
                    ('tokenringmlhistorynaunchanges', (YLeaf(YType.uint32, 'tokenRingMLHistoryNAUNChanges'), ['int'])),
                    ('tokenringmlhistorylineerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryLineErrors'), ['int'])),
                    ('tokenringmlhistoryinternalerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryInternalErrors'), ['int'])),
                    ('tokenringmlhistorybursterrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryBurstErrors'), ['int'])),
                    ('tokenringmlhistoryacerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryACErrors'), ['int'])),
                    ('tokenringmlhistoryaborterrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryAbortErrors'), ['int'])),
                    ('tokenringmlhistorylostframeerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryLostFrameErrors'), ['int'])),
                    ('tokenringmlhistorycongestionerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryCongestionErrors'), ['int'])),
                    ('tokenringmlhistoryframecopiederrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryFrameCopiedErrors'), ['int'])),
                    ('tokenringmlhistoryfrequencyerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryFrequencyErrors'), ['int'])),
                    ('tokenringmlhistorytokenerrors', (YLeaf(YType.uint32, 'tokenRingMLHistoryTokenErrors'), ['int'])),
                    ('tokenringmlhistorysofterrorreports', (YLeaf(YType.uint32, 'tokenRingMLHistorySoftErrorReports'), ['int'])),
                    ('tokenringmlhistoryringpollevents', (YLeaf(YType.uint32, 'tokenRingMLHistoryRingPollEvents'), ['int'])),
                    ('tokenringmlhistoryactivestations', (YLeaf(YType.int32, 'tokenRingMLHistoryActiveStations'), ['int'])),
                ])
                self.tokenringmlhistoryindex = None
                self.tokenringmlhistorysampleindex = None
                self.tokenringmlhistoryintervalstart = None
                self.tokenringmlhistorydropevents = None
                self.tokenringmlhistorymacoctets = None
                self.tokenringmlhistorymacpkts = None
                self.tokenringmlhistoryringpurgeevents = None
                self.tokenringmlhistoryringpurgepkts = None
                self.tokenringmlhistorybeaconevents = None
                self.tokenringmlhistorybeacontime = None
                self.tokenringmlhistorybeaconpkts = None
                self.tokenringmlhistoryclaimtokenevents = None
                self.tokenringmlhistoryclaimtokenpkts = None
                self.tokenringmlhistorynaunchanges = None
                self.tokenringmlhistorylineerrors = None
                self.tokenringmlhistoryinternalerrors = None
                self.tokenringmlhistorybursterrors = None
                self.tokenringmlhistoryacerrors = None
                self.tokenringmlhistoryaborterrors = None
                self.tokenringmlhistorylostframeerrors = None
                self.tokenringmlhistorycongestionerrors = None
                self.tokenringmlhistoryframecopiederrors = None
                self.tokenringmlhistoryfrequencyerrors = None
                self.tokenringmlhistorytokenerrors = None
                self.tokenringmlhistorysofterrorreports = None
                self.tokenringmlhistoryringpollevents = None
                self.tokenringmlhistoryactivestations = None
                self._segment_path = lambda: "tokenRingMLHistoryEntry" + "[tokenRingMLHistoryIndex='" + str(self.tokenringmlhistoryindex) + "']" + "[tokenRingMLHistorySampleIndex='" + str(self.tokenringmlhistorysampleindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingMLHistoryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.TokenRingMLHistoryTable.TokenRingMLHistoryEntry, ['tokenringmlhistoryindex', 'tokenringmlhistorysampleindex', 'tokenringmlhistoryintervalstart', 'tokenringmlhistorydropevents', 'tokenringmlhistorymacoctets', 'tokenringmlhistorymacpkts', 'tokenringmlhistoryringpurgeevents', 'tokenringmlhistoryringpurgepkts', 'tokenringmlhistorybeaconevents', 'tokenringmlhistorybeacontime', 'tokenringmlhistorybeaconpkts', 'tokenringmlhistoryclaimtokenevents', 'tokenringmlhistoryclaimtokenpkts', 'tokenringmlhistorynaunchanges', 'tokenringmlhistorylineerrors', 'tokenringmlhistoryinternalerrors', 'tokenringmlhistorybursterrors', 'tokenringmlhistoryacerrors', 'tokenringmlhistoryaborterrors', 'tokenringmlhistorylostframeerrors', 'tokenringmlhistorycongestionerrors', 'tokenringmlhistoryframecopiederrors', 'tokenringmlhistoryfrequencyerrors', 'tokenringmlhistorytokenerrors', 'tokenringmlhistorysofterrorreports', 'tokenringmlhistoryringpollevents', 'tokenringmlhistoryactivestations'], name, value)




    class TokenRingPHistoryTable(Entity):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringphistoryentry
        
        	A collection of promiscuous statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`TokenRingPHistoryEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPHistoryTable.TokenRingPHistoryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.TokenRingPHistoryTable, self).__init__()

            self.yang_name = "tokenRingPHistoryTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tokenRingPHistoryEntry", ("tokenringphistoryentry", TOKENRINGRMONMIB.TokenRingPHistoryTable.TokenRingPHistoryEntry))])
            self._leafs = OrderedDict()

            self.tokenringphistoryentry = YList(self)
            self._segment_path = lambda: "tokenRingPHistoryTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.TokenRingPHistoryTable, [], name, value)


        class TokenRingPHistoryEntry(Entity):
            """
            A collection of promiscuous statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringphistoryindex  (key)
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: tokenringphistorysampleindex  (key)
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: tokenringphistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts
            
            	The total number of good non\-MAC frames received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatabroadcastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatamulticastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts18to63octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts64to127octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts128to255octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts256to511octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between      256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts512to1023octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: tokenringphistorydatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.TokenRingPHistoryTable.TokenRingPHistoryEntry, self).__init__()

                self.yang_name = "tokenRingPHistoryEntry"
                self.yang_parent_name = "tokenRingPHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringphistoryindex','tokenringphistorysampleindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringphistoryindex', (YLeaf(YType.int32, 'tokenRingPHistoryIndex'), ['int'])),
                    ('tokenringphistorysampleindex', (YLeaf(YType.int32, 'tokenRingPHistorySampleIndex'), ['int'])),
                    ('tokenringphistoryintervalstart', (YLeaf(YType.uint32, 'tokenRingPHistoryIntervalStart'), ['int'])),
                    ('tokenringphistorydropevents', (YLeaf(YType.uint32, 'tokenRingPHistoryDropEvents'), ['int'])),
                    ('tokenringphistorydataoctets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataOctets'), ['int'])),
                    ('tokenringphistorydatapkts', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts'), ['int'])),
                    ('tokenringphistorydatabroadcastpkts', (YLeaf(YType.uint32, 'tokenRingPHistoryDataBroadcastPkts'), ['int'])),
                    ('tokenringphistorydatamulticastpkts', (YLeaf(YType.uint32, 'tokenRingPHistoryDataMulticastPkts'), ['int'])),
                    ('tokenringphistorydatapkts18to63octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts18to63Octets'), ['int'])),
                    ('tokenringphistorydatapkts64to127octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts64to127Octets'), ['int'])),
                    ('tokenringphistorydatapkts128to255octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts128to255Octets'), ['int'])),
                    ('tokenringphistorydatapkts256to511octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts256to511Octets'), ['int'])),
                    ('tokenringphistorydatapkts512to1023octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts512to1023Octets'), ['int'])),
                    ('tokenringphistorydatapkts1024to2047octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts1024to2047Octets'), ['int'])),
                    ('tokenringphistorydatapkts2048to4095octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts2048to4095Octets'), ['int'])),
                    ('tokenringphistorydatapkts4096to8191octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts4096to8191Octets'), ['int'])),
                    ('tokenringphistorydatapkts8192to18000octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts8192to18000Octets'), ['int'])),
                    ('tokenringphistorydatapktsgreaterthan18000octets', (YLeaf(YType.uint32, 'tokenRingPHistoryDataPktsGreaterThan18000Octets'), ['int'])),
                ])
                self.tokenringphistoryindex = None
                self.tokenringphistorysampleindex = None
                self.tokenringphistoryintervalstart = None
                self.tokenringphistorydropevents = None
                self.tokenringphistorydataoctets = None
                self.tokenringphistorydatapkts = None
                self.tokenringphistorydatabroadcastpkts = None
                self.tokenringphistorydatamulticastpkts = None
                self.tokenringphistorydatapkts18to63octets = None
                self.tokenringphistorydatapkts64to127octets = None
                self.tokenringphistorydatapkts128to255octets = None
                self.tokenringphistorydatapkts256to511octets = None
                self.tokenringphistorydatapkts512to1023octets = None
                self.tokenringphistorydatapkts1024to2047octets = None
                self.tokenringphistorydatapkts2048to4095octets = None
                self.tokenringphistorydatapkts4096to8191octets = None
                self.tokenringphistorydatapkts8192to18000octets = None
                self.tokenringphistorydatapktsgreaterthan18000octets = None
                self._segment_path = lambda: "tokenRingPHistoryEntry" + "[tokenRingPHistoryIndex='" + str(self.tokenringphistoryindex) + "']" + "[tokenRingPHistorySampleIndex='" + str(self.tokenringphistorysampleindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingPHistoryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.TokenRingPHistoryTable.TokenRingPHistoryEntry, ['tokenringphistoryindex', 'tokenringphistorysampleindex', 'tokenringphistoryintervalstart', 'tokenringphistorydropevents', 'tokenringphistorydataoctets', 'tokenringphistorydatapkts', 'tokenringphistorydatabroadcastpkts', 'tokenringphistorydatamulticastpkts', 'tokenringphistorydatapkts18to63octets', 'tokenringphistorydatapkts64to127octets', 'tokenringphistorydatapkts128to255octets', 'tokenringphistorydatapkts256to511octets', 'tokenringphistorydatapkts512to1023octets', 'tokenringphistorydatapkts1024to2047octets', 'tokenringphistorydatapkts2048to4095octets', 'tokenringphistorydatapkts4096to8191octets', 'tokenringphistorydatapkts8192to18000octets', 'tokenringphistorydatapktsgreaterthan18000octets'], name, value)




    class RingStationControlTable(Entity):
        """
        A list of ringStation table control entries.
        
        .. attribute:: ringstationcontrolentry
        
        	A list of parameters that set up the discovery of stations on a particular interface and the collection of statistics about these stations
        	**type**\: list of  		 :py:class:`RingStationControlEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.RingStationControlTable, self).__init__()

            self.yang_name = "ringStationControlTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ringStationControlEntry", ("ringstationcontrolentry", TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry))])
            self._leafs = OrderedDict()

            self.ringstationcontrolentry = YList(self)
            self._segment_path = lambda: "ringStationControlTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.RingStationControlTable, [], name, value)


        class RingStationControlEntry(Entity):
            """
            A list of parameters that set up the discovery of
            stations on a particular interface and the
            collection of statistics about these stations.
            
            .. attribute:: ringstationcontrolifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device from which ringStation data is collected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\- II [3]
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: ringstationcontroltablesize
            
            	The number of ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolactivestations
            
            	The number of active ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolringstate
            
            	The current status of this ring
            	**type**\:  :py:class:`RingStationControlRingState <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry.RingStationControlRingState>`
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolbeaconsender
            
            	The address of the sender of the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolbeaconnaun
            
            	The address of the NAUN in the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolactivemonitor
            
            	The address of the Active Monitor on this segment.  If this address is unknown, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolorderchanges
            
            	The number of add and delete events in the ringStationOrderTable optionally associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolstatus
            
            	The status of this ringStationControl entry.  If this object is not equal to valid(1), all associated entries in the ringStationTable shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: ringstationcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry, self).__init__()

                self.yang_name = "ringStationControlEntry"
                self.yang_parent_name = "ringStationControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationcontrolifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationcontrolifindex', (YLeaf(YType.int32, 'ringStationControlIfIndex'), ['int'])),
                    ('ringstationcontroltablesize', (YLeaf(YType.int32, 'ringStationControlTableSize'), ['int'])),
                    ('ringstationcontrolactivestations', (YLeaf(YType.int32, 'ringStationControlActiveStations'), ['int'])),
                    ('ringstationcontrolringstate', (YLeaf(YType.enumeration, 'ringStationControlRingState'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TOKENRINGRMONMIB', 'RingStationControlTable.RingStationControlEntry.RingStationControlRingState')])),
                    ('ringstationcontrolbeaconsender', (YLeaf(YType.str, 'ringStationControlBeaconSender'), ['str'])),
                    ('ringstationcontrolbeaconnaun', (YLeaf(YType.str, 'ringStationControlBeaconNAUN'), ['str'])),
                    ('ringstationcontrolactivemonitor', (YLeaf(YType.str, 'ringStationControlActiveMonitor'), ['str'])),
                    ('ringstationcontrolorderchanges', (YLeaf(YType.uint32, 'ringStationControlOrderChanges'), ['int'])),
                    ('ringstationcontrolowner', (YLeaf(YType.str, 'ringStationControlOwner'), ['str'])),
                    ('ringstationcontrolstatus', (YLeaf(YType.enumeration, 'ringStationControlStatus'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntryStatus', '')])),
                    ('ringstationcontroldroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:ringStationControlDroppedFrames'), ['int'])),
                    ('ringstationcontrolcreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:ringStationControlCreateTime'), ['int'])),
                ])
                self.ringstationcontrolifindex = None
                self.ringstationcontroltablesize = None
                self.ringstationcontrolactivestations = None
                self.ringstationcontrolringstate = None
                self.ringstationcontrolbeaconsender = None
                self.ringstationcontrolbeaconnaun = None
                self.ringstationcontrolactivemonitor = None
                self.ringstationcontrolorderchanges = None
                self.ringstationcontrolowner = None
                self.ringstationcontrolstatus = None
                self.ringstationcontroldroppedframes = None
                self.ringstationcontrolcreatetime = None
                self._segment_path = lambda: "ringStationControlEntry" + "[ringStationControlIfIndex='" + str(self.ringstationcontrolifindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry, ['ringstationcontrolifindex', 'ringstationcontroltablesize', 'ringstationcontrolactivestations', 'ringstationcontrolringstate', 'ringstationcontrolbeaconsender', 'ringstationcontrolbeaconnaun', 'ringstationcontrolactivemonitor', 'ringstationcontrolorderchanges', 'ringstationcontrolowner', 'ringstationcontrolstatus', 'ringstationcontroldroppedframes', 'ringstationcontrolcreatetime'], name, value)

            class RingStationControlRingState(Enum):
                """
                RingStationControlRingState (Enum Class)

                The current status of this ring.

                .. data:: normalOperation = 1

                .. data:: ringPurgeState = 2

                .. data:: claimTokenState = 3

                .. data:: beaconFrameStreamingState = 4

                .. data:: beaconBitStreamingState = 5

                .. data:: beaconRingSignalLossState = 6

                .. data:: beaconSetRecoveryModeState = 7

                """

                normalOperation = Enum.YLeaf(1, "normalOperation")

                ringPurgeState = Enum.YLeaf(2, "ringPurgeState")

                claimTokenState = Enum.YLeaf(3, "claimTokenState")

                beaconFrameStreamingState = Enum.YLeaf(4, "beaconFrameStreamingState")

                beaconBitStreamingState = Enum.YLeaf(5, "beaconBitStreamingState")

                beaconRingSignalLossState = Enum.YLeaf(6, "beaconRingSignalLossState")

                beaconSetRecoveryModeState = Enum.YLeaf(7, "beaconSetRecoveryModeState")





    class RingStationTable(Entity):
        """
        A list of ring station entries.  An entry will
        exist for each station that is now or has
        
        
        
        
        
        previously been detected as physically present on
        this ring.
        
        .. attribute:: ringstationentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this device
        	**type**\: list of  		 :py:class:`RingStationEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationTable.RingStationEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.RingStationTable, self).__init__()

            self.yang_name = "ringStationTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ringStationEntry", ("ringstationentry", TOKENRINGRMONMIB.RingStationTable.RingStationEntry))])
            self._leafs = OrderedDict()

            self.ringstationentry = YList(self)
            self._segment_path = lambda: "ringStationTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.RingStationTable, [], name, value)


        class RingStationEntry(Entity):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this device.
            
            .. attribute:: ringstationifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationmacaddress  (key)
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationlastnaun
            
            	The physical address of last known NAUN of this station
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationstationstatus
            
            	The status of this station on the ring
            	**type**\:  :py:class:`RingStationStationStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationTable.RingStationEntry.RingStationStationStatus>`
            
            	**config**\: False
            
            .. attribute:: ringstationlastentertime
            
            	The value of sysUpTime at the time this station last entered the ring.  If the time is unknown, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationlastexittime
            
            	The value of sysUpTime at the time the probe detected that this station last exited the ring. If the time is unknown, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationduplicateaddresses
            
            	The number of times this station experienced a duplicate address error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationinlineerrors
            
            	The total number of line errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationoutlineerrors
            
            	The total number of line errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationinternalerrors
            
            	The total number of adapter internal errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationinbursterrors
            
            	The total number of burst errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationoutbursterrors
            
            	The total number of burst errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationaborterrors
            
            	The total number of abort delimiters reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationlostframeerrors
            
            	The total number of lost frame errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationcongestionerrors
            
            	The total number of receive congestion errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationframecopiederrors
            
            	The total number of frame copied errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationfrequencyerrors
            
            	The total number of frequency errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationtokenerrors
            
            	The total number of token errors reported by this station in error reporting frames detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationinbeaconerrors
            
            	The total number of beacon frames sent by this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationoutbeaconerrors
            
            	The total number of beacon frames detected by the probe that name this station as the NAUN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationinsertions
            
            	The number of times the probe detected this station inserting onto the ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.RingStationTable.RingStationEntry, self).__init__()

                self.yang_name = "ringStationEntry"
                self.yang_parent_name = "ringStationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationifindex','ringstationmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationifindex', (YLeaf(YType.int32, 'ringStationIfIndex'), ['int'])),
                    ('ringstationmacaddress', (YLeaf(YType.str, 'ringStationMacAddress'), ['str'])),
                    ('ringstationlastnaun', (YLeaf(YType.str, 'ringStationLastNAUN'), ['str'])),
                    ('ringstationstationstatus', (YLeaf(YType.enumeration, 'ringStationStationStatus'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TOKENRINGRMONMIB', 'RingStationTable.RingStationEntry.RingStationStationStatus')])),
                    ('ringstationlastentertime', (YLeaf(YType.uint32, 'ringStationLastEnterTime'), ['int'])),
                    ('ringstationlastexittime', (YLeaf(YType.uint32, 'ringStationLastExitTime'), ['int'])),
                    ('ringstationduplicateaddresses', (YLeaf(YType.uint32, 'ringStationDuplicateAddresses'), ['int'])),
                    ('ringstationinlineerrors', (YLeaf(YType.uint32, 'ringStationInLineErrors'), ['int'])),
                    ('ringstationoutlineerrors', (YLeaf(YType.uint32, 'ringStationOutLineErrors'), ['int'])),
                    ('ringstationinternalerrors', (YLeaf(YType.uint32, 'ringStationInternalErrors'), ['int'])),
                    ('ringstationinbursterrors', (YLeaf(YType.uint32, 'ringStationInBurstErrors'), ['int'])),
                    ('ringstationoutbursterrors', (YLeaf(YType.uint32, 'ringStationOutBurstErrors'), ['int'])),
                    ('ringstationacerrors', (YLeaf(YType.uint32, 'ringStationACErrors'), ['int'])),
                    ('ringstationaborterrors', (YLeaf(YType.uint32, 'ringStationAbortErrors'), ['int'])),
                    ('ringstationlostframeerrors', (YLeaf(YType.uint32, 'ringStationLostFrameErrors'), ['int'])),
                    ('ringstationcongestionerrors', (YLeaf(YType.uint32, 'ringStationCongestionErrors'), ['int'])),
                    ('ringstationframecopiederrors', (YLeaf(YType.uint32, 'ringStationFrameCopiedErrors'), ['int'])),
                    ('ringstationfrequencyerrors', (YLeaf(YType.uint32, 'ringStationFrequencyErrors'), ['int'])),
                    ('ringstationtokenerrors', (YLeaf(YType.uint32, 'ringStationTokenErrors'), ['int'])),
                    ('ringstationinbeaconerrors', (YLeaf(YType.uint32, 'ringStationInBeaconErrors'), ['int'])),
                    ('ringstationoutbeaconerrors', (YLeaf(YType.uint32, 'ringStationOutBeaconErrors'), ['int'])),
                    ('ringstationinsertions', (YLeaf(YType.uint32, 'ringStationInsertions'), ['int'])),
                ])
                self.ringstationifindex = None
                self.ringstationmacaddress = None
                self.ringstationlastnaun = None
                self.ringstationstationstatus = None
                self.ringstationlastentertime = None
                self.ringstationlastexittime = None
                self.ringstationduplicateaddresses = None
                self.ringstationinlineerrors = None
                self.ringstationoutlineerrors = None
                self.ringstationinternalerrors = None
                self.ringstationinbursterrors = None
                self.ringstationoutbursterrors = None
                self.ringstationacerrors = None
                self.ringstationaborterrors = None
                self.ringstationlostframeerrors = None
                self.ringstationcongestionerrors = None
                self.ringstationframecopiederrors = None
                self.ringstationfrequencyerrors = None
                self.ringstationtokenerrors = None
                self.ringstationinbeaconerrors = None
                self.ringstationoutbeaconerrors = None
                self.ringstationinsertions = None
                self._segment_path = lambda: "ringStationEntry" + "[ringStationIfIndex='" + str(self.ringstationifindex) + "']" + "[ringStationMacAddress='" + str(self.ringstationmacaddress) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.RingStationTable.RingStationEntry, ['ringstationifindex', 'ringstationmacaddress', 'ringstationlastnaun', 'ringstationstationstatus', 'ringstationlastentertime', 'ringstationlastexittime', 'ringstationduplicateaddresses', 'ringstationinlineerrors', 'ringstationoutlineerrors', 'ringstationinternalerrors', 'ringstationinbursterrors', 'ringstationoutbursterrors', 'ringstationacerrors', 'ringstationaborterrors', 'ringstationlostframeerrors', 'ringstationcongestionerrors', 'ringstationframecopiederrors', 'ringstationfrequencyerrors', 'ringstationtokenerrors', 'ringstationinbeaconerrors', 'ringstationoutbeaconerrors', 'ringstationinsertions'], name, value)

            class RingStationStationStatus(Enum):
                """
                RingStationStationStatus (Enum Class)

                The status of this station on the ring.

                .. data:: active = 1

                .. data:: inactive = 2

                .. data:: forcedRemoval = 3

                """

                active = Enum.YLeaf(1, "active")

                inactive = Enum.YLeaf(2, "inactive")

                forcedRemoval = Enum.YLeaf(3, "forcedRemoval")





    class RingStationOrderTable(Entity):
        """
        A list of ring station entries for stations in
        the ring poll, ordered by their ring\-order.
        
        .. attribute:: ringstationorderentry
        
        	A collection of statistics for a particular      station that is active on a ring monitored by this device.  This table will contain information for every interface that has a ringStationControlStatus equal to valid
        	**type**\: list of  		 :py:class:`RingStationOrderEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationOrderTable.RingStationOrderEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.RingStationOrderTable, self).__init__()

            self.yang_name = "ringStationOrderTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ringStationOrderEntry", ("ringstationorderentry", TOKENRINGRMONMIB.RingStationOrderTable.RingStationOrderEntry))])
            self._leafs = OrderedDict()

            self.ringstationorderentry = YList(self)
            self._segment_path = lambda: "ringStationOrderTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.RingStationOrderTable, [], name, value)


        class RingStationOrderEntry(Entity):
            """
            A collection of statistics for a particular
            
            
            
            
            
            station that is active on a ring monitored by this
            device.  This table will contain information for
            every interface that has a
            ringStationControlStatus equal to valid.
            
            .. attribute:: ringstationorderifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationorderorderindex  (key)
            
            	This index denotes the location of this station with respect to other stations on the ring.  This index is one more than the number of hops downstream that this station is from the rmon probe.  The rmon probe itself gets the value one
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationordermacaddress
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.RingStationOrderTable.RingStationOrderEntry, self).__init__()

                self.yang_name = "ringStationOrderEntry"
                self.yang_parent_name = "ringStationOrderTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationorderifindex','ringstationorderorderindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationorderifindex', (YLeaf(YType.int32, 'ringStationOrderIfIndex'), ['int'])),
                    ('ringstationorderorderindex', (YLeaf(YType.int32, 'ringStationOrderOrderIndex'), ['int'])),
                    ('ringstationordermacaddress', (YLeaf(YType.str, 'ringStationOrderMacAddress'), ['str'])),
                ])
                self.ringstationorderifindex = None
                self.ringstationorderorderindex = None
                self.ringstationordermacaddress = None
                self._segment_path = lambda: "ringStationOrderEntry" + "[ringStationOrderIfIndex='" + str(self.ringstationorderifindex) + "']" + "[ringStationOrderOrderIndex='" + str(self.ringstationorderorderindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationOrderTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.RingStationOrderTable.RingStationOrderEntry, ['ringstationorderifindex', 'ringstationorderorderindex', 'ringstationordermacaddress'], name, value)




    class RingStationConfigControlTable(Entity):
        """
        A list of ring station configuration control
        entries.
        
        .. attribute:: ringstationconfigcontrolentry
        
        	This entry controls active management of stations by the probe.  One entry exists in this table for each active station in the ringStationTable
        	**type**\: list of  		 :py:class:`RingStationConfigControlEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.RingStationConfigControlTable, self).__init__()

            self.yang_name = "ringStationConfigControlTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ringStationConfigControlEntry", ("ringstationconfigcontrolentry", TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry))])
            self._leafs = OrderedDict()

            self.ringstationconfigcontrolentry = YList(self)
            self._segment_path = lambda: "ringStationConfigControlTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.RingStationConfigControlTable, [], name, value)


        class RingStationConfigControlEntry(Entity):
            """
            This entry controls active management of stations
            by the probe.  One entry exists in this table for
            each active station in the ringStationTable.
            
            .. attribute:: ringstationconfigcontrolifindex  (key)
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationconfigcontrolmacaddress  (key)
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationconfigcontrolremove
            
            	Setting this object to `removing(2)' causes a Remove Station MAC frame to be sent.  The agent will set this object to `stable(1)' after processing the request
            	**type**\:  :py:class:`RingStationConfigControlRemove <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlRemove>`
            
            	**config**\: False
            
            .. attribute:: ringstationconfigcontrolupdatestats
            
            	Setting this object to `updating(2)' causes the configuration information associate with this entry to be updated.  The agent will set this object to `stable(1)' after processing the request
            	**type**\:  :py:class:`RingStationConfigControlUpdateStats <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlUpdateStats>`
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry, self).__init__()

                self.yang_name = "ringStationConfigControlEntry"
                self.yang_parent_name = "ringStationConfigControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationconfigcontrolifindex','ringstationconfigcontrolmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationconfigcontrolifindex', (YLeaf(YType.int32, 'ringStationConfigControlIfIndex'), ['int'])),
                    ('ringstationconfigcontrolmacaddress', (YLeaf(YType.str, 'ringStationConfigControlMacAddress'), ['str'])),
                    ('ringstationconfigcontrolremove', (YLeaf(YType.enumeration, 'ringStationConfigControlRemove'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TOKENRINGRMONMIB', 'RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlRemove')])),
                    ('ringstationconfigcontrolupdatestats', (YLeaf(YType.enumeration, 'ringStationConfigControlUpdateStats'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'TOKENRINGRMONMIB', 'RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlUpdateStats')])),
                ])
                self.ringstationconfigcontrolifindex = None
                self.ringstationconfigcontrolmacaddress = None
                self.ringstationconfigcontrolremove = None
                self.ringstationconfigcontrolupdatestats = None
                self._segment_path = lambda: "ringStationConfigControlEntry" + "[ringStationConfigControlIfIndex='" + str(self.ringstationconfigcontrolifindex) + "']" + "[ringStationConfigControlMacAddress='" + str(self.ringstationconfigcontrolmacaddress) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationConfigControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry, ['ringstationconfigcontrolifindex', 'ringstationconfigcontrolmacaddress', 'ringstationconfigcontrolremove', 'ringstationconfigcontrolupdatestats'], name, value)

            class RingStationConfigControlRemove(Enum):
                """
                RingStationConfigControlRemove (Enum Class)

                Setting this object to `removing(2)' causes a

                Remove Station MAC frame to be sent.  The agent

                will set this object to `stable(1)' after

                processing the request.

                .. data:: stable = 1

                .. data:: removing = 2

                """

                stable = Enum.YLeaf(1, "stable")

                removing = Enum.YLeaf(2, "removing")


            class RingStationConfigControlUpdateStats(Enum):
                """
                RingStationConfigControlUpdateStats (Enum Class)

                Setting this object to `updating(2)' causes the

                configuration information associate with this

                entry to be updated.  The agent will set this

                object to `stable(1)' after processing the

                request.

                .. data:: stable = 1

                .. data:: updating = 2

                """

                stable = Enum.YLeaf(1, "stable")

                updating = Enum.YLeaf(2, "updating")





    class RingStationConfigTable(Entity):
        """
        A list of configuration entries for stations on a
        ring monitored by this probe.
        
        .. attribute:: ringstationconfigentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this probe
        	**type**\: list of  		 :py:class:`RingStationConfigEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigTable.RingStationConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.RingStationConfigTable, self).__init__()

            self.yang_name = "ringStationConfigTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ringStationConfigEntry", ("ringstationconfigentry", TOKENRINGRMONMIB.RingStationConfigTable.RingStationConfigEntry))])
            self._leafs = OrderedDict()

            self.ringstationconfigentry = YList(self)
            self._segment_path = lambda: "ringStationConfigTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.RingStationConfigTable, [], name, value)


        class RingStationConfigEntry(Entity):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this probe.
            
            .. attribute:: ringstationconfigifindex  (key)
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: ringstationconfigmacaddress  (key)
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6..6
            
            	**config**\: False
            
            .. attribute:: ringstationconfigupdatetime
            
            	The value of sysUpTime at the time this configuration information was last updated (completely)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ringstationconfiglocation
            
            	The assigned physical location of this station
            	**type**\: str
            
            	**length:** 4..4
            
            	**config**\: False
            
            .. attribute:: ringstationconfigmicrocode
            
            	The microcode EC level of this station
            	**type**\: str
            
            	**length:** 10..10
            
            	**config**\: False
            
            .. attribute:: ringstationconfiggroupaddress
            
            	The low\-order 4 octets of the group address recognized by this station
            	**type**\: str
            
            	**length:** 4..4
            
            	**config**\: False
            
            .. attribute:: ringstationconfigfunctionaladdress
            
            	the functional addresses recognized by this station
            	**type**\: str
            
            	**length:** 4..4
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.RingStationConfigTable.RingStationConfigEntry, self).__init__()

                self.yang_name = "ringStationConfigEntry"
                self.yang_parent_name = "ringStationConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationconfigifindex','ringstationconfigmacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationconfigifindex', (YLeaf(YType.int32, 'ringStationConfigIfIndex'), ['int'])),
                    ('ringstationconfigmacaddress', (YLeaf(YType.str, 'ringStationConfigMacAddress'), ['str'])),
                    ('ringstationconfigupdatetime', (YLeaf(YType.uint32, 'ringStationConfigUpdateTime'), ['int'])),
                    ('ringstationconfiglocation', (YLeaf(YType.str, 'ringStationConfigLocation'), ['str'])),
                    ('ringstationconfigmicrocode', (YLeaf(YType.str, 'ringStationConfigMicrocode'), ['str'])),
                    ('ringstationconfiggroupaddress', (YLeaf(YType.str, 'ringStationConfigGroupAddress'), ['str'])),
                    ('ringstationconfigfunctionaladdress', (YLeaf(YType.str, 'ringStationConfigFunctionalAddress'), ['str'])),
                ])
                self.ringstationconfigifindex = None
                self.ringstationconfigmacaddress = None
                self.ringstationconfigupdatetime = None
                self.ringstationconfiglocation = None
                self.ringstationconfigmicrocode = None
                self.ringstationconfiggroupaddress = None
                self.ringstationconfigfunctionaladdress = None
                self._segment_path = lambda: "ringStationConfigEntry" + "[ringStationConfigIfIndex='" + str(self.ringstationconfigifindex) + "']" + "[ringStationConfigMacAddress='" + str(self.ringstationconfigmacaddress) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.RingStationConfigTable.RingStationConfigEntry, ['ringstationconfigifindex', 'ringstationconfigmacaddress', 'ringstationconfigupdatetime', 'ringstationconfiglocation', 'ringstationconfigmicrocode', 'ringstationconfiggroupaddress', 'ringstationconfigfunctionaladdress'], name, value)




    class SourceRoutingStatsTable(Entity):
        """
        A list of source routing statistics entries.
        
        .. attribute:: sourceroutingstatsentry
        
        	A collection of source routing statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`SourceRoutingStatsEntry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.SourceRoutingStatsTable.SourceRoutingStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.SourceRoutingStatsTable, self).__init__()

            self.yang_name = "sourceRoutingStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sourceRoutingStatsEntry", ("sourceroutingstatsentry", TOKENRINGRMONMIB.SourceRoutingStatsTable.SourceRoutingStatsEntry))])
            self._leafs = OrderedDict()

            self.sourceroutingstatsentry = YList(self)
            self._segment_path = lambda: "sourceRoutingStatsTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.SourceRoutingStatsTable, [], name, value)


        class SourceRoutingStatsEntry(Entity):
            """
            A collection of source routing statistics kept
            for a particular Token Ring interface.
            
            .. attribute:: sourceroutingstatsifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which source routing statistics will be detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsringnumber
            
            	The ring number of the ring monitored by this entry.  When any object in this entry is created, the probe will attempt to discover the ring number.  Only after the ring number is discovered will this object be created.  After creating an object in this entry, the management station should poll this object to detect when it is created.  Only after this object is created can the management station set the sourceRoutingStatsStatus entry to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsinframes
            
            	The count of frames sent into this ring from another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsoutframes
            
            	The count of frames sent from this ring to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsthroughframes
            
            	The count of frames sent from another ring, through this ring, to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsallroutesbroadcastframes
            
            	The total number of good frames received that were All Routes Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatssingleroutebroadcastframes
            
            	The total number of good frames received that were Single Route Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsinoctets
            
            	The count of octets in good frames sent into this ring from another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsoutoctets
            
            	The count of octets in good frames sent from this ring to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsthroughoctets
            
            	The count of octets in good frames sent another ring, through this ring, to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsallroutesbroadcastoctets
            
            	The total number of octets in good frames received that were All Routes Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatssingleroutesbroadcastoctets
            
            	The total number of octets in good frames received that were Single Route Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatslocalllcframes
            
            	The total number of frames received who had no RIF field (or had a RIF field that only included the local ring's number) and were not All Route Broadcast Frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats1hopframes
            
            	The total number of frames received whose route had 1 hop, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats2hopsframes
            
            	The total number of frames received whose route had 2 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats3hopsframes
            
            	The total number of frames received whose route had 3 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats4hopsframes
            
            	The total number of frames received whose route had 4 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats5hopsframes
            
            	The total number of frames received whose route had 5 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats6hopsframes
            
            	The total number of frames received whose route had 6 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats7hopsframes
            
            	The total number of frames received whose route had 7 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstats8hopsframes
            
            	The total number of frames received whose route had 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsmorethan8hopsframes
            
            	The total number of frames received whose route had more than 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsstatus
            
            	The status of this sourceRoutingStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sourceroutingstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.SourceRoutingStatsTable.SourceRoutingStatsEntry, self).__init__()

                self.yang_name = "sourceRoutingStatsEntry"
                self.yang_parent_name = "sourceRoutingStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sourceroutingstatsifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sourceroutingstatsifindex', (YLeaf(YType.int32, 'sourceRoutingStatsIfIndex'), ['int'])),
                    ('sourceroutingstatsringnumber', (YLeaf(YType.int32, 'sourceRoutingStatsRingNumber'), ['int'])),
                    ('sourceroutingstatsinframes', (YLeaf(YType.uint32, 'sourceRoutingStatsInFrames'), ['int'])),
                    ('sourceroutingstatsoutframes', (YLeaf(YType.uint32, 'sourceRoutingStatsOutFrames'), ['int'])),
                    ('sourceroutingstatsthroughframes', (YLeaf(YType.uint32, 'sourceRoutingStatsThroughFrames'), ['int'])),
                    ('sourceroutingstatsallroutesbroadcastframes', (YLeaf(YType.uint32, 'sourceRoutingStatsAllRoutesBroadcastFrames'), ['int'])),
                    ('sourceroutingstatssingleroutebroadcastframes', (YLeaf(YType.uint32, 'sourceRoutingStatsSingleRouteBroadcastFrames'), ['int'])),
                    ('sourceroutingstatsinoctets', (YLeaf(YType.uint32, 'sourceRoutingStatsInOctets'), ['int'])),
                    ('sourceroutingstatsoutoctets', (YLeaf(YType.uint32, 'sourceRoutingStatsOutOctets'), ['int'])),
                    ('sourceroutingstatsthroughoctets', (YLeaf(YType.uint32, 'sourceRoutingStatsThroughOctets'), ['int'])),
                    ('sourceroutingstatsallroutesbroadcastoctets', (YLeaf(YType.uint32, 'sourceRoutingStatsAllRoutesBroadcastOctets'), ['int'])),
                    ('sourceroutingstatssingleroutesbroadcastoctets', (YLeaf(YType.uint32, 'sourceRoutingStatsSingleRoutesBroadcastOctets'), ['int'])),
                    ('sourceroutingstatslocalllcframes', (YLeaf(YType.uint32, 'sourceRoutingStatsLocalLLCFrames'), ['int'])),
                    ('sourceroutingstats1hopframes', (YLeaf(YType.uint32, 'sourceRoutingStats1HopFrames'), ['int'])),
                    ('sourceroutingstats2hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats2HopsFrames'), ['int'])),
                    ('sourceroutingstats3hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats3HopsFrames'), ['int'])),
                    ('sourceroutingstats4hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats4HopsFrames'), ['int'])),
                    ('sourceroutingstats5hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats5HopsFrames'), ['int'])),
                    ('sourceroutingstats6hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats6HopsFrames'), ['int'])),
                    ('sourceroutingstats7hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats7HopsFrames'), ['int'])),
                    ('sourceroutingstats8hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStats8HopsFrames'), ['int'])),
                    ('sourceroutingstatsmorethan8hopsframes', (YLeaf(YType.uint32, 'sourceRoutingStatsMoreThan8HopsFrames'), ['int'])),
                    ('sourceroutingstatsowner', (YLeaf(YType.str, 'sourceRoutingStatsOwner'), ['str'])),
                    ('sourceroutingstatsstatus', (YLeaf(YType.enumeration, 'sourceRoutingStatsStatus'), [('ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB', 'EntryStatus', '')])),
                    ('sourceroutingstatsdroppedframes', (YLeaf(YType.uint32, 'RMON2-MIB:sourceRoutingStatsDroppedFrames'), ['int'])),
                    ('sourceroutingstatscreatetime', (YLeaf(YType.uint32, 'RMON2-MIB:sourceRoutingStatsCreateTime'), ['int'])),
                ])
                self.sourceroutingstatsifindex = None
                self.sourceroutingstatsringnumber = None
                self.sourceroutingstatsinframes = None
                self.sourceroutingstatsoutframes = None
                self.sourceroutingstatsthroughframes = None
                self.sourceroutingstatsallroutesbroadcastframes = None
                self.sourceroutingstatssingleroutebroadcastframes = None
                self.sourceroutingstatsinoctets = None
                self.sourceroutingstatsoutoctets = None
                self.sourceroutingstatsthroughoctets = None
                self.sourceroutingstatsallroutesbroadcastoctets = None
                self.sourceroutingstatssingleroutesbroadcastoctets = None
                self.sourceroutingstatslocalllcframes = None
                self.sourceroutingstats1hopframes = None
                self.sourceroutingstats2hopsframes = None
                self.sourceroutingstats3hopsframes = None
                self.sourceroutingstats4hopsframes = None
                self.sourceroutingstats5hopsframes = None
                self.sourceroutingstats6hopsframes = None
                self.sourceroutingstats7hopsframes = None
                self.sourceroutingstats8hopsframes = None
                self.sourceroutingstatsmorethan8hopsframes = None
                self.sourceroutingstatsowner = None
                self.sourceroutingstatsstatus = None
                self.sourceroutingstatsdroppedframes = None
                self.sourceroutingstatscreatetime = None
                self._segment_path = lambda: "sourceRoutingStatsEntry" + "[sourceRoutingStatsIfIndex='" + str(self.sourceroutingstatsifindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/sourceRoutingStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.SourceRoutingStatsTable.SourceRoutingStatsEntry, ['sourceroutingstatsifindex', 'sourceroutingstatsringnumber', 'sourceroutingstatsinframes', 'sourceroutingstatsoutframes', 'sourceroutingstatsthroughframes', 'sourceroutingstatsallroutesbroadcastframes', 'sourceroutingstatssingleroutebroadcastframes', 'sourceroutingstatsinoctets', 'sourceroutingstatsoutoctets', 'sourceroutingstatsthroughoctets', 'sourceroutingstatsallroutesbroadcastoctets', 'sourceroutingstatssingleroutesbroadcastoctets', 'sourceroutingstatslocalllcframes', 'sourceroutingstats1hopframes', 'sourceroutingstats2hopsframes', 'sourceroutingstats3hopsframes', 'sourceroutingstats4hopsframes', 'sourceroutingstats5hopsframes', 'sourceroutingstats6hopsframes', 'sourceroutingstats7hopsframes', 'sourceroutingstats8hopsframes', 'sourceroutingstatsmorethan8hopsframes', 'sourceroutingstatsowner', 'sourceroutingstatsstatus', 'sourceroutingstatsdroppedframes', 'sourceroutingstatscreatetime'], name, value)



    def clone_ptr(self):
        self._top_entity = TOKENRINGRMONMIB()
        return self._top_entity



