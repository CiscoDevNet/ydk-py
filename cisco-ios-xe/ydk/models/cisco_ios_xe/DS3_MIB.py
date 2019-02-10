""" DS3_MIB 

The is the MIB module that describes
DS3 and E3 interfaces objects.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class DS3MIB(Entity):
    """
    
    
    .. attribute:: dsx3configtable
    
    	The DS3/E3 Configuration table
    	**type**\:  :py:class:`Dsx3ConfigTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3currenttable
    
    	The DS3/E3 current table contains various statistics being collected for the current 15 minute interval
    	**type**\:  :py:class:`Dsx3CurrentTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3CurrentTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3intervaltable
    
    	The DS3/E3 Interval Table contains various statistics collected by each DS3/E3 Interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals.  Each row in this table represents one such interval (identified by dsx3IntervalNumber) and for one specific interface (identifed by dsx3IntervalIndex)
    	**type**\:  :py:class:`Dsx3IntervalTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3IntervalTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3totaltable
    
    	The DS3/E3 Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\:  :py:class:`Dsx3TotalTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3TotalTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3farendconfigtable
    
    	The DS3 Far End Configuration Table contains configuration information reported in the C\-bits from the remote end
    	**type**\:  :py:class:`Dsx3FarEndConfigTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndConfigTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3farendcurrenttable
    
    	The DS3 Far End Current table contains various statistics being collected for the current 15 minute interval.  The statistics are collected from the far end block error code within the C\- bits
    	**type**\:  :py:class:`Dsx3FarEndCurrentTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndCurrentTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3farendintervaltable
    
    	The DS3 Far End Interval Table contains various statistics collected by each DS3 interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals
    	**type**\:  :py:class:`Dsx3FarEndIntervalTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndIntervalTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3farendtotaltable
    
    	The DS3 Far End Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\:  :py:class:`Dsx3FarEndTotalTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndTotalTable>`
    
    	**config**\: False
    
    .. attribute:: dsx3fractable
    
    	This table is deprecated in favour of using ifStackTable.  Implementation of this table was optional.  It was designed for those systems dividing a DS3/E3 into channels containing different data streams that are of local interest.  The DS3/E3 fractional table identifies which DS3/E3 channels associated with a CSU are being used to support a logical interface, i.e., an entry in the interfaces table from the Internet\- standard MIB.  For example, consider a DS3 device with 4 high speed links carrying router traffic, a feed for voice, a feed for video, and a synchronous channel for a non\-routed protocol.  We might describe the allocation of channels, in the dsx3FracTable, as follows\: dsx3FracIfIndex.2. 1 = 3  dsx3FracIfIndex.2.15 = 4 dsx3FracIfIndex.2. 2 = 3  dsx3FracIfIndex.2.16 = 6 dsx3FracIfIndex.2. 3 = 3  dsx3FracIfIndex.2.17 = 6 dsx3FracIfIndex.2. 4 = 3  dsx3FracIfIndex.2.18 = 6 dsx3FracIfIndex.2. 5 = 3  dsx3FracIfIndex.2.19 = 6 dsx3FracIfIndex.2. 6 = 3  dsx3FracIfIndex.2.20 = 6 dsx3FracIfIndex.2. 7 = 4  dsx3FracIfIndex.2.21 = 6 dsx3FracIfIndex.2. 8 = 4  dsx3FracIfIndex.2.22 = 6 dsx3FracIfIndex.2. 9 = 4  dsx3FracIfIndex.2.23 = 6 dsx3FracIfIndex.2.10 = 4  dsx3FracIfIndex.2.24 = 6 dsx3FracIfIndex.2.11 = 4  dsx3FracIfIndex.2.25 = 6 dsx3FracIfIndex.2.12 = 5  dsx3FracIfIndex.2.26 = 6 dsx3FracIfIndex.2.13 = 5  dsx3FracIfIndex.2.27 = 6 dsx3FracIfIndex.2.14 = 5  dsx3FracIfIndex.2.28 = 6 For dsx3M23, dsx3 SYNTRAN, dsx3CbitParity, and dsx3ClearChannel  there are 28 legal channels, numbered 1 throug h 28.  For e3Framed there are 16 legal channels, numbered 1 through 16.  The channels (1..16) correspond directly to the equivalently numbered time\-slots
    	**type**\:  :py:class:`Dsx3FracTable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FracTable>`
    
    	**config**\: False
    
    	**status**\: deprecated
    
    

    """

    _prefix = 'DS3-MIB'
    _revision = '1998-08-01'

    def __init__(self):
        super(DS3MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DS3-MIB"
        self.yang_parent_name = "DS3-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("dsx3ConfigTable", ("dsx3configtable", DS3MIB.Dsx3ConfigTable)), ("dsx3CurrentTable", ("dsx3currenttable", DS3MIB.Dsx3CurrentTable)), ("dsx3IntervalTable", ("dsx3intervaltable", DS3MIB.Dsx3IntervalTable)), ("dsx3TotalTable", ("dsx3totaltable", DS3MIB.Dsx3TotalTable)), ("dsx3FarEndConfigTable", ("dsx3farendconfigtable", DS3MIB.Dsx3FarEndConfigTable)), ("dsx3FarEndCurrentTable", ("dsx3farendcurrenttable", DS3MIB.Dsx3FarEndCurrentTable)), ("dsx3FarEndIntervalTable", ("dsx3farendintervaltable", DS3MIB.Dsx3FarEndIntervalTable)), ("dsx3FarEndTotalTable", ("dsx3farendtotaltable", DS3MIB.Dsx3FarEndTotalTable)), ("dsx3FracTable", ("dsx3fractable", DS3MIB.Dsx3FracTable))])
        self._leafs = OrderedDict()

        self.dsx3configtable = DS3MIB.Dsx3ConfigTable()
        self.dsx3configtable.parent = self
        self._children_name_map["dsx3configtable"] = "dsx3ConfigTable"

        self.dsx3currenttable = DS3MIB.Dsx3CurrentTable()
        self.dsx3currenttable.parent = self
        self._children_name_map["dsx3currenttable"] = "dsx3CurrentTable"

        self.dsx3intervaltable = DS3MIB.Dsx3IntervalTable()
        self.dsx3intervaltable.parent = self
        self._children_name_map["dsx3intervaltable"] = "dsx3IntervalTable"

        self.dsx3totaltable = DS3MIB.Dsx3TotalTable()
        self.dsx3totaltable.parent = self
        self._children_name_map["dsx3totaltable"] = "dsx3TotalTable"

        self.dsx3farendconfigtable = DS3MIB.Dsx3FarEndConfigTable()
        self.dsx3farendconfigtable.parent = self
        self._children_name_map["dsx3farendconfigtable"] = "dsx3FarEndConfigTable"

        self.dsx3farendcurrenttable = DS3MIB.Dsx3FarEndCurrentTable()
        self.dsx3farendcurrenttable.parent = self
        self._children_name_map["dsx3farendcurrenttable"] = "dsx3FarEndCurrentTable"

        self.dsx3farendintervaltable = DS3MIB.Dsx3FarEndIntervalTable()
        self.dsx3farendintervaltable.parent = self
        self._children_name_map["dsx3farendintervaltable"] = "dsx3FarEndIntervalTable"

        self.dsx3farendtotaltable = DS3MIB.Dsx3FarEndTotalTable()
        self.dsx3farendtotaltable.parent = self
        self._children_name_map["dsx3farendtotaltable"] = "dsx3FarEndTotalTable"

        self.dsx3fractable = DS3MIB.Dsx3FracTable()
        self.dsx3fractable.parent = self
        self._children_name_map["dsx3fractable"] = "dsx3FracTable"
        self._segment_path = lambda: "DS3-MIB:DS3-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DS3MIB, [], name, value)


    class Dsx3ConfigTable(Entity):
        """
        The DS3/E3 Configuration table.
        
        .. attribute:: dsx3configentry
        
        	An entry in the DS3/E3 Configuration table
        	**type**\: list of  		 :py:class:`Dsx3ConfigEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3ConfigTable, self).__init__()

            self.yang_name = "dsx3ConfigTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3ConfigEntry", ("dsx3configentry", DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry))])
            self._leafs = OrderedDict()

            self.dsx3configentry = YList(self)
            self._segment_path = lambda: "dsx3ConfigTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3ConfigTable, [], name, value)


        class Dsx3ConfigEntry(Entity):
            """
            An entry in the DS3/E3 Configuration table.
            
            .. attribute:: dsx3lineindex  (key)
            
            	This object should be made equal to ifIndex.  The next paragraph describes its previous usage. Making the object equal to ifIndex allows propoer use of ifStackTable.  Previously, this object was the identifier of a DS3/E3 Interface on a managed device.  If there is an ifEntry that is directly associated with this and only this DS3/E3 interface, it should have the same value as ifIndex.  Otherwise, number the dsx3LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3ifindex
            
            	This value for this object is equal to the value of ifIndex from the Interfaces table of MIB II (RFC 1213)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: dsx3timeelapsed
            
            	The number of seconds that have elapsed since the beginning of the near end current error\- measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 0..899
            
            	**config**\: False
            
            .. attribute:: dsx3validintervals
            
            	The number of previous near end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute near end intervals since the interface has been online.  In the case where the agent is a proxy, it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            .. attribute:: dsx3linetype
            
            	This variable indicates the variety of DS3 C\-bit or E3 application implementing this interface. The type of interface affects the interpretation of the usage and error statistics.  The rate of DS3 is 44.736 Mbps and E3 is 34.368 Mbps.  The dsx3ClearChannel value means that the C\-bits are not used except for sending/receiving AIS. The values, in sequence, describe\:  TITLE\:            SPECIFICATION\: dsx3M23            ANSI T1.107\-1988 [9] dsx3SYNTRAN        ANSI T1.107\-1988 [9] dsx3CbitParity     ANSI T1.107a\-1990 [9a] dsx3ClearChannel   ANSI T1.102\-1987 [8] e3Framed           CCITT G.751 [12] e3Plcp             ETSI T/NA(91)18 [13]
            	**type**\:  :py:class:`Dsx3LineType <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineType>`
            
            	**config**\: False
            
            .. attribute:: dsx3linecoding
            
            	This variable describes the variety of Zero Code Suppression used on this interface, which in turn affects a number of its characteristics.  dsx3B3ZS and e3HDB3 refer to the use of specified patterns of normal bits and bipolar violations which are used to replace sequences of zero bits of a specified length
            	**type**\:  :py:class:`Dsx3LineCoding <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineCoding>`
            
            	**config**\: False
            
            .. attribute:: dsx3sendcode
            
            	This variable indicates what type of code is being sent across the DS3/E3 interface by the device.  (These are optional for E3 interfaces.) Setting this variable causes the interface to begin sending the code requested. The values mean\:     dsx3SendNoCode        sending looped or normal data     dsx3SendLineCode        sending a request for a line loopback     dsx3SendPayloadCode        sending a request for a payload loopback        (i.e., all DS1/E1s in a DS3/E3 frame)     dsx3SendResetCode        sending a loopback deactivation request     dsx3SendDS1LoopCode        requesting to loopback a particular DS1/E1        within a DS3/E3 frame.  The DS1/E1 is        indicated in dsx3Ds1ForRemoteLoop.     dsx3SendTestPattern        sending a test pattern
            	**type**\:  :py:class:`Dsx3SendCode <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3SendCode>`
            
            	**config**\: False
            
            .. attribute:: dsx3circuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: dsx3loopbackconfig
            
            	This variable represents the desired loopback configuration of the DS3/E3 interface.  The values mean\:  dsx3NoLoop   Not in the loopback state.  A device that is   not capable of performing a loopback on   the interface shall always return this as   its value.  dsx3PayloadLoop   The received signal at this interface is looped   through the device.  Typically the received signal   is looped back for retransmission after it has   passed through the device's framing function.  dsx3LineLoop   The received signal at this interface does not   go through the device (minimum penetration) but   is looped back out.  dsx3OtherLoop   Loopbacks that are not defined here.  dsx3InwardLoop   The sent signal at this interface is looped back   through the device.  dsx3DualLoop   Both dsx1LineLoop and dsx1InwardLoop will be   active simultaneously
            	**type**\:  :py:class:`Dsx3LoopbackConfig <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LoopbackConfig>`
            
            	**config**\: False
            
            .. attribute:: dsx3linestatus
            
            	This variable indicates the Line Status of the interface.  It contains loopback state information and failure state information.  The dsx3LineStatus is a bit map represented as a sum, therefore, it can represent multiple failures and a loopback (see dsx3LoopbackConfig object for the type of loopback) simultaneously.  The dsx3NoAlarm must be set if and only if no other flag is set.  If the dsx3loopbackState bit is set, the loopback in effect can be determined from the dsx3loopbackConfig object. The various bit positions are\: 1     dsx3NoAlarm         No alarm present 2     dsx3RcvRAIFailure   Receiving Yellow/Remote                  Alarm Indication 4     dsx3XmitRAIAlarm    Transmitting Yellow/Remote                  Alarm Indication 8     dsx3RcvAIS          Receiving AIS failure state 16     dsx3XmitAIS         Transmitting AIS 32     dsx3LOF             Receiving LOF failure state 64     dsx3LOS             Receiving LOS failure state 128     dsx3LoopbackState   Looping the received signal 256     dsx3RcvTestCode     Receiving a Test Pattern 512     dsx3OtherFailure    any line status not defined                  here 1024     dsx3UnavailSigState Near End in Unavailable Signal                  State 2048     dsx3NetEquipOOS     Carrier Equipment Out of Service
            	**type**\: int
            
            	**range:** 1..4095
            
            	**config**\: False
            
            .. attribute:: dsx3transmitclocksource
            
            	The source of Transmit Clock.  loopTiming indicates that the recovered receive clock is used as the transmit clock.  localTiming indicates that a local clock source is used or that an external clock is attached to the box containing the interface.  throughTiming indicates that transmit clock is derived from the recovered receive clock of another DS3 interface
            	**type**\:  :py:class:`Dsx3TransmitClockSource <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3TransmitClockSource>`
            
            	**config**\: False
            
            .. attribute:: dsx3invalidintervals
            
            	The number of intervals in the range from 0 to dsx3ValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            .. attribute:: dsx3linelength
            
            	The length of the ds3 line in meters.  This object provides information for line build out circuitry if it exists and can use this object to adjust the line build out
            	**type**\: int
            
            	**range:** 0..64000
            
            	**config**\: False
            
            	**units**\: meters
            
            .. attribute:: dsx3linestatuslastchange
            
            	The value of MIB II's sysUpTime object at the time this DS3/E3 entered its current line status state.  If the current state was entered prior to the last re\-initialization of the proxy\-agent, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3linestatuschangetrapenable
            
            	Indicates whether dsx3LineStatusChange traps should be generated for this interface
            	**type**\:  :py:class:`Dsx3LineStatusChangeTrapEnable <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineStatusChangeTrapEnable>`
            
            	**config**\: False
            
            .. attribute:: dsx3loopbackstatus
            
            	This variable represents the current state of the loopback on the DS3 interface.  It contains information about loopbacks established by a manager and remotely from the far end.  The dsx3LoopbackStatus is a bit map represented as a sum, therefore is can represent multiple loopbacks simultaneously.  The various bit positions are\:  1  dsx3NoLoopback  2  dsx3NearEndPayloadLoopback  4  dsx3NearEndLineLoopback  8  dsx3NearEndOtherLoopback 16  dsx3NearEndInwardLoopback 32  dsx3FarEndPayloadLoopback 64  dsx3FarEndLineLoopback
            	**type**\: int
            
            	**range:** 1..127
            
            	**config**\: False
            
            .. attribute:: dsx3channelization
            
            	Indicates whether this ds3/e3 is channelized or unchannelized.  The value of enabledDs1 indicates that this is a DS3 channelized into DS1s.  The value of enabledDs3 indicated that this is a DS3 channelized into DS2s.  Setting this object will cause the creation or deletion of DS2 or DS1 entries in the ifTable.  
            	**type**\:  :py:class:`Dsx3Channelization <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3Channelization>`
            
            	**config**\: False
            
            .. attribute:: dsx3ds1forremoteloop
            
            	Indicates which ds1/e1 on this ds3/e3 will be indicated in the remote ds1 loopback request.  A value of 0 means no DS1 will be looped.  A value of 29 means all ds1s/e1s will be looped
            	**type**\: int
            
            	**range:** 0..29
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry, self).__init__()

                self.yang_name = "dsx3ConfigEntry"
                self.yang_parent_name = "dsx3ConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3lineindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3lineindex', (YLeaf(YType.int32, 'dsx3LineIndex'), ['int'])),
                    ('dsx3ifindex', (YLeaf(YType.int32, 'dsx3IfIndex'), ['int'])),
                    ('dsx3timeelapsed', (YLeaf(YType.int32, 'dsx3TimeElapsed'), ['int'])),
                    ('dsx3validintervals', (YLeaf(YType.int32, 'dsx3ValidIntervals'), ['int'])),
                    ('dsx3linetype', (YLeaf(YType.enumeration, 'dsx3LineType'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineType')])),
                    ('dsx3linecoding', (YLeaf(YType.enumeration, 'dsx3LineCoding'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineCoding')])),
                    ('dsx3sendcode', (YLeaf(YType.enumeration, 'dsx3SendCode'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3SendCode')])),
                    ('dsx3circuitidentifier', (YLeaf(YType.str, 'dsx3CircuitIdentifier'), ['str'])),
                    ('dsx3loopbackconfig', (YLeaf(YType.enumeration, 'dsx3LoopbackConfig'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LoopbackConfig')])),
                    ('dsx3linestatus', (YLeaf(YType.int32, 'dsx3LineStatus'), ['int'])),
                    ('dsx3transmitclocksource', (YLeaf(YType.enumeration, 'dsx3TransmitClockSource'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3TransmitClockSource')])),
                    ('dsx3invalidintervals', (YLeaf(YType.int32, 'dsx3InvalidIntervals'), ['int'])),
                    ('dsx3linelength', (YLeaf(YType.int32, 'dsx3LineLength'), ['int'])),
                    ('dsx3linestatuslastchange', (YLeaf(YType.uint32, 'dsx3LineStatusLastChange'), ['int'])),
                    ('dsx3linestatuschangetrapenable', (YLeaf(YType.enumeration, 'dsx3LineStatusChangeTrapEnable'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineStatusChangeTrapEnable')])),
                    ('dsx3loopbackstatus', (YLeaf(YType.int32, 'dsx3LoopbackStatus'), ['int'])),
                    ('dsx3channelization', (YLeaf(YType.enumeration, 'dsx3Channelization'), [('ydk.models.cisco_ios_xe.DS3_MIB', 'DS3MIB', 'Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3Channelization')])),
                    ('dsx3ds1forremoteloop', (YLeaf(YType.int32, 'dsx3Ds1ForRemoteLoop'), ['int'])),
                ])
                self.dsx3lineindex = None
                self.dsx3ifindex = None
                self.dsx3timeelapsed = None
                self.dsx3validintervals = None
                self.dsx3linetype = None
                self.dsx3linecoding = None
                self.dsx3sendcode = None
                self.dsx3circuitidentifier = None
                self.dsx3loopbackconfig = None
                self.dsx3linestatus = None
                self.dsx3transmitclocksource = None
                self.dsx3invalidintervals = None
                self.dsx3linelength = None
                self.dsx3linestatuslastchange = None
                self.dsx3linestatuschangetrapenable = None
                self.dsx3loopbackstatus = None
                self.dsx3channelization = None
                self.dsx3ds1forremoteloop = None
                self._segment_path = lambda: "dsx3ConfigEntry" + "[dsx3LineIndex='" + str(self.dsx3lineindex) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3ConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry, ['dsx3lineindex', 'dsx3ifindex', 'dsx3timeelapsed', 'dsx3validintervals', 'dsx3linetype', 'dsx3linecoding', 'dsx3sendcode', 'dsx3circuitidentifier', 'dsx3loopbackconfig', 'dsx3linestatus', 'dsx3transmitclocksource', 'dsx3invalidintervals', 'dsx3linelength', 'dsx3linestatuslastchange', 'dsx3linestatuschangetrapenable', 'dsx3loopbackstatus', 'dsx3channelization', 'dsx3ds1forremoteloop'], name, value)

            class Dsx3Channelization(Enum):
                """
                Dsx3Channelization (Enum Class)

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


            class Dsx3LineCoding(Enum):
                """
                Dsx3LineCoding (Enum Class)

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


            class Dsx3LineStatusChangeTrapEnable(Enum):
                """
                Dsx3LineStatusChangeTrapEnable (Enum Class)

                Indicates whether dsx3LineStatusChange traps

                should be generated for this interface.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Dsx3LineType(Enum):
                """
                Dsx3LineType (Enum Class)

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


            class Dsx3LoopbackConfig(Enum):
                """
                Dsx3LoopbackConfig (Enum Class)

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


            class Dsx3SendCode(Enum):
                """
                Dsx3SendCode (Enum Class)

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


            class Dsx3TransmitClockSource(Enum):
                """
                Dsx3TransmitClockSource (Enum Class)

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





    class Dsx3CurrentTable(Entity):
        """
        The DS3/E3 current table contains various
        statistics being collected for the current 15
        minute interval.
        
        .. attribute:: dsx3currententry
        
        	An entry in the DS3/E3 Current table
        	**type**\: list of  		 :py:class:`Dsx3CurrentEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3CurrentTable.Dsx3CurrentEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3CurrentTable, self).__init__()

            self.yang_name = "dsx3CurrentTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3CurrentEntry", ("dsx3currententry", DS3MIB.Dsx3CurrentTable.Dsx3CurrentEntry))])
            self._leafs = OrderedDict()

            self.dsx3currententry = YList(self)
            self._segment_path = lambda: "dsx3CurrentTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3CurrentTable, [], name, value)


        class Dsx3CurrentEntry(Entity):
            """
            An entry in the DS3/E3 Current table.
            
            .. attribute:: dsx3currentindex  (key)
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3currentpess
            
            	The counter associated with the number of P\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentuass
            
            	The counter associated with the number of Unavailable Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentlcvs
            
            	The counter associated with the number of Line Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentpcvs
            
            	The counter associated with the number of P\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentless
            
            	The number of Line Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentccvs
            
            	The number of C\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentcess
            
            	The number of C\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3currentcsess
            
            	The number of C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3CurrentTable.Dsx3CurrentEntry, self).__init__()

                self.yang_name = "dsx3CurrentEntry"
                self.yang_parent_name = "dsx3CurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3currentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3currentindex', (YLeaf(YType.int32, 'dsx3CurrentIndex'), ['int'])),
                    ('dsx3currentpess', (YLeaf(YType.uint32, 'dsx3CurrentPESs'), ['int'])),
                    ('dsx3currentpsess', (YLeaf(YType.uint32, 'dsx3CurrentPSESs'), ['int'])),
                    ('dsx3currentsefss', (YLeaf(YType.uint32, 'dsx3CurrentSEFSs'), ['int'])),
                    ('dsx3currentuass', (YLeaf(YType.uint32, 'dsx3CurrentUASs'), ['int'])),
                    ('dsx3currentlcvs', (YLeaf(YType.uint32, 'dsx3CurrentLCVs'), ['int'])),
                    ('dsx3currentpcvs', (YLeaf(YType.uint32, 'dsx3CurrentPCVs'), ['int'])),
                    ('dsx3currentless', (YLeaf(YType.uint32, 'dsx3CurrentLESs'), ['int'])),
                    ('dsx3currentccvs', (YLeaf(YType.uint32, 'dsx3CurrentCCVs'), ['int'])),
                    ('dsx3currentcess', (YLeaf(YType.uint32, 'dsx3CurrentCESs'), ['int'])),
                    ('dsx3currentcsess', (YLeaf(YType.uint32, 'dsx3CurrentCSESs'), ['int'])),
                ])
                self.dsx3currentindex = None
                self.dsx3currentpess = None
                self.dsx3currentpsess = None
                self.dsx3currentsefss = None
                self.dsx3currentuass = None
                self.dsx3currentlcvs = None
                self.dsx3currentpcvs = None
                self.dsx3currentless = None
                self.dsx3currentccvs = None
                self.dsx3currentcess = None
                self.dsx3currentcsess = None
                self._segment_path = lambda: "dsx3CurrentEntry" + "[dsx3CurrentIndex='" + str(self.dsx3currentindex) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3CurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3CurrentTable.Dsx3CurrentEntry, ['dsx3currentindex', 'dsx3currentpess', 'dsx3currentpsess', 'dsx3currentsefss', 'dsx3currentuass', 'dsx3currentlcvs', 'dsx3currentpcvs', 'dsx3currentless', 'dsx3currentccvs', 'dsx3currentcess', 'dsx3currentcsess'], name, value)




    class Dsx3IntervalTable(Entity):
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
        	**type**\: list of  		 :py:class:`Dsx3IntervalEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3IntervalTable.Dsx3IntervalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3IntervalTable, self).__init__()

            self.yang_name = "dsx3IntervalTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3IntervalEntry", ("dsx3intervalentry", DS3MIB.Dsx3IntervalTable.Dsx3IntervalEntry))])
            self._leafs = OrderedDict()

            self.dsx3intervalentry = YList(self)
            self._segment_path = lambda: "dsx3IntervalTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3IntervalTable, [], name, value)


        class Dsx3IntervalEntry(Entity):
            """
            An entry in the DS3/E3 Interval table.
            
            .. attribute:: dsx3intervalindex  (key)
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3intervalnumber  (key)
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\: int
            
            	**range:** 1..96
            
            	**config**\: False
            
            .. attribute:: dsx3intervalpess
            
            	The counter associated with the number of P\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervaluass
            
            	The counter associated with the number of Unavailable Seconds.  This object may decrease if the occurance of unavailable seconds occurs across an inteval boundary
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervallcvs
            
            	The counter associated with the number of Line Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalpcvs
            
            	The counter associated with the number of P\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalless
            
            	The number of Line Errored  Seconds  (BPVs  or illegal  zero  sequences)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalccvs
            
            	The number of C\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalcess
            
            	The number of C\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalcsess
            
            	The number of C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3intervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3IntervalTable.Dsx3IntervalEntry, self).__init__()

                self.yang_name = "dsx3IntervalEntry"
                self.yang_parent_name = "dsx3IntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3intervalindex','dsx3intervalnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3intervalindex', (YLeaf(YType.int32, 'dsx3IntervalIndex'), ['int'])),
                    ('dsx3intervalnumber', (YLeaf(YType.int32, 'dsx3IntervalNumber'), ['int'])),
                    ('dsx3intervalpess', (YLeaf(YType.uint32, 'dsx3IntervalPESs'), ['int'])),
                    ('dsx3intervalpsess', (YLeaf(YType.uint32, 'dsx3IntervalPSESs'), ['int'])),
                    ('dsx3intervalsefss', (YLeaf(YType.uint32, 'dsx3IntervalSEFSs'), ['int'])),
                    ('dsx3intervaluass', (YLeaf(YType.uint32, 'dsx3IntervalUASs'), ['int'])),
                    ('dsx3intervallcvs', (YLeaf(YType.uint32, 'dsx3IntervalLCVs'), ['int'])),
                    ('dsx3intervalpcvs', (YLeaf(YType.uint32, 'dsx3IntervalPCVs'), ['int'])),
                    ('dsx3intervalless', (YLeaf(YType.uint32, 'dsx3IntervalLESs'), ['int'])),
                    ('dsx3intervalccvs', (YLeaf(YType.uint32, 'dsx3IntervalCCVs'), ['int'])),
                    ('dsx3intervalcess', (YLeaf(YType.uint32, 'dsx3IntervalCESs'), ['int'])),
                    ('dsx3intervalcsess', (YLeaf(YType.uint32, 'dsx3IntervalCSESs'), ['int'])),
                    ('dsx3intervalvaliddata', (YLeaf(YType.boolean, 'dsx3IntervalValidData'), ['bool'])),
                ])
                self.dsx3intervalindex = None
                self.dsx3intervalnumber = None
                self.dsx3intervalpess = None
                self.dsx3intervalpsess = None
                self.dsx3intervalsefss = None
                self.dsx3intervaluass = None
                self.dsx3intervallcvs = None
                self.dsx3intervalpcvs = None
                self.dsx3intervalless = None
                self.dsx3intervalccvs = None
                self.dsx3intervalcess = None
                self.dsx3intervalcsess = None
                self.dsx3intervalvaliddata = None
                self._segment_path = lambda: "dsx3IntervalEntry" + "[dsx3IntervalIndex='" + str(self.dsx3intervalindex) + "']" + "[dsx3IntervalNumber='" + str(self.dsx3intervalnumber) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3IntervalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3IntervalTable.Dsx3IntervalEntry, ['dsx3intervalindex', 'dsx3intervalnumber', 'dsx3intervalpess', 'dsx3intervalpsess', 'dsx3intervalsefss', 'dsx3intervaluass', 'dsx3intervallcvs', 'dsx3intervalpcvs', 'dsx3intervalless', 'dsx3intervalccvs', 'dsx3intervalcess', 'dsx3intervalcsess', 'dsx3intervalvaliddata'], name, value)




    class Dsx3TotalTable(Entity):
        """
        The DS3/E3 Total Table contains the cumulative
        sum of the various statistics for the 24 hour
        period preceding the current interval.
        
        .. attribute:: dsx3totalentry
        
        	An entry in the DS3/E3 Total table
        	**type**\: list of  		 :py:class:`Dsx3TotalEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3TotalTable.Dsx3TotalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3TotalTable, self).__init__()

            self.yang_name = "dsx3TotalTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3TotalEntry", ("dsx3totalentry", DS3MIB.Dsx3TotalTable.Dsx3TotalEntry))])
            self._leafs = OrderedDict()

            self.dsx3totalentry = YList(self)
            self._segment_path = lambda: "dsx3TotalTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3TotalTable, [], name, value)


        class Dsx3TotalEntry(Entity):
            """
            An entry in the DS3/E3 Total table.
            
            .. attribute:: dsx3totalindex  (key)
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3totalpess
            
            	The counter associated with the number of P\-bit Errored Seconds, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds, encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totaluass
            
            	The counter associated with the number of Unavailable Seconds, encountered by a DS3 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totallcvs
            
            	The counter associated with the number of Line Coding Violations encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalpcvs
            
            	The counter associated with the number of P\-bit Coding Violations, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalless
            
            	The number of Line Errored  Seconds  (BPVs  or illegal  zero  sequences) encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalccvs
            
            	The number of C\-bit Coding Violations encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalcess
            
            	The number of C\-bit Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3totalcsess
            
            	The number of C\-bit Severely Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3TotalTable.Dsx3TotalEntry, self).__init__()

                self.yang_name = "dsx3TotalEntry"
                self.yang_parent_name = "dsx3TotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3totalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3totalindex', (YLeaf(YType.int32, 'dsx3TotalIndex'), ['int'])),
                    ('dsx3totalpess', (YLeaf(YType.uint32, 'dsx3TotalPESs'), ['int'])),
                    ('dsx3totalpsess', (YLeaf(YType.uint32, 'dsx3TotalPSESs'), ['int'])),
                    ('dsx3totalsefss', (YLeaf(YType.uint32, 'dsx3TotalSEFSs'), ['int'])),
                    ('dsx3totaluass', (YLeaf(YType.uint32, 'dsx3TotalUASs'), ['int'])),
                    ('dsx3totallcvs', (YLeaf(YType.uint32, 'dsx3TotalLCVs'), ['int'])),
                    ('dsx3totalpcvs', (YLeaf(YType.uint32, 'dsx3TotalPCVs'), ['int'])),
                    ('dsx3totalless', (YLeaf(YType.uint32, 'dsx3TotalLESs'), ['int'])),
                    ('dsx3totalccvs', (YLeaf(YType.uint32, 'dsx3TotalCCVs'), ['int'])),
                    ('dsx3totalcess', (YLeaf(YType.uint32, 'dsx3TotalCESs'), ['int'])),
                    ('dsx3totalcsess', (YLeaf(YType.uint32, 'dsx3TotalCSESs'), ['int'])),
                ])
                self.dsx3totalindex = None
                self.dsx3totalpess = None
                self.dsx3totalpsess = None
                self.dsx3totalsefss = None
                self.dsx3totaluass = None
                self.dsx3totallcvs = None
                self.dsx3totalpcvs = None
                self.dsx3totalless = None
                self.dsx3totalccvs = None
                self.dsx3totalcess = None
                self.dsx3totalcsess = None
                self._segment_path = lambda: "dsx3TotalEntry" + "[dsx3TotalIndex='" + str(self.dsx3totalindex) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3TotalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3TotalTable.Dsx3TotalEntry, ['dsx3totalindex', 'dsx3totalpess', 'dsx3totalpsess', 'dsx3totalsefss', 'dsx3totaluass', 'dsx3totallcvs', 'dsx3totalpcvs', 'dsx3totalless', 'dsx3totalccvs', 'dsx3totalcess', 'dsx3totalcsess'], name, value)




    class Dsx3FarEndConfigTable(Entity):
        """
        The DS3 Far End Configuration Table contains
        configuration information reported in the C\-bits
        from the remote end.
        
        .. attribute:: dsx3farendconfigentry
        
        	An entry in the DS3 Far End Configuration table
        	**type**\: list of  		 :py:class:`Dsx3FarEndConfigEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndConfigTable.Dsx3FarEndConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3FarEndConfigTable, self).__init__()

            self.yang_name = "dsx3FarEndConfigTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3FarEndConfigEntry", ("dsx3farendconfigentry", DS3MIB.Dsx3FarEndConfigTable.Dsx3FarEndConfigEntry))])
            self._leafs = OrderedDict()

            self.dsx3farendconfigentry = YList(self)
            self._segment_path = lambda: "dsx3FarEndConfigTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3FarEndConfigTable, [], name, value)


        class Dsx3FarEndConfigEntry(Entity):
            """
            An entry in the DS3 Far End Configuration table.
            
            .. attribute:: dsx3farendlineindex  (key)
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3farendequipcode
            
            	This is the Far End Equipment Identification code that describes the specific piece of equipment. It is sent within the Path Identification Message
            	**type**\: str
            
            	**length:** 0..10
            
            	**config**\: False
            
            .. attribute:: dsx3farendlocationidcode
            
            	This is the Far End Location Identification code that describes the specific location of the equipment.  It is sent within the Path Identification Message
            	**type**\: str
            
            	**length:** 0..11
            
            	**config**\: False
            
            .. attribute:: dsx3farendframeidcode
            
            	This is the Far End Frame Identification code that identifies where the equipment is located within a building at a given location.  It is sent within the Path Identification Message
            	**type**\: str
            
            	**length:** 0..10
            
            	**config**\: False
            
            .. attribute:: dsx3farendunitcode
            
            	This is the Far End code that identifies the equipment location within a bay.  It is sent within the Path Identification Message
            	**type**\: str
            
            	**length:** 0..6
            
            	**config**\: False
            
            .. attribute:: dsx3farendfacilityidcode
            
            	This code identifies a specific Far End DS3 path. It is sent within the Path Identification Message
            	**type**\: str
            
            	**length:** 0..38
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3FarEndConfigTable.Dsx3FarEndConfigEntry, self).__init__()

                self.yang_name = "dsx3FarEndConfigEntry"
                self.yang_parent_name = "dsx3FarEndConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3farendlineindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3farendlineindex', (YLeaf(YType.int32, 'dsx3FarEndLineIndex'), ['int'])),
                    ('dsx3farendequipcode', (YLeaf(YType.str, 'dsx3FarEndEquipCode'), ['str'])),
                    ('dsx3farendlocationidcode', (YLeaf(YType.str, 'dsx3FarEndLocationIDCode'), ['str'])),
                    ('dsx3farendframeidcode', (YLeaf(YType.str, 'dsx3FarEndFrameIDCode'), ['str'])),
                    ('dsx3farendunitcode', (YLeaf(YType.str, 'dsx3FarEndUnitCode'), ['str'])),
                    ('dsx3farendfacilityidcode', (YLeaf(YType.str, 'dsx3FarEndFacilityIDCode'), ['str'])),
                ])
                self.dsx3farendlineindex = None
                self.dsx3farendequipcode = None
                self.dsx3farendlocationidcode = None
                self.dsx3farendframeidcode = None
                self.dsx3farendunitcode = None
                self.dsx3farendfacilityidcode = None
                self._segment_path = lambda: "dsx3FarEndConfigEntry" + "[dsx3FarEndLineIndex='" + str(self.dsx3farendlineindex) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3FarEndConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3FarEndConfigTable.Dsx3FarEndConfigEntry, ['dsx3farendlineindex', 'dsx3farendequipcode', 'dsx3farendlocationidcode', 'dsx3farendframeidcode', 'dsx3farendunitcode', 'dsx3farendfacilityidcode'], name, value)




    class Dsx3FarEndCurrentTable(Entity):
        """
        The DS3 Far End Current table contains various
        statistics being collected for the current 15
        minute interval.  The statistics are collected
        from the far end block error code within the C\-
        bits.
        
        .. attribute:: dsx3farendcurrententry
        
        	An entry in the DS3 Far End Current table
        	**type**\: list of  		 :py:class:`Dsx3FarEndCurrentEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndCurrentTable.Dsx3FarEndCurrentEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3FarEndCurrentTable, self).__init__()

            self.yang_name = "dsx3FarEndCurrentTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3FarEndCurrentEntry", ("dsx3farendcurrententry", DS3MIB.Dsx3FarEndCurrentTable.Dsx3FarEndCurrentEntry))])
            self._leafs = OrderedDict()

            self.dsx3farendcurrententry = YList(self)
            self._segment_path = lambda: "dsx3FarEndCurrentTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3FarEndCurrentTable, [], name, value)


        class Dsx3FarEndCurrentEntry(Entity):
            """
            An entry in the DS3 Far End Current table.
            
            .. attribute:: dsx3farendcurrentindex  (key)
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3farendtimeelapsed
            
            	The number of seconds that have elapsed since the beginning of the far end current error\-measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 0..899
            
            	**config**\: False
            
            .. attribute:: dsx3farendvalidintervals
            
            	The number of previous far end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute far end intervals since the interface has been online
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            .. attribute:: dsx3farendcurrentcess
            
            	The counter associated with the number of Far Far End C\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendcurrentcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendcurrentccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendcurrentuass
            
            	The counter associated with the number of Far End unavailable seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendinvalidintervals
            
            	The number of intervals in the range from 0 to dsx3FarEndValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3FarEndCurrentTable.Dsx3FarEndCurrentEntry, self).__init__()

                self.yang_name = "dsx3FarEndCurrentEntry"
                self.yang_parent_name = "dsx3FarEndCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3farendcurrentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3farendcurrentindex', (YLeaf(YType.int32, 'dsx3FarEndCurrentIndex'), ['int'])),
                    ('dsx3farendtimeelapsed', (YLeaf(YType.int32, 'dsx3FarEndTimeElapsed'), ['int'])),
                    ('dsx3farendvalidintervals', (YLeaf(YType.int32, 'dsx3FarEndValidIntervals'), ['int'])),
                    ('dsx3farendcurrentcess', (YLeaf(YType.uint32, 'dsx3FarEndCurrentCESs'), ['int'])),
                    ('dsx3farendcurrentcsess', (YLeaf(YType.uint32, 'dsx3FarEndCurrentCSESs'), ['int'])),
                    ('dsx3farendcurrentccvs', (YLeaf(YType.uint32, 'dsx3FarEndCurrentCCVs'), ['int'])),
                    ('dsx3farendcurrentuass', (YLeaf(YType.uint32, 'dsx3FarEndCurrentUASs'), ['int'])),
                    ('dsx3farendinvalidintervals', (YLeaf(YType.int32, 'dsx3FarEndInvalidIntervals'), ['int'])),
                ])
                self.dsx3farendcurrentindex = None
                self.dsx3farendtimeelapsed = None
                self.dsx3farendvalidintervals = None
                self.dsx3farendcurrentcess = None
                self.dsx3farendcurrentcsess = None
                self.dsx3farendcurrentccvs = None
                self.dsx3farendcurrentuass = None
                self.dsx3farendinvalidintervals = None
                self._segment_path = lambda: "dsx3FarEndCurrentEntry" + "[dsx3FarEndCurrentIndex='" + str(self.dsx3farendcurrentindex) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3FarEndCurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3FarEndCurrentTable.Dsx3FarEndCurrentEntry, ['dsx3farendcurrentindex', 'dsx3farendtimeelapsed', 'dsx3farendvalidintervals', 'dsx3farendcurrentcess', 'dsx3farendcurrentcsess', 'dsx3farendcurrentccvs', 'dsx3farendcurrentuass', 'dsx3farendinvalidintervals'], name, value)




    class Dsx3FarEndIntervalTable(Entity):
        """
        The DS3 Far End Interval Table contains various
        statistics collected by each DS3 interface over
        the previous 24 hours of operation.  The past 24
        hours are broken into 96 completed 15 minute
        intervals.
        
        .. attribute:: dsx3farendintervalentry
        
        	An entry in the DS3 Far End Interval table
        	**type**\: list of  		 :py:class:`Dsx3FarEndIntervalEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndIntervalTable.Dsx3FarEndIntervalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3FarEndIntervalTable, self).__init__()

            self.yang_name = "dsx3FarEndIntervalTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3FarEndIntervalEntry", ("dsx3farendintervalentry", DS3MIB.Dsx3FarEndIntervalTable.Dsx3FarEndIntervalEntry))])
            self._leafs = OrderedDict()

            self.dsx3farendintervalentry = YList(self)
            self._segment_path = lambda: "dsx3FarEndIntervalTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3FarEndIntervalTable, [], name, value)


        class Dsx3FarEndIntervalEntry(Entity):
            """
            An entry in the DS3 Far End Interval table.
            
            .. attribute:: dsx3farendintervalindex  (key)
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3farendintervalnumber  (key)
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\: int
            
            	**range:** 1..96
            
            	**config**\: False
            
            .. attribute:: dsx3farendintervalcess
            
            	The counter associated with the number of Far End C\-bit Errored Seconds encountered by a DS3 interface in one of the previous 96, individual 15 minute, intervals. In the case where the agent is a proxy and data is not available, return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendintervalcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendintervalccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendintervaluass
            
            	The counter associated with the number of Far End unavailable seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3FarEndIntervalTable.Dsx3FarEndIntervalEntry, self).__init__()

                self.yang_name = "dsx3FarEndIntervalEntry"
                self.yang_parent_name = "dsx3FarEndIntervalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3farendintervalindex','dsx3farendintervalnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3farendintervalindex', (YLeaf(YType.int32, 'dsx3FarEndIntervalIndex'), ['int'])),
                    ('dsx3farendintervalnumber', (YLeaf(YType.int32, 'dsx3FarEndIntervalNumber'), ['int'])),
                    ('dsx3farendintervalcess', (YLeaf(YType.uint32, 'dsx3FarEndIntervalCESs'), ['int'])),
                    ('dsx3farendintervalcsess', (YLeaf(YType.uint32, 'dsx3FarEndIntervalCSESs'), ['int'])),
                    ('dsx3farendintervalccvs', (YLeaf(YType.uint32, 'dsx3FarEndIntervalCCVs'), ['int'])),
                    ('dsx3farendintervaluass', (YLeaf(YType.uint32, 'dsx3FarEndIntervalUASs'), ['int'])),
                    ('dsx3farendintervalvaliddata', (YLeaf(YType.boolean, 'dsx3FarEndIntervalValidData'), ['bool'])),
                ])
                self.dsx3farendintervalindex = None
                self.dsx3farendintervalnumber = None
                self.dsx3farendintervalcess = None
                self.dsx3farendintervalcsess = None
                self.dsx3farendintervalccvs = None
                self.dsx3farendintervaluass = None
                self.dsx3farendintervalvaliddata = None
                self._segment_path = lambda: "dsx3FarEndIntervalEntry" + "[dsx3FarEndIntervalIndex='" + str(self.dsx3farendintervalindex) + "']" + "[dsx3FarEndIntervalNumber='" + str(self.dsx3farendintervalnumber) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3FarEndIntervalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3FarEndIntervalTable.Dsx3FarEndIntervalEntry, ['dsx3farendintervalindex', 'dsx3farendintervalnumber', 'dsx3farendintervalcess', 'dsx3farendintervalcsess', 'dsx3farendintervalccvs', 'dsx3farendintervaluass', 'dsx3farendintervalvaliddata'], name, value)




    class Dsx3FarEndTotalTable(Entity):
        """
        The DS3 Far End Total Table contains the
        cumulative sum of the various statistics for the
        24 hour period preceding the current interval.
        
        .. attribute:: dsx3farendtotalentry
        
        	An entry in the DS3 Far End Total table
        	**type**\: list of  		 :py:class:`Dsx3FarEndTotalEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FarEndTotalTable.Dsx3FarEndTotalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3FarEndTotalTable, self).__init__()

            self.yang_name = "dsx3FarEndTotalTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3FarEndTotalEntry", ("dsx3farendtotalentry", DS3MIB.Dsx3FarEndTotalTable.Dsx3FarEndTotalEntry))])
            self._leafs = OrderedDict()

            self.dsx3farendtotalentry = YList(self)
            self._segment_path = lambda: "dsx3FarEndTotalTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3FarEndTotalTable, [], name, value)


        class Dsx3FarEndTotalEntry(Entity):
            """
            An entry in the DS3 Far End Total table.
            
            .. attribute:: dsx3farendtotalindex  (key)
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dsx3farendtotalcess
            
            	The counter associated with the number of Far End C\-bit Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendtotalcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendtotalccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dsx3farendtotaluass
            
            	The counter associated with the number of Far End unavailable seconds encountered by a DS3 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3FarEndTotalTable.Dsx3FarEndTotalEntry, self).__init__()

                self.yang_name = "dsx3FarEndTotalEntry"
                self.yang_parent_name = "dsx3FarEndTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3farendtotalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3farendtotalindex', (YLeaf(YType.int32, 'dsx3FarEndTotalIndex'), ['int'])),
                    ('dsx3farendtotalcess', (YLeaf(YType.uint32, 'dsx3FarEndTotalCESs'), ['int'])),
                    ('dsx3farendtotalcsess', (YLeaf(YType.uint32, 'dsx3FarEndTotalCSESs'), ['int'])),
                    ('dsx3farendtotalccvs', (YLeaf(YType.uint32, 'dsx3FarEndTotalCCVs'), ['int'])),
                    ('dsx3farendtotaluass', (YLeaf(YType.uint32, 'dsx3FarEndTotalUASs'), ['int'])),
                ])
                self.dsx3farendtotalindex = None
                self.dsx3farendtotalcess = None
                self.dsx3farendtotalcsess = None
                self.dsx3farendtotalccvs = None
                self.dsx3farendtotaluass = None
                self._segment_path = lambda: "dsx3FarEndTotalEntry" + "[dsx3FarEndTotalIndex='" + str(self.dsx3farendtotalindex) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3FarEndTotalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3FarEndTotalTable.Dsx3FarEndTotalEntry, ['dsx3farendtotalindex', 'dsx3farendtotalcess', 'dsx3farendtotalcsess', 'dsx3farendtotalccvs', 'dsx3farendtotaluass'], name, value)




    class Dsx3FracTable(Entity):
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
        	**type**\: list of  		 :py:class:`Dsx3FracEntry <ydk.models.cisco_ios_xe.DS3_MIB.DS3MIB.Dsx3FracTable.Dsx3FracEntry>`
        
        	**config**\: False
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            super(DS3MIB.Dsx3FracTable, self).__init__()

            self.yang_name = "dsx3FracTable"
            self.yang_parent_name = "DS3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dsx3FracEntry", ("dsx3fracentry", DS3MIB.Dsx3FracTable.Dsx3FracEntry))])
            self._leafs = OrderedDict()

            self.dsx3fracentry = YList(self)
            self._segment_path = lambda: "dsx3FracTable"
            self._absolute_path = lambda: "DS3-MIB:DS3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DS3MIB.Dsx3FracTable, [], name, value)


        class Dsx3FracEntry(Entity):
            """
            An entry in the DS3 Fractional table.
            
            .. attribute:: dsx3fracindex  (key)
            
            	The index value which uniquely identifies  the DS3  interface  to which this entry is applicable The interface identified by a  particular value of  this  index is the same interface as identified by the same value  an  dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: dsx3fracnumber  (key)
            
            	The channel number for this entry
            	**type**\: int
            
            	**range:** 1..31
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: dsx3fracifindex
            
            	An index value that uniquely identifies an interface.  The interface identified by a particular value of this index is the same interface as  identified by the same value an ifIndex object instance. If no interface is currently using a channel, the value should be zero.  If a single interface occupies more  than one  time slot,  that ifIndex value will be found in multiple time slots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DS3-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                super(DS3MIB.Dsx3FracTable.Dsx3FracEntry, self).__init__()

                self.yang_name = "dsx3FracEntry"
                self.yang_parent_name = "dsx3FracTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dsx3fracindex','dsx3fracnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dsx3fracindex', (YLeaf(YType.int32, 'dsx3FracIndex'), ['int'])),
                    ('dsx3fracnumber', (YLeaf(YType.int32, 'dsx3FracNumber'), ['int'])),
                    ('dsx3fracifindex', (YLeaf(YType.int32, 'dsx3FracIfIndex'), ['int'])),
                ])
                self.dsx3fracindex = None
                self.dsx3fracnumber = None
                self.dsx3fracifindex = None
                self._segment_path = lambda: "dsx3FracEntry" + "[dsx3FracIndex='" + str(self.dsx3fracindex) + "']" + "[dsx3FracNumber='" + str(self.dsx3fracnumber) + "']"
                self._absolute_path = lambda: "DS3-MIB:DS3-MIB/dsx3FracTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DS3MIB.Dsx3FracTable.Dsx3FracEntry, ['dsx3fracindex', 'dsx3fracnumber', 'dsx3fracifindex'], name, value)



    def clone_ptr(self):
        self._top_entity = DS3MIB()
        return self._top_entity



