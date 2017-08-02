""" TOKEN_RING_RMON_MIB 


"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Entrystatus(Enum):
    """
    Entrystatus

    .. data:: valid = 1

    .. data:: createRequest = 2

    .. data:: underCreation = 3

    .. data:: invalid = 4

    """

    valid = Enum.YLeaf(1, "valid")

    createRequest = Enum.YLeaf(2, "createRequest")

    underCreation = Enum.YLeaf(3, "underCreation")

    invalid = Enum.YLeaf(4, "invalid")



class TokenRingRmonMib(Entity):
    """
    
    
    .. attribute:: ringstationconfigcontroltable
    
    	A list of ring station configuration control entries
    	**type**\:   :py:class:`Ringstationconfigcontroltable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationconfigcontroltable>`
    
    .. attribute:: ringstationconfigtable
    
    	A list of configuration entries for stations on a ring monitored by this probe
    	**type**\:   :py:class:`Ringstationconfigtable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationconfigtable>`
    
    .. attribute:: ringstationcontroltable
    
    	A list of ringStation table control entries
    	**type**\:   :py:class:`Ringstationcontroltable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationcontroltable>`
    
    .. attribute:: ringstationordertable
    
    	A list of ring station entries for stations in the ring poll, ordered by their ring\-order
    	**type**\:   :py:class:`Ringstationordertable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationordertable>`
    
    .. attribute:: ringstationtable
    
    	A list of ring station entries.  An entry will exist for each station that is now or has      previously been detected as physically present on this ring
    	**type**\:   :py:class:`Ringstationtable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationtable>`
    
    .. attribute:: sourceroutingstatstable
    
    	A list of source routing statistics entries
    	**type**\:   :py:class:`Sourceroutingstatstable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Sourceroutingstatstable>`
    
    .. attribute:: tokenringmlhistorytable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\:   :py:class:`Tokenringmlhistorytable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringmlhistorytable>`
    
    .. attribute:: tokenringmlstatstable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\:   :py:class:`Tokenringmlstatstable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringmlstatstable>`
    
    .. attribute:: tokenringphistorytable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\:   :py:class:`Tokenringphistorytable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringphistorytable>`
    
    .. attribute:: tokenringpstatstable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\:   :py:class:`Tokenringpstatstable <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringpstatstable>`
    
    

    """

    _prefix = 'TOKEN-RING-RMON-MIB'

    def __init__(self):
        super(TokenRingRmonMib, self).__init__()
        self._top_entity = None

        self.yang_name = "TOKEN-RING-RMON-MIB"
        self.yang_parent_name = "TOKEN-RING-RMON-MIB"

        self.ringstationconfigcontroltable = TokenRingRmonMib.Ringstationconfigcontroltable()
        self.ringstationconfigcontroltable.parent = self
        self._children_name_map["ringstationconfigcontroltable"] = "ringStationConfigControlTable"
        self._children_yang_names.add("ringStationConfigControlTable")

        self.ringstationconfigtable = TokenRingRmonMib.Ringstationconfigtable()
        self.ringstationconfigtable.parent = self
        self._children_name_map["ringstationconfigtable"] = "ringStationConfigTable"
        self._children_yang_names.add("ringStationConfigTable")

        self.ringstationcontroltable = TokenRingRmonMib.Ringstationcontroltable()
        self.ringstationcontroltable.parent = self
        self._children_name_map["ringstationcontroltable"] = "ringStationControlTable"
        self._children_yang_names.add("ringStationControlTable")

        self.ringstationordertable = TokenRingRmonMib.Ringstationordertable()
        self.ringstationordertable.parent = self
        self._children_name_map["ringstationordertable"] = "ringStationOrderTable"
        self._children_yang_names.add("ringStationOrderTable")

        self.ringstationtable = TokenRingRmonMib.Ringstationtable()
        self.ringstationtable.parent = self
        self._children_name_map["ringstationtable"] = "ringStationTable"
        self._children_yang_names.add("ringStationTable")

        self.sourceroutingstatstable = TokenRingRmonMib.Sourceroutingstatstable()
        self.sourceroutingstatstable.parent = self
        self._children_name_map["sourceroutingstatstable"] = "sourceRoutingStatsTable"
        self._children_yang_names.add("sourceRoutingStatsTable")

        self.tokenringmlhistorytable = TokenRingRmonMib.Tokenringmlhistorytable()
        self.tokenringmlhistorytable.parent = self
        self._children_name_map["tokenringmlhistorytable"] = "tokenRingMLHistoryTable"
        self._children_yang_names.add("tokenRingMLHistoryTable")

        self.tokenringmlstatstable = TokenRingRmonMib.Tokenringmlstatstable()
        self.tokenringmlstatstable.parent = self
        self._children_name_map["tokenringmlstatstable"] = "tokenRingMLStatsTable"
        self._children_yang_names.add("tokenRingMLStatsTable")

        self.tokenringphistorytable = TokenRingRmonMib.Tokenringphistorytable()
        self.tokenringphistorytable.parent = self
        self._children_name_map["tokenringphistorytable"] = "tokenRingPHistoryTable"
        self._children_yang_names.add("tokenRingPHistoryTable")

        self.tokenringpstatstable = TokenRingRmonMib.Tokenringpstatstable()
        self.tokenringpstatstable.parent = self
        self._children_name_map["tokenringpstatstable"] = "tokenRingPStatsTable"
        self._children_yang_names.add("tokenRingPStatsTable")


    class Tokenringmlstatstable(Entity):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlstatsentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of    :py:class:`Tokenringmlstatsentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Tokenringmlstatstable, self).__init__()

            self.yang_name = "tokenRingMLStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.tokenringmlstatsentry = YList(self)

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
                        super(TokenRingRmonMib.Tokenringmlstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Tokenringmlstatstable, self).__setattr__(name, value)


        class Tokenringmlstatsentry(Entity):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlstatsindex  <key>
            
            	The value of this object uniquely identifies this tokenRingMLStats entry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringmlstatsaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsacerrors
            
            	The total number of AC (Address Copied)  errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState,      beaconSetRecoveryModeState, or beaconRingSignalLossState) from a non\-beaconing state.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeaconpkts
            
            	The total number of beacon MAC packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeacontime
            
            	The total amount of time that the ring has been in the beaconing state
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlstatsbursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state.  The claim token state that comes in response to a beacon state is not counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatscongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsdatasource
            
            	This object identifies the source of the data that this tokenRingMLStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all error reports on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingMLStatsStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: tokenringmlstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingPStatsDropEvents
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatslineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatslostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsmacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsmacpkts
            
            	The total number of MAC packets (excluding packets that were not good frames) received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsnaunchanges
            
            	The total number of NAUN changes detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            .. attribute:: tokenringmlstatsringpollevents
            
            	The total number of ring poll events detected by the probe (i.e. the number of ring polls initiated by the active monitor that were detected)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpurgeevents
            
            	The total number of times that the ring enters the ring purge state from normal ring state.  The ring purge state that comes in response to the claim token or beacon state is not counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpurgepkts
            
            	The total number of ring purge MAC packets detected by probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatssofterrorreports
            
            	The total number of soft error report frames detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsstatus
            
            	The status of this tokenRingMLStats entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.Entrystatus>`
            
            .. attribute:: tokenringmlstatstokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry, self).__init__()

                self.yang_name = "tokenRingMLStatsEntry"
                self.yang_parent_name = "tokenRingMLStatsTable"

                self.tokenringmlstatsindex = YLeaf(YType.int32, "tokenRingMLStatsIndex")

                self.tokenringmlstatsaborterrors = YLeaf(YType.uint32, "tokenRingMLStatsAbortErrors")

                self.tokenringmlstatsacerrors = YLeaf(YType.uint32, "tokenRingMLStatsACErrors")

                self.tokenringmlstatsbeaconevents = YLeaf(YType.uint32, "tokenRingMLStatsBeaconEvents")

                self.tokenringmlstatsbeaconpkts = YLeaf(YType.uint32, "tokenRingMLStatsBeaconPkts")

                self.tokenringmlstatsbeacontime = YLeaf(YType.int32, "tokenRingMLStatsBeaconTime")

                self.tokenringmlstatsbursterrors = YLeaf(YType.uint32, "tokenRingMLStatsBurstErrors")

                self.tokenringmlstatsclaimtokenevents = YLeaf(YType.uint32, "tokenRingMLStatsClaimTokenEvents")

                self.tokenringmlstatsclaimtokenpkts = YLeaf(YType.uint32, "tokenRingMLStatsClaimTokenPkts")

                self.tokenringmlstatscongestionerrors = YLeaf(YType.uint32, "tokenRingMLStatsCongestionErrors")

                self.tokenringmlstatscreatetime = YLeaf(YType.uint32, "RMON2-MIB:tokenRingMLStatsCreateTime")

                self.tokenringmlstatsdatasource = YLeaf(YType.str, "tokenRingMLStatsDataSource")

                self.tokenringmlstatsdropevents = YLeaf(YType.uint32, "tokenRingMLStatsDropEvents")

                self.tokenringmlstatsdroppedframes = YLeaf(YType.uint32, "RMON2-MIB:tokenRingMLStatsDroppedFrames")

                self.tokenringmlstatsframecopiederrors = YLeaf(YType.uint32, "tokenRingMLStatsFrameCopiedErrors")

                self.tokenringmlstatsfrequencyerrors = YLeaf(YType.uint32, "tokenRingMLStatsFrequencyErrors")

                self.tokenringmlstatsinternalerrors = YLeaf(YType.uint32, "tokenRingMLStatsInternalErrors")

                self.tokenringmlstatslineerrors = YLeaf(YType.uint32, "tokenRingMLStatsLineErrors")

                self.tokenringmlstatslostframeerrors = YLeaf(YType.uint32, "tokenRingMLStatsLostFrameErrors")

                self.tokenringmlstatsmacoctets = YLeaf(YType.uint32, "tokenRingMLStatsMacOctets")

                self.tokenringmlstatsmacpkts = YLeaf(YType.uint32, "tokenRingMLStatsMacPkts")

                self.tokenringmlstatsnaunchanges = YLeaf(YType.uint32, "tokenRingMLStatsNAUNChanges")

                self.tokenringmlstatsowner = YLeaf(YType.str, "tokenRingMLStatsOwner")

                self.tokenringmlstatsringpollevents = YLeaf(YType.uint32, "tokenRingMLStatsRingPollEvents")

                self.tokenringmlstatsringpurgeevents = YLeaf(YType.uint32, "tokenRingMLStatsRingPurgeEvents")

                self.tokenringmlstatsringpurgepkts = YLeaf(YType.uint32, "tokenRingMLStatsRingPurgePkts")

                self.tokenringmlstatssofterrorreports = YLeaf(YType.uint32, "tokenRingMLStatsSoftErrorReports")

                self.tokenringmlstatsstatus = YLeaf(YType.enumeration, "tokenRingMLStatsStatus")

                self.tokenringmlstatstokenerrors = YLeaf(YType.uint32, "tokenRingMLStatsTokenErrors")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tokenringmlstatsindex",
                                "tokenringmlstatsaborterrors",
                                "tokenringmlstatsacerrors",
                                "tokenringmlstatsbeaconevents",
                                "tokenringmlstatsbeaconpkts",
                                "tokenringmlstatsbeacontime",
                                "tokenringmlstatsbursterrors",
                                "tokenringmlstatsclaimtokenevents",
                                "tokenringmlstatsclaimtokenpkts",
                                "tokenringmlstatscongestionerrors",
                                "tokenringmlstatscreatetime",
                                "tokenringmlstatsdatasource",
                                "tokenringmlstatsdropevents",
                                "tokenringmlstatsdroppedframes",
                                "tokenringmlstatsframecopiederrors",
                                "tokenringmlstatsfrequencyerrors",
                                "tokenringmlstatsinternalerrors",
                                "tokenringmlstatslineerrors",
                                "tokenringmlstatslostframeerrors",
                                "tokenringmlstatsmacoctets",
                                "tokenringmlstatsmacpkts",
                                "tokenringmlstatsnaunchanges",
                                "tokenringmlstatsowner",
                                "tokenringmlstatsringpollevents",
                                "tokenringmlstatsringpurgeevents",
                                "tokenringmlstatsringpurgepkts",
                                "tokenringmlstatssofterrorreports",
                                "tokenringmlstatsstatus",
                                "tokenringmlstatstokenerrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tokenringmlstatsindex.is_set or
                    self.tokenringmlstatsaborterrors.is_set or
                    self.tokenringmlstatsacerrors.is_set or
                    self.tokenringmlstatsbeaconevents.is_set or
                    self.tokenringmlstatsbeaconpkts.is_set or
                    self.tokenringmlstatsbeacontime.is_set or
                    self.tokenringmlstatsbursterrors.is_set or
                    self.tokenringmlstatsclaimtokenevents.is_set or
                    self.tokenringmlstatsclaimtokenpkts.is_set or
                    self.tokenringmlstatscongestionerrors.is_set or
                    self.tokenringmlstatscreatetime.is_set or
                    self.tokenringmlstatsdatasource.is_set or
                    self.tokenringmlstatsdropevents.is_set or
                    self.tokenringmlstatsdroppedframes.is_set or
                    self.tokenringmlstatsframecopiederrors.is_set or
                    self.tokenringmlstatsfrequencyerrors.is_set or
                    self.tokenringmlstatsinternalerrors.is_set or
                    self.tokenringmlstatslineerrors.is_set or
                    self.tokenringmlstatslostframeerrors.is_set or
                    self.tokenringmlstatsmacoctets.is_set or
                    self.tokenringmlstatsmacpkts.is_set or
                    self.tokenringmlstatsnaunchanges.is_set or
                    self.tokenringmlstatsowner.is_set or
                    self.tokenringmlstatsringpollevents.is_set or
                    self.tokenringmlstatsringpurgeevents.is_set or
                    self.tokenringmlstatsringpurgepkts.is_set or
                    self.tokenringmlstatssofterrorreports.is_set or
                    self.tokenringmlstatsstatus.is_set or
                    self.tokenringmlstatstokenerrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tokenringmlstatsindex.yfilter != YFilter.not_set or
                    self.tokenringmlstatsaborterrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatsacerrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatsbeaconevents.yfilter != YFilter.not_set or
                    self.tokenringmlstatsbeaconpkts.yfilter != YFilter.not_set or
                    self.tokenringmlstatsbeacontime.yfilter != YFilter.not_set or
                    self.tokenringmlstatsbursterrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatsclaimtokenevents.yfilter != YFilter.not_set or
                    self.tokenringmlstatsclaimtokenpkts.yfilter != YFilter.not_set or
                    self.tokenringmlstatscongestionerrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatscreatetime.yfilter != YFilter.not_set or
                    self.tokenringmlstatsdatasource.yfilter != YFilter.not_set or
                    self.tokenringmlstatsdropevents.yfilter != YFilter.not_set or
                    self.tokenringmlstatsdroppedframes.yfilter != YFilter.not_set or
                    self.tokenringmlstatsframecopiederrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatsfrequencyerrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatsinternalerrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatslineerrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatslostframeerrors.yfilter != YFilter.not_set or
                    self.tokenringmlstatsmacoctets.yfilter != YFilter.not_set or
                    self.tokenringmlstatsmacpkts.yfilter != YFilter.not_set or
                    self.tokenringmlstatsnaunchanges.yfilter != YFilter.not_set or
                    self.tokenringmlstatsowner.yfilter != YFilter.not_set or
                    self.tokenringmlstatsringpollevents.yfilter != YFilter.not_set or
                    self.tokenringmlstatsringpurgeevents.yfilter != YFilter.not_set or
                    self.tokenringmlstatsringpurgepkts.yfilter != YFilter.not_set or
                    self.tokenringmlstatssofterrorreports.yfilter != YFilter.not_set or
                    self.tokenringmlstatsstatus.yfilter != YFilter.not_set or
                    self.tokenringmlstatstokenerrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tokenRingMLStatsEntry" + "[tokenRingMLStatsIndex='" + self.tokenringmlstatsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingMLStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tokenringmlstatsindex.is_set or self.tokenringmlstatsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsindex.get_name_leafdata())
                if (self.tokenringmlstatsaborterrors.is_set or self.tokenringmlstatsaborterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsaborterrors.get_name_leafdata())
                if (self.tokenringmlstatsacerrors.is_set or self.tokenringmlstatsacerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsacerrors.get_name_leafdata())
                if (self.tokenringmlstatsbeaconevents.is_set or self.tokenringmlstatsbeaconevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsbeaconevents.get_name_leafdata())
                if (self.tokenringmlstatsbeaconpkts.is_set or self.tokenringmlstatsbeaconpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsbeaconpkts.get_name_leafdata())
                if (self.tokenringmlstatsbeacontime.is_set or self.tokenringmlstatsbeacontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsbeacontime.get_name_leafdata())
                if (self.tokenringmlstatsbursterrors.is_set or self.tokenringmlstatsbursterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsbursterrors.get_name_leafdata())
                if (self.tokenringmlstatsclaimtokenevents.is_set or self.tokenringmlstatsclaimtokenevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsclaimtokenevents.get_name_leafdata())
                if (self.tokenringmlstatsclaimtokenpkts.is_set or self.tokenringmlstatsclaimtokenpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsclaimtokenpkts.get_name_leafdata())
                if (self.tokenringmlstatscongestionerrors.is_set or self.tokenringmlstatscongestionerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatscongestionerrors.get_name_leafdata())
                if (self.tokenringmlstatscreatetime.is_set or self.tokenringmlstatscreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatscreatetime.get_name_leafdata())
                if (self.tokenringmlstatsdatasource.is_set or self.tokenringmlstatsdatasource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsdatasource.get_name_leafdata())
                if (self.tokenringmlstatsdropevents.is_set or self.tokenringmlstatsdropevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsdropevents.get_name_leafdata())
                if (self.tokenringmlstatsdroppedframes.is_set or self.tokenringmlstatsdroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsdroppedframes.get_name_leafdata())
                if (self.tokenringmlstatsframecopiederrors.is_set or self.tokenringmlstatsframecopiederrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsframecopiederrors.get_name_leafdata())
                if (self.tokenringmlstatsfrequencyerrors.is_set or self.tokenringmlstatsfrequencyerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsfrequencyerrors.get_name_leafdata())
                if (self.tokenringmlstatsinternalerrors.is_set or self.tokenringmlstatsinternalerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsinternalerrors.get_name_leafdata())
                if (self.tokenringmlstatslineerrors.is_set or self.tokenringmlstatslineerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatslineerrors.get_name_leafdata())
                if (self.tokenringmlstatslostframeerrors.is_set or self.tokenringmlstatslostframeerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatslostframeerrors.get_name_leafdata())
                if (self.tokenringmlstatsmacoctets.is_set or self.tokenringmlstatsmacoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsmacoctets.get_name_leafdata())
                if (self.tokenringmlstatsmacpkts.is_set or self.tokenringmlstatsmacpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsmacpkts.get_name_leafdata())
                if (self.tokenringmlstatsnaunchanges.is_set or self.tokenringmlstatsnaunchanges.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsnaunchanges.get_name_leafdata())
                if (self.tokenringmlstatsowner.is_set or self.tokenringmlstatsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsowner.get_name_leafdata())
                if (self.tokenringmlstatsringpollevents.is_set or self.tokenringmlstatsringpollevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsringpollevents.get_name_leafdata())
                if (self.tokenringmlstatsringpurgeevents.is_set or self.tokenringmlstatsringpurgeevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsringpurgeevents.get_name_leafdata())
                if (self.tokenringmlstatsringpurgepkts.is_set or self.tokenringmlstatsringpurgepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsringpurgepkts.get_name_leafdata())
                if (self.tokenringmlstatssofterrorreports.is_set or self.tokenringmlstatssofterrorreports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatssofterrorreports.get_name_leafdata())
                if (self.tokenringmlstatsstatus.is_set or self.tokenringmlstatsstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatsstatus.get_name_leafdata())
                if (self.tokenringmlstatstokenerrors.is_set or self.tokenringmlstatstokenerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlstatstokenerrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tokenRingMLStatsIndex" or name == "tokenRingMLStatsAbortErrors" or name == "tokenRingMLStatsACErrors" or name == "tokenRingMLStatsBeaconEvents" or name == "tokenRingMLStatsBeaconPkts" or name == "tokenRingMLStatsBeaconTime" or name == "tokenRingMLStatsBurstErrors" or name == "tokenRingMLStatsClaimTokenEvents" or name == "tokenRingMLStatsClaimTokenPkts" or name == "tokenRingMLStatsCongestionErrors" or name == "tokenRingMLStatsCreateTime" or name == "tokenRingMLStatsDataSource" or name == "tokenRingMLStatsDropEvents" or name == "tokenRingMLStatsDroppedFrames" or name == "tokenRingMLStatsFrameCopiedErrors" or name == "tokenRingMLStatsFrequencyErrors" or name == "tokenRingMLStatsInternalErrors" or name == "tokenRingMLStatsLineErrors" or name == "tokenRingMLStatsLostFrameErrors" or name == "tokenRingMLStatsMacOctets" or name == "tokenRingMLStatsMacPkts" or name == "tokenRingMLStatsNAUNChanges" or name == "tokenRingMLStatsOwner" or name == "tokenRingMLStatsRingPollEvents" or name == "tokenRingMLStatsRingPurgeEvents" or name == "tokenRingMLStatsRingPurgePkts" or name == "tokenRingMLStatsSoftErrorReports" or name == "tokenRingMLStatsStatus" or name == "tokenRingMLStatsTokenErrors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tokenRingMLStatsIndex"):
                    self.tokenringmlstatsindex = value
                    self.tokenringmlstatsindex.value_namespace = name_space
                    self.tokenringmlstatsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsAbortErrors"):
                    self.tokenringmlstatsaborterrors = value
                    self.tokenringmlstatsaborterrors.value_namespace = name_space
                    self.tokenringmlstatsaborterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsACErrors"):
                    self.tokenringmlstatsacerrors = value
                    self.tokenringmlstatsacerrors.value_namespace = name_space
                    self.tokenringmlstatsacerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsBeaconEvents"):
                    self.tokenringmlstatsbeaconevents = value
                    self.tokenringmlstatsbeaconevents.value_namespace = name_space
                    self.tokenringmlstatsbeaconevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsBeaconPkts"):
                    self.tokenringmlstatsbeaconpkts = value
                    self.tokenringmlstatsbeaconpkts.value_namespace = name_space
                    self.tokenringmlstatsbeaconpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsBeaconTime"):
                    self.tokenringmlstatsbeacontime = value
                    self.tokenringmlstatsbeacontime.value_namespace = name_space
                    self.tokenringmlstatsbeacontime.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsBurstErrors"):
                    self.tokenringmlstatsbursterrors = value
                    self.tokenringmlstatsbursterrors.value_namespace = name_space
                    self.tokenringmlstatsbursterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsClaimTokenEvents"):
                    self.tokenringmlstatsclaimtokenevents = value
                    self.tokenringmlstatsclaimtokenevents.value_namespace = name_space
                    self.tokenringmlstatsclaimtokenevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsClaimTokenPkts"):
                    self.tokenringmlstatsclaimtokenpkts = value
                    self.tokenringmlstatsclaimtokenpkts.value_namespace = name_space
                    self.tokenringmlstatsclaimtokenpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsCongestionErrors"):
                    self.tokenringmlstatscongestionerrors = value
                    self.tokenringmlstatscongestionerrors.value_namespace = name_space
                    self.tokenringmlstatscongestionerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsCreateTime"):
                    self.tokenringmlstatscreatetime = value
                    self.tokenringmlstatscreatetime.value_namespace = name_space
                    self.tokenringmlstatscreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsDataSource"):
                    self.tokenringmlstatsdatasource = value
                    self.tokenringmlstatsdatasource.value_namespace = name_space
                    self.tokenringmlstatsdatasource.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsDropEvents"):
                    self.tokenringmlstatsdropevents = value
                    self.tokenringmlstatsdropevents.value_namespace = name_space
                    self.tokenringmlstatsdropevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsDroppedFrames"):
                    self.tokenringmlstatsdroppedframes = value
                    self.tokenringmlstatsdroppedframes.value_namespace = name_space
                    self.tokenringmlstatsdroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsFrameCopiedErrors"):
                    self.tokenringmlstatsframecopiederrors = value
                    self.tokenringmlstatsframecopiederrors.value_namespace = name_space
                    self.tokenringmlstatsframecopiederrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsFrequencyErrors"):
                    self.tokenringmlstatsfrequencyerrors = value
                    self.tokenringmlstatsfrequencyerrors.value_namespace = name_space
                    self.tokenringmlstatsfrequencyerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsInternalErrors"):
                    self.tokenringmlstatsinternalerrors = value
                    self.tokenringmlstatsinternalerrors.value_namespace = name_space
                    self.tokenringmlstatsinternalerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsLineErrors"):
                    self.tokenringmlstatslineerrors = value
                    self.tokenringmlstatslineerrors.value_namespace = name_space
                    self.tokenringmlstatslineerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsLostFrameErrors"):
                    self.tokenringmlstatslostframeerrors = value
                    self.tokenringmlstatslostframeerrors.value_namespace = name_space
                    self.tokenringmlstatslostframeerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsMacOctets"):
                    self.tokenringmlstatsmacoctets = value
                    self.tokenringmlstatsmacoctets.value_namespace = name_space
                    self.tokenringmlstatsmacoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsMacPkts"):
                    self.tokenringmlstatsmacpkts = value
                    self.tokenringmlstatsmacpkts.value_namespace = name_space
                    self.tokenringmlstatsmacpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsNAUNChanges"):
                    self.tokenringmlstatsnaunchanges = value
                    self.tokenringmlstatsnaunchanges.value_namespace = name_space
                    self.tokenringmlstatsnaunchanges.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsOwner"):
                    self.tokenringmlstatsowner = value
                    self.tokenringmlstatsowner.value_namespace = name_space
                    self.tokenringmlstatsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsRingPollEvents"):
                    self.tokenringmlstatsringpollevents = value
                    self.tokenringmlstatsringpollevents.value_namespace = name_space
                    self.tokenringmlstatsringpollevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsRingPurgeEvents"):
                    self.tokenringmlstatsringpurgeevents = value
                    self.tokenringmlstatsringpurgeevents.value_namespace = name_space
                    self.tokenringmlstatsringpurgeevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsRingPurgePkts"):
                    self.tokenringmlstatsringpurgepkts = value
                    self.tokenringmlstatsringpurgepkts.value_namespace = name_space
                    self.tokenringmlstatsringpurgepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsSoftErrorReports"):
                    self.tokenringmlstatssofterrorreports = value
                    self.tokenringmlstatssofterrorreports.value_namespace = name_space
                    self.tokenringmlstatssofterrorreports.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsStatus"):
                    self.tokenringmlstatsstatus = value
                    self.tokenringmlstatsstatus.value_namespace = name_space
                    self.tokenringmlstatsstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLStatsTokenErrors"):
                    self.tokenringmlstatstokenerrors = value
                    self.tokenringmlstatstokenerrors.value_namespace = name_space
                    self.tokenringmlstatstokenerrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tokenringmlstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tokenringmlstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tokenRingMLStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tokenRingMLStatsEntry"):
                for c in self.tokenringmlstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Tokenringmlstatstable.Tokenringmlstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tokenringmlstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tokenRingMLStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tokenringpstatstable(Entity):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringpstatsentry
        
        	A collection of promiscuous statistics kept for non\-MAC packets on a particular Token Ring interface
        	**type**\: list of    :py:class:`Tokenringpstatsentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Tokenringpstatstable, self).__init__()

            self.yang_name = "tokenRingPStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.tokenringpstatsentry = YList(self)

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
                        super(TokenRingRmonMib.Tokenringpstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Tokenringpstatstable, self).__setattr__(name, value)


        class Tokenringpstatsentry(Entity):
            """
            A collection of promiscuous statistics kept for
            non\-MAC packets on a particular Token Ring
            interface.
            
            .. attribute:: tokenringpstatsindex  <key>
            
            	The value of this object uniquely identifies this tokenRingPStats entry
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringpstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatabroadcastpkts
            
            	The total number of good non\-MAC frames received that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatamulticastpkts
            
            	The total number of good non\-MAC frames received that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts
            
            	The total number of non\-MAC packets in good frames.  received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts128to255octets
            
            	The total number of good non\-MAC frames received that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts18to63octets
            
            	The total number of good non\-MAC frames received that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts256to511octets
            
            	The total number of good non\-MAC frames received that were between 256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts512to1023octets
            
            	The total number of good non\-MAC frames received that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts64to127octets
            
            	The total number of good non\-MAC frames received that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatasource
            
            	This object identifies the source of the data that this tokenRingPStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all non\-MAC packets on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingPStatsStatus object is equal to valid(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: tokenringpstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingMLStatsDropEvents
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            .. attribute:: tokenringpstatsstatus
            
            	The status of this tokenRingPStats entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.Entrystatus>`
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry, self).__init__()

                self.yang_name = "tokenRingPStatsEntry"
                self.yang_parent_name = "tokenRingPStatsTable"

                self.tokenringpstatsindex = YLeaf(YType.int32, "tokenRingPStatsIndex")

                self.tokenringpstatscreatetime = YLeaf(YType.uint32, "RMON2-MIB:tokenRingPStatsCreateTime")

                self.tokenringpstatsdatabroadcastpkts = YLeaf(YType.uint32, "tokenRingPStatsDataBroadcastPkts")

                self.tokenringpstatsdatamulticastpkts = YLeaf(YType.uint32, "tokenRingPStatsDataMulticastPkts")

                self.tokenringpstatsdataoctets = YLeaf(YType.uint32, "tokenRingPStatsDataOctets")

                self.tokenringpstatsdatapkts = YLeaf(YType.uint32, "tokenRingPStatsDataPkts")

                self.tokenringpstatsdatapkts1024to2047octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts1024to2047Octets")

                self.tokenringpstatsdatapkts128to255octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts128to255Octets")

                self.tokenringpstatsdatapkts18to63octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts18to63Octets")

                self.tokenringpstatsdatapkts2048to4095octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts2048to4095Octets")

                self.tokenringpstatsdatapkts256to511octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts256to511Octets")

                self.tokenringpstatsdatapkts4096to8191octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts4096to8191Octets")

                self.tokenringpstatsdatapkts512to1023octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts512to1023Octets")

                self.tokenringpstatsdatapkts64to127octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts64to127Octets")

                self.tokenringpstatsdatapkts8192to18000octets = YLeaf(YType.uint32, "tokenRingPStatsDataPkts8192to18000Octets")

                self.tokenringpstatsdatapktsgreaterthan18000octets = YLeaf(YType.uint32, "tokenRingPStatsDataPktsGreaterThan18000Octets")

                self.tokenringpstatsdatasource = YLeaf(YType.str, "tokenRingPStatsDataSource")

                self.tokenringpstatsdropevents = YLeaf(YType.uint32, "tokenRingPStatsDropEvents")

                self.tokenringpstatsdroppedframes = YLeaf(YType.uint32, "RMON2-MIB:tokenRingPStatsDroppedFrames")

                self.tokenringpstatsowner = YLeaf(YType.str, "tokenRingPStatsOwner")

                self.tokenringpstatsstatus = YLeaf(YType.enumeration, "tokenRingPStatsStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tokenringpstatsindex",
                                "tokenringpstatscreatetime",
                                "tokenringpstatsdatabroadcastpkts",
                                "tokenringpstatsdatamulticastpkts",
                                "tokenringpstatsdataoctets",
                                "tokenringpstatsdatapkts",
                                "tokenringpstatsdatapkts1024to2047octets",
                                "tokenringpstatsdatapkts128to255octets",
                                "tokenringpstatsdatapkts18to63octets",
                                "tokenringpstatsdatapkts2048to4095octets",
                                "tokenringpstatsdatapkts256to511octets",
                                "tokenringpstatsdatapkts4096to8191octets",
                                "tokenringpstatsdatapkts512to1023octets",
                                "tokenringpstatsdatapkts64to127octets",
                                "tokenringpstatsdatapkts8192to18000octets",
                                "tokenringpstatsdatapktsgreaterthan18000octets",
                                "tokenringpstatsdatasource",
                                "tokenringpstatsdropevents",
                                "tokenringpstatsdroppedframes",
                                "tokenringpstatsowner",
                                "tokenringpstatsstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tokenringpstatsindex.is_set or
                    self.tokenringpstatscreatetime.is_set or
                    self.tokenringpstatsdatabroadcastpkts.is_set or
                    self.tokenringpstatsdatamulticastpkts.is_set or
                    self.tokenringpstatsdataoctets.is_set or
                    self.tokenringpstatsdatapkts.is_set or
                    self.tokenringpstatsdatapkts1024to2047octets.is_set or
                    self.tokenringpstatsdatapkts128to255octets.is_set or
                    self.tokenringpstatsdatapkts18to63octets.is_set or
                    self.tokenringpstatsdatapkts2048to4095octets.is_set or
                    self.tokenringpstatsdatapkts256to511octets.is_set or
                    self.tokenringpstatsdatapkts4096to8191octets.is_set or
                    self.tokenringpstatsdatapkts512to1023octets.is_set or
                    self.tokenringpstatsdatapkts64to127octets.is_set or
                    self.tokenringpstatsdatapkts8192to18000octets.is_set or
                    self.tokenringpstatsdatapktsgreaterthan18000octets.is_set or
                    self.tokenringpstatsdatasource.is_set or
                    self.tokenringpstatsdropevents.is_set or
                    self.tokenringpstatsdroppedframes.is_set or
                    self.tokenringpstatsowner.is_set or
                    self.tokenringpstatsstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tokenringpstatsindex.yfilter != YFilter.not_set or
                    self.tokenringpstatscreatetime.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatabroadcastpkts.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatamulticastpkts.yfilter != YFilter.not_set or
                    self.tokenringpstatsdataoctets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts1024to2047octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts128to255octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts18to63octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts2048to4095octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts256to511octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts4096to8191octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts512to1023octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts64to127octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapkts8192to18000octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatapktsgreaterthan18000octets.yfilter != YFilter.not_set or
                    self.tokenringpstatsdatasource.yfilter != YFilter.not_set or
                    self.tokenringpstatsdropevents.yfilter != YFilter.not_set or
                    self.tokenringpstatsdroppedframes.yfilter != YFilter.not_set or
                    self.tokenringpstatsowner.yfilter != YFilter.not_set or
                    self.tokenringpstatsstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tokenRingPStatsEntry" + "[tokenRingPStatsIndex='" + self.tokenringpstatsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingPStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tokenringpstatsindex.is_set or self.tokenringpstatsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsindex.get_name_leafdata())
                if (self.tokenringpstatscreatetime.is_set or self.tokenringpstatscreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatscreatetime.get_name_leafdata())
                if (self.tokenringpstatsdatabroadcastpkts.is_set or self.tokenringpstatsdatabroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatabroadcastpkts.get_name_leafdata())
                if (self.tokenringpstatsdatamulticastpkts.is_set or self.tokenringpstatsdatamulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatamulticastpkts.get_name_leafdata())
                if (self.tokenringpstatsdataoctets.is_set or self.tokenringpstatsdataoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdataoctets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts.is_set or self.tokenringpstatsdatapkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts.get_name_leafdata())
                if (self.tokenringpstatsdatapkts1024to2047octets.is_set or self.tokenringpstatsdatapkts1024to2047octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts1024to2047octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts128to255octets.is_set or self.tokenringpstatsdatapkts128to255octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts128to255octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts18to63octets.is_set or self.tokenringpstatsdatapkts18to63octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts18to63octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts2048to4095octets.is_set or self.tokenringpstatsdatapkts2048to4095octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts2048to4095octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts256to511octets.is_set or self.tokenringpstatsdatapkts256to511octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts256to511octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts4096to8191octets.is_set or self.tokenringpstatsdatapkts4096to8191octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts4096to8191octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts512to1023octets.is_set or self.tokenringpstatsdatapkts512to1023octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts512to1023octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts64to127octets.is_set or self.tokenringpstatsdatapkts64to127octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts64to127octets.get_name_leafdata())
                if (self.tokenringpstatsdatapkts8192to18000octets.is_set or self.tokenringpstatsdatapkts8192to18000octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapkts8192to18000octets.get_name_leafdata())
                if (self.tokenringpstatsdatapktsgreaterthan18000octets.is_set or self.tokenringpstatsdatapktsgreaterthan18000octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatapktsgreaterthan18000octets.get_name_leafdata())
                if (self.tokenringpstatsdatasource.is_set or self.tokenringpstatsdatasource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdatasource.get_name_leafdata())
                if (self.tokenringpstatsdropevents.is_set or self.tokenringpstatsdropevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdropevents.get_name_leafdata())
                if (self.tokenringpstatsdroppedframes.is_set or self.tokenringpstatsdroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsdroppedframes.get_name_leafdata())
                if (self.tokenringpstatsowner.is_set or self.tokenringpstatsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsowner.get_name_leafdata())
                if (self.tokenringpstatsstatus.is_set or self.tokenringpstatsstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringpstatsstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tokenRingPStatsIndex" or name == "tokenRingPStatsCreateTime" or name == "tokenRingPStatsDataBroadcastPkts" or name == "tokenRingPStatsDataMulticastPkts" or name == "tokenRingPStatsDataOctets" or name == "tokenRingPStatsDataPkts" or name == "tokenRingPStatsDataPkts1024to2047Octets" or name == "tokenRingPStatsDataPkts128to255Octets" or name == "tokenRingPStatsDataPkts18to63Octets" or name == "tokenRingPStatsDataPkts2048to4095Octets" or name == "tokenRingPStatsDataPkts256to511Octets" or name == "tokenRingPStatsDataPkts4096to8191Octets" or name == "tokenRingPStatsDataPkts512to1023Octets" or name == "tokenRingPStatsDataPkts64to127Octets" or name == "tokenRingPStatsDataPkts8192to18000Octets" or name == "tokenRingPStatsDataPktsGreaterThan18000Octets" or name == "tokenRingPStatsDataSource" or name == "tokenRingPStatsDropEvents" or name == "tokenRingPStatsDroppedFrames" or name == "tokenRingPStatsOwner" or name == "tokenRingPStatsStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tokenRingPStatsIndex"):
                    self.tokenringpstatsindex = value
                    self.tokenringpstatsindex.value_namespace = name_space
                    self.tokenringpstatsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsCreateTime"):
                    self.tokenringpstatscreatetime = value
                    self.tokenringpstatscreatetime.value_namespace = name_space
                    self.tokenringpstatscreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataBroadcastPkts"):
                    self.tokenringpstatsdatabroadcastpkts = value
                    self.tokenringpstatsdatabroadcastpkts.value_namespace = name_space
                    self.tokenringpstatsdatabroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataMulticastPkts"):
                    self.tokenringpstatsdatamulticastpkts = value
                    self.tokenringpstatsdatamulticastpkts.value_namespace = name_space
                    self.tokenringpstatsdatamulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataOctets"):
                    self.tokenringpstatsdataoctets = value
                    self.tokenringpstatsdataoctets.value_namespace = name_space
                    self.tokenringpstatsdataoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts"):
                    self.tokenringpstatsdatapkts = value
                    self.tokenringpstatsdatapkts.value_namespace = name_space
                    self.tokenringpstatsdatapkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts1024to2047Octets"):
                    self.tokenringpstatsdatapkts1024to2047octets = value
                    self.tokenringpstatsdatapkts1024to2047octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts1024to2047octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts128to255Octets"):
                    self.tokenringpstatsdatapkts128to255octets = value
                    self.tokenringpstatsdatapkts128to255octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts128to255octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts18to63Octets"):
                    self.tokenringpstatsdatapkts18to63octets = value
                    self.tokenringpstatsdatapkts18to63octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts18to63octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts2048to4095Octets"):
                    self.tokenringpstatsdatapkts2048to4095octets = value
                    self.tokenringpstatsdatapkts2048to4095octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts2048to4095octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts256to511Octets"):
                    self.tokenringpstatsdatapkts256to511octets = value
                    self.tokenringpstatsdatapkts256to511octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts256to511octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts4096to8191Octets"):
                    self.tokenringpstatsdatapkts4096to8191octets = value
                    self.tokenringpstatsdatapkts4096to8191octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts4096to8191octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts512to1023Octets"):
                    self.tokenringpstatsdatapkts512to1023octets = value
                    self.tokenringpstatsdatapkts512to1023octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts512to1023octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts64to127Octets"):
                    self.tokenringpstatsdatapkts64to127octets = value
                    self.tokenringpstatsdatapkts64to127octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts64to127octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPkts8192to18000Octets"):
                    self.tokenringpstatsdatapkts8192to18000octets = value
                    self.tokenringpstatsdatapkts8192to18000octets.value_namespace = name_space
                    self.tokenringpstatsdatapkts8192to18000octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataPktsGreaterThan18000Octets"):
                    self.tokenringpstatsdatapktsgreaterthan18000octets = value
                    self.tokenringpstatsdatapktsgreaterthan18000octets.value_namespace = name_space
                    self.tokenringpstatsdatapktsgreaterthan18000octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDataSource"):
                    self.tokenringpstatsdatasource = value
                    self.tokenringpstatsdatasource.value_namespace = name_space
                    self.tokenringpstatsdatasource.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDropEvents"):
                    self.tokenringpstatsdropevents = value
                    self.tokenringpstatsdropevents.value_namespace = name_space
                    self.tokenringpstatsdropevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsDroppedFrames"):
                    self.tokenringpstatsdroppedframes = value
                    self.tokenringpstatsdroppedframes.value_namespace = name_space
                    self.tokenringpstatsdroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsOwner"):
                    self.tokenringpstatsowner = value
                    self.tokenringpstatsowner.value_namespace = name_space
                    self.tokenringpstatsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPStatsStatus"):
                    self.tokenringpstatsstatus = value
                    self.tokenringpstatsstatus.value_namespace = name_space
                    self.tokenringpstatsstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tokenringpstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tokenringpstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tokenRingPStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tokenRingPStatsEntry"):
                for c in self.tokenringpstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Tokenringpstatstable.Tokenringpstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tokenringpstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tokenRingPStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tokenringmlhistorytable(Entity):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlhistoryentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of    :py:class:`Tokenringmlhistoryentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Tokenringmlhistorytable, self).__init__()

            self.yang_name = "tokenRingMLHistoryTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.tokenringmlhistoryentry = YList(self)

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
                        super(TokenRingRmonMib.Tokenringmlhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Tokenringmlhistorytable, self).__setattr__(name, value)


        class Tokenringmlhistoryentry(Entity):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlhistoryindex  <key>
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringmlhistorysampleindex  <key>
            
            	An index that uniquely identifies the particular Mac\-Layer sample this entry represents among all Mac\-Layer samples associated with the same historyControlEntry.  This index starts at 1 and increases by one as each new sample is taken
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistoryaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryactivestations
            
            	The maximum number of active stations on the ring detected by the probe during this sampling      interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistorybeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState, beaconSetRecoveryModeState, or beaconRingSignalLossState) during this sampling interval.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybeaconpkts
            
            	The total number of beacon MAC packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybeacontime
            
            	The amount of time that the ring has been in the beaconing state during this sampling interval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistorybursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state during this sampling interval. The claim token state that comes from the beacon state is not counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorycongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorydropevents
            
            	The total number of events in which packets were      dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorylineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorylostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorymacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network during this sampling interval (excluding framing bits but including FCS octets)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorymacpkts
            
            	The total number of MAC packets (excluding those that were not good frames) received during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorynaunchanges
            
            	The total number of NAUN changes detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpollevents
            
            	The total number of ring poll events detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpurgeevents
            
            	The total number of times that the ring entered the ring purge state from normal ring state during this sampling interval.  The ring purge state that comes from the claim token or beacon state is not counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpurgepkts
            
            	The total number of Ring Purge MAC packets detected by the probe during this sampling      interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorysofterrorreports
            
            	The total number of soft error report frames detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorytokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry, self).__init__()

                self.yang_name = "tokenRingMLHistoryEntry"
                self.yang_parent_name = "tokenRingMLHistoryTable"

                self.tokenringmlhistoryindex = YLeaf(YType.int32, "tokenRingMLHistoryIndex")

                self.tokenringmlhistorysampleindex = YLeaf(YType.int32, "tokenRingMLHistorySampleIndex")

                self.tokenringmlhistoryaborterrors = YLeaf(YType.uint32, "tokenRingMLHistoryAbortErrors")

                self.tokenringmlhistoryacerrors = YLeaf(YType.uint32, "tokenRingMLHistoryACErrors")

                self.tokenringmlhistoryactivestations = YLeaf(YType.int32, "tokenRingMLHistoryActiveStations")

                self.tokenringmlhistorybeaconevents = YLeaf(YType.uint32, "tokenRingMLHistoryBeaconEvents")

                self.tokenringmlhistorybeaconpkts = YLeaf(YType.uint32, "tokenRingMLHistoryBeaconPkts")

                self.tokenringmlhistorybeacontime = YLeaf(YType.int32, "tokenRingMLHistoryBeaconTime")

                self.tokenringmlhistorybursterrors = YLeaf(YType.uint32, "tokenRingMLHistoryBurstErrors")

                self.tokenringmlhistoryclaimtokenevents = YLeaf(YType.uint32, "tokenRingMLHistoryClaimTokenEvents")

                self.tokenringmlhistoryclaimtokenpkts = YLeaf(YType.uint32, "tokenRingMLHistoryClaimTokenPkts")

                self.tokenringmlhistorycongestionerrors = YLeaf(YType.uint32, "tokenRingMLHistoryCongestionErrors")

                self.tokenringmlhistorydropevents = YLeaf(YType.uint32, "tokenRingMLHistoryDropEvents")

                self.tokenringmlhistoryframecopiederrors = YLeaf(YType.uint32, "tokenRingMLHistoryFrameCopiedErrors")

                self.tokenringmlhistoryfrequencyerrors = YLeaf(YType.uint32, "tokenRingMLHistoryFrequencyErrors")

                self.tokenringmlhistoryinternalerrors = YLeaf(YType.uint32, "tokenRingMLHistoryInternalErrors")

                self.tokenringmlhistoryintervalstart = YLeaf(YType.uint32, "tokenRingMLHistoryIntervalStart")

                self.tokenringmlhistorylineerrors = YLeaf(YType.uint32, "tokenRingMLHistoryLineErrors")

                self.tokenringmlhistorylostframeerrors = YLeaf(YType.uint32, "tokenRingMLHistoryLostFrameErrors")

                self.tokenringmlhistorymacoctets = YLeaf(YType.uint32, "tokenRingMLHistoryMacOctets")

                self.tokenringmlhistorymacpkts = YLeaf(YType.uint32, "tokenRingMLHistoryMacPkts")

                self.tokenringmlhistorynaunchanges = YLeaf(YType.uint32, "tokenRingMLHistoryNAUNChanges")

                self.tokenringmlhistoryringpollevents = YLeaf(YType.uint32, "tokenRingMLHistoryRingPollEvents")

                self.tokenringmlhistoryringpurgeevents = YLeaf(YType.uint32, "tokenRingMLHistoryRingPurgeEvents")

                self.tokenringmlhistoryringpurgepkts = YLeaf(YType.uint32, "tokenRingMLHistoryRingPurgePkts")

                self.tokenringmlhistorysofterrorreports = YLeaf(YType.uint32, "tokenRingMLHistorySoftErrorReports")

                self.tokenringmlhistorytokenerrors = YLeaf(YType.uint32, "tokenRingMLHistoryTokenErrors")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tokenringmlhistoryindex",
                                "tokenringmlhistorysampleindex",
                                "tokenringmlhistoryaborterrors",
                                "tokenringmlhistoryacerrors",
                                "tokenringmlhistoryactivestations",
                                "tokenringmlhistorybeaconevents",
                                "tokenringmlhistorybeaconpkts",
                                "tokenringmlhistorybeacontime",
                                "tokenringmlhistorybursterrors",
                                "tokenringmlhistoryclaimtokenevents",
                                "tokenringmlhistoryclaimtokenpkts",
                                "tokenringmlhistorycongestionerrors",
                                "tokenringmlhistorydropevents",
                                "tokenringmlhistoryframecopiederrors",
                                "tokenringmlhistoryfrequencyerrors",
                                "tokenringmlhistoryinternalerrors",
                                "tokenringmlhistoryintervalstart",
                                "tokenringmlhistorylineerrors",
                                "tokenringmlhistorylostframeerrors",
                                "tokenringmlhistorymacoctets",
                                "tokenringmlhistorymacpkts",
                                "tokenringmlhistorynaunchanges",
                                "tokenringmlhistoryringpollevents",
                                "tokenringmlhistoryringpurgeevents",
                                "tokenringmlhistoryringpurgepkts",
                                "tokenringmlhistorysofterrorreports",
                                "tokenringmlhistorytokenerrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tokenringmlhistoryindex.is_set or
                    self.tokenringmlhistorysampleindex.is_set or
                    self.tokenringmlhistoryaborterrors.is_set or
                    self.tokenringmlhistoryacerrors.is_set or
                    self.tokenringmlhistoryactivestations.is_set or
                    self.tokenringmlhistorybeaconevents.is_set or
                    self.tokenringmlhistorybeaconpkts.is_set or
                    self.tokenringmlhistorybeacontime.is_set or
                    self.tokenringmlhistorybursterrors.is_set or
                    self.tokenringmlhistoryclaimtokenevents.is_set or
                    self.tokenringmlhistoryclaimtokenpkts.is_set or
                    self.tokenringmlhistorycongestionerrors.is_set or
                    self.tokenringmlhistorydropevents.is_set or
                    self.tokenringmlhistoryframecopiederrors.is_set or
                    self.tokenringmlhistoryfrequencyerrors.is_set or
                    self.tokenringmlhistoryinternalerrors.is_set or
                    self.tokenringmlhistoryintervalstart.is_set or
                    self.tokenringmlhistorylineerrors.is_set or
                    self.tokenringmlhistorylostframeerrors.is_set or
                    self.tokenringmlhistorymacoctets.is_set or
                    self.tokenringmlhistorymacpkts.is_set or
                    self.tokenringmlhistorynaunchanges.is_set or
                    self.tokenringmlhistoryringpollevents.is_set or
                    self.tokenringmlhistoryringpurgeevents.is_set or
                    self.tokenringmlhistoryringpurgepkts.is_set or
                    self.tokenringmlhistorysofterrorreports.is_set or
                    self.tokenringmlhistorytokenerrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryindex.yfilter != YFilter.not_set or
                    self.tokenringmlhistorysampleindex.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryaborterrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryacerrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryactivestations.yfilter != YFilter.not_set or
                    self.tokenringmlhistorybeaconevents.yfilter != YFilter.not_set or
                    self.tokenringmlhistorybeaconpkts.yfilter != YFilter.not_set or
                    self.tokenringmlhistorybeacontime.yfilter != YFilter.not_set or
                    self.tokenringmlhistorybursterrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryclaimtokenevents.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryclaimtokenpkts.yfilter != YFilter.not_set or
                    self.tokenringmlhistorycongestionerrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistorydropevents.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryframecopiederrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryfrequencyerrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryinternalerrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryintervalstart.yfilter != YFilter.not_set or
                    self.tokenringmlhistorylineerrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistorylostframeerrors.yfilter != YFilter.not_set or
                    self.tokenringmlhistorymacoctets.yfilter != YFilter.not_set or
                    self.tokenringmlhistorymacpkts.yfilter != YFilter.not_set or
                    self.tokenringmlhistorynaunchanges.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryringpollevents.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryringpurgeevents.yfilter != YFilter.not_set or
                    self.tokenringmlhistoryringpurgepkts.yfilter != YFilter.not_set or
                    self.tokenringmlhistorysofterrorreports.yfilter != YFilter.not_set or
                    self.tokenringmlhistorytokenerrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tokenRingMLHistoryEntry" + "[tokenRingMLHistoryIndex='" + self.tokenringmlhistoryindex.get() + "']" + "[tokenRingMLHistorySampleIndex='" + self.tokenringmlhistorysampleindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingMLHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tokenringmlhistoryindex.is_set or self.tokenringmlhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryindex.get_name_leafdata())
                if (self.tokenringmlhistorysampleindex.is_set or self.tokenringmlhistorysampleindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorysampleindex.get_name_leafdata())
                if (self.tokenringmlhistoryaborterrors.is_set or self.tokenringmlhistoryaborterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryaborterrors.get_name_leafdata())
                if (self.tokenringmlhistoryacerrors.is_set or self.tokenringmlhistoryacerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryacerrors.get_name_leafdata())
                if (self.tokenringmlhistoryactivestations.is_set or self.tokenringmlhistoryactivestations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryactivestations.get_name_leafdata())
                if (self.tokenringmlhistorybeaconevents.is_set or self.tokenringmlhistorybeaconevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorybeaconevents.get_name_leafdata())
                if (self.tokenringmlhistorybeaconpkts.is_set or self.tokenringmlhistorybeaconpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorybeaconpkts.get_name_leafdata())
                if (self.tokenringmlhistorybeacontime.is_set or self.tokenringmlhistorybeacontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorybeacontime.get_name_leafdata())
                if (self.tokenringmlhistorybursterrors.is_set or self.tokenringmlhistorybursterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorybursterrors.get_name_leafdata())
                if (self.tokenringmlhistoryclaimtokenevents.is_set or self.tokenringmlhistoryclaimtokenevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryclaimtokenevents.get_name_leafdata())
                if (self.tokenringmlhistoryclaimtokenpkts.is_set or self.tokenringmlhistoryclaimtokenpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryclaimtokenpkts.get_name_leafdata())
                if (self.tokenringmlhistorycongestionerrors.is_set or self.tokenringmlhistorycongestionerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorycongestionerrors.get_name_leafdata())
                if (self.tokenringmlhistorydropevents.is_set or self.tokenringmlhistorydropevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorydropevents.get_name_leafdata())
                if (self.tokenringmlhistoryframecopiederrors.is_set or self.tokenringmlhistoryframecopiederrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryframecopiederrors.get_name_leafdata())
                if (self.tokenringmlhistoryfrequencyerrors.is_set or self.tokenringmlhistoryfrequencyerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryfrequencyerrors.get_name_leafdata())
                if (self.tokenringmlhistoryinternalerrors.is_set or self.tokenringmlhistoryinternalerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryinternalerrors.get_name_leafdata())
                if (self.tokenringmlhistoryintervalstart.is_set or self.tokenringmlhistoryintervalstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryintervalstart.get_name_leafdata())
                if (self.tokenringmlhistorylineerrors.is_set or self.tokenringmlhistorylineerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorylineerrors.get_name_leafdata())
                if (self.tokenringmlhistorylostframeerrors.is_set or self.tokenringmlhistorylostframeerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorylostframeerrors.get_name_leafdata())
                if (self.tokenringmlhistorymacoctets.is_set or self.tokenringmlhistorymacoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorymacoctets.get_name_leafdata())
                if (self.tokenringmlhistorymacpkts.is_set or self.tokenringmlhistorymacpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorymacpkts.get_name_leafdata())
                if (self.tokenringmlhistorynaunchanges.is_set or self.tokenringmlhistorynaunchanges.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorynaunchanges.get_name_leafdata())
                if (self.tokenringmlhistoryringpollevents.is_set or self.tokenringmlhistoryringpollevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryringpollevents.get_name_leafdata())
                if (self.tokenringmlhistoryringpurgeevents.is_set or self.tokenringmlhistoryringpurgeevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryringpurgeevents.get_name_leafdata())
                if (self.tokenringmlhistoryringpurgepkts.is_set or self.tokenringmlhistoryringpurgepkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistoryringpurgepkts.get_name_leafdata())
                if (self.tokenringmlhistorysofterrorreports.is_set or self.tokenringmlhistorysofterrorreports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorysofterrorreports.get_name_leafdata())
                if (self.tokenringmlhistorytokenerrors.is_set or self.tokenringmlhistorytokenerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringmlhistorytokenerrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tokenRingMLHistoryIndex" or name == "tokenRingMLHistorySampleIndex" or name == "tokenRingMLHistoryAbortErrors" or name == "tokenRingMLHistoryACErrors" or name == "tokenRingMLHistoryActiveStations" or name == "tokenRingMLHistoryBeaconEvents" or name == "tokenRingMLHistoryBeaconPkts" or name == "tokenRingMLHistoryBeaconTime" or name == "tokenRingMLHistoryBurstErrors" or name == "tokenRingMLHistoryClaimTokenEvents" or name == "tokenRingMLHistoryClaimTokenPkts" or name == "tokenRingMLHistoryCongestionErrors" or name == "tokenRingMLHistoryDropEvents" or name == "tokenRingMLHistoryFrameCopiedErrors" or name == "tokenRingMLHistoryFrequencyErrors" or name == "tokenRingMLHistoryInternalErrors" or name == "tokenRingMLHistoryIntervalStart" or name == "tokenRingMLHistoryLineErrors" or name == "tokenRingMLHistoryLostFrameErrors" or name == "tokenRingMLHistoryMacOctets" or name == "tokenRingMLHistoryMacPkts" or name == "tokenRingMLHistoryNAUNChanges" or name == "tokenRingMLHistoryRingPollEvents" or name == "tokenRingMLHistoryRingPurgeEvents" or name == "tokenRingMLHistoryRingPurgePkts" or name == "tokenRingMLHistorySoftErrorReports" or name == "tokenRingMLHistoryTokenErrors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tokenRingMLHistoryIndex"):
                    self.tokenringmlhistoryindex = value
                    self.tokenringmlhistoryindex.value_namespace = name_space
                    self.tokenringmlhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistorySampleIndex"):
                    self.tokenringmlhistorysampleindex = value
                    self.tokenringmlhistorysampleindex.value_namespace = name_space
                    self.tokenringmlhistorysampleindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryAbortErrors"):
                    self.tokenringmlhistoryaborterrors = value
                    self.tokenringmlhistoryaborterrors.value_namespace = name_space
                    self.tokenringmlhistoryaborterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryACErrors"):
                    self.tokenringmlhistoryacerrors = value
                    self.tokenringmlhistoryacerrors.value_namespace = name_space
                    self.tokenringmlhistoryacerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryActiveStations"):
                    self.tokenringmlhistoryactivestations = value
                    self.tokenringmlhistoryactivestations.value_namespace = name_space
                    self.tokenringmlhistoryactivestations.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryBeaconEvents"):
                    self.tokenringmlhistorybeaconevents = value
                    self.tokenringmlhistorybeaconevents.value_namespace = name_space
                    self.tokenringmlhistorybeaconevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryBeaconPkts"):
                    self.tokenringmlhistorybeaconpkts = value
                    self.tokenringmlhistorybeaconpkts.value_namespace = name_space
                    self.tokenringmlhistorybeaconpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryBeaconTime"):
                    self.tokenringmlhistorybeacontime = value
                    self.tokenringmlhistorybeacontime.value_namespace = name_space
                    self.tokenringmlhistorybeacontime.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryBurstErrors"):
                    self.tokenringmlhistorybursterrors = value
                    self.tokenringmlhistorybursterrors.value_namespace = name_space
                    self.tokenringmlhistorybursterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryClaimTokenEvents"):
                    self.tokenringmlhistoryclaimtokenevents = value
                    self.tokenringmlhistoryclaimtokenevents.value_namespace = name_space
                    self.tokenringmlhistoryclaimtokenevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryClaimTokenPkts"):
                    self.tokenringmlhistoryclaimtokenpkts = value
                    self.tokenringmlhistoryclaimtokenpkts.value_namespace = name_space
                    self.tokenringmlhistoryclaimtokenpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryCongestionErrors"):
                    self.tokenringmlhistorycongestionerrors = value
                    self.tokenringmlhistorycongestionerrors.value_namespace = name_space
                    self.tokenringmlhistorycongestionerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryDropEvents"):
                    self.tokenringmlhistorydropevents = value
                    self.tokenringmlhistorydropevents.value_namespace = name_space
                    self.tokenringmlhistorydropevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryFrameCopiedErrors"):
                    self.tokenringmlhistoryframecopiederrors = value
                    self.tokenringmlhistoryframecopiederrors.value_namespace = name_space
                    self.tokenringmlhistoryframecopiederrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryFrequencyErrors"):
                    self.tokenringmlhistoryfrequencyerrors = value
                    self.tokenringmlhistoryfrequencyerrors.value_namespace = name_space
                    self.tokenringmlhistoryfrequencyerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryInternalErrors"):
                    self.tokenringmlhistoryinternalerrors = value
                    self.tokenringmlhistoryinternalerrors.value_namespace = name_space
                    self.tokenringmlhistoryinternalerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryIntervalStart"):
                    self.tokenringmlhistoryintervalstart = value
                    self.tokenringmlhistoryintervalstart.value_namespace = name_space
                    self.tokenringmlhistoryintervalstart.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryLineErrors"):
                    self.tokenringmlhistorylineerrors = value
                    self.tokenringmlhistorylineerrors.value_namespace = name_space
                    self.tokenringmlhistorylineerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryLostFrameErrors"):
                    self.tokenringmlhistorylostframeerrors = value
                    self.tokenringmlhistorylostframeerrors.value_namespace = name_space
                    self.tokenringmlhistorylostframeerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryMacOctets"):
                    self.tokenringmlhistorymacoctets = value
                    self.tokenringmlhistorymacoctets.value_namespace = name_space
                    self.tokenringmlhistorymacoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryMacPkts"):
                    self.tokenringmlhistorymacpkts = value
                    self.tokenringmlhistorymacpkts.value_namespace = name_space
                    self.tokenringmlhistorymacpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryNAUNChanges"):
                    self.tokenringmlhistorynaunchanges = value
                    self.tokenringmlhistorynaunchanges.value_namespace = name_space
                    self.tokenringmlhistorynaunchanges.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryRingPollEvents"):
                    self.tokenringmlhistoryringpollevents = value
                    self.tokenringmlhistoryringpollevents.value_namespace = name_space
                    self.tokenringmlhistoryringpollevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryRingPurgeEvents"):
                    self.tokenringmlhistoryringpurgeevents = value
                    self.tokenringmlhistoryringpurgeevents.value_namespace = name_space
                    self.tokenringmlhistoryringpurgeevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryRingPurgePkts"):
                    self.tokenringmlhistoryringpurgepkts = value
                    self.tokenringmlhistoryringpurgepkts.value_namespace = name_space
                    self.tokenringmlhistoryringpurgepkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistorySoftErrorReports"):
                    self.tokenringmlhistorysofterrorreports = value
                    self.tokenringmlhistorysofterrorreports.value_namespace = name_space
                    self.tokenringmlhistorysofterrorreports.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingMLHistoryTokenErrors"):
                    self.tokenringmlhistorytokenerrors = value
                    self.tokenringmlhistorytokenerrors.value_namespace = name_space
                    self.tokenringmlhistorytokenerrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tokenringmlhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tokenringmlhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tokenRingMLHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tokenRingMLHistoryEntry"):
                for c in self.tokenringmlhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Tokenringmlhistorytable.Tokenringmlhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tokenringmlhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tokenRingMLHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tokenringphistorytable(Entity):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringphistoryentry
        
        	A collection of promiscuous statistics kept for a particular Token Ring interface
        	**type**\: list of    :py:class:`Tokenringphistoryentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Tokenringphistorytable, self).__init__()

            self.yang_name = "tokenRingPHistoryTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.tokenringphistoryentry = YList(self)

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
                        super(TokenRingRmonMib.Tokenringphistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Tokenringphistorytable, self).__setattr__(name, value)


        class Tokenringphistoryentry(Entity):
            """
            A collection of promiscuous statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringphistoryindex  <key>
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringphistorysampleindex  <key>
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringphistorydatabroadcastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatamulticastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts
            
            	The total number of good non\-MAC frames received during this sampling interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts128to255octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts18to63octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts256to511octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between      256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts512to1023octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts64to127octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry, self).__init__()

                self.yang_name = "tokenRingPHistoryEntry"
                self.yang_parent_name = "tokenRingPHistoryTable"

                self.tokenringphistoryindex = YLeaf(YType.int32, "tokenRingPHistoryIndex")

                self.tokenringphistorysampleindex = YLeaf(YType.int32, "tokenRingPHistorySampleIndex")

                self.tokenringphistorydatabroadcastpkts = YLeaf(YType.uint32, "tokenRingPHistoryDataBroadcastPkts")

                self.tokenringphistorydatamulticastpkts = YLeaf(YType.uint32, "tokenRingPHistoryDataMulticastPkts")

                self.tokenringphistorydataoctets = YLeaf(YType.uint32, "tokenRingPHistoryDataOctets")

                self.tokenringphistorydatapkts = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts")

                self.tokenringphistorydatapkts1024to2047octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts1024to2047Octets")

                self.tokenringphistorydatapkts128to255octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts128to255Octets")

                self.tokenringphistorydatapkts18to63octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts18to63Octets")

                self.tokenringphistorydatapkts2048to4095octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts2048to4095Octets")

                self.tokenringphistorydatapkts256to511octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts256to511Octets")

                self.tokenringphistorydatapkts4096to8191octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts4096to8191Octets")

                self.tokenringphistorydatapkts512to1023octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts512to1023Octets")

                self.tokenringphistorydatapkts64to127octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts64to127Octets")

                self.tokenringphistorydatapkts8192to18000octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPkts8192to18000Octets")

                self.tokenringphistorydatapktsgreaterthan18000octets = YLeaf(YType.uint32, "tokenRingPHistoryDataPktsGreaterThan18000Octets")

                self.tokenringphistorydropevents = YLeaf(YType.uint32, "tokenRingPHistoryDropEvents")

                self.tokenringphistoryintervalstart = YLeaf(YType.uint32, "tokenRingPHistoryIntervalStart")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tokenringphistoryindex",
                                "tokenringphistorysampleindex",
                                "tokenringphistorydatabroadcastpkts",
                                "tokenringphistorydatamulticastpkts",
                                "tokenringphistorydataoctets",
                                "tokenringphistorydatapkts",
                                "tokenringphistorydatapkts1024to2047octets",
                                "tokenringphistorydatapkts128to255octets",
                                "tokenringphistorydatapkts18to63octets",
                                "tokenringphistorydatapkts2048to4095octets",
                                "tokenringphistorydatapkts256to511octets",
                                "tokenringphistorydatapkts4096to8191octets",
                                "tokenringphistorydatapkts512to1023octets",
                                "tokenringphistorydatapkts64to127octets",
                                "tokenringphistorydatapkts8192to18000octets",
                                "tokenringphistorydatapktsgreaterthan18000octets",
                                "tokenringphistorydropevents",
                                "tokenringphistoryintervalstart") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tokenringphistoryindex.is_set or
                    self.tokenringphistorysampleindex.is_set or
                    self.tokenringphistorydatabroadcastpkts.is_set or
                    self.tokenringphistorydatamulticastpkts.is_set or
                    self.tokenringphistorydataoctets.is_set or
                    self.tokenringphistorydatapkts.is_set or
                    self.tokenringphistorydatapkts1024to2047octets.is_set or
                    self.tokenringphistorydatapkts128to255octets.is_set or
                    self.tokenringphistorydatapkts18to63octets.is_set or
                    self.tokenringphistorydatapkts2048to4095octets.is_set or
                    self.tokenringphistorydatapkts256to511octets.is_set or
                    self.tokenringphistorydatapkts4096to8191octets.is_set or
                    self.tokenringphistorydatapkts512to1023octets.is_set or
                    self.tokenringphistorydatapkts64to127octets.is_set or
                    self.tokenringphistorydatapkts8192to18000octets.is_set or
                    self.tokenringphistorydatapktsgreaterthan18000octets.is_set or
                    self.tokenringphistorydropevents.is_set or
                    self.tokenringphistoryintervalstart.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tokenringphistoryindex.yfilter != YFilter.not_set or
                    self.tokenringphistorysampleindex.yfilter != YFilter.not_set or
                    self.tokenringphistorydatabroadcastpkts.yfilter != YFilter.not_set or
                    self.tokenringphistorydatamulticastpkts.yfilter != YFilter.not_set or
                    self.tokenringphistorydataoctets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts1024to2047octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts128to255octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts18to63octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts2048to4095octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts256to511octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts4096to8191octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts512to1023octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts64to127octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapkts8192to18000octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydatapktsgreaterthan18000octets.yfilter != YFilter.not_set or
                    self.tokenringphistorydropevents.yfilter != YFilter.not_set or
                    self.tokenringphistoryintervalstart.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tokenRingPHistoryEntry" + "[tokenRingPHistoryIndex='" + self.tokenringphistoryindex.get() + "']" + "[tokenRingPHistorySampleIndex='" + self.tokenringphistorysampleindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/tokenRingPHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tokenringphistoryindex.is_set or self.tokenringphistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistoryindex.get_name_leafdata())
                if (self.tokenringphistorysampleindex.is_set or self.tokenringphistorysampleindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorysampleindex.get_name_leafdata())
                if (self.tokenringphistorydatabroadcastpkts.is_set or self.tokenringphistorydatabroadcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatabroadcastpkts.get_name_leafdata())
                if (self.tokenringphistorydatamulticastpkts.is_set or self.tokenringphistorydatamulticastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatamulticastpkts.get_name_leafdata())
                if (self.tokenringphistorydataoctets.is_set or self.tokenringphistorydataoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydataoctets.get_name_leafdata())
                if (self.tokenringphistorydatapkts.is_set or self.tokenringphistorydatapkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts.get_name_leafdata())
                if (self.tokenringphistorydatapkts1024to2047octets.is_set or self.tokenringphistorydatapkts1024to2047octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts1024to2047octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts128to255octets.is_set or self.tokenringphistorydatapkts128to255octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts128to255octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts18to63octets.is_set or self.tokenringphistorydatapkts18to63octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts18to63octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts2048to4095octets.is_set or self.tokenringphistorydatapkts2048to4095octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts2048to4095octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts256to511octets.is_set or self.tokenringphistorydatapkts256to511octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts256to511octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts4096to8191octets.is_set or self.tokenringphistorydatapkts4096to8191octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts4096to8191octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts512to1023octets.is_set or self.tokenringphistorydatapkts512to1023octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts512to1023octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts64to127octets.is_set or self.tokenringphistorydatapkts64to127octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts64to127octets.get_name_leafdata())
                if (self.tokenringphistorydatapkts8192to18000octets.is_set or self.tokenringphistorydatapkts8192to18000octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapkts8192to18000octets.get_name_leafdata())
                if (self.tokenringphistorydatapktsgreaterthan18000octets.is_set or self.tokenringphistorydatapktsgreaterthan18000octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydatapktsgreaterthan18000octets.get_name_leafdata())
                if (self.tokenringphistorydropevents.is_set or self.tokenringphistorydropevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistorydropevents.get_name_leafdata())
                if (self.tokenringphistoryintervalstart.is_set or self.tokenringphistoryintervalstart.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tokenringphistoryintervalstart.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tokenRingPHistoryIndex" or name == "tokenRingPHistorySampleIndex" or name == "tokenRingPHistoryDataBroadcastPkts" or name == "tokenRingPHistoryDataMulticastPkts" or name == "tokenRingPHistoryDataOctets" or name == "tokenRingPHistoryDataPkts" or name == "tokenRingPHistoryDataPkts1024to2047Octets" or name == "tokenRingPHistoryDataPkts128to255Octets" or name == "tokenRingPHistoryDataPkts18to63Octets" or name == "tokenRingPHistoryDataPkts2048to4095Octets" or name == "tokenRingPHistoryDataPkts256to511Octets" or name == "tokenRingPHistoryDataPkts4096to8191Octets" or name == "tokenRingPHistoryDataPkts512to1023Octets" or name == "tokenRingPHistoryDataPkts64to127Octets" or name == "tokenRingPHistoryDataPkts8192to18000Octets" or name == "tokenRingPHistoryDataPktsGreaterThan18000Octets" or name == "tokenRingPHistoryDropEvents" or name == "tokenRingPHistoryIntervalStart"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tokenRingPHistoryIndex"):
                    self.tokenringphistoryindex = value
                    self.tokenringphistoryindex.value_namespace = name_space
                    self.tokenringphistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistorySampleIndex"):
                    self.tokenringphistorysampleindex = value
                    self.tokenringphistorysampleindex.value_namespace = name_space
                    self.tokenringphistorysampleindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataBroadcastPkts"):
                    self.tokenringphistorydatabroadcastpkts = value
                    self.tokenringphistorydatabroadcastpkts.value_namespace = name_space
                    self.tokenringphistorydatabroadcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataMulticastPkts"):
                    self.tokenringphistorydatamulticastpkts = value
                    self.tokenringphistorydatamulticastpkts.value_namespace = name_space
                    self.tokenringphistorydatamulticastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataOctets"):
                    self.tokenringphistorydataoctets = value
                    self.tokenringphistorydataoctets.value_namespace = name_space
                    self.tokenringphistorydataoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts"):
                    self.tokenringphistorydatapkts = value
                    self.tokenringphistorydatapkts.value_namespace = name_space
                    self.tokenringphistorydatapkts.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts1024to2047Octets"):
                    self.tokenringphistorydatapkts1024to2047octets = value
                    self.tokenringphistorydatapkts1024to2047octets.value_namespace = name_space
                    self.tokenringphistorydatapkts1024to2047octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts128to255Octets"):
                    self.tokenringphistorydatapkts128to255octets = value
                    self.tokenringphistorydatapkts128to255octets.value_namespace = name_space
                    self.tokenringphistorydatapkts128to255octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts18to63Octets"):
                    self.tokenringphistorydatapkts18to63octets = value
                    self.tokenringphistorydatapkts18to63octets.value_namespace = name_space
                    self.tokenringphistorydatapkts18to63octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts2048to4095Octets"):
                    self.tokenringphistorydatapkts2048to4095octets = value
                    self.tokenringphistorydatapkts2048to4095octets.value_namespace = name_space
                    self.tokenringphistorydatapkts2048to4095octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts256to511Octets"):
                    self.tokenringphistorydatapkts256to511octets = value
                    self.tokenringphistorydatapkts256to511octets.value_namespace = name_space
                    self.tokenringphistorydatapkts256to511octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts4096to8191Octets"):
                    self.tokenringphistorydatapkts4096to8191octets = value
                    self.tokenringphistorydatapkts4096to8191octets.value_namespace = name_space
                    self.tokenringphistorydatapkts4096to8191octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts512to1023Octets"):
                    self.tokenringphistorydatapkts512to1023octets = value
                    self.tokenringphistorydatapkts512to1023octets.value_namespace = name_space
                    self.tokenringphistorydatapkts512to1023octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts64to127Octets"):
                    self.tokenringphistorydatapkts64to127octets = value
                    self.tokenringphistorydatapkts64to127octets.value_namespace = name_space
                    self.tokenringphistorydatapkts64to127octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPkts8192to18000Octets"):
                    self.tokenringphistorydatapkts8192to18000octets = value
                    self.tokenringphistorydatapkts8192to18000octets.value_namespace = name_space
                    self.tokenringphistorydatapkts8192to18000octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDataPktsGreaterThan18000Octets"):
                    self.tokenringphistorydatapktsgreaterthan18000octets = value
                    self.tokenringphistorydatapktsgreaterthan18000octets.value_namespace = name_space
                    self.tokenringphistorydatapktsgreaterthan18000octets.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryDropEvents"):
                    self.tokenringphistorydropevents = value
                    self.tokenringphistorydropevents.value_namespace = name_space
                    self.tokenringphistorydropevents.value_namespace_prefix = name_space_prefix
                if(value_path == "tokenRingPHistoryIntervalStart"):
                    self.tokenringphistoryintervalstart = value
                    self.tokenringphistoryintervalstart.value_namespace = name_space
                    self.tokenringphistoryintervalstart.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tokenringphistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tokenringphistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tokenRingPHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tokenRingPHistoryEntry"):
                for c in self.tokenringphistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Tokenringphistorytable.Tokenringphistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tokenringphistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tokenRingPHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ringstationcontroltable(Entity):
        """
        A list of ringStation table control entries.
        
        .. attribute:: ringstationcontrolentry
        
        	A list of parameters that set up the discovery of stations on a particular interface and the collection of statistics about these stations
        	**type**\: list of    :py:class:`Ringstationcontrolentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Ringstationcontroltable, self).__init__()

            self.yang_name = "ringStationControlTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.ringstationcontrolentry = YList(self)

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
                        super(TokenRingRmonMib.Ringstationcontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Ringstationcontroltable, self).__setattr__(name, value)


        class Ringstationcontrolentry(Entity):
            """
            A list of parameters that set up the discovery of
            stations on a particular interface and the
            collection of statistics about these stations.
            
            .. attribute:: ringstationcontrolifindex  <key>
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device from which ringStation data is collected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\- II [3]
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: ringstationcontrolactivemonitor
            
            	The address of the Active Monitor on this segment.  If this address is unknown, this object shall be equal to six octets of zero
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationcontrolactivestations
            
            	The number of active ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationcontrolbeaconnaun
            
            	The address of the NAUN in the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationcontrolbeaconsender
            
            	The address of the sender of the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontrolorderchanges
            
            	The number of add and delete events in the ringStationOrderTable optionally associated with this ringStationControlEntry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            .. attribute:: ringstationcontrolringstate
            
            	The current status of this ring
            	**type**\:   :py:class:`Ringstationcontrolringstate <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry.Ringstationcontrolringstate>`
            
            .. attribute:: ringstationcontrolstatus
            
            	The status of this ringStationControl entry.  If this object is not equal to valid(1), all associated entries in the ringStationTable shall be deleted by the agent
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.Entrystatus>`
            
            .. attribute:: ringstationcontroltablesize
            
            	The number of ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry, self).__init__()

                self.yang_name = "ringStationControlEntry"
                self.yang_parent_name = "ringStationControlTable"

                self.ringstationcontrolifindex = YLeaf(YType.int32, "ringStationControlIfIndex")

                self.ringstationcontrolactivemonitor = YLeaf(YType.str, "ringStationControlActiveMonitor")

                self.ringstationcontrolactivestations = YLeaf(YType.int32, "ringStationControlActiveStations")

                self.ringstationcontrolbeaconnaun = YLeaf(YType.str, "ringStationControlBeaconNAUN")

                self.ringstationcontrolbeaconsender = YLeaf(YType.str, "ringStationControlBeaconSender")

                self.ringstationcontrolcreatetime = YLeaf(YType.uint32, "RMON2-MIB:ringStationControlCreateTime")

                self.ringstationcontroldroppedframes = YLeaf(YType.uint32, "RMON2-MIB:ringStationControlDroppedFrames")

                self.ringstationcontrolorderchanges = YLeaf(YType.uint32, "ringStationControlOrderChanges")

                self.ringstationcontrolowner = YLeaf(YType.str, "ringStationControlOwner")

                self.ringstationcontrolringstate = YLeaf(YType.enumeration, "ringStationControlRingState")

                self.ringstationcontrolstatus = YLeaf(YType.enumeration, "ringStationControlStatus")

                self.ringstationcontroltablesize = YLeaf(YType.int32, "ringStationControlTableSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ringstationcontrolifindex",
                                "ringstationcontrolactivemonitor",
                                "ringstationcontrolactivestations",
                                "ringstationcontrolbeaconnaun",
                                "ringstationcontrolbeaconsender",
                                "ringstationcontrolcreatetime",
                                "ringstationcontroldroppedframes",
                                "ringstationcontrolorderchanges",
                                "ringstationcontrolowner",
                                "ringstationcontrolringstate",
                                "ringstationcontrolstatus",
                                "ringstationcontroltablesize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry, self).__setattr__(name, value)

            class Ringstationcontrolringstate(Enum):
                """
                Ringstationcontrolringstate

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


            def has_data(self):
                return (
                    self.ringstationcontrolifindex.is_set or
                    self.ringstationcontrolactivemonitor.is_set or
                    self.ringstationcontrolactivestations.is_set or
                    self.ringstationcontrolbeaconnaun.is_set or
                    self.ringstationcontrolbeaconsender.is_set or
                    self.ringstationcontrolcreatetime.is_set or
                    self.ringstationcontroldroppedframes.is_set or
                    self.ringstationcontrolorderchanges.is_set or
                    self.ringstationcontrolowner.is_set or
                    self.ringstationcontrolringstate.is_set or
                    self.ringstationcontrolstatus.is_set or
                    self.ringstationcontroltablesize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ringstationcontrolifindex.yfilter != YFilter.not_set or
                    self.ringstationcontrolactivemonitor.yfilter != YFilter.not_set or
                    self.ringstationcontrolactivestations.yfilter != YFilter.not_set or
                    self.ringstationcontrolbeaconnaun.yfilter != YFilter.not_set or
                    self.ringstationcontrolbeaconsender.yfilter != YFilter.not_set or
                    self.ringstationcontrolcreatetime.yfilter != YFilter.not_set or
                    self.ringstationcontroldroppedframes.yfilter != YFilter.not_set or
                    self.ringstationcontrolorderchanges.yfilter != YFilter.not_set or
                    self.ringstationcontrolowner.yfilter != YFilter.not_set or
                    self.ringstationcontrolringstate.yfilter != YFilter.not_set or
                    self.ringstationcontrolstatus.yfilter != YFilter.not_set or
                    self.ringstationcontroltablesize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ringStationControlEntry" + "[ringStationControlIfIndex='" + self.ringstationcontrolifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ringstationcontrolifindex.is_set or self.ringstationcontrolifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolifindex.get_name_leafdata())
                if (self.ringstationcontrolactivemonitor.is_set or self.ringstationcontrolactivemonitor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolactivemonitor.get_name_leafdata())
                if (self.ringstationcontrolactivestations.is_set or self.ringstationcontrolactivestations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolactivestations.get_name_leafdata())
                if (self.ringstationcontrolbeaconnaun.is_set or self.ringstationcontrolbeaconnaun.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolbeaconnaun.get_name_leafdata())
                if (self.ringstationcontrolbeaconsender.is_set or self.ringstationcontrolbeaconsender.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolbeaconsender.get_name_leafdata())
                if (self.ringstationcontrolcreatetime.is_set or self.ringstationcontrolcreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolcreatetime.get_name_leafdata())
                if (self.ringstationcontroldroppedframes.is_set or self.ringstationcontroldroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontroldroppedframes.get_name_leafdata())
                if (self.ringstationcontrolorderchanges.is_set or self.ringstationcontrolorderchanges.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolorderchanges.get_name_leafdata())
                if (self.ringstationcontrolowner.is_set or self.ringstationcontrolowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolowner.get_name_leafdata())
                if (self.ringstationcontrolringstate.is_set or self.ringstationcontrolringstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolringstate.get_name_leafdata())
                if (self.ringstationcontrolstatus.is_set or self.ringstationcontrolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontrolstatus.get_name_leafdata())
                if (self.ringstationcontroltablesize.is_set or self.ringstationcontroltablesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcontroltablesize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ringStationControlIfIndex" or name == "ringStationControlActiveMonitor" or name == "ringStationControlActiveStations" or name == "ringStationControlBeaconNAUN" or name == "ringStationControlBeaconSender" or name == "ringStationControlCreateTime" or name == "ringStationControlDroppedFrames" or name == "ringStationControlOrderChanges" or name == "ringStationControlOwner" or name == "ringStationControlRingState" or name == "ringStationControlStatus" or name == "ringStationControlTableSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ringStationControlIfIndex"):
                    self.ringstationcontrolifindex = value
                    self.ringstationcontrolifindex.value_namespace = name_space
                    self.ringstationcontrolifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlActiveMonitor"):
                    self.ringstationcontrolactivemonitor = value
                    self.ringstationcontrolactivemonitor.value_namespace = name_space
                    self.ringstationcontrolactivemonitor.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlActiveStations"):
                    self.ringstationcontrolactivestations = value
                    self.ringstationcontrolactivestations.value_namespace = name_space
                    self.ringstationcontrolactivestations.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlBeaconNAUN"):
                    self.ringstationcontrolbeaconnaun = value
                    self.ringstationcontrolbeaconnaun.value_namespace = name_space
                    self.ringstationcontrolbeaconnaun.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlBeaconSender"):
                    self.ringstationcontrolbeaconsender = value
                    self.ringstationcontrolbeaconsender.value_namespace = name_space
                    self.ringstationcontrolbeaconsender.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlCreateTime"):
                    self.ringstationcontrolcreatetime = value
                    self.ringstationcontrolcreatetime.value_namespace = name_space
                    self.ringstationcontrolcreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlDroppedFrames"):
                    self.ringstationcontroldroppedframes = value
                    self.ringstationcontroldroppedframes.value_namespace = name_space
                    self.ringstationcontroldroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlOrderChanges"):
                    self.ringstationcontrolorderchanges = value
                    self.ringstationcontrolorderchanges.value_namespace = name_space
                    self.ringstationcontrolorderchanges.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlOwner"):
                    self.ringstationcontrolowner = value
                    self.ringstationcontrolowner.value_namespace = name_space
                    self.ringstationcontrolowner.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlRingState"):
                    self.ringstationcontrolringstate = value
                    self.ringstationcontrolringstate.value_namespace = name_space
                    self.ringstationcontrolringstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlStatus"):
                    self.ringstationcontrolstatus = value
                    self.ringstationcontrolstatus.value_namespace = name_space
                    self.ringstationcontrolstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationControlTableSize"):
                    self.ringstationcontroltablesize = value
                    self.ringstationcontroltablesize.value_namespace = name_space
                    self.ringstationcontroltablesize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ringstationcontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ringstationcontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ringStationControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ringStationControlEntry"):
                for c in self.ringstationcontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Ringstationcontroltable.Ringstationcontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ringstationcontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ringStationControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ringstationtable(Entity):
        """
        A list of ring station entries.  An entry will
        exist for each station that is now or has
        
        
        
        
        
        previously been detected as physically present on
        this ring.
        
        .. attribute:: ringstationentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this device
        	**type**\: list of    :py:class:`Ringstationentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationtable.Ringstationentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Ringstationtable, self).__init__()

            self.yang_name = "ringStationTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.ringstationentry = YList(self)

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
                        super(TokenRingRmonMib.Ringstationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Ringstationtable, self).__setattr__(name, value)


        class Ringstationentry(Entity):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this device.
            
            .. attribute:: ringstationifindex  <key>
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationmacaddress  <key>
            
            	The physical address of this station
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationaborterrors
            
            	The total number of abort delimiters reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcongestionerrors
            
            	The total number of receive congestion errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationduplicateaddresses
            
            	The number of times this station experienced a duplicate address error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationframecopiederrors
            
            	The total number of frame copied errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationfrequencyerrors
            
            	The total number of frequency errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinbeaconerrors
            
            	The total number of beacon frames sent by this station and detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinbursterrors
            
            	The total number of burst errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinlineerrors
            
            	The total number of line errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinsertions
            
            	The number of times the probe detected this station inserting onto the ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinternalerrors
            
            	The total number of adapter internal errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastentertime
            
            	The value of sysUpTime at the time this station last entered the ring.  If the time is unknown, this value shall be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastexittime
            
            	The value of sysUpTime at the time the probe detected that this station last exited the ring. If the time is unknown, this value shall be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastnaun
            
            	The physical address of last known NAUN of this station
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationlostframeerrors
            
            	The total number of lost frame errors reported by this station in error reporting packets detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutbeaconerrors
            
            	The total number of beacon frames detected by the probe that name this station as the NAUN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutbursterrors
            
            	The total number of burst errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutlineerrors
            
            	The total number of line errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationstationstatus
            
            	The status of this station on the ring
            	**type**\:   :py:class:`Ringstationstationstatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationtable.Ringstationentry.Ringstationstationstatus>`
            
            .. attribute:: ringstationtokenerrors
            
            	The total number of token errors reported by this station in error reporting frames detected by the probe
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Ringstationtable.Ringstationentry, self).__init__()

                self.yang_name = "ringStationEntry"
                self.yang_parent_name = "ringStationTable"

                self.ringstationifindex = YLeaf(YType.int32, "ringStationIfIndex")

                self.ringstationmacaddress = YLeaf(YType.str, "ringStationMacAddress")

                self.ringstationaborterrors = YLeaf(YType.uint32, "ringStationAbortErrors")

                self.ringstationacerrors = YLeaf(YType.uint32, "ringStationACErrors")

                self.ringstationcongestionerrors = YLeaf(YType.uint32, "ringStationCongestionErrors")

                self.ringstationduplicateaddresses = YLeaf(YType.uint32, "ringStationDuplicateAddresses")

                self.ringstationframecopiederrors = YLeaf(YType.uint32, "ringStationFrameCopiedErrors")

                self.ringstationfrequencyerrors = YLeaf(YType.uint32, "ringStationFrequencyErrors")

                self.ringstationinbeaconerrors = YLeaf(YType.uint32, "ringStationInBeaconErrors")

                self.ringstationinbursterrors = YLeaf(YType.uint32, "ringStationInBurstErrors")

                self.ringstationinlineerrors = YLeaf(YType.uint32, "ringStationInLineErrors")

                self.ringstationinsertions = YLeaf(YType.uint32, "ringStationInsertions")

                self.ringstationinternalerrors = YLeaf(YType.uint32, "ringStationInternalErrors")

                self.ringstationlastentertime = YLeaf(YType.uint32, "ringStationLastEnterTime")

                self.ringstationlastexittime = YLeaf(YType.uint32, "ringStationLastExitTime")

                self.ringstationlastnaun = YLeaf(YType.str, "ringStationLastNAUN")

                self.ringstationlostframeerrors = YLeaf(YType.uint32, "ringStationLostFrameErrors")

                self.ringstationoutbeaconerrors = YLeaf(YType.uint32, "ringStationOutBeaconErrors")

                self.ringstationoutbursterrors = YLeaf(YType.uint32, "ringStationOutBurstErrors")

                self.ringstationoutlineerrors = YLeaf(YType.uint32, "ringStationOutLineErrors")

                self.ringstationstationstatus = YLeaf(YType.enumeration, "ringStationStationStatus")

                self.ringstationtokenerrors = YLeaf(YType.uint32, "ringStationTokenErrors")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ringstationifindex",
                                "ringstationmacaddress",
                                "ringstationaborterrors",
                                "ringstationacerrors",
                                "ringstationcongestionerrors",
                                "ringstationduplicateaddresses",
                                "ringstationframecopiederrors",
                                "ringstationfrequencyerrors",
                                "ringstationinbeaconerrors",
                                "ringstationinbursterrors",
                                "ringstationinlineerrors",
                                "ringstationinsertions",
                                "ringstationinternalerrors",
                                "ringstationlastentertime",
                                "ringstationlastexittime",
                                "ringstationlastnaun",
                                "ringstationlostframeerrors",
                                "ringstationoutbeaconerrors",
                                "ringstationoutbursterrors",
                                "ringstationoutlineerrors",
                                "ringstationstationstatus",
                                "ringstationtokenerrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Ringstationtable.Ringstationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Ringstationtable.Ringstationentry, self).__setattr__(name, value)

            class Ringstationstationstatus(Enum):
                """
                Ringstationstationstatus

                The status of this station on the ring.

                .. data:: active = 1

                .. data:: inactive = 2

                .. data:: forcedRemoval = 3

                """

                active = Enum.YLeaf(1, "active")

                inactive = Enum.YLeaf(2, "inactive")

                forcedRemoval = Enum.YLeaf(3, "forcedRemoval")


            def has_data(self):
                return (
                    self.ringstationifindex.is_set or
                    self.ringstationmacaddress.is_set or
                    self.ringstationaborterrors.is_set or
                    self.ringstationacerrors.is_set or
                    self.ringstationcongestionerrors.is_set or
                    self.ringstationduplicateaddresses.is_set or
                    self.ringstationframecopiederrors.is_set or
                    self.ringstationfrequencyerrors.is_set or
                    self.ringstationinbeaconerrors.is_set or
                    self.ringstationinbursterrors.is_set or
                    self.ringstationinlineerrors.is_set or
                    self.ringstationinsertions.is_set or
                    self.ringstationinternalerrors.is_set or
                    self.ringstationlastentertime.is_set or
                    self.ringstationlastexittime.is_set or
                    self.ringstationlastnaun.is_set or
                    self.ringstationlostframeerrors.is_set or
                    self.ringstationoutbeaconerrors.is_set or
                    self.ringstationoutbursterrors.is_set or
                    self.ringstationoutlineerrors.is_set or
                    self.ringstationstationstatus.is_set or
                    self.ringstationtokenerrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ringstationifindex.yfilter != YFilter.not_set or
                    self.ringstationmacaddress.yfilter != YFilter.not_set or
                    self.ringstationaborterrors.yfilter != YFilter.not_set or
                    self.ringstationacerrors.yfilter != YFilter.not_set or
                    self.ringstationcongestionerrors.yfilter != YFilter.not_set or
                    self.ringstationduplicateaddresses.yfilter != YFilter.not_set or
                    self.ringstationframecopiederrors.yfilter != YFilter.not_set or
                    self.ringstationfrequencyerrors.yfilter != YFilter.not_set or
                    self.ringstationinbeaconerrors.yfilter != YFilter.not_set or
                    self.ringstationinbursterrors.yfilter != YFilter.not_set or
                    self.ringstationinlineerrors.yfilter != YFilter.not_set or
                    self.ringstationinsertions.yfilter != YFilter.not_set or
                    self.ringstationinternalerrors.yfilter != YFilter.not_set or
                    self.ringstationlastentertime.yfilter != YFilter.not_set or
                    self.ringstationlastexittime.yfilter != YFilter.not_set or
                    self.ringstationlastnaun.yfilter != YFilter.not_set or
                    self.ringstationlostframeerrors.yfilter != YFilter.not_set or
                    self.ringstationoutbeaconerrors.yfilter != YFilter.not_set or
                    self.ringstationoutbursterrors.yfilter != YFilter.not_set or
                    self.ringstationoutlineerrors.yfilter != YFilter.not_set or
                    self.ringstationstationstatus.yfilter != YFilter.not_set or
                    self.ringstationtokenerrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ringStationEntry" + "[ringStationIfIndex='" + self.ringstationifindex.get() + "']" + "[ringStationMacAddress='" + self.ringstationmacaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ringstationifindex.is_set or self.ringstationifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationifindex.get_name_leafdata())
                if (self.ringstationmacaddress.is_set or self.ringstationmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationmacaddress.get_name_leafdata())
                if (self.ringstationaborterrors.is_set or self.ringstationaborterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationaborterrors.get_name_leafdata())
                if (self.ringstationacerrors.is_set or self.ringstationacerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationacerrors.get_name_leafdata())
                if (self.ringstationcongestionerrors.is_set or self.ringstationcongestionerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationcongestionerrors.get_name_leafdata())
                if (self.ringstationduplicateaddresses.is_set or self.ringstationduplicateaddresses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationduplicateaddresses.get_name_leafdata())
                if (self.ringstationframecopiederrors.is_set or self.ringstationframecopiederrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationframecopiederrors.get_name_leafdata())
                if (self.ringstationfrequencyerrors.is_set or self.ringstationfrequencyerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationfrequencyerrors.get_name_leafdata())
                if (self.ringstationinbeaconerrors.is_set or self.ringstationinbeaconerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationinbeaconerrors.get_name_leafdata())
                if (self.ringstationinbursterrors.is_set or self.ringstationinbursterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationinbursterrors.get_name_leafdata())
                if (self.ringstationinlineerrors.is_set or self.ringstationinlineerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationinlineerrors.get_name_leafdata())
                if (self.ringstationinsertions.is_set or self.ringstationinsertions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationinsertions.get_name_leafdata())
                if (self.ringstationinternalerrors.is_set or self.ringstationinternalerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationinternalerrors.get_name_leafdata())
                if (self.ringstationlastentertime.is_set or self.ringstationlastentertime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationlastentertime.get_name_leafdata())
                if (self.ringstationlastexittime.is_set or self.ringstationlastexittime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationlastexittime.get_name_leafdata())
                if (self.ringstationlastnaun.is_set or self.ringstationlastnaun.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationlastnaun.get_name_leafdata())
                if (self.ringstationlostframeerrors.is_set or self.ringstationlostframeerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationlostframeerrors.get_name_leafdata())
                if (self.ringstationoutbeaconerrors.is_set or self.ringstationoutbeaconerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationoutbeaconerrors.get_name_leafdata())
                if (self.ringstationoutbursterrors.is_set or self.ringstationoutbursterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationoutbursterrors.get_name_leafdata())
                if (self.ringstationoutlineerrors.is_set or self.ringstationoutlineerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationoutlineerrors.get_name_leafdata())
                if (self.ringstationstationstatus.is_set or self.ringstationstationstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationstationstatus.get_name_leafdata())
                if (self.ringstationtokenerrors.is_set or self.ringstationtokenerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationtokenerrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ringStationIfIndex" or name == "ringStationMacAddress" or name == "ringStationAbortErrors" or name == "ringStationACErrors" or name == "ringStationCongestionErrors" or name == "ringStationDuplicateAddresses" or name == "ringStationFrameCopiedErrors" or name == "ringStationFrequencyErrors" or name == "ringStationInBeaconErrors" or name == "ringStationInBurstErrors" or name == "ringStationInLineErrors" or name == "ringStationInsertions" or name == "ringStationInternalErrors" or name == "ringStationLastEnterTime" or name == "ringStationLastExitTime" or name == "ringStationLastNAUN" or name == "ringStationLostFrameErrors" or name == "ringStationOutBeaconErrors" or name == "ringStationOutBurstErrors" or name == "ringStationOutLineErrors" or name == "ringStationStationStatus" or name == "ringStationTokenErrors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ringStationIfIndex"):
                    self.ringstationifindex = value
                    self.ringstationifindex.value_namespace = name_space
                    self.ringstationifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationMacAddress"):
                    self.ringstationmacaddress = value
                    self.ringstationmacaddress.value_namespace = name_space
                    self.ringstationmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationAbortErrors"):
                    self.ringstationaborterrors = value
                    self.ringstationaborterrors.value_namespace = name_space
                    self.ringstationaborterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationACErrors"):
                    self.ringstationacerrors = value
                    self.ringstationacerrors.value_namespace = name_space
                    self.ringstationacerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationCongestionErrors"):
                    self.ringstationcongestionerrors = value
                    self.ringstationcongestionerrors.value_namespace = name_space
                    self.ringstationcongestionerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationDuplicateAddresses"):
                    self.ringstationduplicateaddresses = value
                    self.ringstationduplicateaddresses.value_namespace = name_space
                    self.ringstationduplicateaddresses.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationFrameCopiedErrors"):
                    self.ringstationframecopiederrors = value
                    self.ringstationframecopiederrors.value_namespace = name_space
                    self.ringstationframecopiederrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationFrequencyErrors"):
                    self.ringstationfrequencyerrors = value
                    self.ringstationfrequencyerrors.value_namespace = name_space
                    self.ringstationfrequencyerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationInBeaconErrors"):
                    self.ringstationinbeaconerrors = value
                    self.ringstationinbeaconerrors.value_namespace = name_space
                    self.ringstationinbeaconerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationInBurstErrors"):
                    self.ringstationinbursterrors = value
                    self.ringstationinbursterrors.value_namespace = name_space
                    self.ringstationinbursterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationInLineErrors"):
                    self.ringstationinlineerrors = value
                    self.ringstationinlineerrors.value_namespace = name_space
                    self.ringstationinlineerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationInsertions"):
                    self.ringstationinsertions = value
                    self.ringstationinsertions.value_namespace = name_space
                    self.ringstationinsertions.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationInternalErrors"):
                    self.ringstationinternalerrors = value
                    self.ringstationinternalerrors.value_namespace = name_space
                    self.ringstationinternalerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationLastEnterTime"):
                    self.ringstationlastentertime = value
                    self.ringstationlastentertime.value_namespace = name_space
                    self.ringstationlastentertime.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationLastExitTime"):
                    self.ringstationlastexittime = value
                    self.ringstationlastexittime.value_namespace = name_space
                    self.ringstationlastexittime.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationLastNAUN"):
                    self.ringstationlastnaun = value
                    self.ringstationlastnaun.value_namespace = name_space
                    self.ringstationlastnaun.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationLostFrameErrors"):
                    self.ringstationlostframeerrors = value
                    self.ringstationlostframeerrors.value_namespace = name_space
                    self.ringstationlostframeerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationOutBeaconErrors"):
                    self.ringstationoutbeaconerrors = value
                    self.ringstationoutbeaconerrors.value_namespace = name_space
                    self.ringstationoutbeaconerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationOutBurstErrors"):
                    self.ringstationoutbursterrors = value
                    self.ringstationoutbursterrors.value_namespace = name_space
                    self.ringstationoutbursterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationOutLineErrors"):
                    self.ringstationoutlineerrors = value
                    self.ringstationoutlineerrors.value_namespace = name_space
                    self.ringstationoutlineerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationStationStatus"):
                    self.ringstationstationstatus = value
                    self.ringstationstationstatus.value_namespace = name_space
                    self.ringstationstationstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationTokenErrors"):
                    self.ringstationtokenerrors = value
                    self.ringstationtokenerrors.value_namespace = name_space
                    self.ringstationtokenerrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ringstationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ringstationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ringStationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ringStationEntry"):
                for c in self.ringstationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Ringstationtable.Ringstationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ringstationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ringStationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ringstationordertable(Entity):
        """
        A list of ring station entries for stations in
        the ring poll, ordered by their ring\-order.
        
        .. attribute:: ringstationorderentry
        
        	A collection of statistics for a particular      station that is active on a ring monitored by this device.  This table will contain information for every interface that has a ringStationControlStatus equal to valid
        	**type**\: list of    :py:class:`Ringstationorderentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationordertable.Ringstationorderentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Ringstationordertable, self).__init__()

            self.yang_name = "ringStationOrderTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.ringstationorderentry = YList(self)

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
                        super(TokenRingRmonMib.Ringstationordertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Ringstationordertable, self).__setattr__(name, value)


        class Ringstationorderentry(Entity):
            """
            A collection of statistics for a particular
            
            
            
            
            
            station that is active on a ring monitored by this
            device.  This table will contain information for
            every interface that has a
            ringStationControlStatus equal to valid.
            
            .. attribute:: ringstationorderifindex  <key>
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationorderorderindex  <key>
            
            	This index denotes the location of this station with respect to other stations on the ring.  This index is one more than the number of hops downstream that this station is from the rmon probe.  The rmon probe itself gets the value one
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationordermacaddress
            
            	The physical address of this station
            	**type**\:  str
            
            	**length:** 6
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Ringstationordertable.Ringstationorderentry, self).__init__()

                self.yang_name = "ringStationOrderEntry"
                self.yang_parent_name = "ringStationOrderTable"

                self.ringstationorderifindex = YLeaf(YType.int32, "ringStationOrderIfIndex")

                self.ringstationorderorderindex = YLeaf(YType.int32, "ringStationOrderOrderIndex")

                self.ringstationordermacaddress = YLeaf(YType.str, "ringStationOrderMacAddress")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ringstationorderifindex",
                                "ringstationorderorderindex",
                                "ringstationordermacaddress") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Ringstationordertable.Ringstationorderentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Ringstationordertable.Ringstationorderentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ringstationorderifindex.is_set or
                    self.ringstationorderorderindex.is_set or
                    self.ringstationordermacaddress.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ringstationorderifindex.yfilter != YFilter.not_set or
                    self.ringstationorderorderindex.yfilter != YFilter.not_set or
                    self.ringstationordermacaddress.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ringStationOrderEntry" + "[ringStationOrderIfIndex='" + self.ringstationorderifindex.get() + "']" + "[ringStationOrderOrderIndex='" + self.ringstationorderorderindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationOrderTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ringstationorderifindex.is_set or self.ringstationorderifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationorderifindex.get_name_leafdata())
                if (self.ringstationorderorderindex.is_set or self.ringstationorderorderindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationorderorderindex.get_name_leafdata())
                if (self.ringstationordermacaddress.is_set or self.ringstationordermacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationordermacaddress.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ringStationOrderIfIndex" or name == "ringStationOrderOrderIndex" or name == "ringStationOrderMacAddress"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ringStationOrderIfIndex"):
                    self.ringstationorderifindex = value
                    self.ringstationorderifindex.value_namespace = name_space
                    self.ringstationorderifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationOrderOrderIndex"):
                    self.ringstationorderorderindex = value
                    self.ringstationorderorderindex.value_namespace = name_space
                    self.ringstationorderorderindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationOrderMacAddress"):
                    self.ringstationordermacaddress = value
                    self.ringstationordermacaddress.value_namespace = name_space
                    self.ringstationordermacaddress.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ringstationorderentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ringstationorderentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ringStationOrderTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ringStationOrderEntry"):
                for c in self.ringstationorderentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Ringstationordertable.Ringstationorderentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ringstationorderentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ringStationOrderEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ringstationconfigcontroltable(Entity):
        """
        A list of ring station configuration control
        entries.
        
        .. attribute:: ringstationconfigcontrolentry
        
        	This entry controls active management of stations by the probe.  One entry exists in this table for each active station in the ringStationTable
        	**type**\: list of    :py:class:`Ringstationconfigcontrolentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Ringstationconfigcontroltable, self).__init__()

            self.yang_name = "ringStationConfigControlTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.ringstationconfigcontrolentry = YList(self)

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
                        super(TokenRingRmonMib.Ringstationconfigcontroltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Ringstationconfigcontroltable, self).__setattr__(name, value)


        class Ringstationconfigcontrolentry(Entity):
            """
            This entry controls active management of stations
            by the probe.  One entry exists in this table for
            each active station in the ringStationTable.
            
            .. attribute:: ringstationconfigcontrolifindex  <key>
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationconfigcontrolmacaddress  <key>
            
            	The physical address of this station
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationconfigcontrolremove
            
            	Setting this object to `removing(2)' causes a Remove Station MAC frame to be sent.  The agent will set this object to `stable(1)' after processing the request
            	**type**\:   :py:class:`Ringstationconfigcontrolremove <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.Ringstationconfigcontrolremove>`
            
            .. attribute:: ringstationconfigcontrolupdatestats
            
            	Setting this object to `updating(2)' causes the configuration information associate with this entry to be updated.  The agent will set this object to `stable(1)' after processing the request
            	**type**\:   :py:class:`Ringstationconfigcontrolupdatestats <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry.Ringstationconfigcontrolupdatestats>`
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry, self).__init__()

                self.yang_name = "ringStationConfigControlEntry"
                self.yang_parent_name = "ringStationConfigControlTable"

                self.ringstationconfigcontrolifindex = YLeaf(YType.int32, "ringStationConfigControlIfIndex")

                self.ringstationconfigcontrolmacaddress = YLeaf(YType.str, "ringStationConfigControlMacAddress")

                self.ringstationconfigcontrolremove = YLeaf(YType.enumeration, "ringStationConfigControlRemove")

                self.ringstationconfigcontrolupdatestats = YLeaf(YType.enumeration, "ringStationConfigControlUpdateStats")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ringstationconfigcontrolifindex",
                                "ringstationconfigcontrolmacaddress",
                                "ringstationconfigcontrolremove",
                                "ringstationconfigcontrolupdatestats") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry, self).__setattr__(name, value)

            class Ringstationconfigcontrolremove(Enum):
                """
                Ringstationconfigcontrolremove

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
                Ringstationconfigcontrolupdatestats

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


            def has_data(self):
                return (
                    self.ringstationconfigcontrolifindex.is_set or
                    self.ringstationconfigcontrolmacaddress.is_set or
                    self.ringstationconfigcontrolremove.is_set or
                    self.ringstationconfigcontrolupdatestats.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ringstationconfigcontrolifindex.yfilter != YFilter.not_set or
                    self.ringstationconfigcontrolmacaddress.yfilter != YFilter.not_set or
                    self.ringstationconfigcontrolremove.yfilter != YFilter.not_set or
                    self.ringstationconfigcontrolupdatestats.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ringStationConfigControlEntry" + "[ringStationConfigControlIfIndex='" + self.ringstationconfigcontrolifindex.get() + "']" + "[ringStationConfigControlMacAddress='" + self.ringstationconfigcontrolmacaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationConfigControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ringstationconfigcontrolifindex.is_set or self.ringstationconfigcontrolifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigcontrolifindex.get_name_leafdata())
                if (self.ringstationconfigcontrolmacaddress.is_set or self.ringstationconfigcontrolmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigcontrolmacaddress.get_name_leafdata())
                if (self.ringstationconfigcontrolremove.is_set or self.ringstationconfigcontrolremove.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigcontrolremove.get_name_leafdata())
                if (self.ringstationconfigcontrolupdatestats.is_set or self.ringstationconfigcontrolupdatestats.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigcontrolupdatestats.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ringStationConfigControlIfIndex" or name == "ringStationConfigControlMacAddress" or name == "ringStationConfigControlRemove" or name == "ringStationConfigControlUpdateStats"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ringStationConfigControlIfIndex"):
                    self.ringstationconfigcontrolifindex = value
                    self.ringstationconfigcontrolifindex.value_namespace = name_space
                    self.ringstationconfigcontrolifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigControlMacAddress"):
                    self.ringstationconfigcontrolmacaddress = value
                    self.ringstationconfigcontrolmacaddress.value_namespace = name_space
                    self.ringstationconfigcontrolmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigControlRemove"):
                    self.ringstationconfigcontrolremove = value
                    self.ringstationconfigcontrolremove.value_namespace = name_space
                    self.ringstationconfigcontrolremove.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigControlUpdateStats"):
                    self.ringstationconfigcontrolupdatestats = value
                    self.ringstationconfigcontrolupdatestats.value_namespace = name_space
                    self.ringstationconfigcontrolupdatestats.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ringstationconfigcontrolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ringstationconfigcontrolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ringStationConfigControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ringStationConfigControlEntry"):
                for c in self.ringstationconfigcontrolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Ringstationconfigcontroltable.Ringstationconfigcontrolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ringstationconfigcontrolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ringStationConfigControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ringstationconfigtable(Entity):
        """
        A list of configuration entries for stations on a
        ring monitored by this probe.
        
        .. attribute:: ringstationconfigentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this probe
        	**type**\: list of    :py:class:`Ringstationconfigentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Ringstationconfigtable, self).__init__()

            self.yang_name = "ringStationConfigTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.ringstationconfigentry = YList(self)

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
                        super(TokenRingRmonMib.Ringstationconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Ringstationconfigtable, self).__setattr__(name, value)


        class Ringstationconfigentry(Entity):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this probe.
            
            .. attribute:: ringstationconfigifindex  <key>
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationconfigmacaddress  <key>
            
            	The physical address of this station
            	**type**\:  str
            
            	**length:** 6
            
            .. attribute:: ringstationconfigfunctionaladdress
            
            	the functional addresses recognized by this station
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: ringstationconfiggroupaddress
            
            	The low\-order 4 octets of the group address recognized by this station
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: ringstationconfiglocation
            
            	The assigned physical location of this station
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: ringstationconfigmicrocode
            
            	The microcode EC level of this station
            	**type**\:  str
            
            	**length:** 10
            
            .. attribute:: ringstationconfigupdatetime
            
            	The value of sysUpTime at the time this configuration information was last updated (completely)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry, self).__init__()

                self.yang_name = "ringStationConfigEntry"
                self.yang_parent_name = "ringStationConfigTable"

                self.ringstationconfigifindex = YLeaf(YType.int32, "ringStationConfigIfIndex")

                self.ringstationconfigmacaddress = YLeaf(YType.str, "ringStationConfigMacAddress")

                self.ringstationconfigfunctionaladdress = YLeaf(YType.str, "ringStationConfigFunctionalAddress")

                self.ringstationconfiggroupaddress = YLeaf(YType.str, "ringStationConfigGroupAddress")

                self.ringstationconfiglocation = YLeaf(YType.str, "ringStationConfigLocation")

                self.ringstationconfigmicrocode = YLeaf(YType.str, "ringStationConfigMicrocode")

                self.ringstationconfigupdatetime = YLeaf(YType.uint32, "ringStationConfigUpdateTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ringstationconfigifindex",
                                "ringstationconfigmacaddress",
                                "ringstationconfigfunctionaladdress",
                                "ringstationconfiggroupaddress",
                                "ringstationconfiglocation",
                                "ringstationconfigmicrocode",
                                "ringstationconfigupdatetime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ringstationconfigifindex.is_set or
                    self.ringstationconfigmacaddress.is_set or
                    self.ringstationconfigfunctionaladdress.is_set or
                    self.ringstationconfiggroupaddress.is_set or
                    self.ringstationconfiglocation.is_set or
                    self.ringstationconfigmicrocode.is_set or
                    self.ringstationconfigupdatetime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ringstationconfigifindex.yfilter != YFilter.not_set or
                    self.ringstationconfigmacaddress.yfilter != YFilter.not_set or
                    self.ringstationconfigfunctionaladdress.yfilter != YFilter.not_set or
                    self.ringstationconfiggroupaddress.yfilter != YFilter.not_set or
                    self.ringstationconfiglocation.yfilter != YFilter.not_set or
                    self.ringstationconfigmicrocode.yfilter != YFilter.not_set or
                    self.ringstationconfigupdatetime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ringStationConfigEntry" + "[ringStationConfigIfIndex='" + self.ringstationconfigifindex.get() + "']" + "[ringStationConfigMacAddress='" + self.ringstationconfigmacaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/ringStationConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ringstationconfigifindex.is_set or self.ringstationconfigifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigifindex.get_name_leafdata())
                if (self.ringstationconfigmacaddress.is_set or self.ringstationconfigmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigmacaddress.get_name_leafdata())
                if (self.ringstationconfigfunctionaladdress.is_set or self.ringstationconfigfunctionaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigfunctionaladdress.get_name_leafdata())
                if (self.ringstationconfiggroupaddress.is_set or self.ringstationconfiggroupaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfiggroupaddress.get_name_leafdata())
                if (self.ringstationconfiglocation.is_set or self.ringstationconfiglocation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfiglocation.get_name_leafdata())
                if (self.ringstationconfigmicrocode.is_set or self.ringstationconfigmicrocode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigmicrocode.get_name_leafdata())
                if (self.ringstationconfigupdatetime.is_set or self.ringstationconfigupdatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ringstationconfigupdatetime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ringStationConfigIfIndex" or name == "ringStationConfigMacAddress" or name == "ringStationConfigFunctionalAddress" or name == "ringStationConfigGroupAddress" or name == "ringStationConfigLocation" or name == "ringStationConfigMicrocode" or name == "ringStationConfigUpdateTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ringStationConfigIfIndex"):
                    self.ringstationconfigifindex = value
                    self.ringstationconfigifindex.value_namespace = name_space
                    self.ringstationconfigifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigMacAddress"):
                    self.ringstationconfigmacaddress = value
                    self.ringstationconfigmacaddress.value_namespace = name_space
                    self.ringstationconfigmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigFunctionalAddress"):
                    self.ringstationconfigfunctionaladdress = value
                    self.ringstationconfigfunctionaladdress.value_namespace = name_space
                    self.ringstationconfigfunctionaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigGroupAddress"):
                    self.ringstationconfiggroupaddress = value
                    self.ringstationconfiggroupaddress.value_namespace = name_space
                    self.ringstationconfiggroupaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigLocation"):
                    self.ringstationconfiglocation = value
                    self.ringstationconfiglocation.value_namespace = name_space
                    self.ringstationconfiglocation.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigMicrocode"):
                    self.ringstationconfigmicrocode = value
                    self.ringstationconfigmicrocode.value_namespace = name_space
                    self.ringstationconfigmicrocode.value_namespace_prefix = name_space_prefix
                if(value_path == "ringStationConfigUpdateTime"):
                    self.ringstationconfigupdatetime = value
                    self.ringstationconfigupdatetime.value_namespace = name_space
                    self.ringstationconfigupdatetime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ringstationconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ringstationconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ringStationConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ringStationConfigEntry"):
                for c in self.ringstationconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Ringstationconfigtable.Ringstationconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ringstationconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ringStationConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Sourceroutingstatstable(Entity):
        """
        A list of source routing statistics entries.
        
        .. attribute:: sourceroutingstatsentry
        
        	A collection of source routing statistics kept for a particular Token Ring interface
        	**type**\: list of    :py:class:`Sourceroutingstatsentry <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry>`
        
        

        """

        _prefix = 'TOKEN-RING-RMON-MIB'

        def __init__(self):
            super(TokenRingRmonMib.Sourceroutingstatstable, self).__init__()

            self.yang_name = "sourceRoutingStatsTable"
            self.yang_parent_name = "TOKEN-RING-RMON-MIB"

            self.sourceroutingstatsentry = YList(self)

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
                        super(TokenRingRmonMib.Sourceroutingstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenRingRmonMib.Sourceroutingstatstable, self).__setattr__(name, value)


        class Sourceroutingstatsentry(Entity):
            """
            A collection of source routing statistics kept
            for a particular Token Ring interface.
            
            .. attribute:: sourceroutingstatsifindex  <key>
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which source routing statistics will be detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sourceroutingstats1hopframes
            
            	The total number of frames received whose route had 1 hop, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats2hopsframes
            
            	The total number of frames received whose route had 2 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats3hopsframes
            
            	The total number of frames received whose route had 3 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats4hopsframes
            
            	The total number of frames received whose route had 4 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats5hopsframes
            
            	The total number of frames received whose route had 5 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats6hopsframes
            
            	The total number of frames received whose route had 6 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats7hopsframes
            
            	The total number of frames received whose route had 7 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats8hopsframes
            
            	The total number of frames received whose route had 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsallroutesbroadcastframes
            
            	The total number of good frames received that were All Routes Broadcast
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsallroutesbroadcastoctets
            
            	The total number of octets in good frames received that were All Routes Broadcast
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsinframes
            
            	The count of frames sent into this ring from another ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsinoctets
            
            	The count of octets in good frames sent into this ring from another ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatslocalllcframes
            
            	The total number of frames received who had no RIF field (or had a RIF field that only included the local ring's number) and were not All Route Broadcast Frames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsmorethan8hopsframes
            
            	The total number of frames received whose route had more than 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsoutframes
            
            	The count of frames sent from this ring to another ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsoutoctets
            
            	The count of octets in good frames sent from this ring to another ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            .. attribute:: sourceroutingstatsringnumber
            
            	The ring number of the ring monitored by this entry.  When any object in this entry is created, the probe will attempt to discover the ring number.  Only after the ring number is discovered will this object be created.  After creating an object in this entry, the management station should poll this object to detect when it is created.  Only after this object is created can the management station set the sourceRoutingStatsStatus entry to valid(1)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sourceroutingstatssingleroutebroadcastframes
            
            	The total number of good frames received that were Single Route Broadcast
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatssingleroutesbroadcastoctets
            
            	The total number of octets in good frames received that were Single Route Broadcast
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsstatus
            
            	The status of this sourceRoutingStats entry
            	**type**\:   :py:class:`Entrystatus <ydk.models.cisco_ios_xe.TOKEN_RING_RMON_MIB.Entrystatus>`
            
            .. attribute:: sourceroutingstatsthroughframes
            
            	The count of frames sent from another ring, through this ring, to another ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsthroughoctets
            
            	The count of octets in good frames sent another ring, through this ring, to another ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKEN-RING-RMON-MIB'

            def __init__(self):
                super(TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry, self).__init__()

                self.yang_name = "sourceRoutingStatsEntry"
                self.yang_parent_name = "sourceRoutingStatsTable"

                self.sourceroutingstatsifindex = YLeaf(YType.int32, "sourceRoutingStatsIfIndex")

                self.sourceroutingstats1hopframes = YLeaf(YType.uint32, "sourceRoutingStats1HopFrames")

                self.sourceroutingstats2hopsframes = YLeaf(YType.uint32, "sourceRoutingStats2HopsFrames")

                self.sourceroutingstats3hopsframes = YLeaf(YType.uint32, "sourceRoutingStats3HopsFrames")

                self.sourceroutingstats4hopsframes = YLeaf(YType.uint32, "sourceRoutingStats4HopsFrames")

                self.sourceroutingstats5hopsframes = YLeaf(YType.uint32, "sourceRoutingStats5HopsFrames")

                self.sourceroutingstats6hopsframes = YLeaf(YType.uint32, "sourceRoutingStats6HopsFrames")

                self.sourceroutingstats7hopsframes = YLeaf(YType.uint32, "sourceRoutingStats7HopsFrames")

                self.sourceroutingstats8hopsframes = YLeaf(YType.uint32, "sourceRoutingStats8HopsFrames")

                self.sourceroutingstatsallroutesbroadcastframes = YLeaf(YType.uint32, "sourceRoutingStatsAllRoutesBroadcastFrames")

                self.sourceroutingstatsallroutesbroadcastoctets = YLeaf(YType.uint32, "sourceRoutingStatsAllRoutesBroadcastOctets")

                self.sourceroutingstatscreatetime = YLeaf(YType.uint32, "RMON2-MIB:sourceRoutingStatsCreateTime")

                self.sourceroutingstatsdroppedframes = YLeaf(YType.uint32, "RMON2-MIB:sourceRoutingStatsDroppedFrames")

                self.sourceroutingstatsinframes = YLeaf(YType.uint32, "sourceRoutingStatsInFrames")

                self.sourceroutingstatsinoctets = YLeaf(YType.uint32, "sourceRoutingStatsInOctets")

                self.sourceroutingstatslocalllcframes = YLeaf(YType.uint32, "sourceRoutingStatsLocalLLCFrames")

                self.sourceroutingstatsmorethan8hopsframes = YLeaf(YType.uint32, "sourceRoutingStatsMoreThan8HopsFrames")

                self.sourceroutingstatsoutframes = YLeaf(YType.uint32, "sourceRoutingStatsOutFrames")

                self.sourceroutingstatsoutoctets = YLeaf(YType.uint32, "sourceRoutingStatsOutOctets")

                self.sourceroutingstatsowner = YLeaf(YType.str, "sourceRoutingStatsOwner")

                self.sourceroutingstatsringnumber = YLeaf(YType.int32, "sourceRoutingStatsRingNumber")

                self.sourceroutingstatssingleroutebroadcastframes = YLeaf(YType.uint32, "sourceRoutingStatsSingleRouteBroadcastFrames")

                self.sourceroutingstatssingleroutesbroadcastoctets = YLeaf(YType.uint32, "sourceRoutingStatsSingleRoutesBroadcastOctets")

                self.sourceroutingstatsstatus = YLeaf(YType.enumeration, "sourceRoutingStatsStatus")

                self.sourceroutingstatsthroughframes = YLeaf(YType.uint32, "sourceRoutingStatsThroughFrames")

                self.sourceroutingstatsthroughoctets = YLeaf(YType.uint32, "sourceRoutingStatsThroughOctets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sourceroutingstatsifindex",
                                "sourceroutingstats1hopframes",
                                "sourceroutingstats2hopsframes",
                                "sourceroutingstats3hopsframes",
                                "sourceroutingstats4hopsframes",
                                "sourceroutingstats5hopsframes",
                                "sourceroutingstats6hopsframes",
                                "sourceroutingstats7hopsframes",
                                "sourceroutingstats8hopsframes",
                                "sourceroutingstatsallroutesbroadcastframes",
                                "sourceroutingstatsallroutesbroadcastoctets",
                                "sourceroutingstatscreatetime",
                                "sourceroutingstatsdroppedframes",
                                "sourceroutingstatsinframes",
                                "sourceroutingstatsinoctets",
                                "sourceroutingstatslocalllcframes",
                                "sourceroutingstatsmorethan8hopsframes",
                                "sourceroutingstatsoutframes",
                                "sourceroutingstatsoutoctets",
                                "sourceroutingstatsowner",
                                "sourceroutingstatsringnumber",
                                "sourceroutingstatssingleroutebroadcastframes",
                                "sourceroutingstatssingleroutesbroadcastoctets",
                                "sourceroutingstatsstatus",
                                "sourceroutingstatsthroughframes",
                                "sourceroutingstatsthroughoctets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.sourceroutingstatsifindex.is_set or
                    self.sourceroutingstats1hopframes.is_set or
                    self.sourceroutingstats2hopsframes.is_set or
                    self.sourceroutingstats3hopsframes.is_set or
                    self.sourceroutingstats4hopsframes.is_set or
                    self.sourceroutingstats5hopsframes.is_set or
                    self.sourceroutingstats6hopsframes.is_set or
                    self.sourceroutingstats7hopsframes.is_set or
                    self.sourceroutingstats8hopsframes.is_set or
                    self.sourceroutingstatsallroutesbroadcastframes.is_set or
                    self.sourceroutingstatsallroutesbroadcastoctets.is_set or
                    self.sourceroutingstatscreatetime.is_set or
                    self.sourceroutingstatsdroppedframes.is_set or
                    self.sourceroutingstatsinframes.is_set or
                    self.sourceroutingstatsinoctets.is_set or
                    self.sourceroutingstatslocalllcframes.is_set or
                    self.sourceroutingstatsmorethan8hopsframes.is_set or
                    self.sourceroutingstatsoutframes.is_set or
                    self.sourceroutingstatsoutoctets.is_set or
                    self.sourceroutingstatsowner.is_set or
                    self.sourceroutingstatsringnumber.is_set or
                    self.sourceroutingstatssingleroutebroadcastframes.is_set or
                    self.sourceroutingstatssingleroutesbroadcastoctets.is_set or
                    self.sourceroutingstatsstatus.is_set or
                    self.sourceroutingstatsthroughframes.is_set or
                    self.sourceroutingstatsthroughoctets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sourceroutingstatsifindex.yfilter != YFilter.not_set or
                    self.sourceroutingstats1hopframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats2hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats3hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats4hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats5hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats6hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats7hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstats8hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsallroutesbroadcastframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsallroutesbroadcastoctets.yfilter != YFilter.not_set or
                    self.sourceroutingstatscreatetime.yfilter != YFilter.not_set or
                    self.sourceroutingstatsdroppedframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsinframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsinoctets.yfilter != YFilter.not_set or
                    self.sourceroutingstatslocalllcframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsmorethan8hopsframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsoutframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsoutoctets.yfilter != YFilter.not_set or
                    self.sourceroutingstatsowner.yfilter != YFilter.not_set or
                    self.sourceroutingstatsringnumber.yfilter != YFilter.not_set or
                    self.sourceroutingstatssingleroutebroadcastframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatssingleroutesbroadcastoctets.yfilter != YFilter.not_set or
                    self.sourceroutingstatsstatus.yfilter != YFilter.not_set or
                    self.sourceroutingstatsthroughframes.yfilter != YFilter.not_set or
                    self.sourceroutingstatsthroughoctets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sourceRoutingStatsEntry" + "[sourceRoutingStatsIfIndex='" + self.sourceroutingstatsifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/sourceRoutingStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sourceroutingstatsifindex.is_set or self.sourceroutingstatsifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsifindex.get_name_leafdata())
                if (self.sourceroutingstats1hopframes.is_set or self.sourceroutingstats1hopframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats1hopframes.get_name_leafdata())
                if (self.sourceroutingstats2hopsframes.is_set or self.sourceroutingstats2hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats2hopsframes.get_name_leafdata())
                if (self.sourceroutingstats3hopsframes.is_set or self.sourceroutingstats3hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats3hopsframes.get_name_leafdata())
                if (self.sourceroutingstats4hopsframes.is_set or self.sourceroutingstats4hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats4hopsframes.get_name_leafdata())
                if (self.sourceroutingstats5hopsframes.is_set or self.sourceroutingstats5hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats5hopsframes.get_name_leafdata())
                if (self.sourceroutingstats6hopsframes.is_set or self.sourceroutingstats6hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats6hopsframes.get_name_leafdata())
                if (self.sourceroutingstats7hopsframes.is_set or self.sourceroutingstats7hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats7hopsframes.get_name_leafdata())
                if (self.sourceroutingstats8hopsframes.is_set or self.sourceroutingstats8hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstats8hopsframes.get_name_leafdata())
                if (self.sourceroutingstatsallroutesbroadcastframes.is_set or self.sourceroutingstatsallroutesbroadcastframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsallroutesbroadcastframes.get_name_leafdata())
                if (self.sourceroutingstatsallroutesbroadcastoctets.is_set or self.sourceroutingstatsallroutesbroadcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsallroutesbroadcastoctets.get_name_leafdata())
                if (self.sourceroutingstatscreatetime.is_set or self.sourceroutingstatscreatetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatscreatetime.get_name_leafdata())
                if (self.sourceroutingstatsdroppedframes.is_set or self.sourceroutingstatsdroppedframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsdroppedframes.get_name_leafdata())
                if (self.sourceroutingstatsinframes.is_set or self.sourceroutingstatsinframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsinframes.get_name_leafdata())
                if (self.sourceroutingstatsinoctets.is_set or self.sourceroutingstatsinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsinoctets.get_name_leafdata())
                if (self.sourceroutingstatslocalllcframes.is_set or self.sourceroutingstatslocalllcframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatslocalllcframes.get_name_leafdata())
                if (self.sourceroutingstatsmorethan8hopsframes.is_set or self.sourceroutingstatsmorethan8hopsframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsmorethan8hopsframes.get_name_leafdata())
                if (self.sourceroutingstatsoutframes.is_set or self.sourceroutingstatsoutframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsoutframes.get_name_leafdata())
                if (self.sourceroutingstatsoutoctets.is_set or self.sourceroutingstatsoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsoutoctets.get_name_leafdata())
                if (self.sourceroutingstatsowner.is_set or self.sourceroutingstatsowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsowner.get_name_leafdata())
                if (self.sourceroutingstatsringnumber.is_set or self.sourceroutingstatsringnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsringnumber.get_name_leafdata())
                if (self.sourceroutingstatssingleroutebroadcastframes.is_set or self.sourceroutingstatssingleroutebroadcastframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatssingleroutebroadcastframes.get_name_leafdata())
                if (self.sourceroutingstatssingleroutesbroadcastoctets.is_set or self.sourceroutingstatssingleroutesbroadcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatssingleroutesbroadcastoctets.get_name_leafdata())
                if (self.sourceroutingstatsstatus.is_set or self.sourceroutingstatsstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsstatus.get_name_leafdata())
                if (self.sourceroutingstatsthroughframes.is_set or self.sourceroutingstatsthroughframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsthroughframes.get_name_leafdata())
                if (self.sourceroutingstatsthroughoctets.is_set or self.sourceroutingstatsthroughoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sourceroutingstatsthroughoctets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sourceRoutingStatsIfIndex" or name == "sourceRoutingStats1HopFrames" or name == "sourceRoutingStats2HopsFrames" or name == "sourceRoutingStats3HopsFrames" or name == "sourceRoutingStats4HopsFrames" or name == "sourceRoutingStats5HopsFrames" or name == "sourceRoutingStats6HopsFrames" or name == "sourceRoutingStats7HopsFrames" or name == "sourceRoutingStats8HopsFrames" or name == "sourceRoutingStatsAllRoutesBroadcastFrames" or name == "sourceRoutingStatsAllRoutesBroadcastOctets" or name == "sourceRoutingStatsCreateTime" or name == "sourceRoutingStatsDroppedFrames" or name == "sourceRoutingStatsInFrames" or name == "sourceRoutingStatsInOctets" or name == "sourceRoutingStatsLocalLLCFrames" or name == "sourceRoutingStatsMoreThan8HopsFrames" or name == "sourceRoutingStatsOutFrames" or name == "sourceRoutingStatsOutOctets" or name == "sourceRoutingStatsOwner" or name == "sourceRoutingStatsRingNumber" or name == "sourceRoutingStatsSingleRouteBroadcastFrames" or name == "sourceRoutingStatsSingleRoutesBroadcastOctets" or name == "sourceRoutingStatsStatus" or name == "sourceRoutingStatsThroughFrames" or name == "sourceRoutingStatsThroughOctets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sourceRoutingStatsIfIndex"):
                    self.sourceroutingstatsifindex = value
                    self.sourceroutingstatsifindex.value_namespace = name_space
                    self.sourceroutingstatsifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats1HopFrames"):
                    self.sourceroutingstats1hopframes = value
                    self.sourceroutingstats1hopframes.value_namespace = name_space
                    self.sourceroutingstats1hopframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats2HopsFrames"):
                    self.sourceroutingstats2hopsframes = value
                    self.sourceroutingstats2hopsframes.value_namespace = name_space
                    self.sourceroutingstats2hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats3HopsFrames"):
                    self.sourceroutingstats3hopsframes = value
                    self.sourceroutingstats3hopsframes.value_namespace = name_space
                    self.sourceroutingstats3hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats4HopsFrames"):
                    self.sourceroutingstats4hopsframes = value
                    self.sourceroutingstats4hopsframes.value_namespace = name_space
                    self.sourceroutingstats4hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats5HopsFrames"):
                    self.sourceroutingstats5hopsframes = value
                    self.sourceroutingstats5hopsframes.value_namespace = name_space
                    self.sourceroutingstats5hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats6HopsFrames"):
                    self.sourceroutingstats6hopsframes = value
                    self.sourceroutingstats6hopsframes.value_namespace = name_space
                    self.sourceroutingstats6hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats7HopsFrames"):
                    self.sourceroutingstats7hopsframes = value
                    self.sourceroutingstats7hopsframes.value_namespace = name_space
                    self.sourceroutingstats7hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStats8HopsFrames"):
                    self.sourceroutingstats8hopsframes = value
                    self.sourceroutingstats8hopsframes.value_namespace = name_space
                    self.sourceroutingstats8hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsAllRoutesBroadcastFrames"):
                    self.sourceroutingstatsallroutesbroadcastframes = value
                    self.sourceroutingstatsallroutesbroadcastframes.value_namespace = name_space
                    self.sourceroutingstatsallroutesbroadcastframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsAllRoutesBroadcastOctets"):
                    self.sourceroutingstatsallroutesbroadcastoctets = value
                    self.sourceroutingstatsallroutesbroadcastoctets.value_namespace = name_space
                    self.sourceroutingstatsallroutesbroadcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsCreateTime"):
                    self.sourceroutingstatscreatetime = value
                    self.sourceroutingstatscreatetime.value_namespace = name_space
                    self.sourceroutingstatscreatetime.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsDroppedFrames"):
                    self.sourceroutingstatsdroppedframes = value
                    self.sourceroutingstatsdroppedframes.value_namespace = name_space
                    self.sourceroutingstatsdroppedframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsInFrames"):
                    self.sourceroutingstatsinframes = value
                    self.sourceroutingstatsinframes.value_namespace = name_space
                    self.sourceroutingstatsinframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsInOctets"):
                    self.sourceroutingstatsinoctets = value
                    self.sourceroutingstatsinoctets.value_namespace = name_space
                    self.sourceroutingstatsinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsLocalLLCFrames"):
                    self.sourceroutingstatslocalllcframes = value
                    self.sourceroutingstatslocalllcframes.value_namespace = name_space
                    self.sourceroutingstatslocalllcframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsMoreThan8HopsFrames"):
                    self.sourceroutingstatsmorethan8hopsframes = value
                    self.sourceroutingstatsmorethan8hopsframes.value_namespace = name_space
                    self.sourceroutingstatsmorethan8hopsframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsOutFrames"):
                    self.sourceroutingstatsoutframes = value
                    self.sourceroutingstatsoutframes.value_namespace = name_space
                    self.sourceroutingstatsoutframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsOutOctets"):
                    self.sourceroutingstatsoutoctets = value
                    self.sourceroutingstatsoutoctets.value_namespace = name_space
                    self.sourceroutingstatsoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsOwner"):
                    self.sourceroutingstatsowner = value
                    self.sourceroutingstatsowner.value_namespace = name_space
                    self.sourceroutingstatsowner.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsRingNumber"):
                    self.sourceroutingstatsringnumber = value
                    self.sourceroutingstatsringnumber.value_namespace = name_space
                    self.sourceroutingstatsringnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsSingleRouteBroadcastFrames"):
                    self.sourceroutingstatssingleroutebroadcastframes = value
                    self.sourceroutingstatssingleroutebroadcastframes.value_namespace = name_space
                    self.sourceroutingstatssingleroutebroadcastframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsSingleRoutesBroadcastOctets"):
                    self.sourceroutingstatssingleroutesbroadcastoctets = value
                    self.sourceroutingstatssingleroutesbroadcastoctets.value_namespace = name_space
                    self.sourceroutingstatssingleroutesbroadcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsStatus"):
                    self.sourceroutingstatsstatus = value
                    self.sourceroutingstatsstatus.value_namespace = name_space
                    self.sourceroutingstatsstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsThroughFrames"):
                    self.sourceroutingstatsthroughframes = value
                    self.sourceroutingstatsthroughframes.value_namespace = name_space
                    self.sourceroutingstatsthroughframes.value_namespace_prefix = name_space_prefix
                if(value_path == "sourceRoutingStatsThroughOctets"):
                    self.sourceroutingstatsthroughoctets = value
                    self.sourceroutingstatsthroughoctets.value_namespace = name_space
                    self.sourceroutingstatsthroughoctets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sourceroutingstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sourceroutingstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sourceRoutingStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sourceRoutingStatsEntry"):
                for c in self.sourceroutingstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenRingRmonMib.Sourceroutingstatstable.Sourceroutingstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sourceroutingstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sourceRoutingStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ringstationconfigcontroltable is not None and self.ringstationconfigcontroltable.has_data()) or
            (self.ringstationconfigtable is not None and self.ringstationconfigtable.has_data()) or
            (self.ringstationcontroltable is not None and self.ringstationcontroltable.has_data()) or
            (self.ringstationordertable is not None and self.ringstationordertable.has_data()) or
            (self.ringstationtable is not None and self.ringstationtable.has_data()) or
            (self.sourceroutingstatstable is not None and self.sourceroutingstatstable.has_data()) or
            (self.tokenringmlhistorytable is not None and self.tokenringmlhistorytable.has_data()) or
            (self.tokenringmlstatstable is not None and self.tokenringmlstatstable.has_data()) or
            (self.tokenringphistorytable is not None and self.tokenringphistorytable.has_data()) or
            (self.tokenringpstatstable is not None and self.tokenringpstatstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ringstationconfigcontroltable is not None and self.ringstationconfigcontroltable.has_operation()) or
            (self.ringstationconfigtable is not None and self.ringstationconfigtable.has_operation()) or
            (self.ringstationcontroltable is not None and self.ringstationcontroltable.has_operation()) or
            (self.ringstationordertable is not None and self.ringstationordertable.has_operation()) or
            (self.ringstationtable is not None and self.ringstationtable.has_operation()) or
            (self.sourceroutingstatstable is not None and self.sourceroutingstatstable.has_operation()) or
            (self.tokenringmlhistorytable is not None and self.tokenringmlhistorytable.has_operation()) or
            (self.tokenringmlstatstable is not None and self.tokenringmlstatstable.has_operation()) or
            (self.tokenringphistorytable is not None and self.tokenringphistorytable.has_operation()) or
            (self.tokenringpstatstable is not None and self.tokenringpstatstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB" + path_buffer

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

        if (child_yang_name == "ringStationConfigControlTable"):
            if (self.ringstationconfigcontroltable is None):
                self.ringstationconfigcontroltable = TokenRingRmonMib.Ringstationconfigcontroltable()
                self.ringstationconfigcontroltable.parent = self
                self._children_name_map["ringstationconfigcontroltable"] = "ringStationConfigControlTable"
            return self.ringstationconfigcontroltable

        if (child_yang_name == "ringStationConfigTable"):
            if (self.ringstationconfigtable is None):
                self.ringstationconfigtable = TokenRingRmonMib.Ringstationconfigtable()
                self.ringstationconfigtable.parent = self
                self._children_name_map["ringstationconfigtable"] = "ringStationConfigTable"
            return self.ringstationconfigtable

        if (child_yang_name == "ringStationControlTable"):
            if (self.ringstationcontroltable is None):
                self.ringstationcontroltable = TokenRingRmonMib.Ringstationcontroltable()
                self.ringstationcontroltable.parent = self
                self._children_name_map["ringstationcontroltable"] = "ringStationControlTable"
            return self.ringstationcontroltable

        if (child_yang_name == "ringStationOrderTable"):
            if (self.ringstationordertable is None):
                self.ringstationordertable = TokenRingRmonMib.Ringstationordertable()
                self.ringstationordertable.parent = self
                self._children_name_map["ringstationordertable"] = "ringStationOrderTable"
            return self.ringstationordertable

        if (child_yang_name == "ringStationTable"):
            if (self.ringstationtable is None):
                self.ringstationtable = TokenRingRmonMib.Ringstationtable()
                self.ringstationtable.parent = self
                self._children_name_map["ringstationtable"] = "ringStationTable"
            return self.ringstationtable

        if (child_yang_name == "sourceRoutingStatsTable"):
            if (self.sourceroutingstatstable is None):
                self.sourceroutingstatstable = TokenRingRmonMib.Sourceroutingstatstable()
                self.sourceroutingstatstable.parent = self
                self._children_name_map["sourceroutingstatstable"] = "sourceRoutingStatsTable"
            return self.sourceroutingstatstable

        if (child_yang_name == "tokenRingMLHistoryTable"):
            if (self.tokenringmlhistorytable is None):
                self.tokenringmlhistorytable = TokenRingRmonMib.Tokenringmlhistorytable()
                self.tokenringmlhistorytable.parent = self
                self._children_name_map["tokenringmlhistorytable"] = "tokenRingMLHistoryTable"
            return self.tokenringmlhistorytable

        if (child_yang_name == "tokenRingMLStatsTable"):
            if (self.tokenringmlstatstable is None):
                self.tokenringmlstatstable = TokenRingRmonMib.Tokenringmlstatstable()
                self.tokenringmlstatstable.parent = self
                self._children_name_map["tokenringmlstatstable"] = "tokenRingMLStatsTable"
            return self.tokenringmlstatstable

        if (child_yang_name == "tokenRingPHistoryTable"):
            if (self.tokenringphistorytable is None):
                self.tokenringphistorytable = TokenRingRmonMib.Tokenringphistorytable()
                self.tokenringphistorytable.parent = self
                self._children_name_map["tokenringphistorytable"] = "tokenRingPHistoryTable"
            return self.tokenringphistorytable

        if (child_yang_name == "tokenRingPStatsTable"):
            if (self.tokenringpstatstable is None):
                self.tokenringpstatstable = TokenRingRmonMib.Tokenringpstatstable()
                self.tokenringpstatstable.parent = self
                self._children_name_map["tokenringpstatstable"] = "tokenRingPStatsTable"
            return self.tokenringpstatstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ringStationConfigControlTable" or name == "ringStationConfigTable" or name == "ringStationControlTable" or name == "ringStationOrderTable" or name == "ringStationTable" or name == "sourceRoutingStatsTable" or name == "tokenRingMLHistoryTable" or name == "tokenRingMLStatsTable" or name == "tokenRingPHistoryTable" or name == "tokenRingPStatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TokenRingRmonMib()
        return self._top_entity

