""" TOKENRING_MIB 

The MIB module for IEEE Token Ring entities.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



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


class Dot5Chipsetibm16(Identity):
    """
    IBM's 16/4 Mbs chip set.
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(Dot5Chipsetibm16, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:TOKENRING-MIB", "TOKENRING-MIB", "TOKENRING-MIB:dot5ChipSetIBM16")


class TokenringMib(Entity):
    """
    
    
    .. attribute:: dot5statstable
    
    	A table containing Token Ring statistics, one entry per 802.5 interface.     All the statistics are defined using the syntax Counter32 as 32\-bit wrap around counters.  Thus, if an interface's hardware maintains these statistics in 16\-bit counters, then the agent must read the hardware's counters frequently enough to prevent loss of significance, in order to maintain 32\-bit counters in software
    	**type**\:   :py:class:`Dot5Statstable <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Statstable>`
    
    .. attribute:: dot5table
    
    	This table contains Token Ring interface parameters and state variables, one entry per 802.5 interface
    	**type**\:   :py:class:`Dot5Table <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table>`
    
    .. attribute:: dot5timertable
    
    	This table contains Token Ring interface timer values, one entry per 802.5 interface
    	**type**\:   :py:class:`Dot5Timertable <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Timertable>`
    
    	**status**\: obsolete
    
    

    """

    _prefix = 'TOKENRING-MIB'
    _revision = '1994-10-23'

    def __init__(self):
        super(TokenringMib, self).__init__()
        self._top_entity = None

        self.yang_name = "TOKENRING-MIB"
        self.yang_parent_name = "TOKENRING-MIB"

        self.dot5statstable = TokenringMib.Dot5Statstable()
        self.dot5statstable.parent = self
        self._children_name_map["dot5statstable"] = "dot5StatsTable"
        self._children_yang_names.add("dot5StatsTable")

        self.dot5table = TokenringMib.Dot5Table()
        self.dot5table.parent = self
        self._children_name_map["dot5table"] = "dot5Table"
        self._children_yang_names.add("dot5Table")

        self.dot5timertable = TokenringMib.Dot5Timertable()
        self.dot5timertable.parent = self
        self._children_name_map["dot5timertable"] = "dot5TimerTable"
        self._children_yang_names.add("dot5TimerTable")


    class Dot5Table(Entity):
        """
        This table contains Token Ring interface
        parameters and state variables, one entry
        per 802.5 interface.
        
        .. attribute:: dot5entry
        
        	A list of Token Ring status and parameter values for an 802.5 interface
        	**type**\: list of    :py:class:`Dot5Entry <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table.Dot5Entry>`
        
        

        """

        _prefix = 'TOKENRING-MIB'
        _revision = '1994-10-23'

        def __init__(self):
            super(TokenringMib.Dot5Table, self).__init__()

            self.yang_name = "dot5Table"
            self.yang_parent_name = "TOKENRING-MIB"

            self.dot5entry = YList(self)

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
                        super(TokenringMib.Dot5Table, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenringMib.Dot5Table, self).__setattr__(name, value)


        class Dot5Entry(Entity):
            """
            A list of Token Ring status and parameter
            values for an 802.5 interface.
            
            .. attribute:: dot5ifindex  <key>
            
            	The value of this object identifies the 802.5 interface for which this entry contains management information.  The value of this object for a particular interface has the same value as the ifIndex object, defined in MIB\-II for the same interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5actmonparticipate
            
            	If this object has a value of true(1) then this interface will participate in the active monitor selection process.  If the value is false(2) then it will not. Setting this object does not take effect until the next Active Monitor election, and might not take effect until the next time the interface is opened
            	**type**\:   :py:class:`Dot5Actmonparticipate <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table.Dot5Entry.Dot5Actmonparticipate>`
            
            .. attribute:: dot5commands
            
            	When this object is set to the value of open(2), the station should go into the open state.  The progress and success of the open is given by the values of the objects dot5RingState and dot5RingOpenStatus.     When this object is set to the value of reset(3), then the station should do a reset.  On a reset, all MIB counters should retain their values, if possible. Other side affects are dependent on the hardware chip set.     When this object is set to the value of close(4), the station should go into the stopped state by removing itself from the ring.     Setting this object to a value of noop(1) has no effect.     When read, this object always has a value of noop(1).     The open(2) and close(4) values correspond to the up(1) and down(2) values of MIB\-II's ifAdminStatus and ifOperStatus, i.e., the setting of ifAdminStatus and   dot5Commands affects the values of both dot5Commands and ifOperStatus
            	**type**\:   :py:class:`Dot5Commands <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table.Dot5Entry.Dot5Commands>`
            
            .. attribute:: dot5functional
            
            	The bit mask of all Token Ring functional addresses for which this interface will accept frames
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot5lastbeaconsent
            
            	The value of MIB\-II's sysUpTime object at which the local system last transmitted a Beacon frame on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5ringopenstatus
            
            	This object indicates the success, or the reason for failure, of the station's most recent attempt to enter the ring
            	**type**\:   :py:class:`Dot5Ringopenstatus <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table.Dot5Entry.Dot5Ringopenstatus>`
            
            .. attribute:: dot5ringspeed
            
            	The ring\-speed at the next insertion into the ring.  Note that this may or may not be different to the current ring\-speed which is given by MIB\-II's ifSpeed.  For interfaces which do not support changing ring\-speed, dot5RingSpeed can only be set to its current value.  When dot5RingSpeed has the value unknown(1), the ring's actual ring\-speed is to be used
            	**type**\:   :py:class:`Dot5Ringspeed <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table.Dot5Entry.Dot5Ringspeed>`
            
            .. attribute:: dot5ringstate
            
            	The current interface state with respect to entering or leaving the ring
            	**type**\:   :py:class:`Dot5Ringstate <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Table.Dot5Entry.Dot5Ringstate>`
            
            .. attribute:: dot5ringstatus
            
            	The current interface status which can be used to diagnose fluctuating problems that can occur on token rings, after a station has successfully been added to the ring.    Before an open is completed, this object has the value for the 'no status' condition.  The dot5RingState and dot5RingOpenStatus objects provide for debugging problems when the station can not even enter the ring.     The object's value is a sum of values, one for each currently applicable condition.  The following values are defined for various conditions\:          0 = No Problems detected        32 = Ring Recovery        64 = Single Station       256 = Remove Received       512 = reserved      1024 = Auto\-Removal Error      2048 = Lobe Wire Fault      4096 = Transmit Beacon      8192 = Soft Error     16384 = Hard Error     32768 = Signal Loss    131072 = no status, open not completed
            	**type**\:  int
            
            	**range:** 0..262143
            
            .. attribute:: dot5upstream
            
            	The MAC\-address of the up stream neighbor station in the ring
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'TOKENRING-MIB'
            _revision = '1994-10-23'

            def __init__(self):
                super(TokenringMib.Dot5Table.Dot5Entry, self).__init__()

                self.yang_name = "dot5Entry"
                self.yang_parent_name = "dot5Table"

                self.dot5ifindex = YLeaf(YType.int32, "dot5IfIndex")

                self.dot5actmonparticipate = YLeaf(YType.enumeration, "dot5ActMonParticipate")

                self.dot5commands = YLeaf(YType.enumeration, "dot5Commands")

                self.dot5functional = YLeaf(YType.str, "dot5Functional")

                self.dot5lastbeaconsent = YLeaf(YType.uint32, "dot5LastBeaconSent")

                self.dot5ringopenstatus = YLeaf(YType.enumeration, "dot5RingOpenStatus")

                self.dot5ringspeed = YLeaf(YType.enumeration, "dot5RingSpeed")

                self.dot5ringstate = YLeaf(YType.enumeration, "dot5RingState")

                self.dot5ringstatus = YLeaf(YType.int32, "dot5RingStatus")

                self.dot5upstream = YLeaf(YType.str, "dot5UpStream")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot5ifindex",
                                "dot5actmonparticipate",
                                "dot5commands",
                                "dot5functional",
                                "dot5lastbeaconsent",
                                "dot5ringopenstatus",
                                "dot5ringspeed",
                                "dot5ringstate",
                                "dot5ringstatus",
                                "dot5upstream") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenringMib.Dot5Table.Dot5Entry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenringMib.Dot5Table.Dot5Entry, self).__setattr__(name, value)

            class Dot5Actmonparticipate(Enum):
                """
                Dot5Actmonparticipate

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
                Dot5Commands

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
                Dot5Ringopenstatus

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
                Dot5Ringspeed

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
                Dot5Ringstate

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


            def has_data(self):
                return (
                    self.dot5ifindex.is_set or
                    self.dot5actmonparticipate.is_set or
                    self.dot5commands.is_set or
                    self.dot5functional.is_set or
                    self.dot5lastbeaconsent.is_set or
                    self.dot5ringopenstatus.is_set or
                    self.dot5ringspeed.is_set or
                    self.dot5ringstate.is_set or
                    self.dot5ringstatus.is_set or
                    self.dot5upstream.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot5ifindex.yfilter != YFilter.not_set or
                    self.dot5actmonparticipate.yfilter != YFilter.not_set or
                    self.dot5commands.yfilter != YFilter.not_set or
                    self.dot5functional.yfilter != YFilter.not_set or
                    self.dot5lastbeaconsent.yfilter != YFilter.not_set or
                    self.dot5ringopenstatus.yfilter != YFilter.not_set or
                    self.dot5ringspeed.yfilter != YFilter.not_set or
                    self.dot5ringstate.yfilter != YFilter.not_set or
                    self.dot5ringstatus.yfilter != YFilter.not_set or
                    self.dot5upstream.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot5Entry" + "[dot5IfIndex='" + self.dot5ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKENRING-MIB:TOKENRING-MIB/dot5Table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot5ifindex.is_set or self.dot5ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5ifindex.get_name_leafdata())
                if (self.dot5actmonparticipate.is_set or self.dot5actmonparticipate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5actmonparticipate.get_name_leafdata())
                if (self.dot5commands.is_set or self.dot5commands.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5commands.get_name_leafdata())
                if (self.dot5functional.is_set or self.dot5functional.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5functional.get_name_leafdata())
                if (self.dot5lastbeaconsent.is_set or self.dot5lastbeaconsent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5lastbeaconsent.get_name_leafdata())
                if (self.dot5ringopenstatus.is_set or self.dot5ringopenstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5ringopenstatus.get_name_leafdata())
                if (self.dot5ringspeed.is_set or self.dot5ringspeed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5ringspeed.get_name_leafdata())
                if (self.dot5ringstate.is_set or self.dot5ringstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5ringstate.get_name_leafdata())
                if (self.dot5ringstatus.is_set or self.dot5ringstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5ringstatus.get_name_leafdata())
                if (self.dot5upstream.is_set or self.dot5upstream.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5upstream.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot5IfIndex" or name == "dot5ActMonParticipate" or name == "dot5Commands" or name == "dot5Functional" or name == "dot5LastBeaconSent" or name == "dot5RingOpenStatus" or name == "dot5RingSpeed" or name == "dot5RingState" or name == "dot5RingStatus" or name == "dot5UpStream"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot5IfIndex"):
                    self.dot5ifindex = value
                    self.dot5ifindex.value_namespace = name_space
                    self.dot5ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5ActMonParticipate"):
                    self.dot5actmonparticipate = value
                    self.dot5actmonparticipate.value_namespace = name_space
                    self.dot5actmonparticipate.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5Commands"):
                    self.dot5commands = value
                    self.dot5commands.value_namespace = name_space
                    self.dot5commands.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5Functional"):
                    self.dot5functional = value
                    self.dot5functional.value_namespace = name_space
                    self.dot5functional.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5LastBeaconSent"):
                    self.dot5lastbeaconsent = value
                    self.dot5lastbeaconsent.value_namespace = name_space
                    self.dot5lastbeaconsent.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5RingOpenStatus"):
                    self.dot5ringopenstatus = value
                    self.dot5ringopenstatus.value_namespace = name_space
                    self.dot5ringopenstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5RingSpeed"):
                    self.dot5ringspeed = value
                    self.dot5ringspeed.value_namespace = name_space
                    self.dot5ringspeed.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5RingState"):
                    self.dot5ringstate = value
                    self.dot5ringstate.value_namespace = name_space
                    self.dot5ringstate.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5RingStatus"):
                    self.dot5ringstatus = value
                    self.dot5ringstatus.value_namespace = name_space
                    self.dot5ringstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5UpStream"):
                    self.dot5upstream = value
                    self.dot5upstream.value_namespace = name_space
                    self.dot5upstream.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot5entry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot5entry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot5Table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKENRING-MIB:TOKENRING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot5Entry"):
                for c in self.dot5entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenringMib.Dot5Table.Dot5Entry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot5entry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot5Entry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Dot5Statsentry <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Statstable.Dot5Statsentry>`
        
        

        """

        _prefix = 'TOKENRING-MIB'
        _revision = '1994-10-23'

        def __init__(self):
            super(TokenringMib.Dot5Statstable, self).__init__()

            self.yang_name = "dot5StatsTable"
            self.yang_parent_name = "TOKENRING-MIB"

            self.dot5statsentry = YList(self)

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
                        super(TokenringMib.Dot5Statstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenringMib.Dot5Statstable, self).__setattr__(name, value)


        class Dot5Statsentry(Entity):
            """
            An entry contains the 802.5 statistics
            for a particular interface.
            
            .. attribute:: dot5statsifindex  <key>
            
            	The value of this object identifies the 802.5 interface for which this entry contains management information.  The value of this object for a particular interface has the same value as MIB\-II's ifIndex object for the same interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5statsaborttranserrors
            
            	This counter is incremented when a station transmits an abort delimiter while transmitting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsacerrors
            
            	This counter is incremented when a station receives an AMP or SMP frame in which A is equal to C is equal to 0, and then receives another SMP frame with A is equal to C is equal to 0 without first receiving an AMP frame. It denotes a station that cannot set the AC bits properly
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsbursterrors
            
            	This counter is incremented when a station detects the absence of transitions for five half\-bit timers (burst\-five error)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsframecopiederrors
            
            	This counter is incremented when a station recognizes a frame addressed to its specific address and detects that the FS field A bits are set to 1 indicating a possible line hit or duplicate address
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsfreqerrors
            
            	The number of times the interface has detected that the frequency of the incoming signal differs from the expected frequency by more than that specified by the IEEE 802.5 standard
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsharderrors
            
            	The number of times this interface has detected an immediately recoverable fatal error.  It denotes the number of times this interface is either transmitting or receiving beacon MAC frames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsinternalerrors
            
            	This counter is incremented when a station recognizes an internal error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslineerrors
            
            	This counter is incremented when a frame or token is copied or repeated by a station, the E bit is zero in the frame or token and one of the following conditions exists\: 1) there is a non\-data bit (J or K bit) between the SD and the ED of the frame or token, or 2) there is an FCS error in the frame
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslobewires
            
            	The number of times the interface has detected an open or short circuit in the lobe data path.  The adapter will be closed and dot5RingState will signify this condition
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslostframeerrors
            
            	This counter is incremented when a station is transmitting and its TRR timer expires. This condition denotes a condition where a transmitting station in strip mode does not receive the trailer of the frame before the TRR timer goes off
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsreceivecongestions
            
            	This counter is incremented when a station recognizes a frame addressed to its specific address, but has no available buffer space indicating that the station is congested
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsrecoverys
            
            	The number of Claim Token MAC frames received or transmitted after the interface has received a Ring Purge MAC frame.  This counter signifies the number of times the ring has been purged and is being recovered back into a normal operating state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsremoves
            
            	The number of times the interface has received a Remove Ring Station MAC frame request.  When this frame is received the interface will enter the close state and dot5RingState will signify this condition
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssignalloss
            
            	The number of times this interface has detected the loss of signal condition from the ring
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssingles
            
            	The number of times the interface has sensed that it is the only station on the ring.  This will happen if the interface is the first one up on a ring, or if there is a hardware problem
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssofterrors
            
            	The number of Soft Errors the interface has detected. It directly corresponds to the number of Report Error MAC frames that this interface has transmitted. Soft Errors are those which are recoverable by the MAC layer protocols
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statstokenerrors
            
            	This counter is incremented when a station acting as the active monitor recognizes an error condition that needs a token transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statstransmitbeacons
            
            	The number of times this interface has transmitted a beacon frame
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'TOKENRING-MIB'
            _revision = '1994-10-23'

            def __init__(self):
                super(TokenringMib.Dot5Statstable.Dot5Statsentry, self).__init__()

                self.yang_name = "dot5StatsEntry"
                self.yang_parent_name = "dot5StatsTable"

                self.dot5statsifindex = YLeaf(YType.int32, "dot5StatsIfIndex")

                self.dot5statsaborttranserrors = YLeaf(YType.uint32, "dot5StatsAbortTransErrors")

                self.dot5statsacerrors = YLeaf(YType.uint32, "dot5StatsACErrors")

                self.dot5statsbursterrors = YLeaf(YType.uint32, "dot5StatsBurstErrors")

                self.dot5statsframecopiederrors = YLeaf(YType.uint32, "dot5StatsFrameCopiedErrors")

                self.dot5statsfreqerrors = YLeaf(YType.uint32, "dot5StatsFreqErrors")

                self.dot5statsharderrors = YLeaf(YType.uint32, "dot5StatsHardErrors")

                self.dot5statsinternalerrors = YLeaf(YType.uint32, "dot5StatsInternalErrors")

                self.dot5statslineerrors = YLeaf(YType.uint32, "dot5StatsLineErrors")

                self.dot5statslobewires = YLeaf(YType.uint32, "dot5StatsLobeWires")

                self.dot5statslostframeerrors = YLeaf(YType.uint32, "dot5StatsLostFrameErrors")

                self.dot5statsreceivecongestions = YLeaf(YType.uint32, "dot5StatsReceiveCongestions")

                self.dot5statsrecoverys = YLeaf(YType.uint32, "dot5StatsRecoverys")

                self.dot5statsremoves = YLeaf(YType.uint32, "dot5StatsRemoves")

                self.dot5statssignalloss = YLeaf(YType.uint32, "dot5StatsSignalLoss")

                self.dot5statssingles = YLeaf(YType.uint32, "dot5StatsSingles")

                self.dot5statssofterrors = YLeaf(YType.uint32, "dot5StatsSoftErrors")

                self.dot5statstokenerrors = YLeaf(YType.uint32, "dot5StatsTokenErrors")

                self.dot5statstransmitbeacons = YLeaf(YType.uint32, "dot5StatsTransmitBeacons")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot5statsifindex",
                                "dot5statsaborttranserrors",
                                "dot5statsacerrors",
                                "dot5statsbursterrors",
                                "dot5statsframecopiederrors",
                                "dot5statsfreqerrors",
                                "dot5statsharderrors",
                                "dot5statsinternalerrors",
                                "dot5statslineerrors",
                                "dot5statslobewires",
                                "dot5statslostframeerrors",
                                "dot5statsreceivecongestions",
                                "dot5statsrecoverys",
                                "dot5statsremoves",
                                "dot5statssignalloss",
                                "dot5statssingles",
                                "dot5statssofterrors",
                                "dot5statstokenerrors",
                                "dot5statstransmitbeacons") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenringMib.Dot5Statstable.Dot5Statsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenringMib.Dot5Statstable.Dot5Statsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot5statsifindex.is_set or
                    self.dot5statsaborttranserrors.is_set or
                    self.dot5statsacerrors.is_set or
                    self.dot5statsbursterrors.is_set or
                    self.dot5statsframecopiederrors.is_set or
                    self.dot5statsfreqerrors.is_set or
                    self.dot5statsharderrors.is_set or
                    self.dot5statsinternalerrors.is_set or
                    self.dot5statslineerrors.is_set or
                    self.dot5statslobewires.is_set or
                    self.dot5statslostframeerrors.is_set or
                    self.dot5statsreceivecongestions.is_set or
                    self.dot5statsrecoverys.is_set or
                    self.dot5statsremoves.is_set or
                    self.dot5statssignalloss.is_set or
                    self.dot5statssingles.is_set or
                    self.dot5statssofterrors.is_set or
                    self.dot5statstokenerrors.is_set or
                    self.dot5statstransmitbeacons.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot5statsifindex.yfilter != YFilter.not_set or
                    self.dot5statsaborttranserrors.yfilter != YFilter.not_set or
                    self.dot5statsacerrors.yfilter != YFilter.not_set or
                    self.dot5statsbursterrors.yfilter != YFilter.not_set or
                    self.dot5statsframecopiederrors.yfilter != YFilter.not_set or
                    self.dot5statsfreqerrors.yfilter != YFilter.not_set or
                    self.dot5statsharderrors.yfilter != YFilter.not_set or
                    self.dot5statsinternalerrors.yfilter != YFilter.not_set or
                    self.dot5statslineerrors.yfilter != YFilter.not_set or
                    self.dot5statslobewires.yfilter != YFilter.not_set or
                    self.dot5statslostframeerrors.yfilter != YFilter.not_set or
                    self.dot5statsreceivecongestions.yfilter != YFilter.not_set or
                    self.dot5statsrecoverys.yfilter != YFilter.not_set or
                    self.dot5statsremoves.yfilter != YFilter.not_set or
                    self.dot5statssignalloss.yfilter != YFilter.not_set or
                    self.dot5statssingles.yfilter != YFilter.not_set or
                    self.dot5statssofterrors.yfilter != YFilter.not_set or
                    self.dot5statstokenerrors.yfilter != YFilter.not_set or
                    self.dot5statstransmitbeacons.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot5StatsEntry" + "[dot5StatsIfIndex='" + self.dot5statsifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKENRING-MIB:TOKENRING-MIB/dot5StatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot5statsifindex.is_set or self.dot5statsifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsifindex.get_name_leafdata())
                if (self.dot5statsaborttranserrors.is_set or self.dot5statsaborttranserrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsaborttranserrors.get_name_leafdata())
                if (self.dot5statsacerrors.is_set or self.dot5statsacerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsacerrors.get_name_leafdata())
                if (self.dot5statsbursterrors.is_set or self.dot5statsbursterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsbursterrors.get_name_leafdata())
                if (self.dot5statsframecopiederrors.is_set or self.dot5statsframecopiederrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsframecopiederrors.get_name_leafdata())
                if (self.dot5statsfreqerrors.is_set or self.dot5statsfreqerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsfreqerrors.get_name_leafdata())
                if (self.dot5statsharderrors.is_set or self.dot5statsharderrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsharderrors.get_name_leafdata())
                if (self.dot5statsinternalerrors.is_set or self.dot5statsinternalerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsinternalerrors.get_name_leafdata())
                if (self.dot5statslineerrors.is_set or self.dot5statslineerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statslineerrors.get_name_leafdata())
                if (self.dot5statslobewires.is_set or self.dot5statslobewires.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statslobewires.get_name_leafdata())
                if (self.dot5statslostframeerrors.is_set or self.dot5statslostframeerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statslostframeerrors.get_name_leafdata())
                if (self.dot5statsreceivecongestions.is_set or self.dot5statsreceivecongestions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsreceivecongestions.get_name_leafdata())
                if (self.dot5statsrecoverys.is_set or self.dot5statsrecoverys.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsrecoverys.get_name_leafdata())
                if (self.dot5statsremoves.is_set or self.dot5statsremoves.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statsremoves.get_name_leafdata())
                if (self.dot5statssignalloss.is_set or self.dot5statssignalloss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statssignalloss.get_name_leafdata())
                if (self.dot5statssingles.is_set or self.dot5statssingles.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statssingles.get_name_leafdata())
                if (self.dot5statssofterrors.is_set or self.dot5statssofterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statssofterrors.get_name_leafdata())
                if (self.dot5statstokenerrors.is_set or self.dot5statstokenerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statstokenerrors.get_name_leafdata())
                if (self.dot5statstransmitbeacons.is_set or self.dot5statstransmitbeacons.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5statstransmitbeacons.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot5StatsIfIndex" or name == "dot5StatsAbortTransErrors" or name == "dot5StatsACErrors" or name == "dot5StatsBurstErrors" or name == "dot5StatsFrameCopiedErrors" or name == "dot5StatsFreqErrors" or name == "dot5StatsHardErrors" or name == "dot5StatsInternalErrors" or name == "dot5StatsLineErrors" or name == "dot5StatsLobeWires" or name == "dot5StatsLostFrameErrors" or name == "dot5StatsReceiveCongestions" or name == "dot5StatsRecoverys" or name == "dot5StatsRemoves" or name == "dot5StatsSignalLoss" or name == "dot5StatsSingles" or name == "dot5StatsSoftErrors" or name == "dot5StatsTokenErrors" or name == "dot5StatsTransmitBeacons"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot5StatsIfIndex"):
                    self.dot5statsifindex = value
                    self.dot5statsifindex.value_namespace = name_space
                    self.dot5statsifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsAbortTransErrors"):
                    self.dot5statsaborttranserrors = value
                    self.dot5statsaborttranserrors.value_namespace = name_space
                    self.dot5statsaborttranserrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsACErrors"):
                    self.dot5statsacerrors = value
                    self.dot5statsacerrors.value_namespace = name_space
                    self.dot5statsacerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsBurstErrors"):
                    self.dot5statsbursterrors = value
                    self.dot5statsbursterrors.value_namespace = name_space
                    self.dot5statsbursterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsFrameCopiedErrors"):
                    self.dot5statsframecopiederrors = value
                    self.dot5statsframecopiederrors.value_namespace = name_space
                    self.dot5statsframecopiederrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsFreqErrors"):
                    self.dot5statsfreqerrors = value
                    self.dot5statsfreqerrors.value_namespace = name_space
                    self.dot5statsfreqerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsHardErrors"):
                    self.dot5statsharderrors = value
                    self.dot5statsharderrors.value_namespace = name_space
                    self.dot5statsharderrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsInternalErrors"):
                    self.dot5statsinternalerrors = value
                    self.dot5statsinternalerrors.value_namespace = name_space
                    self.dot5statsinternalerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsLineErrors"):
                    self.dot5statslineerrors = value
                    self.dot5statslineerrors.value_namespace = name_space
                    self.dot5statslineerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsLobeWires"):
                    self.dot5statslobewires = value
                    self.dot5statslobewires.value_namespace = name_space
                    self.dot5statslobewires.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsLostFrameErrors"):
                    self.dot5statslostframeerrors = value
                    self.dot5statslostframeerrors.value_namespace = name_space
                    self.dot5statslostframeerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsReceiveCongestions"):
                    self.dot5statsreceivecongestions = value
                    self.dot5statsreceivecongestions.value_namespace = name_space
                    self.dot5statsreceivecongestions.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsRecoverys"):
                    self.dot5statsrecoverys = value
                    self.dot5statsrecoverys.value_namespace = name_space
                    self.dot5statsrecoverys.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsRemoves"):
                    self.dot5statsremoves = value
                    self.dot5statsremoves.value_namespace = name_space
                    self.dot5statsremoves.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsSignalLoss"):
                    self.dot5statssignalloss = value
                    self.dot5statssignalloss.value_namespace = name_space
                    self.dot5statssignalloss.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsSingles"):
                    self.dot5statssingles = value
                    self.dot5statssingles.value_namespace = name_space
                    self.dot5statssingles.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsSoftErrors"):
                    self.dot5statssofterrors = value
                    self.dot5statssofterrors.value_namespace = name_space
                    self.dot5statssofterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsTokenErrors"):
                    self.dot5statstokenerrors = value
                    self.dot5statstokenerrors.value_namespace = name_space
                    self.dot5statstokenerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5StatsTransmitBeacons"):
                    self.dot5statstransmitbeacons = value
                    self.dot5statstransmitbeacons.value_namespace = name_space
                    self.dot5statstransmitbeacons.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot5statsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot5statsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot5StatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKENRING-MIB:TOKENRING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot5StatsEntry"):
                for c in self.dot5statsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenringMib.Dot5Statstable.Dot5Statsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot5statsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot5StatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Dot5Timertable(Entity):
        """
        This table contains Token Ring interface
        timer values, one entry per 802.5
        interface.
        
        .. attribute:: dot5timerentry
        
        	A list of Token Ring timer values for an 802.5 interface
        	**type**\: list of    :py:class:`Dot5Timerentry <ydk.models.cisco_ios_xe.TOKENRING_MIB.TokenringMib.Dot5Timertable.Dot5Timerentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'TOKENRING-MIB'
        _revision = '1994-10-23'

        def __init__(self):
            super(TokenringMib.Dot5Timertable, self).__init__()

            self.yang_name = "dot5TimerTable"
            self.yang_parent_name = "TOKENRING-MIB"

            self.dot5timerentry = YList(self)

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
                        super(TokenringMib.Dot5Timertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TokenringMib.Dot5Timertable, self).__setattr__(name, value)


        class Dot5Timerentry(Entity):
            """
            A list of Token Ring timer values for an
            802.5 interface.
            
            .. attribute:: dot5timerifindex  <key>
            
            	The value of this object identifies the 802.5 interface for which this entry contains timer values.  The value of   this object for a particular interface has the same value as MIB\-II's ifIndex object for the same interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timeractivemon
            
            	The time\-out value used by the active monitor to stimulate the enqueuing of an AMP PDU for transmission, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerbeaconreceive
            
            	The time\-out value which determines how long a station shall receive Beacon frames from its downstream neighbor before entering the Bypass state, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerbeacontransmit
            
            	The time\-out value which determines how long a station shall remain in the state of transmitting Beacon frames before entering the Bypass state, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timererrorreport
            
            	The time\-out value which determines how often a station shall send a Report Error MAC frame to report its error counters, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerholding
            
            	Maximum period of time a station is permitted to transmit frames after capturing a token, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timernotoken
            
            	The time\-out value used to recover from various\-related error situations. If N is the maximum number of stations on the ring, the value of this timer is normally\: dot5TimerReturnRepeat + N\*dot5TimerHolding
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerqueuepdu
            
            	The time\-out value for enqueuing of an SMP PDU after reception of an AMP or SMP frame in which the A and C bits were equal to 0, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerreturnrepeat
            
            	The time\-out value used to ensure the interface will return to Repeat State, in units of 100 micro\-seconds.  The value should be greater than the maximum ring latency
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timerstandbymon
            
            	The time\-out value used by the stand\-by monitors to ensure that there is an active monitor on the ring and to detect a continuous stream of tokens, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: dot5timervalidtransmit
            
            	The time\-out value used by the active monitor to detect the absence of valid transmissions, in units of 100 micro\-seconds
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'TOKENRING-MIB'
            _revision = '1994-10-23'

            def __init__(self):
                super(TokenringMib.Dot5Timertable.Dot5Timerentry, self).__init__()

                self.yang_name = "dot5TimerEntry"
                self.yang_parent_name = "dot5TimerTable"

                self.dot5timerifindex = YLeaf(YType.int32, "dot5TimerIfIndex")

                self.dot5timeractivemon = YLeaf(YType.int32, "dot5TimerActiveMon")

                self.dot5timerbeaconreceive = YLeaf(YType.int32, "dot5TimerBeaconReceive")

                self.dot5timerbeacontransmit = YLeaf(YType.int32, "dot5TimerBeaconTransmit")

                self.dot5timererrorreport = YLeaf(YType.int32, "dot5TimerErrorReport")

                self.dot5timerholding = YLeaf(YType.int32, "dot5TimerHolding")

                self.dot5timernotoken = YLeaf(YType.int32, "dot5TimerNoToken")

                self.dot5timerqueuepdu = YLeaf(YType.int32, "dot5TimerQueuePDU")

                self.dot5timerreturnrepeat = YLeaf(YType.int32, "dot5TimerReturnRepeat")

                self.dot5timerstandbymon = YLeaf(YType.int32, "dot5TimerStandbyMon")

                self.dot5timervalidtransmit = YLeaf(YType.int32, "dot5TimerValidTransmit")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dot5timerifindex",
                                "dot5timeractivemon",
                                "dot5timerbeaconreceive",
                                "dot5timerbeacontransmit",
                                "dot5timererrorreport",
                                "dot5timerholding",
                                "dot5timernotoken",
                                "dot5timerqueuepdu",
                                "dot5timerreturnrepeat",
                                "dot5timerstandbymon",
                                "dot5timervalidtransmit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TokenringMib.Dot5Timertable.Dot5Timerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TokenringMib.Dot5Timertable.Dot5Timerentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.dot5timerifindex.is_set or
                    self.dot5timeractivemon.is_set or
                    self.dot5timerbeaconreceive.is_set or
                    self.dot5timerbeacontransmit.is_set or
                    self.dot5timererrorreport.is_set or
                    self.dot5timerholding.is_set or
                    self.dot5timernotoken.is_set or
                    self.dot5timerqueuepdu.is_set or
                    self.dot5timerreturnrepeat.is_set or
                    self.dot5timerstandbymon.is_set or
                    self.dot5timervalidtransmit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dot5timerifindex.yfilter != YFilter.not_set or
                    self.dot5timeractivemon.yfilter != YFilter.not_set or
                    self.dot5timerbeaconreceive.yfilter != YFilter.not_set or
                    self.dot5timerbeacontransmit.yfilter != YFilter.not_set or
                    self.dot5timererrorreport.yfilter != YFilter.not_set or
                    self.dot5timerholding.yfilter != YFilter.not_set or
                    self.dot5timernotoken.yfilter != YFilter.not_set or
                    self.dot5timerqueuepdu.yfilter != YFilter.not_set or
                    self.dot5timerreturnrepeat.yfilter != YFilter.not_set or
                    self.dot5timerstandbymon.yfilter != YFilter.not_set or
                    self.dot5timervalidtransmit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dot5TimerEntry" + "[dot5TimerIfIndex='" + self.dot5timerifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TOKENRING-MIB:TOKENRING-MIB/dot5TimerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dot5timerifindex.is_set or self.dot5timerifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerifindex.get_name_leafdata())
                if (self.dot5timeractivemon.is_set or self.dot5timeractivemon.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timeractivemon.get_name_leafdata())
                if (self.dot5timerbeaconreceive.is_set or self.dot5timerbeaconreceive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerbeaconreceive.get_name_leafdata())
                if (self.dot5timerbeacontransmit.is_set or self.dot5timerbeacontransmit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerbeacontransmit.get_name_leafdata())
                if (self.dot5timererrorreport.is_set or self.dot5timererrorreport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timererrorreport.get_name_leafdata())
                if (self.dot5timerholding.is_set or self.dot5timerholding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerholding.get_name_leafdata())
                if (self.dot5timernotoken.is_set or self.dot5timernotoken.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timernotoken.get_name_leafdata())
                if (self.dot5timerqueuepdu.is_set or self.dot5timerqueuepdu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerqueuepdu.get_name_leafdata())
                if (self.dot5timerreturnrepeat.is_set or self.dot5timerreturnrepeat.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerreturnrepeat.get_name_leafdata())
                if (self.dot5timerstandbymon.is_set or self.dot5timerstandbymon.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timerstandbymon.get_name_leafdata())
                if (self.dot5timervalidtransmit.is_set or self.dot5timervalidtransmit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dot5timervalidtransmit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dot5TimerIfIndex" or name == "dot5TimerActiveMon" or name == "dot5TimerBeaconReceive" or name == "dot5TimerBeaconTransmit" or name == "dot5TimerErrorReport" or name == "dot5TimerHolding" or name == "dot5TimerNoToken" or name == "dot5TimerQueuePDU" or name == "dot5TimerReturnRepeat" or name == "dot5TimerStandbyMon" or name == "dot5TimerValidTransmit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dot5TimerIfIndex"):
                    self.dot5timerifindex = value
                    self.dot5timerifindex.value_namespace = name_space
                    self.dot5timerifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerActiveMon"):
                    self.dot5timeractivemon = value
                    self.dot5timeractivemon.value_namespace = name_space
                    self.dot5timeractivemon.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerBeaconReceive"):
                    self.dot5timerbeaconreceive = value
                    self.dot5timerbeaconreceive.value_namespace = name_space
                    self.dot5timerbeaconreceive.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerBeaconTransmit"):
                    self.dot5timerbeacontransmit = value
                    self.dot5timerbeacontransmit.value_namespace = name_space
                    self.dot5timerbeacontransmit.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerErrorReport"):
                    self.dot5timererrorreport = value
                    self.dot5timererrorreport.value_namespace = name_space
                    self.dot5timererrorreport.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerHolding"):
                    self.dot5timerholding = value
                    self.dot5timerholding.value_namespace = name_space
                    self.dot5timerholding.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerNoToken"):
                    self.dot5timernotoken = value
                    self.dot5timernotoken.value_namespace = name_space
                    self.dot5timernotoken.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerQueuePDU"):
                    self.dot5timerqueuepdu = value
                    self.dot5timerqueuepdu.value_namespace = name_space
                    self.dot5timerqueuepdu.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerReturnRepeat"):
                    self.dot5timerreturnrepeat = value
                    self.dot5timerreturnrepeat.value_namespace = name_space
                    self.dot5timerreturnrepeat.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerStandbyMon"):
                    self.dot5timerstandbymon = value
                    self.dot5timerstandbymon.value_namespace = name_space
                    self.dot5timerstandbymon.value_namespace_prefix = name_space_prefix
                if(value_path == "dot5TimerValidTransmit"):
                    self.dot5timervalidtransmit = value
                    self.dot5timervalidtransmit.value_namespace = name_space
                    self.dot5timervalidtransmit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.dot5timerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.dot5timerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dot5TimerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TOKENRING-MIB:TOKENRING-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dot5TimerEntry"):
                for c in self.dot5timerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TokenringMib.Dot5Timertable.Dot5Timerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.dot5timerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dot5TimerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.dot5statstable is not None and self.dot5statstable.has_data()) or
            (self.dot5table is not None and self.dot5table.has_data()) or
            (self.dot5timertable is not None and self.dot5timertable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dot5statstable is not None and self.dot5statstable.has_operation()) or
            (self.dot5table is not None and self.dot5table.has_operation()) or
            (self.dot5timertable is not None and self.dot5timertable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "TOKENRING-MIB:TOKENRING-MIB" + path_buffer

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

        if (child_yang_name == "dot5StatsTable"):
            if (self.dot5statstable is None):
                self.dot5statstable = TokenringMib.Dot5Statstable()
                self.dot5statstable.parent = self
                self._children_name_map["dot5statstable"] = "dot5StatsTable"
            return self.dot5statstable

        if (child_yang_name == "dot5Table"):
            if (self.dot5table is None):
                self.dot5table = TokenringMib.Dot5Table()
                self.dot5table.parent = self
                self._children_name_map["dot5table"] = "dot5Table"
            return self.dot5table

        if (child_yang_name == "dot5TimerTable"):
            if (self.dot5timertable is None):
                self.dot5timertable = TokenringMib.Dot5Timertable()
                self.dot5timertable.parent = self
                self._children_name_map["dot5timertable"] = "dot5TimerTable"
            return self.dot5timertable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dot5StatsTable" or name == "dot5Table" or name == "dot5TimerTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TokenringMib()
        return self._top_entity

