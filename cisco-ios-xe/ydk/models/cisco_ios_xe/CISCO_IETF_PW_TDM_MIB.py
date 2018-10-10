""" CISCO_IETF_PW_TDM_MIB 

This MIB contains managed object definitions for
encapsulating TDM (T1,E1, T3, E3, NxDS0) as
pseudo\-wires over packet\-switching networks (PSN).

This MIB supplements the CISCO\-IETF\-PW\-MIB.
The CISCO\-IETF\-PW\-MIB contains structures and MIB
associations generic to Pseudo\-Wire (PW) emulation.
PW\-specific MIBs (such as this) contain config and stats for
specific PW types.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIETFPWTDMMIB(Entity):
    """
    
    
    .. attribute:: cpwctdmobjects
    
    	
    	**type**\:  :py:class:`CpwCTDMObjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMObjects>`
    
    .. attribute:: cpwctdmtable
    
    	This table contains basic information including ifIndex, and pointers to entries in the relevant TDM config tables for this TDM PW
    	**type**\:  :py:class:`CpwCTDMTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMTable>`
    
    .. attribute:: cpwctdmcfgtable
    
    	This table contains a set of parameters that may be referenced by one or more TDM PWs in cpwCTDMTable
    	**type**\:  :py:class:`CpwCTDMCfgTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMCfgTable>`
    
    .. attribute:: cpwctdmperfcurrenttable
    
    	This table provides TDM PW performance information. This includes current 15 minute interval counts.   The table includes counters that work together to integrate errors and the lack of errors on the TDM PW. An error is caused by a missing packet. Missing packet can be a result of, packet loss in the network, (uncorrectable) packet out of sequence, packet length error, jitter buffer overflow, and jitter buffer underflow. The result is declaring whether or not the TDM PW is in Loss of Packet (LOPS) state
    	**type**\:  :py:class:`CpwCTDMPerfCurrentTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable>`
    
    .. attribute:: cpwctdmperfintervaltable
    
    	This table provides performance information per TDM PW similar to the cpwCTDMPerfCurrentTable above. However, these counts represent historical 15 minute intervals. Typically, this table will have a maximum of 96 entries for a 24 hour period, but is not limited to this
    	**type**\:  :py:class:`CpwCTDMPerfIntervalTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable>`
    
    .. attribute:: cpwctdmperf1dayintervaltable
    
    	This table provides performance information per TDM PW similar to the cpwCTDMPerfIntervalTable above. However, these counters represent historical 1 day intervals up to one full month. The table consists of real time data, as such it is not persistence across re\-boot
    	**type**\:  :py:class:`CpwCTDMPerf1DayIntervalTable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-TDM-MIB'
    _revision = '2006-07-21'

    def __init__(self):
        super(CISCOIETFPWTDMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-TDM-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpwCTDMObjects", ("cpwctdmobjects", CISCOIETFPWTDMMIB.CpwCTDMObjects)), ("cpwCTDMTable", ("cpwctdmtable", CISCOIETFPWTDMMIB.CpwCTDMTable)), ("cpwCTDMCfgTable", ("cpwctdmcfgtable", CISCOIETFPWTDMMIB.CpwCTDMCfgTable)), ("cpwCTDMPerfCurrentTable", ("cpwctdmperfcurrenttable", CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable)), ("cpwCTDMPerfIntervalTable", ("cpwctdmperfintervaltable", CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable)), ("cpwCTDMPerf1DayIntervalTable", ("cpwctdmperf1dayintervaltable", CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable))])
        self._leafs = OrderedDict()

        self.cpwctdmobjects = CISCOIETFPWTDMMIB.CpwCTDMObjects()
        self.cpwctdmobjects.parent = self
        self._children_name_map["cpwctdmobjects"] = "cpwCTDMObjects"

        self.cpwctdmtable = CISCOIETFPWTDMMIB.CpwCTDMTable()
        self.cpwctdmtable.parent = self
        self._children_name_map["cpwctdmtable"] = "cpwCTDMTable"

        self.cpwctdmcfgtable = CISCOIETFPWTDMMIB.CpwCTDMCfgTable()
        self.cpwctdmcfgtable.parent = self
        self._children_name_map["cpwctdmcfgtable"] = "cpwCTDMCfgTable"

        self.cpwctdmperfcurrenttable = CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable()
        self.cpwctdmperfcurrenttable.parent = self
        self._children_name_map["cpwctdmperfcurrenttable"] = "cpwCTDMPerfCurrentTable"

        self.cpwctdmperfintervaltable = CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable()
        self.cpwctdmperfintervaltable.parent = self
        self._children_name_map["cpwctdmperfintervaltable"] = "cpwCTDMPerfIntervalTable"

        self.cpwctdmperf1dayintervaltable = CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable()
        self.cpwctdmperf1dayintervaltable.parent = self
        self._children_name_map["cpwctdmperf1dayintervaltable"] = "cpwCTDMPerf1DayIntervalTable"
        self._segment_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIETFPWTDMMIB, [], name, value)


    class CpwCTDMObjects(Entity):
        """
        
        
        .. attribute:: cpwctdmcfgindexnext
        
        	This object contains the value to be used for cpwCTDMCfgIndex when creating entries in the cpwCTDMCfgTable. The value 0 indicates that no unassigned entries are available.  To obtain the value of cpwCTDMCfgIndexNext for a new entry in the cpwCTDMCfgTable, the manager issues a management protocol retrieval operation. The agent will determine through its local policy when this index value will be made available for reuse
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CISCOIETFPWTDMMIB.CpwCTDMObjects, self).__init__()

            self.yang_name = "cpwCTDMObjects"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpwctdmcfgindexnext', (YLeaf(YType.uint32, 'cpwCTDMCfgIndexNext'), ['int'])),
            ])
            self.cpwctdmcfgindexnext = None
            self._segment_path = lambda: "cpwCTDMObjects"
            self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMObjects, ['cpwctdmcfgindexnext'], name, value)


    class CpwCTDMTable(Entity):
        """
        This table contains basic information including ifIndex,
        and pointers to entries in the relevant TDM config
        tables for this TDM PW.
        
        .. attribute:: cpwctdmentry
        
        	This table is indexed by the same index that was created for the associated entry in the VC Table (in the CISCO\-IETF\-PW\-MIB).    \- The CpwVcIndex.  An entry is created in this table by the agent for every entry in the cpwVcTable with a cpwVcType equal to one of the following\: e1Satop(12), t1Satop(13), e3Satop(14), t3Satop(15), basicCesPsn(16), basicTdmIp(17),  tdmCasCesPsn(18), tdmCasTdmIp(19)
        	**type**\: list of  		 :py:class:`CpwCTDMEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CISCOIETFPWTDMMIB.CpwCTDMTable, self).__init__()

            self.yang_name = "cpwCTDMTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwCTDMEntry", ("cpwctdmentry", CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry))])
            self._leafs = OrderedDict()

            self.cpwctdmentry = YList(self)
            self._segment_path = lambda: "cpwCTDMTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMTable, [], name, value)


        class CpwCTDMEntry(Entity):
            """
            This table is indexed by the same index that was
            created for the associated entry in the VC Table
            (in the CISCO\-IETF\-PW\-MIB).
            
              \- The CpwVcIndex.
            
            An entry is created in this table by the agent for every
            entry in the cpwVcTable with a cpwVcType equal to one of the
            following\:
            e1Satop(12), t1Satop(13), e3Satop(14), t3Satop(15),
            basicCesPsn(16), basicTdmIp(17),  tdmCasCesPsn(18),
            tdmCasTdmIp(19).
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            .. attribute:: cpwctdmrate
            
            	The parameter represents the bit\-rate of the TDM service in multiples of the 'basic' 64 Kbit/s rate. It complements the definition of cpwVcType used in CISCO\-IETF\-PW\-MIB. For structure\-agnostic the following should be used\: a) Satop E1 \- 32 b) Satop T1 emulation\:    i)   MUST be set to 24 in the basic emulation mode    ii)  MUST be set to 25 for the 'Octet\-aligned T1'         emulation mode c) Satop E3 \- 535 d) Satop T3 \- 699 For all kinds of structure\-aware emulation, this parameter MUST be set to N where N is the number of DS0 channels in the corresponding attachment circuit
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwctdmifindex
            
            	This is a unique index within the ifTable. It represents the interface index of the full link or the interface index for the bundle holding the group of time slots to be transmitted via this PW connection.  A value of zero indicates an interface index that has yet to be determined. Once set, if the TDM ifIndex is (for some reason) later removed, the agent SHOULD delete the associated PW rows (e.g., this cpwCTDMTable entry). If the agent does not delete the rows,  the agent MUST set this object to zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwcgentdmcfgindex
            
            	Index to the generic parameters in the TDM configuration table that appears in this MIB module. It is likely that multiple TDM PWs of the same characteristic will share a single TDM Cfg entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwcreltdmcfgindex
            
            	Index to the relevant TDM configuration table entry that appears in one of the related MIB modules such as TDMoIP or CESoPSN. It is likely that multiple TDM PWs of the same characteristic will share a single configuration entry of the relevant type. The value 0 implies no entry in other related MIB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmconfigerror
            
            	Any of the bits are set if the local configuration is not compatible with the peer configuration as available from the various parameters options.  \-tdmTypeIncompatible bit is set if the local configuration is not carrying the same TDM type as the peer configuration.  \-peerRtpIncompatible bit is set if the local configuration is configured to send RTP packets for this PW, and the remote is not capable of accepting RTP packets.  \-peerPayloadSizeIncompatible bit is set if the local configuration is not carrying the same Payload Size as the peer configuration
            	**type**\:  :py:class:`CpwCTDMConfigError <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry.CpwCTDMConfigError>`
            
            .. attribute:: cpwctdmtimeelapsed
            
            	The number of seconds, including partial seconds, that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 1..900
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmvalidintervals
            
            	The number of previous 15\-minute intervals for which data was collected. An agent with TDM capability must be capable of supporting at least n intervals. The minimum value of n is 4, The default of n is 32 and the maximum value of n is 96. The value will be <n> unless the measurement was (re\-) started within the last (<n>\*15) minutes, in which case the value will be the number of complete 15 minute intervals for which the agent has at least some data. In certain cases(e.g., in the case where the agent is a proxy) it is possible that some intervals are unavailable. In this case, this interval is the maximum interval number for which data is available
            	**type**\: int
            
            	**range:** 0..96
            
            	**units**\: minutes
            
            .. attribute:: cpwctdmvaliddayintervals
            
            	The number of previous days for which data was collected. An agent with TDM capability must be capable of supporting at least n intervals. The minimum value of n is 1, The default of n is 1 and the maximum value of n is 30
            	**type**\: int
            
            	**range:** 0..30
            
            	**units**\: days
            
            .. attribute:: cpwctdmcurrentindications
            
            	The following defects should be detected and reported upon request\:  \-Stray packets MAY be detected by the PSN and multiplexing layers. Stray packets MUST be discarded by the CE\-bound IWF and their detection MUST NOT affect mechanisms for detection of packet loss.  \-Malformed packets are detected by mismatch between the expected packet size (taking the value of the L bit into account) and the actual packet size inferred from the PSN and multiplexing layers. Malformed in\-order packets MUST be discarded by the CE\-bound IWF and replacement data generated as for lost packets.  \-Excessive packet loss rate is detected by computing the average packet loss rate over the value of cpwCTDMAvePktLossTimeWindow and comparing it with a preconfigured threshold [SATOP].  \-Buffer overrun is detected in the normal operation state when the CE bound IWF's jitter buffer cannot accommodate newly arrived packets.  \-Remote packet loss is indicated by reception of packets  with their R bit set.  \-Packet misorder is detected by looking at the Sequence number provided by the control word.  \-TDM Fault, if L bit in the control word is set, it indicates that TDM data carried in the payload is invalid due an attachment circuit fault.  When the L bit is set the payload MAY be omitted in order to conserve bandwidth.  Note\: the algorithm used to capture these indications is implementation specific
            	**type**\:  :py:class:`CpwCTDMCurrentIndications <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry.CpwCTDMCurrentIndications>`
            
            .. attribute:: cpwctdmlatchedindications
            
            	The state of TDM indicators when the TDM PW last declared an error second (either as ES, SES or a second with errors inside a UAS) condition. At this time, only LOPS can create a failure. Since indicators other than LOPS are useful, all are latched here. For bit definitions, see cpwCTDMCurrentIndications above.  Note\: the algorithm used to latch these indications when entering a defect state is implementation specific
            	**type**\:  :py:class:`CpwCTDMLatchedIndications <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry.CpwCTDMLatchedIndications>`
            
            .. attribute:: cpwctdmlastestimestamp
            
            	The value of sysUpTime at the most recent occasion at which the TDM PW entered the ES or SES state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry, self).__init__()

                self.yang_name = "cpwCTDMEntry"
                self.yang_parent_name = "cpwCTDMTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwctdmrate', (YLeaf(YType.int32, 'cpwCTDMRate'), ['int'])),
                    ('cpwctdmifindex', (YLeaf(YType.int32, 'cpwCTDMIfIndex'), ['int'])),
                    ('cpwcgentdmcfgindex', (YLeaf(YType.uint32, 'cpwCGenTDMCfgIndex'), ['int'])),
                    ('cpwcreltdmcfgindex', (YLeaf(YType.uint32, 'cpwCRelTDMCfgIndex'), ['int'])),
                    ('cpwctdmconfigerror', (YLeaf(YType.bits, 'cpwCTDMConfigError'), ['Bits'])),
                    ('cpwctdmtimeelapsed', (YLeaf(YType.int32, 'cpwCTDMTimeElapsed'), ['int'])),
                    ('cpwctdmvalidintervals', (YLeaf(YType.int32, 'cpwCTDMValidIntervals'), ['int'])),
                    ('cpwctdmvaliddayintervals', (YLeaf(YType.int32, 'cpwCTDMValidDayIntervals'), ['int'])),
                    ('cpwctdmcurrentindications', (YLeaf(YType.bits, 'cpwCTDMCurrentIndications'), ['Bits'])),
                    ('cpwctdmlatchedindications', (YLeaf(YType.bits, 'cpwCTDMLatchedIndications'), ['Bits'])),
                    ('cpwctdmlastestimestamp', (YLeaf(YType.uint32, 'cpwCTDMLastEsTimeStamp'), ['int'])),
                ])
                self.cpwvcindex = None
                self.cpwctdmrate = None
                self.cpwctdmifindex = None
                self.cpwcgentdmcfgindex = None
                self.cpwcreltdmcfgindex = None
                self.cpwctdmconfigerror = Bits()
                self.cpwctdmtimeelapsed = None
                self.cpwctdmvalidintervals = None
                self.cpwctdmvaliddayintervals = None
                self.cpwctdmcurrentindications = Bits()
                self.cpwctdmlatchedindications = Bits()
                self.cpwctdmlastestimestamp = None
                self._segment_path = lambda: "cpwCTDMEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMTable.CpwCTDMEntry, ['cpwvcindex', 'cpwctdmrate', 'cpwctdmifindex', 'cpwcgentdmcfgindex', 'cpwcreltdmcfgindex', 'cpwctdmconfigerror', 'cpwctdmtimeelapsed', 'cpwctdmvalidintervals', 'cpwctdmvaliddayintervals', 'cpwctdmcurrentindications', 'cpwctdmlatchedindications', 'cpwctdmlastestimestamp'], name, value)


    class CpwCTDMCfgTable(Entity):
        """
        This table contains a set of parameters that may be
        referenced by one or more TDM PWs in cpwCTDMTable.
        
        .. attribute:: cpwctdmcfgentry
        
        	These parameters define the characteristics of a TDM PW. They are grouped here to ease NMS burden. Once an entry is created here it may be re\-used by many PWs
        	**type**\: list of  		 :py:class:`CpwCTDMCfgEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CISCOIETFPWTDMMIB.CpwCTDMCfgTable, self).__init__()

            self.yang_name = "cpwCTDMCfgTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwCTDMCfgEntry", ("cpwctdmcfgentry", CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry))])
            self._leafs = OrderedDict()

            self.cpwctdmcfgentry = YList(self)
            self._segment_path = lambda: "cpwCTDMCfgTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMCfgTable, [], name, value)


        class CpwCTDMCfgEntry(Entity):
            """
            These parameters define the characteristics of a
            TDM PW. They are grouped here to ease NMS burden.
            Once an entry is created here it may be re\-used
            by many PWs.
            
            .. attribute:: cpwctdmcfgindex  (key)
            
            	Index to an entry in this table. The value is a copy of the assigned cpwCTDMCfgIndexNext
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmcfgconferr
            
            	This object indicates the various configuration errors, illegal settings within the cpwCTDMCfg table. The errors can be due to several reasons, like Payload size mismatch or Jitter Buffer depth value mistmatch.   payloadSize \- This bit is set if there is Payload size               mismatch between the local and peer               configurations.  jtrBfrDepth \- This bit is set if there is Jitter Buffer               depth value mistmatch. other       \- This bit is set if the error is not due to               payloadSize and jtrBfrDepth mismatch
            	**type**\:  :py:class:`CpwCTDMCfgConfErr <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgConfErr>`
            
            .. attribute:: cpwctdmcfgpayloadsize
            
            	The value of this object indicates the PayLoad Size (in bytes) to be defined during the PW setUp. Upon TX, implementation must be capable of carrying that amount of bytes. Upon RX, when the LEN field is set to 0, the payload of packet  MUST assume this size, and if the actual packet size is inconsistent with this length, the packet MUST be considered to be malformed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpwctdmcfgpktreorder
            
            	If set to true, CE bound packets are queued in the jitter buffer, out of order packets are re\-ordered. The maximum sequence number differential (i.e., the range in which re\-sequencing can occur) is dependant on the depth of the jitter buffer. See cpwCTDMCfgJtrBfrDepth
            	**type**\: bool
            
            .. attribute:: cpwctdmcfgrtphdrused
            
            	If the value of this object is set to false, then a RTP header is not pre\-pended to the TDM packet
            	**type**\: bool
            
            .. attribute:: cpwctdmcfgjtrbfrdepth
            
            	The size of this buffer SHOULD be locally configured to allow accommodation to the PSN\-specific packet delay variation.  If configured to a value not supported by the implementation, the agent MUST return an error code 'jtrBfrDepth' in 'cpwCTDMConfigError '. Jitter buffers are a limited resource to be managed. The actual size should be at least twice as big as the value of cpwCTDMCfgJtrBfrDepth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: microsecond
            
            .. attribute:: cpwctdmcfgpayloadsuppression
            
            	This object indicates whether the Payload suppression is eanbled or disabled. Payload MAY be omitted in order to conserve bandwidth.  enable  \- Payload suppression is allowed. disable \- No Payload suppresion under any condition
            	**type**\:  :py:class:`CpwCTDMCfgPayloadSuppression <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgPayloadSuppression>`
            
            .. attribute:: cpwctdmcfgconsecpktsinsynch
            
            	The number of consecutive packets with sequential sequence numbers that are required to exit the Loss of Packets (LOPS) state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmcfgconsecmisspktsoutsynch
            
            	The number of consecutive missing packets that are required to enter the LOPS state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmcfgsetup2synchtimeout
            
            	The amount of time the host should wait before declaring the pseudo wire in down state,  if the number of consecutive TDM packets that have been received after changing the administrative status to up and after finalization of signaling (if supported) between the two PEs is smaller than cpwCTDMCfgConsecPktsInSynch. Once the the PW has OperStatus of 'up' this parameter is no longer valid. This parameter is defined to ensure that the host does not prematurely inform failure of the PW. In particular PW 'down' notifications should not be sent before expiration of this timer. This parameter is valid only after adminisrative changes of the status of the PW. If the PW fails due to network impairments a 'down' notification should be sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: millisecond
            
            .. attribute:: cpwctdmcfgpktreplacepolicy
            
            	This parameter determines the value to be played when CE bound packets have over/underflow the jitter buffer, or are missing for any reason. This AIS (Alarm Indication Signal) pattern is sent (played) on the TDM line.  ais                    \- AIS (Alarm Indication Signal)                          pattern is sent (played) on                          the TDM line.  implementationSpecific \- Implementation specific pattern is                          sent on the TDM line
            	**type**\:  :py:class:`CpwCTDMCfgPktReplacePolicy <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgPktReplacePolicy>`
            
            .. attribute:: cpwctdmcfgavepktlosstimewindow
            
            	The length of time over which the average packet loss rate should be computed to detect Excessive packet loss rate
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: millisecond
            
            .. attribute:: cpwctdmcfgexcessivepktlossthreshold
            
            	Excessive packet loss rate is detected by computing the average packetloss rate over a  cpwCTDMCfgAvePktLossTimeWindow amount of time and comparing it with this threshold value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmcfgalarmthreshold
            
            	Alarms are only reported when the defect state persists for the length of time specified by this object. The object's unit is millisec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cpwctdmcfgclearalarmthreshold
            
            	Alarm MUST be cleared after the corresponding defect is undetected for the amount of time specified by this object. The object's unit is millisec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cpwctdmcfgmissingpktstoses
            
            	Number of missing packets detected (consecutive or not) within a 1 second window to cause a Severely Error Second (SES) to be counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmcfgtimestampmode
            
            	Timestamp generation MAY be used in one of the following modes\: 1. Absolute mode\: the PSN\-bound IWF sets timestamps  using the clock recovered from the incoming TDM attachment  circuit. As a consequence, the timestamps are closely  correlated with the sequence numbers. All TDM   implementations that support usage of the RTP header MUST  support this mode. 2. Differential mode\: Both IWFs have access to a common  high\-quality timing source, and this source is used for  timestamp generation. Support of this mode is OPTIONAL
            	**type**\:  :py:class:`CpwCTDMCfgTimestampMode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgTimestampMode>`
            
            .. attribute:: cpwctdmcfgstoragetype
            
            	This variable indicates the storage type for this row. The following are the read\-write objects in permanent(4) rows, that an agent must allow to be writable\: cpwCTDMCfgPayloadSize, cpwCTDMCfgPktReorder, cpwCTDMCfgRtpHdrUsed, cpwCTDMCfgJtrBfrDepth, cpwCTDMCfgPayloadSuppression, cpwCTDMCfgConfErr
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: cpwctdmcfgrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  All of the columnar objects have to be set to valid values before the row can be activated. Default value will be automatically provisioned if for those objects not specified during row creation.  No objects in cascading tables have to be populated with related data before the row can be activated.  The following objects cannot be modified if the RowStatus is active\: cpwCTDMCfgPayloadSize, cpwCTDMCfgRtpHdrUsed, cpwCTDMCfgJtrBfrDepth, and cpwCTDMCfgPayloadSuppression.  If the RowStatus is active, the following parameters can be modified\:  cpwCTDMCfgConfErr, cpwCTDMCfgPktReorder,  cpwCTDMCfgConsecPktsInSynch, cpwCTDMCfgConsecMissPktsOutSynch, cpwCTDMCfgSetUp2SynchTimeOut, cpwCTDMCfgPktReplacePolicy, cpwCTDMCfgAvePktLossTimeWindow,  cpwCTDMCfgExcessivePktLossThreshold, cpwCTDMCfgAlarmThreshold, cpwCTDMCfgClearAlarmThreshold, cpwCTDMCfgMissingPktsToSes, cpwCTDMCfgTimestampMode, cpwCTDMCfgStorageType.  A row may be deleted by setting the RowStatus to 'destroy'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry, self).__init__()

                self.yang_name = "cpwCTDMCfgEntry"
                self.yang_parent_name = "cpwCTDMCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwctdmcfgindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwctdmcfgindex', (YLeaf(YType.uint32, 'cpwCTDMCfgIndex'), ['int'])),
                    ('cpwctdmcfgconferr', (YLeaf(YType.bits, 'cpwCTDMCfgConfErr'), ['Bits'])),
                    ('cpwctdmcfgpayloadsize', (YLeaf(YType.uint32, 'cpwCTDMCfgPayloadSize'), ['int'])),
                    ('cpwctdmcfgpktreorder', (YLeaf(YType.boolean, 'cpwCTDMCfgPktReorder'), ['bool'])),
                    ('cpwctdmcfgrtphdrused', (YLeaf(YType.boolean, 'cpwCTDMCfgRtpHdrUsed'), ['bool'])),
                    ('cpwctdmcfgjtrbfrdepth', (YLeaf(YType.uint32, 'cpwCTDMCfgJtrBfrDepth'), ['int'])),
                    ('cpwctdmcfgpayloadsuppression', (YLeaf(YType.enumeration, 'cpwCTDMCfgPayloadSuppression'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CISCOIETFPWTDMMIB', 'CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgPayloadSuppression')])),
                    ('cpwctdmcfgconsecpktsinsynch', (YLeaf(YType.uint32, 'cpwCTDMCfgConsecPktsInSynch'), ['int'])),
                    ('cpwctdmcfgconsecmisspktsoutsynch', (YLeaf(YType.uint32, 'cpwCTDMCfgConsecMissPktsOutSynch'), ['int'])),
                    ('cpwctdmcfgsetup2synchtimeout', (YLeaf(YType.uint32, 'cpwCTDMCfgSetUp2SynchTimeOut'), ['int'])),
                    ('cpwctdmcfgpktreplacepolicy', (YLeaf(YType.enumeration, 'cpwCTDMCfgPktReplacePolicy'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CISCOIETFPWTDMMIB', 'CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgPktReplacePolicy')])),
                    ('cpwctdmcfgavepktlosstimewindow', (YLeaf(YType.int32, 'cpwCTDMCfgAvePktLossTimeWindow'), ['int'])),
                    ('cpwctdmcfgexcessivepktlossthreshold', (YLeaf(YType.uint32, 'cpwCTDMCfgExcessivePktLossThreshold'), ['int'])),
                    ('cpwctdmcfgalarmthreshold', (YLeaf(YType.uint32, 'cpwCTDMCfgAlarmThreshold'), ['int'])),
                    ('cpwctdmcfgclearalarmthreshold', (YLeaf(YType.uint32, 'cpwCTDMCfgClearAlarmThreshold'), ['int'])),
                    ('cpwctdmcfgmissingpktstoses', (YLeaf(YType.uint32, 'cpwCTDMCfgMissingPktsToSes'), ['int'])),
                    ('cpwctdmcfgtimestampmode', (YLeaf(YType.enumeration, 'cpwCTDMCfgTimestampMode'), [('ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB', 'CISCOIETFPWTDMMIB', 'CpwCTDMCfgTable.CpwCTDMCfgEntry.CpwCTDMCfgTimestampMode')])),
                    ('cpwctdmcfgstoragetype', (YLeaf(YType.enumeration, 'cpwCTDMCfgStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('cpwctdmcfgrowstatus', (YLeaf(YType.enumeration, 'cpwCTDMCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cpwctdmcfgindex = None
                self.cpwctdmcfgconferr = Bits()
                self.cpwctdmcfgpayloadsize = None
                self.cpwctdmcfgpktreorder = None
                self.cpwctdmcfgrtphdrused = None
                self.cpwctdmcfgjtrbfrdepth = None
                self.cpwctdmcfgpayloadsuppression = None
                self.cpwctdmcfgconsecpktsinsynch = None
                self.cpwctdmcfgconsecmisspktsoutsynch = None
                self.cpwctdmcfgsetup2synchtimeout = None
                self.cpwctdmcfgpktreplacepolicy = None
                self.cpwctdmcfgavepktlosstimewindow = None
                self.cpwctdmcfgexcessivepktlossthreshold = None
                self.cpwctdmcfgalarmthreshold = None
                self.cpwctdmcfgclearalarmthreshold = None
                self.cpwctdmcfgmissingpktstoses = None
                self.cpwctdmcfgtimestampmode = None
                self.cpwctdmcfgstoragetype = None
                self.cpwctdmcfgrowstatus = None
                self._segment_path = lambda: "cpwCTDMCfgEntry" + "[cpwCTDMCfgIndex='" + str(self.cpwctdmcfgindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMCfgTable.CpwCTDMCfgEntry, ['cpwctdmcfgindex', 'cpwctdmcfgconferr', 'cpwctdmcfgpayloadsize', 'cpwctdmcfgpktreorder', 'cpwctdmcfgrtphdrused', 'cpwctdmcfgjtrbfrdepth', 'cpwctdmcfgpayloadsuppression', 'cpwctdmcfgconsecpktsinsynch', 'cpwctdmcfgconsecmisspktsoutsynch', 'cpwctdmcfgsetup2synchtimeout', 'cpwctdmcfgpktreplacepolicy', 'cpwctdmcfgavepktlosstimewindow', 'cpwctdmcfgexcessivepktlossthreshold', 'cpwctdmcfgalarmthreshold', 'cpwctdmcfgclearalarmthreshold', 'cpwctdmcfgmissingpktstoses', 'cpwctdmcfgtimestampmode', 'cpwctdmcfgstoragetype', 'cpwctdmcfgrowstatus'], name, value)

            class CpwCTDMCfgPayloadSuppression(Enum):
                """
                CpwCTDMCfgPayloadSuppression (Enum Class)

                This object indicates whether the Payload suppression

                is eanbled or disabled.

                Payload MAY be omitted in order to conserve bandwidth.

                enable  \- Payload suppression is allowed.

                disable \- No Payload suppresion under any condition.

                .. data:: enable = 1

                .. data:: disable = 2

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")


            class CpwCTDMCfgPktReplacePolicy(Enum):
                """
                CpwCTDMCfgPktReplacePolicy (Enum Class)

                This parameter determines the value to be played when CE

                bound packets have over/underflow the jitter buffer, or are

                missing for any reason. This AIS (Alarm Indication Signal)

                pattern is sent (played) on the TDM line.

                ais                    \- AIS (Alarm Indication Signal)

                                         pattern is sent (played) on

                                         the TDM line. 

                implementationSpecific \- Implementation specific pattern is

                                         sent on the TDM line.

                .. data:: ais = 1

                .. data:: implementationSpecific = 2

                """

                ais = Enum.YLeaf(1, "ais")

                implementationSpecific = Enum.YLeaf(2, "implementationSpecific")


            class CpwCTDMCfgTimestampMode(Enum):
                """
                CpwCTDMCfgTimestampMode (Enum Class)

                Timestamp generation MAY be used in one of the following

                modes\:

                1. Absolute mode\: the PSN\-bound IWF sets timestamps

                 using the clock recovered from the incoming TDM attachment

                 circuit. As a consequence, the timestamps are closely

                 correlated with the sequence numbers. All TDM 

                 implementations that support usage of the RTP header MUST

                 support this mode.

                2. Differential mode\: Both IWFs have access to a common

                 high\-quality timing source, and this source is used for

                 timestamp generation. Support of this mode is OPTIONAL.

                .. data:: notApplicable = 1

                .. data:: absolute = 2

                .. data:: differential = 3

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                absolute = Enum.YLeaf(2, "absolute")

                differential = Enum.YLeaf(3, "differential")



    class CpwCTDMPerfCurrentTable(Entity):
        """
        This table provides TDM PW performance information.
        This includes current 15 minute interval counts. 
        
        The table includes counters that work together to
        integrate errors and the lack of errors on the TDM PW.
        An error is caused by a missing packet. Missing packet
        can be a result of, packet loss in the network,
        (uncorrectable) packet out of sequence, packet length error,
        jitter buffer overflow, and jitter buffer underflow.
        The result is declaring whether or not the TDM PW is in
        Loss of Packet (LOPS) state.
        
        .. attribute:: cpwctdmperfcurrententry
        
        	An entry in this table is created by the agent for every cpwCTDMTable entry. After 15 minutes, the contents of this table entry are copied to a new entry in the cpwCTDMPerfInterval table and the counts in this entry are reset to zero
        	**type**\: list of  		 :py:class:`CpwCTDMPerfCurrentEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable.CpwCTDMPerfCurrentEntry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable, self).__init__()

            self.yang_name = "cpwCTDMPerfCurrentTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwCTDMPerfCurrentEntry", ("cpwctdmperfcurrententry", CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable.CpwCTDMPerfCurrentEntry))])
            self._leafs = OrderedDict()

            self.cpwctdmperfcurrententry = YList(self)
            self._segment_path = lambda: "cpwCTDMPerfCurrentTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable, [], name, value)


        class CpwCTDMPerfCurrentEntry(Entity):
            """
            An entry in this table is created by the agent for every
            cpwCTDMTable entry. After 15 minutes, the contents of this
            table entry are copied to a new entry in the
            cpwCTDMPerfInterval table and the counts in this entry
            are reset to zero.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            .. attribute:: cpwctdmperfcurrentmissingpkts
            
            	Number of missing packets (as detected via control word sequence number gaps)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentpktsreorder
            
            	Number of packets detected out of sequence (via control word sequence number), but successfully re\-ordered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentjtrbfrunderruns
            
            	Number of times a packet needed to be played out and the jitter buffer was empty
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfcurrentmisorderdropped
            
            	Number of packets detected out of order(via control word sequence numbers), and could not be re\-ordered, or could not fit in the jitter buffer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentmalformedpkt
            
            	Number of packets detected with unexpected size, or bad headers' stack
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentess
            
            	The counter associated with the number of Error Seconds encountered. Any malformed packet, sequence error and similar are considered as error second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfcurrentsess
            
            	The counter associated with the number of Severely Error Seconds encountered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered. Any consequtive five seconds of SES are counted as one UAS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfcurrentfc
            
            	This object represents the number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared. A failure event that begins in one period and ends in another period is counted only in the period in which it begins
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable.CpwCTDMPerfCurrentEntry, self).__init__()

                self.yang_name = "cpwCTDMPerfCurrentEntry"
                self.yang_parent_name = "cpwCTDMPerfCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwctdmperfcurrentmissingpkts', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentMissingPkts'), ['int'])),
                    ('cpwctdmperfcurrentpktsreorder', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentPktsReOrder'), ['int'])),
                    ('cpwctdmperfcurrentjtrbfrunderruns', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentJtrBfrUnderruns'), ['int'])),
                    ('cpwctdmperfcurrentmisorderdropped', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentMisOrderDropped'), ['int'])),
                    ('cpwctdmperfcurrentmalformedpkt', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentMalformedPkt'), ['int'])),
                    ('cpwctdmperfcurrentess', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentESs'), ['int'])),
                    ('cpwctdmperfcurrentsess', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentSESs'), ['int'])),
                    ('cpwctdmperfcurrentuass', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentUASs'), ['int'])),
                    ('cpwctdmperfcurrentfc', (YLeaf(YType.uint32, 'cpwCTDMPerfCurrentFC'), ['int'])),
                ])
                self.cpwvcindex = None
                self.cpwctdmperfcurrentmissingpkts = None
                self.cpwctdmperfcurrentpktsreorder = None
                self.cpwctdmperfcurrentjtrbfrunderruns = None
                self.cpwctdmperfcurrentmisorderdropped = None
                self.cpwctdmperfcurrentmalformedpkt = None
                self.cpwctdmperfcurrentess = None
                self.cpwctdmperfcurrentsess = None
                self.cpwctdmperfcurrentuass = None
                self.cpwctdmperfcurrentfc = None
                self._segment_path = lambda: "cpwCTDMPerfCurrentEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMPerfCurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMPerfCurrentTable.CpwCTDMPerfCurrentEntry, ['cpwvcindex', 'cpwctdmperfcurrentmissingpkts', 'cpwctdmperfcurrentpktsreorder', 'cpwctdmperfcurrentjtrbfrunderruns', 'cpwctdmperfcurrentmisorderdropped', 'cpwctdmperfcurrentmalformedpkt', 'cpwctdmperfcurrentess', 'cpwctdmperfcurrentsess', 'cpwctdmperfcurrentuass', 'cpwctdmperfcurrentfc'], name, value)


    class CpwCTDMPerfIntervalTable(Entity):
        """
        This table provides performance information per TDM PW
        similar to the cpwCTDMPerfCurrentTable above. However,
        these counts represent historical 15 minute intervals.
        Typically, this table will have a maximum of 96 entries
        for a 24 hour period, but is not limited to this.
        
        .. attribute:: cpwctdmperfintervalentry
        
        	An entry in this table is created by the agent for every cpwCTDMPerfCurrentEntry that is 15 minutes old. The contents of the Current entry are copied to the new entry here. The Current entry, then resets its counts to zero for the next current 15 minute interval
        	**type**\: list of  		 :py:class:`CpwCTDMPerfIntervalEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable.CpwCTDMPerfIntervalEntry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable, self).__init__()

            self.yang_name = "cpwCTDMPerfIntervalTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwCTDMPerfIntervalEntry", ("cpwctdmperfintervalentry", CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable.CpwCTDMPerfIntervalEntry))])
            self._leafs = OrderedDict()

            self.cpwctdmperfintervalentry = YList(self)
            self._segment_path = lambda: "cpwCTDMPerfIntervalTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable, [], name, value)


        class CpwCTDMPerfIntervalEntry(Entity):
            """
            An entry in this table is created by the agent for
            every cpwCTDMPerfCurrentEntry that is 15 minutes old.
            The contents of the Current entry are copied to the new
            entry here. The Current entry, then resets its counts
            to zero for the next current 15 minute interval.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            .. attribute:: cpwctdmperfintervalnumber  (key)
            
            	This object indicates a number (normally between 1 and 96 to cover a 24 hour period) which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1. The minimum range of N is 1 through 4.The default range is 1 through 32. The maximum value of N is 1 through 96
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            .. attribute:: cpwctdmperfintervalduration
            
            	The duration of a particular interval in seconds. Adjustments in the system's time\-of\-day clock, may cause the interval to be greater or less than, the normal value. Therefore this actual interval value is provided
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfintervalmissingpkts
            
            	Number of missing packets (as detected via control word sequence number gaps)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervalpktsreorder
            
            	Number of packets detected out of sequence (via control word sequence number), but successfully re\-ordered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervaljtrbfrunderruns
            
            	Number of times a packet needed to be played out and the jitter buffer was empty
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervalmisorderdropped
            
            	Number of packets detected out of order(via control word sequence numbers), and could not be re\-ordered, or could not fit in the jitter buffer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervalmalformedpkt
            
            	Number of packets detected with unexpected size, or bad headers' stack
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervaless
            
            	The counter associated with the number of Error Seconds encountered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfintervalsess
            
            	The counter associated with the number of Severely Error Seconds encountered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfintervalfc
            
            	This object represents the number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared. A failure event that begins in one period and ends in another period is counted only in the period in which it begins
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable.CpwCTDMPerfIntervalEntry, self).__init__()

                self.yang_name = "cpwCTDMPerfIntervalEntry"
                self.yang_parent_name = "cpwCTDMPerfIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwctdmperfintervalnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwctdmperfintervalnumber', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalNumber'), ['int'])),
                    ('cpwctdmperfintervalvaliddata', (YLeaf(YType.boolean, 'cpwCTDMPerfIntervalValidData'), ['bool'])),
                    ('cpwctdmperfintervalduration', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalDuration'), ['int'])),
                    ('cpwctdmperfintervalmissingpkts', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalMissingPkts'), ['int'])),
                    ('cpwctdmperfintervalpktsreorder', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalPktsReOrder'), ['int'])),
                    ('cpwctdmperfintervaljtrbfrunderruns', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalJtrBfrUnderruns'), ['int'])),
                    ('cpwctdmperfintervalmisorderdropped', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalMisOrderDropped'), ['int'])),
                    ('cpwctdmperfintervalmalformedpkt', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalMalformedPkt'), ['int'])),
                    ('cpwctdmperfintervaless', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalESs'), ['int'])),
                    ('cpwctdmperfintervalsess', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalSESs'), ['int'])),
                    ('cpwctdmperfintervaluass', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalUASs'), ['int'])),
                    ('cpwctdmperfintervalfc', (YLeaf(YType.uint32, 'cpwCTDMPerfIntervalFC'), ['int'])),
                ])
                self.cpwvcindex = None
                self.cpwctdmperfintervalnumber = None
                self.cpwctdmperfintervalvaliddata = None
                self.cpwctdmperfintervalduration = None
                self.cpwctdmperfintervalmissingpkts = None
                self.cpwctdmperfintervalpktsreorder = None
                self.cpwctdmperfintervaljtrbfrunderruns = None
                self.cpwctdmperfintervalmisorderdropped = None
                self.cpwctdmperfintervalmalformedpkt = None
                self.cpwctdmperfintervaless = None
                self.cpwctdmperfintervalsess = None
                self.cpwctdmperfintervaluass = None
                self.cpwctdmperfintervalfc = None
                self._segment_path = lambda: "cpwCTDMPerfIntervalEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']" + "[cpwCTDMPerfIntervalNumber='" + str(self.cpwctdmperfintervalnumber) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMPerfIntervalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMPerfIntervalTable.CpwCTDMPerfIntervalEntry, ['cpwvcindex', 'cpwctdmperfintervalnumber', 'cpwctdmperfintervalvaliddata', 'cpwctdmperfintervalduration', 'cpwctdmperfintervalmissingpkts', 'cpwctdmperfintervalpktsreorder', 'cpwctdmperfintervaljtrbfrunderruns', 'cpwctdmperfintervalmisorderdropped', 'cpwctdmperfintervalmalformedpkt', 'cpwctdmperfintervaless', 'cpwctdmperfintervalsess', 'cpwctdmperfintervaluass', 'cpwctdmperfintervalfc'], name, value)


    class CpwCTDMPerf1DayIntervalTable(Entity):
        """
        This table provides performance information per TDM PW
        similar to the cpwCTDMPerfIntervalTable above. However,
        these counters represent historical 1 day intervals up to
        one full month. The table consists of real time data, as
        such it is not persistence across re\-boot.
        
        .. attribute:: cpwctdmperf1dayintervalentry
        
        	An entry is created in this table by the agent for every entry in the cpwCTDMTable table
        	**type**\: list of  		 :py:class:`CpwCTDMPerf1DayIntervalEntry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable.CpwCTDMPerf1DayIntervalEntry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable, self).__init__()

            self.yang_name = "cpwCTDMPerf1DayIntervalTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpwCTDMPerf1DayIntervalEntry", ("cpwctdmperf1dayintervalentry", CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable.CpwCTDMPerf1DayIntervalEntry))])
            self._leafs = OrderedDict()

            self.cpwctdmperf1dayintervalentry = YList(self)
            self._segment_path = lambda: "cpwCTDMPerf1DayIntervalTable"
            self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable, [], name, value)


        class CpwCTDMPerf1DayIntervalEntry(Entity):
            """
            An entry is created in this table by the agent
            for every entry in the cpwCTDMTable table.
            
            .. attribute:: cpwvcindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CISCOIETFPWMIB.CpwVcTable.CpwVcEntry>`
            
            .. attribute:: cpwctdmperf1dayintervalnumber  (key)
            
            	The number of interval, where 1 indicates current day measured period and 2 and above indicate previous days respectively
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperf1dayintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            .. attribute:: cpwctdmperf1dayintervalduration
            
            	The duration of a particular interval in seconds, Adjustments in the system's time\-of\-day clock, may cause the interval to be greater or less than, the normal value. Therefore this actual interval value is provided
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervalmissingpkts
            
            	Number of missing packets (as detected via control word sequence number gaps)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervalpktsreorder
            
            	Number of packets detected out of sequence (via control word sequence number), but successfully re\-ordered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervaljtrbfrunderruns
            
            	Number of times a packet needed to be played out and the jitter buffer was empty
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperf1dayintervalmisorderdropped
            
            	Number of packets detected out of order(via control word sequence numbers), and could not be re\-ordered, or could not fit in the jitter buffer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervalmalformedpkt
            
            	Number of packets detected with unexpected size, or bad headers' stack
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervaless
            
            	The counter associated with the number of Error Seconds encountered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervalsess
            
            	The counter associated with the number of Severely Error Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervaluass
            
            	The counter associated with the number of UnAvailable Seconds. When first entering the UAS state, the number of SES To UAS is added to this object, then as each additional UAS occurs, this object increments by one
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervalfc
            
            	This object represents the number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable.CpwCTDMPerf1DayIntervalEntry, self).__init__()

                self.yang_name = "cpwCTDMPerf1DayIntervalEntry"
                self.yang_parent_name = "cpwCTDMPerf1DayIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpwvcindex','cpwctdmperf1dayintervalnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpwvcindex', (YLeaf(YType.str, 'cpwVcIndex'), ['int'])),
                    ('cpwctdmperf1dayintervalnumber', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalNumber'), ['int'])),
                    ('cpwctdmperf1dayintervalvaliddata', (YLeaf(YType.boolean, 'cpwCTDMPerf1DayIntervalValidData'), ['bool'])),
                    ('cpwctdmperf1dayintervalduration', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalDuration'), ['int'])),
                    ('cpwctdmperf1dayintervalmissingpkts', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalMissingPkts'), ['int'])),
                    ('cpwctdmperf1dayintervalpktsreorder', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalPktsReOrder'), ['int'])),
                    ('cpwctdmperf1dayintervaljtrbfrunderruns', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalJtrBfrUnderruns'), ['int'])),
                    ('cpwctdmperf1dayintervalmisorderdropped', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalMisOrderDropped'), ['int'])),
                    ('cpwctdmperf1dayintervalmalformedpkt', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalMalformedPkt'), ['int'])),
                    ('cpwctdmperf1dayintervaless', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalESs'), ['int'])),
                    ('cpwctdmperf1dayintervalsess', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalSESs'), ['int'])),
                    ('cpwctdmperf1dayintervaluass', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalUASs'), ['int'])),
                    ('cpwctdmperf1dayintervalfc', (YLeaf(YType.uint32, 'cpwCTDMPerf1DayIntervalFC'), ['int'])),
                ])
                self.cpwvcindex = None
                self.cpwctdmperf1dayintervalnumber = None
                self.cpwctdmperf1dayintervalvaliddata = None
                self.cpwctdmperf1dayintervalduration = None
                self.cpwctdmperf1dayintervalmissingpkts = None
                self.cpwctdmperf1dayintervalpktsreorder = None
                self.cpwctdmperf1dayintervaljtrbfrunderruns = None
                self.cpwctdmperf1dayintervalmisorderdropped = None
                self.cpwctdmperf1dayintervalmalformedpkt = None
                self.cpwctdmperf1dayintervaless = None
                self.cpwctdmperf1dayintervalsess = None
                self.cpwctdmperf1dayintervaluass = None
                self.cpwctdmperf1dayintervalfc = None
                self._segment_path = lambda: "cpwCTDMPerf1DayIntervalEntry" + "[cpwVcIndex='" + str(self.cpwvcindex) + "']" + "[cpwCTDMPerf1DayIntervalNumber='" + str(self.cpwctdmperf1dayintervalnumber) + "']"
                self._absolute_path = lambda: "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMPerf1DayIntervalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFPWTDMMIB.CpwCTDMPerf1DayIntervalTable.CpwCTDMPerf1DayIntervalEntry, ['cpwvcindex', 'cpwctdmperf1dayintervalnumber', 'cpwctdmperf1dayintervalvaliddata', 'cpwctdmperf1dayintervalduration', 'cpwctdmperf1dayintervalmissingpkts', 'cpwctdmperf1dayintervalpktsreorder', 'cpwctdmperf1dayintervaljtrbfrunderruns', 'cpwctdmperf1dayintervalmisorderdropped', 'cpwctdmperf1dayintervalmalformedpkt', 'cpwctdmperf1dayintervaless', 'cpwctdmperf1dayintervalsess', 'cpwctdmperf1dayintervaluass', 'cpwctdmperf1dayintervalfc'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIETFPWTDMMIB()
        return self._top_entity

