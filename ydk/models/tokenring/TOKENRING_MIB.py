""" TOKENRING_MIB 

The MIB module for IEEE Token Ring entities.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity_Identity


class Dot5ChipSetIBM16_Identity(ObjectIdentity_Identity):
    """
    IBM's 16/4 Mbs chip set.
    
    

    """

    _prefix = 'tokenring-mib'
    _revision = '1994-10-23'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
        return meta._meta_table['Dot5ChipSetIBM16_Identity']['meta_info']


class Dot5ChipSetTItms380_Identity(ObjectIdentity_Identity):
    """
    Texas Instruments' TMS 380 4Mbs chip\-set
    
    

    """

    _prefix = 'tokenring-mib'
    _revision = '1994-10-23'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
        return meta._meta_table['Dot5ChipSetTItms380_Identity']['meta_info']


class Dot5ChipSetTItms380c16_Identity(ObjectIdentity_Identity):
    """
    Texas Instruments' TMS 380C16 16/4 Mbs chip\-set
    
    

    """

    _prefix = 'tokenring-mib'
    _revision = '1994-10-23'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
        return meta._meta_table['Dot5ChipSetTItms380c16_Identity']['meta_info']


class Dot5TestFullDuplexLoopBack_Identity(ObjectIdentity_Identity):
    """
    Invoking this test on a 802.5 interface causes the
    interface to check the path from memory through the
    chip set's internal logic and back to memory, thus
    checking the proper functioning of the system's
    interface to the chip set.
    
    

    """

    _prefix = 'tokenring-mib'
    _revision = '1994-10-23'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
        return meta._meta_table['Dot5TestFullDuplexLoopBack_Identity']['meta_info']


class Dot5TestInsertFunc_Identity(ObjectIdentity_Identity):
    """
    Invoking this test causes the station to test the insert
    ring logic of the hardware if the station's lobe media
    cable is connected to a wiring concentrator.  Note that
    this command inserts the station into the network, and
    thus, could cause problems if the station is connected
    to a operational network.
    
    

    """

    _prefix = 'tokenring-mib'
    _revision = '1994-10-23'

    def __init__(self):
        ObjectIdentity_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
        return meta._meta_table['Dot5TestInsertFunc_Identity']['meta_info']


class TOKENRINGMIB(object):
    """
    
    
    .. attribute:: dot5statstable
    
    	A table containing Token Ring statistics, one entry per 802.5 interface.     All the statistics are defined using the syntax Counter32 as 32\-bit wrap around counters.  Thus, if an interface's hardware maintains these statistics in 16\-bit counters, then the agent must read the hardware's counters frequently enough to prevent loss of significance, in order to maintain 32\-bit counters in software
    	**type**\: :py:class:`Dot5StatsTable <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5StatsTable>`
    
    .. attribute:: dot5table
    
    	This table contains Token Ring interface parameters and state variables, one entry per 802.5 interface
    	**type**\: :py:class:`Dot5Table <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table>`
    
    .. attribute:: dot5timertable
    
    	This table contains Token Ring interface timer values, one entry per 802.5 interface
    	**type**\: :py:class:`Dot5TimerTable <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5TimerTable>`
    
    

    """

    _prefix = 'tokenring-mib'
    _revision = '1994-10-23'

    def __init__(self):
        self.dot5statstable = TOKENRINGMIB.Dot5StatsTable()
        self.dot5statstable.parent = self
        self.dot5table = TOKENRINGMIB.Dot5Table()
        self.dot5table.parent = self
        self.dot5timertable = TOKENRINGMIB.Dot5TimerTable()
        self.dot5timertable.parent = self


    class Dot5StatsTable(object):
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
        	**type**\: list of :py:class:`Dot5StatsEntry <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5StatsTable.Dot5StatsEntry>`
        
        

        """

        _prefix = 'tokenring-mib'
        _revision = '1994-10-23'

        def __init__(self):
            self.parent = None
            self.dot5statsentry = YList()
            self.dot5statsentry.parent = self
            self.dot5statsentry.name = 'dot5statsentry'


        class Dot5StatsEntry(object):
            """
            An entry contains the 802.5 statistics
            for a particular interface.
            
            .. attribute:: dot5statsifindex
            
            	The value of this object identifies the 802.5 interface for which this entry contains management information.  The value of this object for a particular interface has the same value as MIB\-II's ifIndex object for the same interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5statsaborttranserrors
            
            	This counter is incremented when a station transmits an abort delimiter while transmitting
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsacerrors
            
            	This counter is incremented when a station receives an AMP or SMP frame in which A is equal to C is equal to 0, and then receives another SMP frame with A is equal to C is equal to 0 without first receiving an AMP frame. It denotes a station that cannot set the AC bits properly
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsbursterrors
            
            	This counter is incremented when a station detects the absence of transitions for five half\-bit timers (burst\-five error)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsframecopiederrors
            
            	This counter is incremented when a station recognizes a frame addressed to its specific address and detects that the FS field A bits are set to 1 indicating a possible line hit or duplicate address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsfreqerrors
            
            	The number of times the interface has detected that the frequency of the incoming signal differs from the expected frequency by more than that specified by the IEEE 802.5 standard
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsharderrors
            
            	The number of times this interface has detected an immediately recoverable fatal error.  It denotes the number of times this interface is either transmitting or receiving beacon MAC frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsinternalerrors
            
            	This counter is incremented when a station recognizes an internal error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslineerrors
            
            	This counter is incremented when a frame or token is copied or repeated by a station, the E bit is zero in the frame or token and one of the following conditions exists\: 1) there is a non\-data bit (J or K bit) between the SD and the ED of the frame or token, or 2) there is an FCS error in the frame
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statslobewires
            
            	The number of times the interface has detected an open or short circuit in the lobe data path.  The adapter will be closed and dot5RingState will signify this condition
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
            
            .. attribute:: dot5statsrecoverys
            
            	The number of Claim Token MAC frames received or transmitted after the interface has received a Ring Purge MAC frame.  This counter signifies the number of times the ring has been purged and is being recovered back into a normal operating state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statsremoves
            
            	The number of times the interface has received a Remove Ring Station MAC frame request.  When this frame is received the interface will enter the close state and dot5RingState will signify this condition
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssignalloss
            
            	The number of times this interface has detected the loss of signal condition from the ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssingles
            
            	The number of times the interface has sensed that it is the only station on the ring.  This will happen if the interface is the first one up on a ring, or if there is a hardware problem
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statssofterrors
            
            	The number of Soft Errors the interface has detected. It directly corresponds to the number of Report Error MAC frames that this interface has transmitted. Soft Errors are those which are recoverable by the MAC layer protocols
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statstokenerrors
            
            	This counter is incremented when a station acting as the active monitor recognizes an error condition that needs a token transmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5statstransmitbeacons
            
            	The number of times this interface has transmitted a beacon frame
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tokenring-mib'
            _revision = '1994-10-23'

            def __init__(self):
                self.parent = None
                self.dot5statsifindex = None
                self.dot5statsaborttranserrors = None
                self.dot5statsacerrors = None
                self.dot5statsbursterrors = None
                self.dot5statsframecopiederrors = None
                self.dot5statsfreqerrors = None
                self.dot5statsharderrors = None
                self.dot5statsinternalerrors = None
                self.dot5statslineerrors = None
                self.dot5statslobewires = None
                self.dot5statslostframeerrors = None
                self.dot5statsreceivecongestions = None
                self.dot5statsrecoverys = None
                self.dot5statsremoves = None
                self.dot5statssignalloss = None
                self.dot5statssingles = None
                self.dot5statssofterrors = None
                self.dot5statstokenerrors = None
                self.dot5statstransmitbeacons = None

            @property
            def _common_path(self):
                if self.dot5statsifindex is None:
                    raise YPYDataValidationError('Key property dot5statsifindex is None')

                return '/TOKENRING-MIB:TOKENRING-MIB/TOKENRING-MIB:dot5StatsTable/TOKENRING-MIB:dot5StatsEntry[TOKENRING-MIB:dot5StatsIfIndex = ' + str(self.dot5statsifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot5statsifindex is not None:
                    return True

                if self.dot5statsaborttranserrors is not None:
                    return True

                if self.dot5statsacerrors is not None:
                    return True

                if self.dot5statsbursterrors is not None:
                    return True

                if self.dot5statsframecopiederrors is not None:
                    return True

                if self.dot5statsfreqerrors is not None:
                    return True

                if self.dot5statsharderrors is not None:
                    return True

                if self.dot5statsinternalerrors is not None:
                    return True

                if self.dot5statslineerrors is not None:
                    return True

                if self.dot5statslobewires is not None:
                    return True

                if self.dot5statslostframeerrors is not None:
                    return True

                if self.dot5statsreceivecongestions is not None:
                    return True

                if self.dot5statsrecoverys is not None:
                    return True

                if self.dot5statsremoves is not None:
                    return True

                if self.dot5statssignalloss is not None:
                    return True

                if self.dot5statssingles is not None:
                    return True

                if self.dot5statssofterrors is not None:
                    return True

                if self.dot5statstokenerrors is not None:
                    return True

                if self.dot5statstransmitbeacons is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                return meta._meta_table['TOKENRINGMIB.Dot5StatsTable.Dot5StatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKENRING-MIB:TOKENRING-MIB/TOKENRING-MIB:dot5StatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot5statsentry is not None:
                for child_ref in self.dot5statsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
            return meta._meta_table['TOKENRINGMIB.Dot5StatsTable']['meta_info']


    class Dot5Table(object):
        """
        This table contains Token Ring interface
        parameters and state variables, one entry
        per 802.5 interface.
        
        .. attribute:: dot5entry
        
        	A list of Token Ring status and parameter values for an 802.5 interface
        	**type**\: list of :py:class:`Dot5Entry <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry>`
        
        

        """

        _prefix = 'tokenring-mib'
        _revision = '1994-10-23'

        def __init__(self):
            self.parent = None
            self.dot5entry = YList()
            self.dot5entry.parent = self
            self.dot5entry.name = 'dot5entry'


        class Dot5Entry(object):
            """
            A list of Token Ring status and parameter
            values for an 802.5 interface.
            
            .. attribute:: dot5ifindex
            
            	The value of this object identifies the 802.5 interface for which this entry contains management information.  The value of this object for a particular interface has the same value as the ifIndex object, defined in MIB\-II for the same interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5actmonparticipate
            
            	If this object has a value of true(1) then this interface will participate in the active monitor selection process.  If the value is false(2) then it will not. Setting this object does not take effect until the next Active Monitor election, and might not take effect until the next time the interface is opened
            	**type**\: :py:class:`Dot5ActMonParticipate_Enum <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5ActMonParticipate_Enum>`
            
            .. attribute:: dot5commands
            
            	When this object is set to the value of open(2), the station should go into the open state.  The progress and success of the open is given by the values of the objects dot5RingState and dot5RingOpenStatus.     When this object is set to the value of reset(3), then the station should do a reset.  On a reset, all MIB counters should retain their values, if possible. Other side affects are dependent on the hardware chip set.     When this object is set to the value of close(4), the station should go into the stopped state by removing itself from the ring.     Setting this object to a value of noop(1) has no effect.     When read, this object always has a value of noop(1).     The open(2) and close(4) values correspond to the up(1) and down(2) values of MIB\-II's ifAdminStatus and ifOperStatus, i.e., the setting of ifAdminStatus and   dot5Commands affects the values of both dot5Commands and ifOperStatus
            	**type**\: :py:class:`Dot5Commands_Enum <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Commands_Enum>`
            
            .. attribute:: dot5functional
            
            	The bit mask of all Token Ring functional addresses for which this interface will accept frames
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot5lastbeaconsent
            
            	The value of MIB\-II's sysUpTime object at which the local system last transmitted a Beacon frame on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot5ringopenstatus
            
            	This object indicates the success, or the reason for failure, of the station's most recent attempt to enter the ring
            	**type**\: :py:class:`Dot5RingOpenStatus_Enum <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5RingOpenStatus_Enum>`
            
            .. attribute:: dot5ringspeed
            
            	The ring\-speed at the next insertion into the ring.  Note that this may or may not be different to the current ring\-speed which is given by MIB\-II's ifSpeed.  For interfaces which do not support changing ring\-speed, dot5RingSpeed can only be set to its current value.  When dot5RingSpeed has the value unknown(1), the ring's actual ring\-speed is to be used
            	**type**\: :py:class:`Dot5RingSpeed_Enum <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5RingSpeed_Enum>`
            
            .. attribute:: dot5ringstate
            
            	The current interface state with respect to entering or leaving the ring
            	**type**\: :py:class:`Dot5RingState_Enum <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5RingState_Enum>`
            
            .. attribute:: dot5ringstatus
            
            	The current interface status which can be used to diagnose fluctuating problems that can occur on token rings, after a station has successfully been added to the ring.    Before an open is completed, this object has the value for the 'no status' condition.  The dot5RingState and dot5RingOpenStatus objects provide for debugging problems when the station can not even enter the ring.     The object's value is a sum of values, one for each currently applicable condition.  The following values are defined for various conditions\:          0 = No Problems detected        32 = Ring Recovery        64 = Single Station       256 = Remove Received       512 = reserved      1024 = Auto\-Removal Error      2048 = Lobe Wire Fault      4096 = Transmit Beacon      8192 = Soft Error     16384 = Hard Error     32768 = Signal Loss    131072 = no status, open not completed
            	**type**\: int
            
            	**range:** 0..262143
            
            .. attribute:: dot5upstream
            
            	The MAC\-address of the up stream neighbor station in the ring
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'tokenring-mib'
            _revision = '1994-10-23'

            def __init__(self):
                self.parent = None
                self.dot5ifindex = None
                self.dot5actmonparticipate = None
                self.dot5commands = None
                self.dot5functional = None
                self.dot5lastbeaconsent = None
                self.dot5ringopenstatus = None
                self.dot5ringspeed = None
                self.dot5ringstate = None
                self.dot5ringstatus = None
                self.dot5upstream = None

            class Dot5ActMonParticipate_Enum(Enum):
                """
                Dot5ActMonParticipate_Enum

                If this object has a value of true(1) then
                this interface will participate in the
                active monitor selection process.  If the
                value is false(2) then it will not.
                Setting this object does not take effect
                until the next Active Monitor election, and
                might not take effect until the next time
                the interface is opened.

                """

                TRUE = 1

                FALSE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                    return meta._meta_table['TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5ActMonParticipate_Enum']


            class Dot5Commands_Enum(Enum):
                """
                Dot5Commands_Enum

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

                """

                NOOP = 1

                OPEN = 2

                RESET = 3

                CLOSE = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                    return meta._meta_table['TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5Commands_Enum']


            class Dot5RingOpenStatus_Enum(Enum):
                """
                Dot5RingOpenStatus_Enum

                This object indicates the success, or the
                reason for failure, of the station's most
                recent attempt to enter the ring.

                """

                NOOPEN = 1

                BADPARAM = 2

                LOBEFAILED = 3

                SIGNALLOSS = 4

                INSERTIONTIMEOUT = 5

                RINGFAILED = 6

                BEACONING = 7

                DUPLICATEMAC = 8

                REQUESTFAILED = 9

                REMOVERECEIVED = 10

                OPEN = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                    return meta._meta_table['TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5RingOpenStatus_Enum']


            class Dot5RingSpeed_Enum(Enum):
                """
                Dot5RingSpeed_Enum

                The ring\-speed at the next insertion into
                the ring.  Note that this may or may not be
                different to the current ring\-speed which is
                given by MIB\-II's ifSpeed.  For interfaces
                which do not support changing ring\-speed,
                dot5RingSpeed can only be set to its current
                value.  When dot5RingSpeed has the value
                unknown(1), the ring's actual ring\-speed is
                to be used.

                """

                UNKNOWN = 1

                ONEMEGABIT = 2

                FOURMEGABIT = 3

                SIXTEENMEGABIT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                    return meta._meta_table['TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5RingSpeed_Enum']


            class Dot5RingState_Enum(Enum):
                """
                Dot5RingState_Enum

                The current interface state with respect
                to entering or leaving the ring.

                """

                OPENED = 1

                CLOSED = 2

                OPENING = 3

                CLOSING = 4

                OPENFAILURE = 5

                RINGFAILURE = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                    return meta._meta_table['TOKENRINGMIB.Dot5Table.Dot5Entry.Dot5RingState_Enum']


            @property
            def _common_path(self):
                if self.dot5ifindex is None:
                    raise YPYDataValidationError('Key property dot5ifindex is None')

                return '/TOKENRING-MIB:TOKENRING-MIB/TOKENRING-MIB:dot5Table/TOKENRING-MIB:dot5Entry[TOKENRING-MIB:dot5IfIndex = ' + str(self.dot5ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot5ifindex is not None:
                    return True

                if self.dot5actmonparticipate is not None:
                    return True

                if self.dot5commands is not None:
                    return True

                if self.dot5functional is not None:
                    return True

                if self.dot5lastbeaconsent is not None:
                    return True

                if self.dot5ringopenstatus is not None:
                    return True

                if self.dot5ringspeed is not None:
                    return True

                if self.dot5ringstate is not None:
                    return True

                if self.dot5ringstatus is not None:
                    return True

                if self.dot5upstream is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                return meta._meta_table['TOKENRINGMIB.Dot5Table.Dot5Entry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKENRING-MIB:TOKENRING-MIB/TOKENRING-MIB:dot5Table'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot5entry is not None:
                for child_ref in self.dot5entry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
            return meta._meta_table['TOKENRINGMIB.Dot5Table']['meta_info']


    class Dot5TimerTable(object):
        """
        This table contains Token Ring interface
        timer values, one entry per 802.5
        interface.
        
        .. attribute:: dot5timerentry
        
        	A list of Token Ring timer values for an 802.5 interface
        	**type**\: list of :py:class:`Dot5TimerEntry <ydk.models.tokenring.TOKENRING_MIB.TOKENRINGMIB.Dot5TimerTable.Dot5TimerEntry>`
        
        

        """

        _prefix = 'tokenring-mib'
        _revision = '1994-10-23'

        def __init__(self):
            self.parent = None
            self.dot5timerentry = YList()
            self.dot5timerentry.parent = self
            self.dot5timerentry.name = 'dot5timerentry'


        class Dot5TimerEntry(object):
            """
            A list of Token Ring timer values for an
            802.5 interface.
            
            .. attribute:: dot5timerifindex
            
            	The value of this object identifies the 802.5 interface for which this entry contains timer values.  The value of   this object for a particular interface has the same value as MIB\-II's ifIndex object for the same interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timeractivemon
            
            	The time\-out value used by the active monitor to stimulate the enqueuing of an AMP PDU for transmission, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timerbeaconreceive
            
            	The time\-out value which determines how long a station shall receive Beacon frames from its downstream neighbor before entering the Bypass state, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timerbeacontransmit
            
            	The time\-out value which determines how long a station shall remain in the state of transmitting Beacon frames before entering the Bypass state, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timererrorreport
            
            	The time\-out value which determines how often a station shall send a Report Error MAC frame to report its error counters, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timerholding
            
            	Maximum period of time a station is permitted to transmit frames after capturing a token, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timernotoken
            
            	The time\-out value used to recover from various\-related error situations. If N is the maximum number of stations on the ring, the value of this timer is normally\: dot5TimerReturnRepeat + N\*dot5TimerHolding
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timerqueuepdu
            
            	The time\-out value for enqueuing of an SMP PDU after reception of an AMP or SMP frame in which the A and C bits were equal to 0, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timerreturnrepeat
            
            	The time\-out value used to ensure the interface will return to Repeat State, in units of 100 micro\-seconds.  The value should be greater than the maximum ring latency
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timerstandbymon
            
            	The time\-out value used by the stand\-by monitors to ensure that there is an active monitor on the ring and to detect a continuous stream of tokens, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot5timervalidtransmit
            
            	The time\-out value used by the active monitor to detect the absence of valid transmissions, in units of 100 micro\-seconds
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'tokenring-mib'
            _revision = '1994-10-23'

            def __init__(self):
                self.parent = None
                self.dot5timerifindex = None
                self.dot5timeractivemon = None
                self.dot5timerbeaconreceive = None
                self.dot5timerbeacontransmit = None
                self.dot5timererrorreport = None
                self.dot5timerholding = None
                self.dot5timernotoken = None
                self.dot5timerqueuepdu = None
                self.dot5timerreturnrepeat = None
                self.dot5timerstandbymon = None
                self.dot5timervalidtransmit = None

            @property
            def _common_path(self):
                if self.dot5timerifindex is None:
                    raise YPYDataValidationError('Key property dot5timerifindex is None')

                return '/TOKENRING-MIB:TOKENRING-MIB/TOKENRING-MIB:dot5TimerTable/TOKENRING-MIB:dot5TimerEntry[TOKENRING-MIB:dot5TimerIfIndex = ' + str(self.dot5timerifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot5timerifindex is not None:
                    return True

                if self.dot5timeractivemon is not None:
                    return True

                if self.dot5timerbeaconreceive is not None:
                    return True

                if self.dot5timerbeacontransmit is not None:
                    return True

                if self.dot5timererrorreport is not None:
                    return True

                if self.dot5timerholding is not None:
                    return True

                if self.dot5timernotoken is not None:
                    return True

                if self.dot5timerqueuepdu is not None:
                    return True

                if self.dot5timerreturnrepeat is not None:
                    return True

                if self.dot5timerstandbymon is not None:
                    return True

                if self.dot5timervalidtransmit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
                return meta._meta_table['TOKENRINGMIB.Dot5TimerTable.Dot5TimerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKENRING-MIB:TOKENRING-MIB/TOKENRING-MIB:dot5TimerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot5timerentry is not None:
                for child_ref in self.dot5timerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
            return meta._meta_table['TOKENRINGMIB.Dot5TimerTable']['meta_info']

    @property
    def _common_path(self):

        return '/TOKENRING-MIB:TOKENRING-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.dot5statstable is not None and self.dot5statstable._has_data():
            return True

        if self.dot5statstable is not None and self.dot5statstable.is_presence():
            return True

        if self.dot5table is not None and self.dot5table._has_data():
            return True

        if self.dot5table is not None and self.dot5table.is_presence():
            return True

        if self.dot5timertable is not None and self.dot5timertable._has_data():
            return True

        if self.dot5timertable is not None and self.dot5timertable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.tokenring._meta import _TOKENRING_MIB as meta
        return meta._meta_table['TOKENRINGMIB']['meta_info']


