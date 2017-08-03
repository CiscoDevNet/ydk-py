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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfPwTdmMib(Entity):
    """
    
    
    .. attribute:: cpwctdmcfgtable
    
    	This table contains a set of parameters that may be referenced by one or more TDM PWs in cpwCTDMTable
    	**type**\:   :py:class:`Cpwctdmcfgtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable>`
    
    .. attribute:: cpwctdmobjects
    
    	
    	**type**\:   :py:class:`Cpwctdmobjects <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmobjects>`
    
    .. attribute:: cpwctdmperf1dayintervaltable
    
    	This table provides performance information per TDM PW similar to the cpwCTDMPerfIntervalTable above. However, these counters represent historical 1 day intervals up to one full month. The table consists of real time data, as such it is not persistence across re\-boot
    	**type**\:   :py:class:`Cpwctdmperf1Dayintervaltable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable>`
    
    .. attribute:: cpwctdmperfcurrenttable
    
    	This table provides TDM PW performance information. This includes current 15 minute interval counts.   The table includes counters that work together to integrate errors and the lack of errors on the TDM PW. An error is caused by a missing packet. Missing packet can be a result of, packet loss in the network, (uncorrectable) packet out of sequence, packet length error, jitter buffer overflow, and jitter buffer underflow. The result is declaring whether or not the TDM PW is in Loss of Packet (LOPS) state
    	**type**\:   :py:class:`Cpwctdmperfcurrenttable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable>`
    
    .. attribute:: cpwctdmperfintervaltable
    
    	This table provides performance information per TDM PW similar to the cpwCTDMPerfCurrentTable above. However, these counts represent historical 15 minute intervals. Typically, this table will have a maximum of 96 entries for a 24 hour period, but is not limited to this
    	**type**\:   :py:class:`Cpwctdmperfintervaltable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmperfintervaltable>`
    
    .. attribute:: cpwctdmtable
    
    	This table contains basic information including ifIndex, and pointers to entries in the relevant TDM config tables for this TDM PW
    	**type**\:   :py:class:`Cpwctdmtable <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmtable>`
    
    

    """

    _prefix = 'CISCO-IETF-PW-TDM-MIB'
    _revision = '2006-07-21'

    def __init__(self):
        super(CiscoIetfPwTdmMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-PW-TDM-MIB"
        self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

        self.cpwctdmcfgtable = CiscoIetfPwTdmMib.Cpwctdmcfgtable()
        self.cpwctdmcfgtable.parent = self
        self._children_name_map["cpwctdmcfgtable"] = "cpwCTDMCfgTable"
        self._children_yang_names.add("cpwCTDMCfgTable")

        self.cpwctdmobjects = CiscoIetfPwTdmMib.Cpwctdmobjects()
        self.cpwctdmobjects.parent = self
        self._children_name_map["cpwctdmobjects"] = "cpwCTDMObjects"
        self._children_yang_names.add("cpwCTDMObjects")

        self.cpwctdmperf1dayintervaltable = CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable()
        self.cpwctdmperf1dayintervaltable.parent = self
        self._children_name_map["cpwctdmperf1dayintervaltable"] = "cpwCTDMPerf1DayIntervalTable"
        self._children_yang_names.add("cpwCTDMPerf1DayIntervalTable")

        self.cpwctdmperfcurrenttable = CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable()
        self.cpwctdmperfcurrenttable.parent = self
        self._children_name_map["cpwctdmperfcurrenttable"] = "cpwCTDMPerfCurrentTable"
        self._children_yang_names.add("cpwCTDMPerfCurrentTable")

        self.cpwctdmperfintervaltable = CiscoIetfPwTdmMib.Cpwctdmperfintervaltable()
        self.cpwctdmperfintervaltable.parent = self
        self._children_name_map["cpwctdmperfintervaltable"] = "cpwCTDMPerfIntervalTable"
        self._children_yang_names.add("cpwCTDMPerfIntervalTable")

        self.cpwctdmtable = CiscoIetfPwTdmMib.Cpwctdmtable()
        self.cpwctdmtable.parent = self
        self._children_name_map["cpwctdmtable"] = "cpwCTDMTable"
        self._children_yang_names.add("cpwCTDMTable")


    class Cpwctdmobjects(Entity):
        """
        
        
        .. attribute:: cpwctdmcfgindexnext
        
        	This object contains the value to be used for cpwCTDMCfgIndex when creating entries in the cpwCTDMCfgTable. The value 0 indicates that no unassigned entries are available.  To obtain the value of cpwCTDMCfgIndexNext for a new entry in the cpwCTDMCfgTable, the manager issues a management protocol retrieval operation. The agent will determine through its local policy when this index value will be made available for reuse
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CiscoIetfPwTdmMib.Cpwctdmobjects, self).__init__()

            self.yang_name = "cpwCTDMObjects"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

            self.cpwctdmcfgindexnext = YLeaf(YType.uint32, "cpwCTDMCfgIndexNext")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpwctdmcfgindexnext") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfPwTdmMib.Cpwctdmobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwTdmMib.Cpwctdmobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.cpwctdmcfgindexnext.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpwctdmcfgindexnext.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwCTDMObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpwctdmcfgindexnext.is_set or self.cpwctdmcfgindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpwctdmcfgindexnext.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwCTDMCfgIndexNext"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cpwCTDMCfgIndexNext"):
                self.cpwctdmcfgindexnext = value
                self.cpwctdmcfgindexnext.value_namespace = name_space
                self.cpwctdmcfgindexnext.value_namespace_prefix = name_space_prefix


    class Cpwctdmtable(Entity):
        """
        This table contains basic information including ifIndex,
        and pointers to entries in the relevant TDM config
        tables for this TDM PW.
        
        .. attribute:: cpwctdmentry
        
        	This table is indexed by the same index that was created for the associated entry in the VC Table (in the CISCO\-IETF\-PW\-MIB).    \- The CpwVcIndex.  An entry is created in this table by the agent for every entry in the cpwVcTable with a cpwVcType equal to one of the following\: e1Satop(12), t1Satop(13), e3Satop(14), t3Satop(15), basicCesPsn(16), basicTdmIp(17),  tdmCasCesPsn(18), tdmCasTdmIp(19)
        	**type**\: list of    :py:class:`Cpwctdmentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CiscoIetfPwTdmMib.Cpwctdmtable, self).__init__()

            self.yang_name = "cpwCTDMTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

            self.cpwctdmentry = YList(self)

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
                        super(CiscoIetfPwTdmMib.Cpwctdmtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwTdmMib.Cpwctdmtable, self).__setattr__(name, value)


        class Cpwctdmentry(Entity):
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
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwcgentdmcfgindex
            
            	Index to the generic parameters in the TDM configuration table that appears in this MIB module. It is likely that multiple TDM PWs of the same characteristic will share a single TDM Cfg entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwcreltdmcfgindex
            
            	Index to the relevant TDM configuration table entry that appears in one of the related MIB modules such as TDMoIP or CESoPSN. It is likely that multiple TDM PWs of the same characteristic will share a single configuration entry of the relevant type. The value 0 implies no entry in other related MIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmconfigerror
            
            	Any of the bits are set if the local configuration is not compatible with the peer configuration as available from the various parameters options.  \-tdmTypeIncompatible bit is set if the local configuration is not carrying the same TDM type as the peer configuration.  \-peerRtpIncompatible bit is set if the local configuration is configured to send RTP packets for this PW, and the remote is not capable of accepting RTP packets.  \-peerPayloadSizeIncompatible bit is set if the local configuration is not carrying the same Payload Size as the peer configuration
            	**type**\:   :py:class:`Cpwctdmconfigerror <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmconfigerror>`
            
            .. attribute:: cpwctdmcurrentindications
            
            	The following defects should be detected and reported upon request\:  \-Stray packets MAY be detected by the PSN and multiplexing layers. Stray packets MUST be discarded by the CE\-bound IWF and their detection MUST NOT affect mechanisms for detection of packet loss.  \-Malformed packets are detected by mismatch between the expected packet size (taking the value of the L bit into account) and the actual packet size inferred from the PSN and multiplexing layers. Malformed in\-order packets MUST be discarded by the CE\-bound IWF and replacement data generated as for lost packets.  \-Excessive packet loss rate is detected by computing the average packet loss rate over the value of cpwCTDMAvePktLossTimeWindow and comparing it with a preconfigured threshold [SATOP].  \-Buffer overrun is detected in the normal operation state when the CE bound IWF's jitter buffer cannot accommodate newly arrived packets.  \-Remote packet loss is indicated by reception of packets  with their R bit set.  \-Packet misorder is detected by looking at the Sequence number provided by the control word.  \-TDM Fault, if L bit in the control word is set, it indicates that TDM data carried in the payload is invalid due an attachment circuit fault.  When the L bit is set the payload MAY be omitted in order to conserve bandwidth.  Note\: the algorithm used to capture these indications is implementation specific
            	**type**\:   :py:class:`Cpwctdmcurrentindications <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmcurrentindications>`
            
            .. attribute:: cpwctdmifindex
            
            	This is a unique index within the ifTable. It represents the interface index of the full link or the interface index for the bundle holding the group of time slots to be transmitted via this PW connection.  A value of zero indicates an interface index that has yet to be determined. Once set, if the TDM ifIndex is (for some reason) later removed, the agent SHOULD delete the associated PW rows (e.g., this cpwCTDMTable entry). If the agent does not delete the rows,  the agent MUST set this object to zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cpwctdmlastestimestamp
            
            	The value of sysUpTime at the most recent occasion at which the TDM PW entered the ES or SES state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmlatchedindications
            
            	The state of TDM indicators when the TDM PW last declared an error second (either as ES, SES or a second with errors inside a UAS) condition. At this time, only LOPS can create a failure. Since indicators other than LOPS are useful, all are latched here. For bit definitions, see cpwCTDMCurrentIndications above.  Note\: the algorithm used to latch these indications when entering a defect state is implementation specific
            	**type**\:   :py:class:`Cpwctdmlatchedindications <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmlatchedindications>`
            
            .. attribute:: cpwctdmrate
            
            	The parameter represents the bit\-rate of the TDM service in multiples of the 'basic' 64 Kbit/s rate. It complements the definition of cpwVcType used in CISCO\-IETF\-PW\-MIB. For structure\-agnostic the following should be used\: a) Satop E1 \- 32 b) Satop T1 emulation\:    i)   MUST be set to 24 in the basic emulation mode    ii)  MUST be set to 25 for the 'Octet\-aligned T1'         emulation mode c) Satop E3 \- 535 d) Satop T3 \- 699 For all kinds of structure\-aware emulation, this parameter MUST be set to N where N is the number of DS0 channels in the corresponding attachment circuit
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cpwctdmtimeelapsed
            
            	The number of seconds, including partial seconds, that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 1..900
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmvaliddayintervals
            
            	The number of previous days for which data was collected. An agent with TDM capability must be capable of supporting at least n intervals. The minimum value of n is 1, The default of n is 1 and the maximum value of n is 30
            	**type**\:  int
            
            	**range:** 0..30
            
            	**units**\: days
            
            .. attribute:: cpwctdmvalidintervals
            
            	The number of previous 15\-minute intervals for which data was collected. An agent with TDM capability must be capable of supporting at least n intervals. The minimum value of n is 4, The default of n is 32 and the maximum value of n is 96. The value will be <n> unless the measurement was (re\-) started within the last (<n>\*15) minutes, in which case the value will be the number of complete 15 minute intervals for which the agent has at least some data. In certain cases(e.g., in the case where the agent is a proxy) it is possible that some intervals are unavailable. In this case, this interval is the maximum interval number for which data is available
            	**type**\:  int
            
            	**range:** 0..96
            
            	**units**\: minutes
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry, self).__init__()

                self.yang_name = "cpwCTDMEntry"
                self.yang_parent_name = "cpwCTDMTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwcgentdmcfgindex = YLeaf(YType.uint32, "cpwCGenTDMCfgIndex")

                self.cpwcreltdmcfgindex = YLeaf(YType.uint32, "cpwCRelTDMCfgIndex")

                self.cpwctdmconfigerror = YLeaf(YType.bits, "cpwCTDMConfigError")

                self.cpwctdmcurrentindications = YLeaf(YType.bits, "cpwCTDMCurrentIndications")

                self.cpwctdmifindex = YLeaf(YType.int32, "cpwCTDMIfIndex")

                self.cpwctdmlastestimestamp = YLeaf(YType.uint32, "cpwCTDMLastEsTimeStamp")

                self.cpwctdmlatchedindications = YLeaf(YType.bits, "cpwCTDMLatchedIndications")

                self.cpwctdmrate = YLeaf(YType.int32, "cpwCTDMRate")

                self.cpwctdmtimeelapsed = YLeaf(YType.int32, "cpwCTDMTimeElapsed")

                self.cpwctdmvaliddayintervals = YLeaf(YType.int32, "cpwCTDMValidDayIntervals")

                self.cpwctdmvalidintervals = YLeaf(YType.int32, "cpwCTDMValidIntervals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwcgentdmcfgindex",
                                "cpwcreltdmcfgindex",
                                "cpwctdmconfigerror",
                                "cpwctdmcurrentindications",
                                "cpwctdmifindex",
                                "cpwctdmlastestimestamp",
                                "cpwctdmlatchedindications",
                                "cpwctdmrate",
                                "cpwctdmtimeelapsed",
                                "cpwctdmvaliddayintervals",
                                "cpwctdmvalidintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwcgentdmcfgindex.is_set or
                    self.cpwcreltdmcfgindex.is_set or
                    self.cpwctdmconfigerror.is_set or
                    self.cpwctdmcurrentindications.is_set or
                    self.cpwctdmifindex.is_set or
                    self.cpwctdmlastestimestamp.is_set or
                    self.cpwctdmlatchedindications.is_set or
                    self.cpwctdmrate.is_set or
                    self.cpwctdmtimeelapsed.is_set or
                    self.cpwctdmvaliddayintervals.is_set or
                    self.cpwctdmvalidintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwcgentdmcfgindex.yfilter != YFilter.not_set or
                    self.cpwcreltdmcfgindex.yfilter != YFilter.not_set or
                    self.cpwctdmconfigerror.yfilter != YFilter.not_set or
                    self.cpwctdmcurrentindications.yfilter != YFilter.not_set or
                    self.cpwctdmifindex.yfilter != YFilter.not_set or
                    self.cpwctdmlastestimestamp.yfilter != YFilter.not_set or
                    self.cpwctdmlatchedindications.yfilter != YFilter.not_set or
                    self.cpwctdmrate.yfilter != YFilter.not_set or
                    self.cpwctdmtimeelapsed.yfilter != YFilter.not_set or
                    self.cpwctdmvaliddayintervals.yfilter != YFilter.not_set or
                    self.cpwctdmvalidintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwCTDMEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwcgentdmcfgindex.is_set or self.cpwcgentdmcfgindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwcgentdmcfgindex.get_name_leafdata())
                if (self.cpwcreltdmcfgindex.is_set or self.cpwcreltdmcfgindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwcreltdmcfgindex.get_name_leafdata())
                if (self.cpwctdmconfigerror.is_set or self.cpwctdmconfigerror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmconfigerror.get_name_leafdata())
                if (self.cpwctdmcurrentindications.is_set or self.cpwctdmcurrentindications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcurrentindications.get_name_leafdata())
                if (self.cpwctdmifindex.is_set or self.cpwctdmifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmifindex.get_name_leafdata())
                if (self.cpwctdmlastestimestamp.is_set or self.cpwctdmlastestimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmlastestimestamp.get_name_leafdata())
                if (self.cpwctdmlatchedindications.is_set or self.cpwctdmlatchedindications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmlatchedindications.get_name_leafdata())
                if (self.cpwctdmrate.is_set or self.cpwctdmrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmrate.get_name_leafdata())
                if (self.cpwctdmtimeelapsed.is_set or self.cpwctdmtimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmtimeelapsed.get_name_leafdata())
                if (self.cpwctdmvaliddayintervals.is_set or self.cpwctdmvaliddayintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmvaliddayintervals.get_name_leafdata())
                if (self.cpwctdmvalidintervals.is_set or self.cpwctdmvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmvalidintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwCGenTDMCfgIndex" or name == "cpwCRelTDMCfgIndex" or name == "cpwCTDMConfigError" or name == "cpwCTDMCurrentIndications" or name == "cpwCTDMIfIndex" or name == "cpwCTDMLastEsTimeStamp" or name == "cpwCTDMLatchedIndications" or name == "cpwCTDMRate" or name == "cpwCTDMTimeElapsed" or name == "cpwCTDMValidDayIntervals" or name == "cpwCTDMValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCGenTDMCfgIndex"):
                    self.cpwcgentdmcfgindex = value
                    self.cpwcgentdmcfgindex.value_namespace = name_space
                    self.cpwcgentdmcfgindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCRelTDMCfgIndex"):
                    self.cpwcreltdmcfgindex = value
                    self.cpwcreltdmcfgindex.value_namespace = name_space
                    self.cpwcreltdmcfgindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMConfigError"):
                    self.cpwctdmconfigerror[value] = True
                if(value_path == "cpwCTDMCurrentIndications"):
                    self.cpwctdmcurrentindications[value] = True
                if(value_path == "cpwCTDMIfIndex"):
                    self.cpwctdmifindex = value
                    self.cpwctdmifindex.value_namespace = name_space
                    self.cpwctdmifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMLastEsTimeStamp"):
                    self.cpwctdmlastestimestamp = value
                    self.cpwctdmlastestimestamp.value_namespace = name_space
                    self.cpwctdmlastestimestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMLatchedIndications"):
                    self.cpwctdmlatchedindications[value] = True
                if(value_path == "cpwCTDMRate"):
                    self.cpwctdmrate = value
                    self.cpwctdmrate.value_namespace = name_space
                    self.cpwctdmrate.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMTimeElapsed"):
                    self.cpwctdmtimeelapsed = value
                    self.cpwctdmtimeelapsed.value_namespace = name_space
                    self.cpwctdmtimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMValidDayIntervals"):
                    self.cpwctdmvaliddayintervals = value
                    self.cpwctdmvaliddayintervals.value_namespace = name_space
                    self.cpwctdmvaliddayintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMValidIntervals"):
                    self.cpwctdmvalidintervals = value
                    self.cpwctdmvalidintervals.value_namespace = name_space
                    self.cpwctdmvalidintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwctdmentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwctdmentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwCTDMTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwCTDMEntry"):
                for c in self.cpwctdmentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwctdmentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwCTDMEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwctdmcfgtable(Entity):
        """
        This table contains a set of parameters that may be
        referenced by one or more TDM PWs in cpwCTDMTable.
        
        .. attribute:: cpwctdmcfgentry
        
        	These parameters define the characteristics of a TDM PW. They are grouped here to ease NMS burden. Once an entry is created here it may be re\-used by many PWs
        	**type**\: list of    :py:class:`Cpwctdmcfgentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CiscoIetfPwTdmMib.Cpwctdmcfgtable, self).__init__()

            self.yang_name = "cpwCTDMCfgTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

            self.cpwctdmcfgentry = YList(self)

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
                        super(CiscoIetfPwTdmMib.Cpwctdmcfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwTdmMib.Cpwctdmcfgtable, self).__setattr__(name, value)


        class Cpwctdmcfgentry(Entity):
            """
            These parameters define the characteristics of a
            TDM PW. They are grouped here to ease NMS burden.
            Once an entry is created here it may be re\-used
            by many PWs.
            
            .. attribute:: cpwctdmcfgindex  <key>
            
            	Index to an entry in this table. The value is a copy of the assigned cpwCTDMCfgIndexNext
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmcfgalarmthreshold
            
            	Alarms are only reported when the defect state persists for the length of time specified by this object. The object's unit is millisec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cpwctdmcfgavepktlosstimewindow
            
            	The length of time over which the average packet loss rate should be computed to detect Excessive packet loss rate
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: millisecond
            
            .. attribute:: cpwctdmcfgclearalarmthreshold
            
            	Alarm MUST be cleared after the corresponding defect is undetected for the amount of time specified by this object. The object's unit is millisec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cpwctdmcfgconferr
            
            	This object indicates the various configuration errors, illegal settings within the cpwCTDMCfg table. The errors can be due to several reasons, like Payload size mismatch or Jitter Buffer depth value mistmatch.   payloadSize \- This bit is set if there is Payload size               mismatch between the local and peer               configurations.  jtrBfrDepth \- This bit is set if there is Jitter Buffer               depth value mistmatch. other       \- This bit is set if the error is not due to               payloadSize and jtrBfrDepth mismatch
            	**type**\:   :py:class:`Cpwctdmcfgconferr <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.Cpwctdmcfgconferr>`
            
            .. attribute:: cpwctdmcfgconsecmisspktsoutsynch
            
            	The number of consecutive missing packets that are required to enter the LOPS state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmcfgconsecpktsinsynch
            
            	The number of consecutive packets with sequential sequence numbers that are required to exit the Loss of Packets (LOPS) state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmcfgexcessivepktlossthreshold
            
            	Excessive packet loss rate is detected by computing the average packetloss rate over a  cpwCTDMCfgAvePktLossTimeWindow amount of time and comparing it with this threshold value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmcfgjtrbfrdepth
            
            	The size of this buffer SHOULD be locally configured to allow accommodation to the PSN\-specific packet delay variation.  If configured to a value not supported by the implementation, the agent MUST return an error code 'jtrBfrDepth' in 'cpwCTDMConfigError '. Jitter buffers are a limited resource to be managed. The actual size should be at least twice as big as the value of cpwCTDMCfgJtrBfrDepth
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: microsecond
            
            .. attribute:: cpwctdmcfgmissingpktstoses
            
            	Number of missing packets detected (consecutive or not) within a 1 second window to cause a Severely Error Second (SES) to be counted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmcfgpayloadsize
            
            	The value of this object indicates the PayLoad Size (in bytes) to be defined during the PW setUp. Upon TX, implementation must be capable of carrying that amount of bytes. Upon RX, when the LEN field is set to 0, the payload of packet  MUST assume this size, and if the actual packet size is inconsistent with this length, the packet MUST be considered to be malformed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpwctdmcfgpayloadsuppression
            
            	This object indicates whether the Payload suppression is eanbled or disabled. Payload MAY be omitted in order to conserve bandwidth.  enable  \- Payload suppression is allowed. disable \- No Payload suppresion under any condition
            	**type**\:   :py:class:`Cpwctdmcfgpayloadsuppression <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.Cpwctdmcfgpayloadsuppression>`
            
            .. attribute:: cpwctdmcfgpktreorder
            
            	If set to true, CE bound packets are queued in the jitter buffer, out of order packets are re\-ordered. The maximum sequence number differential (i.e., the range in which re\-sequencing can occur) is dependant on the depth of the jitter buffer. See cpwCTDMCfgJtrBfrDepth
            	**type**\:  bool
            
            .. attribute:: cpwctdmcfgpktreplacepolicy
            
            	This parameter determines the value to be played when CE bound packets have over/underflow the jitter buffer, or are missing for any reason. This AIS (Alarm Indication Signal) pattern is sent (played) on the TDM line.  ais                    \- AIS (Alarm Indication Signal)                          pattern is sent (played) on                          the TDM line.  implementationSpecific \- Implementation specific pattern is                          sent on the TDM line
            	**type**\:   :py:class:`Cpwctdmcfgpktreplacepolicy <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.Cpwctdmcfgpktreplacepolicy>`
            
            .. attribute:: cpwctdmcfgrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  All of the columnar objects have to be set to valid values before the row can be activated. Default value will be automatically provisioned if for those objects not specified during row creation.  No objects in cascading tables have to be populated with related data before the row can be activated.  The following objects cannot be modified if the RowStatus is active\: cpwCTDMCfgPayloadSize, cpwCTDMCfgRtpHdrUsed, cpwCTDMCfgJtrBfrDepth, and cpwCTDMCfgPayloadSuppression.  If the RowStatus is active, the following parameters can be modified\:  cpwCTDMCfgConfErr, cpwCTDMCfgPktReorder,  cpwCTDMCfgConsecPktsInSynch, cpwCTDMCfgConsecMissPktsOutSynch, cpwCTDMCfgSetUp2SynchTimeOut, cpwCTDMCfgPktReplacePolicy, cpwCTDMCfgAvePktLossTimeWindow,  cpwCTDMCfgExcessivePktLossThreshold, cpwCTDMCfgAlarmThreshold, cpwCTDMCfgClearAlarmThreshold, cpwCTDMCfgMissingPktsToSes, cpwCTDMCfgTimestampMode, cpwCTDMCfgStorageType.  A row may be deleted by setting the RowStatus to 'destroy'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cpwctdmcfgrtphdrused
            
            	If the value of this object is set to false, then a RTP header is not pre\-pended to the TDM packet
            	**type**\:  bool
            
            .. attribute:: cpwctdmcfgsetup2synchtimeout
            
            	The amount of time the host should wait before declaring the pseudo wire in down state,  if the number of consecutive TDM packets that have been received after changing the administrative status to up and after finalization of signaling (if supported) between the two PEs is smaller than cpwCTDMCfgConsecPktsInSynch. Once the the PW has OperStatus of 'up' this parameter is no longer valid. This parameter is defined to ensure that the host does not prematurely inform failure of the PW. In particular PW 'down' notifications should not be sent before expiration of this timer. This parameter is valid only after adminisrative changes of the status of the PW. If the PW fails due to network impairments a 'down' notification should be sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: millisecond
            
            .. attribute:: cpwctdmcfgstoragetype
            
            	This variable indicates the storage type for this row. The following are the read\-write objects in permanent(4) rows, that an agent must allow to be writable\: cpwCTDMCfgPayloadSize, cpwCTDMCfgPktReorder, cpwCTDMCfgRtpHdrUsed, cpwCTDMCfgJtrBfrDepth, cpwCTDMCfgPayloadSuppression, cpwCTDMCfgConfErr
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cpwctdmcfgtimestampmode
            
            	Timestamp generation MAY be used in one of the following modes\: 1. Absolute mode\: the PSN\-bound IWF sets timestamps  using the clock recovered from the incoming TDM attachment  circuit. As a consequence, the timestamps are closely  correlated with the sequence numbers. All TDM   implementations that support usage of the RTP header MUST  support this mode. 2. Differential mode\: Both IWFs have access to a common  high\-quality timing source, and this source is used for  timestamp generation. Support of this mode is OPTIONAL
            	**type**\:   :py:class:`Cpwctdmcfgtimestampmode <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.Cpwctdmcfgtimestampmode>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry, self).__init__()

                self.yang_name = "cpwCTDMCfgEntry"
                self.yang_parent_name = "cpwCTDMCfgTable"

                self.cpwctdmcfgindex = YLeaf(YType.uint32, "cpwCTDMCfgIndex")

                self.cpwctdmcfgalarmthreshold = YLeaf(YType.uint32, "cpwCTDMCfgAlarmThreshold")

                self.cpwctdmcfgavepktlosstimewindow = YLeaf(YType.int32, "cpwCTDMCfgAvePktLossTimeWindow")

                self.cpwctdmcfgclearalarmthreshold = YLeaf(YType.uint32, "cpwCTDMCfgClearAlarmThreshold")

                self.cpwctdmcfgconferr = YLeaf(YType.bits, "cpwCTDMCfgConfErr")

                self.cpwctdmcfgconsecmisspktsoutsynch = YLeaf(YType.uint32, "cpwCTDMCfgConsecMissPktsOutSynch")

                self.cpwctdmcfgconsecpktsinsynch = YLeaf(YType.uint32, "cpwCTDMCfgConsecPktsInSynch")

                self.cpwctdmcfgexcessivepktlossthreshold = YLeaf(YType.uint32, "cpwCTDMCfgExcessivePktLossThreshold")

                self.cpwctdmcfgjtrbfrdepth = YLeaf(YType.uint32, "cpwCTDMCfgJtrBfrDepth")

                self.cpwctdmcfgmissingpktstoses = YLeaf(YType.uint32, "cpwCTDMCfgMissingPktsToSes")

                self.cpwctdmcfgpayloadsize = YLeaf(YType.uint32, "cpwCTDMCfgPayloadSize")

                self.cpwctdmcfgpayloadsuppression = YLeaf(YType.enumeration, "cpwCTDMCfgPayloadSuppression")

                self.cpwctdmcfgpktreorder = YLeaf(YType.boolean, "cpwCTDMCfgPktReorder")

                self.cpwctdmcfgpktreplacepolicy = YLeaf(YType.enumeration, "cpwCTDMCfgPktReplacePolicy")

                self.cpwctdmcfgrowstatus = YLeaf(YType.enumeration, "cpwCTDMCfgRowStatus")

                self.cpwctdmcfgrtphdrused = YLeaf(YType.boolean, "cpwCTDMCfgRtpHdrUsed")

                self.cpwctdmcfgsetup2synchtimeout = YLeaf(YType.uint32, "cpwCTDMCfgSetUp2SynchTimeOut")

                self.cpwctdmcfgstoragetype = YLeaf(YType.enumeration, "cpwCTDMCfgStorageType")

                self.cpwctdmcfgtimestampmode = YLeaf(YType.enumeration, "cpwCTDMCfgTimestampMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwctdmcfgindex",
                                "cpwctdmcfgalarmthreshold",
                                "cpwctdmcfgavepktlosstimewindow",
                                "cpwctdmcfgclearalarmthreshold",
                                "cpwctdmcfgconferr",
                                "cpwctdmcfgconsecmisspktsoutsynch",
                                "cpwctdmcfgconsecpktsinsynch",
                                "cpwctdmcfgexcessivepktlossthreshold",
                                "cpwctdmcfgjtrbfrdepth",
                                "cpwctdmcfgmissingpktstoses",
                                "cpwctdmcfgpayloadsize",
                                "cpwctdmcfgpayloadsuppression",
                                "cpwctdmcfgpktreorder",
                                "cpwctdmcfgpktreplacepolicy",
                                "cpwctdmcfgrowstatus",
                                "cpwctdmcfgrtphdrused",
                                "cpwctdmcfgsetup2synchtimeout",
                                "cpwctdmcfgstoragetype",
                                "cpwctdmcfgtimestampmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry, self).__setattr__(name, value)

            class Cpwctdmcfgpayloadsuppression(Enum):
                """
                Cpwctdmcfgpayloadsuppression

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


            class Cpwctdmcfgpktreplacepolicy(Enum):
                """
                Cpwctdmcfgpktreplacepolicy

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


            class Cpwctdmcfgtimestampmode(Enum):
                """
                Cpwctdmcfgtimestampmode

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


            def has_data(self):
                return (
                    self.cpwctdmcfgindex.is_set or
                    self.cpwctdmcfgalarmthreshold.is_set or
                    self.cpwctdmcfgavepktlosstimewindow.is_set or
                    self.cpwctdmcfgclearalarmthreshold.is_set or
                    self.cpwctdmcfgconferr.is_set or
                    self.cpwctdmcfgconsecmisspktsoutsynch.is_set or
                    self.cpwctdmcfgconsecpktsinsynch.is_set or
                    self.cpwctdmcfgexcessivepktlossthreshold.is_set or
                    self.cpwctdmcfgjtrbfrdepth.is_set or
                    self.cpwctdmcfgmissingpktstoses.is_set or
                    self.cpwctdmcfgpayloadsize.is_set or
                    self.cpwctdmcfgpayloadsuppression.is_set or
                    self.cpwctdmcfgpktreorder.is_set or
                    self.cpwctdmcfgpktreplacepolicy.is_set or
                    self.cpwctdmcfgrowstatus.is_set or
                    self.cpwctdmcfgrtphdrused.is_set or
                    self.cpwctdmcfgsetup2synchtimeout.is_set or
                    self.cpwctdmcfgstoragetype.is_set or
                    self.cpwctdmcfgtimestampmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwctdmcfgindex.yfilter != YFilter.not_set or
                    self.cpwctdmcfgalarmthreshold.yfilter != YFilter.not_set or
                    self.cpwctdmcfgavepktlosstimewindow.yfilter != YFilter.not_set or
                    self.cpwctdmcfgclearalarmthreshold.yfilter != YFilter.not_set or
                    self.cpwctdmcfgconferr.yfilter != YFilter.not_set or
                    self.cpwctdmcfgconsecmisspktsoutsynch.yfilter != YFilter.not_set or
                    self.cpwctdmcfgconsecpktsinsynch.yfilter != YFilter.not_set or
                    self.cpwctdmcfgexcessivepktlossthreshold.yfilter != YFilter.not_set or
                    self.cpwctdmcfgjtrbfrdepth.yfilter != YFilter.not_set or
                    self.cpwctdmcfgmissingpktstoses.yfilter != YFilter.not_set or
                    self.cpwctdmcfgpayloadsize.yfilter != YFilter.not_set or
                    self.cpwctdmcfgpayloadsuppression.yfilter != YFilter.not_set or
                    self.cpwctdmcfgpktreorder.yfilter != YFilter.not_set or
                    self.cpwctdmcfgpktreplacepolicy.yfilter != YFilter.not_set or
                    self.cpwctdmcfgrowstatus.yfilter != YFilter.not_set or
                    self.cpwctdmcfgrtphdrused.yfilter != YFilter.not_set or
                    self.cpwctdmcfgsetup2synchtimeout.yfilter != YFilter.not_set or
                    self.cpwctdmcfgstoragetype.yfilter != YFilter.not_set or
                    self.cpwctdmcfgtimestampmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwCTDMCfgEntry" + "[cpwCTDMCfgIndex='" + self.cpwctdmcfgindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwctdmcfgindex.is_set or self.cpwctdmcfgindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgindex.get_name_leafdata())
                if (self.cpwctdmcfgalarmthreshold.is_set or self.cpwctdmcfgalarmthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgalarmthreshold.get_name_leafdata())
                if (self.cpwctdmcfgavepktlosstimewindow.is_set or self.cpwctdmcfgavepktlosstimewindow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgavepktlosstimewindow.get_name_leafdata())
                if (self.cpwctdmcfgclearalarmthreshold.is_set or self.cpwctdmcfgclearalarmthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgclearalarmthreshold.get_name_leafdata())
                if (self.cpwctdmcfgconferr.is_set or self.cpwctdmcfgconferr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgconferr.get_name_leafdata())
                if (self.cpwctdmcfgconsecmisspktsoutsynch.is_set or self.cpwctdmcfgconsecmisspktsoutsynch.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgconsecmisspktsoutsynch.get_name_leafdata())
                if (self.cpwctdmcfgconsecpktsinsynch.is_set or self.cpwctdmcfgconsecpktsinsynch.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgconsecpktsinsynch.get_name_leafdata())
                if (self.cpwctdmcfgexcessivepktlossthreshold.is_set or self.cpwctdmcfgexcessivepktlossthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgexcessivepktlossthreshold.get_name_leafdata())
                if (self.cpwctdmcfgjtrbfrdepth.is_set or self.cpwctdmcfgjtrbfrdepth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgjtrbfrdepth.get_name_leafdata())
                if (self.cpwctdmcfgmissingpktstoses.is_set or self.cpwctdmcfgmissingpktstoses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgmissingpktstoses.get_name_leafdata())
                if (self.cpwctdmcfgpayloadsize.is_set or self.cpwctdmcfgpayloadsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgpayloadsize.get_name_leafdata())
                if (self.cpwctdmcfgpayloadsuppression.is_set or self.cpwctdmcfgpayloadsuppression.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgpayloadsuppression.get_name_leafdata())
                if (self.cpwctdmcfgpktreorder.is_set or self.cpwctdmcfgpktreorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgpktreorder.get_name_leafdata())
                if (self.cpwctdmcfgpktreplacepolicy.is_set or self.cpwctdmcfgpktreplacepolicy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgpktreplacepolicy.get_name_leafdata())
                if (self.cpwctdmcfgrowstatus.is_set or self.cpwctdmcfgrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgrowstatus.get_name_leafdata())
                if (self.cpwctdmcfgrtphdrused.is_set or self.cpwctdmcfgrtphdrused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgrtphdrused.get_name_leafdata())
                if (self.cpwctdmcfgsetup2synchtimeout.is_set or self.cpwctdmcfgsetup2synchtimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgsetup2synchtimeout.get_name_leafdata())
                if (self.cpwctdmcfgstoragetype.is_set or self.cpwctdmcfgstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgstoragetype.get_name_leafdata())
                if (self.cpwctdmcfgtimestampmode.is_set or self.cpwctdmcfgtimestampmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmcfgtimestampmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwCTDMCfgIndex" or name == "cpwCTDMCfgAlarmThreshold" or name == "cpwCTDMCfgAvePktLossTimeWindow" or name == "cpwCTDMCfgClearAlarmThreshold" or name == "cpwCTDMCfgConfErr" or name == "cpwCTDMCfgConsecMissPktsOutSynch" or name == "cpwCTDMCfgConsecPktsInSynch" or name == "cpwCTDMCfgExcessivePktLossThreshold" or name == "cpwCTDMCfgJtrBfrDepth" or name == "cpwCTDMCfgMissingPktsToSes" or name == "cpwCTDMCfgPayloadSize" or name == "cpwCTDMCfgPayloadSuppression" or name == "cpwCTDMCfgPktReorder" or name == "cpwCTDMCfgPktReplacePolicy" or name == "cpwCTDMCfgRowStatus" or name == "cpwCTDMCfgRtpHdrUsed" or name == "cpwCTDMCfgSetUp2SynchTimeOut" or name == "cpwCTDMCfgStorageType" or name == "cpwCTDMCfgTimestampMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwCTDMCfgIndex"):
                    self.cpwctdmcfgindex = value
                    self.cpwctdmcfgindex.value_namespace = name_space
                    self.cpwctdmcfgindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgAlarmThreshold"):
                    self.cpwctdmcfgalarmthreshold = value
                    self.cpwctdmcfgalarmthreshold.value_namespace = name_space
                    self.cpwctdmcfgalarmthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgAvePktLossTimeWindow"):
                    self.cpwctdmcfgavepktlosstimewindow = value
                    self.cpwctdmcfgavepktlosstimewindow.value_namespace = name_space
                    self.cpwctdmcfgavepktlosstimewindow.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgClearAlarmThreshold"):
                    self.cpwctdmcfgclearalarmthreshold = value
                    self.cpwctdmcfgclearalarmthreshold.value_namespace = name_space
                    self.cpwctdmcfgclearalarmthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgConfErr"):
                    self.cpwctdmcfgconferr[value] = True
                if(value_path == "cpwCTDMCfgConsecMissPktsOutSynch"):
                    self.cpwctdmcfgconsecmisspktsoutsynch = value
                    self.cpwctdmcfgconsecmisspktsoutsynch.value_namespace = name_space
                    self.cpwctdmcfgconsecmisspktsoutsynch.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgConsecPktsInSynch"):
                    self.cpwctdmcfgconsecpktsinsynch = value
                    self.cpwctdmcfgconsecpktsinsynch.value_namespace = name_space
                    self.cpwctdmcfgconsecpktsinsynch.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgExcessivePktLossThreshold"):
                    self.cpwctdmcfgexcessivepktlossthreshold = value
                    self.cpwctdmcfgexcessivepktlossthreshold.value_namespace = name_space
                    self.cpwctdmcfgexcessivepktlossthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgJtrBfrDepth"):
                    self.cpwctdmcfgjtrbfrdepth = value
                    self.cpwctdmcfgjtrbfrdepth.value_namespace = name_space
                    self.cpwctdmcfgjtrbfrdepth.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgMissingPktsToSes"):
                    self.cpwctdmcfgmissingpktstoses = value
                    self.cpwctdmcfgmissingpktstoses.value_namespace = name_space
                    self.cpwctdmcfgmissingpktstoses.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgPayloadSize"):
                    self.cpwctdmcfgpayloadsize = value
                    self.cpwctdmcfgpayloadsize.value_namespace = name_space
                    self.cpwctdmcfgpayloadsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgPayloadSuppression"):
                    self.cpwctdmcfgpayloadsuppression = value
                    self.cpwctdmcfgpayloadsuppression.value_namespace = name_space
                    self.cpwctdmcfgpayloadsuppression.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgPktReorder"):
                    self.cpwctdmcfgpktreorder = value
                    self.cpwctdmcfgpktreorder.value_namespace = name_space
                    self.cpwctdmcfgpktreorder.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgPktReplacePolicy"):
                    self.cpwctdmcfgpktreplacepolicy = value
                    self.cpwctdmcfgpktreplacepolicy.value_namespace = name_space
                    self.cpwctdmcfgpktreplacepolicy.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgRowStatus"):
                    self.cpwctdmcfgrowstatus = value
                    self.cpwctdmcfgrowstatus.value_namespace = name_space
                    self.cpwctdmcfgrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgRtpHdrUsed"):
                    self.cpwctdmcfgrtphdrused = value
                    self.cpwctdmcfgrtphdrused.value_namespace = name_space
                    self.cpwctdmcfgrtphdrused.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgSetUp2SynchTimeOut"):
                    self.cpwctdmcfgsetup2synchtimeout = value
                    self.cpwctdmcfgsetup2synchtimeout.value_namespace = name_space
                    self.cpwctdmcfgsetup2synchtimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgStorageType"):
                    self.cpwctdmcfgstoragetype = value
                    self.cpwctdmcfgstoragetype.value_namespace = name_space
                    self.cpwctdmcfgstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMCfgTimestampMode"):
                    self.cpwctdmcfgtimestampmode = value
                    self.cpwctdmcfgtimestampmode.value_namespace = name_space
                    self.cpwctdmcfgtimestampmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwctdmcfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwctdmcfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwCTDMCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwCTDMCfgEntry"):
                for c in self.cpwctdmcfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwctdmcfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwCTDMCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwctdmperfcurrenttable(Entity):
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
        	**type**\: list of    :py:class:`Cpwctdmperfcurrententry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable, self).__init__()

            self.yang_name = "cpwCTDMPerfCurrentTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

            self.cpwctdmperfcurrententry = YList(self)

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
                        super(CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable, self).__setattr__(name, value)


        class Cpwctdmperfcurrententry(Entity):
            """
            An entry in this table is created by the agent for every
            cpwCTDMTable entry. After 15 minutes, the contents of this
            table entry are copied to a new entry in the
            cpwCTDMPerfInterval table and the counts in this entry
            are reset to zero.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwctdmperfcurrentess
            
            	The counter associated with the number of Error Seconds encountered. Any malformed packet, sequence error and similar are considered as error second
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfcurrentfc
            
            	This object represents the number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared. A failure event that begins in one period and ends in another period is counted only in the period in which it begins
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfcurrentjtrbfrunderruns
            
            	Number of times a packet needed to be played out and the jitter buffer was empty
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfcurrentmalformedpkt
            
            	Number of packets detected with unexpected size, or bad headers' stack
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentmisorderdropped
            
            	Number of packets detected out of order(via control word sequence numbers), and could not be re\-ordered, or could not fit in the jitter buffer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentmissingpkts
            
            	Number of missing packets (as detected via control word sequence number gaps)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentpktsreorder
            
            	Number of packets detected out of sequence (via control word sequence number), but successfully re\-ordered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfcurrentsess
            
            	The counter associated with the number of Severely Error Seconds encountered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfcurrentuass
            
            	The counter associated with the number of Unavailable Seconds encountered. Any consequtive five seconds of SES are counted as one UAS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry, self).__init__()

                self.yang_name = "cpwCTDMPerfCurrentEntry"
                self.yang_parent_name = "cpwCTDMPerfCurrentTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwctdmperfcurrentess = YLeaf(YType.uint32, "cpwCTDMPerfCurrentESs")

                self.cpwctdmperfcurrentfc = YLeaf(YType.uint32, "cpwCTDMPerfCurrentFC")

                self.cpwctdmperfcurrentjtrbfrunderruns = YLeaf(YType.uint32, "cpwCTDMPerfCurrentJtrBfrUnderruns")

                self.cpwctdmperfcurrentmalformedpkt = YLeaf(YType.uint32, "cpwCTDMPerfCurrentMalformedPkt")

                self.cpwctdmperfcurrentmisorderdropped = YLeaf(YType.uint32, "cpwCTDMPerfCurrentMisOrderDropped")

                self.cpwctdmperfcurrentmissingpkts = YLeaf(YType.uint32, "cpwCTDMPerfCurrentMissingPkts")

                self.cpwctdmperfcurrentpktsreorder = YLeaf(YType.uint32, "cpwCTDMPerfCurrentPktsReOrder")

                self.cpwctdmperfcurrentsess = YLeaf(YType.uint32, "cpwCTDMPerfCurrentSESs")

                self.cpwctdmperfcurrentuass = YLeaf(YType.uint32, "cpwCTDMPerfCurrentUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwctdmperfcurrentess",
                                "cpwctdmperfcurrentfc",
                                "cpwctdmperfcurrentjtrbfrunderruns",
                                "cpwctdmperfcurrentmalformedpkt",
                                "cpwctdmperfcurrentmisorderdropped",
                                "cpwctdmperfcurrentmissingpkts",
                                "cpwctdmperfcurrentpktsreorder",
                                "cpwctdmperfcurrentsess",
                                "cpwctdmperfcurrentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwctdmperfcurrentess.is_set or
                    self.cpwctdmperfcurrentfc.is_set or
                    self.cpwctdmperfcurrentjtrbfrunderruns.is_set or
                    self.cpwctdmperfcurrentmalformedpkt.is_set or
                    self.cpwctdmperfcurrentmisorderdropped.is_set or
                    self.cpwctdmperfcurrentmissingpkts.is_set or
                    self.cpwctdmperfcurrentpktsreorder.is_set or
                    self.cpwctdmperfcurrentsess.is_set or
                    self.cpwctdmperfcurrentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentess.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentfc.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentjtrbfrunderruns.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentmalformedpkt.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentmisorderdropped.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentmissingpkts.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentpktsreorder.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentsess.yfilter != YFilter.not_set or
                    self.cpwctdmperfcurrentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwCTDMPerfCurrentEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMPerfCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwctdmperfcurrentess.is_set or self.cpwctdmperfcurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentess.get_name_leafdata())
                if (self.cpwctdmperfcurrentfc.is_set or self.cpwctdmperfcurrentfc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentfc.get_name_leafdata())
                if (self.cpwctdmperfcurrentjtrbfrunderruns.is_set or self.cpwctdmperfcurrentjtrbfrunderruns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentjtrbfrunderruns.get_name_leafdata())
                if (self.cpwctdmperfcurrentmalformedpkt.is_set or self.cpwctdmperfcurrentmalformedpkt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentmalformedpkt.get_name_leafdata())
                if (self.cpwctdmperfcurrentmisorderdropped.is_set or self.cpwctdmperfcurrentmisorderdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentmisorderdropped.get_name_leafdata())
                if (self.cpwctdmperfcurrentmissingpkts.is_set or self.cpwctdmperfcurrentmissingpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentmissingpkts.get_name_leafdata())
                if (self.cpwctdmperfcurrentpktsreorder.is_set or self.cpwctdmperfcurrentpktsreorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentpktsreorder.get_name_leafdata())
                if (self.cpwctdmperfcurrentsess.is_set or self.cpwctdmperfcurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentsess.get_name_leafdata())
                if (self.cpwctdmperfcurrentuass.is_set or self.cpwctdmperfcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfcurrentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwCTDMPerfCurrentESs" or name == "cpwCTDMPerfCurrentFC" or name == "cpwCTDMPerfCurrentJtrBfrUnderruns" or name == "cpwCTDMPerfCurrentMalformedPkt" or name == "cpwCTDMPerfCurrentMisOrderDropped" or name == "cpwCTDMPerfCurrentMissingPkts" or name == "cpwCTDMPerfCurrentPktsReOrder" or name == "cpwCTDMPerfCurrentSESs" or name == "cpwCTDMPerfCurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentESs"):
                    self.cpwctdmperfcurrentess = value
                    self.cpwctdmperfcurrentess.value_namespace = name_space
                    self.cpwctdmperfcurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentFC"):
                    self.cpwctdmperfcurrentfc = value
                    self.cpwctdmperfcurrentfc.value_namespace = name_space
                    self.cpwctdmperfcurrentfc.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentJtrBfrUnderruns"):
                    self.cpwctdmperfcurrentjtrbfrunderruns = value
                    self.cpwctdmperfcurrentjtrbfrunderruns.value_namespace = name_space
                    self.cpwctdmperfcurrentjtrbfrunderruns.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentMalformedPkt"):
                    self.cpwctdmperfcurrentmalformedpkt = value
                    self.cpwctdmperfcurrentmalformedpkt.value_namespace = name_space
                    self.cpwctdmperfcurrentmalformedpkt.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentMisOrderDropped"):
                    self.cpwctdmperfcurrentmisorderdropped = value
                    self.cpwctdmperfcurrentmisorderdropped.value_namespace = name_space
                    self.cpwctdmperfcurrentmisorderdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentMissingPkts"):
                    self.cpwctdmperfcurrentmissingpkts = value
                    self.cpwctdmperfcurrentmissingpkts.value_namespace = name_space
                    self.cpwctdmperfcurrentmissingpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentPktsReOrder"):
                    self.cpwctdmperfcurrentpktsreorder = value
                    self.cpwctdmperfcurrentpktsreorder.value_namespace = name_space
                    self.cpwctdmperfcurrentpktsreorder.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentSESs"):
                    self.cpwctdmperfcurrentsess = value
                    self.cpwctdmperfcurrentsess.value_namespace = name_space
                    self.cpwctdmperfcurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfCurrentUASs"):
                    self.cpwctdmperfcurrentuass = value
                    self.cpwctdmperfcurrentuass.value_namespace = name_space
                    self.cpwctdmperfcurrentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwctdmperfcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwctdmperfcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwCTDMPerfCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwCTDMPerfCurrentEntry"):
                for c in self.cpwctdmperfcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwctdmperfcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwCTDMPerfCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwctdmperfintervaltable(Entity):
        """
        This table provides performance information per TDM PW
        similar to the cpwCTDMPerfCurrentTable above. However,
        these counts represent historical 15 minute intervals.
        Typically, this table will have a maximum of 96 entries
        for a 24 hour period, but is not limited to this.
        
        .. attribute:: cpwctdmperfintervalentry
        
        	An entry in this table is created by the agent for every cpwCTDMPerfCurrentEntry that is 15 minutes old. The contents of the Current entry are copied to the new entry here. The Current entry, then resets its counts to zero for the next current 15 minute interval
        	**type**\: list of    :py:class:`Cpwctdmperfintervalentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CiscoIetfPwTdmMib.Cpwctdmperfintervaltable, self).__init__()

            self.yang_name = "cpwCTDMPerfIntervalTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

            self.cpwctdmperfintervalentry = YList(self)

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
                        super(CiscoIetfPwTdmMib.Cpwctdmperfintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwTdmMib.Cpwctdmperfintervaltable, self).__setattr__(name, value)


        class Cpwctdmperfintervalentry(Entity):
            """
            An entry in this table is created by the agent for
            every cpwCTDMPerfCurrentEntry that is 15 minutes old.
            The contents of the Current entry are copied to the new
            entry here. The Current entry, then resets its counts
            to zero for the next current 15 minute interval.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwctdmperfintervalnumber  <key>
            
            	This object indicates a number (normally between 1 and 96 to cover a 24 hour period) which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N\-1. The minimum range of N is 1 through 4.The default range is 1 through 32. The maximum value of N is 1 through 96
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervalduration
            
            	The duration of a particular interval in seconds. Adjustments in the system's time\-of\-day clock, may cause the interval to be greater or less than, the normal value. Therefore this actual interval value is provided
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfintervaless
            
            	The counter associated with the number of Error Seconds encountered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfintervalfc
            
            	This object represents the number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared. A failure event that begins in one period and ends in another period is counted only in the period in which it begins
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervaljtrbfrunderruns
            
            	Number of times a packet needed to be played out and the jitter buffer was empty
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervalmalformedpkt
            
            	Number of packets detected with unexpected size, or bad headers' stack
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervalmisorderdropped
            
            	Number of packets detected out of order(via control word sequence numbers), and could not be re\-ordered, or could not fit in the jitter buffer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervalmissingpkts
            
            	Number of missing packets (as detected via control word sequence number gaps)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervalpktsreorder
            
            	Number of packets detected out of sequence (via control word sequence number), but successfully re\-ordered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperfintervalsess
            
            	The counter associated with the number of Severely Error Seconds encountered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperfintervaluass
            
            	The counter associated with the number of Unavailable Seconds encountered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperfintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry, self).__init__()

                self.yang_name = "cpwCTDMPerfIntervalEntry"
                self.yang_parent_name = "cpwCTDMPerfIntervalTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwctdmperfintervalnumber = YLeaf(YType.uint32, "cpwCTDMPerfIntervalNumber")

                self.cpwctdmperfintervalduration = YLeaf(YType.uint32, "cpwCTDMPerfIntervalDuration")

                self.cpwctdmperfintervaless = YLeaf(YType.uint32, "cpwCTDMPerfIntervalESs")

                self.cpwctdmperfintervalfc = YLeaf(YType.uint32, "cpwCTDMPerfIntervalFC")

                self.cpwctdmperfintervaljtrbfrunderruns = YLeaf(YType.uint32, "cpwCTDMPerfIntervalJtrBfrUnderruns")

                self.cpwctdmperfintervalmalformedpkt = YLeaf(YType.uint32, "cpwCTDMPerfIntervalMalformedPkt")

                self.cpwctdmperfintervalmisorderdropped = YLeaf(YType.uint32, "cpwCTDMPerfIntervalMisOrderDropped")

                self.cpwctdmperfintervalmissingpkts = YLeaf(YType.uint32, "cpwCTDMPerfIntervalMissingPkts")

                self.cpwctdmperfintervalpktsreorder = YLeaf(YType.uint32, "cpwCTDMPerfIntervalPktsReOrder")

                self.cpwctdmperfintervalsess = YLeaf(YType.uint32, "cpwCTDMPerfIntervalSESs")

                self.cpwctdmperfintervaluass = YLeaf(YType.uint32, "cpwCTDMPerfIntervalUASs")

                self.cpwctdmperfintervalvaliddata = YLeaf(YType.boolean, "cpwCTDMPerfIntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwctdmperfintervalnumber",
                                "cpwctdmperfintervalduration",
                                "cpwctdmperfintervaless",
                                "cpwctdmperfintervalfc",
                                "cpwctdmperfintervaljtrbfrunderruns",
                                "cpwctdmperfintervalmalformedpkt",
                                "cpwctdmperfintervalmisorderdropped",
                                "cpwctdmperfintervalmissingpkts",
                                "cpwctdmperfintervalpktsreorder",
                                "cpwctdmperfintervalsess",
                                "cpwctdmperfintervaluass",
                                "cpwctdmperfintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwctdmperfintervalnumber.is_set or
                    self.cpwctdmperfintervalduration.is_set or
                    self.cpwctdmperfintervaless.is_set or
                    self.cpwctdmperfintervalfc.is_set or
                    self.cpwctdmperfintervaljtrbfrunderruns.is_set or
                    self.cpwctdmperfintervalmalformedpkt.is_set or
                    self.cpwctdmperfintervalmisorderdropped.is_set or
                    self.cpwctdmperfintervalmissingpkts.is_set or
                    self.cpwctdmperfintervalpktsreorder.is_set or
                    self.cpwctdmperfintervalsess.is_set or
                    self.cpwctdmperfintervaluass.is_set or
                    self.cpwctdmperfintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalnumber.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalduration.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervaless.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalfc.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervaljtrbfrunderruns.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalmalformedpkt.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalmisorderdropped.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalmissingpkts.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalpktsreorder.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalsess.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervaluass.yfilter != YFilter.not_set or
                    self.cpwctdmperfintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwCTDMPerfIntervalEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + "[cpwCTDMPerfIntervalNumber='" + self.cpwctdmperfintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMPerfIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwctdmperfintervalnumber.is_set or self.cpwctdmperfintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalnumber.get_name_leafdata())
                if (self.cpwctdmperfintervalduration.is_set or self.cpwctdmperfintervalduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalduration.get_name_leafdata())
                if (self.cpwctdmperfintervaless.is_set or self.cpwctdmperfintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervaless.get_name_leafdata())
                if (self.cpwctdmperfintervalfc.is_set or self.cpwctdmperfintervalfc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalfc.get_name_leafdata())
                if (self.cpwctdmperfintervaljtrbfrunderruns.is_set or self.cpwctdmperfintervaljtrbfrunderruns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervaljtrbfrunderruns.get_name_leafdata())
                if (self.cpwctdmperfintervalmalformedpkt.is_set or self.cpwctdmperfintervalmalformedpkt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalmalformedpkt.get_name_leafdata())
                if (self.cpwctdmperfintervalmisorderdropped.is_set or self.cpwctdmperfintervalmisorderdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalmisorderdropped.get_name_leafdata())
                if (self.cpwctdmperfintervalmissingpkts.is_set or self.cpwctdmperfintervalmissingpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalmissingpkts.get_name_leafdata())
                if (self.cpwctdmperfintervalpktsreorder.is_set or self.cpwctdmperfintervalpktsreorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalpktsreorder.get_name_leafdata())
                if (self.cpwctdmperfintervalsess.is_set or self.cpwctdmperfintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalsess.get_name_leafdata())
                if (self.cpwctdmperfintervaluass.is_set or self.cpwctdmperfintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervaluass.get_name_leafdata())
                if (self.cpwctdmperfintervalvaliddata.is_set or self.cpwctdmperfintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperfintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwCTDMPerfIntervalNumber" or name == "cpwCTDMPerfIntervalDuration" or name == "cpwCTDMPerfIntervalESs" or name == "cpwCTDMPerfIntervalFC" or name == "cpwCTDMPerfIntervalJtrBfrUnderruns" or name == "cpwCTDMPerfIntervalMalformedPkt" or name == "cpwCTDMPerfIntervalMisOrderDropped" or name == "cpwCTDMPerfIntervalMissingPkts" or name == "cpwCTDMPerfIntervalPktsReOrder" or name == "cpwCTDMPerfIntervalSESs" or name == "cpwCTDMPerfIntervalUASs" or name == "cpwCTDMPerfIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalNumber"):
                    self.cpwctdmperfintervalnumber = value
                    self.cpwctdmperfintervalnumber.value_namespace = name_space
                    self.cpwctdmperfintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalDuration"):
                    self.cpwctdmperfintervalduration = value
                    self.cpwctdmperfintervalduration.value_namespace = name_space
                    self.cpwctdmperfintervalduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalESs"):
                    self.cpwctdmperfintervaless = value
                    self.cpwctdmperfintervaless.value_namespace = name_space
                    self.cpwctdmperfintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalFC"):
                    self.cpwctdmperfintervalfc = value
                    self.cpwctdmperfintervalfc.value_namespace = name_space
                    self.cpwctdmperfintervalfc.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalJtrBfrUnderruns"):
                    self.cpwctdmperfintervaljtrbfrunderruns = value
                    self.cpwctdmperfintervaljtrbfrunderruns.value_namespace = name_space
                    self.cpwctdmperfintervaljtrbfrunderruns.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalMalformedPkt"):
                    self.cpwctdmperfintervalmalformedpkt = value
                    self.cpwctdmperfintervalmalformedpkt.value_namespace = name_space
                    self.cpwctdmperfintervalmalformedpkt.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalMisOrderDropped"):
                    self.cpwctdmperfintervalmisorderdropped = value
                    self.cpwctdmperfintervalmisorderdropped.value_namespace = name_space
                    self.cpwctdmperfintervalmisorderdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalMissingPkts"):
                    self.cpwctdmperfintervalmissingpkts = value
                    self.cpwctdmperfintervalmissingpkts.value_namespace = name_space
                    self.cpwctdmperfintervalmissingpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalPktsReOrder"):
                    self.cpwctdmperfintervalpktsreorder = value
                    self.cpwctdmperfintervalpktsreorder.value_namespace = name_space
                    self.cpwctdmperfintervalpktsreorder.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalSESs"):
                    self.cpwctdmperfintervalsess = value
                    self.cpwctdmperfintervalsess.value_namespace = name_space
                    self.cpwctdmperfintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalUASs"):
                    self.cpwctdmperfintervaluass = value
                    self.cpwctdmperfintervaluass.value_namespace = name_space
                    self.cpwctdmperfintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerfIntervalValidData"):
                    self.cpwctdmperfintervalvaliddata = value
                    self.cpwctdmperfintervalvaliddata.value_namespace = name_space
                    self.cpwctdmperfintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwctdmperfintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwctdmperfintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwCTDMPerfIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwCTDMPerfIntervalEntry"):
                for c in self.cpwctdmperfintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwctdmperfintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwCTDMPerfIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpwctdmperf1Dayintervaltable(Entity):
        """
        This table provides performance information per TDM PW
        similar to the cpwCTDMPerfIntervalTable above. However,
        these counters represent historical 1 day intervals up to
        one full month. The table consists of real time data, as
        such it is not persistence across re\-boot.
        
        .. attribute:: cpwctdmperf1dayintervalentry
        
        	An entry is created in this table by the agent for every entry in the cpwCTDMTable table
        	**type**\: list of    :py:class:`Cpwctdmperf1Dayintervalentry <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry>`
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            super(CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable, self).__init__()

            self.yang_name = "cpwCTDMPerf1DayIntervalTable"
            self.yang_parent_name = "CISCO-IETF-PW-TDM-MIB"

            self.cpwctdmperf1dayintervalentry = YList(self)

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
                        super(CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable, self).__setattr__(name, value)


        class Cpwctdmperf1Dayintervalentry(Entity):
            """
            An entry is created in this table by the agent
            for every entry in the cpwCTDMTable table.
            
            .. attribute:: cpwvcindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpwvcindex <ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB.CiscoIetfPwMib.Cpwvctable.Cpwvcentry>`
            
            .. attribute:: cpwctdmperf1dayintervalnumber  <key>
            
            	The number of interval, where 1 indicates current day measured period and 2 and above indicate previous days respectively
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperf1dayintervalduration
            
            	The duration of a particular interval in seconds, Adjustments in the system's time\-of\-day clock, may cause the interval to be greater or less than, the normal value. Therefore this actual interval value is provided
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervaless
            
            	The counter associated with the number of Error Seconds encountered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervalfc
            
            	This object represents the number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperf1dayintervaljtrbfrunderruns
            
            	Number of times a packet needed to be played out and the jitter buffer was empty
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpwctdmperf1dayintervalmalformedpkt
            
            	Number of packets detected with unexpected size, or bad headers' stack
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervalmisorderdropped
            
            	Number of packets detected out of order(via control word sequence numbers), and could not be re\-ordered, or could not fit in the jitter buffer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervalmissingpkts
            
            	Number of missing packets (as detected via control word sequence number gaps)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervalpktsreorder
            
            	Number of packets detected out of sequence (via control word sequence number), but successfully re\-ordered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cpwctdmperf1dayintervalsess
            
            	The counter associated with the number of Severely Error Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervaluass
            
            	The counter associated with the number of UnAvailable Seconds. When first entering the UAS state, the number of SES To UAS is added to this object, then as each additional UAS occurs, this object increments by one
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpwctdmperf1dayintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                super(CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry, self).__init__()

                self.yang_name = "cpwCTDMPerf1DayIntervalEntry"
                self.yang_parent_name = "cpwCTDMPerf1DayIntervalTable"

                self.cpwvcindex = YLeaf(YType.str, "cpwVcIndex")

                self.cpwctdmperf1dayintervalnumber = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalNumber")

                self.cpwctdmperf1dayintervalduration = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalDuration")

                self.cpwctdmperf1dayintervaless = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalESs")

                self.cpwctdmperf1dayintervalfc = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalFC")

                self.cpwctdmperf1dayintervaljtrbfrunderruns = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalJtrBfrUnderruns")

                self.cpwctdmperf1dayintervalmalformedpkt = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalMalformedPkt")

                self.cpwctdmperf1dayintervalmisorderdropped = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalMisOrderDropped")

                self.cpwctdmperf1dayintervalmissingpkts = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalMissingPkts")

                self.cpwctdmperf1dayintervalpktsreorder = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalPktsReOrder")

                self.cpwctdmperf1dayintervalsess = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalSESs")

                self.cpwctdmperf1dayintervaluass = YLeaf(YType.uint32, "cpwCTDMPerf1DayIntervalUASs")

                self.cpwctdmperf1dayintervalvaliddata = YLeaf(YType.boolean, "cpwCTDMPerf1DayIntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpwvcindex",
                                "cpwctdmperf1dayintervalnumber",
                                "cpwctdmperf1dayintervalduration",
                                "cpwctdmperf1dayintervaless",
                                "cpwctdmperf1dayintervalfc",
                                "cpwctdmperf1dayintervaljtrbfrunderruns",
                                "cpwctdmperf1dayintervalmalformedpkt",
                                "cpwctdmperf1dayintervalmisorderdropped",
                                "cpwctdmperf1dayintervalmissingpkts",
                                "cpwctdmperf1dayintervalpktsreorder",
                                "cpwctdmperf1dayintervalsess",
                                "cpwctdmperf1dayintervaluass",
                                "cpwctdmperf1dayintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpwvcindex.is_set or
                    self.cpwctdmperf1dayintervalnumber.is_set or
                    self.cpwctdmperf1dayintervalduration.is_set or
                    self.cpwctdmperf1dayintervaless.is_set or
                    self.cpwctdmperf1dayintervalfc.is_set or
                    self.cpwctdmperf1dayintervaljtrbfrunderruns.is_set or
                    self.cpwctdmperf1dayintervalmalformedpkt.is_set or
                    self.cpwctdmperf1dayintervalmisorderdropped.is_set or
                    self.cpwctdmperf1dayintervalmissingpkts.is_set or
                    self.cpwctdmperf1dayintervalpktsreorder.is_set or
                    self.cpwctdmperf1dayintervalsess.is_set or
                    self.cpwctdmperf1dayintervaluass.is_set or
                    self.cpwctdmperf1dayintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpwvcindex.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalnumber.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalduration.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervaless.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalfc.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervaljtrbfrunderruns.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalmalformedpkt.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalmisorderdropped.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalmissingpkts.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalpktsreorder.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalsess.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervaluass.yfilter != YFilter.not_set or
                    self.cpwctdmperf1dayintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpwCTDMPerf1DayIntervalEntry" + "[cpwVcIndex='" + self.cpwvcindex.get() + "']" + "[cpwCTDMPerf1DayIntervalNumber='" + self.cpwctdmperf1dayintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/cpwCTDMPerf1DayIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpwvcindex.is_set or self.cpwvcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwvcindex.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalnumber.is_set or self.cpwctdmperf1dayintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalnumber.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalduration.is_set or self.cpwctdmperf1dayintervalduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalduration.get_name_leafdata())
                if (self.cpwctdmperf1dayintervaless.is_set or self.cpwctdmperf1dayintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervaless.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalfc.is_set or self.cpwctdmperf1dayintervalfc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalfc.get_name_leafdata())
                if (self.cpwctdmperf1dayintervaljtrbfrunderruns.is_set or self.cpwctdmperf1dayintervaljtrbfrunderruns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervaljtrbfrunderruns.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalmalformedpkt.is_set or self.cpwctdmperf1dayintervalmalformedpkt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalmalformedpkt.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalmisorderdropped.is_set or self.cpwctdmperf1dayintervalmisorderdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalmisorderdropped.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalmissingpkts.is_set or self.cpwctdmperf1dayintervalmissingpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalmissingpkts.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalpktsreorder.is_set or self.cpwctdmperf1dayintervalpktsreorder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalpktsreorder.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalsess.is_set or self.cpwctdmperf1dayintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalsess.get_name_leafdata())
                if (self.cpwctdmperf1dayintervaluass.is_set or self.cpwctdmperf1dayintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervaluass.get_name_leafdata())
                if (self.cpwctdmperf1dayintervalvaliddata.is_set or self.cpwctdmperf1dayintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpwctdmperf1dayintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpwVcIndex" or name == "cpwCTDMPerf1DayIntervalNumber" or name == "cpwCTDMPerf1DayIntervalDuration" or name == "cpwCTDMPerf1DayIntervalESs" or name == "cpwCTDMPerf1DayIntervalFC" or name == "cpwCTDMPerf1DayIntervalJtrBfrUnderruns" or name == "cpwCTDMPerf1DayIntervalMalformedPkt" or name == "cpwCTDMPerf1DayIntervalMisOrderDropped" or name == "cpwCTDMPerf1DayIntervalMissingPkts" or name == "cpwCTDMPerf1DayIntervalPktsReOrder" or name == "cpwCTDMPerf1DayIntervalSESs" or name == "cpwCTDMPerf1DayIntervalUASs" or name == "cpwCTDMPerf1DayIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpwVcIndex"):
                    self.cpwvcindex = value
                    self.cpwvcindex.value_namespace = name_space
                    self.cpwvcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalNumber"):
                    self.cpwctdmperf1dayintervalnumber = value
                    self.cpwctdmperf1dayintervalnumber.value_namespace = name_space
                    self.cpwctdmperf1dayintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalDuration"):
                    self.cpwctdmperf1dayintervalduration = value
                    self.cpwctdmperf1dayintervalduration.value_namespace = name_space
                    self.cpwctdmperf1dayintervalduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalESs"):
                    self.cpwctdmperf1dayintervaless = value
                    self.cpwctdmperf1dayintervaless.value_namespace = name_space
                    self.cpwctdmperf1dayintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalFC"):
                    self.cpwctdmperf1dayintervalfc = value
                    self.cpwctdmperf1dayintervalfc.value_namespace = name_space
                    self.cpwctdmperf1dayintervalfc.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalJtrBfrUnderruns"):
                    self.cpwctdmperf1dayintervaljtrbfrunderruns = value
                    self.cpwctdmperf1dayintervaljtrbfrunderruns.value_namespace = name_space
                    self.cpwctdmperf1dayintervaljtrbfrunderruns.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalMalformedPkt"):
                    self.cpwctdmperf1dayintervalmalformedpkt = value
                    self.cpwctdmperf1dayintervalmalformedpkt.value_namespace = name_space
                    self.cpwctdmperf1dayintervalmalformedpkt.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalMisOrderDropped"):
                    self.cpwctdmperf1dayintervalmisorderdropped = value
                    self.cpwctdmperf1dayintervalmisorderdropped.value_namespace = name_space
                    self.cpwctdmperf1dayintervalmisorderdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalMissingPkts"):
                    self.cpwctdmperf1dayintervalmissingpkts = value
                    self.cpwctdmperf1dayintervalmissingpkts.value_namespace = name_space
                    self.cpwctdmperf1dayintervalmissingpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalPktsReOrder"):
                    self.cpwctdmperf1dayintervalpktsreorder = value
                    self.cpwctdmperf1dayintervalpktsreorder.value_namespace = name_space
                    self.cpwctdmperf1dayintervalpktsreorder.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalSESs"):
                    self.cpwctdmperf1dayintervalsess = value
                    self.cpwctdmperf1dayintervalsess.value_namespace = name_space
                    self.cpwctdmperf1dayintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalUASs"):
                    self.cpwctdmperf1dayintervaluass = value
                    self.cpwctdmperf1dayintervaluass.value_namespace = name_space
                    self.cpwctdmperf1dayintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "cpwCTDMPerf1DayIntervalValidData"):
                    self.cpwctdmperf1dayintervalvaliddata = value
                    self.cpwctdmperf1dayintervalvaliddata.value_namespace = name_space
                    self.cpwctdmperf1dayintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpwctdmperf1dayintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpwctdmperf1dayintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpwCTDMPerf1DayIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpwCTDMPerf1DayIntervalEntry"):
                for c in self.cpwctdmperf1dayintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpwctdmperf1dayintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpwCTDMPerf1DayIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cpwctdmcfgtable is not None and self.cpwctdmcfgtable.has_data()) or
            (self.cpwctdmobjects is not None and self.cpwctdmobjects.has_data()) or
            (self.cpwctdmperf1dayintervaltable is not None and self.cpwctdmperf1dayintervaltable.has_data()) or
            (self.cpwctdmperfcurrenttable is not None and self.cpwctdmperfcurrenttable.has_data()) or
            (self.cpwctdmperfintervaltable is not None and self.cpwctdmperfintervaltable.has_data()) or
            (self.cpwctdmtable is not None and self.cpwctdmtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpwctdmcfgtable is not None and self.cpwctdmcfgtable.has_operation()) or
            (self.cpwctdmobjects is not None and self.cpwctdmobjects.has_operation()) or
            (self.cpwctdmperf1dayintervaltable is not None and self.cpwctdmperf1dayintervaltable.has_operation()) or
            (self.cpwctdmperfcurrenttable is not None and self.cpwctdmperfcurrenttable.has_operation()) or
            (self.cpwctdmperfintervaltable is not None and self.cpwctdmperfintervaltable.has_operation()) or
            (self.cpwctdmtable is not None and self.cpwctdmtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB" + path_buffer

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

        if (child_yang_name == "cpwCTDMCfgTable"):
            if (self.cpwctdmcfgtable is None):
                self.cpwctdmcfgtable = CiscoIetfPwTdmMib.Cpwctdmcfgtable()
                self.cpwctdmcfgtable.parent = self
                self._children_name_map["cpwctdmcfgtable"] = "cpwCTDMCfgTable"
            return self.cpwctdmcfgtable

        if (child_yang_name == "cpwCTDMObjects"):
            if (self.cpwctdmobjects is None):
                self.cpwctdmobjects = CiscoIetfPwTdmMib.Cpwctdmobjects()
                self.cpwctdmobjects.parent = self
                self._children_name_map["cpwctdmobjects"] = "cpwCTDMObjects"
            return self.cpwctdmobjects

        if (child_yang_name == "cpwCTDMPerf1DayIntervalTable"):
            if (self.cpwctdmperf1dayintervaltable is None):
                self.cpwctdmperf1dayintervaltable = CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable()
                self.cpwctdmperf1dayintervaltable.parent = self
                self._children_name_map["cpwctdmperf1dayintervaltable"] = "cpwCTDMPerf1DayIntervalTable"
            return self.cpwctdmperf1dayintervaltable

        if (child_yang_name == "cpwCTDMPerfCurrentTable"):
            if (self.cpwctdmperfcurrenttable is None):
                self.cpwctdmperfcurrenttable = CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable()
                self.cpwctdmperfcurrenttable.parent = self
                self._children_name_map["cpwctdmperfcurrenttable"] = "cpwCTDMPerfCurrentTable"
            return self.cpwctdmperfcurrenttable

        if (child_yang_name == "cpwCTDMPerfIntervalTable"):
            if (self.cpwctdmperfintervaltable is None):
                self.cpwctdmperfintervaltable = CiscoIetfPwTdmMib.Cpwctdmperfintervaltable()
                self.cpwctdmperfintervaltable.parent = self
                self._children_name_map["cpwctdmperfintervaltable"] = "cpwCTDMPerfIntervalTable"
            return self.cpwctdmperfintervaltable

        if (child_yang_name == "cpwCTDMTable"):
            if (self.cpwctdmtable is None):
                self.cpwctdmtable = CiscoIetfPwTdmMib.Cpwctdmtable()
                self.cpwctdmtable.parent = self
                self._children_name_map["cpwctdmtable"] = "cpwCTDMTable"
            return self.cpwctdmtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpwCTDMCfgTable" or name == "cpwCTDMObjects" or name == "cpwCTDMPerf1DayIntervalTable" or name == "cpwCTDMPerfCurrentTable" or name == "cpwCTDMPerfIntervalTable" or name == "cpwCTDMTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfPwTdmMib()
        return self._top_entity

