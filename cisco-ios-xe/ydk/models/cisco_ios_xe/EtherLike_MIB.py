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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



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


class EtherlikeMib(Entity):
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
        super(EtherlikeMib, self).__init__()
        self._top_entity = None

        self.yang_name = "EtherLike-MIB"
        self.yang_parent_name = "EtherLike-MIB"

        self.dot3colltable = EtherlikeMib.Dot3Colltable()
        self.dot3colltable.parent = self
        self._children_name_map["dot3colltable"] = "dot3CollTable"
        self._children_yang_names.add("dot3CollTable")

        self.dot3controltable = EtherlikeMib.Dot3Controltable()
        self.dot3controltable.parent = self
        self._children_name_map["dot3controltable"] = "dot3ControlTable"
        self._children_yang_names.add("dot3ControlTable")

        self.dot3hcstatstable = EtherlikeMib.Dot3Hcstatstable()
        self.dot3hcstatstable.parent = self
        self._children_name_map["dot3hcstatstable"] = "dot3HCStatsTable"
        self._children_yang_names.add("dot3HCStatsTable")

        self.dot3pausetable = EtherlikeMib.Dot3Pausetable()
        self.dot3pausetable.parent = self
        self._children_name_map["dot3pausetable"] = "dot3PauseTable"
        self._children_yang_names.add("dot3PauseTable")

        self.dot3statstable = EtherlikeMib.Dot3Statstable()
        self.dot3statstable.parent = self
        self._children_name_map["dot3statstable"] = "dot3StatsTable"
        self._children_yang_names.add("dot3StatsTable")


    class Dot3Statstable(Entity):
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
            super(EtherlikeMib.Dot3Statstable, self).__init__()

            self.yang_name = "dot3StatsTable"
            self.yang_parent_name = "EtherLike-MIB"

            self.dot3statsentry = YList(self)

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
                        super(EtherlikeMib.Dot3Statstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherlikeMib.Dot3Statstable, self).__setattr__(name, value)


        class Dot3Statsentry(Entity):
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
            	**type**\:   :py:class:`Dot3Statsduplexstatus <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3Statsduplexstatus>`
            
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
            	**type**\:   :py:class:`Dot3Statsratecontrolstatus <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry.Dot3Statsratecontrolstatus>`
            
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
                super(EtherlikeMib.Dot3Statstable.Dot3Statsentry, self).__init__()

                self.yang_name = "dot3StatsEntry"
                self.yang_parent_name = "dot3StatsTable"

                self.dot3statsindex = YLeaf(YType.int32, "dot3StatsIndex")

                self.dot3statsalignmenterrors = YLeaf(YType.uint32, "dot3StatsAlignmentErrors")

                self.dot3statscarriersenseerrors = YLeaf(YType.uint32, "dot3StatsCarrierSenseErrors")

                self.dot3statsdeferredtransmissions = YLeaf(YType.uint32, "dot3StatsDeferredTransmissions")

                self.dot3statsduplexstatus = YLeaf(YType.enumeration, "dot3StatsDuplexStatus")

                self.dot3statsetherchipset = YLeaf(YType.str, "dot3StatsEtherChipSet")

                self.dot3statsexcessivecollisions = YLeaf(YType.uint32, "dot3StatsExcessiveCollisions")

                self.dot3statsfcserrors = YLeaf(YType.uint32, "dot3StatsFCSErrors")

                self.dot3statsframetoolongs = YLeaf(YType.uint32, "dot3StatsFrameTooLongs")

                self.dot3statsinternalmacreceiveerrors = YLeaf(YType.uint32, "dot3StatsInternalMacReceiveErrors")

                self.dot3statsinternalmactransmiterrors = YLeaf(YType.uint32, "dot3StatsInternalMacTransmitErrors")

                self.dot3statslatecollisions = YLeaf(YType.uint32, "dot3StatsLateCollisions")

                self.dot3statsmultiplecollisionframes = YLeaf(YType.uint32, "dot3StatsMultipleCollisionFrames")

                self.dot3statsratecontrolability = YLeaf(YType.boolean, "dot3StatsRateControlAbility")

                self.dot3statsratecontrolstatus = YLeaf(YType.enumeration, "dot3StatsRateControlStatus")

                self.dot3statssinglecollisionframes = YLeaf(YType.uint32, "dot3StatsSingleCollisionFrames")

                self.dot3statssqetesterrors = YLeaf(YType.uint32, "dot3StatsSQETestErrors")

                self.dot3statssymbolerrors = YLeaf(YType.uint32, "dot3StatsSymbolErrors")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot3statsindex",
                                "dot3statsalignmenterrors",
                                "dot3statscarriersenseerrors",
                                "dot3statsdeferredtransmissions",
                                "dot3statsduplexstatus",
                                "dot3statsetherchipset",
                                "dot3statsexcessivecollisions",
                                "dot3statsfcserrors",
                                "dot3statsframetoolongs",
                                "dot3statsinternalmacreceiveerrors",
                                "dot3statsinternalmactransmiterrors",
                                "dot3statslatecollisions",
                                "dot3statsmultiplecollisionframes",
                                "dot3statsratecontrolability",
                                "dot3statsratecontrolstatus",
                                "dot3statssinglecollisionframes",
                                "dot3statssqetesterrors",
                                "dot3statssymbolerrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherlikeMib.Dot3Statstable.Dot3Statsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherlikeMib.Dot3Statstable.Dot3Statsentry, self).__setattr__(name, value)

            class Dot3Statsduplexstatus(Enum):
                """
                Dot3Statsduplexstatus

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
                Dot3Statsratecontrolstatus

                The current Rate Control mode of operation of

                the MAC sublayer of this interface.

                .. data:: rateControlOff = 1

                .. data:: rateControlOn = 2

                .. data:: unknown = 3

                """

                rateControlOff = Enum.YLeaf(1, "rateControlOff")

                rateControlOn = Enum.YLeaf(2, "rateControlOn")

                unknown = Enum.YLeaf(3, "unknown")


            def has_data(self):
                return (
                    self.dot3statsindex.is_set or
                    self.dot3statsalignmenterrors.is_set or
                    self.dot3statscarriersenseerrors.is_set or
                    self.dot3statsdeferredtransmissions.is_set or
                    self.dot3statsduplexstatus.is_set or
                    self.dot3statsetherchipset.is_set or
                    self.dot3statsexcessivecollisions.is_set or
                    self.dot3statsfcserrors.is_set or
                    self.dot3statsframetoolongs.is_set or
                    self.dot3statsinternalmacreceiveerrors.is_set or
                    self.dot3statsinternalmactransmiterrors.is_set or
                    self.dot3statslatecollisions.is_set or
                    self.dot3statsmultiplecollisionframes.is_set or
                    self.dot3statsratecontrolability.is_set or
                    self.dot3statsratecontrolstatus.is_set or
                    self.dot3statssinglecollisionframes.is_set or
                    self.dot3statssqetesterrors.is_set or
                    self.dot3statssymbolerrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot3statsindex.yfilter != YFilter.not_set or
                    self.dot3statsalignmenterrors.yfilter != YFilter.not_set or
                    self.dot3statscarriersenseerrors.yfilter != YFilter.not_set or
                    self.dot3statsdeferredtransmissions.yfilter != YFilter.not_set or
                    self.dot3statsduplexstatus.yfilter != YFilter.not_set or
                    self.dot3statsetherchipset.yfilter != YFilter.not_set or
                    self.dot3statsexcessivecollisions.yfilter != YFilter.not_set or
                    self.dot3statsfcserrors.yfilter != YFilter.not_set or
                    self.dot3statsframetoolongs.yfilter != YFilter.not_set or
                    self.dot3statsinternalmacreceiveerrors.yfilter != YFilter.not_set or
                    self.dot3statsinternalmactransmiterrors.yfilter != YFilter.not_set or
                    self.dot3statslatecollisions.yfilter != YFilter.not_set or
                    self.dot3statsmultiplecollisionframes.yfilter != YFilter.not_set or
                    self.dot3statsratecontrolability.yfilter != YFilter.not_set or
                    self.dot3statsratecontrolstatus.yfilter != YFilter.not_set or
                    self.dot3statssinglecollisionframes.yfilter != YFilter.not_set or
                    self.dot3statssqetesterrors.yfilter != YFilter.not_set or
                    self.dot3statssymbolerrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot3StatsEntry" + "[dot3StatsIndex='" + self.dot3statsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EtherLike-MIB:EtherLike-MIB/dot3StatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot3statsindex.is_set or self.dot3statsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsindex.get_name_leafdata())
                if (self.dot3statsalignmenterrors.is_set or self.dot3statsalignmenterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsalignmenterrors.get_name_leafdata())
                if (self.dot3statscarriersenseerrors.is_set or self.dot3statscarriersenseerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statscarriersenseerrors.get_name_leafdata())
                if (self.dot3statsdeferredtransmissions.is_set or self.dot3statsdeferredtransmissions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsdeferredtransmissions.get_name_leafdata())
                if (self.dot3statsduplexstatus.is_set or self.dot3statsduplexstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsduplexstatus.get_name_leafdata())
                if (self.dot3statsetherchipset.is_set or self.dot3statsetherchipset.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsetherchipset.get_name_leafdata())
                if (self.dot3statsexcessivecollisions.is_set or self.dot3statsexcessivecollisions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsexcessivecollisions.get_name_leafdata())
                if (self.dot3statsfcserrors.is_set or self.dot3statsfcserrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsfcserrors.get_name_leafdata())
                if (self.dot3statsframetoolongs.is_set or self.dot3statsframetoolongs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsframetoolongs.get_name_leafdata())
                if (self.dot3statsinternalmacreceiveerrors.is_set or self.dot3statsinternalmacreceiveerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsinternalmacreceiveerrors.get_name_leafdata())
                if (self.dot3statsinternalmactransmiterrors.is_set or self.dot3statsinternalmactransmiterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsinternalmactransmiterrors.get_name_leafdata())
                if (self.dot3statslatecollisions.is_set or self.dot3statslatecollisions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statslatecollisions.get_name_leafdata())
                if (self.dot3statsmultiplecollisionframes.is_set or self.dot3statsmultiplecollisionframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsmultiplecollisionframes.get_name_leafdata())
                if (self.dot3statsratecontrolability.is_set or self.dot3statsratecontrolability.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsratecontrolability.get_name_leafdata())
                if (self.dot3statsratecontrolstatus.is_set or self.dot3statsratecontrolstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsratecontrolstatus.get_name_leafdata())
                if (self.dot3statssinglecollisionframes.is_set or self.dot3statssinglecollisionframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statssinglecollisionframes.get_name_leafdata())
                if (self.dot3statssqetesterrors.is_set or self.dot3statssqetesterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statssqetesterrors.get_name_leafdata())
                if (self.dot3statssymbolerrors.is_set or self.dot3statssymbolerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statssymbolerrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot3StatsIndex" or name == "dot3StatsAlignmentErrors" or name == "dot3StatsCarrierSenseErrors" or name == "dot3StatsDeferredTransmissions" or name == "dot3StatsDuplexStatus" or name == "dot3StatsEtherChipSet" or name == "dot3StatsExcessiveCollisions" or name == "dot3StatsFCSErrors" or name == "dot3StatsFrameTooLongs" or name == "dot3StatsInternalMacReceiveErrors" or name == "dot3StatsInternalMacTransmitErrors" or name == "dot3StatsLateCollisions" or name == "dot3StatsMultipleCollisionFrames" or name == "dot3StatsRateControlAbility" or name == "dot3StatsRateControlStatus" or name == "dot3StatsSingleCollisionFrames" or name == "dot3StatsSQETestErrors" or name == "dot3StatsSymbolErrors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot3StatsIndex"):
                    self.dot3statsindex = value
                    self.dot3statsindex.value_namespace = name_space
                    self.dot3statsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsAlignmentErrors"):
                    self.dot3statsalignmenterrors = value
                    self.dot3statsalignmenterrors.value_namespace = name_space
                    self.dot3statsalignmenterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsCarrierSenseErrors"):
                    self.dot3statscarriersenseerrors = value
                    self.dot3statscarriersenseerrors.value_namespace = name_space
                    self.dot3statscarriersenseerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsDeferredTransmissions"):
                    self.dot3statsdeferredtransmissions = value
                    self.dot3statsdeferredtransmissions.value_namespace = name_space
                    self.dot3statsdeferredtransmissions.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsDuplexStatus"):
                    self.dot3statsduplexstatus = value
                    self.dot3statsduplexstatus.value_namespace = name_space
                    self.dot3statsduplexstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsEtherChipSet"):
                    self.dot3statsetherchipset = value
                    self.dot3statsetherchipset.value_namespace = name_space
                    self.dot3statsetherchipset.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsExcessiveCollisions"):
                    self.dot3statsexcessivecollisions = value
                    self.dot3statsexcessivecollisions.value_namespace = name_space
                    self.dot3statsexcessivecollisions.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsFCSErrors"):
                    self.dot3statsfcserrors = value
                    self.dot3statsfcserrors.value_namespace = name_space
                    self.dot3statsfcserrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsFrameTooLongs"):
                    self.dot3statsframetoolongs = value
                    self.dot3statsframetoolongs.value_namespace = name_space
                    self.dot3statsframetoolongs.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsInternalMacReceiveErrors"):
                    self.dot3statsinternalmacreceiveerrors = value
                    self.dot3statsinternalmacreceiveerrors.value_namespace = name_space
                    self.dot3statsinternalmacreceiveerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsInternalMacTransmitErrors"):
                    self.dot3statsinternalmactransmiterrors = value
                    self.dot3statsinternalmactransmiterrors.value_namespace = name_space
                    self.dot3statsinternalmactransmiterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsLateCollisions"):
                    self.dot3statslatecollisions = value
                    self.dot3statslatecollisions.value_namespace = name_space
                    self.dot3statslatecollisions.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsMultipleCollisionFrames"):
                    self.dot3statsmultiplecollisionframes = value
                    self.dot3statsmultiplecollisionframes.value_namespace = name_space
                    self.dot3statsmultiplecollisionframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsRateControlAbility"):
                    self.dot3statsratecontrolability = value
                    self.dot3statsratecontrolability.value_namespace = name_space
                    self.dot3statsratecontrolability.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsRateControlStatus"):
                    self.dot3statsratecontrolstatus = value
                    self.dot3statsratecontrolstatus.value_namespace = name_space
                    self.dot3statsratecontrolstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsSingleCollisionFrames"):
                    self.dot3statssinglecollisionframes = value
                    self.dot3statssinglecollisionframes.value_namespace = name_space
                    self.dot3statssinglecollisionframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsSQETestErrors"):
                    self.dot3statssqetesterrors = value
                    self.dot3statssqetesterrors.value_namespace = name_space
                    self.dot3statssqetesterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3StatsSymbolErrors"):
                    self.dot3statssymbolerrors = value
                    self.dot3statssymbolerrors.value_namespace = name_space
                    self.dot3statssymbolerrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot3statsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot3statsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot3StatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EtherLike-MIB:EtherLike-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot3StatsEntry"):
                for c in self.dot3statsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherlikeMib.Dot3Statstable.Dot3Statsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot3statsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot3StatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot3Colltable(Entity):
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
            super(EtherlikeMib.Dot3Colltable, self).__init__()

            self.yang_name = "dot3CollTable"
            self.yang_parent_name = "EtherLike-MIB"

            self.dot3collentry = YList(self)

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
                        super(EtherlikeMib.Dot3Colltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherlikeMib.Dot3Colltable, self).__setattr__(name, value)


        class Dot3Collentry(Entity):
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
                super(EtherlikeMib.Dot3Colltable.Dot3Collentry, self).__init__()

                self.yang_name = "dot3CollEntry"
                self.yang_parent_name = "dot3CollTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.dot3collcount = YLeaf(YType.int32, "dot3CollCount")

                self.dot3collfrequencies = YLeaf(YType.uint32, "dot3CollFrequencies")

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
                                "dot3collcount",
                                "dot3collfrequencies") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherlikeMib.Dot3Colltable.Dot3Collentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherlikeMib.Dot3Colltable.Dot3Collentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.dot3collcount.is_set or
                    self.dot3collfrequencies.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.dot3collcount.yfilter != YFilter.not_set or
                    self.dot3collfrequencies.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot3CollEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[dot3CollCount='" + self.dot3collcount.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EtherLike-MIB:EtherLike-MIB/dot3CollTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.dot3collcount.is_set or self.dot3collcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3collcount.get_name_leafdata())
                if (self.dot3collfrequencies.is_set or self.dot3collfrequencies.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3collfrequencies.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "dot3CollCount" or name == "dot3CollFrequencies"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3CollCount"):
                    self.dot3collcount = value
                    self.dot3collcount.value_namespace = name_space
                    self.dot3collcount.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3CollFrequencies"):
                    self.dot3collfrequencies = value
                    self.dot3collfrequencies.value_namespace = name_space
                    self.dot3collfrequencies.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot3collentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot3collentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot3CollTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EtherLike-MIB:EtherLike-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot3CollEntry"):
                for c in self.dot3collentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherlikeMib.Dot3Colltable.Dot3Collentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot3collentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot3CollEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Dot3Controlentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Controltable.Dot3Controlentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherlikeMib.Dot3Controltable, self).__init__()

            self.yang_name = "dot3ControlTable"
            self.yang_parent_name = "EtherLike-MIB"

            self.dot3controlentry = YList(self)

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
                        super(EtherlikeMib.Dot3Controltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherlikeMib.Dot3Controltable, self).__setattr__(name, value)


        class Dot3Controlentry(Entity):
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
                super(EtherlikeMib.Dot3Controltable.Dot3Controlentry, self).__init__()

                self.yang_name = "dot3ControlEntry"
                self.yang_parent_name = "dot3ControlTable"

                self.dot3statsindex = YLeaf(YType.str, "dot3StatsIndex")

                self.dot3controlfunctionssupported = YLeaf(YType.bits, "dot3ControlFunctionsSupported")

                self.dot3controlinunknownopcodes = YLeaf(YType.uint32, "dot3ControlInUnknownOpcodes")

                self.dot3hccontrolinunknownopcodes = YLeaf(YType.uint64, "dot3HCControlInUnknownOpcodes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot3statsindex",
                                "dot3controlfunctionssupported",
                                "dot3controlinunknownopcodes",
                                "dot3hccontrolinunknownopcodes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherlikeMib.Dot3Controltable.Dot3Controlentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherlikeMib.Dot3Controltable.Dot3Controlentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot3statsindex.is_set or
                    self.dot3controlfunctionssupported.is_set or
                    self.dot3controlinunknownopcodes.is_set or
                    self.dot3hccontrolinunknownopcodes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot3statsindex.yfilter != YFilter.not_set or
                    self.dot3controlfunctionssupported.yfilter != YFilter.not_set or
                    self.dot3controlinunknownopcodes.yfilter != YFilter.not_set or
                    self.dot3hccontrolinunknownopcodes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot3ControlEntry" + "[dot3StatsIndex='" + self.dot3statsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EtherLike-MIB:EtherLike-MIB/dot3ControlTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot3statsindex.is_set or self.dot3statsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsindex.get_name_leafdata())
                if (self.dot3controlfunctionssupported.is_set or self.dot3controlfunctionssupported.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3controlfunctionssupported.get_name_leafdata())
                if (self.dot3controlinunknownopcodes.is_set or self.dot3controlinunknownopcodes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3controlinunknownopcodes.get_name_leafdata())
                if (self.dot3hccontrolinunknownopcodes.is_set or self.dot3hccontrolinunknownopcodes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hccontrolinunknownopcodes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot3StatsIndex" or name == "dot3ControlFunctionsSupported" or name == "dot3ControlInUnknownOpcodes" or name == "dot3HCControlInUnknownOpcodes"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot3StatsIndex"):
                    self.dot3statsindex = value
                    self.dot3statsindex.value_namespace = name_space
                    self.dot3statsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3ControlFunctionsSupported"):
                    self.dot3controlfunctionssupported[value] = True
                if(value_path == "dot3ControlInUnknownOpcodes"):
                    self.dot3controlinunknownopcodes = value
                    self.dot3controlinunknownopcodes.value_namespace = name_space
                    self.dot3controlinunknownopcodes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCControlInUnknownOpcodes"):
                    self.dot3hccontrolinunknownopcodes = value
                    self.dot3hccontrolinunknownopcodes.value_namespace = name_space
                    self.dot3hccontrolinunknownopcodes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot3controlentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot3controlentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot3ControlTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EtherLike-MIB:EtherLike-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot3ControlEntry"):
                for c in self.dot3controlentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherlikeMib.Dot3Controltable.Dot3Controlentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot3controlentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot3ControlEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Dot3Pauseentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable.Dot3Pauseentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherlikeMib.Dot3Pausetable, self).__init__()

            self.yang_name = "dot3PauseTable"
            self.yang_parent_name = "EtherLike-MIB"

            self.dot3pauseentry = YList(self)

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
                        super(EtherlikeMib.Dot3Pausetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherlikeMib.Dot3Pausetable, self).__setattr__(name, value)


        class Dot3Pauseentry(Entity):
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
            	**type**\:   :py:class:`Dot3Pauseadminmode <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3Pauseadminmode>`
            
            .. attribute:: dot3pauseopermode
            
            	This object reflects the PAUSE mode currently in use on this interface, as determined by either (1) the result of the auto\-negotiation function or (2) if auto\-negotiation is not enabled or is not implemented for the active MAU attached to this interface, by the value of dot3PauseAdminMode.  Interfaces operating at 100 Mb/s or less will never return 'enabledXmit(2)' or 'enabledRcv(3)'.  Interfaces operating in half\-duplex mode will always return 'disabled(1)'.  Interfaces on which auto\-negotiation is enabled but not yet completed should return the value 'disabled(1)'
            	**type**\:   :py:class:`Dot3Pauseopermode <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Pausetable.Dot3Pauseentry.Dot3Pauseopermode>`
            
            

            """

            _prefix = 'EtherLike-MIB'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherlikeMib.Dot3Pausetable.Dot3Pauseentry, self).__init__()

                self.yang_name = "dot3PauseEntry"
                self.yang_parent_name = "dot3PauseTable"

                self.dot3statsindex = YLeaf(YType.str, "dot3StatsIndex")

                self.dot3hcinpauseframes = YLeaf(YType.uint64, "dot3HCInPauseFrames")

                self.dot3hcoutpauseframes = YLeaf(YType.uint64, "dot3HCOutPauseFrames")

                self.dot3inpauseframes = YLeaf(YType.uint32, "dot3InPauseFrames")

                self.dot3outpauseframes = YLeaf(YType.uint32, "dot3OutPauseFrames")

                self.dot3pauseadminmode = YLeaf(YType.enumeration, "dot3PauseAdminMode")

                self.dot3pauseopermode = YLeaf(YType.enumeration, "dot3PauseOperMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot3statsindex",
                                "dot3hcinpauseframes",
                                "dot3hcoutpauseframes",
                                "dot3inpauseframes",
                                "dot3outpauseframes",
                                "dot3pauseadminmode",
                                "dot3pauseopermode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherlikeMib.Dot3Pausetable.Dot3Pauseentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherlikeMib.Dot3Pausetable.Dot3Pauseentry, self).__setattr__(name, value)

            class Dot3Pauseadminmode(Enum):
                """
                Dot3Pauseadminmode

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
                Dot3Pauseopermode

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


            def has_data(self):
                return (
                    self.dot3statsindex.is_set or
                    self.dot3hcinpauseframes.is_set or
                    self.dot3hcoutpauseframes.is_set or
                    self.dot3inpauseframes.is_set or
                    self.dot3outpauseframes.is_set or
                    self.dot3pauseadminmode.is_set or
                    self.dot3pauseopermode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot3statsindex.yfilter != YFilter.not_set or
                    self.dot3hcinpauseframes.yfilter != YFilter.not_set or
                    self.dot3hcoutpauseframes.yfilter != YFilter.not_set or
                    self.dot3inpauseframes.yfilter != YFilter.not_set or
                    self.dot3outpauseframes.yfilter != YFilter.not_set or
                    self.dot3pauseadminmode.yfilter != YFilter.not_set or
                    self.dot3pauseopermode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot3PauseEntry" + "[dot3StatsIndex='" + self.dot3statsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EtherLike-MIB:EtherLike-MIB/dot3PauseTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot3statsindex.is_set or self.dot3statsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsindex.get_name_leafdata())
                if (self.dot3hcinpauseframes.is_set or self.dot3hcinpauseframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcinpauseframes.get_name_leafdata())
                if (self.dot3hcoutpauseframes.is_set or self.dot3hcoutpauseframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcoutpauseframes.get_name_leafdata())
                if (self.dot3inpauseframes.is_set or self.dot3inpauseframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3inpauseframes.get_name_leafdata())
                if (self.dot3outpauseframes.is_set or self.dot3outpauseframes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3outpauseframes.get_name_leafdata())
                if (self.dot3pauseadminmode.is_set or self.dot3pauseadminmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3pauseadminmode.get_name_leafdata())
                if (self.dot3pauseopermode.is_set or self.dot3pauseopermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3pauseopermode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot3StatsIndex" or name == "dot3HCInPauseFrames" or name == "dot3HCOutPauseFrames" or name == "dot3InPauseFrames" or name == "dot3OutPauseFrames" or name == "dot3PauseAdminMode" or name == "dot3PauseOperMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot3StatsIndex"):
                    self.dot3statsindex = value
                    self.dot3statsindex.value_namespace = name_space
                    self.dot3statsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCInPauseFrames"):
                    self.dot3hcinpauseframes = value
                    self.dot3hcinpauseframes.value_namespace = name_space
                    self.dot3hcinpauseframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCOutPauseFrames"):
                    self.dot3hcoutpauseframes = value
                    self.dot3hcoutpauseframes.value_namespace = name_space
                    self.dot3hcoutpauseframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3InPauseFrames"):
                    self.dot3inpauseframes = value
                    self.dot3inpauseframes.value_namespace = name_space
                    self.dot3inpauseframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3OutPauseFrames"):
                    self.dot3outpauseframes = value
                    self.dot3outpauseframes.value_namespace = name_space
                    self.dot3outpauseframes.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3PauseAdminMode"):
                    self.dot3pauseadminmode = value
                    self.dot3pauseadminmode.value_namespace = name_space
                    self.dot3pauseadminmode.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3PauseOperMode"):
                    self.dot3pauseopermode = value
                    self.dot3pauseopermode.value_namespace = name_space
                    self.dot3pauseopermode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot3pauseentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot3pauseentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot3PauseTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EtherLike-MIB:EtherLike-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot3PauseEntry"):
                for c in self.dot3pauseentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherlikeMib.Dot3Pausetable.Dot3Pauseentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot3pauseentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot3PauseEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Dot3Hcstatsentry <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry>`
        
        

        """

        _prefix = 'EtherLike-MIB'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherlikeMib.Dot3Hcstatstable, self).__init__()

            self.yang_name = "dot3HCStatsTable"
            self.yang_parent_name = "EtherLike-MIB"

            self.dot3hcstatsentry = YList(self)

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
                        super(EtherlikeMib.Dot3Hcstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherlikeMib.Dot3Hcstatstable, self).__setattr__(name, value)


        class Dot3Hcstatsentry(Entity):
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
                super(EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry, self).__init__()

                self.yang_name = "dot3HCStatsEntry"
                self.yang_parent_name = "dot3HCStatsTable"

                self.dot3statsindex = YLeaf(YType.str, "dot3StatsIndex")

                self.dot3hcstatsalignmenterrors = YLeaf(YType.uint64, "dot3HCStatsAlignmentErrors")

                self.dot3hcstatsfcserrors = YLeaf(YType.uint64, "dot3HCStatsFCSErrors")

                self.dot3hcstatsframetoolongs = YLeaf(YType.uint64, "dot3HCStatsFrameTooLongs")

                self.dot3hcstatsinternalmacreceiveerrors = YLeaf(YType.uint64, "dot3HCStatsInternalMacReceiveErrors")

                self.dot3hcstatsinternalmactransmiterrors = YLeaf(YType.uint64, "dot3HCStatsInternalMacTransmitErrors")

                self.dot3hcstatssymbolerrors = YLeaf(YType.uint64, "dot3HCStatsSymbolErrors")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot3statsindex",
                                "dot3hcstatsalignmenterrors",
                                "dot3hcstatsfcserrors",
                                "dot3hcstatsframetoolongs",
                                "dot3hcstatsinternalmacreceiveerrors",
                                "dot3hcstatsinternalmactransmiterrors",
                                "dot3hcstatssymbolerrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot3statsindex.is_set or
                    self.dot3hcstatsalignmenterrors.is_set or
                    self.dot3hcstatsfcserrors.is_set or
                    self.dot3hcstatsframetoolongs.is_set or
                    self.dot3hcstatsinternalmacreceiveerrors.is_set or
                    self.dot3hcstatsinternalmactransmiterrors.is_set or
                    self.dot3hcstatssymbolerrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot3statsindex.yfilter != YFilter.not_set or
                    self.dot3hcstatsalignmenterrors.yfilter != YFilter.not_set or
                    self.dot3hcstatsfcserrors.yfilter != YFilter.not_set or
                    self.dot3hcstatsframetoolongs.yfilter != YFilter.not_set or
                    self.dot3hcstatsinternalmacreceiveerrors.yfilter != YFilter.not_set or
                    self.dot3hcstatsinternalmactransmiterrors.yfilter != YFilter.not_set or
                    self.dot3hcstatssymbolerrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot3HCStatsEntry" + "[dot3StatsIndex='" + self.dot3statsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EtherLike-MIB:EtherLike-MIB/dot3HCStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot3statsindex.is_set or self.dot3statsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3statsindex.get_name_leafdata())
                if (self.dot3hcstatsalignmenterrors.is_set or self.dot3hcstatsalignmenterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcstatsalignmenterrors.get_name_leafdata())
                if (self.dot3hcstatsfcserrors.is_set or self.dot3hcstatsfcserrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcstatsfcserrors.get_name_leafdata())
                if (self.dot3hcstatsframetoolongs.is_set or self.dot3hcstatsframetoolongs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcstatsframetoolongs.get_name_leafdata())
                if (self.dot3hcstatsinternalmacreceiveerrors.is_set or self.dot3hcstatsinternalmacreceiveerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcstatsinternalmacreceiveerrors.get_name_leafdata())
                if (self.dot3hcstatsinternalmactransmiterrors.is_set or self.dot3hcstatsinternalmactransmiterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcstatsinternalmactransmiterrors.get_name_leafdata())
                if (self.dot3hcstatssymbolerrors.is_set or self.dot3hcstatssymbolerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot3hcstatssymbolerrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot3StatsIndex" or name == "dot3HCStatsAlignmentErrors" or name == "dot3HCStatsFCSErrors" or name == "dot3HCStatsFrameTooLongs" or name == "dot3HCStatsInternalMacReceiveErrors" or name == "dot3HCStatsInternalMacTransmitErrors" or name == "dot3HCStatsSymbolErrors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot3StatsIndex"):
                    self.dot3statsindex = value
                    self.dot3statsindex.value_namespace = name_space
                    self.dot3statsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCStatsAlignmentErrors"):
                    self.dot3hcstatsalignmenterrors = value
                    self.dot3hcstatsalignmenterrors.value_namespace = name_space
                    self.dot3hcstatsalignmenterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCStatsFCSErrors"):
                    self.dot3hcstatsfcserrors = value
                    self.dot3hcstatsfcserrors.value_namespace = name_space
                    self.dot3hcstatsfcserrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCStatsFrameTooLongs"):
                    self.dot3hcstatsframetoolongs = value
                    self.dot3hcstatsframetoolongs.value_namespace = name_space
                    self.dot3hcstatsframetoolongs.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCStatsInternalMacReceiveErrors"):
                    self.dot3hcstatsinternalmacreceiveerrors = value
                    self.dot3hcstatsinternalmacreceiveerrors.value_namespace = name_space
                    self.dot3hcstatsinternalmacreceiveerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCStatsInternalMacTransmitErrors"):
                    self.dot3hcstatsinternalmactransmiterrors = value
                    self.dot3hcstatsinternalmactransmiterrors.value_namespace = name_space
                    self.dot3hcstatsinternalmactransmiterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot3HCStatsSymbolErrors"):
                    self.dot3hcstatssymbolerrors = value
                    self.dot3hcstatssymbolerrors.value_namespace = name_space
                    self.dot3hcstatssymbolerrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot3hcstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot3hcstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot3HCStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EtherLike-MIB:EtherLike-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot3HCStatsEntry"):
                for c in self.dot3hcstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherlikeMib.Dot3Hcstatstable.Dot3Hcstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot3hcstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot3HCStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dot3colltable is not None and self.dot3colltable.has_data()) or
            (self.dot3controltable is not None and self.dot3controltable.has_data()) or
            (self.dot3hcstatstable is not None and self.dot3hcstatstable.has_data()) or
            (self.dot3pausetable is not None and self.dot3pausetable.has_data()) or
            (self.dot3statstable is not None and self.dot3statstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dot3colltable is not None and self.dot3colltable.has_operation()) or
            (self.dot3controltable is not None and self.dot3controltable.has_operation()) or
            (self.dot3hcstatstable is not None and self.dot3hcstatstable.has_operation()) or
            (self.dot3pausetable is not None and self.dot3pausetable.has_operation()) or
            (self.dot3statstable is not None and self.dot3statstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "EtherLike-MIB:EtherLike-MIB" + path_buffer

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

        if (child_yang_name == "dot3CollTable"):
            if (self.dot3colltable is None):
                self.dot3colltable = EtherlikeMib.Dot3Colltable()
                self.dot3colltable.parent = self
                self._children_name_map["dot3colltable"] = "dot3CollTable"
            return self.dot3colltable

        if (child_yang_name == "dot3ControlTable"):
            if (self.dot3controltable is None):
                self.dot3controltable = EtherlikeMib.Dot3Controltable()
                self.dot3controltable.parent = self
                self._children_name_map["dot3controltable"] = "dot3ControlTable"
            return self.dot3controltable

        if (child_yang_name == "dot3HCStatsTable"):
            if (self.dot3hcstatstable is None):
                self.dot3hcstatstable = EtherlikeMib.Dot3Hcstatstable()
                self.dot3hcstatstable.parent = self
                self._children_name_map["dot3hcstatstable"] = "dot3HCStatsTable"
            return self.dot3hcstatstable

        if (child_yang_name == "dot3PauseTable"):
            if (self.dot3pausetable is None):
                self.dot3pausetable = EtherlikeMib.Dot3Pausetable()
                self.dot3pausetable.parent = self
                self._children_name_map["dot3pausetable"] = "dot3PauseTable"
            return self.dot3pausetable

        if (child_yang_name == "dot3StatsTable"):
            if (self.dot3statstable is None):
                self.dot3statstable = EtherlikeMib.Dot3Statstable()
                self.dot3statstable.parent = self
                self._children_name_map["dot3statstable"] = "dot3StatsTable"
            return self.dot3statstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dot3CollTable" or name == "dot3ControlTable" or name == "dot3HCStatsTable" or name == "dot3PauseTable" or name == "dot3StatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EtherlikeMib()
        return self._top_entity

