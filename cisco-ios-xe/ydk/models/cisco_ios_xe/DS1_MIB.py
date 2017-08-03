""" DS1_MIB 

The MIB module to describe DS1, E1, DS2, and
E2 interfaces objects.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ds1Mib(Entity):
    """
    
    
    .. attribute:: dsx1chanmappingtable
    
    	The DS1 Channel Mapping table.  This table maps a DS1 channel number on a particular DS3 into an ifIndex.  In the presence of DS2s, this table can be used to map a DS2 channel number on a DS3 into an ifIndex, or used to map a DS1 channel number on a DS2 onto an ifIndex
    	**type**\:   :py:class:`Dsx1Chanmappingtable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Chanmappingtable>`
    
    .. attribute:: dsx1configtable
    
    	The DS1 Configuration table
    	**type**\:   :py:class:`Dsx1Configtable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable>`
    
    .. attribute:: dsx1currenttable
    
    	The DS1 current table contains various statistics being collected for the current 15 minute interval
    	**type**\:   :py:class:`Dsx1Currenttable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Currenttable>`
    
    .. attribute:: dsx1farendcurrenttable
    
    	The DS1 Far End Current table contains various statistics being collected for the current 15 minute interval.  The statistics are collected from the far end messages on the Facilities Data Link.  The definitions are the same as described for the near\-end information
    	**type**\:   :py:class:`Dsx1Farendcurrenttable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Farendcurrenttable>`
    
    .. attribute:: dsx1farendintervaltable
    
    	The DS1 Far End Interval Table contains various statistics collected by each DS1 interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals. Each row in this table represents one such interval (identified by dsx1FarEndIntervalNumber) for one specific instance (identified by dsx1FarEndIntervalIndex)
    	**type**\:   :py:class:`Dsx1Farendintervaltable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Farendintervaltable>`
    
    .. attribute:: dsx1farendtotaltable
    
    	The DS1 Far End Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\:   :py:class:`Dsx1Farendtotaltable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Farendtotaltable>`
    
    .. attribute:: dsx1fractable
    
    	This table is deprecated in favour of using ifStackTable.  The table was mandatory for systems dividing a DS1 into channels containing different data streams that are of local interest.  Systems which are indifferent to data content, such as CSUs, need not implement it.  The DS1 fractional table identifies which DS1 channels associated with a CSU are being used to support a logical interface, i.e., an entry in the interfaces table from the Internet\-standard MIB.  For example, consider an application managing a North American ISDN Primary Rate link whose division is a 384 kbit/s H1 \_B\_ Channel for Video, a second H1 for data to a primary routing peer, and 12 64 kbit/s H0 \_B\_ Channels. Consider that some subset of the H0 channels are used for voice and the remainder are available for dynamic data calls.  We count a total of 14 interfaces multiplexed onto the DS1 interface. Six DS1 channels (for the sake of the example, channels 1..6) are used for Video, six more (7..11 and 13) are used for data, and the remaining 12 are are in channels 12 and 14..24.  Let us further imagine that ifIndex 2 is of type DS1 and refers to the DS1 interface, and that the interfaces layered onto it are numbered 3..16.  We might describe the allocation of channels, in the dsx1FracTable, as follows\: dsx1FracIfIndex.2. 1 = 3  dsx1FracIfIndex.2.13 = 4 dsx1FracIfIndex.2. 2 = 3  dsx1FracIfIndex.2.14 = 6 dsx1FracIfIndex.2. 3 = 3  dsx1FracIfIndex.2.15 = 7 dsx1FracIfIndex.2. 4 = 3  dsx1FracIfIndex.2.16 = 8 dsx1FracIfIndex.2. 5 = 3  dsx1FracIfIndex.2.17 = 9 dsx1FracIfIndex.2. 6 = 3  dsx1FracIfIndex.2.18 = 10 dsx1FracIfIndex.2. 7 = 4  dsx1FracIfIndex.2.19 = 11 dsx1FracIfIndex.2. 8 = 4  dsx1FracIfIndex.2.20 = 12 dsx1FracIfIndex.2. 9 = 4  dsx1FracIfIndex.2.21 = 13 dsx1FracIfIndex.2.10 = 4  dsx1FracIfIndex.2.22 = 14 dsx1FracIfIndex.2.11 = 4  dsx1FracIfIndex.2.23 = 15 dsx1FracIfIndex.2.12 = 5  dsx1FracIfIndex.2.24 = 16  For North American (DS1) interfaces, there are 24 legal channels, numbered 1 through 24.  For G.704 interfaces, there are 31 legal channels, numbered 1 through 31.  The channels (1..31) correspond directly to the equivalently numbered time\-slots
    	**type**\:   :py:class:`Dsx1Fractable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Fractable>`
    
    	**status**\: deprecated
    
    .. attribute:: dsx1intervaltable
    
    	The DS1 Interval Table contains various statistics collected by each DS1 Interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals.  Each row in this table represents one such interval (identified by dsx1IntervalNumber) for one specific instance (identified by dsx1IntervalIndex)
    	**type**\:   :py:class:`Dsx1Intervaltable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Intervaltable>`
    
    .. attribute:: dsx1totaltable
    
    	The DS1 Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\:   :py:class:`Dsx1Totaltable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Totaltable>`
    
    

    """

    _prefix = 'DS1-MIB'
    _revision = '1998-08-01'

    def __init__(self):
        super(Ds1Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "DS1-MIB"
        self.yang_parent_name = "DS1-MIB"

        self.dsx1chanmappingtable = Ds1Mib.Dsx1Chanmappingtable()
        self.dsx1chanmappingtable.parent = self
        self._children_name_map["dsx1chanmappingtable"] = "dsx1ChanMappingTable"
        self._children_yang_names.add("dsx1ChanMappingTable")

        self.dsx1configtable = Ds1Mib.Dsx1Configtable()
        self.dsx1configtable.parent = self
        self._children_name_map["dsx1configtable"] = "dsx1ConfigTable"
        self._children_yang_names.add("dsx1ConfigTable")

        self.dsx1currenttable = Ds1Mib.Dsx1Currenttable()
        self.dsx1currenttable.parent = self
        self._children_name_map["dsx1currenttable"] = "dsx1CurrentTable"
        self._children_yang_names.add("dsx1CurrentTable")

        self.dsx1farendcurrenttable = Ds1Mib.Dsx1Farendcurrenttable()
        self.dsx1farendcurrenttable.parent = self
        self._children_name_map["dsx1farendcurrenttable"] = "dsx1FarEndCurrentTable"
        self._children_yang_names.add("dsx1FarEndCurrentTable")

        self.dsx1farendintervaltable = Ds1Mib.Dsx1Farendintervaltable()
        self.dsx1farendintervaltable.parent = self
        self._children_name_map["dsx1farendintervaltable"] = "dsx1FarEndIntervalTable"
        self._children_yang_names.add("dsx1FarEndIntervalTable")

        self.dsx1farendtotaltable = Ds1Mib.Dsx1Farendtotaltable()
        self.dsx1farendtotaltable.parent = self
        self._children_name_map["dsx1farendtotaltable"] = "dsx1FarEndTotalTable"
        self._children_yang_names.add("dsx1FarEndTotalTable")

        self.dsx1fractable = Ds1Mib.Dsx1Fractable()
        self.dsx1fractable.parent = self
        self._children_name_map["dsx1fractable"] = "dsx1FracTable"
        self._children_yang_names.add("dsx1FracTable")

        self.dsx1intervaltable = Ds1Mib.Dsx1Intervaltable()
        self.dsx1intervaltable.parent = self
        self._children_name_map["dsx1intervaltable"] = "dsx1IntervalTable"
        self._children_yang_names.add("dsx1IntervalTable")

        self.dsx1totaltable = Ds1Mib.Dsx1Totaltable()
        self.dsx1totaltable.parent = self
        self._children_name_map["dsx1totaltable"] = "dsx1TotalTable"
        self._children_yang_names.add("dsx1TotalTable")


    class Dsx1Configtable(Entity):
        """
        The DS1 Configuration table.
        
        .. attribute:: dsx1configentry
        
        	An entry in the DS1 Configuration table
        	**type**\: list of    :py:class:`Dsx1Configentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Configtable, self).__init__()

            self.yang_name = "dsx1ConfigTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1configentry = YList(self)

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
                        super(Ds1Mib.Dsx1Configtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Configtable, self).__setattr__(name, value)


        class Dsx1Configentry(Entity):
            """
            An entry in the DS1 Configuration table.
            
            .. attribute:: dsx1lineindex  <key>
            
            	This object should be made equal to ifIndex.  The next paragraph describes its previous usage. Making the object equal to ifIndex allows proper use of ifStackTable and ds0/ds0bundle mibs.  Previously, this object is the identifier of a DS1 Interface on a managed device.  If there is an ifEntry that is directly associated with this and only this DS1 interface, it should have the same value as ifIndex.  Otherwise, number the dsx1LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1channelization
            
            	Indicates whether this ds1/e1 is channelized or unchannelized.  The value of enabledDs0 indicates that this is a DS1 channelized into DS0s.  The value of enabledDs1 indicated that this is a DS2 channelized into DS1s.  Setting this value will cause the creation or deletion of entries in the ifTable for the DS0s that are within the DS1
            	**type**\:   :py:class:`Dsx1Channelization <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Channelization>`
            
            .. attribute:: dsx1circuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: dsx1ds1channelnumber
            
            	This variable represents the channel number of the DS1/E1 on its parent Ds2/E2 or DS3/E3.  A value of 0 indicated this DS1/E1 does not have a parent DS3/E3
            	**type**\:  int
            
            	**range:** 0..28
            
            .. attribute:: dsx1fdl
            
            	This bitmap describes the use of  the  facili\- ties data link, and is the sum of the capabili\- ties.  Set any bits that are appropriate\:  other(1), dsx1AnsiT1403(2), dsx1Att54016(4), dsx1FdlNone(8)   'other' indicates that a protocol  other  than one following is used.   'dsx1AnsiT1403' refers to the  FDL  exchange recommended by ANSI.   'dsx1Att54016' refers to ESF FDL exchanges.   'dsx1FdlNone' indicates that the device  does not use the FDL
            	**type**\:  int
            
            	**range:** 1..15
            
            .. attribute:: dsx1ifindex
            
            	This value for this object is equal to the value of ifIndex from the Interfaces table of MIB II (RFC 1213)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: dsx1invalidintervals
            
            	The number of intervals in the range from 0 to dsx1ValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\:  int
            
            	**range:** 0..96
            
            .. attribute:: dsx1linecoding
            
            	This variable describes the variety of Zero Code Suppression used on this interface, which in turn affects a number of its characteristics.  dsx1JBZS refers the Jammed Bit Zero Suppression, in which the AT&T specification of at least one pulse every 8 bit periods is literally implemented by forcing a pulse in bit 8 of each channel. Thus, only seven bits per channel, or 1.344 Mbps, is available for data.  dsx1B8ZS refers to the use of a specified pattern of normal bits and bipolar violations which are used to replace a sequence of eight zero bits.  ANSI Clear Channels may use dsx1ZBTSI, or Zero Byte Time Slot Interchange.  E1 links, with or without CRC, use dsx1HDB3 or dsx1AMI.  dsx1AMI refers to a mode wherein no zero code suppression is present and the line encoding does not solve the problem directly.  In this application, the higher layer must provide data which meets or exceeds the pulse density requirements, such as inverting HDLC data.  dsx1B6ZS refers to the user of a specifed pattern of normal bits and bipolar violations which are used to replace a sequence of six zero bits.  Used for DS2
            	**type**\:   :py:class:`Dsx1Linecoding <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Linecoding>`
            
            .. attribute:: dsx1linelength
            
            	The length of the ds1 line in meters. This objects provides information for line build out circuitry.  This object is only useful if the interface has configurable line build out circuitry
            	**type**\:  int
            
            	**range:** 0..64000
            
            	**units**\: meters
            
            .. attribute:: dsx1linestatus
            
            	This variable indicates the Line Status of the interface.  It contains loopback, failure, received 'alarm' and transmitted 'alarms information.  The dsx1LineStatus is a bit map represented as a sum, therefore, it can represent multiple failures (alarms) and a LoopbackState simultaneously.  dsx1NoAlarm must be set if and only if no other flag is set.  If the dsx1loopbackState bit is set, the loopback in effect can be determined from the dsx1loopbackConfig object. The various bit positions are\: 1     dsx1NoAlarm           No alarm present 2     dsx1RcvFarEndLOF      Far end LOF (a.k.a., Yellow Alarm) 4     dsx1XmtFarEndLOF      Near end sending LOF Indication 8     dsx1RcvAIS            Far end sending AIS 16     dsx1XmtAIS            Near end sending AIS 32     dsx1LossOfFrame       Near end LOF (a.k.a., Red Alarm) 64     dsx1LossOfSignal      Near end Loss Of Signal 128     dsx1LoopbackState     Near end is looped 256     dsx1T16AIS            E1 TS16 AIS 512     dsx1RcvFarEndLOMF     Far End Sending TS16 LOMF 1024     dsx1XmtFarEndLOMF     Near End Sending TS16 LOMF 2048     dsx1RcvTestCode       Near End detects a test code 4096     dsx1OtherFailure      any line status not defined here 8192     dsx1UnavailSigState   Near End in Unavailable Signal                  State 16384     dsx1NetEquipOOS       Carrier Equipment Out of Service 32768     dsx1RcvPayloadAIS     DS2 Payload AIS 65536     dsx1Ds2PerfThreshold  DS2 Performance Threshold                  Exceeded
            	**type**\:  int
            
            	**range:** 1..131071
            
            .. attribute:: dsx1linestatuschangetrapenable
            
            	Indicates whether dsx1LineStatusChange traps should be generated for this interface
            	**type**\:   :py:class:`Dsx1Linestatuschangetrapenable <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Linestatuschangetrapenable>`
            
            .. attribute:: dsx1linestatuslastchange
            
            	The value of MIB II's sysUpTime object at the time this DS1 entered its current line status state.  If the current state was entered prior to the last re\-initialization of the proxy\-agent, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1linetype
            
            	This variable indicates  the  variety  of  DS1 Line  implementing  this  circuit.  The type of circuit affects the number of bits  per  second that  the circuit can reasonably carry, as well as the interpretation of the  usage  and  error statistics.  The values, in sequence, describe\:  TITLE\:         SPECIFICATION\: dsx1ESF         Extended SuperFrame DS1 (T1.107) dsx1D4          AT&T D4 format DS1 (T1.107) dsx1E1          ITU\-T Recommendation G.704                  (Table 4a) dsx1E1\-CRC      ITU\-T Recommendation G.704                  (Table 4b) dsxE1\-MF        G.704 (Table 4a) with TS16                  multiframing enabled dsx1E1\-CRC\-MF   G.704 (Table 4b) with TS16                  multiframing enabled dsx1Unframed    DS1 with No Framing dsx1E1Unframed  E1 with No Framing (G.703) dsx1DS2M12      DS2 frame format (T1.107) dsx1E2          E2 frame format (G.704)  For clarification, the capacity for each E1 type is as listed below\: dsx1E1Unframed \- E1, no framing = 32 x 64k = 2048k dsx1E1 or dsx1E1CRC \- E1, with framing,    no signalling = 31 x 64k = 1984k dsx1E1MF or dsx1E1CRCMF \- E1, with framing,    signalling = 30 x 64k = 1920k  For further information See ITU\-T Recomm G.704
            	**type**\:   :py:class:`Dsx1Linetype <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Linetype>`
            
            .. attribute:: dsx1loopbackconfig
            
            	This variable represents the desired loopback configuration of the DS1 interface.  Agents supporting read/write access should return inconsistentValue in response to a requested loopback state that the interface does not support.  The values mean\:  dsx1NoLoop  Not in the loopback state.  A device that is not capable of performing a loopback on the interface shall always return this as its value.  dsx1PayloadLoop  The received signal at this interface is looped through the device.  Typically the received signal is looped back for retransmission after it has passed through the device's framing function.  dsx1LineLoop  The received signal at this interface does not go through the device (minimum penetration) but is looped back out.  dsx1OtherLoop  Loopbacks that are not defined here.  dsx1InwardLoop  The transmitted signal at this interface is looped back and received by the same interface. What is transmitted onto the line is product dependent.  dsx1DualLoop  Both dsx1LineLoop and dsx1InwardLoop will be active simultaneously
            	**type**\:   :py:class:`Dsx1Loopbackconfig <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Loopbackconfig>`
            
            .. attribute:: dsx1loopbackstatus
            
            	This variable represents the current state of the loopback on the DS1 interface.  It contains information about loopbacks established by a manager and remotely from the far end.  The dsx1LoopbackStatus is a bit map represented as a sum, therefore is can represent multiple loopbacks simultaneously.  The various bit positions are\:  1  dsx1NoLoopback  2  dsx1NearEndPayloadLoopback  4  dsx1NearEndLineLoopback  8  dsx1NearEndOtherLoopback 16  dsx1NearEndInwardLoopback 32  dsx1FarEndPayloadLoopback 64  dsx1FarEndLineLoopback
            	**type**\:  int
            
            	**range:** 1..127
            
            .. attribute:: dsx1sendcode
            
            	This variable indicates what type of code is being sent across the DS1 interface by the device. Setting this variable causes the interface to send the code requested.  The values mean\: dsx1SendNoCode sending looped or normal data  dsx1SendLineCode sending a request for a line loopback  dsx1SendPayloadCode sending a request for a payload loopback  dsx1SendResetCode sending a loopback termination request  dsx1SendQRS sending a Quasi\-Random Signal  (QRS)  test pattern  dsx1Send511Pattern sending a 511 bit fixed test pattern  dsx1Send3in24Pattern sending a fixed test pattern of 3 bits set in 24  dsx1SendOtherTestPattern sending a test pattern  other  than  those described by this object
            	**type**\:   :py:class:`Dsx1Sendcode <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Sendcode>`
            
            .. attribute:: dsx1signalmode
            
            	'none' indicates that no bits are reserved for signaling on this channel.  'robbedBit' indicates that DS1 Robbed Bit  Sig\- naling is in use.  'bitOriented' indicates that E1 Channel  Asso\- ciated Signaling is in use.  'messageOriented' indicates that Common  Chan\- nel Signaling is in use either on channel 16 of an E1 link or channel 24 of a DS1
            	**type**\:   :py:class:`Dsx1Signalmode <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Signalmode>`
            
            .. attribute:: dsx1timeelapsed
            
            	The number of seconds that have elapsed since the beginning of the near end current error\- measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            .. attribute:: dsx1transmitclocksource
            
            	The source of Transmit Clock. 'loopTiming' indicates that the recovered re\- ceive clock is used as the transmit clock.  'localTiming' indicates that a local clock source is used or when an external clock is attached to the box containing the interface.  'throughTiming' indicates that recovered re\- ceive clock from another interface is used as the transmit clock
            	**type**\:   :py:class:`Dsx1Transmitclocksource <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1Transmitclocksource>`
            
            .. attribute:: dsx1validintervals
            
            	The number of previous near end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute near end intervals since the interface has been online.  In the case where the agent is a proxy, it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Configtable.Dsx1Configentry, self).__init__()

                self.yang_name = "dsx1ConfigEntry"
                self.yang_parent_name = "dsx1ConfigTable"

                self.dsx1lineindex = YLeaf(YType.int32, "dsx1LineIndex")

                self.dsx1channelization = YLeaf(YType.enumeration, "dsx1Channelization")

                self.dsx1circuitidentifier = YLeaf(YType.str, "dsx1CircuitIdentifier")

                self.dsx1ds1channelnumber = YLeaf(YType.int32, "dsx1Ds1ChannelNumber")

                self.dsx1fdl = YLeaf(YType.int32, "dsx1Fdl")

                self.dsx1ifindex = YLeaf(YType.int32, "dsx1IfIndex")

                self.dsx1invalidintervals = YLeaf(YType.int32, "dsx1InvalidIntervals")

                self.dsx1linecoding = YLeaf(YType.enumeration, "dsx1LineCoding")

                self.dsx1linelength = YLeaf(YType.int32, "dsx1LineLength")

                self.dsx1linestatus = YLeaf(YType.int32, "dsx1LineStatus")

                self.dsx1linestatuschangetrapenable = YLeaf(YType.enumeration, "dsx1LineStatusChangeTrapEnable")

                self.dsx1linestatuslastchange = YLeaf(YType.uint32, "dsx1LineStatusLastChange")

                self.dsx1linetype = YLeaf(YType.enumeration, "dsx1LineType")

                self.dsx1loopbackconfig = YLeaf(YType.enumeration, "dsx1LoopbackConfig")

                self.dsx1loopbackstatus = YLeaf(YType.int32, "dsx1LoopbackStatus")

                self.dsx1sendcode = YLeaf(YType.enumeration, "dsx1SendCode")

                self.dsx1signalmode = YLeaf(YType.enumeration, "dsx1SignalMode")

                self.dsx1timeelapsed = YLeaf(YType.int32, "dsx1TimeElapsed")

                self.dsx1transmitclocksource = YLeaf(YType.enumeration, "dsx1TransmitClockSource")

                self.dsx1validintervals = YLeaf(YType.int32, "dsx1ValidIntervals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1lineindex",
                                "dsx1channelization",
                                "dsx1circuitidentifier",
                                "dsx1ds1channelnumber",
                                "dsx1fdl",
                                "dsx1ifindex",
                                "dsx1invalidintervals",
                                "dsx1linecoding",
                                "dsx1linelength",
                                "dsx1linestatus",
                                "dsx1linestatuschangetrapenable",
                                "dsx1linestatuslastchange",
                                "dsx1linetype",
                                "dsx1loopbackconfig",
                                "dsx1loopbackstatus",
                                "dsx1sendcode",
                                "dsx1signalmode",
                                "dsx1timeelapsed",
                                "dsx1transmitclocksource",
                                "dsx1validintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Configtable.Dsx1Configentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Configtable.Dsx1Configentry, self).__setattr__(name, value)

            class Dsx1Channelization(Enum):
                """
                Dsx1Channelization

                Indicates whether this ds1/e1 is channelized or

                unchannelized.  The value of enabledDs0 indicates

                that this is a DS1 channelized into DS0s.  The

                value of enabledDs1 indicated that this is a DS2

                channelized into DS1s.  Setting this value will

                cause the creation or deletion of entries in the

                ifTable for the DS0s that are within the DS1.

                .. data:: disabled = 1

                .. data:: enabledDs0 = 2

                .. data:: enabledDs1 = 3

                """

                disabled = Enum.YLeaf(1, "disabled")

                enabledDs0 = Enum.YLeaf(2, "enabledDs0")

                enabledDs1 = Enum.YLeaf(3, "enabledDs1")


            class Dsx1Linecoding(Enum):
                """
                Dsx1Linecoding

                This variable describes the variety of Zero Code

                Suppression used on this interface, which in turn

                affects a number of its characteristics.

                dsx1JBZS refers the Jammed Bit Zero Suppression,

                in which the AT&T specification of at least one

                pulse every 8 bit periods is literally implemented

                by forcing a pulse in bit 8 of each channel.

                Thus, only seven bits per channel, or 1.344 Mbps,

                is available for data.

                dsx1B8ZS refers to the use of a specified pattern

                of normal bits and bipolar violations which are

                used to replace a sequence of eight zero bits.

                ANSI Clear Channels may use dsx1ZBTSI, or Zero

                Byte Time Slot Interchange.

                E1 links, with or without CRC, use dsx1HDB3 or

                dsx1AMI.

                dsx1AMI refers to a mode wherein no zero code

                suppression is present and the line encoding does

                not solve the problem directly.  In this

                application, the higher layer must provide data

                which meets or exceeds the pulse density

                requirements, such as inverting HDLC data.

                dsx1B6ZS refers to the user of a specifed pattern

                of normal bits and bipolar violations which are

                used to replace a sequence of six zero bits.  Used

                for DS2.

                .. data:: dsx1JBZS = 1

                .. data:: dsx1B8ZS = 2

                .. data:: dsx1HDB3 = 3

                .. data:: dsx1ZBTSI = 4

                .. data:: dsx1AMI = 5

                .. data:: other = 6

                .. data:: dsx1B6ZS = 7

                """

                dsx1JBZS = Enum.YLeaf(1, "dsx1JBZS")

                dsx1B8ZS = Enum.YLeaf(2, "dsx1B8ZS")

                dsx1HDB3 = Enum.YLeaf(3, "dsx1HDB3")

                dsx1ZBTSI = Enum.YLeaf(4, "dsx1ZBTSI")

                dsx1AMI = Enum.YLeaf(5, "dsx1AMI")

                other = Enum.YLeaf(6, "other")

                dsx1B6ZS = Enum.YLeaf(7, "dsx1B6ZS")


            class Dsx1Linestatuschangetrapenable(Enum):
                """
                Dsx1Linestatuschangetrapenable

                Indicates whether dsx1LineStatusChange traps

                should be generated for this interface.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Dsx1Linetype(Enum):
                """
                Dsx1Linetype

                This variable indicates  the  variety  of  DS1

                Line  implementing  this  circuit.  The type of

                circuit affects the number of bits  per  second

                that  the circuit can reasonably carry, as well

                as the interpretation of the  usage  and  error

                statistics.  The values, in sequence, describe\:

                TITLE\:         SPECIFICATION\:

                dsx1ESF         Extended SuperFrame DS1 (T1.107)

                dsx1D4          AT&T D4 format DS1 (T1.107)

                dsx1E1          ITU\-T Recommendation G.704

                                 (Table 4a)

                dsx1E1\-CRC      ITU\-T Recommendation G.704

                                 (Table 4b)

                dsxE1\-MF        G.704 (Table 4a) with TS16

                                 multiframing enabled

                dsx1E1\-CRC\-MF   G.704 (Table 4b) with TS16

                                 multiframing enabled

                dsx1Unframed    DS1 with No Framing

                dsx1E1Unframed  E1 with No Framing (G.703)

                dsx1DS2M12      DS2 frame format (T1.107)

                dsx1E2          E2 frame format (G.704)

                For clarification, the capacity for each E1 type

                is as listed below\:

                dsx1E1Unframed \- E1, no framing = 32 x 64k = 2048k

                dsx1E1 or dsx1E1CRC \- E1, with framing,

                   no signalling = 31 x 64k = 1984k

                dsx1E1MF or dsx1E1CRCMF \- E1, with framing,

                   signalling = 30 x 64k = 1920k

                For further information See ITU\-T Recomm G.704

                .. data:: other = 1

                .. data:: dsx1ESF = 2

                .. data:: dsx1D4 = 3

                .. data:: dsx1E1 = 4

                .. data:: dsx1E1CRC = 5

                .. data:: dsx1E1MF = 6

                .. data:: dsx1E1CRCMF = 7

                .. data:: dsx1Unframed = 8

                .. data:: dsx1E1Unframed = 9

                .. data:: dsx1DS2M12 = 10

                .. data:: dsx2E2 = 11

                """

                other = Enum.YLeaf(1, "other")

                dsx1ESF = Enum.YLeaf(2, "dsx1ESF")

                dsx1D4 = Enum.YLeaf(3, "dsx1D4")

                dsx1E1 = Enum.YLeaf(4, "dsx1E1")

                dsx1E1CRC = Enum.YLeaf(5, "dsx1E1CRC")

                dsx1E1MF = Enum.YLeaf(6, "dsx1E1MF")

                dsx1E1CRCMF = Enum.YLeaf(7, "dsx1E1CRCMF")

                dsx1Unframed = Enum.YLeaf(8, "dsx1Unframed")

                dsx1E1Unframed = Enum.YLeaf(9, "dsx1E1Unframed")

                dsx1DS2M12 = Enum.YLeaf(10, "dsx1DS2M12")

                dsx2E2 = Enum.YLeaf(11, "dsx2E2")


            class Dsx1Loopbackconfig(Enum):
                """
                Dsx1Loopbackconfig

                This variable represents the desired loopback

                configuration of the DS1 interface.  Agents

                supporting read/write access should return

                inconsistentValue in response to a requested

                loopback state that the interface does not

                support.  The values mean\:

                dsx1NoLoop

                 Not in the loopback state.  A device that is not

                capable of performing a loopback on the interface

                shall always return this as its value.

                dsx1PayloadLoop

                 The received signal at this interface is looped

                through the device.  Typically the received signal

                is looped back for retransmission after it has

                passed through the device's framing function.

                dsx1LineLoop

                 The received signal at this interface does not go

                through the device (minimum penetration) but is

                looped back out.

                dsx1OtherLoop

                 Loopbacks that are not defined here.

                dsx1InwardLoop

                 The transmitted signal at this interface is

                looped back and received by the same interface.

                What is transmitted onto the line is product

                dependent.

                dsx1DualLoop

                 Both dsx1LineLoop and dsx1InwardLoop will be

                active simultaneously.

                .. data:: dsx1NoLoop = 1

                .. data:: dsx1PayloadLoop = 2

                .. data:: dsx1LineLoop = 3

                .. data:: dsx1OtherLoop = 4

                .. data:: dsx1InwardLoop = 5

                .. data:: dsx1DualLoop = 6

                """

                dsx1NoLoop = Enum.YLeaf(1, "dsx1NoLoop")

                dsx1PayloadLoop = Enum.YLeaf(2, "dsx1PayloadLoop")

                dsx1LineLoop = Enum.YLeaf(3, "dsx1LineLoop")

                dsx1OtherLoop = Enum.YLeaf(4, "dsx1OtherLoop")

                dsx1InwardLoop = Enum.YLeaf(5, "dsx1InwardLoop")

                dsx1DualLoop = Enum.YLeaf(6, "dsx1DualLoop")


            class Dsx1Sendcode(Enum):
                """
                Dsx1Sendcode

                This variable indicates what type of code is

                being sent across the DS1 interface by the device.

                Setting this variable causes the interface to send

                the code requested.  The values mean\:

                dsx1SendNoCode

                sending looped or normal data

                dsx1SendLineCode

                sending a request for a line loopback

                dsx1SendPayloadCode

                sending a request for a payload loopback

                dsx1SendResetCode

                sending a loopback termination request

                dsx1SendQRS

                sending a Quasi\-Random Signal  (QRS)  test

                pattern

                dsx1Send511Pattern

                sending a 511 bit fixed test pattern

                dsx1Send3in24Pattern

                sending a fixed test pattern of 3 bits set

                in 24

                dsx1SendOtherTestPattern

                sending a test pattern  other  than  those

                described by this object

                .. data:: dsx1SendNoCode = 1

                .. data:: dsx1SendLineCode = 2

                .. data:: dsx1SendPayloadCode = 3

                .. data:: dsx1SendResetCode = 4

                .. data:: dsx1SendQRS = 5

                .. data:: dsx1Send511Pattern = 6

                .. data:: dsx1Send3in24Pattern = 7

                .. data:: dsx1SendOtherTestPattern = 8

                """

                dsx1SendNoCode = Enum.YLeaf(1, "dsx1SendNoCode")

                dsx1SendLineCode = Enum.YLeaf(2, "dsx1SendLineCode")

                dsx1SendPayloadCode = Enum.YLeaf(3, "dsx1SendPayloadCode")

                dsx1SendResetCode = Enum.YLeaf(4, "dsx1SendResetCode")

                dsx1SendQRS = Enum.YLeaf(5, "dsx1SendQRS")

                dsx1Send511Pattern = Enum.YLeaf(6, "dsx1Send511Pattern")

                dsx1Send3in24Pattern = Enum.YLeaf(7, "dsx1Send3in24Pattern")

                dsx1SendOtherTestPattern = Enum.YLeaf(8, "dsx1SendOtherTestPattern")


            class Dsx1Signalmode(Enum):
                """
                Dsx1Signalmode

                'none' indicates that no bits are reserved for

                signaling on this channel.

                'robbedBit' indicates that DS1 Robbed Bit  Sig\-

                naling is in use.

                'bitOriented' indicates that E1 Channel  Asso\-

                ciated Signaling is in use.

                'messageOriented' indicates that Common  Chan\-

                nel Signaling is in use either on channel 16 of

                an E1 link or channel 24 of a DS1.

                .. data:: none = 1

                .. data:: robbedBit = 2

                .. data:: bitOriented = 3

                .. data:: messageOriented = 4

                .. data:: other = 5

                """

                none = Enum.YLeaf(1, "none")

                robbedBit = Enum.YLeaf(2, "robbedBit")

                bitOriented = Enum.YLeaf(3, "bitOriented")

                messageOriented = Enum.YLeaf(4, "messageOriented")

                other = Enum.YLeaf(5, "other")


            class Dsx1Transmitclocksource(Enum):
                """
                Dsx1Transmitclocksource

                The source of Transmit Clock.

                'loopTiming' indicates that the recovered re\-

                ceive clock is used as the transmit clock.

                'localTiming' indicates that a local clock

                source is used or when an external clock is

                attached to the box containing the interface.

                'throughTiming' indicates that recovered re\-

                ceive clock from another interface is used as

                the transmit clock.

                .. data:: loopTiming = 1

                .. data:: localTiming = 2

                .. data:: throughTiming = 3

                """

                loopTiming = Enum.YLeaf(1, "loopTiming")

                localTiming = Enum.YLeaf(2, "localTiming")

                throughTiming = Enum.YLeaf(3, "throughTiming")


            def has_data(self):
                return (
                    self.dsx1lineindex.is_set or
                    self.dsx1channelization.is_set or
                    self.dsx1circuitidentifier.is_set or
                    self.dsx1ds1channelnumber.is_set or
                    self.dsx1fdl.is_set or
                    self.dsx1ifindex.is_set or
                    self.dsx1invalidintervals.is_set or
                    self.dsx1linecoding.is_set or
                    self.dsx1linelength.is_set or
                    self.dsx1linestatus.is_set or
                    self.dsx1linestatuschangetrapenable.is_set or
                    self.dsx1linestatuslastchange.is_set or
                    self.dsx1linetype.is_set or
                    self.dsx1loopbackconfig.is_set or
                    self.dsx1loopbackstatus.is_set or
                    self.dsx1sendcode.is_set or
                    self.dsx1signalmode.is_set or
                    self.dsx1timeelapsed.is_set or
                    self.dsx1transmitclocksource.is_set or
                    self.dsx1validintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1lineindex.yfilter != YFilter.not_set or
                    self.dsx1channelization.yfilter != YFilter.not_set or
                    self.dsx1circuitidentifier.yfilter != YFilter.not_set or
                    self.dsx1ds1channelnumber.yfilter != YFilter.not_set or
                    self.dsx1fdl.yfilter != YFilter.not_set or
                    self.dsx1ifindex.yfilter != YFilter.not_set or
                    self.dsx1invalidintervals.yfilter != YFilter.not_set or
                    self.dsx1linecoding.yfilter != YFilter.not_set or
                    self.dsx1linelength.yfilter != YFilter.not_set or
                    self.dsx1linestatus.yfilter != YFilter.not_set or
                    self.dsx1linestatuschangetrapenable.yfilter != YFilter.not_set or
                    self.dsx1linestatuslastchange.yfilter != YFilter.not_set or
                    self.dsx1linetype.yfilter != YFilter.not_set or
                    self.dsx1loopbackconfig.yfilter != YFilter.not_set or
                    self.dsx1loopbackstatus.yfilter != YFilter.not_set or
                    self.dsx1sendcode.yfilter != YFilter.not_set or
                    self.dsx1signalmode.yfilter != YFilter.not_set or
                    self.dsx1timeelapsed.yfilter != YFilter.not_set or
                    self.dsx1transmitclocksource.yfilter != YFilter.not_set or
                    self.dsx1validintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1ConfigEntry" + "[dsx1LineIndex='" + self.dsx1lineindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1ConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1lineindex.is_set or self.dsx1lineindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1lineindex.get_name_leafdata())
                if (self.dsx1channelization.is_set or self.dsx1channelization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1channelization.get_name_leafdata())
                if (self.dsx1circuitidentifier.is_set or self.dsx1circuitidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1circuitidentifier.get_name_leafdata())
                if (self.dsx1ds1channelnumber.is_set or self.dsx1ds1channelnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1ds1channelnumber.get_name_leafdata())
                if (self.dsx1fdl.is_set or self.dsx1fdl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1fdl.get_name_leafdata())
                if (self.dsx1ifindex.is_set or self.dsx1ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1ifindex.get_name_leafdata())
                if (self.dsx1invalidintervals.is_set or self.dsx1invalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1invalidintervals.get_name_leafdata())
                if (self.dsx1linecoding.is_set or self.dsx1linecoding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1linecoding.get_name_leafdata())
                if (self.dsx1linelength.is_set or self.dsx1linelength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1linelength.get_name_leafdata())
                if (self.dsx1linestatus.is_set or self.dsx1linestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1linestatus.get_name_leafdata())
                if (self.dsx1linestatuschangetrapenable.is_set or self.dsx1linestatuschangetrapenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1linestatuschangetrapenable.get_name_leafdata())
                if (self.dsx1linestatuslastchange.is_set or self.dsx1linestatuslastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1linestatuslastchange.get_name_leafdata())
                if (self.dsx1linetype.is_set or self.dsx1linetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1linetype.get_name_leafdata())
                if (self.dsx1loopbackconfig.is_set or self.dsx1loopbackconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1loopbackconfig.get_name_leafdata())
                if (self.dsx1loopbackstatus.is_set or self.dsx1loopbackstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1loopbackstatus.get_name_leafdata())
                if (self.dsx1sendcode.is_set or self.dsx1sendcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1sendcode.get_name_leafdata())
                if (self.dsx1signalmode.is_set or self.dsx1signalmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1signalmode.get_name_leafdata())
                if (self.dsx1timeelapsed.is_set or self.dsx1timeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1timeelapsed.get_name_leafdata())
                if (self.dsx1transmitclocksource.is_set or self.dsx1transmitclocksource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1transmitclocksource.get_name_leafdata())
                if (self.dsx1validintervals.is_set or self.dsx1validintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1validintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1LineIndex" or name == "dsx1Channelization" or name == "dsx1CircuitIdentifier" or name == "dsx1Ds1ChannelNumber" or name == "dsx1Fdl" or name == "dsx1IfIndex" or name == "dsx1InvalidIntervals" or name == "dsx1LineCoding" or name == "dsx1LineLength" or name == "dsx1LineStatus" or name == "dsx1LineStatusChangeTrapEnable" or name == "dsx1LineStatusLastChange" or name == "dsx1LineType" or name == "dsx1LoopbackConfig" or name == "dsx1LoopbackStatus" or name == "dsx1SendCode" or name == "dsx1SignalMode" or name == "dsx1TimeElapsed" or name == "dsx1TransmitClockSource" or name == "dsx1ValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1LineIndex"):
                    self.dsx1lineindex = value
                    self.dsx1lineindex.value_namespace = name_space
                    self.dsx1lineindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1Channelization"):
                    self.dsx1channelization = value
                    self.dsx1channelization.value_namespace = name_space
                    self.dsx1channelization.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CircuitIdentifier"):
                    self.dsx1circuitidentifier = value
                    self.dsx1circuitidentifier.value_namespace = name_space
                    self.dsx1circuitidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1Ds1ChannelNumber"):
                    self.dsx1ds1channelnumber = value
                    self.dsx1ds1channelnumber.value_namespace = name_space
                    self.dsx1ds1channelnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1Fdl"):
                    self.dsx1fdl = value
                    self.dsx1fdl.value_namespace = name_space
                    self.dsx1fdl.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IfIndex"):
                    self.dsx1ifindex = value
                    self.dsx1ifindex.value_namespace = name_space
                    self.dsx1ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1InvalidIntervals"):
                    self.dsx1invalidintervals = value
                    self.dsx1invalidintervals.value_namespace = name_space
                    self.dsx1invalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LineCoding"):
                    self.dsx1linecoding = value
                    self.dsx1linecoding.value_namespace = name_space
                    self.dsx1linecoding.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LineLength"):
                    self.dsx1linelength = value
                    self.dsx1linelength.value_namespace = name_space
                    self.dsx1linelength.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LineStatus"):
                    self.dsx1linestatus = value
                    self.dsx1linestatus.value_namespace = name_space
                    self.dsx1linestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LineStatusChangeTrapEnable"):
                    self.dsx1linestatuschangetrapenable = value
                    self.dsx1linestatuschangetrapenable.value_namespace = name_space
                    self.dsx1linestatuschangetrapenable.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LineStatusLastChange"):
                    self.dsx1linestatuslastchange = value
                    self.dsx1linestatuslastchange.value_namespace = name_space
                    self.dsx1linestatuslastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LineType"):
                    self.dsx1linetype = value
                    self.dsx1linetype.value_namespace = name_space
                    self.dsx1linetype.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LoopbackConfig"):
                    self.dsx1loopbackconfig = value
                    self.dsx1loopbackconfig.value_namespace = name_space
                    self.dsx1loopbackconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1LoopbackStatus"):
                    self.dsx1loopbackstatus = value
                    self.dsx1loopbackstatus.value_namespace = name_space
                    self.dsx1loopbackstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1SendCode"):
                    self.dsx1sendcode = value
                    self.dsx1sendcode.value_namespace = name_space
                    self.dsx1sendcode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1SignalMode"):
                    self.dsx1signalmode = value
                    self.dsx1signalmode.value_namespace = name_space
                    self.dsx1signalmode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TimeElapsed"):
                    self.dsx1timeelapsed = value
                    self.dsx1timeelapsed.value_namespace = name_space
                    self.dsx1timeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TransmitClockSource"):
                    self.dsx1transmitclocksource = value
                    self.dsx1transmitclocksource.value_namespace = name_space
                    self.dsx1transmitclocksource.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1ValidIntervals"):
                    self.dsx1validintervals = value
                    self.dsx1validintervals.value_namespace = name_space
                    self.dsx1validintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1configentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1configentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1ConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1ConfigEntry"):
                for c in self.dsx1configentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Configtable.Dsx1Configentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1configentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1ConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Currenttable(Entity):
        """
        The DS1 current table contains various statistics
        being collected for the current 15 minute
        interval.
        
        .. attribute:: dsx1currententry
        
        	An entry in the DS1 Current table
        	**type**\: list of    :py:class:`Dsx1Currententry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Currenttable.Dsx1Currententry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Currenttable, self).__init__()

            self.yang_name = "dsx1CurrentTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1currententry = YList(self)

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
                        super(Ds1Mib.Dsx1Currenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Currenttable, self).__setattr__(name, value)


        class Dsx1Currententry(Entity):
            """
            An entry in the DS1 Current table.
            
            .. attribute:: dsx1currentindex  <key>
            
            	The index value which uniquely identifies  the DS1 interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value as a dsx1LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1currentbess
            
            	The number of Bursty Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentcsss
            
            	The number of Controlled Slip Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentdms
            
            	The number of Degraded Minutes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentess
            
            	The number of Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentlcvs
            
            	The number of Line Code Violations (LCVs)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentless
            
            	The number of Line Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentpcvs
            
            	The number of Path Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentsefss
            
            	The number of Severely Errored Framing Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentsess
            
            	The number of Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1currentuass
            
            	The number of Unavailable Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Currenttable.Dsx1Currententry, self).__init__()

                self.yang_name = "dsx1CurrentEntry"
                self.yang_parent_name = "dsx1CurrentTable"

                self.dsx1currentindex = YLeaf(YType.int32, "dsx1CurrentIndex")

                self.dsx1currentbess = YLeaf(YType.uint32, "dsx1CurrentBESs")

                self.dsx1currentcsss = YLeaf(YType.uint32, "dsx1CurrentCSSs")

                self.dsx1currentdms = YLeaf(YType.uint32, "dsx1CurrentDMs")

                self.dsx1currentess = YLeaf(YType.uint32, "dsx1CurrentESs")

                self.dsx1currentlcvs = YLeaf(YType.uint32, "dsx1CurrentLCVs")

                self.dsx1currentless = YLeaf(YType.uint32, "dsx1CurrentLESs")

                self.dsx1currentpcvs = YLeaf(YType.uint32, "dsx1CurrentPCVs")

                self.dsx1currentsefss = YLeaf(YType.uint32, "dsx1CurrentSEFSs")

                self.dsx1currentsess = YLeaf(YType.uint32, "dsx1CurrentSESs")

                self.dsx1currentuass = YLeaf(YType.uint32, "dsx1CurrentUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1currentindex",
                                "dsx1currentbess",
                                "dsx1currentcsss",
                                "dsx1currentdms",
                                "dsx1currentess",
                                "dsx1currentlcvs",
                                "dsx1currentless",
                                "dsx1currentpcvs",
                                "dsx1currentsefss",
                                "dsx1currentsess",
                                "dsx1currentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Currenttable.Dsx1Currententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Currenttable.Dsx1Currententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1currentindex.is_set or
                    self.dsx1currentbess.is_set or
                    self.dsx1currentcsss.is_set or
                    self.dsx1currentdms.is_set or
                    self.dsx1currentess.is_set or
                    self.dsx1currentlcvs.is_set or
                    self.dsx1currentless.is_set or
                    self.dsx1currentpcvs.is_set or
                    self.dsx1currentsefss.is_set or
                    self.dsx1currentsess.is_set or
                    self.dsx1currentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1currentindex.yfilter != YFilter.not_set or
                    self.dsx1currentbess.yfilter != YFilter.not_set or
                    self.dsx1currentcsss.yfilter != YFilter.not_set or
                    self.dsx1currentdms.yfilter != YFilter.not_set or
                    self.dsx1currentess.yfilter != YFilter.not_set or
                    self.dsx1currentlcvs.yfilter != YFilter.not_set or
                    self.dsx1currentless.yfilter != YFilter.not_set or
                    self.dsx1currentpcvs.yfilter != YFilter.not_set or
                    self.dsx1currentsefss.yfilter != YFilter.not_set or
                    self.dsx1currentsess.yfilter != YFilter.not_set or
                    self.dsx1currentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1CurrentEntry" + "[dsx1CurrentIndex='" + self.dsx1currentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1CurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1currentindex.is_set or self.dsx1currentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentindex.get_name_leafdata())
                if (self.dsx1currentbess.is_set or self.dsx1currentbess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentbess.get_name_leafdata())
                if (self.dsx1currentcsss.is_set or self.dsx1currentcsss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentcsss.get_name_leafdata())
                if (self.dsx1currentdms.is_set or self.dsx1currentdms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentdms.get_name_leafdata())
                if (self.dsx1currentess.is_set or self.dsx1currentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentess.get_name_leafdata())
                if (self.dsx1currentlcvs.is_set or self.dsx1currentlcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentlcvs.get_name_leafdata())
                if (self.dsx1currentless.is_set or self.dsx1currentless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentless.get_name_leafdata())
                if (self.dsx1currentpcvs.is_set or self.dsx1currentpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentpcvs.get_name_leafdata())
                if (self.dsx1currentsefss.is_set or self.dsx1currentsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentsefss.get_name_leafdata())
                if (self.dsx1currentsess.is_set or self.dsx1currentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentsess.get_name_leafdata())
                if (self.dsx1currentuass.is_set or self.dsx1currentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1currentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1CurrentIndex" or name == "dsx1CurrentBESs" or name == "dsx1CurrentCSSs" or name == "dsx1CurrentDMs" or name == "dsx1CurrentESs" or name == "dsx1CurrentLCVs" or name == "dsx1CurrentLESs" or name == "dsx1CurrentPCVs" or name == "dsx1CurrentSEFSs" or name == "dsx1CurrentSESs" or name == "dsx1CurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1CurrentIndex"):
                    self.dsx1currentindex = value
                    self.dsx1currentindex.value_namespace = name_space
                    self.dsx1currentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentBESs"):
                    self.dsx1currentbess = value
                    self.dsx1currentbess.value_namespace = name_space
                    self.dsx1currentbess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentCSSs"):
                    self.dsx1currentcsss = value
                    self.dsx1currentcsss.value_namespace = name_space
                    self.dsx1currentcsss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentDMs"):
                    self.dsx1currentdms = value
                    self.dsx1currentdms.value_namespace = name_space
                    self.dsx1currentdms.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentESs"):
                    self.dsx1currentess = value
                    self.dsx1currentess.value_namespace = name_space
                    self.dsx1currentess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentLCVs"):
                    self.dsx1currentlcvs = value
                    self.dsx1currentlcvs.value_namespace = name_space
                    self.dsx1currentlcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentLESs"):
                    self.dsx1currentless = value
                    self.dsx1currentless.value_namespace = name_space
                    self.dsx1currentless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentPCVs"):
                    self.dsx1currentpcvs = value
                    self.dsx1currentpcvs.value_namespace = name_space
                    self.dsx1currentpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentSEFSs"):
                    self.dsx1currentsefss = value
                    self.dsx1currentsefss.value_namespace = name_space
                    self.dsx1currentsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentSESs"):
                    self.dsx1currentsess = value
                    self.dsx1currentsess.value_namespace = name_space
                    self.dsx1currentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1CurrentUASs"):
                    self.dsx1currentuass = value
                    self.dsx1currentuass.value_namespace = name_space
                    self.dsx1currentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1currententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1currententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1CurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1CurrentEntry"):
                for c in self.dsx1currententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Currenttable.Dsx1Currententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1currententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1CurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Intervaltable(Entity):
        """
        The DS1 Interval Table contains various
        statistics collected by each DS1 Interface over
        the previous 24 hours of operation.  The past 24
        hours are broken into 96 completed 15 minute
        intervals.  Each row in this table represents one
        such interval (identified by dsx1IntervalNumber)
        for one specific instance (identified by
        dsx1IntervalIndex).
        
        .. attribute:: dsx1intervalentry
        
        	An entry in the DS1 Interval table
        	**type**\: list of    :py:class:`Dsx1Intervalentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Intervaltable, self).__init__()

            self.yang_name = "dsx1IntervalTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1intervalentry = YList(self)

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
                        super(Ds1Mib.Dsx1Intervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Intervaltable, self).__setattr__(name, value)


        class Dsx1Intervalentry(Entity):
            """
            An entry in the DS1 Interval table.
            
            .. attribute:: dsx1intervalindex  <key>
            
            	The index value which uniquely identifies the DS1 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value as a dsx1LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1intervalnumber  <key>
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: dsx1intervalbess
            
            	The number of Bursty Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervalcsss
            
            	The number of Controlled Slip Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervaldms
            
            	The number of Degraded Minutes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervaless
            
            	The number of Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervallcvs
            
            	The number of Line Code Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervalless
            
            	The number of Line Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervalpcvs
            
            	The number of Path Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervalsefss
            
            	The number of Severely Errored Framing Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervalsess
            
            	The number of Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervaluass
            
            	The number of Unavailable Seconds.  This object may decrease if the occurance of unavailable seconds occurs across an inteval boundary
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1intervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry, self).__init__()

                self.yang_name = "dsx1IntervalEntry"
                self.yang_parent_name = "dsx1IntervalTable"

                self.dsx1intervalindex = YLeaf(YType.int32, "dsx1IntervalIndex")

                self.dsx1intervalnumber = YLeaf(YType.int32, "dsx1IntervalNumber")

                self.dsx1intervalbess = YLeaf(YType.uint32, "dsx1IntervalBESs")

                self.dsx1intervalcsss = YLeaf(YType.uint32, "dsx1IntervalCSSs")

                self.dsx1intervaldms = YLeaf(YType.uint32, "dsx1IntervalDMs")

                self.dsx1intervaless = YLeaf(YType.uint32, "dsx1IntervalESs")

                self.dsx1intervallcvs = YLeaf(YType.uint32, "dsx1IntervalLCVs")

                self.dsx1intervalless = YLeaf(YType.uint32, "dsx1IntervalLESs")

                self.dsx1intervalpcvs = YLeaf(YType.uint32, "dsx1IntervalPCVs")

                self.dsx1intervalsefss = YLeaf(YType.uint32, "dsx1IntervalSEFSs")

                self.dsx1intervalsess = YLeaf(YType.uint32, "dsx1IntervalSESs")

                self.dsx1intervaluass = YLeaf(YType.uint32, "dsx1IntervalUASs")

                self.dsx1intervalvaliddata = YLeaf(YType.boolean, "dsx1IntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1intervalindex",
                                "dsx1intervalnumber",
                                "dsx1intervalbess",
                                "dsx1intervalcsss",
                                "dsx1intervaldms",
                                "dsx1intervaless",
                                "dsx1intervallcvs",
                                "dsx1intervalless",
                                "dsx1intervalpcvs",
                                "dsx1intervalsefss",
                                "dsx1intervalsess",
                                "dsx1intervaluass",
                                "dsx1intervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1intervalindex.is_set or
                    self.dsx1intervalnumber.is_set or
                    self.dsx1intervalbess.is_set or
                    self.dsx1intervalcsss.is_set or
                    self.dsx1intervaldms.is_set or
                    self.dsx1intervaless.is_set or
                    self.dsx1intervallcvs.is_set or
                    self.dsx1intervalless.is_set or
                    self.dsx1intervalpcvs.is_set or
                    self.dsx1intervalsefss.is_set or
                    self.dsx1intervalsess.is_set or
                    self.dsx1intervaluass.is_set or
                    self.dsx1intervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1intervalindex.yfilter != YFilter.not_set or
                    self.dsx1intervalnumber.yfilter != YFilter.not_set or
                    self.dsx1intervalbess.yfilter != YFilter.not_set or
                    self.dsx1intervalcsss.yfilter != YFilter.not_set or
                    self.dsx1intervaldms.yfilter != YFilter.not_set or
                    self.dsx1intervaless.yfilter != YFilter.not_set or
                    self.dsx1intervallcvs.yfilter != YFilter.not_set or
                    self.dsx1intervalless.yfilter != YFilter.not_set or
                    self.dsx1intervalpcvs.yfilter != YFilter.not_set or
                    self.dsx1intervalsefss.yfilter != YFilter.not_set or
                    self.dsx1intervalsess.yfilter != YFilter.not_set or
                    self.dsx1intervaluass.yfilter != YFilter.not_set or
                    self.dsx1intervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1IntervalEntry" + "[dsx1IntervalIndex='" + self.dsx1intervalindex.get() + "']" + "[dsx1IntervalNumber='" + self.dsx1intervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1IntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1intervalindex.is_set or self.dsx1intervalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalindex.get_name_leafdata())
                if (self.dsx1intervalnumber.is_set or self.dsx1intervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalnumber.get_name_leafdata())
                if (self.dsx1intervalbess.is_set or self.dsx1intervalbess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalbess.get_name_leafdata())
                if (self.dsx1intervalcsss.is_set or self.dsx1intervalcsss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalcsss.get_name_leafdata())
                if (self.dsx1intervaldms.is_set or self.dsx1intervaldms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervaldms.get_name_leafdata())
                if (self.dsx1intervaless.is_set or self.dsx1intervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervaless.get_name_leafdata())
                if (self.dsx1intervallcvs.is_set or self.dsx1intervallcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervallcvs.get_name_leafdata())
                if (self.dsx1intervalless.is_set or self.dsx1intervalless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalless.get_name_leafdata())
                if (self.dsx1intervalpcvs.is_set or self.dsx1intervalpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalpcvs.get_name_leafdata())
                if (self.dsx1intervalsefss.is_set or self.dsx1intervalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalsefss.get_name_leafdata())
                if (self.dsx1intervalsess.is_set or self.dsx1intervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalsess.get_name_leafdata())
                if (self.dsx1intervaluass.is_set or self.dsx1intervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervaluass.get_name_leafdata())
                if (self.dsx1intervalvaliddata.is_set or self.dsx1intervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1intervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1IntervalIndex" or name == "dsx1IntervalNumber" or name == "dsx1IntervalBESs" or name == "dsx1IntervalCSSs" or name == "dsx1IntervalDMs" or name == "dsx1IntervalESs" or name == "dsx1IntervalLCVs" or name == "dsx1IntervalLESs" or name == "dsx1IntervalPCVs" or name == "dsx1IntervalSEFSs" or name == "dsx1IntervalSESs" or name == "dsx1IntervalUASs" or name == "dsx1IntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1IntervalIndex"):
                    self.dsx1intervalindex = value
                    self.dsx1intervalindex.value_namespace = name_space
                    self.dsx1intervalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalNumber"):
                    self.dsx1intervalnumber = value
                    self.dsx1intervalnumber.value_namespace = name_space
                    self.dsx1intervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalBESs"):
                    self.dsx1intervalbess = value
                    self.dsx1intervalbess.value_namespace = name_space
                    self.dsx1intervalbess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalCSSs"):
                    self.dsx1intervalcsss = value
                    self.dsx1intervalcsss.value_namespace = name_space
                    self.dsx1intervalcsss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalDMs"):
                    self.dsx1intervaldms = value
                    self.dsx1intervaldms.value_namespace = name_space
                    self.dsx1intervaldms.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalESs"):
                    self.dsx1intervaless = value
                    self.dsx1intervaless.value_namespace = name_space
                    self.dsx1intervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalLCVs"):
                    self.dsx1intervallcvs = value
                    self.dsx1intervallcvs.value_namespace = name_space
                    self.dsx1intervallcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalLESs"):
                    self.dsx1intervalless = value
                    self.dsx1intervalless.value_namespace = name_space
                    self.dsx1intervalless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalPCVs"):
                    self.dsx1intervalpcvs = value
                    self.dsx1intervalpcvs.value_namespace = name_space
                    self.dsx1intervalpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalSEFSs"):
                    self.dsx1intervalsefss = value
                    self.dsx1intervalsefss.value_namespace = name_space
                    self.dsx1intervalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalSESs"):
                    self.dsx1intervalsess = value
                    self.dsx1intervalsess.value_namespace = name_space
                    self.dsx1intervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalUASs"):
                    self.dsx1intervaluass = value
                    self.dsx1intervaluass.value_namespace = name_space
                    self.dsx1intervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1IntervalValidData"):
                    self.dsx1intervalvaliddata = value
                    self.dsx1intervalvaliddata.value_namespace = name_space
                    self.dsx1intervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1intervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1intervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1IntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1IntervalEntry"):
                for c in self.dsx1intervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1intervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1IntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Totaltable(Entity):
        """
        The DS1 Total Table contains the cumulative sum
        of the various statistics for the 24 hour period
        preceding the current interval.
        
        .. attribute:: dsx1totalentry
        
        	An entry in the DS1 Total table
        	**type**\: list of    :py:class:`Dsx1Totalentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Totaltable.Dsx1Totalentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Totaltable, self).__init__()

            self.yang_name = "dsx1TotalTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1totalentry = YList(self)

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
                        super(Ds1Mib.Dsx1Totaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Totaltable, self).__setattr__(name, value)


        class Dsx1Totalentry(Entity):
            """
            An entry in the DS1 Total table.
            
            .. attribute:: dsx1totalindex  <key>
            
            	The index value which uniquely identifies the DS1 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value as a dsx1LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1totalbess
            
            	The number of Bursty Errored Seconds (BESs) encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totalcsss
            
            	The number of Controlled Slip Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totaldms
            
            	The number of Degraded Minutes (DMs) encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totaless
            
            	The sum of Errored Seconds encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totallcvs
            
            	The number of Line Code Violations (LCVs) encountered by a DS1 interface in the current 15 minute interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totalless
            
            	The number of Line Errored Seconds encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totalpcvs
            
            	The number of Path Coding Violations encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totalsefss
            
            	The number of Severely Errored Framing Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totalsess
            
            	The number of Severely Errored Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1totaluass
            
            	The number of Unavailable Seconds encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Totaltable.Dsx1Totalentry, self).__init__()

                self.yang_name = "dsx1TotalEntry"
                self.yang_parent_name = "dsx1TotalTable"

                self.dsx1totalindex = YLeaf(YType.int32, "dsx1TotalIndex")

                self.dsx1totalbess = YLeaf(YType.uint32, "dsx1TotalBESs")

                self.dsx1totalcsss = YLeaf(YType.uint32, "dsx1TotalCSSs")

                self.dsx1totaldms = YLeaf(YType.uint32, "dsx1TotalDMs")

                self.dsx1totaless = YLeaf(YType.uint32, "dsx1TotalESs")

                self.dsx1totallcvs = YLeaf(YType.uint32, "dsx1TotalLCVs")

                self.dsx1totalless = YLeaf(YType.uint32, "dsx1TotalLESs")

                self.dsx1totalpcvs = YLeaf(YType.uint32, "dsx1TotalPCVs")

                self.dsx1totalsefss = YLeaf(YType.uint32, "dsx1TotalSEFSs")

                self.dsx1totalsess = YLeaf(YType.uint32, "dsx1TotalSESs")

                self.dsx1totaluass = YLeaf(YType.uint32, "dsx1TotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1totalindex",
                                "dsx1totalbess",
                                "dsx1totalcsss",
                                "dsx1totaldms",
                                "dsx1totaless",
                                "dsx1totallcvs",
                                "dsx1totalless",
                                "dsx1totalpcvs",
                                "dsx1totalsefss",
                                "dsx1totalsess",
                                "dsx1totaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Totaltable.Dsx1Totalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Totaltable.Dsx1Totalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1totalindex.is_set or
                    self.dsx1totalbess.is_set or
                    self.dsx1totalcsss.is_set or
                    self.dsx1totaldms.is_set or
                    self.dsx1totaless.is_set or
                    self.dsx1totallcvs.is_set or
                    self.dsx1totalless.is_set or
                    self.dsx1totalpcvs.is_set or
                    self.dsx1totalsefss.is_set or
                    self.dsx1totalsess.is_set or
                    self.dsx1totaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1totalindex.yfilter != YFilter.not_set or
                    self.dsx1totalbess.yfilter != YFilter.not_set or
                    self.dsx1totalcsss.yfilter != YFilter.not_set or
                    self.dsx1totaldms.yfilter != YFilter.not_set or
                    self.dsx1totaless.yfilter != YFilter.not_set or
                    self.dsx1totallcvs.yfilter != YFilter.not_set or
                    self.dsx1totalless.yfilter != YFilter.not_set or
                    self.dsx1totalpcvs.yfilter != YFilter.not_set or
                    self.dsx1totalsefss.yfilter != YFilter.not_set or
                    self.dsx1totalsess.yfilter != YFilter.not_set or
                    self.dsx1totaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1TotalEntry" + "[dsx1TotalIndex='" + self.dsx1totalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1TotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1totalindex.is_set or self.dsx1totalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalindex.get_name_leafdata())
                if (self.dsx1totalbess.is_set or self.dsx1totalbess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalbess.get_name_leafdata())
                if (self.dsx1totalcsss.is_set or self.dsx1totalcsss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalcsss.get_name_leafdata())
                if (self.dsx1totaldms.is_set or self.dsx1totaldms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totaldms.get_name_leafdata())
                if (self.dsx1totaless.is_set or self.dsx1totaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totaless.get_name_leafdata())
                if (self.dsx1totallcvs.is_set or self.dsx1totallcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totallcvs.get_name_leafdata())
                if (self.dsx1totalless.is_set or self.dsx1totalless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalless.get_name_leafdata())
                if (self.dsx1totalpcvs.is_set or self.dsx1totalpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalpcvs.get_name_leafdata())
                if (self.dsx1totalsefss.is_set or self.dsx1totalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalsefss.get_name_leafdata())
                if (self.dsx1totalsess.is_set or self.dsx1totalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totalsess.get_name_leafdata())
                if (self.dsx1totaluass.is_set or self.dsx1totaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1totaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1TotalIndex" or name == "dsx1TotalBESs" or name == "dsx1TotalCSSs" or name == "dsx1TotalDMs" or name == "dsx1TotalESs" or name == "dsx1TotalLCVs" or name == "dsx1TotalLESs" or name == "dsx1TotalPCVs" or name == "dsx1TotalSEFSs" or name == "dsx1TotalSESs" or name == "dsx1TotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1TotalIndex"):
                    self.dsx1totalindex = value
                    self.dsx1totalindex.value_namespace = name_space
                    self.dsx1totalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalBESs"):
                    self.dsx1totalbess = value
                    self.dsx1totalbess.value_namespace = name_space
                    self.dsx1totalbess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalCSSs"):
                    self.dsx1totalcsss = value
                    self.dsx1totalcsss.value_namespace = name_space
                    self.dsx1totalcsss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalDMs"):
                    self.dsx1totaldms = value
                    self.dsx1totaldms.value_namespace = name_space
                    self.dsx1totaldms.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalESs"):
                    self.dsx1totaless = value
                    self.dsx1totaless.value_namespace = name_space
                    self.dsx1totaless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalLCVs"):
                    self.dsx1totallcvs = value
                    self.dsx1totallcvs.value_namespace = name_space
                    self.dsx1totallcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalLESs"):
                    self.dsx1totalless = value
                    self.dsx1totalless.value_namespace = name_space
                    self.dsx1totalless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalPCVs"):
                    self.dsx1totalpcvs = value
                    self.dsx1totalpcvs.value_namespace = name_space
                    self.dsx1totalpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalSEFSs"):
                    self.dsx1totalsefss = value
                    self.dsx1totalsefss.value_namespace = name_space
                    self.dsx1totalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalSESs"):
                    self.dsx1totalsess = value
                    self.dsx1totalsess.value_namespace = name_space
                    self.dsx1totalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1TotalUASs"):
                    self.dsx1totaluass = value
                    self.dsx1totaluass.value_namespace = name_space
                    self.dsx1totaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1totalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1totalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1TotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1TotalEntry"):
                for c in self.dsx1totalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Totaltable.Dsx1Totalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1totalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1TotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Farendcurrenttable(Entity):
        """
        The DS1 Far End Current table contains various
        statistics being collected for the current 15
        minute interval.  The statistics are collected
        from the far end messages on the Facilities Data
        Link.  The definitions are the same as described
        for the near\-end information.
        
        .. attribute:: dsx1farendcurrententry
        
        	An entry in the DS1 Far End Current table
        	**type**\: list of    :py:class:`Dsx1Farendcurrententry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Farendcurrenttable, self).__init__()

            self.yang_name = "dsx1FarEndCurrentTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1farendcurrententry = YList(self)

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
                        super(Ds1Mib.Dsx1Farendcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Farendcurrenttable, self).__setattr__(name, value)


        class Dsx1Farendcurrententry(Entity):
            """
            An entry in the DS1 Far End Current table.
            
            .. attribute:: dsx1farendcurrentindex  <key>
            
            	The index value which uniquely identifies the DS1 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx1LineIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1farendcurrentbess
            
            	The number of Far End Bursty Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentcsss
            
            	The number of Far End Controlled Slip Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentdms
            
            	The number of Far End Degraded Minutes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentess
            
            	The number of Far End Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentless
            
            	The number of Far End Line Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentpcvs
            
            	The number of Far End Path Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentsefss
            
            	The number of Far End Severely Errored Framing Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentsess
            
            	The number of Far End Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendcurrentuass
            
            	The number of Unavailable Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendinvalidintervals
            
            	The number of intervals in the range from 0 to dsx1FarEndValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\:  int
            
            	**range:** 0..96
            
            .. attribute:: dsx1farendtimeelapsed
            
            	The number of seconds that have elapsed since the beginning of the far end current error\-measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            .. attribute:: dsx1farendvalidintervals
            
            	The number of previous far end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute far end intervals since the interface has been online
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry, self).__init__()

                self.yang_name = "dsx1FarEndCurrentEntry"
                self.yang_parent_name = "dsx1FarEndCurrentTable"

                self.dsx1farendcurrentindex = YLeaf(YType.int32, "dsx1FarEndCurrentIndex")

                self.dsx1farendcurrentbess = YLeaf(YType.uint32, "dsx1FarEndCurrentBESs")

                self.dsx1farendcurrentcsss = YLeaf(YType.uint32, "dsx1FarEndCurrentCSSs")

                self.dsx1farendcurrentdms = YLeaf(YType.uint32, "dsx1FarEndCurrentDMs")

                self.dsx1farendcurrentess = YLeaf(YType.uint32, "dsx1FarEndCurrentESs")

                self.dsx1farendcurrentless = YLeaf(YType.uint32, "dsx1FarEndCurrentLESs")

                self.dsx1farendcurrentpcvs = YLeaf(YType.uint32, "dsx1FarEndCurrentPCVs")

                self.dsx1farendcurrentsefss = YLeaf(YType.uint32, "dsx1FarEndCurrentSEFSs")

                self.dsx1farendcurrentsess = YLeaf(YType.uint32, "dsx1FarEndCurrentSESs")

                self.dsx1farendcurrentuass = YLeaf(YType.uint32, "dsx1FarEndCurrentUASs")

                self.dsx1farendinvalidintervals = YLeaf(YType.int32, "dsx1FarEndInvalidIntervals")

                self.dsx1farendtimeelapsed = YLeaf(YType.int32, "dsx1FarEndTimeElapsed")

                self.dsx1farendvalidintervals = YLeaf(YType.int32, "dsx1FarEndValidIntervals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1farendcurrentindex",
                                "dsx1farendcurrentbess",
                                "dsx1farendcurrentcsss",
                                "dsx1farendcurrentdms",
                                "dsx1farendcurrentess",
                                "dsx1farendcurrentless",
                                "dsx1farendcurrentpcvs",
                                "dsx1farendcurrentsefss",
                                "dsx1farendcurrentsess",
                                "dsx1farendcurrentuass",
                                "dsx1farendinvalidintervals",
                                "dsx1farendtimeelapsed",
                                "dsx1farendvalidintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1farendcurrentindex.is_set or
                    self.dsx1farendcurrentbess.is_set or
                    self.dsx1farendcurrentcsss.is_set or
                    self.dsx1farendcurrentdms.is_set or
                    self.dsx1farendcurrentess.is_set or
                    self.dsx1farendcurrentless.is_set or
                    self.dsx1farendcurrentpcvs.is_set or
                    self.dsx1farendcurrentsefss.is_set or
                    self.dsx1farendcurrentsess.is_set or
                    self.dsx1farendcurrentuass.is_set or
                    self.dsx1farendinvalidintervals.is_set or
                    self.dsx1farendtimeelapsed.is_set or
                    self.dsx1farendvalidintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentindex.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentbess.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentcsss.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentdms.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentess.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentless.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentpcvs.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentsefss.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentsess.yfilter != YFilter.not_set or
                    self.dsx1farendcurrentuass.yfilter != YFilter.not_set or
                    self.dsx1farendinvalidintervals.yfilter != YFilter.not_set or
                    self.dsx1farendtimeelapsed.yfilter != YFilter.not_set or
                    self.dsx1farendvalidintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1FarEndCurrentEntry" + "[dsx1FarEndCurrentIndex='" + self.dsx1farendcurrentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1FarEndCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1farendcurrentindex.is_set or self.dsx1farendcurrentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentindex.get_name_leafdata())
                if (self.dsx1farendcurrentbess.is_set or self.dsx1farendcurrentbess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentbess.get_name_leafdata())
                if (self.dsx1farendcurrentcsss.is_set or self.dsx1farendcurrentcsss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentcsss.get_name_leafdata())
                if (self.dsx1farendcurrentdms.is_set or self.dsx1farendcurrentdms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentdms.get_name_leafdata())
                if (self.dsx1farendcurrentess.is_set or self.dsx1farendcurrentess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentess.get_name_leafdata())
                if (self.dsx1farendcurrentless.is_set or self.dsx1farendcurrentless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentless.get_name_leafdata())
                if (self.dsx1farendcurrentpcvs.is_set or self.dsx1farendcurrentpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentpcvs.get_name_leafdata())
                if (self.dsx1farendcurrentsefss.is_set or self.dsx1farendcurrentsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentsefss.get_name_leafdata())
                if (self.dsx1farendcurrentsess.is_set or self.dsx1farendcurrentsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentsess.get_name_leafdata())
                if (self.dsx1farendcurrentuass.is_set or self.dsx1farendcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendcurrentuass.get_name_leafdata())
                if (self.dsx1farendinvalidintervals.is_set or self.dsx1farendinvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendinvalidintervals.get_name_leafdata())
                if (self.dsx1farendtimeelapsed.is_set or self.dsx1farendtimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtimeelapsed.get_name_leafdata())
                if (self.dsx1farendvalidintervals.is_set or self.dsx1farendvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendvalidintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1FarEndCurrentIndex" or name == "dsx1FarEndCurrentBESs" or name == "dsx1FarEndCurrentCSSs" or name == "dsx1FarEndCurrentDMs" or name == "dsx1FarEndCurrentESs" or name == "dsx1FarEndCurrentLESs" or name == "dsx1FarEndCurrentPCVs" or name == "dsx1FarEndCurrentSEFSs" or name == "dsx1FarEndCurrentSESs" or name == "dsx1FarEndCurrentUASs" or name == "dsx1FarEndInvalidIntervals" or name == "dsx1FarEndTimeElapsed" or name == "dsx1FarEndValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1FarEndCurrentIndex"):
                    self.dsx1farendcurrentindex = value
                    self.dsx1farendcurrentindex.value_namespace = name_space
                    self.dsx1farendcurrentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentBESs"):
                    self.dsx1farendcurrentbess = value
                    self.dsx1farendcurrentbess.value_namespace = name_space
                    self.dsx1farendcurrentbess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentCSSs"):
                    self.dsx1farendcurrentcsss = value
                    self.dsx1farendcurrentcsss.value_namespace = name_space
                    self.dsx1farendcurrentcsss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentDMs"):
                    self.dsx1farendcurrentdms = value
                    self.dsx1farendcurrentdms.value_namespace = name_space
                    self.dsx1farendcurrentdms.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentESs"):
                    self.dsx1farendcurrentess = value
                    self.dsx1farendcurrentess.value_namespace = name_space
                    self.dsx1farendcurrentess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentLESs"):
                    self.dsx1farendcurrentless = value
                    self.dsx1farendcurrentless.value_namespace = name_space
                    self.dsx1farendcurrentless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentPCVs"):
                    self.dsx1farendcurrentpcvs = value
                    self.dsx1farendcurrentpcvs.value_namespace = name_space
                    self.dsx1farendcurrentpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentSEFSs"):
                    self.dsx1farendcurrentsefss = value
                    self.dsx1farendcurrentsefss.value_namespace = name_space
                    self.dsx1farendcurrentsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentSESs"):
                    self.dsx1farendcurrentsess = value
                    self.dsx1farendcurrentsess.value_namespace = name_space
                    self.dsx1farendcurrentsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndCurrentUASs"):
                    self.dsx1farendcurrentuass = value
                    self.dsx1farendcurrentuass.value_namespace = name_space
                    self.dsx1farendcurrentuass.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndInvalidIntervals"):
                    self.dsx1farendinvalidintervals = value
                    self.dsx1farendinvalidintervals.value_namespace = name_space
                    self.dsx1farendinvalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTimeElapsed"):
                    self.dsx1farendtimeelapsed = value
                    self.dsx1farendtimeelapsed.value_namespace = name_space
                    self.dsx1farendtimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndValidIntervals"):
                    self.dsx1farendvalidintervals = value
                    self.dsx1farendvalidintervals.value_namespace = name_space
                    self.dsx1farendvalidintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1farendcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1farendcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1FarEndCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1FarEndCurrentEntry"):
                for c in self.dsx1farendcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1farendcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1FarEndCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Farendintervaltable(Entity):
        """
        The DS1 Far End Interval Table contains various
        statistics collected by each DS1 interface over
        the previous 24 hours of operation.  The past 24
        hours are broken into 96 completed 15 minute
        intervals. Each row in this table represents one
        such interval (identified by
        dsx1FarEndIntervalNumber) for one specific
        instance (identified by dsx1FarEndIntervalIndex).
        
        .. attribute:: dsx1farendintervalentry
        
        	An entry in the DS1 Far End Interval table
        	**type**\: list of    :py:class:`Dsx1Farendintervalentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Farendintervaltable, self).__init__()

            self.yang_name = "dsx1FarEndIntervalTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1farendintervalentry = YList(self)

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
                        super(Ds1Mib.Dsx1Farendintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Farendintervaltable, self).__setattr__(name, value)


        class Dsx1Farendintervalentry(Entity):
            """
            An entry in the DS1 Far End Interval table.
            
            .. attribute:: dsx1farendintervalindex  <key>
            
            	The index value which uniquely identifies the DS1 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx1LineIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1farendintervalnumber  <key>
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: dsx1farendintervalbess
            
            	The number of Far End Bursty Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervalcsss
            
            	The number of Far End Controlled Slip Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervaldms
            
            	The number of Far End Degraded Minutes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervaless
            
            	The number of Far End Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervalless
            
            	The number of Far End Line Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervalpcvs
            
            	The number of Far End Path Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervalsefss
            
            	The number of Far End Severely Errored Framing Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervalsess
            
            	The number of Far End Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervaluass
            
            	The number of Unavailable Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry, self).__init__()

                self.yang_name = "dsx1FarEndIntervalEntry"
                self.yang_parent_name = "dsx1FarEndIntervalTable"

                self.dsx1farendintervalindex = YLeaf(YType.int32, "dsx1FarEndIntervalIndex")

                self.dsx1farendintervalnumber = YLeaf(YType.int32, "dsx1FarEndIntervalNumber")

                self.dsx1farendintervalbess = YLeaf(YType.uint32, "dsx1FarEndIntervalBESs")

                self.dsx1farendintervalcsss = YLeaf(YType.uint32, "dsx1FarEndIntervalCSSs")

                self.dsx1farendintervaldms = YLeaf(YType.uint32, "dsx1FarEndIntervalDMs")

                self.dsx1farendintervaless = YLeaf(YType.uint32, "dsx1FarEndIntervalESs")

                self.dsx1farendintervalless = YLeaf(YType.uint32, "dsx1FarEndIntervalLESs")

                self.dsx1farendintervalpcvs = YLeaf(YType.uint32, "dsx1FarEndIntervalPCVs")

                self.dsx1farendintervalsefss = YLeaf(YType.uint32, "dsx1FarEndIntervalSEFSs")

                self.dsx1farendintervalsess = YLeaf(YType.uint32, "dsx1FarEndIntervalSESs")

                self.dsx1farendintervaluass = YLeaf(YType.uint32, "dsx1FarEndIntervalUASs")

                self.dsx1farendintervalvaliddata = YLeaf(YType.boolean, "dsx1FarEndIntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1farendintervalindex",
                                "dsx1farendintervalnumber",
                                "dsx1farendintervalbess",
                                "dsx1farendintervalcsss",
                                "dsx1farendintervaldms",
                                "dsx1farendintervaless",
                                "dsx1farendintervalless",
                                "dsx1farendintervalpcvs",
                                "dsx1farendintervalsefss",
                                "dsx1farendintervalsess",
                                "dsx1farendintervaluass",
                                "dsx1farendintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1farendintervalindex.is_set or
                    self.dsx1farendintervalnumber.is_set or
                    self.dsx1farendintervalbess.is_set or
                    self.dsx1farendintervalcsss.is_set or
                    self.dsx1farendintervaldms.is_set or
                    self.dsx1farendintervaless.is_set or
                    self.dsx1farendintervalless.is_set or
                    self.dsx1farendintervalpcvs.is_set or
                    self.dsx1farendintervalsefss.is_set or
                    self.dsx1farendintervalsess.is_set or
                    self.dsx1farendintervaluass.is_set or
                    self.dsx1farendintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1farendintervalindex.yfilter != YFilter.not_set or
                    self.dsx1farendintervalnumber.yfilter != YFilter.not_set or
                    self.dsx1farendintervalbess.yfilter != YFilter.not_set or
                    self.dsx1farendintervalcsss.yfilter != YFilter.not_set or
                    self.dsx1farendintervaldms.yfilter != YFilter.not_set or
                    self.dsx1farendintervaless.yfilter != YFilter.not_set or
                    self.dsx1farendintervalless.yfilter != YFilter.not_set or
                    self.dsx1farendintervalpcvs.yfilter != YFilter.not_set or
                    self.dsx1farendintervalsefss.yfilter != YFilter.not_set or
                    self.dsx1farendintervalsess.yfilter != YFilter.not_set or
                    self.dsx1farendintervaluass.yfilter != YFilter.not_set or
                    self.dsx1farendintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1FarEndIntervalEntry" + "[dsx1FarEndIntervalIndex='" + self.dsx1farendintervalindex.get() + "']" + "[dsx1FarEndIntervalNumber='" + self.dsx1farendintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1FarEndIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1farendintervalindex.is_set or self.dsx1farendintervalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalindex.get_name_leafdata())
                if (self.dsx1farendintervalnumber.is_set or self.dsx1farendintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalnumber.get_name_leafdata())
                if (self.dsx1farendintervalbess.is_set or self.dsx1farendintervalbess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalbess.get_name_leafdata())
                if (self.dsx1farendintervalcsss.is_set or self.dsx1farendintervalcsss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalcsss.get_name_leafdata())
                if (self.dsx1farendintervaldms.is_set or self.dsx1farendintervaldms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervaldms.get_name_leafdata())
                if (self.dsx1farendintervaless.is_set or self.dsx1farendintervaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervaless.get_name_leafdata())
                if (self.dsx1farendintervalless.is_set or self.dsx1farendintervalless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalless.get_name_leafdata())
                if (self.dsx1farendintervalpcvs.is_set or self.dsx1farendintervalpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalpcvs.get_name_leafdata())
                if (self.dsx1farendintervalsefss.is_set or self.dsx1farendintervalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalsefss.get_name_leafdata())
                if (self.dsx1farendintervalsess.is_set or self.dsx1farendintervalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalsess.get_name_leafdata())
                if (self.dsx1farendintervaluass.is_set or self.dsx1farendintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervaluass.get_name_leafdata())
                if (self.dsx1farendintervalvaliddata.is_set or self.dsx1farendintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1FarEndIntervalIndex" or name == "dsx1FarEndIntervalNumber" or name == "dsx1FarEndIntervalBESs" or name == "dsx1FarEndIntervalCSSs" or name == "dsx1FarEndIntervalDMs" or name == "dsx1FarEndIntervalESs" or name == "dsx1FarEndIntervalLESs" or name == "dsx1FarEndIntervalPCVs" or name == "dsx1FarEndIntervalSEFSs" or name == "dsx1FarEndIntervalSESs" or name == "dsx1FarEndIntervalUASs" or name == "dsx1FarEndIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1FarEndIntervalIndex"):
                    self.dsx1farendintervalindex = value
                    self.dsx1farendintervalindex.value_namespace = name_space
                    self.dsx1farendintervalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalNumber"):
                    self.dsx1farendintervalnumber = value
                    self.dsx1farendintervalnumber.value_namespace = name_space
                    self.dsx1farendintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalBESs"):
                    self.dsx1farendintervalbess = value
                    self.dsx1farendintervalbess.value_namespace = name_space
                    self.dsx1farendintervalbess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalCSSs"):
                    self.dsx1farendintervalcsss = value
                    self.dsx1farendintervalcsss.value_namespace = name_space
                    self.dsx1farendintervalcsss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalDMs"):
                    self.dsx1farendintervaldms = value
                    self.dsx1farendintervaldms.value_namespace = name_space
                    self.dsx1farendintervaldms.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalESs"):
                    self.dsx1farendintervaless = value
                    self.dsx1farendintervaless.value_namespace = name_space
                    self.dsx1farendintervaless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalLESs"):
                    self.dsx1farendintervalless = value
                    self.dsx1farendintervalless.value_namespace = name_space
                    self.dsx1farendintervalless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalPCVs"):
                    self.dsx1farendintervalpcvs = value
                    self.dsx1farendintervalpcvs.value_namespace = name_space
                    self.dsx1farendintervalpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalSEFSs"):
                    self.dsx1farendintervalsefss = value
                    self.dsx1farendintervalsefss.value_namespace = name_space
                    self.dsx1farendintervalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalSESs"):
                    self.dsx1farendintervalsess = value
                    self.dsx1farendintervalsess.value_namespace = name_space
                    self.dsx1farendintervalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalUASs"):
                    self.dsx1farendintervaluass = value
                    self.dsx1farendintervaluass.value_namespace = name_space
                    self.dsx1farendintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndIntervalValidData"):
                    self.dsx1farendintervalvaliddata = value
                    self.dsx1farendintervalvaliddata.value_namespace = name_space
                    self.dsx1farendintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1farendintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1farendintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1FarEndIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1FarEndIntervalEntry"):
                for c in self.dsx1farendintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1farendintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1FarEndIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Farendtotaltable(Entity):
        """
        The DS1 Far End Total Table contains the
        cumulative sum of the various statistics for the
        24 hour period preceding the current interval.
        
        .. attribute:: dsx1farendtotalentry
        
        	An entry in the DS1 Far End Total table
        	**type**\: list of    :py:class:`Dsx1Farendtotalentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Farendtotaltable, self).__init__()

            self.yang_name = "dsx1FarEndTotalTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1farendtotalentry = YList(self)

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
                        super(Ds1Mib.Dsx1Farendtotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Farendtotaltable, self).__setattr__(name, value)


        class Dsx1Farendtotalentry(Entity):
            """
            An entry in the DS1 Far End Total table.
            
            .. attribute:: dsx1farendtotalindex  <key>
            
            	The index value which uniquely identifies the DS1 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx1LineIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1farendtotalbess
            
            	The number of Bursty Errored Seconds (BESs) encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotalcsss
            
            	The number of Far End Controlled Slip Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotaldms
            
            	The number of Degraded Minutes (DMs) encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotaless
            
            	The number of Far End Errored Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotalless
            
            	The number of Far End Line Errored Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotalpcvs
            
            	The number of Far End Path Coding Violations reported via the far end block error count encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotalsefss
            
            	The number of Far End Severely Errored Framing Seconds encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotalsess
            
            	The number of Far End Severely Errored Seconds encountered by a DS1 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1farendtotaluass
            
            	The number of Unavailable Seconds encountered by a DS1 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry, self).__init__()

                self.yang_name = "dsx1FarEndTotalEntry"
                self.yang_parent_name = "dsx1FarEndTotalTable"

                self.dsx1farendtotalindex = YLeaf(YType.int32, "dsx1FarEndTotalIndex")

                self.dsx1farendtotalbess = YLeaf(YType.uint32, "dsx1FarEndTotalBESs")

                self.dsx1farendtotalcsss = YLeaf(YType.uint32, "dsx1FarEndTotalCSSs")

                self.dsx1farendtotaldms = YLeaf(YType.uint32, "dsx1FarEndTotalDMs")

                self.dsx1farendtotaless = YLeaf(YType.uint32, "dsx1FarEndTotalESs")

                self.dsx1farendtotalless = YLeaf(YType.uint32, "dsx1FarEndTotalLESs")

                self.dsx1farendtotalpcvs = YLeaf(YType.uint32, "dsx1FarEndTotalPCVs")

                self.dsx1farendtotalsefss = YLeaf(YType.uint32, "dsx1FarEndTotalSEFSs")

                self.dsx1farendtotalsess = YLeaf(YType.uint32, "dsx1FarEndTotalSESs")

                self.dsx1farendtotaluass = YLeaf(YType.uint32, "dsx1FarEndTotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1farendtotalindex",
                                "dsx1farendtotalbess",
                                "dsx1farendtotalcsss",
                                "dsx1farendtotaldms",
                                "dsx1farendtotaless",
                                "dsx1farendtotalless",
                                "dsx1farendtotalpcvs",
                                "dsx1farendtotalsefss",
                                "dsx1farendtotalsess",
                                "dsx1farendtotaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1farendtotalindex.is_set or
                    self.dsx1farendtotalbess.is_set or
                    self.dsx1farendtotalcsss.is_set or
                    self.dsx1farendtotaldms.is_set or
                    self.dsx1farendtotaless.is_set or
                    self.dsx1farendtotalless.is_set or
                    self.dsx1farendtotalpcvs.is_set or
                    self.dsx1farendtotalsefss.is_set or
                    self.dsx1farendtotalsess.is_set or
                    self.dsx1farendtotaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1farendtotalindex.yfilter != YFilter.not_set or
                    self.dsx1farendtotalbess.yfilter != YFilter.not_set or
                    self.dsx1farendtotalcsss.yfilter != YFilter.not_set or
                    self.dsx1farendtotaldms.yfilter != YFilter.not_set or
                    self.dsx1farendtotaless.yfilter != YFilter.not_set or
                    self.dsx1farendtotalless.yfilter != YFilter.not_set or
                    self.dsx1farendtotalpcvs.yfilter != YFilter.not_set or
                    self.dsx1farendtotalsefss.yfilter != YFilter.not_set or
                    self.dsx1farendtotalsess.yfilter != YFilter.not_set or
                    self.dsx1farendtotaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1FarEndTotalEntry" + "[dsx1FarEndTotalIndex='" + self.dsx1farendtotalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1FarEndTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1farendtotalindex.is_set or self.dsx1farendtotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalindex.get_name_leafdata())
                if (self.dsx1farendtotalbess.is_set or self.dsx1farendtotalbess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalbess.get_name_leafdata())
                if (self.dsx1farendtotalcsss.is_set or self.dsx1farendtotalcsss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalcsss.get_name_leafdata())
                if (self.dsx1farendtotaldms.is_set or self.dsx1farendtotaldms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotaldms.get_name_leafdata())
                if (self.dsx1farendtotaless.is_set or self.dsx1farendtotaless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotaless.get_name_leafdata())
                if (self.dsx1farendtotalless.is_set or self.dsx1farendtotalless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalless.get_name_leafdata())
                if (self.dsx1farendtotalpcvs.is_set or self.dsx1farendtotalpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalpcvs.get_name_leafdata())
                if (self.dsx1farendtotalsefss.is_set or self.dsx1farendtotalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalsefss.get_name_leafdata())
                if (self.dsx1farendtotalsess.is_set or self.dsx1farendtotalsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotalsess.get_name_leafdata())
                if (self.dsx1farendtotaluass.is_set or self.dsx1farendtotaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1farendtotaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1FarEndTotalIndex" or name == "dsx1FarEndTotalBESs" or name == "dsx1FarEndTotalCSSs" or name == "dsx1FarEndTotalDMs" or name == "dsx1FarEndTotalESs" or name == "dsx1FarEndTotalLESs" or name == "dsx1FarEndTotalPCVs" or name == "dsx1FarEndTotalSEFSs" or name == "dsx1FarEndTotalSESs" or name == "dsx1FarEndTotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1FarEndTotalIndex"):
                    self.dsx1farendtotalindex = value
                    self.dsx1farendtotalindex.value_namespace = name_space
                    self.dsx1farendtotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalBESs"):
                    self.dsx1farendtotalbess = value
                    self.dsx1farendtotalbess.value_namespace = name_space
                    self.dsx1farendtotalbess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalCSSs"):
                    self.dsx1farendtotalcsss = value
                    self.dsx1farendtotalcsss.value_namespace = name_space
                    self.dsx1farendtotalcsss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalDMs"):
                    self.dsx1farendtotaldms = value
                    self.dsx1farendtotaldms.value_namespace = name_space
                    self.dsx1farendtotaldms.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalESs"):
                    self.dsx1farendtotaless = value
                    self.dsx1farendtotaless.value_namespace = name_space
                    self.dsx1farendtotaless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalLESs"):
                    self.dsx1farendtotalless = value
                    self.dsx1farendtotalless.value_namespace = name_space
                    self.dsx1farendtotalless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalPCVs"):
                    self.dsx1farendtotalpcvs = value
                    self.dsx1farendtotalpcvs.value_namespace = name_space
                    self.dsx1farendtotalpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalSEFSs"):
                    self.dsx1farendtotalsefss = value
                    self.dsx1farendtotalsefss.value_namespace = name_space
                    self.dsx1farendtotalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalSESs"):
                    self.dsx1farendtotalsess = value
                    self.dsx1farendtotalsess.value_namespace = name_space
                    self.dsx1farendtotalsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FarEndTotalUASs"):
                    self.dsx1farendtotaluass = value
                    self.dsx1farendtotaluass.value_namespace = name_space
                    self.dsx1farendtotaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1farendtotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1farendtotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1FarEndTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1FarEndTotalEntry"):
                for c in self.dsx1farendtotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1farendtotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1FarEndTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Fractable(Entity):
        """
        This table is deprecated in favour of using
        ifStackTable.
        
        The table was mandatory for systems dividing a DS1
        into channels containing different data streams
        that are of local interest.  Systems which are
        indifferent to data content, such as CSUs, need
        not implement it.
        
        The DS1 fractional table identifies which DS1
        channels associated with a CSU are being used to
        support a logical interface, i.e., an entry in the
        interfaces table from the Internet\-standard MIB.
        
        For example, consider an application managing a
        North American ISDN Primary Rate link whose
        division is a 384 kbit/s H1 \_B\_ Channel for Video,
        a second H1 for data to a primary routing peer,
        and 12 64 kbit/s H0 \_B\_ Channels. Consider that
        some subset of the H0 channels are used for voice
        and the remainder are available for dynamic data
        calls.
        
        We count a total of 14 interfaces multiplexed onto
        the DS1 interface. Six DS1 channels (for the sake
        of the example, channels 1..6) are used for Video,
        six more (7..11 and 13) are used for data, and the
        remaining 12 are are in channels 12 and 14..24.
        
        Let us further imagine that ifIndex 2 is of type
        DS1 and refers to the DS1 interface, and that the
        interfaces layered onto it are numbered 3..16.
        
        We might describe the allocation of channels, in
        the dsx1FracTable, as follows\:
        dsx1FracIfIndex.2. 1 = 3  dsx1FracIfIndex.2.13 = 4
        dsx1FracIfIndex.2. 2 = 3  dsx1FracIfIndex.2.14 = 6
        dsx1FracIfIndex.2. 3 = 3  dsx1FracIfIndex.2.15 = 7
        dsx1FracIfIndex.2. 4 = 3  dsx1FracIfIndex.2.16 = 8
        dsx1FracIfIndex.2. 5 = 3  dsx1FracIfIndex.2.17 = 9
        dsx1FracIfIndex.2. 6 = 3  dsx1FracIfIndex.2.18 = 10
        dsx1FracIfIndex.2. 7 = 4  dsx1FracIfIndex.2.19 = 11
        dsx1FracIfIndex.2. 8 = 4  dsx1FracIfIndex.2.20 = 12
        dsx1FracIfIndex.2. 9 = 4  dsx1FracIfIndex.2.21 = 13
        dsx1FracIfIndex.2.10 = 4  dsx1FracIfIndex.2.22 = 14
        dsx1FracIfIndex.2.11 = 4  dsx1FracIfIndex.2.23 = 15
        dsx1FracIfIndex.2.12 = 5  dsx1FracIfIndex.2.24 = 16
        
        For North American (DS1) interfaces, there are 24
        legal channels, numbered 1 through 24.
        
        For G.704 interfaces, there are 31 legal channels,
        numbered 1 through 31.  The channels (1..31)
        correspond directly to the equivalently numbered
        time\-slots.
        
        .. attribute:: dsx1fracentry
        
        	An entry in the DS1 Fractional table
        	**type**\: list of    :py:class:`Dsx1Fracentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Fractable.Dsx1Fracentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Fractable, self).__init__()

            self.yang_name = "dsx1FracTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1fracentry = YList(self)

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
                        super(Ds1Mib.Dsx1Fractable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Fractable, self).__setattr__(name, value)


        class Dsx1Fracentry(Entity):
            """
            An entry in the DS1 Fractional table.
            
            .. attribute:: dsx1fracindex  <key>
            
            	The index value which uniquely identifies  the DS1  interface  to which this entry is applicable The interface identified by a  particular value  of  this  index is the same interface as identified by the same value  an  dsx1LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: dsx1fracnumber  <key>
            
            	The channel number for this entry
            	**type**\:  int
            
            	**range:** 1..31
            
            	**status**\: deprecated
            
            .. attribute:: dsx1fracifindex
            
            	An index value that uniquely identifies an interface.  The interface identified by a particular value of this index is the same  interface as  identified by the same value an ifIndex object instance. If no interface is currently using a channel, the value should be zero.  If a single interface occupies more  than  one  time slot,  that ifIndex value will be found in multiple time slots
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Fractable.Dsx1Fracentry, self).__init__()

                self.yang_name = "dsx1FracEntry"
                self.yang_parent_name = "dsx1FracTable"

                self.dsx1fracindex = YLeaf(YType.int32, "dsx1FracIndex")

                self.dsx1fracnumber = YLeaf(YType.int32, "dsx1FracNumber")

                self.dsx1fracifindex = YLeaf(YType.int32, "dsx1FracIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx1fracindex",
                                "dsx1fracnumber",
                                "dsx1fracifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Fractable.Dsx1Fracentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Fractable.Dsx1Fracentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx1fracindex.is_set or
                    self.dsx1fracnumber.is_set or
                    self.dsx1fracifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx1fracindex.yfilter != YFilter.not_set or
                    self.dsx1fracnumber.yfilter != YFilter.not_set or
                    self.dsx1fracifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1FracEntry" + "[dsx1FracIndex='" + self.dsx1fracindex.get() + "']" + "[dsx1FracNumber='" + self.dsx1fracnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1FracTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx1fracindex.is_set or self.dsx1fracindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1fracindex.get_name_leafdata())
                if (self.dsx1fracnumber.is_set or self.dsx1fracnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1fracnumber.get_name_leafdata())
                if (self.dsx1fracifindex.is_set or self.dsx1fracifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1fracifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx1FracIndex" or name == "dsx1FracNumber" or name == "dsx1FracIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx1FracIndex"):
                    self.dsx1fracindex = value
                    self.dsx1fracindex.value_namespace = name_space
                    self.dsx1fracindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FracNumber"):
                    self.dsx1fracnumber = value
                    self.dsx1fracnumber.value_namespace = name_space
                    self.dsx1fracnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1FracIfIndex"):
                    self.dsx1fracifindex = value
                    self.dsx1fracifindex.value_namespace = name_space
                    self.dsx1fracifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1fracentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1fracentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1FracTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1FracEntry"):
                for c in self.dsx1fracentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Fractable.Dsx1Fracentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1fracentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1FracEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx1Chanmappingtable(Entity):
        """
        The DS1 Channel Mapping table.  This table maps a
        DS1 channel number on a particular DS3 into an
        ifIndex.  In the presence of DS2s, this table can
        be used to map a DS2 channel number on a DS3 into
        an ifIndex, or used to map a DS1 channel number on
        a DS2 onto an ifIndex.
        
        .. attribute:: dsx1chanmappingentry
        
        	An entry in the DS1 Channel Mapping table.  There is an entry in this table corresponding to each ds1 ifEntry within any interface that is channelized to the individual ds1 ifEntry level.  This table is intended to facilitate mapping from channelized interface / channel number to DS1 ifEntry.  (e.g. mapping (DS3 ifIndex, DS1 Channel Number) \-> ifIndex)  While this table provides information that can also be found in the ifStackTable and dsx1ConfigTable, it provides this same information with a single table lookup, rather than by walking the ifStackTable to find the various constituent ds1 ifTable entries, and testing various dsx1ConfigTable entries to check for the entry with the applicable DS1 channel number
        	**type**\: list of    :py:class:`Dsx1Chanmappingentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds1Mib.Dsx1Chanmappingtable, self).__init__()

            self.yang_name = "dsx1ChanMappingTable"
            self.yang_parent_name = "DS1-MIB"

            self.dsx1chanmappingentry = YList(self)

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
                        super(Ds1Mib.Dsx1Chanmappingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds1Mib.Dsx1Chanmappingtable, self).__setattr__(name, value)


        class Dsx1Chanmappingentry(Entity):
            """
            An entry in the DS1 Channel Mapping table.  There
            is an entry in this table corresponding to each
            ds1 ifEntry within any interface that is
            channelized to the individual ds1 ifEntry level.
            
            This table is intended to facilitate mapping from
            channelized interface / channel number to DS1
            ifEntry.  (e.g. mapping (DS3 ifIndex, DS1 Channel
            Number) \-> ifIndex)
            
            While this table provides information that can
            also be found in the ifStackTable and
            dsx1ConfigTable, it provides this same information
            with a single table lookup, rather than by walking
            the ifStackTable to find the various constituent
            ds1 ifTable entries, and testing various
            dsx1ConfigTable entries to check for the entry
            with the applicable DS1 channel number.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: dsx1ds1channelnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..28
            
            	**refers to**\:  :py:class:`dsx1ds1channelnumber <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry>`
            
            .. attribute:: dsx1chanmappedifindex
            
            	This object indicates the ifIndex value assigned by the agent for the individual ds1 ifEntry that corresponds to the given DS1 channel number (specified by the INDEX element dsx1Ds1ChannelNumber) of the given channelized interface (specified by INDEX element ifIndex)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry, self).__init__()

                self.yang_name = "dsx1ChanMappingEntry"
                self.yang_parent_name = "dsx1ChanMappingTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.dsx1ds1channelnumber = YLeaf(YType.str, "dsx1Ds1ChannelNumber")

                self.dsx1chanmappedifindex = YLeaf(YType.int32, "dsx1ChanMappedIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "dsx1ds1channelnumber",
                                "dsx1chanmappedifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.dsx1ds1channelnumber.is_set or
                    self.dsx1chanmappedifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.dsx1ds1channelnumber.yfilter != YFilter.not_set or
                    self.dsx1chanmappedifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx1ChanMappingEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[dsx1Ds1ChannelNumber='" + self.dsx1ds1channelnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS1-MIB:DS1-MIB/dsx1ChanMappingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.dsx1ds1channelnumber.is_set or self.dsx1ds1channelnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1ds1channelnumber.get_name_leafdata())
                if (self.dsx1chanmappedifindex.is_set or self.dsx1chanmappedifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx1chanmappedifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "dsx1Ds1ChannelNumber" or name == "dsx1ChanMappedIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1Ds1ChannelNumber"):
                    self.dsx1ds1channelnumber = value
                    self.dsx1ds1channelnumber.value_namespace = name_space
                    self.dsx1ds1channelnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx1ChanMappedIfIndex"):
                    self.dsx1chanmappedifindex = value
                    self.dsx1chanmappedifindex.value_namespace = name_space
                    self.dsx1chanmappedifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx1chanmappingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx1chanmappingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx1ChanMappingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS1-MIB:DS1-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx1ChanMappingEntry"):
                for c in self.dsx1chanmappingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx1chanmappingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx1ChanMappingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dsx1chanmappingtable is not None and self.dsx1chanmappingtable.has_data()) or
            (self.dsx1configtable is not None and self.dsx1configtable.has_data()) or
            (self.dsx1currenttable is not None and self.dsx1currenttable.has_data()) or
            (self.dsx1farendcurrenttable is not None and self.dsx1farendcurrenttable.has_data()) or
            (self.dsx1farendintervaltable is not None and self.dsx1farendintervaltable.has_data()) or
            (self.dsx1farendtotaltable is not None and self.dsx1farendtotaltable.has_data()) or
            (self.dsx1fractable is not None and self.dsx1fractable.has_data()) or
            (self.dsx1intervaltable is not None and self.dsx1intervaltable.has_data()) or
            (self.dsx1totaltable is not None and self.dsx1totaltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dsx1chanmappingtable is not None and self.dsx1chanmappingtable.has_operation()) or
            (self.dsx1configtable is not None and self.dsx1configtable.has_operation()) or
            (self.dsx1currenttable is not None and self.dsx1currenttable.has_operation()) or
            (self.dsx1farendcurrenttable is not None and self.dsx1farendcurrenttable.has_operation()) or
            (self.dsx1farendintervaltable is not None and self.dsx1farendintervaltable.has_operation()) or
            (self.dsx1farendtotaltable is not None and self.dsx1farendtotaltable.has_operation()) or
            (self.dsx1fractable is not None and self.dsx1fractable.has_operation()) or
            (self.dsx1intervaltable is not None and self.dsx1intervaltable.has_operation()) or
            (self.dsx1totaltable is not None and self.dsx1totaltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "DS1-MIB:DS1-MIB" + path_buffer

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

        if (child_yang_name == "dsx1ChanMappingTable"):
            if (self.dsx1chanmappingtable is None):
                self.dsx1chanmappingtable = Ds1Mib.Dsx1Chanmappingtable()
                self.dsx1chanmappingtable.parent = self
                self._children_name_map["dsx1chanmappingtable"] = "dsx1ChanMappingTable"
            return self.dsx1chanmappingtable

        if (child_yang_name == "dsx1ConfigTable"):
            if (self.dsx1configtable is None):
                self.dsx1configtable = Ds1Mib.Dsx1Configtable()
                self.dsx1configtable.parent = self
                self._children_name_map["dsx1configtable"] = "dsx1ConfigTable"
            return self.dsx1configtable

        if (child_yang_name == "dsx1CurrentTable"):
            if (self.dsx1currenttable is None):
                self.dsx1currenttable = Ds1Mib.Dsx1Currenttable()
                self.dsx1currenttable.parent = self
                self._children_name_map["dsx1currenttable"] = "dsx1CurrentTable"
            return self.dsx1currenttable

        if (child_yang_name == "dsx1FarEndCurrentTable"):
            if (self.dsx1farendcurrenttable is None):
                self.dsx1farendcurrenttable = Ds1Mib.Dsx1Farendcurrenttable()
                self.dsx1farendcurrenttable.parent = self
                self._children_name_map["dsx1farendcurrenttable"] = "dsx1FarEndCurrentTable"
            return self.dsx1farendcurrenttable

        if (child_yang_name == "dsx1FarEndIntervalTable"):
            if (self.dsx1farendintervaltable is None):
                self.dsx1farendintervaltable = Ds1Mib.Dsx1Farendintervaltable()
                self.dsx1farendintervaltable.parent = self
                self._children_name_map["dsx1farendintervaltable"] = "dsx1FarEndIntervalTable"
            return self.dsx1farendintervaltable

        if (child_yang_name == "dsx1FarEndTotalTable"):
            if (self.dsx1farendtotaltable is None):
                self.dsx1farendtotaltable = Ds1Mib.Dsx1Farendtotaltable()
                self.dsx1farendtotaltable.parent = self
                self._children_name_map["dsx1farendtotaltable"] = "dsx1FarEndTotalTable"
            return self.dsx1farendtotaltable

        if (child_yang_name == "dsx1FracTable"):
            if (self.dsx1fractable is None):
                self.dsx1fractable = Ds1Mib.Dsx1Fractable()
                self.dsx1fractable.parent = self
                self._children_name_map["dsx1fractable"] = "dsx1FracTable"
            return self.dsx1fractable

        if (child_yang_name == "dsx1IntervalTable"):
            if (self.dsx1intervaltable is None):
                self.dsx1intervaltable = Ds1Mib.Dsx1Intervaltable()
                self.dsx1intervaltable.parent = self
                self._children_name_map["dsx1intervaltable"] = "dsx1IntervalTable"
            return self.dsx1intervaltable

        if (child_yang_name == "dsx1TotalTable"):
            if (self.dsx1totaltable is None):
                self.dsx1totaltable = Ds1Mib.Dsx1Totaltable()
                self.dsx1totaltable.parent = self
                self._children_name_map["dsx1totaltable"] = "dsx1TotalTable"
            return self.dsx1totaltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dsx1ChanMappingTable" or name == "dsx1ConfigTable" or name == "dsx1CurrentTable" or name == "dsx1FarEndCurrentTable" or name == "dsx1FarEndIntervalTable" or name == "dsx1FarEndTotalTable" or name == "dsx1FracTable" or name == "dsx1IntervalTable" or name == "dsx1TotalTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ds1Mib()
        return self._top_entity

