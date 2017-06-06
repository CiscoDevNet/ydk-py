""" EtherLike_MIB 

The MIB module to describe generic objects for
ethernet\-like network interfaces.

The following reference is used throughout this
MIB module\:

[IEEE 802.3 Std] refers to\:
   IEEE Std 802.3, 2002 Edition\: 'IEEE Standard
   for Information technology \-
   Telecommunications and information exchange
   between systems \- Local and metropolitan
   area networks \- Specific requirements \-
   Part 3\: Carrier sense multiple access with
   collision detection (CSMA/CD) access method
   and physical layer specifications', as
   amended by IEEE Std 802.3ae\-2002\:
   'Amendment\: Media Access Control (MAC)
   Parameters, Physical Layer, and Management
   Parameters for 10 Gb/s Operation', August,
   2002.

Of particular interest is Clause 30, '10 Mb/s,
100 Mb/s, 1000 Mb/s, and 10 Gb/s Management'.

Copyright (C) The Internet Society (2003).  This
version of this MIB module is part of RFC 3635;
see the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentityIdentity


class Dot3ErroriniterrorIdentity(ObjectIdentityIdentity):
    """
    \*\*\*\*\*\*\*\* THIS IDENTITY IS DEPRECATED \*\*\*\*\*\*\*
    
    Couldn't initialize MAC chip for test.
    
    This object identity has been deprecated, since
    the ifTestTable in the IF\-MIB was deprecated,
    and there is no longer a standard mechanism for
    initiating an interface test.  This left no
    standard way of using this object identity.
    
    

    """

    _prefix = 'EtherLike-MIB'
    _revision = '2003-09-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
        return meta._meta_table['Dot3ErroriniterrorIdentity']['meta_info']


class Dot3TesttdrIdentity(ObjectIdentityIdentity):
    """
    \*\*\*\*\*\*\*\* THIS IDENTITY IS DEPRECATED \*\*\*\*\*\*\*
    
    The Time\-Domain Reflectometry (TDR) test is
    specific to ethernet\-like interfaces of type
    10Base5 and 10Base2.  The TDR value may be
    useful in determining the approximate distance
    to a cable fault.  It is advisable to repeat
    this test to check for a consistent resulting
    TDR value, to verify that there is a fault.
    
    A TDR test returns as its result the time
    interval, measured in 10 MHz ticks or 100 nsec
    units, between the start of TDR test
    transmission and the subsequent detection of a
    collision or deassertion of carrier.  On
    successful completion of a TDR test, the result
    is stored as the value of an appropriate
    instance of an appropriate vendor specific MIB
    object, and the OBJECT IDENTIFIER of that
    instance is stored in the appropriate instance
    of the appropriate test result code object
    (thereby indicating where the result has been
    stored).
    
    This object identity has been deprecated, since
    the ifTestTable in the IF\-MIB was deprecated,
    and there is no longer a standard mechanism for
    initiating an interface test.  This left no
    standard way of using this object identity.
    
    

    """

    _prefix = 'EtherLike-MIB'
    _revision = '2003-09-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
        return meta._meta_table['Dot3TesttdrIdentity']['meta_info']


class Dot3TestloopbackIdentity(ObjectIdentityIdentity):
    """
    \*\*\*\*\*\*\*\* THIS IDENTITY IS DEPRECATED \*\*\*\*\*\*\*
    
    This test configures the MAC chip and executes
    an internal loopback test of memory, data paths,
    and the MAC chip logic.  This loopback test can
    only be executed if the interface is offline.
    Once the test has completed, the MAC chip should
    be reinitialized for network operation, but it
    should remain offline.
    
    If an error occurs during a test, the
    appropriate test result object will be set
    to indicate a failure.  The two OBJECT
    IDENTIFIER values dot3ErrorInitError and
    dot3ErrorLoopbackError may be used to provided
    more information as values for an appropriate
    test result code object.
    
    This object identity has been deprecated, since
    the ifTestTable in the IF\-MIB was deprecated,
    and there is no longer a standard mechanism for
    initiating an interface test.  This left no
    standard way of using this object identity.
    
    

    """

    _prefix = 'EtherLike-MIB'
    _revision = '2003-09-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
        return meta._meta_table['Dot3TestloopbackIdentity']['meta_info']


class Dot3ErrorloopbackerrorIdentity(ObjectIdentityIdentity):
    """
    \*\*\*\*\*\*\*\* THIS IDENTITY IS DEPRECATED \*\*\*\*\*\*\*
    
    Expected data not received (or not received
    correctly) in loopback test.
    
    This object identity has been deprecated, since
    the ifTestTable in the IF\-MIB was deprecated,
    and there is no longer a standard mechanism for
    initiating an interface test.  This left no
    standard way of using this object identity.
    
    

    """

    _prefix = 'EtherLike-MIB'
    _revision = '2003-09-19'

    def __init__(self):
        ObjectIdentityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
        return meta._meta_table['Dot3ErrorloopbackerrorIdentity']['meta_info']


class EtherlikeMib(object):
    """
    
    
    .. attribute:: dot3colltable
    
    	A collection of collision histograms for a particular set of interfaces
    	**type**\:   :py:class:`Dot3Colltable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Colltable>`
    
    .. attribute:: dot3controltable
    
    	A table of descriptive and status information about the MAC Control sublayer on the ethernet\-like interfaces attached to a particular system.  There will be one row in this table for each ethernet\-like interface in the system which implements the MAC Control sublayer.  If some, but not all, of the ethernet\-like interfaces in the system implement the MAC Control sublayer, there will be fewer rows in this table than in the dot3StatsTable
    	**type**\:   :py:class:`Dot3Controltable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Controltable>`
    
    .. attribute:: dot3hcstatstable
    
    	A table containing 64\-bit versions of error counters from the dot3StatsTable.  The 32\-bit versions of these counters may roll over quite quickly on higher speed ethernet interfaces. The counters that have 64\-bit versions in this table are the counters that apply to full\-duplex interfaces, since 10 Gb/s and faster ethernet\-like interfaces do not support half\-duplex, and very few 1000 Mb/s ethernet\-like interfaces support half\-duplex.  Entries in this table are recommended for interfaces capable of operating at 1000 Mb/s or faster, and are required for interfaces capable of operating at 10 Gb/s or faster.  Lower speed ethernet\-like interfaces do not need entries in this table, in which case there may be fewer entries in this table than in the dot3StatsTable. However, implementations containing interfaces with a mix of speeds may choose to implement entries in this table for all ethernet\-like interfaces
    	**type**\:   :py:class:`Dot3Hcstatstable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Hcstatstable>`
    
    .. attribute:: dot3pausetable
    
    	A table of descriptive and status information about the MAC Control PAUSE function on the ethernet\-like interfaces attached to a particular system. There will be one row in this table for each ethernet\-like interface in the system which supports the MAC Control PAUSE function (i.e., the 'pause' bit in the corresponding instance of dot3ControlFunctionsSupported is set).  If some, but not all, of the ethernet\-like interfaces in the system implement the MAC Control PAUSE function (for example, if some interfaces only support half\-duplex), there will be fewer rows in this table than in the dot3StatsTable
    	**type**\:   :py:class:`Dot3Pausetable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable>`
    
    .. attribute:: dot3statstable
    
    	Statistics for a collection of ethernet\-like interfaces attached to a particular system. There will be one row in this table for each ethernet\-like interface in the system
    	**type**\:   :py:class:`Dot3Statstable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable>`
    
    

    """

    _prefix = 'EtherLike-MIB'
    _revision = '2003-09-19'

    def __init__(self):
        self.dot3colltable = EtherlikeMib.Dot3Colltable()
        self.dot3colltable.parent = self
        self.dot3controltable = EtherlikeMib.Dot3Controltable()
        self.dot3controltable.parent = self
        self.dot3hcstatstable = EtherlikeMib.Dot3Hcstatstable()
        self.dot3hcstatstable.parent = self
        self.dot3pausetable = EtherlikeMib.Dot3Pausetable()
        self.dot3pausetable.parent = self
        self.dot3statstable = EtherlikeMib.Dot3Statstable()
        self.dot3statstable.parent = self


    class Dot3Statstable(object):
        """
        Statistics for a collection of ethernet\-like
        interfaces attached to a particular system.
        There will be one row in this table for each
        ethernet\-like interface in the system.
        
        .. attribute:: dot3statsentry
        
        	Statistics for a particular interface to an ethernet\-like medium
        	**type**\: list of    :py:class:`Dot3Statsentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.dot3statsentry = YList()
            self.dot3statsentry.parent = self
            self.dot3statsentry.name = 'dot3statsentry'


        class Dot3Statsentry(object):
            """
            Statistics for a particular interface to an
            ethernet\-like medium.
            
            .. attribute:: dot3statsindex  <key>
            
            	An index value that uniquely identifies an interface to an ethernet\-like medium.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot3statsalignmenterrors
            
            	A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check.  The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter does not increment for group encoding schemes greater than 4 bits per group.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsAlignmentErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statscarriersenseerrors
            
            	The number of times that the carrier sense condition was lost or never asserted when attempting to transmit a frame on a particular interface.  The count represented by an instance of this object is incremented at most once per transmission attempt, even if the carrier sense condition fluctuates during a transmission attempt.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsdeferredtransmissions
            
            	A count of frames for which the first transmission attempt on a particular interface is delayed because the medium is busy.  The count represented by an instance of this object does not include frames involved in collisions.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsduplexstatus
            
            	The current mode of operation of the MAC entity.  'unknown' indicates that the current duplex mode could not be determined.  Management control of the duplex mode is accomplished through the MAU MIB.  When an interface does not support autonegotiation, or when autonegotiation is not enabled, the duplex mode is controlled using ifMauDefaultType.  When autonegotiation is supported and enabled, duplex mode is controlled using ifMauAutoNegAdvertisedBits.  In either case, the currently operating duplex mode is reflected both in this object and in ifMauType.  Note that this object provides redundant information with ifMauType.  Normally, redundant objects are discouraged.  However, in this instance, it allows a management application to determine the duplex status of an interface without having to know every possible value of ifMauType.  This was felt to be sufficiently valuable to justify the redundancy
            	**type**\:   :py:class:`Dot3StatsduplexstatusEnum <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsduplexstatusEnum>`
            
            .. attribute:: dot3statsetherchipset
            
            	\*\*\*\*\*\*\*\* THIS OBJECT IS DEPRECATED \*\*\*\*\*\*\*\*  This object contains an OBJECT IDENTIFIER which identifies the chipset used to realize the interface. Ethernet\-like interfaces are typically built out of several different chips. The MIB implementor is presented with a decision of which chip to identify via this object. The implementor should identify the chip which is usually called the Medium Access Control chip. If no such chip is easily identifiable, the implementor should identify the chip which actually gathers the transmit and receive statistics and error indications. This would allow a manager station to correlate the statistics and the chip generating them, giving it the ability to take into account any known anomalies in the chip.  This object has been deprecated.  Implementation feedback indicates that it is of limited use for debugging network problems in the field, and the administrative overhead involved in maintaining a registry of chipset OIDs is not justified
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: dot3statsexcessivecollisions
            
            	A count of frames for which transmission on a particular interface fails due to excessive collisions.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsfcserrors
            
            	A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check.  This count does not include frames received with frame\-too\-long or frame\-too\-short error.  The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  Note\:  Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsFCSErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsframetoolongs
            
            	A count of frames received on a particular interface that exceed the maximum permitted frame size.  The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 80 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsFrameTooLongs object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsinternalmacreceiveerrors
            
            	A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsInternalMacReceiveErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsinternalmactransmiterrors
            
            	A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsInternalMacTransmitErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statslatecollisions
            
            	The number of times that a collision is detected on a particular interface later than one slotTime into the transmission of a packet.  A (late) collision included in a count represented by an instance of this object is also considered as a (generic) collision for purposes of other collision\-related statistics.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsmultiplecollisionframes
            
            	A count of frames that are involved in more than one collision and are subsequently transmitted successfully.  A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsSingleCollisionFrames object.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsratecontrolability
            
            	'true' for interfaces operating at speeds above 1000 Mb/s that support Rate Control through lowering the average data rate of the MAC sublayer, with frame granularity, and 'false' otherwise
            	**type**\:  bool
            
            .. attribute:: dot3statsratecontrolstatus
            
            	The current Rate Control mode of operation of the MAC sublayer of this interface
            	**type**\:   :py:class:`Dot3StatsratecontrolstatusEnum <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsratecontrolstatusEnum>`
            
            .. attribute:: dot3statssinglecollisionframes
            
            	A count of frames that are involved in a single collision, and are subsequently transmitted successfully.  A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsMultipleCollisionFrames object.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statssqetesterrors
            
            	A count of times that the SQE TEST ERROR is received on a particular interface. The SQE TEST ERROR is set in accordance with the rules for verification of the SQE detection mechanism in the PLS Carrier Sense Function as described in IEEE Std. 802.3, 2000 Edition, section 7.2.4.6.  This counter does not increment on interfaces operating at speeds greater than 10 Mb/s, or on interfaces operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statssymbolerrors
            
            	For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.  For an interface operating in half\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII.  For an interface operating in full\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII.  For an interface operating at 10 Gb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Receive Error' on the XGMII.  The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event.  This count does not increment if a collision is present.  This counter does not increment when the interface is operating at 10 Mb/s.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsSymbolErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.dot3statsindex = None
                self.dot3statsalignmenterrors = None
                self.dot3statscarriersenseerrors = None
                self.dot3statsdeferredtransmissions = None
                self.dot3statsduplexstatus = None
                self.dot3statsetherchipset = None
                self.dot3statsexcessivecollisions = None
                self.dot3statsfcserrors = None
                self.dot3statsframetoolongs = None
                self.dot3statsinternalmacreceiveerrors = None
                self.dot3statsinternalmactransmiterrors = None
                self.dot3statslatecollisions = None
                self.dot3statsmultiplecollisionframes = None
                self.dot3statsratecontrolability = None
                self.dot3statsratecontrolstatus = None
                self.dot3statssinglecollisionframes = None
                self.dot3statssqetesterrors = None
                self.dot3statssymbolerrors = None

            class Dot3StatsduplexstatusEnum(Enum):
                """
                Dot3StatsduplexstatusEnum

                The current mode of operation of the MAC

                entity.  'unknown' indicates that the current

                duplex mode could not be determined.

                Management control of the duplex mode is

                accomplished through the MAU MIB.  When

                an interface does not support autonegotiation,

                or when autonegotiation is not enabled, the

                duplex mode is controlled using

                ifMauDefaultType.  When autonegotiation is

                supported and enabled, duplex mode is controlled

                using ifMauAutoNegAdvertisedBits.  In either

                case, the currently operating duplex mode is

                reflected both in this object and in ifMauType.

                Note that this object provides redundant

                information with ifMauType.  Normally, redundant

                objects are discouraged.  However, in this

                instance, it allows a management application to

                determine the duplex status of an interface

                without having to know every possible value of

                ifMauType.  This was felt to be sufficiently

                valuable to justify the redundancy.

                .. data:: unknown = 1

                .. data:: halfDuplex = 2

                .. data:: fullDuplex = 3

                """

                unknown = 1

                halfDuplex = 2

                fullDuplex = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                    return meta._meta_table['EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsduplexstatusEnum']


            class Dot3StatsratecontrolstatusEnum(Enum):
                """
                Dot3StatsratecontrolstatusEnum

                The current Rate Control mode of operation of

                the MAC sublayer of this interface.

                .. data:: rateControlOff = 1

                .. data:: rateControlOn = 2

                .. data:: unknown = 3

                """

                rateControlOff = 1

                rateControlOn = 2

                unknown = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                    return meta._meta_table['EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3StatsratecontrolstatusEnum']


            @property
            def _common_path(self):
                if self.dot3statsindex is None:
                    raise YPYModelError('Key property dot3statsindex is None')

                return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3StatsTable/EtherLike-MIB:dot3StatsEntry[EtherLike-MIB:dot3StatsIndex = ' + str(self.dot3statsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot3statsindex is not None:
                    return True

                if self.dot3statsalignmenterrors is not None:
                    return True

                if self.dot3statscarriersenseerrors is not None:
                    return True

                if self.dot3statsdeferredtransmissions is not None:
                    return True

                if self.dot3statsduplexstatus is not None:
                    return True

                if self.dot3statsetherchipset is not None:
                    return True

                if self.dot3statsexcessivecollisions is not None:
                    return True

                if self.dot3statsfcserrors is not None:
                    return True

                if self.dot3statsframetoolongs is not None:
                    return True

                if self.dot3statsinternalmacreceiveerrors is not None:
                    return True

                if self.dot3statsinternalmactransmiterrors is not None:
                    return True

                if self.dot3statslatecollisions is not None:
                    return True

                if self.dot3statsmultiplecollisionframes is not None:
                    return True

                if self.dot3statsratecontrolability is not None:
                    return True

                if self.dot3statsratecontrolstatus is not None:
                    return True

                if self.dot3statssinglecollisionframes is not None:
                    return True

                if self.dot3statssqetesterrors is not None:
                    return True

                if self.dot3statssymbolerrors is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                return meta._meta_table['EtherlikeMib.Dot3Statstable.Dot3Statsentry']['meta_info']

        @property
        def _common_path(self):

            return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3StatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot3statsentry is not None:
                for child_ref in self.dot3statsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
            return meta._meta_table['EtherlikeMib.Dot3Statstable']['meta_info']


    class Dot3Colltable(object):
        """
        A collection of collision histograms for a
        particular set of interfaces.
        
        .. attribute:: dot3collentry
        
        	A cell in the histogram of per\-frame collisions for a particular interface.  An instance of this object represents the frequency of individual MAC frames for which the transmission (successful or otherwise) on a particular interface is accompanied by a particular number of media collisions
        	**type**\: list of    :py:class:`Dot3Collentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Colltable.Dot3Collentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.dot3collentry = YList()
            self.dot3collentry.parent = self
            self.dot3collentry.name = 'dot3collentry'


        class Dot3Collentry(object):
            """
            A cell in the histogram of per\-frame
            collisions for a particular interface.  An
            instance of this object represents the
            frequency of individual MAC frames for which
            the transmission (successful or otherwise) on a
            particular interface is accompanied by a
            particular number of media collisions.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: dot3collcount  <key>
            
            	The number of per\-frame media collisions for which a particular collision histogram cell represents the frequency on a particular interface
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: dot3collfrequencies
            
            	A count of individual MAC frames for which the transmission (successful or otherwise) on a particular interface occurs after the frame has experienced exactly the number of collisions in the associated dot3CollCount object.  For example, a frame which is transmitted on interface 77 after experiencing exactly 4 collisions would be indicated by incrementing only dot3CollFrequencies.77.4. No other instance of dot3CollFrequencies would be incremented in this example.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.dot3collcount = None
                self.dot3collfrequencies = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.dot3collcount is None:
                    raise YPYModelError('Key property dot3collcount is None')

                return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3CollTable/EtherLike-MIB:dot3CollEntry[EtherLike-MIB:ifIndex = ' + str(self.ifindex) + '][EtherLike-MIB:dot3CollCount = ' + str(self.dot3collcount) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.dot3collcount is not None:
                    return True

                if self.dot3collfrequencies is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                return meta._meta_table['EtherlikeMib.Dot3Colltable.Dot3Collentry']['meta_info']

        @property
        def _common_path(self):

            return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3CollTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot3collentry is not None:
                for child_ref in self.dot3collentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
            return meta._meta_table['EtherlikeMib.Dot3Colltable']['meta_info']


    class Dot3Controltable(object):
        """
        A table of descriptive and status information
        about the MAC Control sublayer on the
        ethernet\-like interfaces attached to a
        particular system.  There will be one row in
        this table for each ethernet\-like interface in
        the system which implements the MAC Control
        sublayer.  If some, but not all, of the
        ethernet\-like interfaces in the system implement
        the MAC Control sublayer, there will be fewer
        rows in this table than in the dot3StatsTable.
        
        .. attribute:: dot3controlentry
        
        	An entry in the table, containing information about the MAC Control sublayer on a single ethernet\-like interface
        	**type**\: list of    :py:class:`Dot3Controlentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Controltable.Dot3Controlentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.dot3controlentry = YList()
            self.dot3controlentry.parent = self
            self.dot3controlentry.name = 'dot3controlentry'


        class Dot3Controlentry(object):
            """
            An entry in the table, containing information
            about the MAC Control sublayer on a single
            ethernet\-like interface.
            
            .. attribute:: dot3statsindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: dot3controlfunctionssupported
            
            	A list of the possible MAC Control functions implemented for this interface
            	**type**\:   :py:class:`Dot3Controlfunctionssupported <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Controltable.Dot3Controlentry.Dot3Controlfunctionssupported>`
            
            .. attribute:: dot3controlinunknownopcodes
            
            	A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCControlInUnknownOpcodes object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3hccontrolinunknownopcodes
            
            	A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.  This counter is a 64 bit version of dot3ControlInUnknownOpcodes.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.dot3statsindex = None
                self.dot3controlfunctionssupported = EtherlikeMib.Dot3Controltable.Dot3Controlentry.Dot3Controlfunctionssupported()
                self.dot3controlinunknownopcodes = None
                self.dot3hccontrolinunknownopcodes = None

            class Dot3Controlfunctionssupported(FixedBitsDict):
                """
                Dot3Controlfunctionssupported

                A list of the possible MAC Control functions
                implemented for this interface.
                Keys are:- pause

                """

                def __init__(self):
                    self._dictionary = { 
                        'pause':False,
                    }
                    self._pos_map = { 
                        'pause':0,
                    }

            @property
            def _common_path(self):
                if self.dot3statsindex is None:
                    raise YPYModelError('Key property dot3statsindex is None')

                return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3ControlTable/EtherLike-MIB:dot3ControlEntry[EtherLike-MIB:dot3StatsIndex = ' + str(self.dot3statsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot3statsindex is not None:
                    return True

                if self.dot3controlfunctionssupported is not None:
                    if self.dot3controlfunctionssupported._has_data():
                        return True

                if self.dot3controlinunknownopcodes is not None:
                    return True

                if self.dot3hccontrolinunknownopcodes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                return meta._meta_table['EtherlikeMib.Dot3Controltable.Dot3Controlentry']['meta_info']

        @property
        def _common_path(self):

            return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3ControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot3controlentry is not None:
                for child_ref in self.dot3controlentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
            return meta._meta_table['EtherlikeMib.Dot3Controltable']['meta_info']


    class Dot3Pausetable(object):
        """
        A table of descriptive and status information
        about the MAC Control PAUSE function on the
        ethernet\-like interfaces attached to a
        particular system. There will be one row in
        this table for each ethernet\-like interface in
        the system which supports the MAC Control PAUSE
        function (i.e., the 'pause' bit in the
        corresponding instance of
        dot3ControlFunctionsSupported is set).  If some,
        but not all, of the ethernet\-like interfaces in
        the system implement the MAC Control PAUSE
        function (for example, if some interfaces only
        support half\-duplex), there will be fewer rows
        in this table than in the dot3StatsTable.
        
        .. attribute:: dot3pauseentry
        
        	An entry in the table, containing information about the MAC Control PAUSE function on a single ethernet\-like interface
        	**type**\: list of    :py:class:`Dot3Pauseentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable.Dot3Pauseentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.dot3pauseentry = YList()
            self.dot3pauseentry.parent = self
            self.dot3pauseentry.name = 'dot3pauseentry'


        class Dot3Pauseentry(object):
            """
            An entry in the table, containing information
            about the MAC Control PAUSE function on a single
            ethernet\-like interface.
            
            .. attribute:: dot3statsindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: dot3hcinpauseframes
            
            	A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  This counter is a 64 bit version of dot3InPauseFrames.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcoutpauseframes
            
            	A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  This counter is a 64 bit version of dot3OutPauseFrames.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3inpauseframes
            
            	A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCInPauseFrames object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3outpauseframes
            
            	A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCOutPauseFrames object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3pauseadminmode
            
            	This object is used to configure the default administrative PAUSE mode for this interface.  This object represents the administratively\-configured PAUSE mode for this interface.  If auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, the value of this object determines the operational PAUSE mode of the interface whenever it is operating in full\-duplex mode.  In this case, a set to this object will force the interface into the specified mode.  If auto\-negotiation is implemented and enabled for the MAU attached to this interface, the PAUSE mode for this interface is determined by auto\-negotiation, and the value of this object denotes the mode to which the interface will automatically revert if/when auto\-negotiation is later disabled.  Note that when auto\-negotiation is running, administrative control of the PAUSE mode may be accomplished using the ifMauAutoNegCapAdvertisedBits object in the MAU\-MIB.  Note that the value of this object is ignored when the interface is not operating in full\-duplex mode.  An attempt to set this object to 'enabledXmit(2)' or 'enabledRcv(3)' will fail on interfaces that do not support operation at greater than 100 Mb/s
            	**type**\:   :py:class:`Dot3PauseadminmodeEnum <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseadminmodeEnum>`
            
            .. attribute:: dot3pauseopermode
            
            	This object reflects the PAUSE mode currently in use on this interface, as determined by either (1) the result of the auto\-negotiation function or (2) if auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, by the value of dot3PauseAdminMode.  Interfaces operating at 100 Mb/s or less will never return 'enabledXmit(2)' or 'enabledRcv(3)'.  Interfaces operating in half\-duplex mode will always return 'disabled(1)'.  Interfaces on which auto\-negotiation is enabled but not yet completed should return the value 'disabled(1)'
            	**type**\:   :py:class:`Dot3PauseopermodeEnum <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseopermodeEnum>`
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.dot3statsindex = None
                self.dot3hcinpauseframes = None
                self.dot3hcoutpauseframes = None
                self.dot3inpauseframes = None
                self.dot3outpauseframes = None
                self.dot3pauseadminmode = None
                self.dot3pauseopermode = None

            class Dot3PauseadminmodeEnum(Enum):
                """
                Dot3PauseadminmodeEnum

                This object is used to configure the default

                administrative PAUSE mode for this interface.

                This object represents the

                administratively\-configured PAUSE mode for this

                interface.  If auto\-negotiation is not enabled

                or is not implemented for the active MAU

                attached to this interface, the value of this

                object determines the operational PAUSE mode

                of the interface whenever it is operating in

                full\-duplex mode.  In this case, a set to this

                object will force the interface into the

                specified mode.

                If auto\-negotiation is implemented and enabled

                for the MAU attached to this interface, the

                PAUSE mode for this interface is determined by

                auto\-negotiation, and the value of this object

                denotes the mode to which the interface will

                automatically revert if/when auto\-negotiation is

                later disabled.  Note that when auto\-negotiation

                is running, administrative control of the PAUSE

                mode may be accomplished using the

                ifMauAutoNegCapAdvertisedBits object in the

                MAU\-MIB.

                Note that the value of this object is ignored

                when the interface is not operating in

                full\-duplex mode.

                An attempt to set this object to

                'enabledXmit(2)' or 'enabledRcv(3)' will fail

                on interfaces that do not support operation

                at greater than 100 Mb/s.

                .. data:: disabled = 1

                .. data:: enabledXmit = 2

                .. data:: enabledRcv = 3

                .. data:: enabledXmitAndRcv = 4

                """

                disabled = 1

                enabledXmit = 2

                enabledRcv = 3

                enabledXmitAndRcv = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                    return meta._meta_table['EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseadminmodeEnum']


            class Dot3PauseopermodeEnum(Enum):
                """
                Dot3PauseopermodeEnum

                This object reflects the PAUSE mode currently

                in use on this interface, as determined by

                either (1) the result of the auto\-negotiation

                function or (2) if auto\-negotiation is not

                enabled or is not implemented for the active MAU

                attached to this interface, by the value of

                dot3PauseAdminMode.  Interfaces operating at

                100 Mb/s or less will never return

                'enabledXmit(2)' or 'enabledRcv(3)'.  Interfaces

                operating in half\-duplex mode will always return

                'disabled(1)'.  Interfaces on which

                auto\-negotiation is enabled but not yet

                completed should return the value

                'disabled(1)'.

                .. data:: disabled = 1

                .. data:: enabledXmit = 2

                .. data:: enabledRcv = 3

                .. data:: enabledXmitAndRcv = 4

                """

                disabled = 1

                enabledXmit = 2

                enabledRcv = 3

                enabledXmitAndRcv = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                    return meta._meta_table['EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3PauseopermodeEnum']


            @property
            def _common_path(self):
                if self.dot3statsindex is None:
                    raise YPYModelError('Key property dot3statsindex is None')

                return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3PauseTable/EtherLike-MIB:dot3PauseEntry[EtherLike-MIB:dot3StatsIndex = ' + str(self.dot3statsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot3statsindex is not None:
                    return True

                if self.dot3hcinpauseframes is not None:
                    return True

                if self.dot3hcoutpauseframes is not None:
                    return True

                if self.dot3inpauseframes is not None:
                    return True

                if self.dot3outpauseframes is not None:
                    return True

                if self.dot3pauseadminmode is not None:
                    return True

                if self.dot3pauseopermode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                return meta._meta_table['EtherlikeMib.Dot3Pausetable.Dot3Pauseentry']['meta_info']

        @property
        def _common_path(self):

            return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3PauseTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot3pauseentry is not None:
                for child_ref in self.dot3pauseentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
            return meta._meta_table['EtherlikeMib.Dot3Pausetable']['meta_info']


    class Dot3Hcstatstable(object):
        """
        A table containing 64\-bit versions of error
        counters from the dot3StatsTable.  The 32\-bit
        versions of these counters may roll over quite
        quickly on higher speed ethernet interfaces.
        The counters that have 64\-bit versions in this
        table are the counters that apply to full\-duplex
        interfaces, since 10 Gb/s and faster
        ethernet\-like interfaces do not support
        half\-duplex, and very few 1000 Mb/s
        ethernet\-like interfaces support half\-duplex.
        
        Entries in this table are recommended for
        interfaces capable of operating at 1000 Mb/s or
        faster, and are required for interfaces capable
        of operating at 10 Gb/s or faster.  Lower speed
        ethernet\-like interfaces do not need entries in
        this table, in which case there may be fewer
        entries in this table than in the
        dot3StatsTable. However, implementations
        containing interfaces with a mix of speeds may
        choose to implement entries in this table for
        all ethernet\-like interfaces.
        
        .. attribute:: dot3hcstatsentry
        
        	An entry containing 64\-bit statistics for a single ethernet\-like interface
        	**type**\: list of    :py:class:`Dot3Hcstatsentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.dot3hcstatsentry = YList()
            self.dot3hcstatsentry.parent = self
            self.dot3hcstatsentry.name = 'dot3hcstatsentry'


        class Dot3Hcstatsentry(object):
            """
            An entry containing 64\-bit statistics for a
            single ethernet\-like interface.
            
            .. attribute:: dot3statsindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: dot3hcstatsalignmenterrors
            
            	A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check.  The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter does not increment for group encoding schemes greater than 4 bits per group.  This counter is a 64 bit version of dot3StatsAlignmentErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsfcserrors
            
            	A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check.  This count does not include frames received with frame\-too\-long or frame\-too\-short error.  The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  Note\:  Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check.  This counter is a 64 bit version of dot3StatsFCSErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsframetoolongs
            
            	A count of frames received on a particular interface that exceed the maximum permitted frame size.  The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter is a 64 bit version of dot3StatsFrameTooLongs.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsinternalmacreceiveerrors
            
            	A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.  This counter is a 64 bit version of dot3StatsInternalMacReceiveErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsinternalmactransmiterrors
            
            	A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.  This counter is a 64 bit version of dot3StatsInternalMacTransmitErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatssymbolerrors
            
            	For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.  For an interface operating in half\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII.  For an interface operating in full\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII.  For an interface operating at 10 Gb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Receive Error' on the XGMII.  The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event.  This count does not increment if a collision is present.  This counter is a 64 bit version of dot3StatsSymbolErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.dot3statsindex = None
                self.dot3hcstatsalignmenterrors = None
                self.dot3hcstatsfcserrors = None
                self.dot3hcstatsframetoolongs = None
                self.dot3hcstatsinternalmacreceiveerrors = None
                self.dot3hcstatsinternalmactransmiterrors = None
                self.dot3hcstatssymbolerrors = None

            @property
            def _common_path(self):
                if self.dot3statsindex is None:
                    raise YPYModelError('Key property dot3statsindex is None')

                return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3HCStatsTable/EtherLike-MIB:dot3HCStatsEntry[EtherLike-MIB:dot3StatsIndex = ' + str(self.dot3statsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot3statsindex is not None:
                    return True

                if self.dot3hcstatsalignmenterrors is not None:
                    return True

                if self.dot3hcstatsfcserrors is not None:
                    return True

                if self.dot3hcstatsframetoolongs is not None:
                    return True

                if self.dot3hcstatsinternalmacreceiveerrors is not None:
                    return True

                if self.dot3hcstatsinternalmactransmiterrors is not None:
                    return True

                if self.dot3hcstatssymbolerrors is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
                return meta._meta_table['EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/EtherLike-MIB:EtherLike-MIB/EtherLike-MIB:dot3HCStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot3hcstatsentry is not None:
                for child_ref in self.dot3hcstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
            return meta._meta_table['EtherlikeMib.Dot3Hcstatstable']['meta_info']

    @property
    def _common_path(self):

        return '/EtherLike-MIB:EtherLike-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dot3colltable is not None and self.dot3colltable._has_data():
            return True

        if self.dot3controltable is not None and self.dot3controltable._has_data():
            return True

        if self.dot3hcstatstable is not None and self.dot3hcstatstable._has_data():
            return True

        if self.dot3pausetable is not None and self.dot3pausetable._has_data():
            return True

        if self.dot3statstable is not None and self.dot3statstable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _EtherLike_MIB as meta
        return meta._meta_table['EtherlikeMib']['meta_info']


