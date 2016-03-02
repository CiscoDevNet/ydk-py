""" DS3_MIB 

The is the MIB module that describes
DS3 and E3 interfaces objects.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class DS3MIB(object):
    """
    
    
    .. attribute:: dsx3configtable
    
    	The DS3/E3 Configuration table
    	**type**\: :py:class:`Dsx3ConfigTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable>`
    
    .. attribute:: dsx3currenttable
    
    	The DS3/E3 current table contains various statistics being collected for the current 15 minute interval
    	**type**\: :py:class:`Dsx3CurrentTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3CurrentTable>`
    
    .. attribute:: dsx3farendconfigtable
    
    	The DS3 Far End Configuration Table contains configuration information reported in the C\-bits from the remote end
    	**type**\: :py:class:`Dsx3FarEndConfigTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndConfigTable>`
    
    .. attribute:: dsx3farendcurrenttable
    
    	The DS3 Far End Current table contains various statistics being collected for the current 15 minute interval.  The statistics are collected from the far end block error code within the C\- bits
    	**type**\: :py:class:`Dsx3FarEndCurrentTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndCurrentTable>`
    
    .. attribute:: dsx3farendintervaltable
    
    	The DS3 Far End Interval Table contains various statistics collected by each DS3 interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals
    	**type**\: :py:class:`Dsx3FarEndIntervalTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndIntervalTable>`
    
    .. attribute:: dsx3farendtotaltable
    
    	The DS3 Far End Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\: :py:class:`Dsx3FarEndTotalTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndTotalTable>`
    
    .. attribute:: dsx3fractable
    
    	This table is deprecated in favour of using ifStackTable.  Implementation of this table was optional.  It was designed for those systems dividing a DS3/E3 into channels containing different data streams that are of local interest.  The DS3/E3 fractional table identifies which DS3/E3 channels associated with a CSU are being used to support a logical interface, i.e., an entry in the interfaces table from the Internet\- standard MIB.  For example, consider a DS3 device with 4 high speed links carrying router traffic, a feed for voice, a feed for video, and a synchronous channel for a non\-routed protocol.  We might describe the allocation of channels, in the dsx3FracTable, as follows\: dsx3FracIfIndex.2. 1 = 3  dsx3FracIfIndex.2.15 = 4 dsx3FracIfIndex.2. 2 = 3  dsx3FracIfIndex.2.16 = 6 dsx3FracIfIndex.2. 3 = 3  dsx3FracIfIndex.2.17 = 6 dsx3FracIfIndex.2. 4 = 3  dsx3FracIfIndex.2.18 = 6 dsx3FracIfIndex.2. 5 = 3  dsx3FracIfIndex.2.19 = 6 dsx3FracIfIndex.2. 6 = 3  dsx3FracIfIndex.2.20 = 6 dsx3FracIfIndex.2. 7 = 4  dsx3FracIfIndex.2.21 = 6 dsx3FracIfIndex.2. 8 = 4  dsx3FracIfIndex.2.22 = 6 dsx3FracIfIndex.2. 9 = 4  dsx3FracIfIndex.2.23 = 6 dsx3FracIfIndex.2.10 = 4  dsx3FracIfIndex.2.24 = 6 dsx3FracIfIndex.2.11 = 4  dsx3FracIfIndex.2.25 = 6 dsx3FracIfIndex.2.12 = 5  dsx3FracIfIndex.2.26 = 6 dsx3FracIfIndex.2.13 = 5  dsx3FracIfIndex.2.27 = 6 dsx3FracIfIndex.2.14 = 5  dsx3FracIfIndex.2.28 = 6 For dsx3M23, dsx3 SYNTRAN, dsx3CbitParity, and dsx3ClearChannel  there are 28 legal channels, numbered 1 throug h 28.  For e3Framed there are 16 legal channels, numbered 1 through 16.  The channels (1..16) correspond directly to the equivalently numbered time\-slots
    	**type**\: :py:class:`Dsx3FracTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FracTable>`
    
    .. attribute:: dsx3intervaltable
    
    	The DS3/E3 Interval Table contains various statistics collected by each DS3/E3 Interface over the previous 24 hours of operation.  The past 24 hours are broken into 96 completed 15 minute intervals.  Each row in this table represents one such interval (identified by dsx3IntervalNumber) and for one specific interface (identifed by dsx3IntervalIndex)
    	**type**\: :py:class:`Dsx3IntervalTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3IntervalTable>`
    
    .. attribute:: dsx3totaltable
    
    	The DS3/E3 Total Table contains the cumulative sum of the various statistics for the 24 hour period preceding the current interval
    	**type**\: :py:class:`Dsx3TotalTable <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3TotalTable>`
    
    

    """

    _prefix = 'ds3-mib'
    _revision = '1998-08-01'

    def __init__(self):
        self.dsx3configtable = DS3MIB.Dsx3ConfigTable()
        self.dsx3configtable.parent = self
        self.dsx3currenttable = DS3MIB.Dsx3CurrentTable()
        self.dsx3currenttable.parent = self
        self.dsx3farendconfigtable = DS3MIB.Dsx3FarEndConfigTable()
        self.dsx3farendconfigtable.parent = self
        self.dsx3farendcurrenttable = DS3MIB.Dsx3FarEndCurrentTable()
        self.dsx3farendcurrenttable.parent = self
        self.dsx3farendintervaltable = DS3MIB.Dsx3FarEndIntervalTable()
        self.dsx3farendintervaltable.parent = self
        self.dsx3farendtotaltable = DS3MIB.Dsx3FarEndTotalTable()
        self.dsx3farendtotaltable.parent = self
        self.dsx3fractable = DS3MIB.Dsx3FracTable()
        self.dsx3fractable.parent = self
        self.dsx3intervaltable = DS3MIB.Dsx3IntervalTable()
        self.dsx3intervaltable.parent = self
        self.dsx3totaltable = DS3MIB.Dsx3TotalTable()
        self.dsx3totaltable.parent = self


    class Dsx3ConfigTable(object):
        """
        The DS3/E3 Configuration table.
        
        .. attribute:: dsx3configentry
        
        	An entry in the DS3/E3 Configuration table
        	**type**\: list of :py:class:`Dsx3ConfigEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3configentry = YList()
            self.dsx3configentry.parent = self
            self.dsx3configentry.name = 'dsx3configentry'


        class Dsx3ConfigEntry(object):
            """
            An entry in the DS3/E3 Configuration table.
            
            .. attribute:: dsx3lineindex
            
            	This object should be made equal to ifIndex.  The next paragraph describes its previous usage. Making the object equal to ifIndex allows propoer use of ifStackTable.  Previously, this object was the identifier of a DS3/E3 Interface on a managed device.  If there is an ifEntry that is directly associated with this and only this DS3/E3 interface, it should have the same value as ifIndex.  Otherwise, number the dsx3LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3channelization
            
            	Indicates whether this ds3/e3 is channelized or unchannelized.  The value of enabledDs1 indicates that this is a DS3 channelized into DS1s.  The value of enabledDs3 indicated that this is a DS3 channelized into DS2s.  Setting this object will cause the creation or deletion of DS2 or DS1 entries in the ifTable.  
            	**type**\: :py:class:`Dsx3Channelization_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3Channelization_Enum>`
            
            .. attribute:: dsx3circuitidentifier
            
            	This variable contains the transmission vendor's circuit identifier, for the purpose of facilitating troubleshooting
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: dsx3ds1forremoteloop
            
            	Indicates which ds1/e1 on this ds3/e3 will be indicated in the remote ds1 loopback request.  A value of 0 means no DS1 will be looped.  A value of 29 means all ds1s/e1s will be looped
            	**type**\: int
            
            	**range:** 0..29
            
            .. attribute:: dsx3ifindex
            
            	This value for this object is equal to the value of ifIndex from the Interfaces table of MIB II (RFC 1213)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3invalidintervals
            
            	The number of intervals in the range from 0 to dsx3ValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\: int
            
            	**range:** 0..96
            
            .. attribute:: dsx3linecoding
            
            	This variable describes the variety of Zero Code Suppression used on this interface, which in turn affects a number of its characteristics.  dsx3B3ZS and e3HDB3 refer to the use of specified patterns of normal bits and bipolar violations which are used to replace sequences of zero bits of a specified length
            	**type**\: :py:class:`Dsx3LineCoding_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineCoding_Enum>`
            
            .. attribute:: dsx3linelength
            
            	The length of the ds3 line in meters.  This object provides information for line build out circuitry if it exists and can use this object to adjust the line build out
            	**type**\: int
            
            	**range:** 0..64000
            
            .. attribute:: dsx3linestatus
            
            	This variable indicates the Line Status of the interface.  It contains loopback state information and failure state information.  The dsx3LineStatus is a bit map represented as a sum, therefore, it can represent multiple failures and a loopback (see dsx3LoopbackConfig object for the type of loopback) simultaneously.  The dsx3NoAlarm must be set if and only if no other flag is set.  If the dsx3loopbackState bit is set, the loopback in effect can be determined from the dsx3loopbackConfig object. The various bit positions are\: 1     dsx3NoAlarm         No alarm present 2     dsx3RcvRAIFailure   Receiving Yellow/Remote                  Alarm Indication 4     dsx3XmitRAIAlarm    Transmitting Yellow/Remote                  Alarm Indication 8     dsx3RcvAIS          Receiving AIS failure state 16     dsx3XmitAIS         Transmitting AIS 32     dsx3LOF             Receiving LOF failure state 64     dsx3LOS             Receiving LOS failure state 128     dsx3LoopbackState   Looping the received signal 256     dsx3RcvTestCode     Receiving a Test Pattern 512     dsx3OtherFailure    any line status not defined                  here 1024     dsx3UnavailSigState Near End in Unavailable Signal                  State 2048     dsx3NetEquipOOS     Carrier Equipment Out of Service
            	**type**\: int
            
            	**range:** 1..4095
            
            .. attribute:: dsx3linestatuschangetrapenable
            
            	Indicates whether dsx3LineStatusChange traps should be generated for this interface
            	**type**\: :py:class:`Dsx3LineStatusChangeTrapEnable_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineStatusChangeTrapEnable_Enum>`
            
            .. attribute:: dsx3linestatuslastchange
            
            	The value of MIB II's sysUpTime object at the time this DS3/E3 entered its current line status state.  If the current state was entered prior to the last re\-initialization of the proxy\-agent, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3linetype
            
            	This variable indicates the variety of DS3 C\-bit or E3 application implementing this interface. The type of interface affects the interpretation of the usage and error statistics.  The rate of DS3 is 44.736 Mbps and E3 is 34.368 Mbps.  The dsx3ClearChannel value means that the C\-bits are not used except for sending/receiving AIS. The values, in sequence, describe\:  TITLE\:            SPECIFICATION\: dsx3M23            ANSI T1.107\-1988 [9] dsx3SYNTRAN        ANSI T1.107\-1988 [9] dsx3CbitParity     ANSI T1.107a\-1990 [9a] dsx3ClearChannel   ANSI T1.102\-1987 [8] e3Framed           CCITT G.751 [12] e3Plcp             ETSI T/NA(91)18 [13]
            	**type**\: :py:class:`Dsx3LineType_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineType_Enum>`
            
            .. attribute:: dsx3loopbackconfig
            
            	This variable represents the desired loopback configuration of the DS3/E3 interface.  The values mean\:  dsx3NoLoop   Not in the loopback state.  A device that is   not capable of performing a loopback on   the interface shall always return this as   its value.  dsx3PayloadLoop   The received signal at this interface is looped   through the device.  Typically the received signal   is looped back for retransmission after it has   passed through the device's framing function.  dsx3LineLoop   The received signal at this interface does not   go through the device (minimum penetration) but   is looped back out.  dsx3OtherLoop   Loopbacks that are not defined here.  dsx3InwardLoop   The sent signal at this interface is looped back   through the device.  dsx3DualLoop   Both dsx1LineLoop and dsx1InwardLoop will be   active simultaneously
            	**type**\: :py:class:`Dsx3LoopbackConfig_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LoopbackConfig_Enum>`
            
            .. attribute:: dsx3loopbackstatus
            
            	This variable represents the current state of the loopback on the DS3 interface.  It contains information about loopbacks established by a manager and remotely from the far end.  The dsx3LoopbackStatus is a bit map represented as a sum, therefore is can represent multiple loopbacks simultaneously.  The various bit positions are\:  1  dsx3NoLoopback  2  dsx3NearEndPayloadLoopback  4  dsx3NearEndLineLoopback  8  dsx3NearEndOtherLoopback 16  dsx3NearEndInwardLoopback 32  dsx3FarEndPayloadLoopback 64  dsx3FarEndLineLoopback
            	**type**\: int
            
            	**range:** 1..127
            
            .. attribute:: dsx3sendcode
            
            	This variable indicates what type of code is being sent across the DS3/E3 interface by the device.  (These are optional for E3 interfaces.) Setting this variable causes the interface to begin sending the code requested. The values mean\:     dsx3SendNoCode        sending looped or normal data     dsx3SendLineCode        sending a request for a line loopback     dsx3SendPayloadCode        sending a request for a payload loopback        (i.e., all DS1/E1s in a DS3/E3 frame)     dsx3SendResetCode        sending a loopback deactivation request     dsx3SendDS1LoopCode        requesting to loopback a particular DS1/E1        within a DS3/E3 frame.  The DS1/E1 is        indicated in dsx3Ds1ForRemoteLoop.     dsx3SendTestPattern        sending a test pattern
            	**type**\: :py:class:`Dsx3SendCode_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3SendCode_Enum>`
            
            .. attribute:: dsx3timeelapsed
            
            	The number of seconds that have elapsed since the beginning of the near end current error\- measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 0..899
            
            .. attribute:: dsx3transmitclocksource
            
            	The source of Transmit Clock.  loopTiming indicates that the recovered receive clock is used as the transmit clock.  localTiming indicates that a local clock source is used or that an external clock is attached to the box containing the interface.  throughTiming indicates that transmit clock is derived from the recovered receive clock of another DS3 interface
            	**type**\: :py:class:`Dsx3TransmitClockSource_Enum <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3TransmitClockSource_Enum>`
            
            .. attribute:: dsx3validintervals
            
            	The number of previous near end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute near end intervals since the interface has been online.  In the case where the agent is a proxy, it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available
            	**type**\: int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3lineindex = None
                self.dsx3channelization = None
                self.dsx3circuitidentifier = None
                self.dsx3ds1forremoteloop = None
                self.dsx3ifindex = None
                self.dsx3invalidintervals = None
                self.dsx3linecoding = None
                self.dsx3linelength = None
                self.dsx3linestatus = None
                self.dsx3linestatuschangetrapenable = None
                self.dsx3linestatuslastchange = None
                self.dsx3linetype = None
                self.dsx3loopbackconfig = None
                self.dsx3loopbackstatus = None
                self.dsx3sendcode = None
                self.dsx3timeelapsed = None
                self.dsx3transmitclocksource = None
                self.dsx3validintervals = None

            class Dsx3Channelization_Enum(Enum):
                """
                Dsx3Channelization_Enum

                Indicates whether this ds3/e3 is channelized or
                unchannelized.  The value of enabledDs1 indicates
                that this is a DS3 channelized into DS1s.  The
                value of enabledDs3 indicated that this is a DS3
                channelized into DS2s.  Setting this object will
                cause the creation or deletion of DS2 or DS1
                entries in the ifTable.  

                """

                DISABLED = 1

                ENABLEDDS1 = 2

                ENABLEDDS2 = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3Channelization_Enum']


            class Dsx3LineCoding_Enum(Enum):
                """
                Dsx3LineCoding_Enum

                This variable describes the variety of Zero Code
                Suppression used on this interface, which in turn
                affects a number of its characteristics.
                
                dsx3B3ZS and e3HDB3 refer to the use of specified
                patterns of normal bits and bipolar violations
                which are used to replace sequences of zero bits
                of a specified length.

                """

                DSX3OTHER = 1

                DSX3B3ZS = 2

                E3HDB3 = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineCoding_Enum']


            class Dsx3LineStatusChangeTrapEnable_Enum(Enum):
                """
                Dsx3LineStatusChangeTrapEnable_Enum

                Indicates whether dsx3LineStatusChange traps
                should be generated for this interface.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineStatusChangeTrapEnable_Enum']


            class Dsx3LineType_Enum(Enum):
                """
                Dsx3LineType_Enum

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

                """

                DSX3OTHER = 1

                DSX3M23 = 2

                DSX3SYNTRAN = 3

                DSX3CBITPARITY = 4

                DSX3CLEARCHANNEL = 5

                E3OTHER = 6

                E3FRAMED = 7

                E3PLCP = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LineType_Enum']


            class Dsx3LoopbackConfig_Enum(Enum):
                """
                Dsx3LoopbackConfig_Enum

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

                """

                DSX3NOLOOP = 1

                DSX3PAYLOADLOOP = 2

                DSX3LINELOOP = 3

                DSX3OTHERLOOP = 4

                DSX3INWARDLOOP = 5

                DSX3DUALLOOP = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3LoopbackConfig_Enum']


            class Dsx3SendCode_Enum(Enum):
                """
                Dsx3SendCode_Enum

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

                """

                DSX3SENDNOCODE = 1

                DSX3SENDLINECODE = 2

                DSX3SENDPAYLOADCODE = 3

                DSX3SENDRESETCODE = 4

                DSX3SENDDS1LOOPCODE = 5

                DSX3SENDTESTPATTERN = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3SendCode_Enum']


            class Dsx3TransmitClockSource_Enum(Enum):
                """
                Dsx3TransmitClockSource_Enum

                The source of Transmit Clock.
                
                loopTiming indicates that the recovered receive clock
                is used as the transmit clock.
                
                localTiming indicates that a local clock source is used
                or that an external clock is attached to the box
                containing the interface.
                
                throughTiming indicates that transmit clock is derived
                from the recovered receive clock of another DS3
                interface.

                """

                LOOPTIMING = 1

                LOCALTIMING = 2

                THROUGHTIMING = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ds3._meta import _DS3_MIB as meta
                    return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry.Dsx3TransmitClockSource_Enum']


            @property
            def _common_path(self):
                if self.dsx3lineindex is None:
                    raise YPYDataValidationError('Key property dsx3lineindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3ConfigTable/DS3-MIB:dsx3ConfigEntry[DS3-MIB:dsx3LineIndex = ' + str(self.dsx3lineindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3lineindex is not None:
                    return True

                if self.dsx3channelization is not None:
                    return True

                if self.dsx3circuitidentifier is not None:
                    return True

                if self.dsx3ds1forremoteloop is not None:
                    return True

                if self.dsx3ifindex is not None:
                    return True

                if self.dsx3invalidintervals is not None:
                    return True

                if self.dsx3linecoding is not None:
                    return True

                if self.dsx3linelength is not None:
                    return True

                if self.dsx3linestatus is not None:
                    return True

                if self.dsx3linestatuschangetrapenable is not None:
                    return True

                if self.dsx3linestatuslastchange is not None:
                    return True

                if self.dsx3linetype is not None:
                    return True

                if self.dsx3loopbackconfig is not None:
                    return True

                if self.dsx3loopbackstatus is not None:
                    return True

                if self.dsx3sendcode is not None:
                    return True

                if self.dsx3timeelapsed is not None:
                    return True

                if self.dsx3transmitclocksource is not None:
                    return True

                if self.dsx3validintervals is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3ConfigTable.Dsx3ConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3ConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3configentry is not None:
                for child_ref in self.dsx3configentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3ConfigTable']['meta_info']


    class Dsx3CurrentTable(object):
        """
        The DS3/E3 current table contains various
        statistics being collected for the current 15
        minute interval.
        
        .. attribute:: dsx3currententry
        
        	An entry in the DS3/E3 Current table
        	**type**\: list of :py:class:`Dsx3CurrentEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3CurrentTable.Dsx3CurrentEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3currententry = YList()
            self.dsx3currententry.parent = self
            self.dsx3currententry.name = 'dsx3currententry'


        class Dsx3CurrentEntry(object):
            """
            An entry in the DS3/E3 Current table.
            
            .. attribute:: dsx3currentindex
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3currentccvs
            
            	The number of C\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentcess
            
            	The number of C\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentcsess
            
            	The number of C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentlcvs
            
            	The counter associated with the number of Line Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentless
            
            	The number of Line Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentpcvs
            
            	The counter associated with the number of P\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentpess
            
            	The counter associated with the number of P\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3currentuass
            
            	The counter associated with the number of Unavailable Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3currentindex = None
                self.dsx3currentccvs = None
                self.dsx3currentcess = None
                self.dsx3currentcsess = None
                self.dsx3currentlcvs = None
                self.dsx3currentless = None
                self.dsx3currentpcvs = None
                self.dsx3currentpess = None
                self.dsx3currentpsess = None
                self.dsx3currentsefss = None
                self.dsx3currentuass = None

            @property
            def _common_path(self):
                if self.dsx3currentindex is None:
                    raise YPYDataValidationError('Key property dsx3currentindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3CurrentTable/DS3-MIB:dsx3CurrentEntry[DS3-MIB:dsx3CurrentIndex = ' + str(self.dsx3currentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3currentindex is not None:
                    return True

                if self.dsx3currentccvs is not None:
                    return True

                if self.dsx3currentcess is not None:
                    return True

                if self.dsx3currentcsess is not None:
                    return True

                if self.dsx3currentlcvs is not None:
                    return True

                if self.dsx3currentless is not None:
                    return True

                if self.dsx3currentpcvs is not None:
                    return True

                if self.dsx3currentpess is not None:
                    return True

                if self.dsx3currentpsess is not None:
                    return True

                if self.dsx3currentsefss is not None:
                    return True

                if self.dsx3currentuass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3CurrentTable.Dsx3CurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3CurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3currententry is not None:
                for child_ref in self.dsx3currententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3CurrentTable']['meta_info']


    class Dsx3FarEndConfigTable(object):
        """
        The DS3 Far End Configuration Table contains
        configuration information reported in the C\-bits
        from the remote end.
        
        .. attribute:: dsx3farendconfigentry
        
        	An entry in the DS3 Far End Configuration table
        	**type**\: list of :py:class:`Dsx3FarEndConfigEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndConfigTable.Dsx3FarEndConfigEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3farendconfigentry = YList()
            self.dsx3farendconfigentry.parent = self
            self.dsx3farendconfigentry.name = 'dsx3farendconfigentry'


        class Dsx3FarEndConfigEntry(object):
            """
            An entry in the DS3 Far End Configuration table.
            
            .. attribute:: dsx3farendlineindex
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendequipcode
            
            	This is the Far End Equipment Identification code that describes the specific piece of equipment. It is sent within the Path Identification Message
            	**type**\: str
            
            	**range:** 0..10
            
            .. attribute:: dsx3farendfacilityidcode
            
            	This code identifies a specific Far End DS3 path. It is sent within the Path Identification Message
            	**type**\: str
            
            	**range:** 0..38
            
            .. attribute:: dsx3farendframeidcode
            
            	This is the Far End Frame Identification code that identifies where the equipment is located within a building at a given location.  It is sent within the Path Identification Message
            	**type**\: str
            
            	**range:** 0..10
            
            .. attribute:: dsx3farendlocationidcode
            
            	This is the Far End Location Identification code that describes the specific location of the equipment.  It is sent within the Path Identification Message
            	**type**\: str
            
            	**range:** 0..11
            
            .. attribute:: dsx3farendunitcode
            
            	This is the Far End code that identifies the equipment location within a bay.  It is sent within the Path Identification Message
            	**type**\: str
            
            	**range:** 0..6
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3farendlineindex = None
                self.dsx3farendequipcode = None
                self.dsx3farendfacilityidcode = None
                self.dsx3farendframeidcode = None
                self.dsx3farendlocationidcode = None
                self.dsx3farendunitcode = None

            @property
            def _common_path(self):
                if self.dsx3farendlineindex is None:
                    raise YPYDataValidationError('Key property dsx3farendlineindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndConfigTable/DS3-MIB:dsx3FarEndConfigEntry[DS3-MIB:dsx3FarEndLineIndex = ' + str(self.dsx3farendlineindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3farendlineindex is not None:
                    return True

                if self.dsx3farendequipcode is not None:
                    return True

                if self.dsx3farendfacilityidcode is not None:
                    return True

                if self.dsx3farendframeidcode is not None:
                    return True

                if self.dsx3farendlocationidcode is not None:
                    return True

                if self.dsx3farendunitcode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3FarEndConfigTable.Dsx3FarEndConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3farendconfigentry is not None:
                for child_ref in self.dsx3farendconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3FarEndConfigTable']['meta_info']


    class Dsx3FarEndCurrentTable(object):
        """
        The DS3 Far End Current table contains various
        statistics being collected for the current 15
        minute interval.  The statistics are collected
        from the far end block error code within the C\-
        bits.
        
        .. attribute:: dsx3farendcurrententry
        
        	An entry in the DS3 Far End Current table
        	**type**\: list of :py:class:`Dsx3FarEndCurrentEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndCurrentTable.Dsx3FarEndCurrentEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3farendcurrententry = YList()
            self.dsx3farendcurrententry.parent = self
            self.dsx3farendcurrententry.name = 'dsx3farendcurrententry'


        class Dsx3FarEndCurrentEntry(object):
            """
            An entry in the DS3 Far End Current table.
            
            .. attribute:: dsx3farendcurrentindex
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendcurrentccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendcurrentcess
            
            	The counter associated with the number of Far Far End C\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendcurrentcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendcurrentuass
            
            	The counter associated with the number of Far End unavailable seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendinvalidintervals
            
            	The number of intervals in the range from 0 to dsx3FarEndValidIntervals for which no data is available.  This object will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations)
            	**type**\: int
            
            	**range:** 0..96
            
            .. attribute:: dsx3farendtimeelapsed
            
            	The number of seconds that have elapsed since the beginning of the far end current error\-measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\: int
            
            	**range:** 0..899
            
            .. attribute:: dsx3farendvalidintervals
            
            	The number of previous far end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute far end intervals since the interface has been online
            	**type**\: int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3farendcurrentindex = None
                self.dsx3farendcurrentccvs = None
                self.dsx3farendcurrentcess = None
                self.dsx3farendcurrentcsess = None
                self.dsx3farendcurrentuass = None
                self.dsx3farendinvalidintervals = None
                self.dsx3farendtimeelapsed = None
                self.dsx3farendvalidintervals = None

            @property
            def _common_path(self):
                if self.dsx3farendcurrentindex is None:
                    raise YPYDataValidationError('Key property dsx3farendcurrentindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndCurrentTable/DS3-MIB:dsx3FarEndCurrentEntry[DS3-MIB:dsx3FarEndCurrentIndex = ' + str(self.dsx3farendcurrentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3farendcurrentindex is not None:
                    return True

                if self.dsx3farendcurrentccvs is not None:
                    return True

                if self.dsx3farendcurrentcess is not None:
                    return True

                if self.dsx3farendcurrentcsess is not None:
                    return True

                if self.dsx3farendcurrentuass is not None:
                    return True

                if self.dsx3farendinvalidintervals is not None:
                    return True

                if self.dsx3farendtimeelapsed is not None:
                    return True

                if self.dsx3farendvalidintervals is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3FarEndCurrentTable.Dsx3FarEndCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3farendcurrententry is not None:
                for child_ref in self.dsx3farendcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3FarEndCurrentTable']['meta_info']


    class Dsx3FarEndIntervalTable(object):
        """
        The DS3 Far End Interval Table contains various
        statistics collected by each DS3 interface over
        the previous 24 hours of operation.  The past 24
        hours are broken into 96 completed 15 minute
        intervals.
        
        .. attribute:: dsx3farendintervalentry
        
        	An entry in the DS3 Far End Interval table
        	**type**\: list of :py:class:`Dsx3FarEndIntervalEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndIntervalTable.Dsx3FarEndIntervalEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3farendintervalentry = YList()
            self.dsx3farendintervalentry.parent = self
            self.dsx3farendintervalentry.name = 'dsx3farendintervalentry'


        class Dsx3FarEndIntervalEntry(object):
            """
            An entry in the DS3 Far End Interval table.
            
            .. attribute:: dsx3farendintervalindex
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendintervalnumber
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: dsx3farendintervalccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervalcess
            
            	The counter associated with the number of Far End C\-bit Errored Seconds encountered by a DS3 interface in one of the previous 96, individual 15 minute, intervals. In the case where the agent is a proxy and data is not available, return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervalcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervaluass
            
            	The counter associated with the number of Far End unavailable seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendintervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3farendintervalindex = None
                self.dsx3farendintervalnumber = None
                self.dsx3farendintervalccvs = None
                self.dsx3farendintervalcess = None
                self.dsx3farendintervalcsess = None
                self.dsx3farendintervaluass = None
                self.dsx3farendintervalvaliddata = None

            @property
            def _common_path(self):
                if self.dsx3farendintervalindex is None:
                    raise YPYDataValidationError('Key property dsx3farendintervalindex is None')
                if self.dsx3farendintervalnumber is None:
                    raise YPYDataValidationError('Key property dsx3farendintervalnumber is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndIntervalTable/DS3-MIB:dsx3FarEndIntervalEntry[DS3-MIB:dsx3FarEndIntervalIndex = ' + str(self.dsx3farendintervalindex) + '][DS3-MIB:dsx3FarEndIntervalNumber = ' + str(self.dsx3farendintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3farendintervalindex is not None:
                    return True

                if self.dsx3farendintervalnumber is not None:
                    return True

                if self.dsx3farendintervalccvs is not None:
                    return True

                if self.dsx3farendintervalcess is not None:
                    return True

                if self.dsx3farendintervalcsess is not None:
                    return True

                if self.dsx3farendintervaluass is not None:
                    return True

                if self.dsx3farendintervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3FarEndIntervalTable.Dsx3FarEndIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3farendintervalentry is not None:
                for child_ref in self.dsx3farendintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3FarEndIntervalTable']['meta_info']


    class Dsx3FarEndTotalTable(object):
        """
        The DS3 Far End Total Table contains the
        cumulative sum of the various statistics for the
        24 hour period preceding the current interval.
        
        .. attribute:: dsx3farendtotalentry
        
        	An entry in the DS3 Far End Total table
        	**type**\: list of :py:class:`Dsx3FarEndTotalEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FarEndTotalTable.Dsx3FarEndTotalEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3farendtotalentry = YList()
            self.dsx3farendtotalentry.parent = self
            self.dsx3farendtotalentry.name = 'dsx3farendtotalentry'


        class Dsx3FarEndTotalEntry(object):
            """
            An entry in the DS3 Far End Total table.
            
            .. attribute:: dsx3farendtotalindex
            
            	The index value which uniquely identifies the DS3 interface to which this entry is applicable.  The interface identified by a particular value of this index is identical to the interface identified by the same value of dsx3LineIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3farendtotalccvs
            
            	The counter associated with the number of Far End C\-bit Coding Violations reported via the far end block error count encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendtotalcess
            
            	The counter associated with the number of Far End C\-bit Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendtotalcsess
            
            	The counter associated with the number of Far End C\-bit Severely Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3farendtotaluass
            
            	The counter associated with the number of Far End unavailable seconds encountered by a DS3 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3farendtotalindex = None
                self.dsx3farendtotalccvs = None
                self.dsx3farendtotalcess = None
                self.dsx3farendtotalcsess = None
                self.dsx3farendtotaluass = None

            @property
            def _common_path(self):
                if self.dsx3farendtotalindex is None:
                    raise YPYDataValidationError('Key property dsx3farendtotalindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndTotalTable/DS3-MIB:dsx3FarEndTotalEntry[DS3-MIB:dsx3FarEndTotalIndex = ' + str(self.dsx3farendtotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3farendtotalindex is not None:
                    return True

                if self.dsx3farendtotalccvs is not None:
                    return True

                if self.dsx3farendtotalcess is not None:
                    return True

                if self.dsx3farendtotalcsess is not None:
                    return True

                if self.dsx3farendtotaluass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3FarEndTotalTable.Dsx3FarEndTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3farendtotalentry is not None:
                for child_ref in self.dsx3farendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3FarEndTotalTable']['meta_info']


    class Dsx3FracTable(object):
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
        	**type**\: list of :py:class:`Dsx3FracEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3FracTable.Dsx3FracEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3fracentry = YList()
            self.dsx3fracentry.parent = self
            self.dsx3fracentry.name = 'dsx3fracentry'


        class Dsx3FracEntry(object):
            """
            An entry in the DS3 Fractional table.
            
            .. attribute:: dsx3fracindex
            
            	The index value which uniquely identifies  the DS3  interface  to which this entry is applicable The interface identified by a  particular value of  this  index is the same interface as identified by the same value  an  dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3fracnumber
            
            	The channel number for this entry
            	**type**\: int
            
            	**range:** 1..31
            
            .. attribute:: dsx3fracifindex
            
            	An index value that uniquely identifies an interface.  The interface identified by a particular value of this index is the same interface as  identified by the same value an ifIndex object instance. If no interface is currently using a channel, the value should be zero.  If a single interface occupies more  than one  time slot,  that ifIndex value will be found in multiple time slots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3fracindex = None
                self.dsx3fracnumber = None
                self.dsx3fracifindex = None

            @property
            def _common_path(self):
                if self.dsx3fracindex is None:
                    raise YPYDataValidationError('Key property dsx3fracindex is None')
                if self.dsx3fracnumber is None:
                    raise YPYDataValidationError('Key property dsx3fracnumber is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FracTable/DS3-MIB:dsx3FracEntry[DS3-MIB:dsx3FracIndex = ' + str(self.dsx3fracindex) + '][DS3-MIB:dsx3FracNumber = ' + str(self.dsx3fracnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3fracindex is not None:
                    return True

                if self.dsx3fracnumber is not None:
                    return True

                if self.dsx3fracifindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3FracTable.Dsx3FracEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FracTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3fracentry is not None:
                for child_ref in self.dsx3fracentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3FracTable']['meta_info']


    class Dsx3IntervalTable(object):
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
        	**type**\: list of :py:class:`Dsx3IntervalEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3IntervalTable.Dsx3IntervalEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3intervalentry = YList()
            self.dsx3intervalentry.parent = self
            self.dsx3intervalentry.name = 'dsx3intervalentry'


        class Dsx3IntervalEntry(object):
            """
            An entry in the DS3/E3 Interval table.
            
            .. attribute:: dsx3intervalindex
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3intervalnumber
            
            	A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the 15 minutes interval completed 23 hours and 45 minutes prior to interval 1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: dsx3intervalccvs
            
            	The number of C\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalcess
            
            	The number of C\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalcsess
            
            	The number of C\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervallcvs
            
            	The counter associated with the number of Line Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalless
            
            	The number of Line Errored  Seconds  (BPVs  or illegal  zero  sequences)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalpcvs
            
            	The counter associated with the number of P\-bit Coding Violations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalpess
            
            	The counter associated with the number of P\-bit Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervaluass
            
            	The counter associated with the number of Unavailable Seconds.  This object may decrease if the occurance of unavailable seconds occurs across an inteval boundary
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3intervalvaliddata
            
            	This variable indicates if the data for this interval is valid
            	**type**\: bool
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3intervalindex = None
                self.dsx3intervalnumber = None
                self.dsx3intervalccvs = None
                self.dsx3intervalcess = None
                self.dsx3intervalcsess = None
                self.dsx3intervallcvs = None
                self.dsx3intervalless = None
                self.dsx3intervalpcvs = None
                self.dsx3intervalpess = None
                self.dsx3intervalpsess = None
                self.dsx3intervalsefss = None
                self.dsx3intervaluass = None
                self.dsx3intervalvaliddata = None

            @property
            def _common_path(self):
                if self.dsx3intervalindex is None:
                    raise YPYDataValidationError('Key property dsx3intervalindex is None')
                if self.dsx3intervalnumber is None:
                    raise YPYDataValidationError('Key property dsx3intervalnumber is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3IntervalTable/DS3-MIB:dsx3IntervalEntry[DS3-MIB:dsx3IntervalIndex = ' + str(self.dsx3intervalindex) + '][DS3-MIB:dsx3IntervalNumber = ' + str(self.dsx3intervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3intervalindex is not None:
                    return True

                if self.dsx3intervalnumber is not None:
                    return True

                if self.dsx3intervalccvs is not None:
                    return True

                if self.dsx3intervalcess is not None:
                    return True

                if self.dsx3intervalcsess is not None:
                    return True

                if self.dsx3intervallcvs is not None:
                    return True

                if self.dsx3intervalless is not None:
                    return True

                if self.dsx3intervalpcvs is not None:
                    return True

                if self.dsx3intervalpess is not None:
                    return True

                if self.dsx3intervalpsess is not None:
                    return True

                if self.dsx3intervalsefss is not None:
                    return True

                if self.dsx3intervaluass is not None:
                    return True

                if self.dsx3intervalvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3IntervalTable.Dsx3IntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3IntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3intervalentry is not None:
                for child_ref in self.dsx3intervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3IntervalTable']['meta_info']


    class Dsx3TotalTable(object):
        """
        The DS3/E3 Total Table contains the cumulative
        sum of the various statistics for the 24 hour
        period preceding the current interval.
        
        .. attribute:: dsx3totalentry
        
        	An entry in the DS3/E3 Total table
        	**type**\: list of :py:class:`Dsx3TotalEntry <ydk.models.ds3.DS3_MIB.DS3MIB.Dsx3TotalTable.Dsx3TotalEntry>`
        
        

        """

        _prefix = 'ds3-mib'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3totalentry = YList()
            self.dsx3totalentry.parent = self
            self.dsx3totalentry.name = 'dsx3totalentry'


        class Dsx3TotalEntry(object):
            """
            An entry in the DS3/E3 Total table.
            
            .. attribute:: dsx3totalindex
            
            	The index value which uniquely identifies the DS3/E3 interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value an dsx3LineIndex object instance
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3totalccvs
            
            	The number of C\-bit Coding Violations encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalcess
            
            	The number of C\-bit Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalcsess
            
            	The number of C\-bit Severely Errored Seconds encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totallcvs
            
            	The counter associated with the number of Line Coding Violations encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalless
            
            	The number of Line Errored  Seconds  (BPVs  or illegal  zero  sequences) encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalpcvs
            
            	The counter associated with the number of P\-bit Coding Violations, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalpess
            
            	The counter associated with the number of P\-bit Errored Seconds, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalpsess
            
            	The counter associated with the number of P\-bit Severely Errored Seconds, encountered by a DS3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totalsefss
            
            	The counter associated with the number of Severely Errored Framing Seconds, encountered by a DS3/E3 interface in the previous 24 hour interval. Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3totaluass
            
            	The counter associated with the number of Unavailable Seconds, encountered by a DS3 interface in the previous 24 hour interval.  Invalid 15 minute intervals count as 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ds3-mib'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx3totalindex = None
                self.dsx3totalccvs = None
                self.dsx3totalcess = None
                self.dsx3totalcsess = None
                self.dsx3totallcvs = None
                self.dsx3totalless = None
                self.dsx3totalpcvs = None
                self.dsx3totalpess = None
                self.dsx3totalpsess = None
                self.dsx3totalsefss = None
                self.dsx3totaluass = None

            @property
            def _common_path(self):
                if self.dsx3totalindex is None:
                    raise YPYDataValidationError('Key property dsx3totalindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3TotalTable/DS3-MIB:dsx3TotalEntry[DS3-MIB:dsx3TotalIndex = ' + str(self.dsx3totalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dsx3totalindex is not None:
                    return True

                if self.dsx3totalccvs is not None:
                    return True

                if self.dsx3totalcess is not None:
                    return True

                if self.dsx3totalcsess is not None:
                    return True

                if self.dsx3totallcvs is not None:
                    return True

                if self.dsx3totalless is not None:
                    return True

                if self.dsx3totalpcvs is not None:
                    return True

                if self.dsx3totalpess is not None:
                    return True

                if self.dsx3totalpsess is not None:
                    return True

                if self.dsx3totalsefss is not None:
                    return True

                if self.dsx3totaluass is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ds3._meta import _DS3_MIB as meta
                return meta._meta_table['DS3MIB.Dsx3TotalTable.Dsx3TotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3TotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dsx3totalentry is not None:
                for child_ref in self.dsx3totalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ds3._meta import _DS3_MIB as meta
            return meta._meta_table['DS3MIB.Dsx3TotalTable']['meta_info']

    @property
    def _common_path(self):

        return '/DS3-MIB:DS3-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.dsx3configtable is not None and self.dsx3configtable._has_data():
            return True

        if self.dsx3configtable is not None and self.dsx3configtable.is_presence():
            return True

        if self.dsx3currenttable is not None and self.dsx3currenttable._has_data():
            return True

        if self.dsx3currenttable is not None and self.dsx3currenttable.is_presence():
            return True

        if self.dsx3farendconfigtable is not None and self.dsx3farendconfigtable._has_data():
            return True

        if self.dsx3farendconfigtable is not None and self.dsx3farendconfigtable.is_presence():
            return True

        if self.dsx3farendcurrenttable is not None and self.dsx3farendcurrenttable._has_data():
            return True

        if self.dsx3farendcurrenttable is not None and self.dsx3farendcurrenttable.is_presence():
            return True

        if self.dsx3farendintervaltable is not None and self.dsx3farendintervaltable._has_data():
            return True

        if self.dsx3farendintervaltable is not None and self.dsx3farendintervaltable.is_presence():
            return True

        if self.dsx3farendtotaltable is not None and self.dsx3farendtotaltable._has_data():
            return True

        if self.dsx3farendtotaltable is not None and self.dsx3farendtotaltable.is_presence():
            return True

        if self.dsx3fractable is not None and self.dsx3fractable._has_data():
            return True

        if self.dsx3fractable is not None and self.dsx3fractable.is_presence():
            return True

        if self.dsx3intervaltable is not None and self.dsx3intervaltable._has_data():
            return True

        if self.dsx3intervaltable is not None and self.dsx3intervaltable.is_presence():
            return True

        if self.dsx3totaltable is not None and self.dsx3totaltable._has_data():
            return True

        if self.dsx3totaltable is not None and self.dsx3totaltable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ds3._meta import _DS3_MIB as meta
        return meta._meta_table['DS3MIB']['meta_info']


