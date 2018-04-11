""" TOKENRING_MIB 

The MIB module for IEEE Token Ring entities.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Dot5Testinsertfunc(Identity):
    """
    Invoking this test causes the station to test the insert
    ring logic of the hardware if the station's lobe media
    cable is connected to a wiring concentrator.  Note that
    this command inserts the station into the network, and
    thus, could cause problems if the station is connected
    to a operational network.
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(Dot5Testinsertfunc, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:TOKENRING-MIB", "TOKENRING-MIB", "TOKENRING-MIB:dot5TestInsertFunc")


class Dot5Testfullduplexloopback(Identity):
    """
    Invoking this test on a 802.5 interface causes the
    interface to check the path from memory through the
    chip set's internal logic and back to memory, thus
    checking the proper functioning of the system's
    interface to the chip set.
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(Dot5Testfullduplexloopback, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:TOKENRING-MIB", "TOKENRING-MIB", "TOKENRING-MIB:dot5TestFullDuplexLoopBack")


class Dot5Chipsetibm16(Identity):
    """
    IBM's 16/4 Mbs chip set.
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(Dot5Chipsetibm16, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:TOKENRING-MIB", "TOKENRING-MIB", "TOKENRING-MIB:dot5ChipSetIBM16")


class Dot5Chipsettitms380(Identity):
    """
    Texas Instruments' TMS 380 4Mbs chip\-set
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(Dot5Chipsettitms380, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:TOKENRING-MIB", "TOKENRING-MIB", "TOKENRING-MIB:dot5ChipSetTItms380")


class Dot5Chipsettitms380C16(Identity):
    """
    Texas Instruments' TMS 380C16 16/4 Mbs chip\-set
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(Dot5Chipsettitms380C16, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:TOKENRING-MIB", "TOKENRING-MIB", "TOKENRING-MIB:dot5ChipSetTItms380c16")


class TOKENRINGMIB(Entity):
    """
    
    
    .. attribute:: dot5table
    
    	This table contains Token Ring interface parameters and state variables, one entry per 802.5 interface
    	**type**\:  :py:class:`Dot5Table <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table>`
    
    .. attribute:: dot5statstable
    
    	A table containing Token Ring statistics, one entry per 802.5 interface.     All the statistics are defined using the syntax Counter32 as 32\-bit wrap around counters.  Thus, if an interface's hardware maintains these statistics in 16\-bit counters, then the agent must read the hardware's counters frequently enough to prevent loss of significance, in order to maintain 32\-bit counters in software
    	**type**\:  :py:class:`Dot5Statstable <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Statstable>`
    
    .. attribute:: dot5timertable
    
    	This table contains Token Ring interface timer values, one entry per 802.5 interface
    	**type**\:  :py:class:`Dot5Timertable <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Timertable>`
    
    	**status**\: obsolete
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(TOKENRINGMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "TOKENRING-MIB"
        self.yang_parent_name = "TOKENRING-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("dot5Table", ("dot5table", TOKENRINGMIB.Dot5Table)), ("dot5StatsTable", ("dot5statstable", TOKENRINGMIB.Dot5Statstable)), ("dot5TimerTable", ("dot5timertable", TOKENRINGMIB.Dot5Timertable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.dot5table = TOKENRINGMIB.Dot5Table()
        self.dot5table.parent = self
        self._children_name_map["dot5table"] = "dot5Table"
        self._children_yang_names.add("dot5Table")

        self.dot5statstable = TOKENRINGMIB.Dot5Statstable()
        self.dot5statstable.parent = self
        self._children_name_map["dot5statstable"] = "dot5StatsTable"
        self._children_yang_names.add("dot5StatsTable")

        self.dot5timertable = TOKENRINGMIB.Dot5Timertable()
        self.dot5timertable.parent = self
        self._children_name_map["dot5timertable"] = "dot5TimerTable"
        self._children_yang_names.add("dot5TimerTable")
        self._segment_path = lambda: "TOKENRING-MIB:TOKENRING-MIB"


    class Dot5Table(Entity):
        """
        This table contains Token Ring interface
        parameters and state variables, one entry
        per 802.5 interface.
        
        .. attribute:: dot5entry
        
        	A list of Token Ring status and parameter values for an 802.5 interface
        	**type**\: list of  		 :py:class:`Dot5Entry <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry>`
        
        

        """

        _prefix = 'TOKENRING-MIB'
        _revision = '1994-10-23'

        def __init__(self):
            super(TOKENRINGMIB.Dot5Table, self).__init__()

            self.yang_name = "dot5Table"
            self.yang_parent_name = "TOKENRING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot5Entry", ("dot5entry", TOKENRINGMIB.Dot5Table.Dot5Entry))])
            self._leafs = OrderedDict()

            self.dot5entry = YList(self)
            self._segment_path = lambda: "dot5Table"
            self._absolute_path = lambda: "TOKENRING-MIB:TOKENRING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGMIB.Dot5Table, [], name, value)


        class Dot5Entry(Entity):
            """
            A list of Token Ring status and parameter
            values for an 802.5 interface.
            
            .. attribute:: dot5ifindex  (key)
            
            	The value of this object identifies the 802.5 interface for which this entry contains management information.  The value of this object for a particular interface has the same value as the ifIndex object, defined in MIB\-II for the same interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5commands
            
            	When this object is set to the value of open(2), the station should go into the open state.  The progress and success of the open is given by the values of the objects dot5RingState and dot5RingOpenStatus.     When this object is set to the value of reset(3), then the station should do a reset.  On a reset, all MIB counters should retain their values, if possible. Other side affects are dependent on the hardware chip set.     When this object is set to the value of close(4), the station should go into the stopped state by removing itself from the ring.     Setting this object to a value of noop(1) has no effect.     When read, this object always has a value of noop(1).     The open(2) and close(4) values correspond to the up(1) and down(2) values of MIB\-II's ifAdminStatus and ifOperStatus, i.e., the setting of ifAdminStatus and   dot5Commands affects the values of both dot5Commands and ifOperStatus
            	**type**\:  :py:class:`Dot5Commands <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Commands>`
            
            .. attribute:: dot5ringstatus
            
            	The current interface status which can be used to diagnose fluctuating problems that can occur on token rings, after a station has successfully been added to the ring.    Before an open is completed, this object has the value for the 'no status' condition.  The dot5RingState and dot5RingOpenStatus objects provide for debugging problems when the station can not even enter the ring.     The object's value is a sum of values, one for each currently applicable condition.  The following values are defined for various conditions\:          0 = No Problems detected        32 = Ring Recovery        64 = Single Station       256 = Remove Received       512 = reserved      1024 = Auto\-Removal Error      2048 = Lobe Wire Fault      4096 = Transmit Beacon      8192 = Soft Error     16384 = Hard Error     32768 = Signal Loss    131072 = no status, open not completed
            	**type**\: int
            
            	**range:** 0..262143
            
            .. attribute:: dot5ringstate
            
            	The current interface state with respect to entering or leaving the ring
            	**type**\:  :py:class:`Dot5Ringstate <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Ringstate>`
            
            .. attribute:: dot5ringopenstatus
            
            	This object indicates the success, or the reason for failure, of the station's most recent attempt to enter the ring
            	**type**\:  :py:class:`Dot5Ringopenstatus <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Ringopenstatus>`
            
            .. attribute:: dot5ringspeed
            
            	The ring\-speed at the next insertion into the ring.  Note that this may or may not be different to the current ring\-speed which is given by MIB\-II's ifSpeed.  For interfaces which do not support changing ring\-speed, dot5RingSpeed can only be set to its current value.  When dot5RingSpeed has the value unknown(1), the ring's actual ring\-speed is to be used
            	**type**\:  :py:class:`Dot5Ringspeed <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Ringspeed>`
            
            .. attribute:: dot5upstream
            
            	The MAC\-address of the up stream neighbor station in the ring
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot5actmonparticipate
            
            	If this object has a value of true(1) then this interface will participate in the active monitor selection process.  If the value is false(2) then it will not. Setting this object does not take effect until the next Active Monitor election, and might not take effect until the next time the interface is opened
            	**type**\:  :py:class:`Dot5Actmonparticipate <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Actmonparticipate>`
            
            .. attribute:: dot5functional
            
            	The bit mask of all Token Ring functional addresses for which this interface will accept frames
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot5lastbeaconsent
            
            	The value of MIB\-II's sysUpTime object at which the local system last transmitted a Beacon frame on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKENRING-MIB'
            _revision = '1994-10-23'

            def __init__(self):
                super(TOKENRINGMIB.Dot5Table.Dot5Entry, self).__init__()

                self.yang_name = "dot5Entry"
                self.yang_parent_name = "dot5Table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot5ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot5ifindex', YLeaf(YType.int32, 'dot5IfIndex')),
                    ('dot5commands', YLeaf(YType.enumeration, 'dot5Commands')),
                    ('dot5ringstatus', YLeaf(YType.int32, 'dot5RingStatus')),
                    ('dot5ringstate', YLeaf(YType.enumeration, 'dot5RingState')),
                    ('dot5ringopenstatus', YLeaf(YType.enumeration, 'dot5RingOpenStatus')),
                    ('dot5ringspeed', YLeaf(YType.enumeration, 'dot5RingSpeed')),
                    ('dot5upstream', YLeaf(YType.str, 'dot5UpStream')),
                    ('dot5actmonparticipate', YLeaf(YType.enumeration, 'dot5ActMonParticipate')),
                    ('dot5functional', YLeaf(YType.str, 'dot5Functional')),
                    ('dot5lastbeaconsent', YLeaf(YType.uint32, 'dot5LastBeaconSent')),
                ])
                self.dot5ifindex = None
                self.dot5commands = None
                self.dot5ringstatus = None
                self.dot5ringstate = None
                self.dot5ringopenstatus = None
                self.dot5ringspeed = None
                self.dot5upstream = None
                self.dot5actmonparticipate = None
                self.dot5functional = None
                self.dot5lastbeaconsent = None
                self._segment_path = lambda: "dot5Entry" + "[dot5IfIndex='" + str(self.dot5ifindex) + "']"
                self._absolute_path = lambda: "TOKENRING-MIB:TOKENRING-MIB/dot5Table/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGMIB.Dot5Table.Dot5Entry, ['dot5ifindex', 'dot5commands', 'dot5ringstatus', 'dot5ringstate', 'dot5ringopenstatus', 'dot5ringspeed', 'dot5upstream', 'dot5actmonparticipate', 'dot5functional', 'dot5lastbeaconsent'], name, value)

            class Dot5Actmonparticipate(Enum):
                """
                Dot5Actmonparticipate (Enum Class)

                If this object has a value of true(1) then

                this interface will participate in the

                active monitor selection process.  If the

                value is false(2) then it will not.

                Setting this object does not take effect

                until the next Active Monitor election, and

                might not take effect until the next time

                the interface is opened.

                .. data:: true = 1

                .. data:: false = 2

                """

                true = Enum.YLeaf(1, "true")

                false = Enum.YLeaf(2, "false")


            class Dot5Commands(Enum):
                """
                Dot5Commands (Enum Class)

                When this object is set to the value of

                open(2), the station should go into the

                open state.  The progress and success of

                the open is given by the values of the

                objects dot5RingState and

                dot5RingOpenStatus.

                    When this object is set to the value

                of reset(3), then the station should do

                a reset.  On a reset, all MIB counters

                should retain their values, if possible.

                Other side affects are dependent on the

                hardware chip set.

                    When this object is set to the value

                of close(4), the station should go into

                the stopped state by removing itself

                from the ring.

                    Setting this object to a value of

                noop(1) has no effect.

                    When read, this object always has a

                value of noop(1).

                    The open(2) and close(4) values

                correspond to the up(1) and down(2) values

                of MIB\-II's ifAdminStatus and ifOperStatus,

                i.e., the setting of ifAdminStatus and

                dot5Commands affects the values of both

                dot5Commands and ifOperStatus.

                .. data:: noop = 1

                .. data:: open = 2

                .. data:: reset = 3

                .. data:: close = 4

                """

                noop = Enum.YLeaf(1, "noop")

                open = Enum.YLeaf(2, "open")

                reset = Enum.YLeaf(3, "reset")

                close = Enum.YLeaf(4, "close")


            class Dot5Ringopenstatus(Enum):
                """
                Dot5Ringopenstatus (Enum Class)

                This object indicates the success, or the

                reason for failure, of the station's most

                recent attempt to enter the ring.

                .. data:: noOpen = 1

                .. data:: badParam = 2

                .. data:: lobeFailed = 3

                .. data:: signalLoss = 4

                .. data:: insertionTimeout = 5

                .. data:: ringFailed = 6

                .. data:: beaconing = 7

                .. data:: duplicateMAC = 8

                .. data:: requestFailed = 9

                .. data:: removeReceived = 10

                .. data:: open = 11

                """

                noOpen = Enum.YLeaf(1, "noOpen")

                badParam = Enum.YLeaf(2, "badParam")

                lobeFailed = Enum.YLeaf(3, "lobeFailed")

                signalLoss = Enum.YLeaf(4, "signalLoss")

                insertionTimeout = Enum.YLeaf(5, "insertionTimeout")

                ringFailed = Enum.YLeaf(6, "ringFailed")

                beaconing = Enum.YLeaf(7, "beaconing")

                duplicateMAC = Enum.YLeaf(8, "duplicateMAC")

                requestFailed = Enum.YLeaf(9, "requestFailed")

                removeReceived = Enum.YLeaf(10, "removeReceived")

                open = Enum.YLeaf(11, "open")


            class Dot5Ringspeed(Enum):
                """
                Dot5Ringspeed (Enum Class)

                The ring\-speed at the next insertion into

                the ring.  Note that this may or may not be

                different to the current ring\-speed which is

                given by MIB\-II's ifSpeed.  For interfaces

                which do not support changing ring\-speed,

                dot5RingSpeed can only be set to its current

                value.  When dot5RingSpeed has the value

                unknown(1), the ring's actual ring\-speed is

                to be used.

                .. data:: unknown = 1

                .. data:: oneMegabit = 2

                .. data:: fourMegabit = 3

                .. data:: sixteenMegabit = 4

                """

                unknown = Enum.YLeaf(1, "unknown")

                oneMegabit = Enum.YLeaf(2, "oneMegabit")

                fourMegabit = Enum.YLeaf(3, "fourMegabit")

                sixteenMegabit = Enum.YLeaf(4, "sixteenMegabit")


            class Dot5Ringstate(Enum):
                """
                Dot5Ringstate (Enum Class)

                The current interface state with respect

                to entering or leaving the ring.

                .. data:: opened = 1

                .. data:: closed = 2

                .. data:: opening = 3

                .. data:: closing = 4

                .. data:: openFailure = 5

                .. data:: ringFailure = 6

                """

                opened = Enum.YLeaf(1, "opened")

                closed = Enum.YLeaf(2, "closed")

                opening = Enum.YLeaf(3, "opening")

                closing = Enum.YLeaf(4, "closing")

                openFailure = Enum.YLeaf(5, "openFailure")

                ringFailure = Enum.YLeaf(6, "ringFailure")



    class Dot5Statstable(Entity):
        """
        A table containing Token Ring statistics,
        one entry per 802.5 interface.
            All the statistics are defined using
        the syntax Counter32 as 32\-bit wrap around
        counters.  Thus, if an interface's
        hardware maintains these statistics in
        16\-bit counters, then the agent must read
        the hardware's counters frequently enough
        to prevent loss of significance, in order
        to maintain 32\-bit counters in software.
        
        .. attribute:: dot5statsentry
        
        	An entry contains the 802.5 statistics for a particular interface
        	**type**\: list of  		 :py:class:`Dot5Statsentry <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Statstable.Dot5Statsentry>`
        
        

        """

        _prefix = 'TOKENRING-MIB'
        _revision = '1994-10-23'

        def __init__(self):
            super(TOKENRINGMIB.Dot5Statstable, self).__init__()

            self.yang_name = "dot5StatsTable"
            self.yang_parent_name = "TOKENRING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot5StatsEntry", ("dot5statsentry", TOKENRINGMIB.Dot5Statstable.Dot5Statsentry))])
            self._leafs = OrderedDict()

            self.dot5statsentry = YList(self)
            self._segment_path = lambda: "dot5StatsTable"
            self._absolute_path = lambda: "TOKENRING-MIB:TOKENRING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGMIB.Dot5Statstable, [], name, value)


        class Dot5Statsentry(Entity):
            """
            An entry contains the 802.5 statistics
            for a particular interface.
            
            .. attribute:: dot5statsifindex  (key)
            
            	The value of this object identifies the 802.5 interface for which this entry contains management information.  The value of this object for a particular interface has the same value as MIB\-II's ifIndex object for the same interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5statslineerrors
            
            	This counter is incremented when a frame or token is copied or repeated by a station, the E bit is zero in the frame or token and one of the following conditions exists\: 1) there is a non\-data bit (J or K bit) between the SD and the ED of the frame or token, or 2) there is an FCS error in the frame
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsbursterrors
            
            	This counter is incremented when a station detects the absence of transitions for five half\-bit timers (burst\-five error)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsacerrors
            
            	This counter is incremented when a station receives an AMP or SMP frame in which A is equal to C is equal to 0, and then receives another SMP frame with A is equal to C is equal to 0 without first receiving an AMP frame. It denotes a station that cannot set the AC bits properly
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsaborttranserrors
            
            	This counter is incremented when a station transmits an abort delimiter while transmitting
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsinternalerrors
            
            	This counter is incremented when a station recognizes an internal error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslostframeerrors
            
            	This counter is incremented when a station is transmitting and its TRR timer expires. This condition denotes a condition where a transmitting station in strip mode does not receive the trailer of the frame before the TRR timer goes off
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsreceivecongestions
            
            	This counter is incremented when a station recognizes a frame addressed to its specific address, but has no available buffer space indicating that the station is congested
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsframecopiederrors
            
            	This counter is incremented when a station recognizes a frame addressed to its specific address and detects that the FS field A bits are set to 1 indicating a possible line hit or duplicate address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statstokenerrors
            
            	This counter is incremented when a station acting as the active monitor recognizes an error condition that needs a token transmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssofterrors
            
            	The number of Soft Errors the interface has detected. It directly corresponds to the number of Report Error MAC frames that this interface has transmitted. Soft Errors are those which are recoverable by the MAC layer protocols
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsharderrors
            
            	The number of times this interface has detected an immediately recoverable fatal error.  It denotes the number of times this interface is either transmitting or receiving beacon MAC frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssignalloss
            
            	The number of times this interface has detected the loss of signal condition from the ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statstransmitbeacons
            
            	The number of times this interface has transmitted a beacon frame
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsrecoverys
            
            	The number of Claim Token MAC frames received or transmitted after the interface has received a Ring Purge MAC frame.  This counter signifies the number of times the ring has been purged and is being recovered back into a normal operating state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslobewires
            
            	The number of times the interface has detected an open or short circuit in the lobe data path.  The adapter will be closed and dot5RingState will signify this condition
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsremoves
            
            	The number of times the interface has received a Remove Ring Station MAC frame request.  When this frame is received the interface will enter the close state and dot5RingState will signify this condition
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssingles
            
            	The number of times the interface has sensed that it is the only station on the ring.  This will happen if the interface is the first one up on a ring, or if there is a hardware problem
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsfreqerrors
            
            	The number of times the interface has detected that the frequency of the incoming signal differs from the expected frequency by more than that specified by the IEEE 802.5 standard
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKENRING-MIB'
            _revision = '1994-10-23'

            def __init__(self):
                super(TOKENRINGMIB.Dot5Statstable.Dot5Statsentry, self).__init__()

                self.yang_name = "dot5StatsEntry"
                self.yang_parent_name = "dot5StatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot5statsifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot5statsifindex', YLeaf(YType.int32, 'dot5StatsIfIndex')),
                    ('dot5statslineerrors', YLeaf(YType.uint32, 'dot5StatsLineErrors')),
                    ('dot5statsbursterrors', YLeaf(YType.uint32, 'dot5StatsBurstErrors')),
                    ('dot5statsacerrors', YLeaf(YType.uint32, 'dot5StatsACErrors')),
                    ('dot5statsaborttranserrors', YLeaf(YType.uint32, 'dot5StatsAbortTransErrors')),
                    ('dot5statsinternalerrors', YLeaf(YType.uint32, 'dot5StatsInternalErrors')),
                    ('dot5statslostframeerrors', YLeaf(YType.uint32, 'dot5StatsLostFrameErrors')),
                    ('dot5statsreceivecongestions', YLeaf(YType.uint32, 'dot5StatsReceiveCongestions')),
                    ('dot5statsframecopiederrors', YLeaf(YType.uint32, 'dot5StatsFrameCopiedErrors')),
                    ('dot5statstokenerrors', YLeaf(YType.uint32, 'dot5StatsTokenErrors')),
                    ('dot5statssofterrors', YLeaf(YType.uint32, 'dot5StatsSoftErrors')),
                    ('dot5statsharderrors', YLeaf(YType.uint32, 'dot5StatsHardErrors')),
                    ('dot5statssignalloss', YLeaf(YType.uint32, 'dot5StatsSignalLoss')),
                    ('dot5statstransmitbeacons', YLeaf(YType.uint32, 'dot5StatsTransmitBeacons')),
                    ('dot5statsrecoverys', YLeaf(YType.uint32, 'dot5StatsRecoverys')),
                    ('dot5statslobewires', YLeaf(YType.uint32, 'dot5StatsLobeWires')),
                    ('dot5statsremoves', YLeaf(YType.uint32, 'dot5StatsRemoves')),
                    ('dot5statssingles', YLeaf(YType.uint32, 'dot5StatsSingles')),
                    ('dot5statsfreqerrors', YLeaf(YType.uint32, 'dot5StatsFreqErrors')),
                ])
                self.dot5statsifindex = None
                self.dot5statslineerrors = None
                self.dot5statsbursterrors = None
                self.dot5statsacerrors = None
                self.dot5statsaborttranserrors = None
                self.dot5statsinternalerrors = None
                self.dot5statslostframeerrors = None
                self.dot5statsreceivecongestions = None
                self.dot5statsframecopiederrors = None
                self.dot5statstokenerrors = None
                self.dot5statssofterrors = None
                self.dot5statsharderrors = None
                self.dot5statssignalloss = None
                self.dot5statstransmitbeacons = None
                self.dot5statsrecoverys = None
                self.dot5statslobewires = None
                self.dot5statsremoves = None
                self.dot5statssingles = None
                self.dot5statsfreqerrors = None
                self._segment_path = lambda: "dot5StatsEntry" + "[dot5StatsIfIndex='" + str(self.dot5statsifindex) + "']"
                self._absolute_path = lambda: "TOKENRING-MIB:TOKENRING-MIB/dot5StatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGMIB.Dot5Statstable.Dot5Statsentry, ['dot5statsifindex', 'dot5statslineerrors', 'dot5statsbursterrors', 'dot5statsacerrors', 'dot5statsaborttranserrors', 'dot5statsinternalerrors', 'dot5statslostframeerrors', 'dot5statsreceivecongestions', 'dot5statsframecopiederrors', 'dot5statstokenerrors', 'dot5statssofterrors', 'dot5statsharderrors', 'dot5statssignalloss', 'dot5statstransmitbeacons', 'dot5statsrecoverys', 'dot5statslobewires', 'dot5statsremoves', 'dot5statssingles', 'dot5statsfreqerrors'], name, value)


    class Dot5Timertable(Entity):
        """
        This table contains Token Ring interface
        timer values, one entry per 802.5
        interface.
        
        .. attribute:: dot5timerentry
        
        	A list of Token Ring timer values for an 802.5 interface
        	**type**\: list of  		 :py:class:`Dot5Timerentry <ydk.models.cisco_ios_xe.TOKENRING_MIB.TOKENRINGMIB.Dot5Timertable.Dot5Timerentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'TOKENRING-MIB'
        _revision = '1994-10-23'

        def __init__(self):
            super(TOKENRINGMIB.Dot5Timertable, self).__init__()

            self.yang_name = "dot5TimerTable"
            self.yang_parent_name = "TOKENRING-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("dot5TimerEntry", ("dot5timerentry", TOKENRINGMIB.Dot5Timertable.Dot5Timerentry))])
            self._leafs = OrderedDict()

            self.dot5timerentry = YList(self)
            self._segment_path = lambda: "dot5TimerTable"
            self._absolute_path = lambda: "TOKENRING-MIB:TOKENRING-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TOKENRINGMIB.Dot5Timertable, [], name, value)


        class Dot5Timerentry(Entity):
            """
            A list of Token Ring timer values for an
            802.5 interface.
            
            .. attribute:: dot5timerifindex  (key)
            
            	The value of this object identifies the 802.5 interface for which this entry contains timer values.  The value of   this object for a particular interface has the same value as MIB\-II's ifIndex object for the same interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerreturnrepeat
            
            	The time\-out value used to ensure the interface will return to Repeat State, in units of 100 micro\-seconds.  The value should be greater than the maximum ring latency
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerholding
            
            	Maximum period of time a station is permitted to transmit frames after capturing a token, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerqueuepdu
            
            	The time\-out value for enqueuing of an SMP PDU after reception of an AMP or SMP frame in which the A and C bits were equal to 0, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timervalidtransmit
            
            	The time\-out value used by the active monitor to detect the absence of valid transmissions, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timernotoken
            
            	The time\-out value used to recover from various\-related error situations. If N is the maximum number of stations on the ring, the value of this timer is normally\: dot5TimerReturnRepeat + N\*dot5TimerHolding
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timeractivemon
            
            	The time\-out value used by the active monitor to stimulate the enqueuing of an AMP PDU for transmission, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerstandbymon
            
            	The time\-out value used by the stand\-by monitors to ensure that there is an active monitor on the ring and to detect a continuous stream of tokens, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timererrorreport
            
            	The time\-out value which determines how often a station shall send a Report Error MAC frame to report its error counters, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerbeacontransmit
            
            	The time\-out value which determines how long a station shall remain in the state of transmitting Beacon frames before entering the Bypass state, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerbeaconreceive
            
            	The time\-out value which determines how long a station shall receive Beacon frames from its downstream neighbor before entering the Bypass state, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'TOKENRING-MIB'
            _revision = '1994-10-23'

            def __init__(self):
                super(TOKENRINGMIB.Dot5Timertable.Dot5Timerentry, self).__init__()

                self.yang_name = "dot5TimerEntry"
                self.yang_parent_name = "dot5TimerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot5timerifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot5timerifindex', YLeaf(YType.int32, 'dot5TimerIfIndex')),
                    ('dot5timerreturnrepeat', YLeaf(YType.int32, 'dot5TimerReturnRepeat')),
                    ('dot5timerholding', YLeaf(YType.int32, 'dot5TimerHolding')),
                    ('dot5timerqueuepdu', YLeaf(YType.int32, 'dot5TimerQueuePDU')),
                    ('dot5timervalidtransmit', YLeaf(YType.int32, 'dot5TimerValidTransmit')),
                    ('dot5timernotoken', YLeaf(YType.int32, 'dot5TimerNoToken')),
                    ('dot5timeractivemon', YLeaf(YType.int32, 'dot5TimerActiveMon')),
                    ('dot5timerstandbymon', YLeaf(YType.int32, 'dot5TimerStandbyMon')),
                    ('dot5timererrorreport', YLeaf(YType.int32, 'dot5TimerErrorReport')),
                    ('dot5timerbeacontransmit', YLeaf(YType.int32, 'dot5TimerBeaconTransmit')),
                    ('dot5timerbeaconreceive', YLeaf(YType.int32, 'dot5TimerBeaconReceive')),
                ])
                self.dot5timerifindex = None
                self.dot5timerreturnrepeat = None
                self.dot5timerholding = None
                self.dot5timerqueuepdu = None
                self.dot5timervalidtransmit = None
                self.dot5timernotoken = None
                self.dot5timeractivemon = None
                self.dot5timerstandbymon = None
                self.dot5timererrorreport = None
                self.dot5timerbeacontransmit = None
                self.dot5timerbeaconreceive = None
                self._segment_path = lambda: "dot5TimerEntry" + "[dot5TimerIfIndex='" + str(self.dot5timerifindex) + "']"
                self._absolute_path = lambda: "TOKENRING-MIB:TOKENRING-MIB/dot5TimerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TOKENRINGMIB.Dot5Timertable.Dot5Timerentry, ['dot5timerifindex', 'dot5timerreturnrepeat', 'dot5timerholding', 'dot5timerqueuepdu', 'dot5timervalidtransmit', 'dot5timernotoken', 'dot5timeractivemon', 'dot5timerstandbymon', 'dot5timererrorreport', 'dot5timerbeacontransmit', 'dot5timerbeaconreceive'], name, value)

    def clone_ptr(self):
        self._top_entity = TOKENRINGMIB()
        return self._top_entity

