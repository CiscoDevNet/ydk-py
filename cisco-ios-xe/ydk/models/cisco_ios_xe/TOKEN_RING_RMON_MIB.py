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
    	**type**\:  :py:class:`Tokenringmlstatstable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringmlstatstable>`
    
    .. attribute:: tokenringpstatstable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\:  :py:class:`Tokenringpstatstable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringpstatstable>`
    
    .. attribute:: tokenringmlhistorytable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\:  :py:class:`Tokenringmlhistorytable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringmlhistorytable>`
    
    .. attribute:: tokenringphistorytable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\:  :py:class:`Tokenringphistorytable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringphistorytable>`
    
    .. attribute:: ringstationcontroltable
    
    	A list of ringStation table control entries
    	**type**\:  :py:class:`Ringstationcontroltable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationcontroltable>`
    
    .. attribute:: ringstationtable
    
    	A list of ring station entries.  An entry will exist for each station that is now or has      previously been detected as physically present on this ring
    	**type**\:  :py:class:`Ringstationtable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationtable>`
    
    .. attribute:: ringstationordertable
    
    	A list of ring station entries for stations in the ring poll, ordered by their ring\-order
    	**type**\:  :py:class:`Ringstationordertable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationordertable>`
    
    .. attribute:: ringstationconfigcontroltable
    
    	A list of ring station configuration control entries
    	**type**\:  :py:class:`Ringstationconfigcontroltable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationconfigcontroltable>`
    
    .. attribute:: ringstationconfigtable
    
    	A list of configuration entries for stations on a ring monitored by this probe
    	**type**\:  :py:class:`Ringstationconfigtable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationconfigtable>`
    
    .. attribute:: sourceroutingstatstable
    
    	A list of source routing statistics entries
    	**type**\:  :py:class:`Sourceroutingstatstable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Sourceroutingstatstable>`
    
    

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
        self._child_container_classes = OrderedDict([("tokenRingMLStatsTable", ("tokenringmlstatstable", TOKENRINGRMONMIB.Tokenringmlstatstable)), ("tokenRingPStatsTable", ("tokenringpstatstable", TOKENRINGRMONMIB.Tokenringpstatstable)), ("tokenRingMLHistoryTable", ("tokenringmlhistorytable", TOKENRINGRMONMIB.Tokenringmlhistorytable)), ("tokenRingPHistoryTable", ("tokenringphistorytable", TOKENRINGRMONMIB.Tokenringphistorytable)), ("ringStationControlTable", ("ringstationcontroltable", TOKENRINGRMONMIB.Ringstationcontroltable)), ("ringStationTable", ("ringstationtable", TOKENRINGRMONMIB.Ringstationtable)), ("ringStationOrderTable", ("ringstationordertable", TOKENRINGRMONMIB.Ringstationordertable)), ("ringStationConfigControlTable", ("ringstationconfigcontroltable", TOKENRINGRMONMIB.Ringstationconfigcontroltable)), ("ringStationConfigTable", ("ringstationconfigtable", TOKENRINGRMONMIB.Ringstationconfigtable)), ("sourceRoutingStatsTable", ("sourceroutingstatstable", TOKENRINGRMONMIB.Sourceroutingstatstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.tokenringmlstatstable = TOKENRINGRMONMIB.Tokenringmlstatstable()
        self.tokenringmlstatstable.parent = self
        self._children_name_map["tokenringmlstatstable"] = "tokenRingMLStatsTable"
        self._children_yang_names.add("tokenRingMLStatsTable")

        self.tokenringpstatstable = TOKENRINGRMONMIB.Tokenringpstatstable()
        self.tokenringpstatstable.parent = self
        self._children_name_map["tokenringpstatstable"] = "tokenRingPStatsTable"
        self._children_yang_names.add("tokenRingPStatsTable")

        self.tokenringmlhistorytable = TOKENRINGRMONMIB.Tokenringmlhistorytable()
        self.tokenringmlhistorytable.parent = self
        self._children_name_map["tokenringmlhistorytable"] = "tokenRingMLHistoryTable"
        self._children_yang_names.add("tokenRingMLHistoryTable")

        self.tokenringphistorytable = TOKENRINGRMONMIB.Tokenringphistorytable()
        self.tokenringphistorytable.parent = self
        self._children_name_map["tokenringphistorytable"] = "tokenRingPHistoryTable"
        self._children_yang_names.add("tokenRingPHistoryTable")

        self.ringstationcontroltable = TOKENRINGRMONMIB.Ringstationcontroltable()
        self.ringstationcontroltable.parent = self
        self._children_name_map["ringstationcontroltable"] = "ringStationControlTable"
        self._children_yang_names.add("ringStationControlTable")

        self.ringstationtable = TOKENRINGRMONMIB.Ringstationtable()
        self.ringstationtable.parent = self
        self._children_name_map["ringstationtable"] = "ringStationTable"
        self._children_yang_names.add("ringStationTable")

        self.ringstationordertable = TOKENRINGRMONMIB.Ringstationordertable()
        self.ringstationordertable.parent = self
        self._children_name_map["ringstationordertable"] = "ringStationOrderTable"
        self._children_yang_names.add("ringStationOrderTable")

        self.ringstationconfigcontroltable = TOKENRINGRMONMIB.Ringstationconfigcontroltable()
        self.ringstationconfigcontroltable.parent = self
        self._children_name_map["ringstationconfigcontroltable"] = "ringStationConfigControlTable"
        self._children_yang_names.add("ringStationConfigControlTable")

        self.ringstationconfigtable = TOKENRINGRMONMIB.Ringstationconfigtable()
        self.ringstationconfigtable.parent = self
        self._children_name_map["ringstationconfigtable"] = "ringStationConfigTable"
        self._children_yang_names.add("ringStationConfigTable")

        self.sourceroutingstatstable = TOKENRINGRMONMIB.Sourceroutingstatstable()
        self.sourceroutingstatstable.parent = self
        self._children_name_map["sourceroutingstatstable"] = "sourceRoutingStatsTable"
        self._children_yang_names.add("sourceRoutingStatsTable")
        self._segment_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB"


    class Tokenringmlstatstable(Entity):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlstatsentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`Tokenringmlstatsentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringmlstatstable.Tokenringmlstatsentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Tokenringmlstatstable, self).__init__()

            self.yang_name = "tokenRingMLStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("tokenRingMLStatsEntry", ("tokenringmlstatsentry", TOKENRINGRMONMIB.Tokenringmlstatstable.Tokenringmlstatsentry))])
            self._leafs = OrderedDict()

            self.tokenringmlstatsentry = YList(self)
            self._segment_path = lambda: "tokenRingMLStatsTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Tokenringmlstatstable, [], name, value)


        class Tokenringmlstatsentry(Entity):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlstatsindex  (key)
            
            	The value of this object uniquely identifies this tokenRingMLStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringmlstatsdatasource
            
            	This object identifies the source of the data that this tokenRingMLStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all error reports on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingMLStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: tokenringmlstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingPStatsDropEvents
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsmacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsmacpkts
            
            	The total number of MAC packets (excluding packets that were not good frames) received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpurgeevents
            
            	The total number of times that the ring enters the ring purge state from normal ring state.  The ring purge state that comes in response to the claim token or beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpurgepkts
            
            	The total number of ring purge MAC packets detected by probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState,      beaconSetRecoveryModeState, or beaconRingSignalLossState) from a non\-beaconing state.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeacontime
            
            	The total amount of time that the ring has been in the beaconing state
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlstatsbeaconpkts
            
            	The total number of beacon MAC packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state.  The claim token state that comes in response to a beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsnaunchanges
            
            	The total number of NAUN changes detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatslineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsacerrors
            
            	The total number of AC (Address Copied)  errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatslostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatscongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatstokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatssofterrorreports
            
            	The total number of soft error report frames detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpollevents
            
            	The total number of ring poll events detected by the probe (i.e. the number of ring polls initiated by the active monitor that were detected)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: tokenringmlstatsstatus
            
            	The status of this tokenRingMLStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            .. attribute:: tokenringmlstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Tokenringmlstatstable.Tokenringmlstatsentry, self).__init__()

                self.yang_name = "tokenRingMLStatsEntry"
                self.yang_parent_name = "tokenRingMLStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringmlstatsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringmlstatsindex', YLeaf(YType.int32, 'tokenRingMLStatsIndex')),
                    ('tokenringmlstatsdatasource', YLeaf(YType.str, 'tokenRingMLStatsDataSource')),
                    ('tokenringmlstatsdropevents', YLeaf(YType.uint32, 'tokenRingMLStatsDropEvents')),
                    ('tokenringmlstatsmacoctets', YLeaf(YType.uint32, 'tokenRingMLStatsMacOctets')),
                    ('tokenringmlstatsmacpkts', YLeaf(YType.uint32, 'tokenRingMLStatsMacPkts')),
                    ('tokenringmlstatsringpurgeevents', YLeaf(YType.uint32, 'tokenRingMLStatsRingPurgeEvents')),
                    ('tokenringmlstatsringpurgepkts', YLeaf(YType.uint32, 'tokenRingMLStatsRingPurgePkts')),
                    ('tokenringmlstatsbeaconevents', YLeaf(YType.uint32, 'tokenRingMLStatsBeaconEvents')),
                    ('tokenringmlstatsbeacontime', YLeaf(YType.int32, 'tokenRingMLStatsBeaconTime')),
                    ('tokenringmlstatsbeaconpkts', YLeaf(YType.uint32, 'tokenRingMLStatsBeaconPkts')),
                    ('tokenringmlstatsclaimtokenevents', YLeaf(YType.uint32, 'tokenRingMLStatsClaimTokenEvents')),
                    ('tokenringmlstatsclaimtokenpkts', YLeaf(YType.uint32, 'tokenRingMLStatsClaimTokenPkts')),
                    ('tokenringmlstatsnaunchanges', YLeaf(YType.uint32, 'tokenRingMLStatsNAUNChanges')),
                    ('tokenringmlstatslineerrors', YLeaf(YType.uint32, 'tokenRingMLStatsLineErrors')),
                    ('tokenringmlstatsinternalerrors', YLeaf(YType.uint32, 'tokenRingMLStatsInternalErrors')),
                    ('tokenringmlstatsbursterrors', YLeaf(YType.uint32, 'tokenRingMLStatsBurstErrors')),
                    ('tokenringmlstatsacerrors', YLeaf(YType.uint32, 'tokenRingMLStatsACErrors')),
                    ('tokenringmlstatsaborterrors', YLeaf(YType.uint32, 'tokenRingMLStatsAbortErrors')),
                    ('tokenringmlstatslostframeerrors', YLeaf(YType.uint32, 'tokenRingMLStatsLostFrameErrors')),
                    ('tokenringmlstatscongestionerrors', YLeaf(YType.uint32, 'tokenRingMLStatsCongestionErrors')),
                    ('tokenringmlstatsframecopiederrors', YLeaf(YType.uint32, 'tokenRingMLStatsFrameCopiedErrors')),
                    ('tokenringmlstatsfrequencyerrors', YLeaf(YType.uint32, 'tokenRingMLStatsFrequencyErrors')),
                    ('tokenringmlstatstokenerrors', YLeaf(YType.uint32, 'tokenRingMLStatsTokenErrors')),
                    ('tokenringmlstatssofterrorreports', YLeaf(YType.uint32, 'tokenRingMLStatsSoftErrorReports')),
                    ('tokenringmlstatsringpollevents', YLeaf(YType.uint32, 'tokenRingMLStatsRingPollEvents')),
                    ('tokenringmlstatsowner', YLeaf(YType.str, 'tokenRingMLStatsOwner')),
                    ('tokenringmlstatsstatus', YLeaf(YType.enumeration, 'tokenRingMLStatsStatus')),
                    ('tokenringmlstatsdroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:tokenRingMLStatsDroppedFrames')),
                    ('tokenringmlstatscreatetime', YLeaf(YType.uint32, 'RMON2-MIB:tokenRingMLStatsCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Tokenringmlstatstable.Tokenringmlstatsentry, ['tokenringmlstatsindex', 'tokenringmlstatsdatasource', 'tokenringmlstatsdropevents', 'tokenringmlstatsmacoctets', 'tokenringmlstatsmacpkts', 'tokenringmlstatsringpurgeevents', 'tokenringmlstatsringpurgepkts', 'tokenringmlstatsbeaconevents', 'tokenringmlstatsbeacontime', 'tokenringmlstatsbeaconpkts', 'tokenringmlstatsclaimtokenevents', 'tokenringmlstatsclaimtokenpkts', 'tokenringmlstatsnaunchanges', 'tokenringmlstatslineerrors', 'tokenringmlstatsinternalerrors', 'tokenringmlstatsbursterrors', 'tokenringmlstatsacerrors', 'tokenringmlstatsaborterrors', 'tokenringmlstatslostframeerrors', 'tokenringmlstatscongestionerrors', 'tokenringmlstatsframecopiederrors', 'tokenringmlstatsfrequencyerrors', 'tokenringmlstatstokenerrors', 'tokenringmlstatssofterrorreports', 'tokenringmlstatsringpollevents', 'tokenringmlstatsowner', 'tokenringmlstatsstatus', 'tokenringmlstatsdroppedframes', 'tokenringmlstatscreatetime'], name, value)


    class Tokenringpstatstable(Entity):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringpstatsentry
        
        	A collection of promiscuous statistics kept for non\-MAC packets on a particular Token Ring interface
        	**type**\: list of  		 :py:class:`Tokenringpstatsentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringpstatstable.Tokenringpstatsentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Tokenringpstatstable, self).__init__()

            self.yang_name = "tokenRingPStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("tokenRingPStatsEntry", ("tokenringpstatsentry", TOKENRINGRMONMIB.Tokenringpstatstable.Tokenringpstatsentry))])
            self._leafs = OrderedDict()

            self.tokenringpstatsentry = YList(self)
            self._segment_path = lambda: "tokenRingPStatsTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Tokenringpstatstable, [], name, value)


        class Tokenringpstatsentry(Entity):
            """
            A collection of promiscuous statistics kept for
            non\-MAC packets on a particular Token Ring
            interface.
            
            .. attribute:: tokenringpstatsindex  (key)
            
            	The value of this object uniquely identifies this tokenRingPStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringpstatsdatasource
            
            	This object identifies the source of the data that this tokenRingPStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all non\-MAC packets on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingPStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: tokenringpstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingMLStatsDropEvents
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts
            
            	The total number of non\-MAC packets in good frames.  received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatabroadcastpkts
            
            	The total number of good non\-MAC frames received that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatamulticastpkts
            
            	The total number of good non\-MAC frames received that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts18to63octets
            
            	The total number of good non\-MAC frames received that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts64to127octets
            
            	The total number of good non\-MAC frames received that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts128to255octets
            
            	The total number of good non\-MAC frames received that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts256to511octets
            
            	The total number of good non\-MAC frames received that were between 256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts512to1023octets
            
            	The total number of good non\-MAC frames received that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: tokenringpstatsstatus
            
            	The status of this tokenRingPStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            .. attribute:: tokenringpstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Tokenringpstatstable.Tokenringpstatsentry, self).__init__()

                self.yang_name = "tokenRingPStatsEntry"
                self.yang_parent_name = "tokenRingPStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringpstatsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringpstatsindex', YLeaf(YType.int32, 'tokenRingPStatsIndex')),
                    ('tokenringpstatsdatasource', YLeaf(YType.str, 'tokenRingPStatsDataSource')),
                    ('tokenringpstatsdropevents', YLeaf(YType.uint32, 'tokenRingPStatsDropEvents')),
                    ('tokenringpstatsdataoctets', YLeaf(YType.uint32, 'tokenRingPStatsDataOctets')),
                    ('tokenringpstatsdatapkts', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts')),
                    ('tokenringpstatsdatabroadcastpkts', YLeaf(YType.uint32, 'tokenRingPStatsDataBroadcastPkts')),
                    ('tokenringpstatsdatamulticastpkts', YLeaf(YType.uint32, 'tokenRingPStatsDataMulticastPkts')),
                    ('tokenringpstatsdatapkts18to63octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts18to63Octets')),
                    ('tokenringpstatsdatapkts64to127octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts64to127Octets')),
                    ('tokenringpstatsdatapkts128to255octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts128to255Octets')),
                    ('tokenringpstatsdatapkts256to511octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts256to511Octets')),
                    ('tokenringpstatsdatapkts512to1023octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts512to1023Octets')),
                    ('tokenringpstatsdatapkts1024to2047octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts1024to2047Octets')),
                    ('tokenringpstatsdatapkts2048to4095octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts2048to4095Octets')),
                    ('tokenringpstatsdatapkts4096to8191octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts4096to8191Octets')),
                    ('tokenringpstatsdatapkts8192to18000octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPkts8192to18000Octets')),
                    ('tokenringpstatsdatapktsgreaterthan18000octets', YLeaf(YType.uint32, 'tokenRingPStatsDataPktsGreaterThan18000Octets')),
                    ('tokenringpstatsowner', YLeaf(YType.str, 'tokenRingPStatsOwner')),
                    ('tokenringpstatsstatus', YLeaf(YType.enumeration, 'tokenRingPStatsStatus')),
                    ('tokenringpstatsdroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:tokenRingPStatsDroppedFrames')),
                    ('tokenringpstatscreatetime', YLeaf(YType.uint32, 'RMON2-MIB:tokenRingPStatsCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Tokenringpstatstable.Tokenringpstatsentry, ['tokenringpstatsindex', 'tokenringpstatsdatasource', 'tokenringpstatsdropevents', 'tokenringpstatsdataoctets', 'tokenringpstatsdatapkts', 'tokenringpstatsdatabroadcastpkts', 'tokenringpstatsdatamulticastpkts', 'tokenringpstatsdatapkts18to63octets', 'tokenringpstatsdatapkts64to127octets', 'tokenringpstatsdatapkts128to255octets', 'tokenringpstatsdatapkts256to511octets', 'tokenringpstatsdatapkts512to1023octets', 'tokenringpstatsdatapkts1024to2047octets', 'tokenringpstatsdatapkts2048to4095octets', 'tokenringpstatsdatapkts4096to8191octets', 'tokenringpstatsdatapkts8192to18000octets', 'tokenringpstatsdatapktsgreaterthan18000octets', 'tokenringpstatsowner', 'tokenringpstatsstatus', 'tokenringpstatsdroppedframes', 'tokenringpstatscreatetime'], name, value)


    class Tokenringmlhistorytable(Entity):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlhistoryentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`Tokenringmlhistoryentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringmlhistorytable.Tokenringmlhistoryentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Tokenringmlhistorytable, self).__init__()

            self.yang_name = "tokenRingMLHistoryTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("tokenRingMLHistoryEntry", ("tokenringmlhistoryentry", TOKENRINGRMONMIB.Tokenringmlhistorytable.Tokenringmlhistoryentry))])
            self._leafs = OrderedDict()

            self.tokenringmlhistoryentry = YList(self)
            self._segment_path = lambda: "tokenRingMLHistoryTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Tokenringmlhistorytable, [], name, value)


        class Tokenringmlhistoryentry(Entity):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlhistoryindex  (key)
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringmlhistorysampleindex  (key)
            
            	An index that uniquely identifies the particular Mac\-Layer sample this entry represents among all Mac\-Layer samples associated with the same historyControlEntry.  This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorydropevents
            
            	The total number of events in which packets were      dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorymacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network during this sampling interval (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorymacpkts
            
            	The total number of MAC packets (excluding those that were not good frames) received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpurgeevents
            
            	The total number of times that the ring entered the ring purge state from normal ring state during this sampling interval.  The ring purge state that comes from the claim token or beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpurgepkts
            
            	The total number of Ring Purge MAC packets detected by the probe during this sampling      interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState, beaconSetRecoveryModeState, or beaconRingSignalLossState) during this sampling interval.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybeacontime
            
            	The amount of time that the ring has been in the beaconing state during this sampling interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistorybeaconpkts
            
            	The total number of beacon MAC packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state during this sampling interval. The claim token state that comes from the beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorynaunchanges
            
            	The total number of NAUN changes detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorylineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorylostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorycongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorytokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorysofterrorreports
            
            	The total number of soft error report frames detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpollevents
            
            	The total number of ring poll events detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryactivestations
            
            	The maximum number of active stations on the ring detected by the probe during this sampling      interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Tokenringmlhistorytable.Tokenringmlhistoryentry, self).__init__()

                self.yang_name = "tokenRingMLHistoryEntry"
                self.yang_parent_name = "tokenRingMLHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringmlhistoryindex','tokenringmlhistorysampleindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringmlhistoryindex', YLeaf(YType.int32, 'tokenRingMLHistoryIndex')),
                    ('tokenringmlhistorysampleindex', YLeaf(YType.int32, 'tokenRingMLHistorySampleIndex')),
                    ('tokenringmlhistoryintervalstart', YLeaf(YType.uint32, 'tokenRingMLHistoryIntervalStart')),
                    ('tokenringmlhistorydropevents', YLeaf(YType.uint32, 'tokenRingMLHistoryDropEvents')),
                    ('tokenringmlhistorymacoctets', YLeaf(YType.uint32, 'tokenRingMLHistoryMacOctets')),
                    ('tokenringmlhistorymacpkts', YLeaf(YType.uint32, 'tokenRingMLHistoryMacPkts')),
                    ('tokenringmlhistoryringpurgeevents', YLeaf(YType.uint32, 'tokenRingMLHistoryRingPurgeEvents')),
                    ('tokenringmlhistoryringpurgepkts', YLeaf(YType.uint32, 'tokenRingMLHistoryRingPurgePkts')),
                    ('tokenringmlhistorybeaconevents', YLeaf(YType.uint32, 'tokenRingMLHistoryBeaconEvents')),
                    ('tokenringmlhistorybeacontime', YLeaf(YType.int32, 'tokenRingMLHistoryBeaconTime')),
                    ('tokenringmlhistorybeaconpkts', YLeaf(YType.uint32, 'tokenRingMLHistoryBeaconPkts')),
                    ('tokenringmlhistoryclaimtokenevents', YLeaf(YType.uint32, 'tokenRingMLHistoryClaimTokenEvents')),
                    ('tokenringmlhistoryclaimtokenpkts', YLeaf(YType.uint32, 'tokenRingMLHistoryClaimTokenPkts')),
                    ('tokenringmlhistorynaunchanges', YLeaf(YType.uint32, 'tokenRingMLHistoryNAUNChanges')),
                    ('tokenringmlhistorylineerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryLineErrors')),
                    ('tokenringmlhistoryinternalerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryInternalErrors')),
                    ('tokenringmlhistorybursterrors', YLeaf(YType.uint32, 'tokenRingMLHistoryBurstErrors')),
                    ('tokenringmlhistoryacerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryACErrors')),
                    ('tokenringmlhistoryaborterrors', YLeaf(YType.uint32, 'tokenRingMLHistoryAbortErrors')),
                    ('tokenringmlhistorylostframeerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryLostFrameErrors')),
                    ('tokenringmlhistorycongestionerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryCongestionErrors')),
                    ('tokenringmlhistoryframecopiederrors', YLeaf(YType.uint32, 'tokenRingMLHistoryFrameCopiedErrors')),
                    ('tokenringmlhistoryfrequencyerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryFrequencyErrors')),
                    ('tokenringmlhistorytokenerrors', YLeaf(YType.uint32, 'tokenRingMLHistoryTokenErrors')),
                    ('tokenringmlhistorysofterrorreports', YLeaf(YType.uint32, 'tokenRingMLHistorySoftErrorReports')),
                    ('tokenringmlhistoryringpollevents', YLeaf(YType.uint32, 'tokenRingMLHistoryRingPollEvents')),
                    ('tokenringmlhistoryactivestations', YLeaf(YType.int32, 'tokenRingMLHistoryActiveStations')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Tokenringmlhistorytable.Tokenringmlhistoryentry, ['tokenringmlhistoryindex', 'tokenringmlhistorysampleindex', 'tokenringmlhistoryintervalstart', 'tokenringmlhistorydropevents', 'tokenringmlhistorymacoctets', 'tokenringmlhistorymacpkts', 'tokenringmlhistoryringpurgeevents', 'tokenringmlhistoryringpurgepkts', 'tokenringmlhistorybeaconevents', 'tokenringmlhistorybeacontime', 'tokenringmlhistorybeaconpkts', 'tokenringmlhistoryclaimtokenevents', 'tokenringmlhistoryclaimtokenpkts', 'tokenringmlhistorynaunchanges', 'tokenringmlhistorylineerrors', 'tokenringmlhistoryinternalerrors', 'tokenringmlhistorybursterrors', 'tokenringmlhistoryacerrors', 'tokenringmlhistoryaborterrors', 'tokenringmlhistorylostframeerrors', 'tokenringmlhistorycongestionerrors', 'tokenringmlhistoryframecopiederrors', 'tokenringmlhistoryfrequencyerrors', 'tokenringmlhistorytokenerrors', 'tokenringmlhistorysofterrorreports', 'tokenringmlhistoryringpollevents', 'tokenringmlhistoryactivestations'], name, value)


    class Tokenringphistorytable(Entity):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringphistoryentry
        
        	A collection of promiscuous statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`Tokenringphistoryentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Tokenringphistorytable.Tokenringphistoryentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Tokenringphistorytable, self).__init__()

            self.yang_name = "tokenRingPHistoryTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("tokenRingPHistoryEntry", ("tokenringphistoryentry", TOKENRINGRMONMIB.Tokenringphistorytable.Tokenringphistoryentry))])
            self._leafs = OrderedDict()

            self.tokenringphistoryentry = YList(self)
            self._segment_path = lambda: "tokenRingPHistoryTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Tokenringphistorytable, [], name, value)


        class Tokenringphistoryentry(Entity):
            """
            A collection of promiscuous statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringphistoryindex  (key)
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringphistorysampleindex  (key)
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringphistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts
            
            	The total number of good non\-MAC frames received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatabroadcastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatamulticastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts18to63octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts64to127octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts128to255octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts256to511octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between      256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts512to1023octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Tokenringphistorytable.Tokenringphistoryentry, self).__init__()

                self.yang_name = "tokenRingPHistoryEntry"
                self.yang_parent_name = "tokenRingPHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tokenringphistoryindex','tokenringphistorysampleindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tokenringphistoryindex', YLeaf(YType.int32, 'tokenRingPHistoryIndex')),
                    ('tokenringphistorysampleindex', YLeaf(YType.int32, 'tokenRingPHistorySampleIndex')),
                    ('tokenringphistoryintervalstart', YLeaf(YType.uint32, 'tokenRingPHistoryIntervalStart')),
                    ('tokenringphistorydropevents', YLeaf(YType.uint32, 'tokenRingPHistoryDropEvents')),
                    ('tokenringphistorydataoctets', YLeaf(YType.uint32, 'tokenRingPHistoryDataOctets')),
                    ('tokenringphistorydatapkts', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts')),
                    ('tokenringphistorydatabroadcastpkts', YLeaf(YType.uint32, 'tokenRingPHistoryDataBroadcastPkts')),
                    ('tokenringphistorydatamulticastpkts', YLeaf(YType.uint32, 'tokenRingPHistoryDataMulticastPkts')),
                    ('tokenringphistorydatapkts18to63octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts18to63Octets')),
                    ('tokenringphistorydatapkts64to127octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts64to127Octets')),
                    ('tokenringphistorydatapkts128to255octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts128to255Octets')),
                    ('tokenringphistorydatapkts256to511octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts256to511Octets')),
                    ('tokenringphistorydatapkts512to1023octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts512to1023Octets')),
                    ('tokenringphistorydatapkts1024to2047octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts1024to2047Octets')),
                    ('tokenringphistorydatapkts2048to4095octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts2048to4095Octets')),
                    ('tokenringphistorydatapkts4096to8191octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts4096to8191Octets')),
                    ('tokenringphistorydatapkts8192to18000octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPkts8192to18000Octets')),
                    ('tokenringphistorydatapktsgreaterthan18000octets', YLeaf(YType.uint32, 'tokenRingPHistoryDataPktsGreaterThan18000Octets')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Tokenringphistorytable.Tokenringphistoryentry, ['tokenringphistoryindex', 'tokenringphistorysampleindex', 'tokenringphistoryintervalstart', 'tokenringphistorydropevents', 'tokenringphistorydataoctets', 'tokenringphistorydatapkts', 'tokenringphistorydatabroadcastpkts', 'tokenringphistorydatamulticastpkts', 'tokenringphistorydatapkts18to63octets', 'tokenringphistorydatapkts64to127octets', 'tokenringphistorydatapkts128to255octets', 'tokenringphistorydatapkts256to511octets', 'tokenringphistorydatapkts512to1023octets', 'tokenringphistorydatapkts1024to2047octets', 'tokenringphistorydatapkts2048to4095octets', 'tokenringphistorydatapkts4096to8191octets', 'tokenringphistorydatapkts8192to18000octets', 'tokenringphistorydatapktsgreaterthan18000octets'], name, value)


    class Ringstationcontroltable(Entity):
        """
        A list of ringStation table control entries.
        
        .. attribute:: ringstationcontrolentry
        
        	A list of parameters that set up the discovery of stations on a particular interface and the collection of statistics about these stations
        	**type**\: list of  		 :py:class:`Ringstationcontrolentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationcontroltable.Ringstationcontrolentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Ringstationcontroltable, self).__init__()

            self.yang_name = "ringStationControlTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ringStationControlEntry", ("ringstationcontrolentry", TOKENRINGRMONMIB.Ringstationcontroltable.Ringstationcontrolentry))])
            self._leafs = OrderedDict()

            self.ringstationcontrolentry = YList(self)
            self._segment_path = lambda: "ringStationControlTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Ringstationcontroltable, [], name, value)


        class Ringstationcontrolentry(Entity):
            """
            A list of parameters that set up the discovery of
            stations on a particular interface and the
            collection of statistics about these stations.
            
            .. attribute:: ringstationcontrolifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device from which ringStation data is collected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\- II [3]
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: ringstationcontroltablesize
            
            	The number of ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationcontrolactivestations
            
            	The number of active ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationcontrolringstate
            
            	The current status of this ring
            	**type**\:  :py:class:`Ringstationcontrolringstate <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationcontroltable.Ringstationcontrolentry.Ringstationcontrolringstate>`
            
            .. attribute:: ringstationcontrolbeaconsender
            
            	The address of the sender of the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationcontrolbeaconnaun
            
            	The address of the NAUN in the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationcontrolactivemonitor
            
            	The address of the Active Monitor on this segment.  If this address is unknown, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationcontrolorderchanges
            
            	The number of add and delete events in the ringStationOrderTable optionally associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: ringstationcontrolstatus
            
            	The status of this ringStationControl entry.  If this object is not equal to valid(1), all associated entries in the ringStationTable shall be deleted by the agent
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            .. attribute:: ringstationcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Ringstationcontroltable.Ringstationcontrolentry, self).__init__()

                self.yang_name = "ringStationControlEntry"
                self.yang_parent_name = "ringStationControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationcontrolifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationcontrolifindex', YLeaf(YType.int32, 'ringStationControlIfIndex')),
                    ('ringstationcontroltablesize', YLeaf(YType.int32, 'ringStationControlTableSize')),
                    ('ringstationcontrolactivestations', YLeaf(YType.int32, 'ringStationControlActiveStations')),
                    ('ringstationcontrolringstate', YLeaf(YType.enumeration, 'ringStationControlRingState')),
                    ('ringstationcontrolbeaconsender', YLeaf(YType.str, 'ringStationControlBeaconSender')),
                    ('ringstationcontrolbeaconnaun', YLeaf(YType.str, 'ringStationControlBeaconNAUN')),
                    ('ringstationcontrolactivemonitor', YLeaf(YType.str, 'ringStationControlActiveMonitor')),
                    ('ringstationcontrolorderchanges', YLeaf(YType.uint32, 'ringStationControlOrderChanges')),
                    ('ringstationcontrolowner', YLeaf(YType.str, 'ringStationControlOwner')),
                    ('ringstationcontrolstatus', YLeaf(YType.enumeration, 'ringStationControlStatus')),
                    ('ringstationcontroldroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:ringStationControlDroppedFrames')),
                    ('ringstationcontrolcreatetime', YLeaf(YType.uint32, 'RMON2-MIB:ringStationControlCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Ringstationcontroltable.Ringstationcontrolentry, ['ringstationcontrolifindex', 'ringstationcontroltablesize', 'ringstationcontrolactivestations', 'ringstationcontrolringstate', 'ringstationcontrolbeaconsender', 'ringstationcontrolbeaconnaun', 'ringstationcontrolactivemonitor', 'ringstationcontrolorderchanges', 'ringstationcontrolowner', 'ringstationcontrolstatus', 'ringstationcontroldroppedframes', 'ringstationcontrolcreatetime'], name, value)

            class Ringstationcontrolringstate(Enum):
                """
                Ringstationcontrolringstate (Enum Class)

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



    class Ringstationtable(Entity):
        """
        A list of ring station entries.  An entry will
        exist for each station that is now or has
        
        
        
        
        
        previously been detected as physically present on
        this ring.
        
        .. attribute:: ringstationentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this device
        	**type**\: list of  		 :py:class:`Ringstationentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationtable.Ringstationentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Ringstationtable, self).__init__()

            self.yang_name = "ringStationTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ringStationEntry", ("ringstationentry", TOKENRINGRMONMIB.Ringstationtable.Ringstationentry))])
            self._leafs = OrderedDict()

            self.ringstationentry = YList(self)
            self._segment_path = lambda: "ringStationTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Ringstationtable, [], name, value)


        class Ringstationentry(Entity):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this device.
            
            .. attribute:: ringstationifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationmacaddress  (key)
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationlastnaun
            
            	The physical address of last known NAUN of this station
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationstationstatus
            
            	The status of this station on the ring
            	**type**\:  :py:class:`Ringstationstationstatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationtable.Ringstationentry.Ringstationstationstatus>`
            
            .. attribute:: ringstationlastentertime
            
            	The value of sysUpTime at the time this station last entered the ring.  If the time is unknown, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastexittime
            
            	The value of sysUpTime at the time the probe detected that this station last exited the ring. If the time is unknown, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationduplicateaddresses
            
            	The number of times this station experienced a duplicate address error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinlineerrors
            
            	The total number of line errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutlineerrors
            
            	The total number of line errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinternalerrors
            
            	The total number of adapter internal errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinbursterrors
            
            	The total number of burst errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutbursterrors
            
            	The total number of burst errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationaborterrors
            
            	The total number of abort delimiters reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlostframeerrors
            
            	The total number of lost frame errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcongestionerrors
            
            	The total number of receive congestion errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationframecopiederrors
            
            	The total number of frame copied errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationfrequencyerrors
            
            	The total number of frequency errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationtokenerrors
            
            	The total number of token errors reported by this station in error reporting frames detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinbeaconerrors
            
            	The total number of beacon frames sent by this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutbeaconerrors
            
            	The total number of beacon frames detected by the probe that name this station as the NAUN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinsertions
            
            	The number of times the probe detected this station inserting onto the ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Ringstationtable.Ringstationentry, self).__init__()

                self.yang_name = "ringStationEntry"
                self.yang_parent_name = "ringStationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationifindex','ringstationmacaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationifindex', YLeaf(YType.int32, 'ringStationIfIndex')),
                    ('ringstationmacaddress', YLeaf(YType.str, 'ringStationMacAddress')),
                    ('ringstationlastnaun', YLeaf(YType.str, 'ringStationLastNAUN')),
                    ('ringstationstationstatus', YLeaf(YType.enumeration, 'ringStationStationStatus')),
                    ('ringstationlastentertime', YLeaf(YType.uint32, 'ringStationLastEnterTime')),
                    ('ringstationlastexittime', YLeaf(YType.uint32, 'ringStationLastExitTime')),
                    ('ringstationduplicateaddresses', YLeaf(YType.uint32, 'ringStationDuplicateAddresses')),
                    ('ringstationinlineerrors', YLeaf(YType.uint32, 'ringStationInLineErrors')),
                    ('ringstationoutlineerrors', YLeaf(YType.uint32, 'ringStationOutLineErrors')),
                    ('ringstationinternalerrors', YLeaf(YType.uint32, 'ringStationInternalErrors')),
                    ('ringstationinbursterrors', YLeaf(YType.uint32, 'ringStationInBurstErrors')),
                    ('ringstationoutbursterrors', YLeaf(YType.uint32, 'ringStationOutBurstErrors')),
                    ('ringstationacerrors', YLeaf(YType.uint32, 'ringStationACErrors')),
                    ('ringstationaborterrors', YLeaf(YType.uint32, 'ringStationAbortErrors')),
                    ('ringstationlostframeerrors', YLeaf(YType.uint32, 'ringStationLostFrameErrors')),
                    ('ringstationcongestionerrors', YLeaf(YType.uint32, 'ringStationCongestionErrors')),
                    ('ringstationframecopiederrors', YLeaf(YType.uint32, 'ringStationFrameCopiedErrors')),
                    ('ringstationfrequencyerrors', YLeaf(YType.uint32, 'ringStationFrequencyErrors')),
                    ('ringstationtokenerrors', YLeaf(YType.uint32, 'ringStationTokenErrors')),
                    ('ringstationinbeaconerrors', YLeaf(YType.uint32, 'ringStationInBeaconErrors')),
                    ('ringstationoutbeaconerrors', YLeaf(YType.uint32, 'ringStationOutBeaconErrors')),
                    ('ringstationinsertions', YLeaf(YType.uint32, 'ringStationInsertions')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Ringstationtable.Ringstationentry, ['ringstationifindex', 'ringstationmacaddress', 'ringstationlastnaun', 'ringstationstationstatus', 'ringstationlastentertime', 'ringstationlastexittime', 'ringstationduplicateaddresses', 'ringstationinlineerrors', 'ringstationoutlineerrors', 'ringstationinternalerrors', 'ringstationinbursterrors', 'ringstationoutbursterrors', 'ringstationacerrors', 'ringstationaborterrors', 'ringstationlostframeerrors', 'ringstationcongestionerrors', 'ringstationframecopiederrors', 'ringstationfrequencyerrors', 'ringstationtokenerrors', 'ringstationinbeaconerrors', 'ringstationoutbeaconerrors', 'ringstationinsertions'], name, value)

            class Ringstationstationstatus(Enum):
                """
                Ringstationstationstatus (Enum Class)

                The status of this station on the ring.

                .. data:: active = 1

                .. data:: inactive = 2

                .. data:: forcedRemoval = 3

                """

                active = Enum.YLeaf(1, "active")

                inactive = Enum.YLeaf(2, "inactive")

                forcedRemoval = Enum.YLeaf(3, "forcedRemoval")



    class Ringstationordertable(Entity):
        """
        A list of ring station entries for stations in
        the ring poll, ordered by their ring\-order.
        
        .. attribute:: ringstationorderentry
        
        	A collection of statistics for a particular      station that is active on a ring monitored by this device.  This table will contain information for every interface that has a ringStationControlStatus equal to valid
        	**type**\: list of  		 :py:class:`Ringstationorderentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationordertable.Ringstationorderentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Ringstationordertable, self).__init__()

            self.yang_name = "ringStationOrderTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ringStationOrderEntry", ("ringstationorderentry", TOKENRINGRMONMIB.Ringstationordertable.Ringstationorderentry))])
            self._leafs = OrderedDict()

            self.ringstationorderentry = YList(self)
            self._segment_path = lambda: "ringStationOrderTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Ringstationordertable, [], name, value)


        class Ringstationorderentry(Entity):
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
            
            .. attribute:: ringstationorderorderindex  (key)
            
            	This index denotes the location of this station with respect to other stations on the ring.  This index is one more than the number of hops downstream that this station is from the rmon probe.  The rmon probe itself gets the value one
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationordermacaddress
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Ringstationordertable.Ringstationorderentry, self).__init__()

                self.yang_name = "ringStationOrderEntry"
                self.yang_parent_name = "ringStationOrderTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationorderifindex','ringstationorderorderindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationorderifindex', YLeaf(YType.int32, 'ringStationOrderIfIndex')),
                    ('ringstationorderorderindex', YLeaf(YType.int32, 'ringStationOrderOrderIndex')),
                    ('ringstationordermacaddress', YLeaf(YType.str, 'ringStationOrderMacAddress')),
                ])
                self.ringstationorderifindex = None
                self.ringstationorderorderindex = None
                self.ringstationordermacaddress = None
                self._segment_path = lambda: "ringStationOrderEntry" + "[ringStationOrderIfIndex='" + str(self.ringstationorderifindex) + "']" + "[ringStationOrderOrderIndex='" + str(self.ringstationorderorderindex) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationOrderTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Ringstationordertable.Ringstationorderentry, ['ringstationorderifindex', 'ringstationorderorderindex', 'ringstationordermacaddress'], name, value)


    class Ringstationconfigcontroltable(Entity):
        """
        A list of ring station configuration control
        entries.
        
        .. attribute:: ringstationconfigcontrolentry
        
        	This entry controls active management of stations by the probe.  One entry exists in this table for each active station in the ringStationTable
        	**type**\: list of  		 :py:class:`Ringstationconfigcontrolentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationconfigcontroltable.Ringstationconfigcontrolentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Ringstationconfigcontroltable, self).__init__()

            self.yang_name = "ringStationConfigControlTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ringStationConfigControlEntry", ("ringstationconfigcontrolentry", TOKENRINGRMONMIB.Ringstationconfigcontroltable.Ringstationconfigcontrolentry))])
            self._leafs = OrderedDict()

            self.ringstationconfigcontrolentry = YList(self)
            self._segment_path = lambda: "ringStationConfigControlTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Ringstationconfigcontroltable, [], name, value)


        class Ringstationconfigcontrolentry(Entity):
            """
            This entry controls active management of stations
            by the probe.  One entry exists in this table for
            each active station in the ringStationTable.
            
            .. attribute:: ringstationconfigcontrolifindex  (key)
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationconfigcontrolmacaddress  (key)
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationconfigcontrolremove
            
            	Setting this object to `removing(2)' causes a Remove Station MAC frame to be sent.  The agent will set this object to `stable(1)' after processing the request
            	**type**\:  :py:class:`Ringstationconfigcontrolremove <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.Ringstationconfigcontrolremove>`
            
            .. attribute:: ringstationconfigcontrolupdatestats
            
            	Setting this object to `updating(2)' causes the configuration information associate with this entry to be updated.  The agent will set this object to `stable(1)' after processing the request
            	**type**\:  :py:class:`Ringstationconfigcontrolupdatestats <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.Ringstationconfigcontrolupdatestats>`
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Ringstationconfigcontroltable.Ringstationconfigcontrolentry, self).__init__()

                self.yang_name = "ringStationConfigControlEntry"
                self.yang_parent_name = "ringStationConfigControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationconfigcontrolifindex','ringstationconfigcontrolmacaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationconfigcontrolifindex', YLeaf(YType.int32, 'ringStationConfigControlIfIndex')),
                    ('ringstationconfigcontrolmacaddress', YLeaf(YType.str, 'ringStationConfigControlMacAddress')),
                    ('ringstationconfigcontrolremove', YLeaf(YType.enumeration, 'ringStationConfigControlRemove')),
                    ('ringstationconfigcontrolupdatestats', YLeaf(YType.enumeration, 'ringStationConfigControlUpdateStats')),
                ])
                self.ringstationconfigcontrolifindex = None
                self.ringstationconfigcontrolmacaddress = None
                self.ringstationconfigcontrolremove = None
                self.ringstationconfigcontrolupdatestats = None
                self._segment_path = lambda: "ringStationConfigControlEntry" + "[ringStationConfigControlIfIndex='" + str(self.ringstationconfigcontrolifindex) + "']" + "[ringStationConfigControlMacAddress='" + str(self.ringstationconfigcontrolmacaddress) + "']"
                self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationConfigControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Ringstationconfigcontroltable.Ringstationconfigcontrolentry, ['ringstationconfigcontrolifindex', 'ringstationconfigcontrolmacaddress', 'ringstationconfigcontrolremove', 'ringstationconfigcontrolupdatestats'], name, value)

            class Ringstationconfigcontrolremove(Enum):
                """
                Ringstationconfigcontrolremove (Enum Class)

                Setting this object to `removing(2)' causes a

                Remove Station MAC frame to be sent.  The agent

                will set this object to `stable(1)' after

                processing the request.

                .. data:: stable = 1

                .. data:: removing = 2

                """

                stable = Enum.YLeaf(1, "stable")

                removing = Enum.YLeaf(2, "removing")


            class Ringstationconfigcontrolupdatestats(Enum):
                """
                Ringstationconfigcontrolupdatestats (Enum Class)

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



    class Ringstationconfigtable(Entity):
        """
        A list of configuration entries for stations on a
        ring monitored by this probe.
        
        .. attribute:: ringstationconfigentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this probe
        	**type**\: list of  		 :py:class:`Ringstationconfigentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Ringstationconfigtable.Ringstationconfigentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Ringstationconfigtable, self).__init__()

            self.yang_name = "ringStationConfigTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ringStationConfigEntry", ("ringstationconfigentry", TOKENRINGRMONMIB.Ringstationconfigtable.Ringstationconfigentry))])
            self._leafs = OrderedDict()

            self.ringstationconfigentry = YList(self)
            self._segment_path = lambda: "ringStationConfigTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Ringstationconfigtable, [], name, value)


        class Ringstationconfigentry(Entity):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this probe.
            
            .. attribute:: ringstationconfigifindex  (key)
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationconfigmacaddress  (key)
            
            	The physical address of this station
            	**type**\: str
            
            	**length:** 6
            
            .. attribute:: ringstationconfigupdatetime
            
            	The value of sysUpTime at the time this configuration information was last updated (completely)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationconfiglocation
            
            	The assigned physical location of this station
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: ringstationconfigmicrocode
            
            	The microcode EC level of this station
            	**type**\: str
            
            	**length:** 10
            
            .. attribute:: ringstationconfiggroupaddress
            
            	The low\-order 4 octets of the group address recognized by this station
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: ringstationconfigfunctionaladdress
            
            	the functional addresses recognized by this station
            	**type**\: str
            
            	**length:** 4
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Ringstationconfigtable.Ringstationconfigentry, self).__init__()

                self.yang_name = "ringStationConfigEntry"
                self.yang_parent_name = "ringStationConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ringstationconfigifindex','ringstationconfigmacaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ringstationconfigifindex', YLeaf(YType.int32, 'ringStationConfigIfIndex')),
                    ('ringstationconfigmacaddress', YLeaf(YType.str, 'ringStationConfigMacAddress')),
                    ('ringstationconfigupdatetime', YLeaf(YType.uint32, 'ringStationConfigUpdateTime')),
                    ('ringstationconfiglocation', YLeaf(YType.str, 'ringStationConfigLocation')),
                    ('ringstationconfigmicrocode', YLeaf(YType.str, 'ringStationConfigMicrocode')),
                    ('ringstationconfiggroupaddress', YLeaf(YType.str, 'ringStationConfigGroupAddress')),
                    ('ringstationconfigfunctionaladdress', YLeaf(YType.str, 'ringStationConfigFunctionalAddress')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Ringstationconfigtable.Ringstationconfigentry, ['ringstationconfigifindex', 'ringstationconfigmacaddress', 'ringstationconfigupdatetime', 'ringstationconfiglocation', 'ringstationconfigmicrocode', 'ringstationconfiggroupaddress', 'ringstationconfigfunctionaladdress'], name, value)


    class Sourceroutingstatstable(Entity):
        """
        A list of source routing statistics entries.
        
        .. attribute:: sourceroutingstatsentry
        
        	A collection of source routing statistics kept for a particular Token Ring interface
        	**type**\: list of  		 :py:class:`Sourceroutingstatsentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.Sourceroutingstatstable.Sourceroutingstatsentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TOKENRINGRMONMIB.Sourceroutingstatstable, self).__init__()

            self.yang_name = "sourceRoutingStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sourceRoutingStatsEntry", ("sourceroutingstatsentry", TOKENRINGRMONMIB.Sourceroutingstatstable.Sourceroutingstatsentry))])
            self._leafs = OrderedDict()

            self.sourceroutingstatsentry = YList(self)
            self._segment_path = lambda: "sourceRoutingStatsTable"
            self._absolute_path = lambda: "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGRMONMIB.Sourceroutingstatstable, [], name, value)


        class Sourceroutingstatsentry(Entity):
            """
            A collection of source routing statistics kept
            for a particular Token Ring interface.
            
            .. attribute:: sourceroutingstatsifindex  (key)
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which source routing statistics will be detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sourceroutingstatsringnumber
            
            	The ring number of the ring monitored by this entry.  When any object in this entry is created, the probe will attempt to discover the ring number.  Only after the ring number is discovered will this object be created.  After creating an object in this entry, the management station should poll this object to detect when it is created.  Only after this object is created can the management station set the sourceRoutingStatsStatus entry to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sourceroutingstatsinframes
            
            	The count of frames sent into this ring from another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsoutframes
            
            	The count of frames sent from this ring to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsthroughframes
            
            	The count of frames sent from another ring, through this ring, to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsallroutesbroadcastframes
            
            	The total number of good frames received that were All Routes Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatssingleroutebroadcastframes
            
            	The total number of good frames received that were Single Route Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsinoctets
            
            	The count of octets in good frames sent into this ring from another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsoutoctets
            
            	The count of octets in good frames sent from this ring to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsthroughoctets
            
            	The count of octets in good frames sent another ring, through this ring, to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsallroutesbroadcastoctets
            
            	The total number of octets in good frames received that were All Routes Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatssingleroutesbroadcastoctets
            
            	The total number of octets in good frames received that were Single Route Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatslocalllcframes
            
            	The total number of frames received who had no RIF field (or had a RIF field that only included the local ring's number) and were not All Route Broadcast Frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats1hopframes
            
            	The total number of frames received whose route had 1 hop, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats2hopsframes
            
            	The total number of frames received whose route had 2 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats3hopsframes
            
            	The total number of frames received whose route had 3 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats4hopsframes
            
            	The total number of frames received whose route had 4 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats5hopsframes
            
            	The total number of frames received whose route had 5 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats6hopsframes
            
            	The total number of frames received whose route had 6 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats7hopsframes
            
            	The total number of frames received whose route had 7 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats8hopsframes
            
            	The total number of frames received whose route had 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsmorethan8hopsframes
            
            	The total number of frames received whose route had more than 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: sourceroutingstatsstatus
            
            	The status of this sourceRoutingStats entry
            	**type**\:  :py:class:`EntryStatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.EntryStatus>`
            
            .. attribute:: sourceroutingstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TOKENRINGRMONMIB.Sourceroutingstatstable.Sourceroutingstatsentry, self).__init__()

                self.yang_name = "sourceRoutingStatsEntry"
                self.yang_parent_name = "sourceRoutingStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sourceroutingstatsifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sourceroutingstatsifindex', YLeaf(YType.int32, 'sourceRoutingStatsIfIndex')),
                    ('sourceroutingstatsringnumber', YLeaf(YType.int32, 'sourceRoutingStatsRingNumber')),
                    ('sourceroutingstatsinframes', YLeaf(YType.uint32, 'sourceRoutingStatsInFrames')),
                    ('sourceroutingstatsoutframes', YLeaf(YType.uint32, 'sourceRoutingStatsOutFrames')),
                    ('sourceroutingstatsthroughframes', YLeaf(YType.uint32, 'sourceRoutingStatsThroughFrames')),
                    ('sourceroutingstatsallroutesbroadcastframes', YLeaf(YType.uint32, 'sourceRoutingStatsAllRoutesBroadcastFrames')),
                    ('sourceroutingstatssingleroutebroadcastframes', YLeaf(YType.uint32, 'sourceRoutingStatsSingleRouteBroadcastFrames')),
                    ('sourceroutingstatsinoctets', YLeaf(YType.uint32, 'sourceRoutingStatsInOctets')),
                    ('sourceroutingstatsoutoctets', YLeaf(YType.uint32, 'sourceRoutingStatsOutOctets')),
                    ('sourceroutingstatsthroughoctets', YLeaf(YType.uint32, 'sourceRoutingStatsThroughOctets')),
                    ('sourceroutingstatsallroutesbroadcastoctets', YLeaf(YType.uint32, 'sourceRoutingStatsAllRoutesBroadcastOctets')),
                    ('sourceroutingstatssingleroutesbroadcastoctets', YLeaf(YType.uint32, 'sourceRoutingStatsSingleRoutesBroadcastOctets')),
                    ('sourceroutingstatslocalllcframes', YLeaf(YType.uint32, 'sourceRoutingStatsLocalLLCFrames')),
                    ('sourceroutingstats1hopframes', YLeaf(YType.uint32, 'sourceRoutingStats1HopFrames')),
                    ('sourceroutingstats2hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats2HopsFrames')),
                    ('sourceroutingstats3hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats3HopsFrames')),
                    ('sourceroutingstats4hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats4HopsFrames')),
                    ('sourceroutingstats5hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats5HopsFrames')),
                    ('sourceroutingstats6hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats6HopsFrames')),
                    ('sourceroutingstats7hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats7HopsFrames')),
                    ('sourceroutingstats8hopsframes', YLeaf(YType.uint32, 'sourceRoutingStats8HopsFrames')),
                    ('sourceroutingstatsmorethan8hopsframes', YLeaf(YType.uint32, 'sourceRoutingStatsMoreThan8HopsFrames')),
                    ('sourceroutingstatsowner', YLeaf(YType.str, 'sourceRoutingStatsOwner')),
                    ('sourceroutingstatsstatus', YLeaf(YType.enumeration, 'sourceRoutingStatsStatus')),
                    ('sourceroutingstatsdroppedframes', YLeaf(YType.uint32, 'RMON2-MIB:sourceRoutingStatsDroppedFrames')),
                    ('sourceroutingstatscreatetime', YLeaf(YType.uint32, 'RMON2-MIB:sourceRoutingStatsCreateTime')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGRMONMIB.Sourceroutingstatstable.Sourceroutingstatsentry, ['sourceroutingstatsifindex', 'sourceroutingstatsringnumber', 'sourceroutingstatsinframes', 'sourceroutingstatsoutframes', 'sourceroutingstatsthroughframes', 'sourceroutingstatsallroutesbroadcastframes', 'sourceroutingstatssingleroutebroadcastframes', 'sourceroutingstatsinoctets', 'sourceroutingstatsoutoctets', 'sourceroutingstatsthroughoctets', 'sourceroutingstatsallroutesbroadcastoctets', 'sourceroutingstatssingleroutesbroadcastoctets', 'sourceroutingstatslocalllcframes', 'sourceroutingstats1hopframes', 'sourceroutingstats2hopsframes', 'sourceroutingstats3hopsframes', 'sourceroutingstats4hopsframes', 'sourceroutingstats5hopsframes', 'sourceroutingstats6hopsframes', 'sourceroutingstats7hopsframes', 'sourceroutingstats8hopsframes', 'sourceroutingstatsmorethan8hopsframes', 'sourceroutingstatsowner', 'sourceroutingstatsstatus', 'sourceroutingstatsdroppedframes', 'sourceroutingstatscreatetime'], name, value)

    def clone_ptr(self):
        self._top_entity = TOKENRINGRMONMIB()
        return self._top_entity

