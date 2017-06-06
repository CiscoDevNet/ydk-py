""" DS3_MIB 

The is the MIB module that describes
DS3 and E3 interfaces objects.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ds3Mib(object):
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
        self.dsx3configtable = Ds3Mib.Dsx3Configtable()
        self.dsx3configtable.parent = self
        self.dsx3currenttable = Ds3Mib.Dsx3Currenttable()
        self.dsx3currenttable.parent = self
        self.dsx3farendconfigtable = Ds3Mib.Dsx3Farendconfigtable()
        self.dsx3farendconfigtable.parent = self
        self.dsx3farendcurrenttable = Ds3Mib.Dsx3Farendcurrenttable()
        self.dsx3farendcurrenttable.parent = self
        self.dsx3farendintervaltable = Ds3Mib.Dsx3Farendintervaltable()
        self.dsx3farendintervaltable.parent = self
        self.dsx3farendtotaltable = Ds3Mib.Dsx3Farendtotaltable()
        self.dsx3farendtotaltable.parent = self
        self.dsx3fractable = Ds3Mib.Dsx3Fractable()
        self.dsx3fractable.parent = self
        self.dsx3intervaltable = Ds3Mib.Dsx3Intervaltable()
        self.dsx3intervaltable.parent = self
        self.dsx3totaltable = Ds3Mib.Dsx3Totaltable()
        self.dsx3totaltable.parent = self


    class Dsx3Configtable(object):
        """
        The DS3/E3 Configuration table.
        
        .. attribute:: dsx3configentry
        
        	An entry in the DS3/E3 Configuration table
        	**type**\: list of    :py:class:`Dsx3Configentry <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry>`
        
        

        """

        _prefix = 'DS3-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx3configentry = YList()
            self.dsx3configentry.parent = self
            self.dsx3configentry.name = 'dsx3configentry'


        class Dsx3Configentry(object):
            """
            An entry in the DS3/E3 Configuration table.
            
            .. attribute:: dsx3lineindex  <key>
            
            	This object should be made equal to ifIndex.  The next paragraph describes its previous usage. Making the object equal to ifIndex allows propoer use of ifStackTable.  Previously, this object was the identifier of a DS3/E3 Interface on a managed device.  If there is an ifEntry that is directly associated with this and only this DS3/E3 interface, it should have the same value as ifIndex.  Otherwise, number the dsx3LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx3channelization
            
            	Indicates whether this ds3/e3 is channelized or unchannelized.  The value of enabledDs1 indicates that this is a DS3 channelized into DS1s.  The value of enabledDs3 indicated that this is a DS3 channelized into DS2s.  Setting this object will cause the creation or deletion of DS2 or DS1 entries in the ifTable.  
            	**type**\:   :py:class:`Dsx3ChannelizationEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3ChannelizationEnum>`
            
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
            	**type**\:   :py:class:`Dsx3LinecodingEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinecodingEnum>`
            
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
            	**type**\:   :py:class:`Dsx3LinestatuschangetrapenableEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinestatuschangetrapenableEnum>`
            
            .. attribute:: dsx3linestatuslastchange
            
            	The value of MIB II's sysUpTime object at the time this DS3/E3 entered its current line status state.  If the current state was entered prior to the last re\-initialization of the proxy\-agent, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx3linetype
            
            	This variable indicates the variety of DS3 C\-bit or E3 application implementing this interface. The type of interface affects the interpretation of the usage and error statistics.  The rate of DS3 is 44.736 Mbps and E3 is 34.368 Mbps.  The dsx3ClearChannel value means that the C\-bits are not used except for sending/receiving AIS. The values, in sequence, describe\:  TITLE\:            SPECIFICATION\: dsx3M23            ANSI T1.107\-1988 [9] dsx3SYNTRAN        ANSI T1.107\-1988 [9] dsx3CbitParity     ANSI T1.107a\-1990 [9a] dsx3ClearChannel   ANSI T1.102\-1987 [8] e3Framed           CCITT G.751 [12] e3Plcp             ETSI T/NA(91)18 [13]
            	**type**\:   :py:class:`Dsx3LinetypeEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinetypeEnum>`
            
            .. attribute:: dsx3loopbackconfig
            
            	This variable represents the desired loopback configuration of the DS3/E3 interface.  The values mean\:  dsx3NoLoop   Not in the loopback state.  A device that is   not capable of performing a loopback on   the interface shall always return this as   its value.  dsx3PayloadLoop   The received signal at this interface is looped   through the device.  Typically the received signal   is looped back for retransmission after it has   passed through the device's framing function.  dsx3LineLoop   The received signal at this interface does not   go through the device (minimum penetration) but   is looped back out.  dsx3OtherLoop   Loopbacks that are not defined here.  dsx3InwardLoop   The sent signal at this interface is looped back   through the device.  dsx3DualLoop   Both dsx1LineLoop and dsx1InwardLoop will be   active simultaneously
            	**type**\:   :py:class:`Dsx3LoopbackconfigEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LoopbackconfigEnum>`
            
            .. attribute:: dsx3loopbackstatus
            
            	This variable represents the current state of the loopback on the DS3 interface.  It contains information about loopbacks established by a manager and remotely from the far end.  The dsx3LoopbackStatus is a bit map represented as a sum, therefore is can represent multiple loopbacks simultaneously.  The various bit positions are\:  1  dsx3NoLoopback  2  dsx3NearEndPayloadLoopback  4  dsx3NearEndLineLoopback  8  dsx3NearEndOtherLoopback 16  dsx3NearEndInwardLoopback 32  dsx3FarEndPayloadLoopback 64  dsx3FarEndLineLoopback
            	**type**\:  int
            
            	**range:** 1..127
            
            .. attribute:: dsx3sendcode
            
            	This variable indicates what type of code is being sent across the DS3/E3 interface by the device.  (These are optional for E3 interfaces.) Setting this variable causes the interface to begin sending the code requested. The values mean\:     dsx3SendNoCode        sending looped or normal data     dsx3SendLineCode        sending a request for a line loopback     dsx3SendPayloadCode        sending a request for a payload loopback        (i.e., all DS1/E1s in a DS3/E3 frame)     dsx3SendResetCode        sending a loopback deactivation request     dsx3SendDS1LoopCode        requesting to loopback a particular DS1/E1        within a DS3/E3 frame.  The DS1/E1 is        indicated in dsx3Ds1ForRemoteLoop.     dsx3SendTestPattern        sending a test pattern
            	**type**\:   :py:class:`Dsx3SendcodeEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3SendcodeEnum>`
            
            .. attribute:: dsx3timeelapsed
            
            	The number of seconds that have elapsed since the beginning of the near end current error\- measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            .. attribute:: dsx3transmitclocksource
            
            	The source of Transmit Clock.  loopTiming indicates that the recovered receive clock is used as the transmit clock.  localTiming indicates that a local clock source is used or that an external clock is attached to the box containing the interface.  throughTiming indicates that transmit clock is derived from the recovered receive clock of another DS3 interface
            	**type**\:   :py:class:`Dsx3TransmitclocksourceEnum <ydk.models.cisco_ios_xe.DS3_MIB.Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3TransmitclocksourceEnum>`
            
            .. attribute:: dsx3validintervals
            
            	The number of previous near end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute near end intervals since the interface has been online.  In the case where the agent is a proxy, it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'DS3-MIB'
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

            class Dsx3ChannelizationEnum(Enum):
                """
                Dsx3ChannelizationEnum

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

                disabled = 1

                enabledDs1 = 2

                enabledDs2 = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3ChannelizationEnum']


            class Dsx3LinecodingEnum(Enum):
                """
                Dsx3LinecodingEnum

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

                dsx3Other = 1

                dsx3B3ZS = 2

                e3HDB3 = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinecodingEnum']


            class Dsx3LinestatuschangetrapenableEnum(Enum):
                """
                Dsx3LinestatuschangetrapenableEnum

                Indicates whether dsx3LineStatusChange traps

                should be generated for this interface.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinestatuschangetrapenableEnum']


            class Dsx3LinetypeEnum(Enum):
                """
                Dsx3LinetypeEnum

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

                dsx3other = 1

                dsx3M23 = 2

                dsx3SYNTRAN = 3

                dsx3CbitParity = 4

                dsx3ClearChannel = 5

                e3other = 6

                e3Framed = 7

                e3Plcp = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LinetypeEnum']


            class Dsx3LoopbackconfigEnum(Enum):
                """
                Dsx3LoopbackconfigEnum

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

                dsx3NoLoop = 1

                dsx3PayloadLoop = 2

                dsx3LineLoop = 3

                dsx3OtherLoop = 4

                dsx3InwardLoop = 5

                dsx3DualLoop = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3LoopbackconfigEnum']


            class Dsx3SendcodeEnum(Enum):
                """
                Dsx3SendcodeEnum

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

                dsx3SendNoCode = 1

                dsx3SendLineCode = 2

                dsx3SendPayloadCode = 3

                dsx3SendResetCode = 4

                dsx3SendDS1LoopCode = 5

                dsx3SendTestPattern = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3SendcodeEnum']


            class Dsx3TransmitclocksourceEnum(Enum):
                """
                Dsx3TransmitclocksourceEnum

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

                loopTiming = 1

                localTiming = 2

                throughTiming = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                    return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry.Dsx3TransmitclocksourceEnum']


            @property
            def _common_path(self):
                if self.dsx3lineindex is None:
                    raise YPYModelError('Key property dsx3lineindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3ConfigTable/DS3-MIB:dsx3ConfigEntry[DS3-MIB:dsx3LineIndex = ' + str(self.dsx3lineindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Configtable.Dsx3Configentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3ConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3configentry is not None:
                for child_ref in self.dsx3configentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Configtable']['meta_info']


    class Dsx3Currenttable(object):
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
            self.parent = None
            self.dsx3currententry = YList()
            self.dsx3currententry.parent = self
            self.dsx3currententry.name = 'dsx3currententry'


        class Dsx3Currententry(object):
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
                    raise YPYModelError('Key property dsx3currentindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3CurrentTable/DS3-MIB:dsx3CurrentEntry[DS3-MIB:dsx3CurrentIndex = ' + str(self.dsx3currentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Currenttable.Dsx3Currententry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3CurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3currententry is not None:
                for child_ref in self.dsx3currententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Currenttable']['meta_info']


    class Dsx3Intervaltable(object):
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
            self.parent = None
            self.dsx3intervalentry = YList()
            self.dsx3intervalentry.parent = self
            self.dsx3intervalentry.name = 'dsx3intervalentry'


        class Dsx3Intervalentry(object):
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
                    raise YPYModelError('Key property dsx3intervalindex is None')
                if self.dsx3intervalnumber is None:
                    raise YPYModelError('Key property dsx3intervalnumber is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3IntervalTable/DS3-MIB:dsx3IntervalEntry[DS3-MIB:dsx3IntervalIndex = ' + str(self.dsx3intervalindex) + '][DS3-MIB:dsx3IntervalNumber = ' + str(self.dsx3intervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Intervaltable.Dsx3Intervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3IntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3intervalentry is not None:
                for child_ref in self.dsx3intervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Intervaltable']['meta_info']


    class Dsx3Totaltable(object):
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
            self.parent = None
            self.dsx3totalentry = YList()
            self.dsx3totalentry.parent = self
            self.dsx3totalentry.name = 'dsx3totalentry'


        class Dsx3Totalentry(object):
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
                    raise YPYModelError('Key property dsx3totalindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3TotalTable/DS3-MIB:dsx3TotalEntry[DS3-MIB:dsx3TotalIndex = ' + str(self.dsx3totalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Totaltable.Dsx3Totalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3TotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3totalentry is not None:
                for child_ref in self.dsx3totalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Totaltable']['meta_info']


    class Dsx3Farendconfigtable(object):
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
            self.parent = None
            self.dsx3farendconfigentry = YList()
            self.dsx3farendconfigentry.parent = self
            self.dsx3farendconfigentry.name = 'dsx3farendconfigentry'


        class Dsx3Farendconfigentry(object):
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
                    raise YPYModelError('Key property dsx3farendlineindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndConfigTable/DS3-MIB:dsx3FarEndConfigEntry[DS3-MIB:dsx3FarEndLineIndex = ' + str(self.dsx3farendlineindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Farendconfigtable.Dsx3Farendconfigentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3farendconfigentry is not None:
                for child_ref in self.dsx3farendconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Farendconfigtable']['meta_info']


    class Dsx3Farendcurrenttable(object):
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
            self.parent = None
            self.dsx3farendcurrententry = YList()
            self.dsx3farendcurrententry.parent = self
            self.dsx3farendcurrententry.name = 'dsx3farendcurrententry'


        class Dsx3Farendcurrententry(object):
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
                    raise YPYModelError('Key property dsx3farendcurrentindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndCurrentTable/DS3-MIB:dsx3FarEndCurrentEntry[DS3-MIB:dsx3FarEndCurrentIndex = ' + str(self.dsx3farendcurrentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Farendcurrenttable.Dsx3Farendcurrententry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3farendcurrententry is not None:
                for child_ref in self.dsx3farendcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Farendcurrenttable']['meta_info']


    class Dsx3Farendintervaltable(object):
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
            self.parent = None
            self.dsx3farendintervalentry = YList()
            self.dsx3farendintervalentry.parent = self
            self.dsx3farendintervalentry.name = 'dsx3farendintervalentry'


        class Dsx3Farendintervalentry(object):
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
                    raise YPYModelError('Key property dsx3farendintervalindex is None')
                if self.dsx3farendintervalnumber is None:
                    raise YPYModelError('Key property dsx3farendintervalnumber is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndIntervalTable/DS3-MIB:dsx3FarEndIntervalEntry[DS3-MIB:dsx3FarEndIntervalIndex = ' + str(self.dsx3farendintervalindex) + '][DS3-MIB:dsx3FarEndIntervalNumber = ' + str(self.dsx3farendintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Farendintervaltable.Dsx3Farendintervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3farendintervalentry is not None:
                for child_ref in self.dsx3farendintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Farendintervaltable']['meta_info']


    class Dsx3Farendtotaltable(object):
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
            self.parent = None
            self.dsx3farendtotalentry = YList()
            self.dsx3farendtotalentry.parent = self
            self.dsx3farendtotalentry.name = 'dsx3farendtotalentry'


        class Dsx3Farendtotalentry(object):
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
                self.parent = None
                self.dsx3farendtotalindex = None
                self.dsx3farendtotalccvs = None
                self.dsx3farendtotalcess = None
                self.dsx3farendtotalcsess = None
                self.dsx3farendtotaluass = None

            @property
            def _common_path(self):
                if self.dsx3farendtotalindex is None:
                    raise YPYModelError('Key property dsx3farendtotalindex is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndTotalTable/DS3-MIB:dsx3FarEndTotalEntry[DS3-MIB:dsx3FarEndTotalIndex = ' + str(self.dsx3farendtotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Farendtotaltable.Dsx3Farendtotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3farendtotalentry is not None:
                for child_ref in self.dsx3farendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Farendtotaltable']['meta_info']


    class Dsx3Fractable(object):
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
            self.parent = None
            self.dsx3fracentry = YList()
            self.dsx3fracentry.parent = self
            self.dsx3fracentry.name = 'dsx3fracentry'


        class Dsx3Fracentry(object):
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
                self.parent = None
                self.dsx3fracindex = None
                self.dsx3fracnumber = None
                self.dsx3fracifindex = None

            @property
            def _common_path(self):
                if self.dsx3fracindex is None:
                    raise YPYModelError('Key property dsx3fracindex is None')
                if self.dsx3fracnumber is None:
                    raise YPYModelError('Key property dsx3fracnumber is None')

                return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FracTable/DS3-MIB:dsx3FracEntry[DS3-MIB:dsx3FracIndex = ' + str(self.dsx3fracindex) + '][DS3-MIB:dsx3FracNumber = ' + str(self.dsx3fracnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx3fracindex is not None:
                    return True

                if self.dsx3fracnumber is not None:
                    return True

                if self.dsx3fracifindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
                return meta._meta_table['Ds3Mib.Dsx3Fractable.Dsx3Fracentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS3-MIB:DS3-MIB/DS3-MIB:dsx3FracTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx3fracentry is not None:
                for child_ref in self.dsx3fracentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
            return meta._meta_table['Ds3Mib.Dsx3Fractable']['meta_info']

    @property
    def _common_path(self):

        return '/DS3-MIB:DS3-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dsx3configtable is not None and self.dsx3configtable._has_data():
            return True

        if self.dsx3currenttable is not None and self.dsx3currenttable._has_data():
            return True

        if self.dsx3farendconfigtable is not None and self.dsx3farendconfigtable._has_data():
            return True

        if self.dsx3farendcurrenttable is not None and self.dsx3farendcurrenttable._has_data():
            return True

        if self.dsx3farendintervaltable is not None and self.dsx3farendintervaltable._has_data():
            return True

        if self.dsx3farendtotaltable is not None and self.dsx3farendtotaltable._has_data():
            return True

        if self.dsx3fractable is not None and self.dsx3fractable._has_data():
            return True

        if self.dsx3intervaltable is not None and self.dsx3intervaltable._has_data():
            return True

        if self.dsx3totaltable is not None and self.dsx3totaltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _DS3_MIB as meta
        return meta._meta_table['Ds3Mib']['meta_info']


