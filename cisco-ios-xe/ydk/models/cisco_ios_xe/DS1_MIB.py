""" DS1_MIB 

The MIB module to describe DS1, E1, DS2, and
E2 interfaces objects.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ds1Mib(object):
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
        self.dsx1chanmappingtable = Ds1Mib.Dsx1Chanmappingtable()
        self.dsx1chanmappingtable.parent = self
        self.dsx1configtable = Ds1Mib.Dsx1Configtable()
        self.dsx1configtable.parent = self
        self.dsx1currenttable = Ds1Mib.Dsx1Currenttable()
        self.dsx1currenttable.parent = self
        self.dsx1farendcurrenttable = Ds1Mib.Dsx1Farendcurrenttable()
        self.dsx1farendcurrenttable.parent = self
        self.dsx1farendintervaltable = Ds1Mib.Dsx1Farendintervaltable()
        self.dsx1farendintervaltable.parent = self
        self.dsx1farendtotaltable = Ds1Mib.Dsx1Farendtotaltable()
        self.dsx1farendtotaltable.parent = self
        self.dsx1fractable = Ds1Mib.Dsx1Fractable()
        self.dsx1fractable.parent = self
        self.dsx1intervaltable = Ds1Mib.Dsx1Intervaltable()
        self.dsx1intervaltable.parent = self
        self.dsx1totaltable = Ds1Mib.Dsx1Totaltable()
        self.dsx1totaltable.parent = self


    class Dsx1Configtable(object):
        """
        The DS1 Configuration table.
        
        .. attribute:: dsx1configentry
        
        	An entry in the DS1 Configuration table
        	**type**\: list of    :py:class:`Dsx1Configentry <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry>`
        
        

        """

        _prefix = 'DS1-MIB'
        _revision = '1998-08-01'

        def __init__(self):
            self.parent = None
            self.dsx1configentry = YList()
            self.dsx1configentry.parent = self
            self.dsx1configentry.name = 'dsx1configentry'


        class Dsx1Configentry(object):
            """
            An entry in the DS1 Configuration table.
            
            .. attribute:: dsx1lineindex  <key>
            
            	This object should be made equal to ifIndex.  The next paragraph describes its previous usage. Making the object equal to ifIndex allows proper use of ifStackTable and ds0/ds0bundle mibs.  Previously, this object is the identifier of a DS1 Interface on a managed device.  If there is an ifEntry that is directly associated with this and only this DS1 interface, it should have the same value as ifIndex.  Otherwise, number the dsx1LineIndices with an unique identifier following the rules of choosing a number that is greater than ifNumber and numbering the inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g, network side) with odd numbers
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dsx1channelization
            
            	Indicates whether this ds1/e1 is channelized or unchannelized.  The value of enabledDs0 indicates that this is a DS1 channelized into DS0s.  The value of enabledDs1 indicated that this is a DS2 channelized into DS1s.  Setting this value will cause the creation or deletion of entries in the ifTable for the DS0s that are within the DS1
            	**type**\:   :py:class:`Dsx1ChannelizationEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1ChannelizationEnum>`
            
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
            	**type**\:   :py:class:`Dsx1LinecodingEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinecodingEnum>`
            
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
            	**type**\:   :py:class:`Dsx1LinestatuschangetrapenableEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinestatuschangetrapenableEnum>`
            
            .. attribute:: dsx1linestatuslastchange
            
            	The value of MIB II's sysUpTime object at the time this DS1 entered its current line status state.  If the current state was entered prior to the last re\-initialization of the proxy\-agent, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dsx1linetype
            
            	This variable indicates  the  variety  of  DS1 Line  implementing  this  circuit.  The type of circuit affects the number of bits  per  second that  the circuit can reasonably carry, as well as the interpretation of the  usage  and  error statistics.  The values, in sequence, describe\:  TITLE\:         SPECIFICATION\: dsx1ESF         Extended SuperFrame DS1 (T1.107) dsx1D4          AT&T D4 format DS1 (T1.107) dsx1E1          ITU\-T Recommendation G.704                  (Table 4a) dsx1E1\-CRC      ITU\-T Recommendation G.704                  (Table 4b) dsxE1\-MF        G.704 (Table 4a) with TS16                  multiframing enabled dsx1E1\-CRC\-MF   G.704 (Table 4b) with TS16                  multiframing enabled dsx1Unframed    DS1 with No Framing dsx1E1Unframed  E1 with No Framing (G.703) dsx1DS2M12      DS2 frame format (T1.107) dsx1E2          E2 frame format (G.704)  For clarification, the capacity for each E1 type is as listed below\: dsx1E1Unframed \- E1, no framing = 32 x 64k = 2048k dsx1E1 or dsx1E1CRC \- E1, with framing,    no signalling = 31 x 64k = 1984k dsx1E1MF or dsx1E1CRCMF \- E1, with framing,    signalling = 30 x 64k = 1920k  For further information See ITU\-T Recomm G.704
            	**type**\:   :py:class:`Dsx1LinetypeEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinetypeEnum>`
            
            .. attribute:: dsx1loopbackconfig
            
            	This variable represents the desired loopback configuration of the DS1 interface.  Agents supporting read/write access should return inconsistentValue in response to a requested loopback state that the interface does not support.  The values mean\:  dsx1NoLoop  Not in the loopback state.  A device that is not capable of performing a loopback on the interface shall always return this as its value.  dsx1PayloadLoop  The received signal at this interface is looped through the device.  Typically the received signal is looped back for retransmission after it has passed through the device's framing function.  dsx1LineLoop  The received signal at this interface does not go through the device (minimum penetration) but is looped back out.  dsx1OtherLoop  Loopbacks that are not defined here.  dsx1InwardLoop  The transmitted signal at this interface is looped back and received by the same interface. What is transmitted onto the line is product dependent.  dsx1DualLoop  Both dsx1LineLoop and dsx1InwardLoop will be active simultaneously
            	**type**\:   :py:class:`Dsx1LoopbackconfigEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LoopbackconfigEnum>`
            
            .. attribute:: dsx1loopbackstatus
            
            	This variable represents the current state of the loopback on the DS1 interface.  It contains information about loopbacks established by a manager and remotely from the far end.  The dsx1LoopbackStatus is a bit map represented as a sum, therefore is can represent multiple loopbacks simultaneously.  The various bit positions are\:  1  dsx1NoLoopback  2  dsx1NearEndPayloadLoopback  4  dsx1NearEndLineLoopback  8  dsx1NearEndOtherLoopback 16  dsx1NearEndInwardLoopback 32  dsx1FarEndPayloadLoopback 64  dsx1FarEndLineLoopback
            	**type**\:  int
            
            	**range:** 1..127
            
            .. attribute:: dsx1sendcode
            
            	This variable indicates what type of code is being sent across the DS1 interface by the device. Setting this variable causes the interface to send the code requested.  The values mean\: dsx1SendNoCode sending looped or normal data  dsx1SendLineCode sending a request for a line loopback  dsx1SendPayloadCode sending a request for a payload loopback  dsx1SendResetCode sending a loopback termination request  dsx1SendQRS sending a Quasi\-Random Signal  (QRS)  test pattern  dsx1Send511Pattern sending a 511 bit fixed test pattern  dsx1Send3in24Pattern sending a fixed test pattern of 3 bits set in 24  dsx1SendOtherTestPattern sending a test pattern  other  than  those described by this object
            	**type**\:   :py:class:`Dsx1SendcodeEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SendcodeEnum>`
            
            .. attribute:: dsx1signalmode
            
            	'none' indicates that no bits are reserved for signaling on this channel.  'robbedBit' indicates that DS1 Robbed Bit  Sig\- naling is in use.  'bitOriented' indicates that E1 Channel  Asso\- ciated Signaling is in use.  'messageOriented' indicates that Common  Chan\- nel Signaling is in use either on channel 16 of an E1 link or channel 24 of a DS1
            	**type**\:   :py:class:`Dsx1SignalmodeEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SignalmodeEnum>`
            
            .. attribute:: dsx1timeelapsed
            
            	The number of seconds that have elapsed since the beginning of the near end current error\- measurement period.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            .. attribute:: dsx1transmitclocksource
            
            	The source of Transmit Clock. 'loopTiming' indicates that the recovered re\- ceive clock is used as the transmit clock.  'localTiming' indicates that a local clock source is used or when an external clock is attached to the box containing the interface.  'throughTiming' indicates that recovered re\- ceive clock from another interface is used as the transmit clock
            	**type**\:   :py:class:`Dsx1TransmitclocksourceEnum <ydk.models.cisco_ios_xe.DS1_MIB.Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1TransmitclocksourceEnum>`
            
            .. attribute:: dsx1validintervals
            
            	The number of previous near end intervals for which data was collected.  The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of complete 15 minute near end intervals since the interface has been online.  In the case where the agent is a proxy, it is possible that some intervals are unavailable.  In this case, this interval is the maximum interval number for which data is available
            	**type**\:  int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'DS1-MIB'
            _revision = '1998-08-01'

            def __init__(self):
                self.parent = None
                self.dsx1lineindex = None
                self.dsx1channelization = None
                self.dsx1circuitidentifier = None
                self.dsx1ds1channelnumber = None
                self.dsx1fdl = None
                self.dsx1ifindex = None
                self.dsx1invalidintervals = None
                self.dsx1linecoding = None
                self.dsx1linelength = None
                self.dsx1linestatus = None
                self.dsx1linestatuschangetrapenable = None
                self.dsx1linestatuslastchange = None
                self.dsx1linetype = None
                self.dsx1loopbackconfig = None
                self.dsx1loopbackstatus = None
                self.dsx1sendcode = None
                self.dsx1signalmode = None
                self.dsx1timeelapsed = None
                self.dsx1transmitclocksource = None
                self.dsx1validintervals = None

            class Dsx1ChannelizationEnum(Enum):
                """
                Dsx1ChannelizationEnum

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

                disabled = 1

                enabledDs0 = 2

                enabledDs1 = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1ChannelizationEnum']


            class Dsx1LinecodingEnum(Enum):
                """
                Dsx1LinecodingEnum

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

                dsx1JBZS = 1

                dsx1B8ZS = 2

                dsx1HDB3 = 3

                dsx1ZBTSI = 4

                dsx1AMI = 5

                other = 6

                dsx1B6ZS = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinecodingEnum']


            class Dsx1LinestatuschangetrapenableEnum(Enum):
                """
                Dsx1LinestatuschangetrapenableEnum

                Indicates whether dsx1LineStatusChange traps

                should be generated for this interface.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinestatuschangetrapenableEnum']


            class Dsx1LinetypeEnum(Enum):
                """
                Dsx1LinetypeEnum

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

                other = 1

                dsx1ESF = 2

                dsx1D4 = 3

                dsx1E1 = 4

                dsx1E1CRC = 5

                dsx1E1MF = 6

                dsx1E1CRCMF = 7

                dsx1Unframed = 8

                dsx1E1Unframed = 9

                dsx1DS2M12 = 10

                dsx2E2 = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LinetypeEnum']


            class Dsx1LoopbackconfigEnum(Enum):
                """
                Dsx1LoopbackconfigEnum

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

                dsx1NoLoop = 1

                dsx1PayloadLoop = 2

                dsx1LineLoop = 3

                dsx1OtherLoop = 4

                dsx1InwardLoop = 5

                dsx1DualLoop = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1LoopbackconfigEnum']


            class Dsx1SendcodeEnum(Enum):
                """
                Dsx1SendcodeEnum

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

                dsx1SendNoCode = 1

                dsx1SendLineCode = 2

                dsx1SendPayloadCode = 3

                dsx1SendResetCode = 4

                dsx1SendQRS = 5

                dsx1Send511Pattern = 6

                dsx1Send3in24Pattern = 7

                dsx1SendOtherTestPattern = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SendcodeEnum']


            class Dsx1SignalmodeEnum(Enum):
                """
                Dsx1SignalmodeEnum

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

                none = 1

                robbedBit = 2

                bitOriented = 3

                messageOriented = 4

                other = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1SignalmodeEnum']


            class Dsx1TransmitclocksourceEnum(Enum):
                """
                Dsx1TransmitclocksourceEnum

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

                loopTiming = 1

                localTiming = 2

                throughTiming = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                    return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry.Dsx1TransmitclocksourceEnum']


            @property
            def _common_path(self):
                if self.dsx1lineindex is None:
                    raise YPYModelError('Key property dsx1lineindex is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1ConfigTable/DS1-MIB:dsx1ConfigEntry[DS1-MIB:dsx1LineIndex = ' + str(self.dsx1lineindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1lineindex is not None:
                    return True

                if self.dsx1channelization is not None:
                    return True

                if self.dsx1circuitidentifier is not None:
                    return True

                if self.dsx1ds1channelnumber is not None:
                    return True

                if self.dsx1fdl is not None:
                    return True

                if self.dsx1ifindex is not None:
                    return True

                if self.dsx1invalidintervals is not None:
                    return True

                if self.dsx1linecoding is not None:
                    return True

                if self.dsx1linelength is not None:
                    return True

                if self.dsx1linestatus is not None:
                    return True

                if self.dsx1linestatuschangetrapenable is not None:
                    return True

                if self.dsx1linestatuslastchange is not None:
                    return True

                if self.dsx1linetype is not None:
                    return True

                if self.dsx1loopbackconfig is not None:
                    return True

                if self.dsx1loopbackstatus is not None:
                    return True

                if self.dsx1sendcode is not None:
                    return True

                if self.dsx1signalmode is not None:
                    return True

                if self.dsx1timeelapsed is not None:
                    return True

                if self.dsx1transmitclocksource is not None:
                    return True

                if self.dsx1validintervals is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Configtable.Dsx1Configentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1ConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1configentry is not None:
                for child_ref in self.dsx1configentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Configtable']['meta_info']


    class Dsx1Currenttable(object):
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
            self.parent = None
            self.dsx1currententry = YList()
            self.dsx1currententry.parent = self
            self.dsx1currententry.name = 'dsx1currententry'


        class Dsx1Currententry(object):
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
                self.parent = None
                self.dsx1currentindex = None
                self.dsx1currentbess = None
                self.dsx1currentcsss = None
                self.dsx1currentdms = None
                self.dsx1currentess = None
                self.dsx1currentlcvs = None
                self.dsx1currentless = None
                self.dsx1currentpcvs = None
                self.dsx1currentsefss = None
                self.dsx1currentsess = None
                self.dsx1currentuass = None

            @property
            def _common_path(self):
                if self.dsx1currentindex is None:
                    raise YPYModelError('Key property dsx1currentindex is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1CurrentTable/DS1-MIB:dsx1CurrentEntry[DS1-MIB:dsx1CurrentIndex = ' + str(self.dsx1currentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1currentindex is not None:
                    return True

                if self.dsx1currentbess is not None:
                    return True

                if self.dsx1currentcsss is not None:
                    return True

                if self.dsx1currentdms is not None:
                    return True

                if self.dsx1currentess is not None:
                    return True

                if self.dsx1currentlcvs is not None:
                    return True

                if self.dsx1currentless is not None:
                    return True

                if self.dsx1currentpcvs is not None:
                    return True

                if self.dsx1currentsefss is not None:
                    return True

                if self.dsx1currentsess is not None:
                    return True

                if self.dsx1currentuass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Currenttable.Dsx1Currententry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1CurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1currententry is not None:
                for child_ref in self.dsx1currententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Currenttable']['meta_info']


    class Dsx1Intervaltable(object):
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
            self.parent = None
            self.dsx1intervalentry = YList()
            self.dsx1intervalentry.parent = self
            self.dsx1intervalentry.name = 'dsx1intervalentry'


        class Dsx1Intervalentry(object):
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
                self.parent = None
                self.dsx1intervalindex = None
                self.dsx1intervalnumber = None
                self.dsx1intervalbess = None
                self.dsx1intervalcsss = None
                self.dsx1intervaldms = None
                self.dsx1intervaless = None
                self.dsx1intervallcvs = None
                self.dsx1intervalless = None
                self.dsx1intervalpcvs = None
                self.dsx1intervalsefss = None
                self.dsx1intervalsess = None
                self.dsx1intervaluass = None
                self.dsx1intervalvaliddata = None

            @property
            def _common_path(self):
                if self.dsx1intervalindex is None:
                    raise YPYModelError('Key property dsx1intervalindex is None')
                if self.dsx1intervalnumber is None:
                    raise YPYModelError('Key property dsx1intervalnumber is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1IntervalTable/DS1-MIB:dsx1IntervalEntry[DS1-MIB:dsx1IntervalIndex = ' + str(self.dsx1intervalindex) + '][DS1-MIB:dsx1IntervalNumber = ' + str(self.dsx1intervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1intervalindex is not None:
                    return True

                if self.dsx1intervalnumber is not None:
                    return True

                if self.dsx1intervalbess is not None:
                    return True

                if self.dsx1intervalcsss is not None:
                    return True

                if self.dsx1intervaldms is not None:
                    return True

                if self.dsx1intervaless is not None:
                    return True

                if self.dsx1intervallcvs is not None:
                    return True

                if self.dsx1intervalless is not None:
                    return True

                if self.dsx1intervalpcvs is not None:
                    return True

                if self.dsx1intervalsefss is not None:
                    return True

                if self.dsx1intervalsess is not None:
                    return True

                if self.dsx1intervaluass is not None:
                    return True

                if self.dsx1intervalvaliddata is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Intervaltable.Dsx1Intervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1IntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1intervalentry is not None:
                for child_ref in self.dsx1intervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Intervaltable']['meta_info']


    class Dsx1Totaltable(object):
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
            self.parent = None
            self.dsx1totalentry = YList()
            self.dsx1totalentry.parent = self
            self.dsx1totalentry.name = 'dsx1totalentry'


        class Dsx1Totalentry(object):
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
                self.parent = None
                self.dsx1totalindex = None
                self.dsx1totalbess = None
                self.dsx1totalcsss = None
                self.dsx1totaldms = None
                self.dsx1totaless = None
                self.dsx1totallcvs = None
                self.dsx1totalless = None
                self.dsx1totalpcvs = None
                self.dsx1totalsefss = None
                self.dsx1totalsess = None
                self.dsx1totaluass = None

            @property
            def _common_path(self):
                if self.dsx1totalindex is None:
                    raise YPYModelError('Key property dsx1totalindex is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1TotalTable/DS1-MIB:dsx1TotalEntry[DS1-MIB:dsx1TotalIndex = ' + str(self.dsx1totalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1totalindex is not None:
                    return True

                if self.dsx1totalbess is not None:
                    return True

                if self.dsx1totalcsss is not None:
                    return True

                if self.dsx1totaldms is not None:
                    return True

                if self.dsx1totaless is not None:
                    return True

                if self.dsx1totallcvs is not None:
                    return True

                if self.dsx1totalless is not None:
                    return True

                if self.dsx1totalpcvs is not None:
                    return True

                if self.dsx1totalsefss is not None:
                    return True

                if self.dsx1totalsess is not None:
                    return True

                if self.dsx1totaluass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Totaltable.Dsx1Totalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1TotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1totalentry is not None:
                for child_ref in self.dsx1totalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Totaltable']['meta_info']


    class Dsx1Farendcurrenttable(object):
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
            self.parent = None
            self.dsx1farendcurrententry = YList()
            self.dsx1farendcurrententry.parent = self
            self.dsx1farendcurrententry.name = 'dsx1farendcurrententry'


        class Dsx1Farendcurrententry(object):
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
                self.parent = None
                self.dsx1farendcurrentindex = None
                self.dsx1farendcurrentbess = None
                self.dsx1farendcurrentcsss = None
                self.dsx1farendcurrentdms = None
                self.dsx1farendcurrentess = None
                self.dsx1farendcurrentless = None
                self.dsx1farendcurrentpcvs = None
                self.dsx1farendcurrentsefss = None
                self.dsx1farendcurrentsess = None
                self.dsx1farendcurrentuass = None
                self.dsx1farendinvalidintervals = None
                self.dsx1farendtimeelapsed = None
                self.dsx1farendvalidintervals = None

            @property
            def _common_path(self):
                if self.dsx1farendcurrentindex is None:
                    raise YPYModelError('Key property dsx1farendcurrentindex is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FarEndCurrentTable/DS1-MIB:dsx1FarEndCurrentEntry[DS1-MIB:dsx1FarEndCurrentIndex = ' + str(self.dsx1farendcurrentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1farendcurrentindex is not None:
                    return True

                if self.dsx1farendcurrentbess is not None:
                    return True

                if self.dsx1farendcurrentcsss is not None:
                    return True

                if self.dsx1farendcurrentdms is not None:
                    return True

                if self.dsx1farendcurrentess is not None:
                    return True

                if self.dsx1farendcurrentless is not None:
                    return True

                if self.dsx1farendcurrentpcvs is not None:
                    return True

                if self.dsx1farendcurrentsefss is not None:
                    return True

                if self.dsx1farendcurrentsess is not None:
                    return True

                if self.dsx1farendcurrentuass is not None:
                    return True

                if self.dsx1farendinvalidintervals is not None:
                    return True

                if self.dsx1farendtimeelapsed is not None:
                    return True

                if self.dsx1farendvalidintervals is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Farendcurrenttable.Dsx1Farendcurrententry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FarEndCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1farendcurrententry is not None:
                for child_ref in self.dsx1farendcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Farendcurrenttable']['meta_info']


    class Dsx1Farendintervaltable(object):
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
            self.parent = None
            self.dsx1farendintervalentry = YList()
            self.dsx1farendintervalentry.parent = self
            self.dsx1farendintervalentry.name = 'dsx1farendintervalentry'


        class Dsx1Farendintervalentry(object):
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
                self.parent = None
                self.dsx1farendintervalindex = None
                self.dsx1farendintervalnumber = None
                self.dsx1farendintervalbess = None
                self.dsx1farendintervalcsss = None
                self.dsx1farendintervaldms = None
                self.dsx1farendintervaless = None
                self.dsx1farendintervalless = None
                self.dsx1farendintervalpcvs = None
                self.dsx1farendintervalsefss = None
                self.dsx1farendintervalsess = None
                self.dsx1farendintervaluass = None
                self.dsx1farendintervalvaliddata = None

            @property
            def _common_path(self):
                if self.dsx1farendintervalindex is None:
                    raise YPYModelError('Key property dsx1farendintervalindex is None')
                if self.dsx1farendintervalnumber is None:
                    raise YPYModelError('Key property dsx1farendintervalnumber is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FarEndIntervalTable/DS1-MIB:dsx1FarEndIntervalEntry[DS1-MIB:dsx1FarEndIntervalIndex = ' + str(self.dsx1farendintervalindex) + '][DS1-MIB:dsx1FarEndIntervalNumber = ' + str(self.dsx1farendintervalnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1farendintervalindex is not None:
                    return True

                if self.dsx1farendintervalnumber is not None:
                    return True

                if self.dsx1farendintervalbess is not None:
                    return True

                if self.dsx1farendintervalcsss is not None:
                    return True

                if self.dsx1farendintervaldms is not None:
                    return True

                if self.dsx1farendintervaless is not None:
                    return True

                if self.dsx1farendintervalless is not None:
                    return True

                if self.dsx1farendintervalpcvs is not None:
                    return True

                if self.dsx1farendintervalsefss is not None:
                    return True

                if self.dsx1farendintervalsess is not None:
                    return True

                if self.dsx1farendintervaluass is not None:
                    return True

                if self.dsx1farendintervalvaliddata is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Farendintervaltable.Dsx1Farendintervalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FarEndIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1farendintervalentry is not None:
                for child_ref in self.dsx1farendintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Farendintervaltable']['meta_info']


    class Dsx1Farendtotaltable(object):
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
            self.parent = None
            self.dsx1farendtotalentry = YList()
            self.dsx1farendtotalentry.parent = self
            self.dsx1farendtotalentry.name = 'dsx1farendtotalentry'


        class Dsx1Farendtotalentry(object):
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
                self.parent = None
                self.dsx1farendtotalindex = None
                self.dsx1farendtotalbess = None
                self.dsx1farendtotalcsss = None
                self.dsx1farendtotaldms = None
                self.dsx1farendtotaless = None
                self.dsx1farendtotalless = None
                self.dsx1farendtotalpcvs = None
                self.dsx1farendtotalsefss = None
                self.dsx1farendtotalsess = None
                self.dsx1farendtotaluass = None

            @property
            def _common_path(self):
                if self.dsx1farendtotalindex is None:
                    raise YPYModelError('Key property dsx1farendtotalindex is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FarEndTotalTable/DS1-MIB:dsx1FarEndTotalEntry[DS1-MIB:dsx1FarEndTotalIndex = ' + str(self.dsx1farendtotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1farendtotalindex is not None:
                    return True

                if self.dsx1farendtotalbess is not None:
                    return True

                if self.dsx1farendtotalcsss is not None:
                    return True

                if self.dsx1farendtotaldms is not None:
                    return True

                if self.dsx1farendtotaless is not None:
                    return True

                if self.dsx1farendtotalless is not None:
                    return True

                if self.dsx1farendtotalpcvs is not None:
                    return True

                if self.dsx1farendtotalsefss is not None:
                    return True

                if self.dsx1farendtotalsess is not None:
                    return True

                if self.dsx1farendtotaluass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Farendtotaltable.Dsx1Farendtotalentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FarEndTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1farendtotalentry is not None:
                for child_ref in self.dsx1farendtotalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Farendtotaltable']['meta_info']


    class Dsx1Fractable(object):
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
            self.parent = None
            self.dsx1fracentry = YList()
            self.dsx1fracentry.parent = self
            self.dsx1fracentry.name = 'dsx1fracentry'


        class Dsx1Fracentry(object):
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
                self.parent = None
                self.dsx1fracindex = None
                self.dsx1fracnumber = None
                self.dsx1fracifindex = None

            @property
            def _common_path(self):
                if self.dsx1fracindex is None:
                    raise YPYModelError('Key property dsx1fracindex is None')
                if self.dsx1fracnumber is None:
                    raise YPYModelError('Key property dsx1fracnumber is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FracTable/DS1-MIB:dsx1FracEntry[DS1-MIB:dsx1FracIndex = ' + str(self.dsx1fracindex) + '][DS1-MIB:dsx1FracNumber = ' + str(self.dsx1fracnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dsx1fracindex is not None:
                    return True

                if self.dsx1fracnumber is not None:
                    return True

                if self.dsx1fracifindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Fractable.Dsx1Fracentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1FracTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1fracentry is not None:
                for child_ref in self.dsx1fracentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Fractable']['meta_info']


    class Dsx1Chanmappingtable(object):
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
            self.parent = None
            self.dsx1chanmappingentry = YList()
            self.dsx1chanmappingentry.parent = self
            self.dsx1chanmappingentry.name = 'dsx1chanmappingentry'


        class Dsx1Chanmappingentry(object):
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
                self.parent = None
                self.ifindex = None
                self.dsx1ds1channelnumber = None
                self.dsx1chanmappedifindex = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.dsx1ds1channelnumber is None:
                    raise YPYModelError('Key property dsx1ds1channelnumber is None')

                return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1ChanMappingTable/DS1-MIB:dsx1ChanMappingEntry[DS1-MIB:ifIndex = ' + str(self.ifindex) + '][DS1-MIB:dsx1Ds1ChannelNumber = ' + str(self.dsx1ds1channelnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.dsx1ds1channelnumber is not None:
                    return True

                if self.dsx1chanmappedifindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
                return meta._meta_table['Ds1Mib.Dsx1Chanmappingtable.Dsx1Chanmappingentry']['meta_info']

        @property
        def _common_path(self):

            return '/DS1-MIB:DS1-MIB/DS1-MIB:dsx1ChanMappingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dsx1chanmappingentry is not None:
                for child_ref in self.dsx1chanmappingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
            return meta._meta_table['Ds1Mib.Dsx1Chanmappingtable']['meta_info']

    @property
    def _common_path(self):

        return '/DS1-MIB:DS1-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dsx1chanmappingtable is not None and self.dsx1chanmappingtable._has_data():
            return True

        if self.dsx1configtable is not None and self.dsx1configtable._has_data():
            return True

        if self.dsx1currenttable is not None and self.dsx1currenttable._has_data():
            return True

        if self.dsx1farendcurrenttable is not None and self.dsx1farendcurrenttable._has_data():
            return True

        if self.dsx1farendintervaltable is not None and self.dsx1farendintervaltable._has_data():
            return True

        if self.dsx1farendtotaltable is not None and self.dsx1farendtotaltable._has_data():
            return True

        if self.dsx1fractable is not None and self.dsx1fractable._has_data():
            return True

        if self.dsx1intervaltable is not None and self.dsx1intervaltable._has_data():
            return True

        if self.dsx1totaltable is not None and self.dsx1totaltable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _DS1_MIB as meta
        return meta._meta_table['Ds1Mib']['meta_info']


