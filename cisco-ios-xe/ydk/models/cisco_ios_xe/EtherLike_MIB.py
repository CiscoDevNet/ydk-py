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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Dot3Testtdr(Identity):
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
        super(Dot3Testtdr, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", "EtherLike-MIB", "EtherLike-MIB:dot3TestTdr")


class Dot3Testloopback(Identity):
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
        super(Dot3Testloopback, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", "EtherLike-MIB", "EtherLike-MIB:dot3TestLoopBack")


class Dot3Erroriniterror(Identity):
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
        super(Dot3Erroriniterror, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", "EtherLike-MIB", "EtherLike-MIB:dot3ErrorInitError")


class Dot3Errorloopbackerror(Identity):
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
        super(Dot3Errorloopbackerror, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", "EtherLike-MIB", "EtherLike-MIB:dot3ErrorLoopbackError")


class EtherLikeMIB(Entity):
    """
    
    
    .. attribute:: dot3statstable
    
    	Statistics for a collection of ethernet\-like interfaces attached to a particular system. There will be one row in this table for each ethernet\-like interface in the system
    	**type**\:  :py:class:`Dot3Statstable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable>`
    
    .. attribute:: dot3colltable
    
    	A collection of collision histograms for a particular set of interfaces
    	**type**\:  :py:class:`Dot3Colltable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Colltable>`
    
    .. attribute:: dot3controltable
    
    	A table of descriptive and status information about the MAC Control sublayer on the ethernet\-like interfaces attached to a particular system.  There will be one row in this table for each ethernet\-like interface in the system which implements the MAC Control sublayer.  If some, but not all, of the ethernet\-like interfaces in the system implement the MAC Control sublayer, there will be fewer rows in this table than in the dot3StatsTable
    	**type**\:  :py:class:`Dot3Controltable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Controltable>`
    
    .. attribute:: dot3pausetable
    
    	A table of descriptive and status information about the MAC Control PAUSE function on the ethernet\-like interfaces attached to a particular system. There will be one row in this table for each ethernet\-like interface in the system which supports the MAC Control PAUSE function (i.e., the 'pause' bit in the corresponding instance of dot3ControlFunctionsSupported is set).  If some, but not all, of the ethernet\-like interfaces in the system implement the MAC Control PAUSE function (for example, if some interfaces only support half\-duplex), there will be fewer rows in this table than in the dot3StatsTable
    	**type**\:  :py:class:`Dot3Pausetable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Pausetable>`
    
    .. attribute:: dot3hcstatstable
    
    	A table containing 64\-bit versions of error counters from the dot3StatsTable.  The 32\-bit versions of these counters may roll over quite quickly on higher speed ethernet interfaces. The counters that have 64\-bit versions in this table are the counters that apply to full\-duplex interfaces, since 10 Gb/s and faster ethernet\-like interfaces do not support half\-duplex, and very few 1000 Mb/s ethernet\-like interfaces support half\-duplex.  Entries in this table are recommended for interfaces capable of operating at 1000 Mb/s or faster, and are required for interfaces capable of operating at 10 Gb/s or faster.  Lower speed ethernet\-like interfaces do not need entries in this table, in which case there may be fewer entries in this table than in the dot3StatsTable. However, implementations containing interfaces with a mix of speeds may choose to implement entries in this table for all ethernet\-like interfaces
    	**type**\:  :py:class:`Dot3Hcstatstable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Hcstatstable>`
    
    

    """

    _prefix = 'EtherLike-MIB'
    _revision = '2003-09-19'

    def __init__(self):
        super(EtherLikeMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "EtherLike-MIB"
        self.yang_parent_name = "EtherLike-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("dot3StatsTable", ("dot3statstable", EtherLikeMIB.Dot3Statstable)), ("dot3CollTable", ("dot3colltable", EtherLikeMIB.Dot3Colltable)), ("dot3ControlTable", ("dot3controltable", EtherLikeMIB.Dot3Controltable)), ("dot3PauseTable", ("dot3pausetable", EtherLikeMIB.Dot3Pausetable)), ("dot3HCStatsTable", ("dot3hcstatstable", EtherLikeMIB.Dot3Hcstatstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.dot3statstable = EtherLikeMIB.Dot3Statstable()
        self.dot3statstable.parent = self
        self._children_name_map["dot3statstable"] = "dot3StatsTable"
        self._children_yang_names.add("dot3StatsTable")

        self.dot3colltable = EtherLikeMIB.Dot3Colltable()
        self.dot3colltable.parent = self
        self._children_name_map["dot3colltable"] = "dot3CollTable"
        self._children_yang_names.add("dot3CollTable")

        self.dot3controltable = EtherLikeMIB.Dot3Controltable()
        self.dot3controltable.parent = self
        self._children_name_map["dot3controltable"] = "dot3ControlTable"
        self._children_yang_names.add("dot3ControlTable")

        self.dot3pausetable = EtherLikeMIB.Dot3Pausetable()
        self.dot3pausetable.parent = self
        self._children_name_map["dot3pausetable"] = "dot3PauseTable"
        self._children_yang_names.add("dot3PauseTable")

        self.dot3hcstatstable = EtherLikeMIB.Dot3Hcstatstable()
        self.dot3hcstatstable.parent = self
        self._children_name_map["dot3hcstatstable"] = "dot3HCStatsTable"
        self._children_yang_names.add("dot3HCStatsTable")
        self._segment_path = lambda: "EtherLike-MIB:EtherLike-MIB"


    class Dot3Statstable(Entity):
        """
        Statistics for a collection of ethernet\-like
        interfaces attached to a particular system.
        There will be one row in this table for each
        ethernet\-like interface in the system.
        
        .. attribute:: dot3statsentry
        
        	Statistics for a particular interface to an ethernet\-like medium
        	**type**\: list of  		 :py:class:`Dot3Statsentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3Statstable, self).__init__()

            self.yang_name = "dot3StatsTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot3StatsEntry", ("dot3statsentry", EtherLikeMIB.Dot3Statstable.Dot3Statsentry))])
            self._leafs = OrderedDict()

            self.dot3statsentry = YList(self)
            self._segment_path = lambda: "dot3StatsTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3Statstable, [], name, value)


        class Dot3Statsentry(Entity):
            """
            Statistics for a particular interface to an
            ethernet\-like medium.
            
            .. attribute:: dot3statsindex  (key)
            
            	An index value that uniquely identifies an interface to an ethernet\-like medium.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot3statsalignmenterrors
            
            	A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check.  The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter does not increment for group encoding schemes greater than 4 bits per group.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsAlignmentErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsfcserrors
            
            	A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check.  This count does not include frames received with frame\-too\-long or frame\-too\-short error.  The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  Note\:  Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsFCSErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statssinglecollisionframes
            
            	A count of frames that are involved in a single collision, and are subsequently transmitted successfully.  A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsMultipleCollisionFrames object.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsmultiplecollisionframes
            
            	A count of frames that are involved in more than one collision and are subsequently transmitted successfully.  A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsSingleCollisionFrames object.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statssqetesterrors
            
            	A count of times that the SQE TEST ERROR is received on a particular interface. The SQE TEST ERROR is set in accordance with the rules for verification of the SQE detection mechanism in the PLS Carrier Sense Function as described in IEEE Std. 802.3, 2000 Edition, section 7.2.4.6.  This counter does not increment on interfaces operating at speeds greater than 10 Mb/s, or on interfaces operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsdeferredtransmissions
            
            	A count of frames for which the first transmission attempt on a particular interface is delayed because the medium is busy.  The count represented by an instance of this object does not include frames involved in collisions.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statslatecollisions
            
            	The number of times that a collision is detected on a particular interface later than one slotTime into the transmission of a packet.  A (late) collision included in a count represented by an instance of this object is also considered as a (generic) collision for purposes of other collision\-related statistics.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsexcessivecollisions
            
            	A count of frames for which transmission on a particular interface fails due to excessive collisions.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsinternalmactransmiterrors
            
            	A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsInternalMacTransmitErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statscarriersenseerrors
            
            	The number of times that the carrier sense condition was lost or never asserted when attempting to transmit a frame on a particular interface.  The count represented by an instance of this object is incremented at most once per transmission attempt, even if the carrier sense condition fluctuates during a transmission attempt.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsframetoolongs
            
            	A count of frames received on a particular interface that exceed the maximum permitted frame size.  The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 80 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsFrameTooLongs object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsinternalmacreceiveerrors
            
            	A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsInternalMacReceiveErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsetherchipset
            
            	\*\*\*\*\*\*\*\* THIS OBJECT IS DEPRECATED \*\*\*\*\*\*\*\*  This object contains an OBJECT IDENTIFIER which identifies the chipset used to realize the interface. Ethernet\-like interfaces are typically built out of several different chips. The MIB implementor is presented with a decision of which chip to identify via this object. The implementor should identify the chip which is usually called the Medium Access Control chip. If no such chip is easily identifiable, the implementor should identify the chip which actually gathers the transmit and receive statistics and error indications. This would allow a manager station to correlate the statistics and the chip generating them, giving it the ability to take into account any known anomalies in the chip.  This object has been deprecated.  Implementation feedback indicates that it is of limited use for debugging network problems in the field, and the administrative overhead involved in maintaining a registry of chipset OIDs is not justified
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: dot3statssymbolerrors
            
            	For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.  For an interface operating in half\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII.  For an interface operating in full\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII.  For an interface operating at 10 Gb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Receive Error' on the XGMII.  The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event.  This count does not increment if a collision is present.  This counter does not increment when the interface is operating at 10 Mb/s.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsSymbolErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3statsduplexstatus
            
            	The current mode of operation of the MAC entity.  'unknown' indicates that the current duplex mode could not be determined.  Management control of the duplex mode is accomplished through the MAU MIB.  When an interface does not support autonegotiation, or when autonegotiation is not enabled, the duplex mode is controlled using ifMauDefaultType.  When autonegotiation is supported and enabled, duplex mode is controlled using ifMauAutoNegAdvertisedBits.  In either case, the currently operating duplex mode is reflected both in this object and in ifMauType.  Note that this object provides redundant information with ifMauType.  Normally, redundant objects are discouraged.  However, in this instance, it allows a management application to determine the duplex status of an interface without having to know every possible value of ifMauType.  This was felt to be sufficiently valuable to justify the redundancy
            	**type**\:  :py:class:`Dot3Statsduplexstatus <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry.Dot3Statsduplexstatus>`
            
            .. attribute:: dot3statsratecontrolability
            
            	'true' for interfaces operating at speeds above 1000 Mb/s that support Rate Control through lowering the average data rate of the MAC sublayer, with frame granularity, and 'false' otherwise
            	**type**\: bool
            
            .. attribute:: dot3statsratecontrolstatus
            
            	The current Rate Control mode of operation of the MAC sublayer of this interface
            	**type**\:  :py:class:`Dot3Statsratecontrolstatus <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry.Dot3Statsratecontrolstatus>`
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3Statstable.Dot3Statsentry, self).__init__()

                self.yang_name = "dot3StatsEntry"
                self.yang_parent_name = "dot3StatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', YLeaf(YType.int32, 'dot3StatsIndex')),
                    ('dot3statsalignmenterrors', YLeaf(YType.uint32, 'dot3StatsAlignmentErrors')),
                    ('dot3statsfcserrors', YLeaf(YType.uint32, 'dot3StatsFCSErrors')),
                    ('dot3statssinglecollisionframes', YLeaf(YType.uint32, 'dot3StatsSingleCollisionFrames')),
                    ('dot3statsmultiplecollisionframes', YLeaf(YType.uint32, 'dot3StatsMultipleCollisionFrames')),
                    ('dot3statssqetesterrors', YLeaf(YType.uint32, 'dot3StatsSQETestErrors')),
                    ('dot3statsdeferredtransmissions', YLeaf(YType.uint32, 'dot3StatsDeferredTransmissions')),
                    ('dot3statslatecollisions', YLeaf(YType.uint32, 'dot3StatsLateCollisions')),
                    ('dot3statsexcessivecollisions', YLeaf(YType.uint32, 'dot3StatsExcessiveCollisions')),
                    ('dot3statsinternalmactransmiterrors', YLeaf(YType.uint32, 'dot3StatsInternalMacTransmitErrors')),
                    ('dot3statscarriersenseerrors', YLeaf(YType.uint32, 'dot3StatsCarrierSenseErrors')),
                    ('dot3statsframetoolongs', YLeaf(YType.uint32, 'dot3StatsFrameTooLongs')),
                    ('dot3statsinternalmacreceiveerrors', YLeaf(YType.uint32, 'dot3StatsInternalMacReceiveErrors')),
                    ('dot3statsetherchipset', YLeaf(YType.str, 'dot3StatsEtherChipSet')),
                    ('dot3statssymbolerrors', YLeaf(YType.uint32, 'dot3StatsSymbolErrors')),
                    ('dot3statsduplexstatus', YLeaf(YType.enumeration, 'dot3StatsDuplexStatus')),
                    ('dot3statsratecontrolability', YLeaf(YType.boolean, 'dot3StatsRateControlAbility')),
                    ('dot3statsratecontrolstatus', YLeaf(YType.enumeration, 'dot3StatsRateControlStatus')),
                ])
                self.dot3statsindex = None
                self.dot3statsalignmenterrors = None
                self.dot3statsfcserrors = None
                self.dot3statssinglecollisionframes = None
                self.dot3statsmultiplecollisionframes = None
                self.dot3statssqetesterrors = None
                self.dot3statsdeferredtransmissions = None
                self.dot3statslatecollisions = None
                self.dot3statsexcessivecollisions = None
                self.dot3statsinternalmactransmiterrors = None
                self.dot3statscarriersenseerrors = None
                self.dot3statsframetoolongs = None
                self.dot3statsinternalmacreceiveerrors = None
                self.dot3statsetherchipset = None
                self.dot3statssymbolerrors = None
                self.dot3statsduplexstatus = None
                self.dot3statsratecontrolability = None
                self.dot3statsratecontrolstatus = None
                self._segment_path = lambda: "dot3StatsEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3StatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3Statstable.Dot3Statsentry, ['dot3statsindex', 'dot3statsalignmenterrors', 'dot3statsfcserrors', 'dot3statssinglecollisionframes', 'dot3statsmultiplecollisionframes', 'dot3statssqetesterrors', 'dot3statsdeferredtransmissions', 'dot3statslatecollisions', 'dot3statsexcessivecollisions', 'dot3statsinternalmactransmiterrors', 'dot3statscarriersenseerrors', 'dot3statsframetoolongs', 'dot3statsinternalmacreceiveerrors', 'dot3statsetherchipset', 'dot3statssymbolerrors', 'dot3statsduplexstatus', 'dot3statsratecontrolability', 'dot3statsratecontrolstatus'], name, value)

            class Dot3Statsduplexstatus(Enum):
                """
                Dot3Statsduplexstatus (Enum Class)

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

                unknown = Enum.YLeaf(1, "unknown")

                halfDuplex = Enum.YLeaf(2, "halfDuplex")

                fullDuplex = Enum.YLeaf(3, "fullDuplex")


            class Dot3Statsratecontrolstatus(Enum):
                """
                Dot3Statsratecontrolstatus (Enum Class)

                The current Rate Control mode of operation of

                the MAC sublayer of this interface.

                .. data:: rateControlOff = 1

                .. data:: rateControlOn = 2

                .. data:: unknown = 3

                """

                rateControlOff = Enum.YLeaf(1, "rateControlOff")

                rateControlOn = Enum.YLeaf(2, "rateControlOn")

                unknown = Enum.YLeaf(3, "unknown")



    class Dot3Colltable(Entity):
        """
        A collection of collision histograms for a
        particular set of interfaces.
        
        .. attribute:: dot3collentry
        
        	A cell in the histogram of per\-frame collisions for a particular interface.  An instance of this object represents the frequency of individual MAC frames for which the transmission (successful or otherwise) on a particular interface is accompanied by a particular number of media collisions
        	**type**\: list of  		 :py:class:`Dot3Collentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Colltable.Dot3Collentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3Colltable, self).__init__()

            self.yang_name = "dot3CollTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot3CollEntry", ("dot3collentry", EtherLikeMIB.Dot3Colltable.Dot3Collentry))])
            self._leafs = OrderedDict()

            self.dot3collentry = YList(self)
            self._segment_path = lambda: "dot3CollTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3Colltable, [], name, value)


        class Dot3Collentry(Entity):
            """
            A cell in the histogram of per\-frame
            collisions for a particular interface.  An
            instance of this object represents the
            frequency of individual MAC frames for which
            the transmission (successful or otherwise) on a
            particular interface is accompanied by a
            particular number of media collisions.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: dot3collcount  (key)
            
            	The number of per\-frame media collisions for which a particular collision histogram cell represents the frequency on a particular interface
            	**type**\: int
            
            	**range:** 1..16
            
            .. attribute:: dot3collfrequencies
            
            	A count of individual MAC frames for which the transmission (successful or otherwise) on a particular interface occurs after the frame has experienced exactly the number of collisions in the associated dot3CollCount object.  For example, a frame which is transmitted on interface 77 after experiencing exactly 4 collisions would be indicated by incrementing only dot3CollFrequencies.77.4. No other instance of dot3CollFrequencies would be incremented in this example.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3Colltable.Dot3Collentry, self).__init__()

                self.yang_name = "dot3CollEntry"
                self.yang_parent_name = "dot3CollTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','dot3collcount']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('dot3collcount', YLeaf(YType.int32, 'dot3CollCount')),
                    ('dot3collfrequencies', YLeaf(YType.uint32, 'dot3CollFrequencies')),
                ])
                self.ifindex = None
                self.dot3collcount = None
                self.dot3collfrequencies = None
                self._segment_path = lambda: "dot3CollEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[dot3CollCount='" + str(self.dot3collcount) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3CollTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3Colltable.Dot3Collentry, ['ifindex', 'dot3collcount', 'dot3collfrequencies'], name, value)


    class Dot3Controltable(Entity):
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
        	**type**\: list of  		 :py:class:`Dot3Controlentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Controltable.Dot3Controlentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3Controltable, self).__init__()

            self.yang_name = "dot3ControlTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot3ControlEntry", ("dot3controlentry", EtherLikeMIB.Dot3Controltable.Dot3Controlentry))])
            self._leafs = OrderedDict()

            self.dot3controlentry = YList(self)
            self._segment_path = lambda: "dot3ControlTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3Controltable, [], name, value)


        class Dot3Controlentry(Entity):
            """
            An entry in the table, containing information
            about the MAC Control sublayer on a single
            ethernet\-like interface.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: dot3controlfunctionssupported
            
            	A list of the possible MAC Control functions implemented for this interface
            	**type**\:  :py:class:`Dot3Controlfunctionssupported <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Controltable.Dot3Controlentry.Dot3Controlfunctionssupported>`
            
            .. attribute:: dot3controlinunknownopcodes
            
            	A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCControlInUnknownOpcodes object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3hccontrolinunknownopcodes
            
            	A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.  This counter is a 64 bit version of dot3ControlInUnknownOpcodes.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3Controltable.Dot3Controlentry, self).__init__()

                self.yang_name = "dot3ControlEntry"
                self.yang_parent_name = "dot3ControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', YLeaf(YType.str, 'dot3StatsIndex')),
                    ('dot3controlfunctionssupported', YLeaf(YType.bits, 'dot3ControlFunctionsSupported')),
                    ('dot3controlinunknownopcodes', YLeaf(YType.uint32, 'dot3ControlInUnknownOpcodes')),
                    ('dot3hccontrolinunknownopcodes', YLeaf(YType.uint64, 'dot3HCControlInUnknownOpcodes')),
                ])
                self.dot3statsindex = None
                self.dot3controlfunctionssupported = Bits()
                self.dot3controlinunknownopcodes = None
                self.dot3hccontrolinunknownopcodes = None
                self._segment_path = lambda: "dot3ControlEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3ControlTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3Controltable.Dot3Controlentry, ['dot3statsindex', 'dot3controlfunctionssupported', 'dot3controlinunknownopcodes', 'dot3hccontrolinunknownopcodes'], name, value)


    class Dot3Pausetable(Entity):
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
        	**type**\: list of  		 :py:class:`Dot3Pauseentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Pausetable.Dot3Pauseentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3Pausetable, self).__init__()

            self.yang_name = "dot3PauseTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot3PauseEntry", ("dot3pauseentry", EtherLikeMIB.Dot3Pausetable.Dot3Pauseentry))])
            self._leafs = OrderedDict()

            self.dot3pauseentry = YList(self)
            self._segment_path = lambda: "dot3PauseTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3Pausetable, [], name, value)


        class Dot3Pauseentry(Entity):
            """
            An entry in the table, containing information
            about the MAC Control PAUSE function on a single
            ethernet\-like interface.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: dot3pauseadminmode
            
            	This object is used to configure the default administrative PAUSE mode for this interface.  This object represents the administratively\-configured PAUSE mode for this interface.  If auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, the value of this object determines the operational PAUSE mode of the interface whenever it is operating in full\-duplex mode.  In this case, a set to this object will force the interface into the specified mode.  If auto\-negotiation is implemented and enabled for the MAU attached to this interface, the PAUSE mode for this interface is determined by auto\-negotiation, and the value of this object denotes the mode to which the interface will automatically revert if/when auto\-negotiation is later disabled.  Note that when auto\-negotiation is running, administrative control of the PAUSE mode may be accomplished using the ifMauAutoNegCapAdvertisedBits object in the MAU\-MIB.  Note that the value of this object is ignored when the interface is not operating in full\-duplex mode.  An attempt to set this object to 'enabledXmit(2)' or 'enabledRcv(3)' will fail on interfaces that do not support operation at greater than 100 Mb/s
            	**type**\:  :py:class:`Dot3Pauseadminmode <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Pausetable.Dot3Pauseentry.Dot3Pauseadminmode>`
            
            .. attribute:: dot3pauseopermode
            
            	This object reflects the PAUSE mode currently in use on this interface, as determined by either (1) the result of the auto\-negotiation function or (2) if auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, by the value of dot3PauseAdminMode.  Interfaces operating at 100 Mb/s or less will never return 'enabledXmit(2)' or 'enabledRcv(3)'.  Interfaces operating in half\-duplex mode will always return 'disabled(1)'.  Interfaces on which auto\-negotiation is enabled but not yet completed should return the value 'disabled(1)'
            	**type**\:  :py:class:`Dot3Pauseopermode <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Pausetable.Dot3Pauseentry.Dot3Pauseopermode>`
            
            .. attribute:: dot3inpauseframes
            
            	A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCInPauseFrames object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3outpauseframes
            
            	A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCOutPauseFrames object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3hcinpauseframes
            
            	A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  This counter is a 64 bit version of dot3InPauseFrames.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcoutpauseframes
            
            	A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  This counter is a 64 bit version of dot3OutPauseFrames.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3Pausetable.Dot3Pauseentry, self).__init__()

                self.yang_name = "dot3PauseEntry"
                self.yang_parent_name = "dot3PauseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', YLeaf(YType.str, 'dot3StatsIndex')),
                    ('dot3pauseadminmode', YLeaf(YType.enumeration, 'dot3PauseAdminMode')),
                    ('dot3pauseopermode', YLeaf(YType.enumeration, 'dot3PauseOperMode')),
                    ('dot3inpauseframes', YLeaf(YType.uint32, 'dot3InPauseFrames')),
                    ('dot3outpauseframes', YLeaf(YType.uint32, 'dot3OutPauseFrames')),
                    ('dot3hcinpauseframes', YLeaf(YType.uint64, 'dot3HCInPauseFrames')),
                    ('dot3hcoutpauseframes', YLeaf(YType.uint64, 'dot3HCOutPauseFrames')),
                ])
                self.dot3statsindex = None
                self.dot3pauseadminmode = None
                self.dot3pauseopermode = None
                self.dot3inpauseframes = None
                self.dot3outpauseframes = None
                self.dot3hcinpauseframes = None
                self.dot3hcoutpauseframes = None
                self._segment_path = lambda: "dot3PauseEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3PauseTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3Pausetable.Dot3Pauseentry, ['dot3statsindex', 'dot3pauseadminmode', 'dot3pauseopermode', 'dot3inpauseframes', 'dot3outpauseframes', 'dot3hcinpauseframes', 'dot3hcoutpauseframes'], name, value)

            class Dot3Pauseadminmode(Enum):
                """
                Dot3Pauseadminmode (Enum Class)

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

                disabled = Enum.YLeaf(1, "disabled")

                enabledXmit = Enum.YLeaf(2, "enabledXmit")

                enabledRcv = Enum.YLeaf(3, "enabledRcv")

                enabledXmitAndRcv = Enum.YLeaf(4, "enabledXmitAndRcv")


            class Dot3Pauseopermode(Enum):
                """
                Dot3Pauseopermode (Enum Class)

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

                disabled = Enum.YLeaf(1, "disabled")

                enabledXmit = Enum.YLeaf(2, "enabledXmit")

                enabledRcv = Enum.YLeaf(3, "enabledRcv")

                enabledXmitAndRcv = Enum.YLeaf(4, "enabledXmitAndRcv")



    class Dot3Hcstatstable(Entity):
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
        	**type**\: list of  		 :py:class:`Dot3Hcstatsentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Hcstatstable.Dot3Hcstatsentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3Hcstatstable, self).__init__()

            self.yang_name = "dot3HCStatsTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot3HCStatsEntry", ("dot3hcstatsentry", EtherLikeMIB.Dot3Hcstatstable.Dot3Hcstatsentry))])
            self._leafs = OrderedDict()

            self.dot3hcstatsentry = YList(self)
            self._segment_path = lambda: "dot3HCStatsTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3Hcstatstable, [], name, value)


        class Dot3Hcstatsentry(Entity):
            """
            An entry containing 64\-bit statistics for a
            single ethernet\-like interface.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: dot3hcstatsalignmenterrors
            
            	A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check.  The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter does not increment for group encoding schemes greater than 4 bits per group.  This counter is a 64 bit version of dot3StatsAlignmentErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsfcserrors
            
            	A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check.  This count does not include frames received with frame\-too\-long or frame\-too\-short error.  The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  Note\:  Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check.  This counter is a 64 bit version of dot3StatsFCSErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsinternalmactransmiterrors
            
            	A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.  This counter is a 64 bit version of dot3StatsInternalMacTransmitErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsframetoolongs
            
            	A count of frames received on a particular interface that exceed the maximum permitted frame size.  The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter is a 64 bit version of dot3StatsFrameTooLongs.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatsinternalmacreceiveerrors
            
            	A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.  This counter is a 64 bit version of dot3StatsInternalMacReceiveErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot3hcstatssymbolerrors
            
            	For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.  For an interface operating in half\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII.  For an interface operating in full\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII.  For an interface operating at 10 Gb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Receive Error' on the XGMII.  The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event.  This count does not increment if a collision is present.  This counter is a 64 bit version of dot3StatsSymbolErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3Hcstatstable.Dot3Hcstatsentry, self).__init__()

                self.yang_name = "dot3HCStatsEntry"
                self.yang_parent_name = "dot3HCStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', YLeaf(YType.str, 'dot3StatsIndex')),
                    ('dot3hcstatsalignmenterrors', YLeaf(YType.uint64, 'dot3HCStatsAlignmentErrors')),
                    ('dot3hcstatsfcserrors', YLeaf(YType.uint64, 'dot3HCStatsFCSErrors')),
                    ('dot3hcstatsinternalmactransmiterrors', YLeaf(YType.uint64, 'dot3HCStatsInternalMacTransmitErrors')),
                    ('dot3hcstatsframetoolongs', YLeaf(YType.uint64, 'dot3HCStatsFrameTooLongs')),
                    ('dot3hcstatsinternalmacreceiveerrors', YLeaf(YType.uint64, 'dot3HCStatsInternalMacReceiveErrors')),
                    ('dot3hcstatssymbolerrors', YLeaf(YType.uint64, 'dot3HCStatsSymbolErrors')),
                ])
                self.dot3statsindex = None
                self.dot3hcstatsalignmenterrors = None
                self.dot3hcstatsfcserrors = None
                self.dot3hcstatsinternalmactransmiterrors = None
                self.dot3hcstatsframetoolongs = None
                self.dot3hcstatsinternalmacreceiveerrors = None
                self.dot3hcstatssymbolerrors = None
                self._segment_path = lambda: "dot3HCStatsEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3HCStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3Hcstatstable.Dot3Hcstatsentry, ['dot3statsindex', 'dot3hcstatsalignmenterrors', 'dot3hcstatsfcserrors', 'dot3hcstatsinternalmactransmiterrors', 'dot3hcstatsframetoolongs', 'dot3hcstatsinternalmacreceiveerrors', 'dot3hcstatssymbolerrors'], name, value)

    def clone_ptr(self):
        self._top_entity = EtherLikeMIB()
        return self._top_entity

