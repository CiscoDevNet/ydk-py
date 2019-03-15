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

from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity



class Dot3ErrorInitError(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", pref="EtherLike-MIB", tag="EtherLike-MIB:dot3ErrorInitError"):
        super(Dot3ErrorInitError, self).__init__(ns, pref, tag)



class Dot3TestTdr(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", pref="EtherLike-MIB", tag="EtherLike-MIB:dot3TestTdr"):
        super(Dot3TestTdr, self).__init__(ns, pref, tag)



class Dot3ErrorLoopbackError(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", pref="EtherLike-MIB", tag="EtherLike-MIB:dot3ErrorLoopbackError"):
        super(Dot3ErrorLoopbackError, self).__init__(ns, pref, tag)



class Dot3TestLoopBack(ObjectIdentity):
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

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:EtherLike-MIB", pref="EtherLike-MIB", tag="EtherLike-MIB:dot3TestLoopBack"):
        super(Dot3TestLoopBack, self).__init__(ns, pref, tag)



class EtherLikeMIB(Entity):
    """
    
    
    .. attribute:: dot3statstable
    
    	Statistics for a collection of ethernet\-like interfaces attached to a particular system. There will be one row in this table for each ethernet\-like interface in the system
    	**type**\:  :py:class:`Dot3StatsTable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable>`
    
    	**config**\: False
    
    .. attribute:: dot3colltable
    
    	A collection of collision histograms for a particular set of interfaces
    	**type**\:  :py:class:`Dot3CollTable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3CollTable>`
    
    	**config**\: False
    
    .. attribute:: dot3controltable
    
    	A table of descriptive and status information about the MAC Control sublayer on the ethernet\-like interfaces attached to a particular system.  There will be one row in this table for each ethernet\-like interface in the system which implements the MAC Control sublayer.  If some, but not all, of the ethernet\-like interfaces in the system implement the MAC Control sublayer, there will be fewer rows in this table than in the dot3StatsTable
    	**type**\:  :py:class:`Dot3ControlTable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3ControlTable>`
    
    	**config**\: False
    
    .. attribute:: dot3pausetable
    
    	A table of descriptive and status information about the MAC Control PAUSE function on the ethernet\-like interfaces attached to a particular system. There will be one row in this table for each ethernet\-like interface in the system which supports the MAC Control PAUSE function (i.e., the 'pause' bit in the corresponding instance of dot3ControlFunctionsSupported is set).  If some, but not all, of the ethernet\-like interfaces in the system implement the MAC Control PAUSE function (for example, if some interfaces only support half\-duplex), there will be fewer rows in this table than in the dot3StatsTable
    	**type**\:  :py:class:`Dot3PauseTable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3PauseTable>`
    
    	**config**\: False
    
    .. attribute:: dot3hcstatstable
    
    	A table containing 64\-bit versions of error counters from the dot3StatsTable.  The 32\-bit versions of these counters may roll over quite quickly on higher speed ethernet interfaces. The counters that have 64\-bit versions in this table are the counters that apply to full\-duplex interfaces, since 10 Gb/s and faster ethernet\-like interfaces do not support half\-duplex, and very few 1000 Mb/s ethernet\-like interfaces support half\-duplex.  Entries in this table are recommended for interfaces capable of operating at 1000 Mb/s or faster, and are required for interfaces capable of operating at 10 Gb/s or faster.  Lower speed ethernet\-like interfaces do not need entries in this table, in which case there may be fewer entries in this table than in the dot3StatsTable. However, implementations containing interfaces with a mix of speeds may choose to implement entries in this table for all ethernet\-like interfaces
    	**type**\:  :py:class:`Dot3HCStatsTable <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3HCStatsTable>`
    
    	**config**\: False
    
    

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
        self._child_classes = OrderedDict([("dot3StatsTable", ("dot3statstable", EtherLikeMIB.Dot3StatsTable)), ("dot3CollTable", ("dot3colltable", EtherLikeMIB.Dot3CollTable)), ("dot3ControlTable", ("dot3controltable", EtherLikeMIB.Dot3ControlTable)), ("dot3PauseTable", ("dot3pausetable", EtherLikeMIB.Dot3PauseTable)), ("dot3HCStatsTable", ("dot3hcstatstable", EtherLikeMIB.Dot3HCStatsTable))])
        self._leafs = OrderedDict()

        self.dot3statstable = EtherLikeMIB.Dot3StatsTable()
        self.dot3statstable.parent = self
        self._children_name_map["dot3statstable"] = "dot3StatsTable"

        self.dot3colltable = EtherLikeMIB.Dot3CollTable()
        self.dot3colltable.parent = self
        self._children_name_map["dot3colltable"] = "dot3CollTable"

        self.dot3controltable = EtherLikeMIB.Dot3ControlTable()
        self.dot3controltable.parent = self
        self._children_name_map["dot3controltable"] = "dot3ControlTable"

        self.dot3pausetable = EtherLikeMIB.Dot3PauseTable()
        self.dot3pausetable.parent = self
        self._children_name_map["dot3pausetable"] = "dot3PauseTable"

        self.dot3hcstatstable = EtherLikeMIB.Dot3HCStatsTable()
        self.dot3hcstatstable.parent = self
        self._children_name_map["dot3hcstatstable"] = "dot3HCStatsTable"
        self._segment_path = lambda: "EtherLike-MIB:EtherLike-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EtherLikeMIB, [], name, value)


    class Dot3StatsTable(Entity):
        """
        Statistics for a collection of ethernet\-like
        interfaces attached to a particular system.
        There will be one row in this table for each
        ethernet\-like interface in the system.
        
        .. attribute:: dot3statsentry
        
        	Statistics for a particular interface to an ethernet\-like medium
        	**type**\: list of  		 :py:class:`Dot3StatsEntry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3StatsTable, self).__init__()

            self.yang_name = "dot3StatsTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot3StatsEntry", ("dot3statsentry", EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry))])
            self._leafs = OrderedDict()

            self.dot3statsentry = YList(self)
            self._segment_path = lambda: "dot3StatsTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3StatsTable, [], name, value)


        class Dot3StatsEntry(Entity):
            """
            Statistics for a particular interface to an
            ethernet\-like medium.
            
            .. attribute:: dot3statsindex  (key)
            
            	An index value that uniquely identifies an interface to an ethernet\-like medium.  The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: dot3statsalignmenterrors
            
            	A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check.  The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter does not increment for group encoding schemes greater than 4 bits per group.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsAlignmentErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsfcserrors
            
            	A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check.  This count does not include frames received with frame\-too\-long or frame\-too\-short error.  The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  Note\:  Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsFCSErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statssinglecollisionframes
            
            	A count of frames that are involved in a single collision, and are subsequently transmitted successfully.  A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsMultipleCollisionFrames object.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsmultiplecollisionframes
            
            	A count of frames that are involved in more than one collision and are subsequently transmitted successfully.  A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts, ifOutMulticastPkts, or ifOutBroadcastPkts, and is not counted by the corresponding instance of the dot3StatsSingleCollisionFrames object.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statssqetesterrors
            
            	A count of times that the SQE TEST ERROR is received on a particular interface. The SQE TEST ERROR is set in accordance with the rules for verification of the SQE detection mechanism in the PLS Carrier Sense Function as described in IEEE Std. 802.3, 2000 Edition, section 7.2.4.6.  This counter does not increment on interfaces operating at speeds greater than 10 Mb/s, or on interfaces operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsdeferredtransmissions
            
            	A count of frames for which the first transmission attempt on a particular interface is delayed because the medium is busy.  The count represented by an instance of this object does not include frames involved in collisions.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statslatecollisions
            
            	The number of times that a collision is detected on a particular interface later than one slotTime into the transmission of a packet.  A (late) collision included in a count represented by an instance of this object is also considered as a (generic) collision for purposes of other collision\-related statistics.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsexcessivecollisions
            
            	A count of frames for which transmission on a particular interface fails due to excessive collisions.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsinternalmactransmiterrors
            
            	A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsInternalMacTransmitErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statscarriersenseerrors
            
            	The number of times that the carrier sense condition was lost or never asserted when attempting to transmit a frame on a particular interface.  The count represented by an instance of this object is incremented at most once per transmission attempt, even if the carrier sense condition fluctuates during a transmission attempt.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsframetoolongs
            
            	A count of frames received on a particular interface that exceed the maximum permitted frame size.  The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 80 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsFrameTooLongs object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsinternalmacreceiveerrors
            
            	A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsInternalMacReceiveErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsetherchipset
            
            	\*\*\*\*\*\*\*\* THIS OBJECT IS DEPRECATED \*\*\*\*\*\*\*\*  This object contains an OBJECT IDENTIFIER which identifies the chipset used to realize the interface. Ethernet\-like interfaces are typically built out of several different chips. The MIB implementor is presented with a decision of which chip to identify via this object. The implementor should identify the chip which is usually called the Medium Access Control chip. If no such chip is easily identifiable, the implementor should identify the chip which actually gathers the transmit and receive statistics and error indications. This would allow a manager station to correlate the statistics and the chip generating them, giving it the ability to take into account any known anomalies in the chip.  This object has been deprecated.  Implementation feedback indicates that it is of limited use for debugging network problems in the field, and the administrative overhead involved in maintaining a registry of chipset OIDs is not justified
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: dot3statssymbolerrors
            
            	For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.  For an interface operating in half\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII.  For an interface operating in full\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII.  For an interface operating at 10 Gb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Receive Error' on the XGMII.  The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event.  This count does not increment if a collision is present.  This counter does not increment when the interface is operating at 10 Mb/s.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCStatsSymbolErrors object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3statsduplexstatus
            
            	The current mode of operation of the MAC entity.  'unknown' indicates that the current duplex mode could not be determined.  Management control of the duplex mode is accomplished through the MAU MIB.  When an interface does not support autonegotiation, or when autonegotiation is not enabled, the duplex mode is controlled using ifMauDefaultType.  When autonegotiation is supported and enabled, duplex mode is controlled using ifMauAutoNegAdvertisedBits.  In either case, the currently operating duplex mode is reflected both in this object and in ifMauType.  Note that this object provides redundant information with ifMauType.  Normally, redundant objects are discouraged.  However, in this instance, it allows a management application to determine the duplex status of an interface without having to know every possible value of ifMauType.  This was felt to be sufficiently valuable to justify the redundancy
            	**type**\:  :py:class:`Dot3StatsDuplexStatus <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry.Dot3StatsDuplexStatus>`
            
            	**config**\: False
            
            .. attribute:: dot3statsratecontrolability
            
            	'true' for interfaces operating at speeds above 1000 Mb/s that support Rate Control through lowering the average data rate of the MAC sublayer, with frame granularity, and 'false' otherwise
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: dot3statsratecontrolstatus
            
            	The current Rate Control mode of operation of the MAC sublayer of this interface
            	**type**\:  :py:class:`Dot3StatsRateControlStatus <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry.Dot3StatsRateControlStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry, self).__init__()

                self.yang_name = "dot3StatsEntry"
                self.yang_parent_name = "dot3StatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', (YLeaf(YType.int32, 'dot3StatsIndex'), ['int'])),
                    ('dot3statsalignmenterrors', (YLeaf(YType.uint32, 'dot3StatsAlignmentErrors'), ['int'])),
                    ('dot3statsfcserrors', (YLeaf(YType.uint32, 'dot3StatsFCSErrors'), ['int'])),
                    ('dot3statssinglecollisionframes', (YLeaf(YType.uint32, 'dot3StatsSingleCollisionFrames'), ['int'])),
                    ('dot3statsmultiplecollisionframes', (YLeaf(YType.uint32, 'dot3StatsMultipleCollisionFrames'), ['int'])),
                    ('dot3statssqetesterrors', (YLeaf(YType.uint32, 'dot3StatsSQETestErrors'), ['int'])),
                    ('dot3statsdeferredtransmissions', (YLeaf(YType.uint32, 'dot3StatsDeferredTransmissions'), ['int'])),
                    ('dot3statslatecollisions', (YLeaf(YType.uint32, 'dot3StatsLateCollisions'), ['int'])),
                    ('dot3statsexcessivecollisions', (YLeaf(YType.uint32, 'dot3StatsExcessiveCollisions'), ['int'])),
                    ('dot3statsinternalmactransmiterrors', (YLeaf(YType.uint32, 'dot3StatsInternalMacTransmitErrors'), ['int'])),
                    ('dot3statscarriersenseerrors', (YLeaf(YType.uint32, 'dot3StatsCarrierSenseErrors'), ['int'])),
                    ('dot3statsframetoolongs', (YLeaf(YType.uint32, 'dot3StatsFrameTooLongs'), ['int'])),
                    ('dot3statsinternalmacreceiveerrors', (YLeaf(YType.uint32, 'dot3StatsInternalMacReceiveErrors'), ['int'])),
                    ('dot3statsetherchipset', (YLeaf(YType.str, 'dot3StatsEtherChipSet'), ['str'])),
                    ('dot3statssymbolerrors', (YLeaf(YType.uint32, 'dot3StatsSymbolErrors'), ['int'])),
                    ('dot3statsduplexstatus', (YLeaf(YType.enumeration, 'dot3StatsDuplexStatus'), [('ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherLikeMIB', 'Dot3StatsTable.Dot3StatsEntry.Dot3StatsDuplexStatus')])),
                    ('dot3statsratecontrolability', (YLeaf(YType.boolean, 'dot3StatsRateControlAbility'), ['bool'])),
                    ('dot3statsratecontrolstatus', (YLeaf(YType.enumeration, 'dot3StatsRateControlStatus'), [('ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherLikeMIB', 'Dot3StatsTable.Dot3StatsEntry.Dot3StatsRateControlStatus')])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry, [u'dot3statsindex', u'dot3statsalignmenterrors', u'dot3statsfcserrors', u'dot3statssinglecollisionframes', u'dot3statsmultiplecollisionframes', u'dot3statssqetesterrors', u'dot3statsdeferredtransmissions', u'dot3statslatecollisions', u'dot3statsexcessivecollisions', u'dot3statsinternalmactransmiterrors', u'dot3statscarriersenseerrors', u'dot3statsframetoolongs', u'dot3statsinternalmacreceiveerrors', u'dot3statsetherchipset', u'dot3statssymbolerrors', u'dot3statsduplexstatus', u'dot3statsratecontrolability', u'dot3statsratecontrolstatus'], name, value)

            class Dot3StatsDuplexStatus(Enum):
                """
                Dot3StatsDuplexStatus (Enum Class)

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


            class Dot3StatsRateControlStatus(Enum):
                """
                Dot3StatsRateControlStatus (Enum Class)

                The current Rate Control mode of operation of

                the MAC sublayer of this interface.

                .. data:: rateControlOff = 1

                .. data:: rateControlOn = 2

                .. data:: unknown = 3

                """

                rateControlOff = Enum.YLeaf(1, "rateControlOff")

                rateControlOn = Enum.YLeaf(2, "rateControlOn")

                unknown = Enum.YLeaf(3, "unknown")





    class Dot3CollTable(Entity):
        """
        A collection of collision histograms for a
        particular set of interfaces.
        
        .. attribute:: dot3collentry
        
        	A cell in the histogram of per\-frame collisions for a particular interface.  An instance of this object represents the frequency of individual MAC frames for which the transmission (successful or otherwise) on a particular interface is accompanied by a particular number of media collisions
        	**type**\: list of  		 :py:class:`Dot3CollEntry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3CollTable.Dot3CollEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3CollTable, self).__init__()

            self.yang_name = "dot3CollTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot3CollEntry", ("dot3collentry", EtherLikeMIB.Dot3CollTable.Dot3CollEntry))])
            self._leafs = OrderedDict()

            self.dot3collentry = YList(self)
            self._segment_path = lambda: "dot3CollTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3CollTable, [], name, value)


        class Dot3CollEntry(Entity):
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
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: dot3collcount  (key)
            
            	The number of per\-frame media collisions for which a particular collision histogram cell represents the frequency on a particular interface
            	**type**\: int
            
            	**range:** 1..16
            
            	**config**\: False
            
            .. attribute:: dot3collfrequencies
            
            	A count of individual MAC frames for which the transmission (successful or otherwise) on a particular interface occurs after the frame has experienced exactly the number of collisions in the associated dot3CollCount object.  For example, a frame which is transmitted on interface 77 after experiencing exactly 4 collisions would be indicated by incrementing only dot3CollFrequencies.77.4. No other instance of dot3CollFrequencies would be incremented in this example.  This counter does not increment when the interface is operating in full\-duplex mode.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3CollTable.Dot3CollEntry, self).__init__()

                self.yang_name = "dot3CollEntry"
                self.yang_parent_name = "dot3CollTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','dot3collcount']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('dot3collcount', (YLeaf(YType.int32, 'dot3CollCount'), ['int'])),
                    ('dot3collfrequencies', (YLeaf(YType.uint32, 'dot3CollFrequencies'), ['int'])),
                ])
                self.ifindex = None
                self.dot3collcount = None
                self.dot3collfrequencies = None
                self._segment_path = lambda: "dot3CollEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[dot3CollCount='" + str(self.dot3collcount) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3CollTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3CollTable.Dot3CollEntry, [u'ifindex', u'dot3collcount', u'dot3collfrequencies'], name, value)




    class Dot3ControlTable(Entity):
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
        	**type**\: list of  		 :py:class:`Dot3ControlEntry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3ControlTable.Dot3ControlEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3ControlTable, self).__init__()

            self.yang_name = "dot3ControlTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot3ControlEntry", ("dot3controlentry", EtherLikeMIB.Dot3ControlTable.Dot3ControlEntry))])
            self._leafs = OrderedDict()

            self.dot3controlentry = YList(self)
            self._segment_path = lambda: "dot3ControlTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3ControlTable, [], name, value)


        class Dot3ControlEntry(Entity):
            """
            An entry in the table, containing information
            about the MAC Control sublayer on a single
            ethernet\-like interface.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry>`
            
            	**config**\: False
            
            .. attribute:: dot3controlfunctionssupported
            
            	A list of the possible MAC Control functions implemented for this interface
            	**type**\:  :py:class:`Dot3ControlFunctionsSupported <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3ControlTable.Dot3ControlEntry.Dot3ControlFunctionsSupported>`
            
            	**config**\: False
            
            .. attribute:: dot3controlinunknownopcodes
            
            	A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCControlInUnknownOpcodes object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3hccontrolinunknownopcodes
            
            	A count of MAC Control frames received on this interface that contain an opcode that is not supported by this device.  This counter is a 64 bit version of dot3ControlInUnknownOpcodes.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3ControlTable.Dot3ControlEntry, self).__init__()

                self.yang_name = "dot3ControlEntry"
                self.yang_parent_name = "dot3ControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', (YLeaf(YType.str, 'dot3StatsIndex'), ['int'])),
                    ('dot3controlfunctionssupported', (YLeaf(YType.bits, 'dot3ControlFunctionsSupported'), ['Bits'])),
                    ('dot3controlinunknownopcodes', (YLeaf(YType.uint32, 'dot3ControlInUnknownOpcodes'), ['int'])),
                    ('dot3hccontrolinunknownopcodes', (YLeaf(YType.uint64, 'dot3HCControlInUnknownOpcodes'), ['int'])),
                ])
                self.dot3statsindex = None
                self.dot3controlfunctionssupported = Bits()
                self.dot3controlinunknownopcodes = None
                self.dot3hccontrolinunknownopcodes = None
                self._segment_path = lambda: "dot3ControlEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/dot3ControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3ControlTable.Dot3ControlEntry, [u'dot3statsindex', u'dot3controlfunctionssupported', u'dot3controlinunknownopcodes', u'dot3hccontrolinunknownopcodes'], name, value)




    class Dot3PauseTable(Entity):
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
        	**type**\: list of  		 :py:class:`Dot3PauseEntry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3PauseTable.Dot3PauseEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3PauseTable, self).__init__()

            self.yang_name = "dot3PauseTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot3PauseEntry", ("dot3pauseentry", EtherLikeMIB.Dot3PauseTable.Dot3PauseEntry))])
            self._leafs = OrderedDict()

            self.dot3pauseentry = YList(self)
            self._segment_path = lambda: "dot3PauseTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3PauseTable, [], name, value)


        class Dot3PauseEntry(Entity):
            """
            An entry in the table, containing information
            about the MAC Control PAUSE function on a single
            ethernet\-like interface.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry>`
            
            	**config**\: False
            
            .. attribute:: dot3pauseadminmode
            
            	This object is used to configure the default administrative PAUSE mode for this interface.  This object represents the administratively\-configured PAUSE mode for this interface.  If auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, the value of this object determines the operational PAUSE mode of the interface whenever it is operating in full\-duplex mode.  In this case, a set to this object will force the interface into the specified mode.  If auto\-negotiation is implemented and enabled for the MAU attached to this interface, the PAUSE mode for this interface is determined by auto\-negotiation, and the value of this object denotes the mode to which the interface will automatically revert if/when auto\-negotiation is later disabled.  Note that when auto\-negotiation is running, administrative control of the PAUSE mode may be accomplished using the ifMauAutoNegCapAdvertisedBits object in the MAU\-MIB.  Note that the value of this object is ignored when the interface is not operating in full\-duplex mode.  An attempt to set this object to 'enabledXmit(2)' or 'enabledRcv(3)' will fail on interfaces that do not support operation at greater than 100 Mb/s
            	**type**\:  :py:class:`Dot3PauseAdminMode <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3PauseTable.Dot3PauseEntry.Dot3PauseAdminMode>`
            
            	**config**\: False
            
            .. attribute:: dot3pauseopermode
            
            	This object reflects the PAUSE mode currently in use on this interface, as determined by either (1) the result of the auto\-negotiation function or (2) if auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, by the value of dot3PauseAdminMode.  Interfaces operating at 100 Mb/s or less will never return 'enabledXmit(2)' or 'enabledRcv(3)'.  Interfaces operating in half\-duplex mode will always return 'disabled(1)'.  Interfaces on which auto\-negotiation is enabled but not yet completed should return the value 'disabled(1)'
            	**type**\:  :py:class:`Dot3PauseOperMode <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3PauseTable.Dot3PauseEntry.Dot3PauseOperMode>`
            
            	**config**\: False
            
            .. attribute:: dot3inpauseframes
            
            	A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCInPauseFrames object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3outpauseframes
            
            	A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  For interfaces operating at 10 Gb/s, this counter can roll over in less than 5 minutes if it is incrementing at its maximum rate.  Since that amount of time could be less than a management station's poll cycle time, in order to avoid a loss of information, a management station is advised to poll the dot3HCOutPauseFrames object for 10 Gb/s or faster interfaces.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dot3hcinpauseframes
            
            	A count of MAC Control frames received on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  This counter is a 64 bit version of dot3InPauseFrames.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot3hcoutpauseframes
            
            	A count of MAC Control frames transmitted on this interface with an opcode indicating the PAUSE operation.  This counter does not increment when the interface is operating in half\-duplex mode.  This counter is a 64 bit version of dot3OutPauseFrames.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3PauseTable.Dot3PauseEntry, self).__init__()

                self.yang_name = "dot3PauseEntry"
                self.yang_parent_name = "dot3PauseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', (YLeaf(YType.str, 'dot3StatsIndex'), ['int'])),
                    ('dot3pauseadminmode', (YLeaf(YType.enumeration, 'dot3PauseAdminMode'), [('ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherLikeMIB', 'Dot3PauseTable.Dot3PauseEntry.Dot3PauseAdminMode')])),
                    ('dot3pauseopermode', (YLeaf(YType.enumeration, 'dot3PauseOperMode'), [('ydk.models.cisco_ios_xe.EtherLike_MIB', 'EtherLikeMIB', 'Dot3PauseTable.Dot3PauseEntry.Dot3PauseOperMode')])),
                    ('dot3inpauseframes', (YLeaf(YType.uint32, 'dot3InPauseFrames'), ['int'])),
                    ('dot3outpauseframes', (YLeaf(YType.uint32, 'dot3OutPauseFrames'), ['int'])),
                    ('dot3hcinpauseframes', (YLeaf(YType.uint64, 'dot3HCInPauseFrames'), ['int'])),
                    ('dot3hcoutpauseframes', (YLeaf(YType.uint64, 'dot3HCOutPauseFrames'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3PauseTable.Dot3PauseEntry, [u'dot3statsindex', u'dot3pauseadminmode', u'dot3pauseopermode', u'dot3inpauseframes', u'dot3outpauseframes', u'dot3hcinpauseframes', u'dot3hcoutpauseframes'], name, value)

            class Dot3PauseAdminMode(Enum):
                """
                Dot3PauseAdminMode (Enum Class)

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


            class Dot3PauseOperMode(Enum):
                """
                Dot3PauseOperMode (Enum Class)

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





    class Dot3HCStatsTable(Entity):
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
        	**type**\: list of  		 :py:class:`Dot3HCStatsEntry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3HCStatsTable.Dot3HCStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherLikeMIB.Dot3HCStatsTable, self).__init__()

            self.yang_name = "dot3HCStatsTable"
            self.yang_parent_name = "EtherLike-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("dot3HCStatsEntry", ("dot3hcstatsentry", EtherLikeMIB.Dot3HCStatsTable.Dot3HCStatsEntry))])
            self._leafs = OrderedDict()

            self.dot3hcstatsentry = YList(self)
            self._segment_path = lambda: "dot3HCStatsTable"
            self._absolute_path = lambda: "EtherLike-MIB:EtherLike-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLikeMIB.Dot3HCStatsTable, [], name, value)


        class Dot3HCStatsEntry(Entity):
            """
            An entry containing 64\-bit statistics for a
            single ethernet\-like interface.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry>`
            
            	**config**\: False
            
            .. attribute:: dot3hcstatsalignmenterrors
            
            	A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check.  The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter does not increment for group encoding schemes greater than 4 bits per group.  This counter is a 64 bit version of dot3StatsAlignmentErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot3hcstatsfcserrors
            
            	A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check.  This count does not include frames received with frame\-too\-long or frame\-too\-short error.  The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  Note\:  Coding errors detected by the physical layer for speeds above 10 Mb/s will cause the frame to fail the FCS check.  This counter is a 64 bit version of dot3StatsFCSErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot3hcstatsinternalmactransmiterrors
            
            	A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsLateCollisions object, the dot3StatsExcessiveCollisions object, or the dot3StatsCarrierSenseErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.  This counter is a 64 bit version of dot3StatsInternalMacTransmitErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot3hcstatsframetoolongs
            
            	A count of frames received on a particular interface that exceed the maximum permitted frame size.  The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions pertain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.  This counter is a 64 bit version of dot3StatsFrameTooLongs.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot3hcstatsinternalmacreceiveerrors
            
            	A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the dot3StatsFrameTooLongs object, the dot3StatsAlignmentErrors object, or the dot3StatsFCSErrors object.  The precise meaning of the count represented by an instance of this object is implementation\- specific.  In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.  This counter is a 64 bit version of dot3StatsInternalMacReceiveErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: dot3hcstatssymbolerrors
            
            	For an interface operating at 100 Mb/s, the number of times there was an invalid data symbol when a valid carrier was present.  For an interface operating in half\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than slotTime, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' or 'carrier extend error' on the GMII.  For an interface operating in full\-duplex mode at 1000 Mb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Data reception error' on the GMII.  For an interface operating at 10 Gb/s, the number of times the receiving media is non\-idle (a carrier event) for a period of time equal to or greater than minFrameSize, and during which there was at least one occurrence of an event that causes the PHY to indicate 'Receive Error' on the XGMII.  The count represented by an instance of this object is incremented at most once per carrier event, even if multiple symbol errors occur during the carrier event.  This count does not increment if a collision is present.  This counter is a 64 bit version of dot3StatsSymbolErrors.  It should be used on interfaces operating at 10 Gb/s or faster.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherLikeMIB.Dot3HCStatsTable.Dot3HCStatsEntry, self).__init__()

                self.yang_name = "dot3HCStatsEntry"
                self.yang_parent_name = "dot3HCStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', (YLeaf(YType.str, 'dot3StatsIndex'), ['int'])),
                    ('dot3hcstatsalignmenterrors', (YLeaf(YType.uint64, 'dot3HCStatsAlignmentErrors'), ['int'])),
                    ('dot3hcstatsfcserrors', (YLeaf(YType.uint64, 'dot3HCStatsFCSErrors'), ['int'])),
                    ('dot3hcstatsinternalmactransmiterrors', (YLeaf(YType.uint64, 'dot3HCStatsInternalMacTransmitErrors'), ['int'])),
                    ('dot3hcstatsframetoolongs', (YLeaf(YType.uint64, 'dot3HCStatsFrameTooLongs'), ['int'])),
                    ('dot3hcstatsinternalmacreceiveerrors', (YLeaf(YType.uint64, 'dot3HCStatsInternalMacReceiveErrors'), ['int'])),
                    ('dot3hcstatssymbolerrors', (YLeaf(YType.uint64, 'dot3HCStatsSymbolErrors'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLikeMIB.Dot3HCStatsTable.Dot3HCStatsEntry, [u'dot3statsindex', u'dot3hcstatsalignmenterrors', u'dot3hcstatsfcserrors', u'dot3hcstatsinternalmactransmiterrors', u'dot3hcstatsframetoolongs', u'dot3hcstatsinternalmacreceiveerrors', u'dot3hcstatssymbolerrors'], name, value)



    def clone_ptr(self):
        self._top_entity = EtherLikeMIB()
        return self._top_entity



