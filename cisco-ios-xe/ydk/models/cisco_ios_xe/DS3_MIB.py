""" DS3_MIB 

The is the MIB module that describes
DS3 and E3 interfaces objects.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ds3Mib(Entity):
    """
    
    
    .. attribute:: dsx3configtable
    
    	The DS3/E3 Configuration table
    	**type**\:   :py:class:`Dsx3Configtable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable>`
    
    .. attribute:: dsx3currenttable
    
    	The DS3/E3 current table contains various statistics being collected for the current 15 minute interval
    	**type**\:   :py:class:`Dsx3Currenttable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Currenttable>`
    
    .. attribute:: dsx3farendconfigtable
    
    	The DS3 Far End Configuration Table contains configuration information reported in the C\-bits from the remote end
    	**type**\:   :py:class:`Dsx3Farendconfigtable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendconfigtable>`
    
    .. attribute:: dsx3farendcurrenttable
    
    	The DS3 Far End Current table contains various statistics being collected for the current 15 minute interval.  The statistics are collected from the far end block error code within the C\- bits
    	**type**\:   :py:class:`Dsx3Farendcurrenttable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendcurrenttable>`
    
    .. attribute:: dsx3farendintervaltable
    
    	The DS3 Far End Interval Table contains various statistics collected by each DS3 interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals
    	**type**\:   :py:class:`Dsx3Farendintervaltable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendintervaltable>`
    
    .. attribute:: dsx3farendtotaltable
    
    	The DS3 Far End Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\:   :py:class:`Dsx3Farendtotaltable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendtotaltable>`
    
    .. attribute:: dsx3fractable
    
    	This table is deprecated in favour of using ifStackTable.  Implementation of this table was optional.  It was designed for those systems dividing a DS3/E3 into channels containing different data streams that are of local interest.  The DS3/E3 fractional table identifies which DS3/E3 channels associated with a CSU are being used to support a logical interface, i.e., an entry in the interfaces table from the Internet\- standard MIB.  For example, consider a DS3 device with 4 high speed links carrying router traffic, a feed for voice, a feed for video, and a synchronous channel for a non\-routed protocol.  We might describe the allocation of channels, in the dsx3FracTable, as follows\: dsx3FracIfIndex.2. 1 = 3  dsx3FracIfIndex.2.15 = 4 dsx3FracIfIndex.2. 2 = 3  dsx3FracIfIndex.2.16 = 6 dsx3FracIfIndex.2. 3 = 3  dsx3FracIfIndex.2.17 = 6 dsx3FracIfIndex.2. 4 = 3  dsx3FracIfIndex.2.18 = 6 dsx3FracIfIndex.2. 5 = 3  dsx3FracIfIndex.2.19 = 6 dsx3FracIfIndex.2. 6 = 3  dsx3FracIfIndex.2.20 = 6 dsx3FracIfIndex.2. 7 = 4  dsx3FracIfIndex.2.21 = 6 dsx3FracIfIndex.2. 8 = 4  dsx3FracIfIndex.2.22 = 6 dsx3FracIfIndex.2. 9 = 4  dsx3FracIfIndex.2.23 = 6 dsx3FracIfIndex.2.10 = 4  dsx3FracIfIndex.2.24 = 6 dsx3FracIfIndex.2.11 = 4  dsx3FracIfIndex.2.25 = 6 dsx3FracIfIndex.2.12 = 5  dsx3FracIfIndex.2.26 = 6 dsx3FracIfIndex.2.13 = 5  dsx3FracIfIndex.2.27 = 6 dsx3FracIfIndex.2.14 = 5  dsx3FracIfIndex.2.28 = 6 For dsx3M23, dsx3 SYNTRAN, dsx3CbitParity, and dsx3ClearChannel  there are 28 legal channels, numbered 1 throug h 28.  For e3Framed there are 16 legal channels, numbered 1 through 16.  The channels (1..16) correspond directly to the equivalently numbered time\-slots
    	**type**\:   :py:class:`Dsx3Fractable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Fractable>`
    
    	**status**\: deprecated
    
    .. attribute:: dsx3intervaltable
    
    	The DS3/E3 Interval Table contains various statistics collected by each DS3/E3 Interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals.  Each row in this table represents one such interval (identified by dsx3IntervalNumber) and for one specific interface (identifed by dsx3IntervalIndex)
    	**type**\:   :py:class:`Dsx3Intervaltable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Intervaltable>`
    
    .. attribute:: dsx3totaltable
    
    	The DS3/E3 Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\:   :py:class:`Dsx3Totaltable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Totaltable>`
    
    

    """

    _prefix = 'DS3-MIB'
    _revision = '1998-08-01'

    def __init__(self):
        super(Ds3Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "DS3-MIB"
        self.yang_parent_name = "DS3-MIB"

        self.dsx3configtable = Ds3Mib.Dsx3Configtable()
        self.dsx3configtable.parent = self
        self._children_name_map["dsx3configtable"] = "dsx3ConfigTable"
        self._children_yang_names.add("dsx3ConfigTable")

        self.dsx3currenttable = Ds3Mib.Dsx3Currenttable()
        self.dsx3currenttable.parent = self
        self._children_name_map["dsx3currenttable"] = "dsx3CurrentTable"
        self._children_yang_names.add("dsx3CurrentTable")

        self.dsx3farendconfigtable = Ds3Mib.Dsx3Farendconfigtable()
        self.dsx3farendconfigtable.parent = self
        self._children_name_map["dsx3farendconfigtable"] = "dsx3FarEndConfigTable"
        self._children_yang_names.add("dsx3FarEndConfigTable")

        self.dsx3farendcurrenttable = Ds3Mib.Dsx3Farendcurrenttable()
        self.dsx3farendcurrenttable.parent = self
        self._children_name_map["dsx3farendcurrenttable"] = "dsx3FarEndCurrentTable"
        self._children_yang_names.add("dsx3FarEndCurrentTable")

        self.dsx3farendintervaltable = Ds3Mib.Dsx3Farendintervaltable()
        self.dsx3farendintervaltable.parent = self
        self._children_name_map["dsx3farendintervaltable"] = "dsx3FarEndIntervalTable"
        self._children_yang_names.add("dsx3FarEndIntervalTable")

        self.dsx3farendtotaltable = Ds3Mib.Dsx3Farendtotaltable()
        self.dsx3farendtotaltable.parent = self
        self._children_name_map["dsx3farendtotaltable"] = "dsx3FarEndTotalTable"
        self._children_yang_names.add("dsx3FarEndTotalTable")

        self.dsx3fractable = Ds3Mib.Dsx3Fractable()
        self.dsx3fractable.parent = self
        self._children_name_map["dsx3fractable"] = "dsx3FracTable"
        self._children_yang_names.add("dsx3FracTable")

        self.dsx3intervaltable = Ds3Mib.Dsx3Intervaltable()
        self.dsx3intervaltable.parent = self
        self._children_name_map["dsx3intervaltable"] = "dsx3IntervalTable"
        self._children_yang_names.add("dsx3IntervalTable")

        self.dsx3totaltable = Ds3Mib.Dsx3Totaltable()
        self.dsx3totaltable.parent = self
        self._children_name_map["dsx3totaltable"] = "dsx3TotalTable"
        self._children_yang_names.add("dsx3TotalTable")


    class Dsx3Configtable(Entity):
        """
        The DS3/E3 Configuration table.
        
        .. attribute:: dsx3configentry
        
        	An entry in the DS3/E3 Configuration table
        	**type**\: list of    :py:class:`Dsx3Configentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Configtable, self).__init__()

            self.yang_name = "dsx3ConfigTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3configentry = YList(self)

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
                        super(Ds3Mib.Dsx3Configtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Configtable, self).__setattr__(name, value)


        class Dsx3Configentry(Entity):
            """
            An entry in the DS3/E3 Configuration table.
            
            .. attribute:: dsx3lineindex  <key>
            
            	This object should be made equal to ifIndex.  The next paragraph describes its previous usage. Making the object equal to ifIndex allows propoer use of ifStackTable.  Previously, this object was the identifier of a DS3/E3 Interface on a managed device.  If there is an ifEntry that is directly associated with this and only this DS3/E3 interface, it should have the same value as ifIndex.  Otherwise, number the dsx3LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3channelization
            
            	Indicates whether this ds3/e3 is channelized or unchannelized.  The value of enabledDs1 indicates that this is a DS3 channelized into DS1s.  The value of enabledDs3 indicated that this is a DS3 channelized into DS2s.  Setting this object will cause the creation or deletion of DS2 or DS1 entries in the ifTable.  
            	**type**\:   :py:class:`Dsx3Channelization <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Channelization>`
            
            .. attribute:: dsx3circuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: dsx3ds1forremoteloop
            
            	Indicates which ds1/e1 on this ds3/e3 will be indicated in the remote ds1 loopback request.  A value of 0 means no DS1 will be looped.  A value of 29 means all ds1s/e1s will be looped
            	**type**\:  int
            
            	**range:** 0..29
            
            .. attribute:: dsx3ifindex
            
            	This value for this object is equal to the value of ifIndex from the Interfaces table of MIB II (RFC 1213)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: dsx3invalidintervals
            
            	The number of intervals in the range from 0 to dsx3ValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\:  int
            
            	**range:** 0..96
            
            .. attribute:: dsx3linecoding
            
            	This variable describes the variety of Zero Code Suppression used on this interface, which in turn affects a number of its characteristics.  dsx3B3ZS and e3HDB3 refer to the use of specified patterns of normal bits and bipolar violations which are used to replace sequences of zero bits of a specified length
            	**type**\:   :py:class:`Dsx3Linecoding <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Linecoding>`
            
            .. attribute:: dsx3linelength
            
            	The length of the ds3 line in meters.  This object provides information for line build out circuitry if it exists and can use this object to adjust the line build out
            	**type**\:  int
            
            	**range:** 0..64000
            
            	**units**\: meters
            
            .. attribute:: dsx3linestatus
            
            	This variable indicates the Line Status of the interface.  It contains loopback state information and failure state information.  The dsx3LineStatus is a bit map represented as a sum, therefore, it can represent multiple failures and a loopback (see dsx3LoopbackConfig object for the type of loopback) simultaneously.  The dsx3NoAlarm must be set if and only if no other flag is set.  If the dsx3loopbackState bit is set, the loopback in effect can be determined from the dsx3loopbackConfig object. The various bit positions are\: 1     dsx3NoAlarm         No alarm present 2     dsx3RcvRAIFailure   Receiving Yellow/Remote                  Alarm Indication 4     dsx3XmitRAIAlarm    Transmitting Yellow/Remote                  Alarm Indication 8     dsx3RcvAIS          Receiving AIS failure state 16     dsx3XmitAIS         Transmitting AIS 32     dsx3LOF             Receiving LOF failure state 64     dsx3LOS             Receiving LOS failure state 128     dsx3LoopbackState   Looping the received signal 256     dsx3RcvTestCode     Receiving a Test Pattern 512     dsx3OtherFailure    any line status not defined                  here 1024     dsx3UnavailSigState Near End in Unavailable Signal                  State 2048     dsx3NetEquipOOS     Carrier Equipment Out of Service
            	**type**\:  int
            
            	**range:** 1..4095
            
            .. attribute:: dsx3linestatuschangetrapenable
            
            	Indicates whether dsx3LineStatusChange traps should be generated for this interface
            	**type**\:   :py:class:`Dsx3Linestatuschangetrapenable <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Linestatuschangetrapenable>`
            
            .. attribute:: dsx3linestatuslastchange
            
            	The value of MIB II's sysUpTime object at the time this DS3/E3 entered its current line status state.  If the current state was entered prior to the last re\-initialization of the proxy\-agent, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3linetype
            
            	This variable indicates the variety of DS3 C\-bit or E3 application implementing this interface. The type of interface affects the interpretation of the usage and error statistics.  The rate of DS3 is 44.736 Mbps and E3 is 34.368 Mbps.  The dsx3ClearChannel value means that the C\-bits are not used except for sending/receiving AIS. The values, in sequence, describe\:  TITLE\:            SPECIFICATION\: dsx3M23            ANSI T1.107\-1988 [9] dsx3SYNTRAN        ANSI T1.107\-1988 [9] dsx3CbitParity     ANSI T1.107a\-1990 [9a] dsx3ClearChannel   ANSI T1.102\-1987 [8] e3Framed           CCITT G.751 [12] e3Plcp             ETSI T/NA(91)18 [13]
            	**type**\:   :py:class:`Dsx3Linetype <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Linetype>`
            
            .. attribute:: dsx3loopbackconfig
            
            	This variable represents the desired loopback configuration of the DS3/E3 interface.  The values mean\:  dsx3NoLoop   Not in the loopback state.  A device that is   not capable of performing a loopback on   the interface shall always return this as   its value.  dsx3PayloadLoop   The received signal at this interface is looped   through the device.  Typically the received signal   is looped back for retransmission after it has   passed through the device's framing function.  dsx3LineLoop   The received signal at this interface does not   go through the device (minimum penetration) but   is looped back out.  dsx3OtherLoop   Loopbacks that are not defined here.  dsx3InwardLoop   The sent signal at this interface is looped back   through the device.  dsx3DualLoop   Both dsx1LineLoop and dsx1InwardLoop will be   active simultaneously
            	**type**\:   :py:class:`Dsx3Loopbackconfig <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Loopbackconfig>`
            
            .. attribute:: dsx3loopbackstatus
            
            	This variable represents the current state of the loopback on the DS3 interface.  It contains information about loopbacks established by a manager and remotely from the far end.  The dsx3LoopbackStatus is a bit map represented as a sum, therefore is can represent multiple loopbacks simultaneously.  The various bit positions are\:  1  dsx3NoLoopback  2  dsx3NearEndPayloadLoopback  4  dsx3NearEndLineLoopback  8  dsx3NearEndOtherLoopback 16  dsx3NearEndInwardLoopback 32  dsx3FarEndPayloadLoopback 64  dsx3FarEndLineLoopback
            	**type**\:  int
            
            	**range:** 1..127
            
            .. attribute:: dsx3sendcode
            
            	This variable indicates what type of code is being sent across the DS3/E3 interface by the device.  (These are optional for E3 interfaces.) Setting this variable causes the interface to begin sending the code requested. The values mean\:     dsx3SendNoCode        sending looped or normal data     dsx3SendLineCode        sending a request for a line loopback     dsx3SendPayloadCode        sending a request for a payload loopback        (i.e., all DS1/E1s in a DS3/E3 frame)     dsx3SendResetCode        sending a loopback deactivation request     dsx3SendDS1LoopCode        requesting to loopback a particular DS1/E1        within a DS3/E3 frame.  The DS1/E1 is        indicated in dsx3Ds1ForRemoteLoop.     dsx3SendTestPattern        sending a test pattern
            	**type**\:   :py:class:`Dsx3Sendcode <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Sendcode>`
            
            .. attribute:: dsx3timeelapsed
            
            	The number of seconds that have elapsed since the beginning of the near end current error\- measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            .. attribute:: dsx3transmitclocksource
            
            	The source of Transmit Clock.  loopTiming indicates that the recovered receive clock is used as the transmit clock.  localTiming indicates that a local clock source is used or that an external clock is attached to the box containing the interface.  throughTiming indicates that transmit clock is derived from the recovered receive clock of another DS3 interface
            	**type**\:   :py:class:`Dsx3Transmitclocksource <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3Transmitclocksource>`
            
            .. attribute:: dsx3validintervals
            
            	The number of previous near end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute near end intervals since the interface has been online.  In the case where the agent is a proxy, it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Configtable.Dsx3Configentry, self).__init__()

                self.yang_name = "dsx3ConfigEntry"
                self.yang_parent_name = "dsx3ConfigTable"

                self.dsx3lineindex = YLeaf(YType.int32, "dsx3LineIndex")

                self.dsx3channelization = YLeaf(YType.enumeration, "dsx3Channelization")

                self.dsx3circuitidentifier = YLeaf(YType.str, "dsx3CircuitIdentifier")

                self.dsx3ds1forremoteloop = YLeaf(YType.int32, "dsx3Ds1ForRemoteLoop")

                self.dsx3ifindex = YLeaf(YType.int32, "dsx3IfIndex")

                self.dsx3invalidintervals = YLeaf(YType.int32, "dsx3InvalidIntervals")

                self.dsx3linecoding = YLeaf(YType.enumeration, "dsx3LineCoding")

                self.dsx3linelength = YLeaf(YType.int32, "dsx3LineLength")

                self.dsx3linestatus = YLeaf(YType.int32, "dsx3LineStatus")

                self.dsx3linestatuschangetrapenable = YLeaf(YType.enumeration, "dsx3LineStatusChangeTrapEnable")

                self.dsx3linestatuslastchange = YLeaf(YType.uint32, "dsx3LineStatusLastChange")

                self.dsx3linetype = YLeaf(YType.enumeration, "dsx3LineType")

                self.dsx3loopbackconfig = YLeaf(YType.enumeration, "dsx3LoopbackConfig")

                self.dsx3loopbackstatus = YLeaf(YType.int32, "dsx3LoopbackStatus")

                self.dsx3sendcode = YLeaf(YType.enumeration, "dsx3SendCode")

                self.dsx3timeelapsed = YLeaf(YType.int32, "dsx3TimeElapsed")

                self.dsx3transmitclocksource = YLeaf(YType.enumeration, "dsx3TransmitClockSource")

                self.dsx3validintervals = YLeaf(YType.int32, "dsx3ValidIntervals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3lineindex",
                                "dsx3channelization",
                                "dsx3circuitidentifier",
                                "dsx3ds1forremoteloop",
                                "dsx3ifindex",
                                "dsx3invalidintervals",
                                "dsx3linecoding",
                                "dsx3linelength",
                                "dsx3linestatus",
                                "dsx3linestatuschangetrapenable",
                                "dsx3linestatuslastchange",
                                "dsx3linetype",
                                "dsx3loopbackconfig",
                                "dsx3loopbackstatus",
                                "dsx3sendcode",
                                "dsx3timeelapsed",
                                "dsx3transmitclocksource",
                                "dsx3validintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Configtable.Dsx3Configentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Configtable.Dsx3Configentry, self).__setattr__(name, value)

            class Dsx3Channelization(Enum):
                """
                Dsx3Channelization

                Indicates whether this ds3/e3 is channelized or

                unchannelized.  The value of enabledDs1 indicates

                that this is a DS3 channelized into DS1s.  The

                value of enabledDs3 indicated that this is a DS3

                channelized into DS2s.  Setting this object will

                cause the creation or deletion of DS2 or DS1

                entries in the ifTable.  

                .. data:: disabled = 1

                .. data:: enabledDs1 = 2

                .. data:: enabledDs2 = 3

                """

                disabled = Enum.YLeaf(1, "disabled")

                enabledDs1 = Enum.YLeaf(2, "enabledDs1")

                enabledDs2 = Enum.YLeaf(3, "enabledDs2")


            class Dsx3Linecoding(Enum):
                """
                Dsx3Linecoding

                This variable describes the variety of Zero Code

                Suppression used on this interface, which in turn

                affects a number of its characteristics.

                dsx3B3ZS and e3HDB3 refer to the use of specified

                patterns of normal bits and bipolar violations

                which are used to replace sequences of zero bits

                of a specified length.

                .. data:: dsx3Other = 1

                .. data:: dsx3B3ZS = 2

                .. data:: e3HDB3 = 3

                """

                dsx3Other = Enum.YLeaf(1, "dsx3Other")

                dsx3B3ZS = Enum.YLeaf(2, "dsx3B3ZS")

                e3HDB3 = Enum.YLeaf(3, "e3HDB3")


            class Dsx3Linestatuschangetrapenable(Enum):
                """
                Dsx3Linestatuschangetrapenable

                Indicates whether dsx3LineStatusChange traps

                should be generated for this interface.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Dsx3Linetype(Enum):
                """
                Dsx3Linetype

                This variable indicates the variety of DS3 C\-bit

                or E3 application implementing this interface. The

                type of interface affects the interpretation of

                the usage and error statistics.  The rate of DS3

                is 44.736 Mbps and E3 is 34.368 Mbps.  The

                dsx3ClearChannel value means that the C\-bits are

                not used except for sending/receiving AIS.

                The values, in sequence, describe\:

                TITLE\:            SPECIFICATION\:

                dsx3M23            ANSI T1.107\-1988 [9]

                dsx3SYNTRAN        ANSI T1.107\-1988 [9]

                dsx3CbitParity     ANSI T1.107a\-1990 [9a]

                dsx3ClearChannel   ANSI T1.102\-1987 [8]

                e3Framed           CCITT G.751 [12]

                e3Plcp             ETSI T/NA(91)18 [13].

                .. data:: dsx3other = 1

                .. data:: dsx3M23 = 2

                .. data:: dsx3SYNTRAN = 3

                .. data:: dsx3CbitParity = 4

                .. data:: dsx3ClearChannel = 5

                .. data:: e3other = 6

                .. data:: e3Framed = 7

                .. data:: e3Plcp = 8

                """

                dsx3other = Enum.YLeaf(1, "dsx3other")

                dsx3M23 = Enum.YLeaf(2, "dsx3M23")

                dsx3SYNTRAN = Enum.YLeaf(3, "dsx3SYNTRAN")

                dsx3CbitParity = Enum.YLeaf(4, "dsx3CbitParity")

                dsx3ClearChannel = Enum.YLeaf(5, "dsx3ClearChannel")

                e3other = Enum.YLeaf(6, "e3other")

                e3Framed = Enum.YLeaf(7, "e3Framed")

                e3Plcp = Enum.YLeaf(8, "e3Plcp")


            class Dsx3Loopbackconfig(Enum):
                """
                Dsx3Loopbackconfig

                This variable represents the desired loopback

                configuration of the DS3/E3 interface.

                The values mean\:

                dsx3NoLoop

                  Not in the loopback state.  A device that is

                  not capable of performing a loopback on

                  the interface shall always return this as

                  its value.

                dsx3PayloadLoop

                  The received signal at this interface is looped

                  through the device.  Typically the received signal

                  is looped back for retransmission after it has

                  passed through the device's framing function.

                dsx3LineLoop

                  The received signal at this interface does not

                  go through the device (minimum penetration) but

                  is looped back out.

                dsx3OtherLoop

                  Loopbacks that are not defined here.

                dsx3InwardLoop

                  The sent signal at this interface is looped back

                  through the device.

                dsx3DualLoop

                  Both dsx1LineLoop and dsx1InwardLoop will be

                  active simultaneously.

                .. data:: dsx3NoLoop = 1

                .. data:: dsx3PayloadLoop = 2

                .. data:: dsx3LineLoop = 3

                .. data:: dsx3OtherLoop = 4

                .. data:: dsx3InwardLoop = 5

                .. data:: dsx3DualLoop = 6

                """

                dsx3NoLoop = Enum.YLeaf(1, "dsx3NoLoop")

                dsx3PayloadLoop = Enum.YLeaf(2, "dsx3PayloadLoop")

                dsx3LineLoop = Enum.YLeaf(3, "dsx3LineLoop")

                dsx3OtherLoop = Enum.YLeaf(4, "dsx3OtherLoop")

                dsx3InwardLoop = Enum.YLeaf(5, "dsx3InwardLoop")

                dsx3DualLoop = Enum.YLeaf(6, "dsx3DualLoop")


            class Dsx3Sendcode(Enum):
                """
                Dsx3Sendcode

                This variable indicates what type of code is

                being sent across the DS3/E3 interface by the

                device.  (These are optional for E3 interfaces.)

                Setting this variable causes the interface to

                begin sending the code requested.

                The values mean\:

                   dsx3SendNoCode

                       sending looped or normal data

                   dsx3SendLineCode

                       sending a request for a line loopback

                   dsx3SendPayloadCode

                       sending a request for a payload loopback

                       (i.e., all DS1/E1s in a DS3/E3 frame)

                   dsx3SendResetCode

                       sending a loopback deactivation request

                   dsx3SendDS1LoopCode

                       requesting to loopback a particular DS1/E1

                       within a DS3/E3 frame.  The DS1/E1 is

                       indicated in dsx3Ds1ForRemoteLoop.

                   dsx3SendTestPattern

                       sending a test pattern.

                .. data:: dsx3SendNoCode = 1

                .. data:: dsx3SendLineCode = 2

                .. data:: dsx3SendPayloadCode = 3

                .. data:: dsx3SendResetCode = 4

                .. data:: dsx3SendDS1LoopCode = 5

                .. data:: dsx3SendTestPattern = 6

                """

                dsx3SendNoCode = Enum.YLeaf(1, "dsx3SendNoCode")

                dsx3SendLineCode = Enum.YLeaf(2, "dsx3SendLineCode")

                dsx3SendPayloadCode = Enum.YLeaf(3, "dsx3SendPayloadCode")

                dsx3SendResetCode = Enum.YLeaf(4, "dsx3SendResetCode")

                dsx3SendDS1LoopCode = Enum.YLeaf(5, "dsx3SendDS1LoopCode")

                dsx3SendTestPattern = Enum.YLeaf(6, "dsx3SendTestPattern")


            class Dsx3Transmitclocksource(Enum):
                """
                Dsx3Transmitclocksource

                The source of Transmit Clock.

                loopTiming indicates that the recovered receive clock

                is used as the transmit clock.

                localTiming indicates that a local clock source is used

                or that an external clock is attached to the box

                containing the interface.

                throughTiming indicates that transmit clock is derived

                from the recovered receive clock of another DS3

                interface.

                .. data:: loopTiming = 1

                .. data:: localTiming = 2

                .. data:: throughTiming = 3

                """

                loopTiming = Enum.YLeaf(1, "loopTiming")

                localTiming = Enum.YLeaf(2, "localTiming")

                throughTiming = Enum.YLeaf(3, "throughTiming")


            def has_data(self):
                return (
                    self.dsx3lineindex.is_set or
                    self.dsx3channelization.is_set or
                    self.dsx3circuitidentifier.is_set or
                    self.dsx3ds1forremoteloop.is_set or
                    self.dsx3ifindex.is_set or
                    self.dsx3invalidintervals.is_set or
                    self.dsx3linecoding.is_set or
                    self.dsx3linelength.is_set or
                    self.dsx3linestatus.is_set or
                    self.dsx3linestatuschangetrapenable.is_set or
                    self.dsx3linestatuslastchange.is_set or
                    self.dsx3linetype.is_set or
                    self.dsx3loopbackconfig.is_set or
                    self.dsx3loopbackstatus.is_set or
                    self.dsx3sendcode.is_set or
                    self.dsx3timeelapsed.is_set or
                    self.dsx3transmitclocksource.is_set or
                    self.dsx3validintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3lineindex.yfilter != YFilter.not_set or
                    self.dsx3channelization.yfilter != YFilter.not_set or
                    self.dsx3circuitidentifier.yfilter != YFilter.not_set or
                    self.dsx3ds1forremoteloop.yfilter != YFilter.not_set or
                    self.dsx3ifindex.yfilter != YFilter.not_set or
                    self.dsx3invalidintervals.yfilter != YFilter.not_set or
                    self.dsx3linecoding.yfilter != YFilter.not_set or
                    self.dsx3linelength.yfilter != YFilter.not_set or
                    self.dsx3linestatus.yfilter != YFilter.not_set or
                    self.dsx3linestatuschangetrapenable.yfilter != YFilter.not_set or
                    self.dsx3linestatuslastchange.yfilter != YFilter.not_set or
                    self.dsx3linetype.yfilter != YFilter.not_set or
                    self.dsx3loopbackconfig.yfilter != YFilter.not_set or
                    self.dsx3loopbackstatus.yfilter != YFilter.not_set or
                    self.dsx3sendcode.yfilter != YFilter.not_set or
                    self.dsx3timeelapsed.yfilter != YFilter.not_set or
                    self.dsx3transmitclocksource.yfilter != YFilter.not_set or
                    self.dsx3validintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3ConfigEntry" + "[dsx3LineIndex='" + self.dsx3lineindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3ConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3lineindex.is_set or self.dsx3lineindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3lineindex.get_name_leafdata())
                if (self.dsx3channelization.is_set or self.dsx3channelization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3channelization.get_name_leafdata())
                if (self.dsx3circuitidentifier.is_set or self.dsx3circuitidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3circuitidentifier.get_name_leafdata())
                if (self.dsx3ds1forremoteloop.is_set or self.dsx3ds1forremoteloop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3ds1forremoteloop.get_name_leafdata())
                if (self.dsx3ifindex.is_set or self.dsx3ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3ifindex.get_name_leafdata())
                if (self.dsx3invalidintervals.is_set or self.dsx3invalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3invalidintervals.get_name_leafdata())
                if (self.dsx3linecoding.is_set or self.dsx3linecoding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3linecoding.get_name_leafdata())
                if (self.dsx3linelength.is_set or self.dsx3linelength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3linelength.get_name_leafdata())
                if (self.dsx3linestatus.is_set or self.dsx3linestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3linestatus.get_name_leafdata())
                if (self.dsx3linestatuschangetrapenable.is_set or self.dsx3linestatuschangetrapenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3linestatuschangetrapenable.get_name_leafdata())
                if (self.dsx3linestatuslastchange.is_set or self.dsx3linestatuslastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3linestatuslastchange.get_name_leafdata())
                if (self.dsx3linetype.is_set or self.dsx3linetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3linetype.get_name_leafdata())
                if (self.dsx3loopbackconfig.is_set or self.dsx3loopbackconfig.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3loopbackconfig.get_name_leafdata())
                if (self.dsx3loopbackstatus.is_set or self.dsx3loopbackstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3loopbackstatus.get_name_leafdata())
                if (self.dsx3sendcode.is_set or self.dsx3sendcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3sendcode.get_name_leafdata())
                if (self.dsx3timeelapsed.is_set or self.dsx3timeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3timeelapsed.get_name_leafdata())
                if (self.dsx3transmitclocksource.is_set or self.dsx3transmitclocksource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3transmitclocksource.get_name_leafdata())
                if (self.dsx3validintervals.is_set or self.dsx3validintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3validintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3LineIndex" or name == "dsx3Channelization" or name == "dsx3CircuitIdentifier" or name == "dsx3Ds1ForRemoteLoop" or name == "dsx3IfIndex" or name == "dsx3InvalidIntervals" or name == "dsx3LineCoding" or name == "dsx3LineLength" or name == "dsx3LineStatus" or name == "dsx3LineStatusChangeTrapEnable" or name == "dsx3LineStatusLastChange" or name == "dsx3LineType" or name == "dsx3LoopbackConfig" or name == "dsx3LoopbackStatus" or name == "dsx3SendCode" or name == "dsx3TimeElapsed" or name == "dsx3TransmitClockSource" or name == "dsx3ValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3LineIndex"):
                    self.dsx3lineindex = value
                    self.dsx3lineindex.value_namespace = name_space
                    self.dsx3lineindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3Channelization"):
                    self.dsx3channelization = value
                    self.dsx3channelization.value_namespace = name_space
                    self.dsx3channelization.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CircuitIdentifier"):
                    self.dsx3circuitidentifier = value
                    self.dsx3circuitidentifier.value_namespace = name_space
                    self.dsx3circuitidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3Ds1ForRemoteLoop"):
                    self.dsx3ds1forremoteloop = value
                    self.dsx3ds1forremoteloop.value_namespace = name_space
                    self.dsx3ds1forremoteloop.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IfIndex"):
                    self.dsx3ifindex = value
                    self.dsx3ifindex.value_namespace = name_space
                    self.dsx3ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3InvalidIntervals"):
                    self.dsx3invalidintervals = value
                    self.dsx3invalidintervals.value_namespace = name_space
                    self.dsx3invalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LineCoding"):
                    self.dsx3linecoding = value
                    self.dsx3linecoding.value_namespace = name_space
                    self.dsx3linecoding.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LineLength"):
                    self.dsx3linelength = value
                    self.dsx3linelength.value_namespace = name_space
                    self.dsx3linelength.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LineStatus"):
                    self.dsx3linestatus = value
                    self.dsx3linestatus.value_namespace = name_space
                    self.dsx3linestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LineStatusChangeTrapEnable"):
                    self.dsx3linestatuschangetrapenable = value
                    self.dsx3linestatuschangetrapenable.value_namespace = name_space
                    self.dsx3linestatuschangetrapenable.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LineStatusLastChange"):
                    self.dsx3linestatuslastchange = value
                    self.dsx3linestatuslastchange.value_namespace = name_space
                    self.dsx3linestatuslastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LineType"):
                    self.dsx3linetype = value
                    self.dsx3linetype.value_namespace = name_space
                    self.dsx3linetype.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LoopbackConfig"):
                    self.dsx3loopbackconfig = value
                    self.dsx3loopbackconfig.value_namespace = name_space
                    self.dsx3loopbackconfig.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3LoopbackStatus"):
                    self.dsx3loopbackstatus = value
                    self.dsx3loopbackstatus.value_namespace = name_space
                    self.dsx3loopbackstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3SendCode"):
                    self.dsx3sendcode = value
                    self.dsx3sendcode.value_namespace = name_space
                    self.dsx3sendcode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TimeElapsed"):
                    self.dsx3timeelapsed = value
                    self.dsx3timeelapsed.value_namespace = name_space
                    self.dsx3timeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TransmitClockSource"):
                    self.dsx3transmitclocksource = value
                    self.dsx3transmitclocksource.value_namespace = name_space
                    self.dsx3transmitclocksource.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3ValidIntervals"):
                    self.dsx3validintervals = value
                    self.dsx3validintervals.value_namespace = name_space
                    self.dsx3validintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3configentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3configentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3ConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3ConfigEntry"):
                for c in self.dsx3configentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Configtable.Dsx3Configentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3configentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3ConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Currenttable(Entity):
        """
        The DS3/E3 current table contains various
        statistics being collected for the current 15
        minute interval.
        
        .. attribute:: dsx3currententry
        
        	An entry in the DS3/E3 Current table
        	**type**\: list of    :py:class:`Dsx3Currententry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Currenttable.Dsx3Currententry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Currenttable, self).__init__()

            self.yang_name = "dsx3CurrentTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3currententry = YList(self)

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
                        super(Ds3Mib.Dsx3Currenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Currenttable, self).__setattr__(name, value)


        class Dsx3Currententry(Entity):
            """
            An entry in the DS3/E3 Current table.
            
            .. attribute:: dsx3currentindex  <key>
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3currentccvs
            
            	The number of C\-bit Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentcess
            
            	The number of C\-bit Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentcsess
            
            	The number of C\-bit Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentlcvs
            
            	The counter associated with the number of Line Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentless
            
            	The number of Line Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentpcvs
            
            	The counter associated with the number of P\-bit Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentpess
            
            	The counter associated with the number of P\-bit Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentuass
            
            	The counter associated with the number of Unavailable Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Currenttable.Dsx3Currententry, self).__init__()

                self.yang_name = "dsx3CurrentEntry"
                self.yang_parent_name = "dsx3CurrentTable"

                self.dsx3currentindex = YLeaf(YType.int32, "dsx3CurrentIndex")

                self.dsx3currentccvs = YLeaf(YType.uint32, "dsx3CurrentCCVs")

                self.dsx3currentcess = YLeaf(YType.uint32, "dsx3CurrentCESs")

                self.dsx3currentcsess = YLeaf(YType.uint32, "dsx3CurrentCSESs")

                self.dsx3currentlcvs = YLeaf(YType.uint32, "dsx3CurrentLCVs")

                self.dsx3currentless = YLeaf(YType.uint32, "dsx3CurrentLESs")

                self.dsx3currentpcvs = YLeaf(YType.uint32, "dsx3CurrentPCVs")

                self.dsx3currentpess = YLeaf(YType.uint32, "dsx3CurrentPESs")

                self.dsx3currentpsess = YLeaf(YType.uint32, "dsx3CurrentPSESs")

                self.dsx3currentsefss = YLeaf(YType.uint32, "dsx3CurrentSEFSs")

                self.dsx3currentuass = YLeaf(YType.uint32, "dsx3CurrentUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3currentindex",
                                "dsx3currentccvs",
                                "dsx3currentcess",
                                "dsx3currentcsess",
                                "dsx3currentlcvs",
                                "dsx3currentless",
                                "dsx3currentpcvs",
                                "dsx3currentpess",
                                "dsx3currentpsess",
                                "dsx3currentsefss",
                                "dsx3currentuass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Currenttable.Dsx3Currententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Currenttable.Dsx3Currententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3currentindex.is_set or
                    self.dsx3currentccvs.is_set or
                    self.dsx3currentcess.is_set or
                    self.dsx3currentcsess.is_set or
                    self.dsx3currentlcvs.is_set or
                    self.dsx3currentless.is_set or
                    self.dsx3currentpcvs.is_set or
                    self.dsx3currentpess.is_set or
                    self.dsx3currentpsess.is_set or
                    self.dsx3currentsefss.is_set or
                    self.dsx3currentuass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3currentindex.yfilter != YFilter.not_set or
                    self.dsx3currentccvs.yfilter != YFilter.not_set or
                    self.dsx3currentcess.yfilter != YFilter.not_set or
                    self.dsx3currentcsess.yfilter != YFilter.not_set or
                    self.dsx3currentlcvs.yfilter != YFilter.not_set or
                    self.dsx3currentless.yfilter != YFilter.not_set or
                    self.dsx3currentpcvs.yfilter != YFilter.not_set or
                    self.dsx3currentpess.yfilter != YFilter.not_set or
                    self.dsx3currentpsess.yfilter != YFilter.not_set or
                    self.dsx3currentsefss.yfilter != YFilter.not_set or
                    self.dsx3currentuass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3CurrentEntry" + "[dsx3CurrentIndex='" + self.dsx3currentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3CurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3currentindex.is_set or self.dsx3currentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentindex.get_name_leafdata())
                if (self.dsx3currentccvs.is_set or self.dsx3currentccvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentccvs.get_name_leafdata())
                if (self.dsx3currentcess.is_set or self.dsx3currentcess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentcess.get_name_leafdata())
                if (self.dsx3currentcsess.is_set or self.dsx3currentcsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentcsess.get_name_leafdata())
                if (self.dsx3currentlcvs.is_set or self.dsx3currentlcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentlcvs.get_name_leafdata())
                if (self.dsx3currentless.is_set or self.dsx3currentless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentless.get_name_leafdata())
                if (self.dsx3currentpcvs.is_set or self.dsx3currentpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentpcvs.get_name_leafdata())
                if (self.dsx3currentpess.is_set or self.dsx3currentpess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentpess.get_name_leafdata())
                if (self.dsx3currentpsess.is_set or self.dsx3currentpsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentpsess.get_name_leafdata())
                if (self.dsx3currentsefss.is_set or self.dsx3currentsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentsefss.get_name_leafdata())
                if (self.dsx3currentuass.is_set or self.dsx3currentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3currentuass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3CurrentIndex" or name == "dsx3CurrentCCVs" or name == "dsx3CurrentCESs" or name == "dsx3CurrentCSESs" or name == "dsx3CurrentLCVs" or name == "dsx3CurrentLESs" or name == "dsx3CurrentPCVs" or name == "dsx3CurrentPESs" or name == "dsx3CurrentPSESs" or name == "dsx3CurrentSEFSs" or name == "dsx3CurrentUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3CurrentIndex"):
                    self.dsx3currentindex = value
                    self.dsx3currentindex.value_namespace = name_space
                    self.dsx3currentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentCCVs"):
                    self.dsx3currentccvs = value
                    self.dsx3currentccvs.value_namespace = name_space
                    self.dsx3currentccvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentCESs"):
                    self.dsx3currentcess = value
                    self.dsx3currentcess.value_namespace = name_space
                    self.dsx3currentcess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentCSESs"):
                    self.dsx3currentcsess = value
                    self.dsx3currentcsess.value_namespace = name_space
                    self.dsx3currentcsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentLCVs"):
                    self.dsx3currentlcvs = value
                    self.dsx3currentlcvs.value_namespace = name_space
                    self.dsx3currentlcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentLESs"):
                    self.dsx3currentless = value
                    self.dsx3currentless.value_namespace = name_space
                    self.dsx3currentless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentPCVs"):
                    self.dsx3currentpcvs = value
                    self.dsx3currentpcvs.value_namespace = name_space
                    self.dsx3currentpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentPESs"):
                    self.dsx3currentpess = value
                    self.dsx3currentpess.value_namespace = name_space
                    self.dsx3currentpess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentPSESs"):
                    self.dsx3currentpsess = value
                    self.dsx3currentpsess.value_namespace = name_space
                    self.dsx3currentpsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentSEFSs"):
                    self.dsx3currentsefss = value
                    self.dsx3currentsefss.value_namespace = name_space
                    self.dsx3currentsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3CurrentUASs"):
                    self.dsx3currentuass = value
                    self.dsx3currentuass.value_namespace = name_space
                    self.dsx3currentuass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3currententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3currententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3CurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3CurrentEntry"):
                for c in self.dsx3currententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Currenttable.Dsx3Currententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3currententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3CurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Intervaltable(Entity):
        """
        The DS3/E3 Interval Table contains various
        statistics collected by each DS3/E3 Interface over
        the previous 24 hours of operation.  The past 24
        hours are broken into 96 completed 15 minute
        intervals.  Each row in this table represents one
        such interval (identified by dsx3IntervalNumber)
        and for one specific interface (identifed by
        dsx3IntervalIndex).
        
        .. attribute:: dsx3intervalentry
        
        	An entry in the DS3/E3 Interval table
        	**type**\: list of    :py:class:`Dsx3Intervalentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Intervaltable, self).__init__()

            self.yang_name = "dsx3IntervalTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3intervalentry = YList(self)

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
                        super(Ds3Mib.Dsx3Intervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Intervaltable, self).__setattr__(name, value)


        class Dsx3Intervalentry(Entity):
            """
            An entry in the DS3/E3 Interval table.
            
            .. attribute:: dsx3intervalindex  <key>
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3intervalnumber  <key>
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: dsx3intervalccvs
            
            	The number of C\-bit Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalcess
            
            	The number of C\-bit Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalcsess
            
            	The number of C\-bit Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervallcvs
            
            	The counter associated with the number of Line Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalless
            
            	The number of Line Errored  Seconds  (BPVs  or illegal  zero  sequences)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalpcvs
            
            	The counter associated with the number of P\-bit Coding Violations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalpess
            
            	The counter associated with the number of P\-bit Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervaluass
            
            	The counter associated with the number of Unavailable Seconds.  This object may decrease if the occurance of unavailable seconds occurs across an inteval boundary
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry, self).__init__()

                self.yang_name = "dsx3IntervalEntry"
                self.yang_parent_name = "dsx3IntervalTable"

                self.dsx3intervalindex = YLeaf(YType.int32, "dsx3IntervalIndex")

                self.dsx3intervalnumber = YLeaf(YType.int32, "dsx3IntervalNumber")

                self.dsx3intervalccvs = YLeaf(YType.uint32, "dsx3IntervalCCVs")

                self.dsx3intervalcess = YLeaf(YType.uint32, "dsx3IntervalCESs")

                self.dsx3intervalcsess = YLeaf(YType.uint32, "dsx3IntervalCSESs")

                self.dsx3intervallcvs = YLeaf(YType.uint32, "dsx3IntervalLCVs")

                self.dsx3intervalless = YLeaf(YType.uint32, "dsx3IntervalLESs")

                self.dsx3intervalpcvs = YLeaf(YType.uint32, "dsx3IntervalPCVs")

                self.dsx3intervalpess = YLeaf(YType.uint32, "dsx3IntervalPESs")

                self.dsx3intervalpsess = YLeaf(YType.uint32, "dsx3IntervalPSESs")

                self.dsx3intervalsefss = YLeaf(YType.uint32, "dsx3IntervalSEFSs")

                self.dsx3intervaluass = YLeaf(YType.uint32, "dsx3IntervalUASs")

                self.dsx3intervalvaliddata = YLeaf(YType.boolean, "dsx3IntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3intervalindex",
                                "dsx3intervalnumber",
                                "dsx3intervalccvs",
                                "dsx3intervalcess",
                                "dsx3intervalcsess",
                                "dsx3intervallcvs",
                                "dsx3intervalless",
                                "dsx3intervalpcvs",
                                "dsx3intervalpess",
                                "dsx3intervalpsess",
                                "dsx3intervalsefss",
                                "dsx3intervaluass",
                                "dsx3intervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3intervalindex.is_set or
                    self.dsx3intervalnumber.is_set or
                    self.dsx3intervalccvs.is_set or
                    self.dsx3intervalcess.is_set or
                    self.dsx3intervalcsess.is_set or
                    self.dsx3intervallcvs.is_set or
                    self.dsx3intervalless.is_set or
                    self.dsx3intervalpcvs.is_set or
                    self.dsx3intervalpess.is_set or
                    self.dsx3intervalpsess.is_set or
                    self.dsx3intervalsefss.is_set or
                    self.dsx3intervaluass.is_set or
                    self.dsx3intervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3intervalindex.yfilter != YFilter.not_set or
                    self.dsx3intervalnumber.yfilter != YFilter.not_set or
                    self.dsx3intervalccvs.yfilter != YFilter.not_set or
                    self.dsx3intervalcess.yfilter != YFilter.not_set or
                    self.dsx3intervalcsess.yfilter != YFilter.not_set or
                    self.dsx3intervallcvs.yfilter != YFilter.not_set or
                    self.dsx3intervalless.yfilter != YFilter.not_set or
                    self.dsx3intervalpcvs.yfilter != YFilter.not_set or
                    self.dsx3intervalpess.yfilter != YFilter.not_set or
                    self.dsx3intervalpsess.yfilter != YFilter.not_set or
                    self.dsx3intervalsefss.yfilter != YFilter.not_set or
                    self.dsx3intervaluass.yfilter != YFilter.not_set or
                    self.dsx3intervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3IntervalEntry" + "[dsx3IntervalIndex='" + self.dsx3intervalindex.get() + "']" + "[dsx3IntervalNumber='" + self.dsx3intervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3IntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3intervalindex.is_set or self.dsx3intervalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalindex.get_name_leafdata())
                if (self.dsx3intervalnumber.is_set or self.dsx3intervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalnumber.get_name_leafdata())
                if (self.dsx3intervalccvs.is_set or self.dsx3intervalccvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalccvs.get_name_leafdata())
                if (self.dsx3intervalcess.is_set or self.dsx3intervalcess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalcess.get_name_leafdata())
                if (self.dsx3intervalcsess.is_set or self.dsx3intervalcsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalcsess.get_name_leafdata())
                if (self.dsx3intervallcvs.is_set or self.dsx3intervallcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervallcvs.get_name_leafdata())
                if (self.dsx3intervalless.is_set or self.dsx3intervalless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalless.get_name_leafdata())
                if (self.dsx3intervalpcvs.is_set or self.dsx3intervalpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalpcvs.get_name_leafdata())
                if (self.dsx3intervalpess.is_set or self.dsx3intervalpess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalpess.get_name_leafdata())
                if (self.dsx3intervalpsess.is_set or self.dsx3intervalpsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalpsess.get_name_leafdata())
                if (self.dsx3intervalsefss.is_set or self.dsx3intervalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalsefss.get_name_leafdata())
                if (self.dsx3intervaluass.is_set or self.dsx3intervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervaluass.get_name_leafdata())
                if (self.dsx3intervalvaliddata.is_set or self.dsx3intervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3intervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3IntervalIndex" or name == "dsx3IntervalNumber" or name == "dsx3IntervalCCVs" or name == "dsx3IntervalCESs" or name == "dsx3IntervalCSESs" or name == "dsx3IntervalLCVs" or name == "dsx3IntervalLESs" or name == "dsx3IntervalPCVs" or name == "dsx3IntervalPESs" or name == "dsx3IntervalPSESs" or name == "dsx3IntervalSEFSs" or name == "dsx3IntervalUASs" or name == "dsx3IntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3IntervalIndex"):
                    self.dsx3intervalindex = value
                    self.dsx3intervalindex.value_namespace = name_space
                    self.dsx3intervalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalNumber"):
                    self.dsx3intervalnumber = value
                    self.dsx3intervalnumber.value_namespace = name_space
                    self.dsx3intervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalCCVs"):
                    self.dsx3intervalccvs = value
                    self.dsx3intervalccvs.value_namespace = name_space
                    self.dsx3intervalccvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalCESs"):
                    self.dsx3intervalcess = value
                    self.dsx3intervalcess.value_namespace = name_space
                    self.dsx3intervalcess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalCSESs"):
                    self.dsx3intervalcsess = value
                    self.dsx3intervalcsess.value_namespace = name_space
                    self.dsx3intervalcsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalLCVs"):
                    self.dsx3intervallcvs = value
                    self.dsx3intervallcvs.value_namespace = name_space
                    self.dsx3intervallcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalLESs"):
                    self.dsx3intervalless = value
                    self.dsx3intervalless.value_namespace = name_space
                    self.dsx3intervalless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalPCVs"):
                    self.dsx3intervalpcvs = value
                    self.dsx3intervalpcvs.value_namespace = name_space
                    self.dsx3intervalpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalPESs"):
                    self.dsx3intervalpess = value
                    self.dsx3intervalpess.value_namespace = name_space
                    self.dsx3intervalpess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalPSESs"):
                    self.dsx3intervalpsess = value
                    self.dsx3intervalpsess.value_namespace = name_space
                    self.dsx3intervalpsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalSEFSs"):
                    self.dsx3intervalsefss = value
                    self.dsx3intervalsefss.value_namespace = name_space
                    self.dsx3intervalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalUASs"):
                    self.dsx3intervaluass = value
                    self.dsx3intervaluass.value_namespace = name_space
                    self.dsx3intervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3IntervalValidData"):
                    self.dsx3intervalvaliddata = value
                    self.dsx3intervalvaliddata.value_namespace = name_space
                    self.dsx3intervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3intervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3intervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3IntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3IntervalEntry"):
                for c in self.dsx3intervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3intervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3IntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Totaltable(Entity):
        """
        The DS3/E3 Total Table contains the cumulative
        sum of the various statistics for the 24 hour
        period preceding the current interval.
        
        .. attribute:: dsx3totalentry
        
        	An entry in the DS3/E3 Total table
        	**type**\: list of    :py:class:`Dsx3Totalentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Totaltable.Dsx3Totalentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Totaltable, self).__init__()

            self.yang_name = "dsx3TotalTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3totalentry = YList(self)

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
                        super(Ds3Mib.Dsx3Totaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Totaltable, self).__setattr__(name, value)


        class Dsx3Totalentry(Entity):
            """
            An entry in the DS3/E3 Total table.
            
            .. attribute:: dsx3totalindex  <key>
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3totalccvs
            
            	The number of C\-bit Coding Violations encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalcess
            
            	The number of C\-bit Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalcsess
            
            	The number of C\-bit Severely Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totallcvs
            
            	The counter associated with the number of Line Coding Violations encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalless
            
            	The number of Line Errored  Seconds  (BPVs  or illegal  zero  sequences) encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalpcvs
            
            	The counter associated with the number of P\-bit Coding Violations, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalpess
            
            	The counter associated with the number of P\-bit Errored Seconds, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds, encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totaluass
            
            	The counter associated with the number of Unavailable Seconds, encountered by a DS3 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Totaltable.Dsx3Totalentry, self).__init__()

                self.yang_name = "dsx3TotalEntry"
                self.yang_parent_name = "dsx3TotalTable"

                self.dsx3totalindex = YLeaf(YType.int32, "dsx3TotalIndex")

                self.dsx3totalccvs = YLeaf(YType.uint32, "dsx3TotalCCVs")

                self.dsx3totalcess = YLeaf(YType.uint32, "dsx3TotalCESs")

                self.dsx3totalcsess = YLeaf(YType.uint32, "dsx3TotalCSESs")

                self.dsx3totallcvs = YLeaf(YType.uint32, "dsx3TotalLCVs")

                self.dsx3totalless = YLeaf(YType.uint32, "dsx3TotalLESs")

                self.dsx3totalpcvs = YLeaf(YType.uint32, "dsx3TotalPCVs")

                self.dsx3totalpess = YLeaf(YType.uint32, "dsx3TotalPESs")

                self.dsx3totalpsess = YLeaf(YType.uint32, "dsx3TotalPSESs")

                self.dsx3totalsefss = YLeaf(YType.uint32, "dsx3TotalSEFSs")

                self.dsx3totaluass = YLeaf(YType.uint32, "dsx3TotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3totalindex",
                                "dsx3totalccvs",
                                "dsx3totalcess",
                                "dsx3totalcsess",
                                "dsx3totallcvs",
                                "dsx3totalless",
                                "dsx3totalpcvs",
                                "dsx3totalpess",
                                "dsx3totalpsess",
                                "dsx3totalsefss",
                                "dsx3totaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Totaltable.Dsx3Totalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Totaltable.Dsx3Totalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3totalindex.is_set or
                    self.dsx3totalccvs.is_set or
                    self.dsx3totalcess.is_set or
                    self.dsx3totalcsess.is_set or
                    self.dsx3totallcvs.is_set or
                    self.dsx3totalless.is_set or
                    self.dsx3totalpcvs.is_set or
                    self.dsx3totalpess.is_set or
                    self.dsx3totalpsess.is_set or
                    self.dsx3totalsefss.is_set or
                    self.dsx3totaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3totalindex.yfilter != YFilter.not_set or
                    self.dsx3totalccvs.yfilter != YFilter.not_set or
                    self.dsx3totalcess.yfilter != YFilter.not_set or
                    self.dsx3totalcsess.yfilter != YFilter.not_set or
                    self.dsx3totallcvs.yfilter != YFilter.not_set or
                    self.dsx3totalless.yfilter != YFilter.not_set or
                    self.dsx3totalpcvs.yfilter != YFilter.not_set or
                    self.dsx3totalpess.yfilter != YFilter.not_set or
                    self.dsx3totalpsess.yfilter != YFilter.not_set or
                    self.dsx3totalsefss.yfilter != YFilter.not_set or
                    self.dsx3totaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3TotalEntry" + "[dsx3TotalIndex='" + self.dsx3totalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3TotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3totalindex.is_set or self.dsx3totalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalindex.get_name_leafdata())
                if (self.dsx3totalccvs.is_set or self.dsx3totalccvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalccvs.get_name_leafdata())
                if (self.dsx3totalcess.is_set or self.dsx3totalcess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalcess.get_name_leafdata())
                if (self.dsx3totalcsess.is_set or self.dsx3totalcsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalcsess.get_name_leafdata())
                if (self.dsx3totallcvs.is_set or self.dsx3totallcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totallcvs.get_name_leafdata())
                if (self.dsx3totalless.is_set or self.dsx3totalless.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalless.get_name_leafdata())
                if (self.dsx3totalpcvs.is_set or self.dsx3totalpcvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalpcvs.get_name_leafdata())
                if (self.dsx3totalpess.is_set or self.dsx3totalpess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalpess.get_name_leafdata())
                if (self.dsx3totalpsess.is_set or self.dsx3totalpsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalpsess.get_name_leafdata())
                if (self.dsx3totalsefss.is_set or self.dsx3totalsefss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totalsefss.get_name_leafdata())
                if (self.dsx3totaluass.is_set or self.dsx3totaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3totaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3TotalIndex" or name == "dsx3TotalCCVs" or name == "dsx3TotalCESs" or name == "dsx3TotalCSESs" or name == "dsx3TotalLCVs" or name == "dsx3TotalLESs" or name == "dsx3TotalPCVs" or name == "dsx3TotalPESs" or name == "dsx3TotalPSESs" or name == "dsx3TotalSEFSs" or name == "dsx3TotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3TotalIndex"):
                    self.dsx3totalindex = value
                    self.dsx3totalindex.value_namespace = name_space
                    self.dsx3totalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalCCVs"):
                    self.dsx3totalccvs = value
                    self.dsx3totalccvs.value_namespace = name_space
                    self.dsx3totalccvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalCESs"):
                    self.dsx3totalcess = value
                    self.dsx3totalcess.value_namespace = name_space
                    self.dsx3totalcess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalCSESs"):
                    self.dsx3totalcsess = value
                    self.dsx3totalcsess.value_namespace = name_space
                    self.dsx3totalcsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalLCVs"):
                    self.dsx3totallcvs = value
                    self.dsx3totallcvs.value_namespace = name_space
                    self.dsx3totallcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalLESs"):
                    self.dsx3totalless = value
                    self.dsx3totalless.value_namespace = name_space
                    self.dsx3totalless.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalPCVs"):
                    self.dsx3totalpcvs = value
                    self.dsx3totalpcvs.value_namespace = name_space
                    self.dsx3totalpcvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalPESs"):
                    self.dsx3totalpess = value
                    self.dsx3totalpess.value_namespace = name_space
                    self.dsx3totalpess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalPSESs"):
                    self.dsx3totalpsess = value
                    self.dsx3totalpsess.value_namespace = name_space
                    self.dsx3totalpsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalSEFSs"):
                    self.dsx3totalsefss = value
                    self.dsx3totalsefss.value_namespace = name_space
                    self.dsx3totalsefss.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3TotalUASs"):
                    self.dsx3totaluass = value
                    self.dsx3totaluass.value_namespace = name_space
                    self.dsx3totaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3totalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3totalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3TotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3TotalEntry"):
                for c in self.dsx3totalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Totaltable.Dsx3Totalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3totalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3TotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Farendconfigtable(Entity):
        """
        The DS3 Far End Configuration Table contains
        configuration information reported in the C\-bits
        from the remote end.
        
        .. attribute:: dsx3farendconfigentry
        
        	An entry in the DS3 Far End Configuration table
        	**type**\: list of    :py:class:`Dsx3Farendconfigentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Farendconfigtable, self).__init__()

            self.yang_name = "dsx3FarEndConfigTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3farendconfigentry = YList(self)

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
                        super(Ds3Mib.Dsx3Farendconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Farendconfigtable, self).__setattr__(name, value)


        class Dsx3Farendconfigentry(Entity):
            """
            An entry in the DS3 Far End Configuration table.
            
            .. attribute:: dsx3farendlineindex  <key>
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendequipcode
            
            	This is the Far End Equipment Identification code that describes the specific piece of equipment. It is sent within the Path Identification Message
            	**type**\:  str
            
            	**length:** 0..10
            
            .. attribute:: dsx3farendfacilityidcode
            
            	This code identifies a specific Far End DS3 path. It is sent within the Path Identification Message
            	**type**\:  str
            
            	**length:** 0..38
            
            .. attribute:: dsx3farendframeidcode
            
            	This is the Far End Frame Identification code that identifies where the equipment is located within a building at a given location.  It is sent within the Path Identification Message
            	**type**\:  str
            
            	**length:** 0..10
            
            .. attribute:: dsx3farendlocationidcode
            
            	This is the Far End Location Identification code that describes the specific location of the equipment.  It is sent within the Path Identification Message
            	**type**\:  str
            
            	**length:** 0..11
            
            .. attribute:: dsx3farendunitcode
            
            	This is the Far End code that identifies the equipment location within a bay.  It is sent within the Path Identification Message
            	**type**\:  str
            
            	**length:** 0..6
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry, self).__init__()

                self.yang_name = "dsx3FarEndConfigEntry"
                self.yang_parent_name = "dsx3FarEndConfigTable"

                self.dsx3farendlineindex = YLeaf(YType.int32, "dsx3FarEndLineIndex")

                self.dsx3farendequipcode = YLeaf(YType.str, "dsx3FarEndEquipCode")

                self.dsx3farendfacilityidcode = YLeaf(YType.str, "dsx3FarEndFacilityIDCode")

                self.dsx3farendframeidcode = YLeaf(YType.str, "dsx3FarEndFrameIDCode")

                self.dsx3farendlocationidcode = YLeaf(YType.str, "dsx3FarEndLocationIDCode")

                self.dsx3farendunitcode = YLeaf(YType.str, "dsx3FarEndUnitCode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3farendlineindex",
                                "dsx3farendequipcode",
                                "dsx3farendfacilityidcode",
                                "dsx3farendframeidcode",
                                "dsx3farendlocationidcode",
                                "dsx3farendunitcode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3farendlineindex.is_set or
                    self.dsx3farendequipcode.is_set or
                    self.dsx3farendfacilityidcode.is_set or
                    self.dsx3farendframeidcode.is_set or
                    self.dsx3farendlocationidcode.is_set or
                    self.dsx3farendunitcode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3farendlineindex.yfilter != YFilter.not_set or
                    self.dsx3farendequipcode.yfilter != YFilter.not_set or
                    self.dsx3farendfacilityidcode.yfilter != YFilter.not_set or
                    self.dsx3farendframeidcode.yfilter != YFilter.not_set or
                    self.dsx3farendlocationidcode.yfilter != YFilter.not_set or
                    self.dsx3farendunitcode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3FarEndConfigEntry" + "[dsx3FarEndLineIndex='" + self.dsx3farendlineindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3FarEndConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3farendlineindex.is_set or self.dsx3farendlineindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendlineindex.get_name_leafdata())
                if (self.dsx3farendequipcode.is_set or self.dsx3farendequipcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendequipcode.get_name_leafdata())
                if (self.dsx3farendfacilityidcode.is_set or self.dsx3farendfacilityidcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendfacilityidcode.get_name_leafdata())
                if (self.dsx3farendframeidcode.is_set or self.dsx3farendframeidcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendframeidcode.get_name_leafdata())
                if (self.dsx3farendlocationidcode.is_set or self.dsx3farendlocationidcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendlocationidcode.get_name_leafdata())
                if (self.dsx3farendunitcode.is_set or self.dsx3farendunitcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendunitcode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3FarEndLineIndex" or name == "dsx3FarEndEquipCode" or name == "dsx3FarEndFacilityIDCode" or name == "dsx3FarEndFrameIDCode" or name == "dsx3FarEndLocationIDCode" or name == "dsx3FarEndUnitCode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3FarEndLineIndex"):
                    self.dsx3farendlineindex = value
                    self.dsx3farendlineindex.value_namespace = name_space
                    self.dsx3farendlineindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndEquipCode"):
                    self.dsx3farendequipcode = value
                    self.dsx3farendequipcode.value_namespace = name_space
                    self.dsx3farendequipcode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndFacilityIDCode"):
                    self.dsx3farendfacilityidcode = value
                    self.dsx3farendfacilityidcode.value_namespace = name_space
                    self.dsx3farendfacilityidcode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndFrameIDCode"):
                    self.dsx3farendframeidcode = value
                    self.dsx3farendframeidcode.value_namespace = name_space
                    self.dsx3farendframeidcode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndLocationIDCode"):
                    self.dsx3farendlocationidcode = value
                    self.dsx3farendlocationidcode.value_namespace = name_space
                    self.dsx3farendlocationidcode.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndUnitCode"):
                    self.dsx3farendunitcode = value
                    self.dsx3farendunitcode.value_namespace = name_space
                    self.dsx3farendunitcode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3farendconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3farendconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3FarEndConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3FarEndConfigEntry"):
                for c in self.dsx3farendconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3farendconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3FarEndConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Farendcurrenttable(Entity):
        """
        The DS3 Far End Current table contains various
        statistics being collected for the current 15
        minute interval.  The statistics are collected
        from the far end block error code within the C\-
        bits.
        
        .. attribute:: dsx3farendcurrententry
        
        	An entry in the DS3 Far End Current table
        	**type**\: list of    :py:class:`Dsx3Farendcurrententry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Farendcurrenttable, self).__init__()

            self.yang_name = "dsx3FarEndCurrentTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3farendcurrententry = YList(self)

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
                        super(Ds3Mib.Dsx3Farendcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Farendcurrenttable, self).__setattr__(name, value)


        class Dsx3Farendcurrententry(Entity):
            """
            An entry in the DS3 Far End Current table.
            
            .. attribute:: dsx3farendcurrentindex  <key>
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendcurrentccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendcurrentcess
            
            	The counter associated with the number of Far Far End C\-bit Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendcurrentcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendcurrentuass
            
            	The counter associated with the number of Far End unavailable seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendinvalidintervals
            
            	The number of intervals in the range from 0 to dsx3FarEndValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\:  int
            
            	**range:** 0..96
            
            .. attribute:: dsx3farendtimeelapsed
            
            	The number of seconds that have elapsed since the beginning of the far end current error\-measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            .. attribute:: dsx3farendvalidintervals
            
            	The number of previous far end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute far end intervals since the interface has been online
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry, self).__init__()

                self.yang_name = "dsx3FarEndCurrentEntry"
                self.yang_parent_name = "dsx3FarEndCurrentTable"

                self.dsx3farendcurrentindex = YLeaf(YType.int32, "dsx3FarEndCurrentIndex")

                self.dsx3farendcurrentccvs = YLeaf(YType.uint32, "dsx3FarEndCurrentCCVs")

                self.dsx3farendcurrentcess = YLeaf(YType.uint32, "dsx3FarEndCurrentCESs")

                self.dsx3farendcurrentcsess = YLeaf(YType.uint32, "dsx3FarEndCurrentCSESs")

                self.dsx3farendcurrentuass = YLeaf(YType.uint32, "dsx3FarEndCurrentUASs")

                self.dsx3farendinvalidintervals = YLeaf(YType.int32, "dsx3FarEndInvalidIntervals")

                self.dsx3farendtimeelapsed = YLeaf(YType.int32, "dsx3FarEndTimeElapsed")

                self.dsx3farendvalidintervals = YLeaf(YType.int32, "dsx3FarEndValidIntervals")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3farendcurrentindex",
                                "dsx3farendcurrentccvs",
                                "dsx3farendcurrentcess",
                                "dsx3farendcurrentcsess",
                                "dsx3farendcurrentuass",
                                "dsx3farendinvalidintervals",
                                "dsx3farendtimeelapsed",
                                "dsx3farendvalidintervals") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3farendcurrentindex.is_set or
                    self.dsx3farendcurrentccvs.is_set or
                    self.dsx3farendcurrentcess.is_set or
                    self.dsx3farendcurrentcsess.is_set or
                    self.dsx3farendcurrentuass.is_set or
                    self.dsx3farendinvalidintervals.is_set or
                    self.dsx3farendtimeelapsed.is_set or
                    self.dsx3farendvalidintervals.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3farendcurrentindex.yfilter != YFilter.not_set or
                    self.dsx3farendcurrentccvs.yfilter != YFilter.not_set or
                    self.dsx3farendcurrentcess.yfilter != YFilter.not_set or
                    self.dsx3farendcurrentcsess.yfilter != YFilter.not_set or
                    self.dsx3farendcurrentuass.yfilter != YFilter.not_set or
                    self.dsx3farendinvalidintervals.yfilter != YFilter.not_set or
                    self.dsx3farendtimeelapsed.yfilter != YFilter.not_set or
                    self.dsx3farendvalidintervals.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3FarEndCurrentEntry" + "[dsx3FarEndCurrentIndex='" + self.dsx3farendcurrentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3FarEndCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3farendcurrentindex.is_set or self.dsx3farendcurrentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendcurrentindex.get_name_leafdata())
                if (self.dsx3farendcurrentccvs.is_set or self.dsx3farendcurrentccvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendcurrentccvs.get_name_leafdata())
                if (self.dsx3farendcurrentcess.is_set or self.dsx3farendcurrentcess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendcurrentcess.get_name_leafdata())
                if (self.dsx3farendcurrentcsess.is_set or self.dsx3farendcurrentcsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendcurrentcsess.get_name_leafdata())
                if (self.dsx3farendcurrentuass.is_set or self.dsx3farendcurrentuass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendcurrentuass.get_name_leafdata())
                if (self.dsx3farendinvalidintervals.is_set or self.dsx3farendinvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendinvalidintervals.get_name_leafdata())
                if (self.dsx3farendtimeelapsed.is_set or self.dsx3farendtimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendtimeelapsed.get_name_leafdata())
                if (self.dsx3farendvalidintervals.is_set or self.dsx3farendvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendvalidintervals.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3FarEndCurrentIndex" or name == "dsx3FarEndCurrentCCVs" or name == "dsx3FarEndCurrentCESs" or name == "dsx3FarEndCurrentCSESs" or name == "dsx3FarEndCurrentUASs" or name == "dsx3FarEndInvalidIntervals" or name == "dsx3FarEndTimeElapsed" or name == "dsx3FarEndValidIntervals"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3FarEndCurrentIndex"):
                    self.dsx3farendcurrentindex = value
                    self.dsx3farendcurrentindex.value_namespace = name_space
                    self.dsx3farendcurrentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndCurrentCCVs"):
                    self.dsx3farendcurrentccvs = value
                    self.dsx3farendcurrentccvs.value_namespace = name_space
                    self.dsx3farendcurrentccvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndCurrentCESs"):
                    self.dsx3farendcurrentcess = value
                    self.dsx3farendcurrentcess.value_namespace = name_space
                    self.dsx3farendcurrentcess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndCurrentCSESs"):
                    self.dsx3farendcurrentcsess = value
                    self.dsx3farendcurrentcsess.value_namespace = name_space
                    self.dsx3farendcurrentcsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndCurrentUASs"):
                    self.dsx3farendcurrentuass = value
                    self.dsx3farendcurrentuass.value_namespace = name_space
                    self.dsx3farendcurrentuass.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndInvalidIntervals"):
                    self.dsx3farendinvalidintervals = value
                    self.dsx3farendinvalidintervals.value_namespace = name_space
                    self.dsx3farendinvalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndTimeElapsed"):
                    self.dsx3farendtimeelapsed = value
                    self.dsx3farendtimeelapsed.value_namespace = name_space
                    self.dsx3farendtimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndValidIntervals"):
                    self.dsx3farendvalidintervals = value
                    self.dsx3farendvalidintervals.value_namespace = name_space
                    self.dsx3farendvalidintervals.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3farendcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3farendcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3FarEndCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3FarEndCurrentEntry"):
                for c in self.dsx3farendcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3farendcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3FarEndCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Farendintervaltable(Entity):
        """
        The DS3 Far End Interval Table contains various
        statistics collected by each DS3 interface over
        the previous 24 hours of operation.  The past 24
        hours are broken into 96 completed 15 minute
        intervals.
        
        .. attribute:: dsx3farendintervalentry
        
        	An entry in the DS3 Far End Interval table
        	**type**\: list of    :py:class:`Dsx3Farendintervalentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Farendintervaltable, self).__init__()

            self.yang_name = "dsx3FarEndIntervalTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3farendintervalentry = YList(self)

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
                        super(Ds3Mib.Dsx3Farendintervaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Farendintervaltable, self).__setattr__(name, value)


        class Dsx3Farendintervalentry(Entity):
            """
            An entry in the DS3 Far End Interval table.
            
            .. attribute:: dsx3farendintervalindex  <key>
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendintervalnumber  <key>
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: dsx3farendintervalccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervalcess
            
            	The counter associated with the number of Far End C\-bit Errored Seconds encountered by a DS3 interface in one of the previous 96, individual 15 minute, intervals. In the case where the agent is a proxy and data is not available, return noSuchInstance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervalcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervaluass
            
            	The counter associated with the number of Far End unavailable seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry, self).__init__()

                self.yang_name = "dsx3FarEndIntervalEntry"
                self.yang_parent_name = "dsx3FarEndIntervalTable"

                self.dsx3farendintervalindex = YLeaf(YType.int32, "dsx3FarEndIntervalIndex")

                self.dsx3farendintervalnumber = YLeaf(YType.int32, "dsx3FarEndIntervalNumber")

                self.dsx3farendintervalccvs = YLeaf(YType.uint32, "dsx3FarEndIntervalCCVs")

                self.dsx3farendintervalcess = YLeaf(YType.uint32, "dsx3FarEndIntervalCESs")

                self.dsx3farendintervalcsess = YLeaf(YType.uint32, "dsx3FarEndIntervalCSESs")

                self.dsx3farendintervaluass = YLeaf(YType.uint32, "dsx3FarEndIntervalUASs")

                self.dsx3farendintervalvaliddata = YLeaf(YType.boolean, "dsx3FarEndIntervalValidData")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3farendintervalindex",
                                "dsx3farendintervalnumber",
                                "dsx3farendintervalccvs",
                                "dsx3farendintervalcess",
                                "dsx3farendintervalcsess",
                                "dsx3farendintervaluass",
                                "dsx3farendintervalvaliddata") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3farendintervalindex.is_set or
                    self.dsx3farendintervalnumber.is_set or
                    self.dsx3farendintervalccvs.is_set or
                    self.dsx3farendintervalcess.is_set or
                    self.dsx3farendintervalcsess.is_set or
                    self.dsx3farendintervaluass.is_set or
                    self.dsx3farendintervalvaliddata.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3farendintervalindex.yfilter != YFilter.not_set or
                    self.dsx3farendintervalnumber.yfilter != YFilter.not_set or
                    self.dsx3farendintervalccvs.yfilter != YFilter.not_set or
                    self.dsx3farendintervalcess.yfilter != YFilter.not_set or
                    self.dsx3farendintervalcsess.yfilter != YFilter.not_set or
                    self.dsx3farendintervaluass.yfilter != YFilter.not_set or
                    self.dsx3farendintervalvaliddata.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3FarEndIntervalEntry" + "[dsx3FarEndIntervalIndex='" + self.dsx3farendintervalindex.get() + "']" + "[dsx3FarEndIntervalNumber='" + self.dsx3farendintervalnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3FarEndIntervalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3farendintervalindex.is_set or self.dsx3farendintervalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervalindex.get_name_leafdata())
                if (self.dsx3farendintervalnumber.is_set or self.dsx3farendintervalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervalnumber.get_name_leafdata())
                if (self.dsx3farendintervalccvs.is_set or self.dsx3farendintervalccvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervalccvs.get_name_leafdata())
                if (self.dsx3farendintervalcess.is_set or self.dsx3farendintervalcess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervalcess.get_name_leafdata())
                if (self.dsx3farendintervalcsess.is_set or self.dsx3farendintervalcsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervalcsess.get_name_leafdata())
                if (self.dsx3farendintervaluass.is_set or self.dsx3farendintervaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervaluass.get_name_leafdata())
                if (self.dsx3farendintervalvaliddata.is_set or self.dsx3farendintervalvaliddata.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendintervalvaliddata.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3FarEndIntervalIndex" or name == "dsx3FarEndIntervalNumber" or name == "dsx3FarEndIntervalCCVs" or name == "dsx3FarEndIntervalCESs" or name == "dsx3FarEndIntervalCSESs" or name == "dsx3FarEndIntervalUASs" or name == "dsx3FarEndIntervalValidData"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3FarEndIntervalIndex"):
                    self.dsx3farendintervalindex = value
                    self.dsx3farendintervalindex.value_namespace = name_space
                    self.dsx3farendintervalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndIntervalNumber"):
                    self.dsx3farendintervalnumber = value
                    self.dsx3farendintervalnumber.value_namespace = name_space
                    self.dsx3farendintervalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndIntervalCCVs"):
                    self.dsx3farendintervalccvs = value
                    self.dsx3farendintervalccvs.value_namespace = name_space
                    self.dsx3farendintervalccvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndIntervalCESs"):
                    self.dsx3farendintervalcess = value
                    self.dsx3farendintervalcess.value_namespace = name_space
                    self.dsx3farendintervalcess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndIntervalCSESs"):
                    self.dsx3farendintervalcsess = value
                    self.dsx3farendintervalcsess.value_namespace = name_space
                    self.dsx3farendintervalcsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndIntervalUASs"):
                    self.dsx3farendintervaluass = value
                    self.dsx3farendintervaluass.value_namespace = name_space
                    self.dsx3farendintervaluass.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndIntervalValidData"):
                    self.dsx3farendintervalvaliddata = value
                    self.dsx3farendintervalvaliddata.value_namespace = name_space
                    self.dsx3farendintervalvaliddata.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3farendintervalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3farendintervalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3FarEndIntervalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3FarEndIntervalEntry"):
                for c in self.dsx3farendintervalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3farendintervalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3FarEndIntervalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Farendtotaltable(Entity):
        """
        The DS3 Far End Total Table contains the
        cumulative sum of the various statistics for the
        24 hour period preceding the current interval.
        
        .. attribute:: dsx3farendtotalentry
        
        	An entry in the DS3 Far End Total table
        	**type**\: list of    :py:class:`Dsx3Farendtotalentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Farendtotaltable, self).__init__()

            self.yang_name = "dsx3FarEndTotalTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3farendtotalentry = YList(self)

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
                        super(Ds3Mib.Dsx3Farendtotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Farendtotaltable, self).__setattr__(name, value)


        class Dsx3Farendtotalentry(Entity):
            """
            An entry in the DS3 Far End Total table.
            
            .. attribute:: dsx3farendtotalindex  <key>
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendtotalccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendtotalcess
            
            	The counter associated with the number of Far End C\-bit Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendtotalcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendtotaluass
            
            	The counter associated with the number of Far End unavailable seconds encountered by a DS3 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry, self).__init__()

                self.yang_name = "dsx3FarEndTotalEntry"
                self.yang_parent_name = "dsx3FarEndTotalTable"

                self.dsx3farendtotalindex = YLeaf(YType.int32, "dsx3FarEndTotalIndex")

                self.dsx3farendtotalccvs = YLeaf(YType.uint32, "dsx3FarEndTotalCCVs")

                self.dsx3farendtotalcess = YLeaf(YType.uint32, "dsx3FarEndTotalCESs")

                self.dsx3farendtotalcsess = YLeaf(YType.uint32, "dsx3FarEndTotalCSESs")

                self.dsx3farendtotaluass = YLeaf(YType.uint32, "dsx3FarEndTotalUASs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3farendtotalindex",
                                "dsx3farendtotalccvs",
                                "dsx3farendtotalcess",
                                "dsx3farendtotalcsess",
                                "dsx3farendtotaluass") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3farendtotalindex.is_set or
                    self.dsx3farendtotalccvs.is_set or
                    self.dsx3farendtotalcess.is_set or
                    self.dsx3farendtotalcsess.is_set or
                    self.dsx3farendtotaluass.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3farendtotalindex.yfilter != YFilter.not_set or
                    self.dsx3farendtotalccvs.yfilter != YFilter.not_set or
                    self.dsx3farendtotalcess.yfilter != YFilter.not_set or
                    self.dsx3farendtotalcsess.yfilter != YFilter.not_set or
                    self.dsx3farendtotaluass.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3FarEndTotalEntry" + "[dsx3FarEndTotalIndex='" + self.dsx3farendtotalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3FarEndTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3farendtotalindex.is_set or self.dsx3farendtotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendtotalindex.get_name_leafdata())
                if (self.dsx3farendtotalccvs.is_set or self.dsx3farendtotalccvs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendtotalccvs.get_name_leafdata())
                if (self.dsx3farendtotalcess.is_set or self.dsx3farendtotalcess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendtotalcess.get_name_leafdata())
                if (self.dsx3farendtotalcsess.is_set or self.dsx3farendtotalcsess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendtotalcsess.get_name_leafdata())
                if (self.dsx3farendtotaluass.is_set or self.dsx3farendtotaluass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3farendtotaluass.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3FarEndTotalIndex" or name == "dsx3FarEndTotalCCVs" or name == "dsx3FarEndTotalCESs" or name == "dsx3FarEndTotalCSESs" or name == "dsx3FarEndTotalUASs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3FarEndTotalIndex"):
                    self.dsx3farendtotalindex = value
                    self.dsx3farendtotalindex.value_namespace = name_space
                    self.dsx3farendtotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndTotalCCVs"):
                    self.dsx3farendtotalccvs = value
                    self.dsx3farendtotalccvs.value_namespace = name_space
                    self.dsx3farendtotalccvs.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndTotalCESs"):
                    self.dsx3farendtotalcess = value
                    self.dsx3farendtotalcess.value_namespace = name_space
                    self.dsx3farendtotalcess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndTotalCSESs"):
                    self.dsx3farendtotalcsess = value
                    self.dsx3farendtotalcsess.value_namespace = name_space
                    self.dsx3farendtotalcsess.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FarEndTotalUASs"):
                    self.dsx3farendtotaluass = value
                    self.dsx3farendtotaluass.value_namespace = name_space
                    self.dsx3farendtotaluass.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3farendtotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3farendtotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3FarEndTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3FarEndTotalEntry"):
                for c in self.dsx3farendtotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3farendtotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3FarEndTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dsx3Fractable(Entity):
        """
        This table is deprecated in favour of using
        ifStackTable.
        
        Implementation of this table was optional.  It was
        designed for those systems dividing a DS3/E3 into
        channels containing different data streams that
        are of local interest.
        
        The DS3/E3 fractional table identifies which
        DS3/E3 channels associated with a CSU are being
        used to support a logical interface, i.e., an
        entry in the interfaces table from the Internet\-
        standard MIB.
        
        For example, consider a DS3 device with 4 high
        speed links carrying router traffic, a feed for
        voice, a feed for video, and a synchronous channel
        for a non\-routed protocol.  We might describe the
        allocation of channels, in the dsx3FracTable, as
        follows\:
        dsx3FracIfIndex.2. 1 = 3  dsx3FracIfIndex.2.15 = 4
        dsx3FracIfIndex.2. 2 = 3  dsx3FracIfIndex.2.16 = 6
        dsx3FracIfIndex.2. 3 = 3  dsx3FracIfIndex.2.17 = 6
        dsx3FracIfIndex.2. 4 = 3  dsx3FracIfIndex.2.18 = 6
        dsx3FracIfIndex.2. 5 = 3  dsx3FracIfIndex.2.19 = 6
        dsx3FracIfIndex.2. 6 = 3  dsx3FracIfIndex.2.20 = 6
        dsx3FracIfIndex.2. 7 = 4  dsx3FracIfIndex.2.21 = 6
        dsx3FracIfIndex.2. 8 = 4  dsx3FracIfIndex.2.22 = 6
        dsx3FracIfIndex.2. 9 = 4  dsx3FracIfIndex.2.23 = 6
        dsx3FracIfIndex.2.10 = 4  dsx3FracIfIndex.2.24 = 6
        dsx3FracIfIndex.2.11 = 4  dsx3FracIfIndex.2.25 = 6
        dsx3FracIfIndex.2.12 = 5  dsx3FracIfIndex.2.26 = 6
        dsx3FracIfIndex.2.13 = 5  dsx3FracIfIndex.2.27 = 6
        dsx3FracIfIndex.2.14 = 5  dsx3FracIfIndex.2.28 = 6
        For dsx3M23, dsx3 SYNTRAN, dsx3CbitParity, and
        dsx3ClearChannel  there are 28 legal channels,
        numbered 1 throug h 28.
        
        For e3Framed there are 16 legal channels, numbered
        1 through 16.  The channels (1..16) correspond
        directly to the equivalently numbered time\-slots.
        
        .. attribute:: dsx3fracentry
        
        	An entry in the DS3 Fractional table
        	**type**\: list of    :py:class:`Dsx3Fracentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Fractable.Dsx3Fracentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(Ds3Mib.Dsx3Fractable, self).__init__()

            self.yang_name = "dsx3FracTable"
            self.yang_parent_name = "DS3-MIB"

            self.dsx3fracentry = YList(self)

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
                        super(Ds3Mib.Dsx3Fractable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ds3Mib.Dsx3Fractable, self).__setattr__(name, value)


        class Dsx3Fracentry(Entity):
            """
            An entry in the DS3 Fractional table.
            
            .. attribute:: dsx3fracindex  <key>
            
            	The index value which uniquely identifies  the DS3  interface  to which this entry is applicable The interface identified by a  particular value of  this  index is the same interface as identified by the same value  an  dsx3LineIndex object instance
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: dsx3fracnumber  <key>
            
            	The channel number for this entry
            	**type**\:  int
            
            	**range:** 1..31
            
            	**status**\: deprecated
            
            .. attribute:: dsx3fracifindex
            
            	An index value that uniquely identifies an interface.  The interface identified by a particular value of this index is the same interface as  identified by the same value an ifIndex object instance. If no interface is currently using a channel, the value should be zero.  If a single interface occupies more  than one  time slot,  that ifIndex value will be found in multiple time slots
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(Ds3Mib.Dsx3Fractable.Dsx3Fracentry, self).__init__()

                self.yang_name = "dsx3FracEntry"
                self.yang_parent_name = "dsx3FracTable"

                self.dsx3fracindex = YLeaf(YType.int32, "dsx3FracIndex")

                self.dsx3fracnumber = YLeaf(YType.int32, "dsx3FracNumber")

                self.dsx3fracifindex = YLeaf(YType.int32, "dsx3FracIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dsx3fracindex",
                                "dsx3fracnumber",
                                "dsx3fracifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ds3Mib.Dsx3Fractable.Dsx3Fracentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ds3Mib.Dsx3Fractable.Dsx3Fracentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dsx3fracindex.is_set or
                    self.dsx3fracnumber.is_set or
                    self.dsx3fracifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dsx3fracindex.yfilter != YFilter.not_set or
                    self.dsx3fracnumber.yfilter != YFilter.not_set or
                    self.dsx3fracifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dsx3FracEntry" + "[dsx3FracIndex='" + self.dsx3fracindex.get() + "']" + "[dsx3FracNumber='" + self.dsx3fracnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DS3-MIB:DS3-MIB/dsx3FracTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dsx3fracindex.is_set or self.dsx3fracindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3fracindex.get_name_leafdata())
                if (self.dsx3fracnumber.is_set or self.dsx3fracnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3fracnumber.get_name_leafdata())
                if (self.dsx3fracifindex.is_set or self.dsx3fracifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsx3fracifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dsx3FracIndex" or name == "dsx3FracNumber" or name == "dsx3FracIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dsx3FracIndex"):
                    self.dsx3fracindex = value
                    self.dsx3fracindex.value_namespace = name_space
                    self.dsx3fracindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FracNumber"):
                    self.dsx3fracnumber = value
                    self.dsx3fracnumber.value_namespace = name_space
                    self.dsx3fracnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "dsx3FracIfIndex"):
                    self.dsx3fracifindex = value
                    self.dsx3fracifindex.value_namespace = name_space
                    self.dsx3fracifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dsx3fracentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dsx3fracentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dsx3FracTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DS3-MIB:DS3-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dsx3FracEntry"):
                for c in self.dsx3fracentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ds3Mib.Dsx3Fractable.Dsx3Fracentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dsx3fracentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dsx3FracEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dsx3configtable is not None and self.dsx3configtable.has_data()) or
            (self.dsx3currenttable is not None and self.dsx3currenttable.has_data()) or
            (self.dsx3farendconfigtable is not None and self.dsx3farendconfigtable.has_data()) or
            (self.dsx3farendcurrenttable is not None and self.dsx3farendcurrenttable.has_data()) or
            (self.dsx3farendintervaltable is not None and self.dsx3farendintervaltable.has_data()) or
            (self.dsx3farendtotaltable is not None and self.dsx3farendtotaltable.has_data()) or
            (self.dsx3fractable is not None and self.dsx3fractable.has_data()) or
            (self.dsx3intervaltable is not None and self.dsx3intervaltable.has_data()) or
            (self.dsx3totaltable is not None and self.dsx3totaltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dsx3configtable is not None and self.dsx3configtable.has_operation()) or
            (self.dsx3currenttable is not None and self.dsx3currenttable.has_operation()) or
            (self.dsx3farendconfigtable is not None and self.dsx3farendconfigtable.has_operation()) or
            (self.dsx3farendcurrenttable is not None and self.dsx3farendcurrenttable.has_operation()) or
            (self.dsx3farendintervaltable is not None and self.dsx3farendintervaltable.has_operation()) or
            (self.dsx3farendtotaltable is not None and self.dsx3farendtotaltable.has_operation()) or
            (self.dsx3fractable is not None and self.dsx3fractable.has_operation()) or
            (self.dsx3intervaltable is not None and self.dsx3intervaltable.has_operation()) or
            (self.dsx3totaltable is not None and self.dsx3totaltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "DS3-MIB:DS3-MIB" + path_buffer

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

        if (child_yang_name == "dsx3ConfigTable"):
            if (self.dsx3configtable is None):
                self.dsx3configtable = Ds3Mib.Dsx3Configtable()
                self.dsx3configtable.parent = self
                self._children_name_map["dsx3configtable"] = "dsx3ConfigTable"
            return self.dsx3configtable

        if (child_yang_name == "dsx3CurrentTable"):
            if (self.dsx3currenttable is None):
                self.dsx3currenttable = Ds3Mib.Dsx3Currenttable()
                self.dsx3currenttable.parent = self
                self._children_name_map["dsx3currenttable"] = "dsx3CurrentTable"
            return self.dsx3currenttable

        if (child_yang_name == "dsx3FarEndConfigTable"):
            if (self.dsx3farendconfigtable is None):
                self.dsx3farendconfigtable = Ds3Mib.Dsx3Farendconfigtable()
                self.dsx3farendconfigtable.parent = self
                self._children_name_map["dsx3farendconfigtable"] = "dsx3FarEndConfigTable"
            return self.dsx3farendconfigtable

        if (child_yang_name == "dsx3FarEndCurrentTable"):
            if (self.dsx3farendcurrenttable is None):
                self.dsx3farendcurrenttable = Ds3Mib.Dsx3Farendcurrenttable()
                self.dsx3farendcurrenttable.parent = self
                self._children_name_map["dsx3farendcurrenttable"] = "dsx3FarEndCurrentTable"
            return self.dsx3farendcurrenttable

        if (child_yang_name == "dsx3FarEndIntervalTable"):
            if (self.dsx3farendintervaltable is None):
                self.dsx3farendintervaltable = Ds3Mib.Dsx3Farendintervaltable()
                self.dsx3farendintervaltable.parent = self
                self._children_name_map["dsx3farendintervaltable"] = "dsx3FarEndIntervalTable"
            return self.dsx3farendintervaltable

        if (child_yang_name == "dsx3FarEndTotalTable"):
            if (self.dsx3farendtotaltable is None):
                self.dsx3farendtotaltable = Ds3Mib.Dsx3Farendtotaltable()
                self.dsx3farendtotaltable.parent = self
                self._children_name_map["dsx3farendtotaltable"] = "dsx3FarEndTotalTable"
            return self.dsx3farendtotaltable

        if (child_yang_name == "dsx3FracTable"):
            if (self.dsx3fractable is None):
                self.dsx3fractable = Ds3Mib.Dsx3Fractable()
                self.dsx3fractable.parent = self
                self._children_name_map["dsx3fractable"] = "dsx3FracTable"
            return self.dsx3fractable

        if (child_yang_name == "dsx3IntervalTable"):
            if (self.dsx3intervaltable is None):
                self.dsx3intervaltable = Ds3Mib.Dsx3Intervaltable()
                self.dsx3intervaltable.parent = self
                self._children_name_map["dsx3intervaltable"] = "dsx3IntervalTable"
            return self.dsx3intervaltable

        if (child_yang_name == "dsx3TotalTable"):
            if (self.dsx3totaltable is None):
                self.dsx3totaltable = Ds3Mib.Dsx3Totaltable()
                self.dsx3totaltable.parent = self
                self._children_name_map["dsx3totaltable"] = "dsx3TotalTable"
            return self.dsx3totaltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dsx3ConfigTable" or name == "dsx3CurrentTable" or name == "dsx3FarEndConfigTable" or name == "dsx3FarEndCurrentTable" or name == "dsx3FarEndIntervalTable" or name == "dsx3FarEndTotalTable" or name == "dsx3FracTable" or name == "dsx3IntervalTable" or name == "dsx3TotalTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ds3Mib()
        return self._top_entity

