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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIetfPwTdmMib(object):
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
        self.cpwctdmcfgtable = CiscoIetfPwTdmMib.Cpwctdmcfgtable()
        self.cpwctdmcfgtable.parent = self
        self.cpwctdmobjects = CiscoIetfPwTdmMib.Cpwctdmobjects()
        self.cpwctdmobjects.parent = self
        self.cpwctdmperf1dayintervaltable = CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable()
        self.cpwctdmperf1dayintervaltable.parent = self
        self.cpwctdmperfcurrenttable = CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable()
        self.cpwctdmperfcurrenttable.parent = self
        self.cpwctdmperfintervaltable = CiscoIetfPwTdmMib.Cpwctdmperfintervaltable()
        self.cpwctdmperfintervaltable.parent = self
        self.cpwctdmtable = CiscoIetfPwTdmMib.Cpwctdmtable()
        self.cpwctdmtable.parent = self


    class Cpwctdmobjects(object):
        """
        
        
        .. attribute:: cpwctdmcfgindexnext
        
        	This object contains the value to be used for cpwCTDMCfgIndex when creating entries in the cpwCTDMCfgTable. The value 0 indicates that no unassigned entries are available.  To obtain the value of cpwCTDMCfgIndexNext for a new entry in the cpwCTDMCfgTable, the manager issues a management protocol retrieval operation. The agent will determine through its local policy when this index value will be made available for reuse
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-PW-TDM-MIB'
        _revision = '2006-07-21'

        def __init__(self):
            self.parent = None
            self.cpwctdmcfgindexnext = None

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwctdmcfgindexnext is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
            return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmobjects']['meta_info']


    class Cpwctdmtable(object):
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
            self.parent = None
            self.cpwctdmentry = YList()
            self.cpwctdmentry.parent = self
            self.cpwctdmentry.name = 'cpwctdmentry'


        class Cpwctdmentry(object):
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
                self.parent = None
                self.cpwvcindex = None
                self.cpwcgentdmcfgindex = None
                self.cpwcreltdmcfgindex = None
                self.cpwctdmconfigerror = CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmconfigerror()
                self.cpwctdmcurrentindications = CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmcurrentindications()
                self.cpwctdmifindex = None
                self.cpwctdmlastestimestamp = None
                self.cpwctdmlatchedindications = CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry.Cpwctdmlatchedindications()
                self.cpwctdmrate = None
                self.cpwctdmtimeelapsed = None
                self.cpwctdmvaliddayintervals = None
                self.cpwctdmvalidintervals = None

            class Cpwctdmconfigerror(FixedBitsDict):
                """
                Cpwctdmconfigerror

                Any of the bits are set if the local configuration is
                not compatible with the peer configuration as available
                from the various parameters options.
                
                \-tdmTypeIncompatible bit is set if the local configuration
                is not carrying the same TDM type as the peer configuration.
                
                \-peerRtpIncompatible bit is set if the local configuration
                is configured to send RTP packets for this PW, and the
                remote is not capable of accepting RTP packets.
                
                \-peerPayloadSizeIncompatible bit is set if the local
                configuration is not carrying the same Payload Size as the
                peer configuration.
                Keys are:- other , tdmTypeIncompatible , peerRtpIncompatible , peerPayloadSizeIncompatible

                """

                def __init__(self):
                    self._dictionary = { 
                        'other':False,
                        'tdmTypeIncompatible':False,
                        'peerRtpIncompatible':False,
                        'peerPayloadSizeIncompatible':False,
                    }
                    self._pos_map = { 
                        'other':0,
                        'tdmTypeIncompatible':1,
                        'peerRtpIncompatible':2,
                        'peerPayloadSizeIncompatible':3,
                    }

            class Cpwctdmcurrentindications(FixedBitsDict):
                """
                Cpwctdmcurrentindications

                The following defects should be detected and reported
                upon request\:
                
                \-Stray packets MAY be detected by the PSN and multiplexing
                layers. Stray packets MUST be discarded by the CE\-bound IWF
                and their detection MUST NOT affect mechanisms for
                detection of packet loss.
                
                \-Malformed packets are detected by mismatch between the
                expected packet size (taking the value of the L bit into
                account) and the actual packet size inferred from the PSN
                and multiplexing layers. Malformed in\-order packets MUST be
                discarded by the CE\-bound IWF and replacement data
                generated as for lost packets.
                
                \-Excessive packet loss rate is detected by computing the
                average packet loss rate over the value of
                cpwCTDMAvePktLossTimeWindow and comparing it with a
                preconfigured threshold [SATOP].
                
                \-Buffer overrun is detected in the normal operation state
                when the CE bound IWF's jitter buffer cannot accommodate
                newly arrived packets.
                
                \-Remote packet loss is indicated by reception of packets 
                with their R bit set.
                
                \-Packet misorder is detected by looking at the Sequence
                number provided by the control word.
                
                \-TDM Fault, if L bit in the control word is set, it
                indicates that TDM data carried in the payload is invalid
                due an attachment circuit fault.  When the L bit is set the
                payload MAY be omitted in order to conserve bandwidth.
                
                Note\: the algorithm used to capture these indications
                is implementation specific.
                Keys are:- pktMisOrder , tdmFault , packetLoss , bufferUnderrun , malformedPacket , bufferOverrun , remotePktLoss , other , strayPacket , excessivePktLossRate

                """

                def __init__(self):
                    self._dictionary = { 
                        'pktMisOrder':False,
                        'tdmFault':False,
                        'packetLoss':False,
                        'bufferUnderrun':False,
                        'malformedPacket':False,
                        'bufferOverrun':False,
                        'remotePktLoss':False,
                        'other':False,
                        'strayPacket':False,
                        'excessivePktLossRate':False,
                    }
                    self._pos_map = { 
                        'pktMisOrder':7,
                        'tdmFault':9,
                        'packetLoss':8,
                        'bufferUnderrun':5,
                        'malformedPacket':2,
                        'bufferOverrun':4,
                        'remotePktLoss':6,
                        'other':0,
                        'strayPacket':1,
                        'excessivePktLossRate':3,
                    }

            class Cpwctdmlatchedindications(FixedBitsDict):
                """
                Cpwctdmlatchedindications

                The state of TDM indicators when the TDM PW last declared
                an error second (either as ES, SES or a second with
                errors inside a UAS) condition. At this time, only LOPS
                can create a failure. Since indicators other than LOPS are
                useful, all are latched here. For bit definitions, see
                cpwCTDMCurrentIndications above.
                
                Note\: the algorithm used to latch these indications when
                entering a defect state is implementation specific.
                Keys are:- pktMisOrder , tdmFault , packetLoss , bufferUnderrun , malformedPacket , bufferOverrun , remotePktLoss , other , staryPacket , excessivePktLossRate

                """

                def __init__(self):
                    self._dictionary = { 
                        'pktMisOrder':False,
                        'tdmFault':False,
                        'packetLoss':False,
                        'bufferUnderrun':False,
                        'malformedPacket':False,
                        'bufferOverrun':False,
                        'remotePktLoss':False,
                        'other':False,
                        'staryPacket':False,
                        'excessivePktLossRate':False,
                    }
                    self._pos_map = { 
                        'pktMisOrder':7,
                        'tdmFault':9,
                        'packetLoss':8,
                        'bufferUnderrun':5,
                        'malformedPacket':2,
                        'bufferOverrun':4,
                        'remotePktLoss':6,
                        'other':0,
                        'staryPacket':1,
                        'excessivePktLossRate':3,
                    }

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMTable/CISCO-IETF-PW-TDM-MIB:cpwCTDMEntry[CISCO-IETF-PW-TDM-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwcgentdmcfgindex is not None:
                    return True

                if self.cpwcreltdmcfgindex is not None:
                    return True

                if self.cpwctdmconfigerror is not None:
                    if self.cpwctdmconfigerror._has_data():
                        return True

                if self.cpwctdmcurrentindications is not None:
                    if self.cpwctdmcurrentindications._has_data():
                        return True

                if self.cpwctdmifindex is not None:
                    return True

                if self.cpwctdmlastestimestamp is not None:
                    return True

                if self.cpwctdmlatchedindications is not None:
                    if self.cpwctdmlatchedindications._has_data():
                        return True

                if self.cpwctdmrate is not None:
                    return True

                if self.cpwctdmtimeelapsed is not None:
                    return True

                if self.cpwctdmvaliddayintervals is not None:
                    return True

                if self.cpwctdmvalidintervals is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmtable.Cpwctdmentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwctdmentry is not None:
                for child_ref in self.cpwctdmentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
            return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmtable']['meta_info']


    class Cpwctdmcfgtable(object):
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
            self.parent = None
            self.cpwctdmcfgentry = YList()
            self.cpwctdmcfgentry.parent = self
            self.cpwctdmcfgentry.name = 'cpwctdmcfgentry'


        class Cpwctdmcfgentry(object):
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
            	**type**\:   :py:class:`CpwctdmcfgpayloadsuppressionEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpayloadsuppressionEnum>`
            
            .. attribute:: cpwctdmcfgpktreorder
            
            	If set to true, CE bound packets are queued in the jitter buffer, out of order packets are re\-ordered. The maximum sequence number differential (i.e., the range in which re\-sequencing can occur) is dependant on the depth of the jitter buffer. See cpwCTDMCfgJtrBfrDepth
            	**type**\:  bool
            
            .. attribute:: cpwctdmcfgpktreplacepolicy
            
            	This parameter determines the value to be played when CE bound packets have over/underflow the jitter buffer, or are missing for any reason. This AIS (Alarm Indication Signal) pattern is sent (played) on the TDM line.  ais                    \- AIS (Alarm Indication Signal)                          pattern is sent (played) on                          the TDM line.  implementationSpecific \- Implementation specific pattern is                          sent on the TDM line
            	**type**\:   :py:class:`CpwctdmcfgpktreplacepolicyEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpktreplacepolicyEnum>`
            
            .. attribute:: cpwctdmcfgrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  All of the columnar objects have to be set to valid values before the row can be activated. Default value will be automatically provisioned if for those objects not specified during row creation.  No objects in cascading tables have to be populated with related data before the row can be activated.  The following objects cannot be modified if the RowStatus is active\: cpwCTDMCfgPayloadSize, cpwCTDMCfgRtpHdrUsed, cpwCTDMCfgJtrBfrDepth, and cpwCTDMCfgPayloadSuppression.  If the RowStatus is active, the following parameters can be modified\:  cpwCTDMCfgConfErr, cpwCTDMCfgPktReorder,  cpwCTDMCfgConsecPktsInSynch, cpwCTDMCfgConsecMissPktsOutSynch, cpwCTDMCfgSetUp2SynchTimeOut, cpwCTDMCfgPktReplacePolicy, cpwCTDMCfgAvePktLossTimeWindow,  cpwCTDMCfgExcessivePktLossThreshold, cpwCTDMCfgAlarmThreshold, cpwCTDMCfgClearAlarmThreshold, cpwCTDMCfgMissingPktsToSes, cpwCTDMCfgTimestampMode, cpwCTDMCfgStorageType.  A row may be deleted by setting the RowStatus to 'destroy'
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: cpwctdmcfgtimestampmode
            
            	Timestamp generation MAY be used in one of the following modes\: 1. Absolute mode\: the PSN\-bound IWF sets timestamps  using the clock recovered from the incoming TDM attachment  circuit. As a consequence, the timestamps are closely  correlated with the sequence numbers. All TDM   implementations that support usage of the RTP header MUST  support this mode. 2. Differential mode\: Both IWFs have access to a common  high\-quality timing source, and this source is used for  timestamp generation. Support of this mode is OPTIONAL
            	**type**\:   :py:class:`CpwctdmcfgtimestampmodeEnum <ydk.models.cisco_ios_xe.CISCO_IETF_PW_TDM_MIB.CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgtimestampmodeEnum>`
            
            

            """

            _prefix = 'CISCO-IETF-PW-TDM-MIB'
            _revision = '2006-07-21'

            def __init__(self):
                self.parent = None
                self.cpwctdmcfgindex = None
                self.cpwctdmcfgalarmthreshold = None
                self.cpwctdmcfgavepktlosstimewindow = None
                self.cpwctdmcfgclearalarmthreshold = None
                self.cpwctdmcfgconferr = CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.Cpwctdmcfgconferr()
                self.cpwctdmcfgconsecmisspktsoutsynch = None
                self.cpwctdmcfgconsecpktsinsynch = None
                self.cpwctdmcfgexcessivepktlossthreshold = None
                self.cpwctdmcfgjtrbfrdepth = None
                self.cpwctdmcfgmissingpktstoses = None
                self.cpwctdmcfgpayloadsize = None
                self.cpwctdmcfgpayloadsuppression = None
                self.cpwctdmcfgpktreorder = None
                self.cpwctdmcfgpktreplacepolicy = None
                self.cpwctdmcfgrowstatus = None
                self.cpwctdmcfgrtphdrused = None
                self.cpwctdmcfgsetup2synchtimeout = None
                self.cpwctdmcfgstoragetype = None
                self.cpwctdmcfgtimestampmode = None

            class CpwctdmcfgpayloadsuppressionEnum(Enum):
                """
                CpwctdmcfgpayloadsuppressionEnum

                This object indicates whether the Payload suppression

                is eanbled or disabled.

                Payload MAY be omitted in order to conserve bandwidth.

                enable  \- Payload suppression is allowed.

                disable \- No Payload suppresion under any condition.

                .. data:: enable = 1

                .. data:: disable = 2

                """

                enable = 1

                disable = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                    return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpayloadsuppressionEnum']


            class CpwctdmcfgpktreplacepolicyEnum(Enum):
                """
                CpwctdmcfgpktreplacepolicyEnum

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

                ais = 1

                implementationSpecific = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                    return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgpktreplacepolicyEnum']


            class CpwctdmcfgtimestampmodeEnum(Enum):
                """
                CpwctdmcfgtimestampmodeEnum

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

                notApplicable = 1

                absolute = 2

                differential = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                    return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry.CpwctdmcfgtimestampmodeEnum']


            class Cpwctdmcfgconferr(FixedBitsDict):
                """
                Cpwctdmcfgconferr

                This object indicates the various configuration errors,
                illegal settings within the cpwCTDMCfg table. The errors
                can be due to several reasons, like Payload size mismatch
                or Jitter Buffer depth value mistmatch. 
                
                payloadSize \- This bit is set if there is Payload size
                              mismatch between the local and peer
                              configurations. 
                jtrBfrDepth \- This bit is set if there is Jitter Buffer
                              depth value mistmatch.
                other       \- This bit is set if the error is not due to
                              payloadSize and jtrBfrDepth mismatch.
                Keys are:- other , jtrBfrDepth , payloadSize

                """

                def __init__(self):
                    self._dictionary = { 
                        'other':False,
                        'jtrBfrDepth':False,
                        'payloadSize':False,
                    }
                    self._pos_map = { 
                        'other':0,
                        'jtrBfrDepth':2,
                        'payloadSize':1,
                    }

            @property
            def _common_path(self):
                if self.cpwctdmcfgindex is None:
                    raise YPYModelError('Key property cpwctdmcfgindex is None')

                return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMCfgTable/CISCO-IETF-PW-TDM-MIB:cpwCTDMCfgEntry[CISCO-IETF-PW-TDM-MIB:cpwCTDMCfgIndex = ' + str(self.cpwctdmcfgindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwctdmcfgindex is not None:
                    return True

                if self.cpwctdmcfgalarmthreshold is not None:
                    return True

                if self.cpwctdmcfgavepktlosstimewindow is not None:
                    return True

                if self.cpwctdmcfgclearalarmthreshold is not None:
                    return True

                if self.cpwctdmcfgconferr is not None:
                    if self.cpwctdmcfgconferr._has_data():
                        return True

                if self.cpwctdmcfgconsecmisspktsoutsynch is not None:
                    return True

                if self.cpwctdmcfgconsecpktsinsynch is not None:
                    return True

                if self.cpwctdmcfgexcessivepktlossthreshold is not None:
                    return True

                if self.cpwctdmcfgjtrbfrdepth is not None:
                    return True

                if self.cpwctdmcfgmissingpktstoses is not None:
                    return True

                if self.cpwctdmcfgpayloadsize is not None:
                    return True

                if self.cpwctdmcfgpayloadsuppression is not None:
                    return True

                if self.cpwctdmcfgpktreorder is not None:
                    return True

                if self.cpwctdmcfgpktreplacepolicy is not None:
                    return True

                if self.cpwctdmcfgrowstatus is not None:
                    return True

                if self.cpwctdmcfgrtphdrused is not None:
                    return True

                if self.cpwctdmcfgsetup2synchtimeout is not None:
                    return True

                if self.cpwctdmcfgstoragetype is not None:
                    return True

                if self.cpwctdmcfgtimestampmode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable.Cpwctdmcfgentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwctdmcfgentry is not None:
                for child_ref in self.cpwctdmcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
            return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmcfgtable']['meta_info']


    class Cpwctdmperfcurrenttable(object):
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
            self.parent = None
            self.cpwctdmperfcurrententry = YList()
            self.cpwctdmperfcurrententry.parent = self
            self.cpwctdmperfcurrententry.name = 'cpwctdmperfcurrententry'


        class Cpwctdmperfcurrententry(object):
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
                self.parent = None
                self.cpwvcindex = None
                self.cpwctdmperfcurrentess = None
                self.cpwctdmperfcurrentfc = None
                self.cpwctdmperfcurrentjtrbfrunderruns = None
                self.cpwctdmperfcurrentmalformedpkt = None
                self.cpwctdmperfcurrentmisorderdropped = None
                self.cpwctdmperfcurrentmissingpkts = None
                self.cpwctdmperfcurrentpktsreorder = None
                self.cpwctdmperfcurrentsess = None
                self.cpwctdmperfcurrentuass = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')

                return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfCurrentTable/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfCurrentEntry[CISCO-IETF-PW-TDM-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwctdmperfcurrentess is not None:
                    return True

                if self.cpwctdmperfcurrentfc is not None:
                    return True

                if self.cpwctdmperfcurrentjtrbfrunderruns is not None:
                    return True

                if self.cpwctdmperfcurrentmalformedpkt is not None:
                    return True

                if self.cpwctdmperfcurrentmisorderdropped is not None:
                    return True

                if self.cpwctdmperfcurrentmissingpkts is not None:
                    return True

                if self.cpwctdmperfcurrentpktsreorder is not None:
                    return True

                if self.cpwctdmperfcurrentsess is not None:
                    return True

                if self.cpwctdmperfcurrentuass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable.Cpwctdmperfcurrententry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwctdmperfcurrententry is not None:
                for child_ref in self.cpwctdmperfcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
            return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmperfcurrenttable']['meta_info']


    class Cpwctdmperfintervaltable(object):
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
            self.parent = None
            self.cpwctdmperfintervalentry = YList()
            self.cpwctdmperfintervalentry.parent = self
            self.cpwctdmperfintervalentry.name = 'cpwctdmperfintervalentry'


        class Cpwctdmperfintervalentry(object):
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
                self.parent = None
                self.cpwvcindex = None
                self.cpwctdmperfintervalnumber = None
                self.cpwctdmperfintervalduration = None
                self.cpwctdmperfintervaless = None
                self.cpwctdmperfintervalfc = None
                self.cpwctdmperfintervaljtrbfrunderruns = None
                self.cpwctdmperfintervalmalformedpkt = None
                self.cpwctdmperfintervalmisorderdropped = None
                self.cpwctdmperfintervalmissingpkts = None
                self.cpwctdmperfintervalpktsreorder = None
                self.cpwctdmperfintervalsess = None
                self.cpwctdmperfintervaluass = None
                self.cpwctdmperfintervalvaliddata = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')
                if self.cpwctdmperfintervalnumber is None:
                    raise YPYModelError('Key property cpwctdmperfintervalnumber is None')

                return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfIntervalTable/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfIntervalEntry[CISCO-IETF-PW-TDM-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfIntervalNumber = ' + str(self.cpwctdmperfintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwctdmperfintervalnumber is not None:
                    return True

                if self.cpwctdmperfintervalduration is not None:
                    return True

                if self.cpwctdmperfintervaless is not None:
                    return True

                if self.cpwctdmperfintervalfc is not None:
                    return True

                if self.cpwctdmperfintervaljtrbfrunderruns is not None:
                    return True

                if self.cpwctdmperfintervalmalformedpkt is not None:
                    return True

                if self.cpwctdmperfintervalmisorderdropped is not None:
                    return True

                if self.cpwctdmperfintervalmissingpkts is not None:
                    return True

                if self.cpwctdmperfintervalpktsreorder is not None:
                    return True

                if self.cpwctdmperfintervalsess is not None:
                    return True

                if self.cpwctdmperfintervaluass is not None:
                    return True

                if self.cpwctdmperfintervalvaliddata is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmperfintervaltable.Cpwctdmperfintervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerfIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwctdmperfintervalentry is not None:
                for child_ref in self.cpwctdmperfintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
            return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmperfintervaltable']['meta_info']


    class Cpwctdmperf1Dayintervaltable(object):
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
            self.parent = None
            self.cpwctdmperf1dayintervalentry = YList()
            self.cpwctdmperf1dayintervalentry.parent = self
            self.cpwctdmperf1dayintervalentry.name = 'cpwctdmperf1dayintervalentry'


        class Cpwctdmperf1Dayintervalentry(object):
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
                self.parent = None
                self.cpwvcindex = None
                self.cpwctdmperf1dayintervalnumber = None
                self.cpwctdmperf1dayintervalduration = None
                self.cpwctdmperf1dayintervaless = None
                self.cpwctdmperf1dayintervalfc = None
                self.cpwctdmperf1dayintervaljtrbfrunderruns = None
                self.cpwctdmperf1dayintervalmalformedpkt = None
                self.cpwctdmperf1dayintervalmisorderdropped = None
                self.cpwctdmperf1dayintervalmissingpkts = None
                self.cpwctdmperf1dayintervalpktsreorder = None
                self.cpwctdmperf1dayintervalsess = None
                self.cpwctdmperf1dayintervaluass = None
                self.cpwctdmperf1dayintervalvaliddata = None

            @property
            def _common_path(self):
                if self.cpwvcindex is None:
                    raise YPYModelError('Key property cpwvcindex is None')
                if self.cpwctdmperf1dayintervalnumber is None:
                    raise YPYModelError('Key property cpwctdmperf1dayintervalnumber is None')

                return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerf1DayIntervalTable/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerf1DayIntervalEntry[CISCO-IETF-PW-TDM-MIB:cpwVcIndex = ' + str(self.cpwvcindex) + '][CISCO-IETF-PW-TDM-MIB:cpwCTDMPerf1DayIntervalNumber = ' + str(self.cpwctdmperf1dayintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpwvcindex is not None:
                    return True

                if self.cpwctdmperf1dayintervalnumber is not None:
                    return True

                if self.cpwctdmperf1dayintervalduration is not None:
                    return True

                if self.cpwctdmperf1dayintervaless is not None:
                    return True

                if self.cpwctdmperf1dayintervalfc is not None:
                    return True

                if self.cpwctdmperf1dayintervaljtrbfrunderruns is not None:
                    return True

                if self.cpwctdmperf1dayintervalmalformedpkt is not None:
                    return True

                if self.cpwctdmperf1dayintervalmisorderdropped is not None:
                    return True

                if self.cpwctdmperf1dayintervalmissingpkts is not None:
                    return True

                if self.cpwctdmperf1dayintervalpktsreorder is not None:
                    return True

                if self.cpwctdmperf1dayintervalsess is not None:
                    return True

                if self.cpwctdmperf1dayintervaluass is not None:
                    return True

                if self.cpwctdmperf1dayintervalvaliddata is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
                return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable.Cpwctdmperf1Dayintervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB/CISCO-IETF-PW-TDM-MIB:cpwCTDMPerf1DayIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpwctdmperf1dayintervalentry is not None:
                for child_ref in self.cpwctdmperf1dayintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
            return meta._meta_table['CiscoIetfPwTdmMib.Cpwctdmperf1Dayintervaltable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IETF-PW-TDM-MIB:CISCO-IETF-PW-TDM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cpwctdmcfgtable is not None and self.cpwctdmcfgtable._has_data():
            return True

        if self.cpwctdmobjects is not None and self.cpwctdmobjects._has_data():
            return True

        if self.cpwctdmperf1dayintervaltable is not None and self.cpwctdmperf1dayintervaltable._has_data():
            return True

        if self.cpwctdmperfcurrenttable is not None and self.cpwctdmperfcurrenttable._has_data():
            return True

        if self.cpwctdmperfintervaltable is not None and self.cpwctdmperfintervaltable._has_data():
            return True

        if self.cpwctdmtable is not None and self.cpwctdmtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IETF_PW_TDM_MIB as meta
        return meta._meta_table['CiscoIetfPwTdmMib']['meta_info']


