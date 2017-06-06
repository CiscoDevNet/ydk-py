""" CISCO_RF_MIB 

This MIB provides configuration control and status for the
Redundancy Framework (RF) subsystem. RF provides a mechanism
for logical redundancy of software functionality and is
designed to support 1\:1 redundancy on processor cards. RF is
not intended to solve all redundancy schemes. Nor is RF
designed to support redundant hardware, such as power
supplies.

Redundancy is concerned with the duplication of data elements
and software functions to provide an alternative in case of
failure. It is a key component to meeting 99.999% availability
requirements for Class 5 carrier solutions.

In the scope of this MIB definition, peer software elements
are redundant and redundant software elements are peers.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class RfactionEnum(Enum):
    """
    RfactionEnum

    Administrative commands to invoke in the RF subsystem.

    noAction

        \- no action (do nothing)

    reloadPeer

        \- reset the redundant peer unit

    reloadShelf

        \- reset the entire shelf

    switchActivity

        \- safely SWACT to peer unit and go standby

    forceSwitchActivity

        \- switch activity; ignoring pre\-conditions, system

          warnings and safety checks.

    When the value is set to 'noAction' no operation is performed.

    When read, the value 'noAction' is always returned.

    .. data:: noAction = 0

    .. data:: reloadPeer = 1

    .. data:: reloadShelf = 2

    .. data:: switchActivity = 3

    .. data:: forceSwitchActivity = 4

    """

    noAction = 0

    reloadPeer = 1

    reloadShelf = 2

    switchActivity = 3

    forceSwitchActivity = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['RfactionEnum']


class RfclientstatusEnum(Enum):
    """
    RfclientstatusEnum

    The status of a RF client before, during and after

    switchover.

    noStatus

        \- No status information is available for this client.

    clientNotRedundant

        \- Client is active. But there is no redundancy to this

          client. This could be because there is no standby or

          the client cannot claim that the standby client can

          take over without losing data or traffic during a

          switchover.

    clientRedundancyInProgress

        \- The client is trying to sync all data to standby and

          achieve redundancy.

    clientRedundant

        \- The client is redundant and ready for switchover. The 

          client can safely claim that there is no data or traffic 

          loss if there is a switchover.

    .. data:: noStatus = 1

    .. data:: clientNotRedundant = 2

    .. data:: clientRedundancyInProgress = 3

    .. data:: clientRedundant = 4

    """

    noStatus = 1

    clientNotRedundant = 2

    clientRedundancyInProgress = 3

    clientRedundant = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['RfclientstatusEnum']


class RfissustateEnum(Enum):
    """
    RfissustateEnum

    ISSU state represents the current system state.

    unset

        \- unset state; if the system is booted from tftp or from

          ROMMON such that the image is not the first in BOOT

    init

        \- init state; the first ISSU state that the system will

          move to after the unset state, when the ISSU process

          has just been kicked off. The first CLI that is executed

          to make this happen is the loadversion CLI.

    loadVersion

        \- Once the loadversion CLI has been executed, the state

          of the system is changed to reflect this, and this state

          is called the loadVersion state. The boot variable on

          the Standby is updated to point to the new image that the

          Standby needs to load and then it is reset.

    runVersion

        \- runVersion state; When the system is in the loadversion

          state, the Active is running the old image and the

          Standby is running the new image. When the runversion

          CLI is executed, a switchover occurs, and the Standby

          running the new image takes over as the Active. The

          state of the system at this stage is updated to

          runversion.

    commitVersion

        \- in the runversion state, the Active is running the

          new image, and the Standby is running the old image.

          When the user is satisfied with the functioning of

          the system, they execute the commitversion CLI, which

          will prepend the boot variable on the Standby with

          the new image, and then the Standby is reset. After

          this, the Standby comes up with the new image, and

          the state of the system is updated to reflect the

          commitVersion state.

    .. data:: unset = 0

    .. data:: init = 1

    .. data:: loadVersion = 2

    .. data:: runVersion = 3

    .. data:: commitVersion = 4

    """

    unset = 0

    init = 1

    loadVersion = 2

    runVersion = 3

    commitVersion = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['RfissustateEnum']


class Rfissustaterev1Enum(Enum):
    """
    Rfissustaterev1Enum

    ISSU state represents the current system state.

    init

        \- This state represents the initial state of the system.

          The ISSU process is not running at this stage. The only

          CLI for ISSU process that can be executed in this state

          is the loadversion CLI.

    systemReset

        \- If a system reset occurs, or the abortversion CLI is 

          executed, the state of the system is pushed to this state.

    loadVersion

        \- When the Standby signs in after the loadversion CLI

          is executed, the state of the system is changed to

          loadVersion.

    loadVersionSwitchover

        \- If a switchover occurs in the loadVersion state, by

          the user, or because the Active crashes, the new

          state of the system will be loadVersionSwitchover.

          It is analogous to the runVersion state, except that

          the runversion CLI was not executed.

    runVersion

        \- When the Standby signs in after executing the

          runversion CLI, the state of the system is changed

          to runVersion.

    runVersionSwitchover

        \- if a switchover occurs while the system is in the

          runVersion state, the new state will be called

          runVersionSwitchover. It is analogous to the

          loadVersion state.

    commitVersion

        \- When the Standby signs in after the commitversion CLI

          is executed, the state of the system is changed to

          commitVersion.

    .. data:: init = 0

    .. data:: systemReset = 1

    .. data:: loadVersion = 3

    .. data:: loadVersionSwitchover = 4

    .. data:: runVersion = 6

    .. data:: runVersionSwitchover = 7

    .. data:: commitVersion = 9

    """

    init = 0

    systemReset = 1

    loadVersion = 3

    loadVersionSwitchover = 4

    runVersion = 6

    runVersionSwitchover = 7

    commitVersion = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['Rfissustaterev1Enum']


class RfmodeEnum(Enum):
    """
    RfmodeEnum

    The characterization of the redundancy subsystem.

    nonRedundant

        \- the system is not redundant.

    staticLoadShareNonRedundant

        \- the system is \*not\* redundant but is load sharing.

          The load sharing is \*not\* based on operational load

          (i.e. number of calls, etc).

    dynamicLoadShareNonRedundant

        \- the system is \*not\* redundant but is load sharing.

          Load sharing is based on operational load.

    staticLoadShareRedundant

        \- the system is redundant and is load sharing. The

          load sharing is \*not\* based on operational load.

    dynamicLoadShareRedundant

        \- the system is redundant and is load sharing. Load

          sharing is based on operational load.

    coldStandbyRedundant

        \- the system is redundant but the redundant peer unit is

          not fully initialized and is not able to retain

          established calls.

    warmStandbyRedundant

        \- the system is redundant and the redundant peer unit is

          immediately able to handle new calls. The redundant

          unit is unable to retain established calls.

    hotStandbyRedundant

        \- the system is redundant and the redundant peer unit is

          able to 'instantaneously' retain established calls and

          immediately able to handle new calls.

    .. data:: nonRedundant = 1

    .. data:: staticLoadShareNonRedundant = 2

    .. data:: dynamicLoadShareNonRedundant = 3

    .. data:: staticLoadShareRedundant = 4

    .. data:: dynamicLoadShareRedundant = 5

    .. data:: coldStandbyRedundant = 6

    .. data:: warmStandbyRedundant = 7

    .. data:: hotStandbyRedundant = 8

    """

    nonRedundant = 1

    staticLoadShareNonRedundant = 2

    dynamicLoadShareNonRedundant = 3

    staticLoadShareRedundant = 4

    dynamicLoadShareRedundant = 5

    coldStandbyRedundant = 6

    warmStandbyRedundant = 7

    hotStandbyRedundant = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['RfmodeEnum']


class RfstateEnum(Enum):
    """
    RfstateEnum

    The current state of the RF subsystem.

    notKnown

        \- state is unknown

    disabled

        \- RF is not operational on this unit

    initialization

        \- establish necessary system services

    negotiation

        \- peer unit discovery and negotiation

    standbyCold

        \- client notification on standby unit

    \*standbyColdConfig

        \- standby configuration is updated from active configuration

    \*standbyColdFileSys

        \- standby file system (FS) is updated from the active FS

    \*standbyColdBulk

        \- clients sync data from active to standby

    standbyHot

        \- incremental client data sync continues. This unit is

          ready to take over activity.

    activeFast

        \- call maintenance efforts during a SWACT

    activeDrain

        \- client clean\-up phase

    activePreconfig

        \- unit is active but has not read its configuration

    activePostconfig

        \- unit is active and is post\-processing its configuration

    active

        \- unit is active and processing calls

    activeExtraload

        \- unit is active and processing calls for all feature

          boards in the system

    activeHandback

        \- unit is active, processing calls and is in the process

          of handing some resources to the other unit in the system

    \* Sub\-state of 'standbyCold'

    .. data:: notKnown = 1

    .. data:: disabled = 2

    .. data:: initialization = 3

    .. data:: negotiation = 4

    .. data:: standbyCold = 5

    .. data:: standbyColdConfig = 6

    .. data:: standbyColdFileSys = 7

    .. data:: standbyColdBulk = 8

    .. data:: standbyHot = 9

    .. data:: activeFast = 10

    .. data:: activeDrain = 11

    .. data:: activePreconfig = 12

    .. data:: activePostconfig = 13

    .. data:: active = 14

    .. data:: activeExtraload = 15

    .. data:: activeHandback = 16

    """

    notKnown = 1

    disabled = 2

    initialization = 3

    negotiation = 4

    standbyCold = 5

    standbyColdConfig = 6

    standbyColdFileSys = 7

    standbyColdBulk = 8

    standbyHot = 9

    activeFast = 10

    activeDrain = 11

    activePreconfig = 12

    activePostconfig = 13

    active = 14

    activeExtraload = 15

    activeHandback = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['RfstateEnum']


class RfswactreasontypeEnum(Enum):
    """
    RfswactreasontypeEnum

    Reason codes for the switch of activity from an active

    redundant unit to its standby peer unit.

    unsupported

        \- the 'reason code' is an unsupported feature

    none

        \- no SWACT has occurred

    notKnown

        \- reason is unknown

    userInitiated

        \- a safe, manual SWACT was initiated by user

    userForced

        \- a manual SWACT was forced by user; ignoring

          pre\-conditions, warnings and safety checks

    activeUnitFailed

        \- active unit failure caused an auto SWACT

    activeUnitRemoved

        \- active unit removal caused an auto SWACT

    .. data:: unsupported = 1

    .. data:: none = 2

    .. data:: notKnown = 3

    .. data:: userInitiated = 4

    .. data:: userForced = 5

    .. data:: activeUnitFailed = 6

    .. data:: activeUnitRemoved = 7

    """

    unsupported = 1

    none = 2

    notKnown = 3

    userInitiated = 4

    userForced = 5

    activeUnitFailed = 6

    activeUnitRemoved = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['RfswactreasontypeEnum']



class CiscoRfMib(object):
    """
    
    
    .. attribute:: crfcfg
    
    	
    	**type**\:   :py:class:`Crfcfg <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfcfg>`
    
    .. attribute:: crfhistory
    
    	
    	**type**\:   :py:class:`Crfhistory <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfhistory>`
    
    .. attribute:: crfhistoryswitchovertable
    
    	A table that tracks the history of all switchovers that have occurred since system initialization. The maximum number of entries permissible in this table is defined by cRFHistoryTableMaxLength. When the number of entries in the table reaches the maximum limit, the next entry would replace the oldest existing entry in the table
    	**type**\:   :py:class:`Crfhistoryswitchovertable <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfhistoryswitchovertable>`
    
    .. attribute:: crfstatus
    
    	
    	**type**\:   :py:class:`Crfstatus <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfstatus>`
    
    .. attribute:: crfstatusrfclienttable
    
    	This table contains a list of RF clients that are registered on the device.   RF clients are applications that have registered with  the Redundancy Facility (RF) to receive RF events and  notifications. The purpose of RF clients is to synchronize  any relevant data with the standby unit
    	**type**\:   :py:class:`Crfstatusrfclienttable <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfstatusrfclienttable>`
    
    .. attribute:: crfstatusrfmodecapstable
    
    	This table containing a list of redundancy modes that can be supported on the device
    	**type**\:   :py:class:`Crfstatusrfmodecapstable <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfstatusrfmodecapstable>`
    
    

    """

    _prefix = 'CISCO-RF-MIB'
    _revision = '2005-09-01'

    def __init__(self):
        self.crfcfg = CiscoRfMib.Crfcfg()
        self.crfcfg.parent = self
        self.crfhistory = CiscoRfMib.Crfhistory()
        self.crfhistory.parent = self
        self.crfhistoryswitchovertable = CiscoRfMib.Crfhistoryswitchovertable()
        self.crfhistoryswitchovertable.parent = self
        self.crfstatus = CiscoRfMib.Crfstatus()
        self.crfstatus.parent = self
        self.crfstatusrfclienttable = CiscoRfMib.Crfstatusrfclienttable()
        self.crfstatusrfclienttable.parent = self
        self.crfstatusrfmodecapstable = CiscoRfMib.Crfstatusrfmodecapstable()
        self.crfstatusrfmodecapstable.parent = self


    class Crfstatus(object):
        """
        
        
        .. attribute:: crfstatusduplexmode
        
        	Indicates whether the redundant peer unit has been detected or not. If the redundant peer unit is detected, this object is true. If the redundant peer unit is not detected, this object is false
        	**type**\:  bool
        
        .. attribute:: crfstatusfailovertime
        
        	The value of sysUpTime when the primary redundant unit took over as active. The value of this object will be 0 till the first switchover
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfstatusissufromversion
        
        	The IOS version from with the user is upgrading
        	**type**\:  str
        
        .. attribute:: crfstatusissustate
        
        	The current ISSU state of the system
        	**type**\:   :py:class:`RfissustateEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfissustateEnum>`
        
        	**status**\: deprecated
        
        .. attribute:: crfstatusissustaterev1
        
        	The current ISSU state of the system
        	**type**\:   :py:class:`Rfissustaterev1Enum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfissustaterev1Enum>`
        
        .. attribute:: crfstatusissutoversion
        
        	The IOS version to with the user is upgrading
        	**type**\:  str
        
        .. attribute:: crfstatuslastswactreasoncode
        
        	The reason for the last switch of activity
        	**type**\:   :py:class:`RfswactreasontypeEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfswactreasontypeEnum>`
        
        .. attribute:: crfstatusmanualswactinhibit
        
        	Indicates whether a manual switch of activity is permitted. If a manual switch of activity is allowed, this object is false. If a manual switch of activity is not allowed, this object is true. Note that the value of this object is the inverse of the status of manual SWACTs.  This object does not indicate whether a switch of activity is or has occurred. This object only indicates if the user\-controllable capability is enabled or not.  A switch of activity is the event in which the standby redundant unit becomes active and the previously active unit becomes standby
        	**type**\:  bool
        
        .. attribute:: crfstatuspeerstandbyentrytime
        
        	The value of sysUpTime when the peer redundant unit entered the standbyHot state. The value will be 0 on system initialization
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfstatuspeerunitid
        
        	A unique identifier for the redundant peer unit. This identifier is implementation\-specific but the method for selecting the id must remain consistent throughout the redundant system.  Some example identifiers include\: slot id, physical or logical entity id, or a unique id assigned internally by the RF subsystem
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: crfstatuspeerunitstate
        
        	The current state of RF on the peer unit
        	**type**\:   :py:class:`RfstateEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfstateEnum>`
        
        .. attribute:: crfstatusprimarymode
        
        	Indicates whether this is the primary redundant unit or not. If this unit is the primary unit, this object is true. If this unit is the secondary unit, this object is false.  Note that the terms 'primary/secondary' are not synonymous with the terms 'active/standby'. At any given time, the primary unit may be the active unit, or the primary unit may be the standby unit. Likewise,   the secondary unit, at any given time, may be the active unit, or the secondary unit may be the standby unit.  The primary unit is given a higher priority or precedence over the secondary unit. In a race condition (usually at initialization time) or any situation where the redundant units are unable to successfully negotiate activity between themselves, the primary unit will always become the active unit and the secondary unit will fall back to standby. Only one redundant unit can be the primary unit at any given time.  The algorithm for determining the primary unit is system dependent, such as 'the redundant unit with the lower numeric unit id is always the primary unit.'
        	**type**\:  bool
        
        .. attribute:: crfstatusunitid
        
        	A unique identifier for this redundant unit. This identifier is implementation\-specific but the method for selecting the id must remain consistent throughout the redundant system.  Some example identifiers include\: slot id, physical or logical entity id, or a unique id assigned internally by the RF subsystem
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: crfstatusunitstate
        
        	The current state of RF on this unit
        	**type**\:   :py:class:`RfstateEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfstateEnum>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            self.parent = None
            self.crfstatusduplexmode = None
            self.crfstatusfailovertime = None
            self.crfstatusissufromversion = None
            self.crfstatusissustate = None
            self.crfstatusissustaterev1 = None
            self.crfstatusissutoversion = None
            self.crfstatuslastswactreasoncode = None
            self.crfstatusmanualswactinhibit = None
            self.crfstatuspeerstandbyentrytime = None
            self.crfstatuspeerunitid = None
            self.crfstatuspeerunitstate = None
            self.crfstatusprimarymode = None
            self.crfstatusunitid = None
            self.crfstatusunitstate = None

        @property
        def _common_path(self):

            return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFStatus'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crfstatusduplexmode is not None:
                return True

            if self.crfstatusfailovertime is not None:
                return True

            if self.crfstatusissufromversion is not None:
                return True

            if self.crfstatusissustate is not None:
                return True

            if self.crfstatusissustaterev1 is not None:
                return True

            if self.crfstatusissutoversion is not None:
                return True

            if self.crfstatuslastswactreasoncode is not None:
                return True

            if self.crfstatusmanualswactinhibit is not None:
                return True

            if self.crfstatuspeerstandbyentrytime is not None:
                return True

            if self.crfstatuspeerunitid is not None:
                return True

            if self.crfstatuspeerunitstate is not None:
                return True

            if self.crfstatusprimarymode is not None:
                return True

            if self.crfstatusunitid is not None:
                return True

            if self.crfstatusunitstate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
            return meta._meta_table['CiscoRfMib.Crfstatus']['meta_info']


    class Crfcfg(object):
        """
        
        
        .. attribute:: crfcfgadminaction
        
        	This variable is set to invoke RF subsystem action commands. The commands are useful for maintenance and software upgrade activities
        	**type**\:   :py:class:`RfactionEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfactionEnum>`
        
        .. attribute:: crfcfgkeepalivethresh
        
        	On platforms that support keep\-alives, the keep\-alive threshold value designates the number of lost keep\-alives tolerated before a failure condition is declared. If this occurs, a SWACT notification is sent.  On platforms that do not support keep\-alives, this object has no purpose or effect
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfcfgkeepalivethreshmax
        
        	The maximum acceptable value for the cRFCfgKeepaliveThresh object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfcfgkeepalivethreshmin
        
        	The minimum acceptable value for the cRFCfgKeepaliveThresh object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfcfgkeepalivetimer
        
        	On platforms that support keep\-alives, the keep\-alive timer value is used to guard against lost keep\-alives. The RF subsystem expects to receive a keep\-alive within this period. If a keep\-alive is not received within this time period, a SWACT notification is sent.  On platforms that do not support keep\-alives, this object has no purpose or effect
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgkeepalivetimermax
        
        	The maximum acceptable value for the cRFCfgKeepaliveTimer object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgkeepalivetimermin
        
        	The minimum acceptable value for the cRFCfgKeepaliveTimer object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgmaintenancemode
        
        	Indicates whether redundant units may communicate synchronization messages with each other. If communication is not permitted, this object is set to 'true'. If communication is permitted, this object is set to 'false'.  If the value of this object is 'true', the redundant system is considered to be in a maintenance mode of operation. If the value of this object is 'false', the redundant system is considered to be in a normal (non\-maintenance) mode of operation.  In maintenance mode (true), the active unit will not communicate with the standby unit. The standby unit progression will not occur. When maintenance mode is disabled (false), the standby unit is reset to recover.  Maintenance mode (true) is useful for maintenance\-type operations
        	**type**\:  bool
        
        .. attribute:: crfcfgnotifsenabled
        
        	Allows enabling/disabling of RF subsystem notifications
        	**type**\:  bool
        
        .. attribute:: crfcfgnotiftimer
        
        	Note that the term 'notification' here refers to an RF notification and not an SNMP notification.  As the standby unit progresses to the 'standbyHot' state, asynchronous messages are sent from the active unit to the standby unit which must then be acknowledged by the standby unit. If the active unit receives the acknowledgement during the time period specified by this object, progression proceeds as normal. If the timer expires and an acknowledgement was not received by the active unit, a switch of activity occurs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgnotiftimermax
        
        	The maximum acceptable value for the cRFCfgNotifTimer object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgnotiftimermin
        
        	The minimum acceptable value for the cRFCfgNotifTimer object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgredundancymode
        
        	Indicates the redundancy mode configured on the device
        	**type**\:   :py:class:`RfmodeEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfmodeEnum>`
        
        .. attribute:: crfcfgredundancymodedescr
        
        	Further clarifies or describes the redundancy mode indicated by cRFCfgRedundancyMode. Implementation\-specific terminology associated with the current redundancy mode may be presented here
        	**type**\:  str
        
        .. attribute:: crfcfgredundancyopermode
        
        	Indicate the operational redundancy mode of the device
        	**type**\:   :py:class:`RfmodeEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfmodeEnum>`
        
        .. attribute:: crfcfgsplitmode
        
        	Indicates whether redundant units may communicate synchronization messages with each other. If communication is not permitted, this object is set to true. If communication is permitted, this object is set to false.  In split mode (true), the active unit will not communicate with the standby unit. The standby unit progression will not occur. When split mode is disabled (false), the standby unit is reset to recover.  Split mode (true) is useful for maintenance operations
        	**type**\:  bool
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            self.parent = None
            self.crfcfgadminaction = None
            self.crfcfgkeepalivethresh = None
            self.crfcfgkeepalivethreshmax = None
            self.crfcfgkeepalivethreshmin = None
            self.crfcfgkeepalivetimer = None
            self.crfcfgkeepalivetimermax = None
            self.crfcfgkeepalivetimermin = None
            self.crfcfgmaintenancemode = None
            self.crfcfgnotifsenabled = None
            self.crfcfgnotiftimer = None
            self.crfcfgnotiftimermax = None
            self.crfcfgnotiftimermin = None
            self.crfcfgredundancymode = None
            self.crfcfgredundancymodedescr = None
            self.crfcfgredundancyopermode = None
            self.crfcfgsplitmode = None

        @property
        def _common_path(self):

            return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFCfg'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crfcfgadminaction is not None:
                return True

            if self.crfcfgkeepalivethresh is not None:
                return True

            if self.crfcfgkeepalivethreshmax is not None:
                return True

            if self.crfcfgkeepalivethreshmin is not None:
                return True

            if self.crfcfgkeepalivetimer is not None:
                return True

            if self.crfcfgkeepalivetimermax is not None:
                return True

            if self.crfcfgkeepalivetimermin is not None:
                return True

            if self.crfcfgmaintenancemode is not None:
                return True

            if self.crfcfgnotifsenabled is not None:
                return True

            if self.crfcfgnotiftimer is not None:
                return True

            if self.crfcfgnotiftimermax is not None:
                return True

            if self.crfcfgnotiftimermin is not None:
                return True

            if self.crfcfgredundancymode is not None:
                return True

            if self.crfcfgredundancymodedescr is not None:
                return True

            if self.crfcfgredundancyopermode is not None:
                return True

            if self.crfcfgsplitmode is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
            return meta._meta_table['CiscoRfMib.Crfcfg']['meta_info']


    class Crfhistory(object):
        """
        
        
        .. attribute:: crfhistorycoldstarts
        
        	Indicates the number of system cold starts. This includes the number of system cold starts due to switchover failure and the number of manual restarts
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfhistorystandbyavailtime
        
        	Indicates the cumulative time that a standby redundant unit has been available since last system initialization
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: crfhistorytablemaxlength
        
        	Maximum number of entries permissible in the history table. A value of 0 will result in no history being maintained
        	**type**\:  int
        
        	**range:** 0..50
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            self.parent = None
            self.crfhistorycoldstarts = None
            self.crfhistorystandbyavailtime = None
            self.crfhistorytablemaxlength = None

        @property
        def _common_path(self):

            return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crfhistorycoldstarts is not None:
                return True

            if self.crfhistorystandbyavailtime is not None:
                return True

            if self.crfhistorytablemaxlength is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
            return meta._meta_table['CiscoRfMib.Crfhistory']['meta_info']


    class Crfstatusrfmodecapstable(object):
        """
        This table containing a list of redundancy modes that can be
        supported on the device.
        
        .. attribute:: crfstatusrfmodecapsentry
        
        	An entry containing the device implementation specific terminology associated with the redundancy mode that can be supported on the device
        	**type**\: list of    :py:class:`Crfstatusrfmodecapsentry <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            self.parent = None
            self.crfstatusrfmodecapsentry = YList()
            self.crfstatusrfmodecapsentry.parent = self
            self.crfstatusrfmodecapsentry.name = 'crfstatusrfmodecapsentry'


        class Crfstatusrfmodecapsentry(object):
            """
            An entry containing the device implementation specific
            terminology associated with the redundancy mode that can be
            supported on the device.
            
            .. attribute:: crfstatusrfmodecapsmode  <key>
            
            	The redundancy mode that can be supported on the device
            	**type**\:   :py:class:`RfmodeEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfmodeEnum>`
            
            .. attribute:: crfstatusrfmodecapsmodedescr
            
            	The description of the device implementation specific terminology associated with its supported redundancy mode
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                self.parent = None
                self.crfstatusrfmodecapsmode = None
                self.crfstatusrfmodecapsmodedescr = None

            @property
            def _common_path(self):
                if self.crfstatusrfmodecapsmode is None:
                    raise YPYModelError('Key property crfstatusrfmodecapsmode is None')

                return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFStatusRFModeCapsTable/CISCO-RF-MIB:cRFStatusRFModeCapsEntry[CISCO-RF-MIB:cRFStatusRFModeCapsMode = ' + str(self.crfstatusrfmodecapsmode) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.crfstatusrfmodecapsmode is not None:
                    return True

                if self.crfstatusrfmodecapsmodedescr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
                return meta._meta_table['CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFStatusRFModeCapsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crfstatusrfmodecapsentry is not None:
                for child_ref in self.crfstatusrfmodecapsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
            return meta._meta_table['CiscoRfMib.Crfstatusrfmodecapstable']['meta_info']


    class Crfhistoryswitchovertable(object):
        """
        A table that tracks the history of all switchovers that
        have occurred since system initialization. The maximum
        number of entries permissible in this table is defined by
        cRFHistoryTableMaxLength. When the number of entries in
        the table reaches the maximum limit, the next entry
        would replace the oldest existing entry in the table.
        
        .. attribute:: crfhistoryswitchoverentry
        
        	The entries in this table contain the switchover information. Each entry in the table is indexed by cRFHistorySwitchOverIndex. The index wraps around to 1 after reaching the maximum value
        	**type**\: list of    :py:class:`Crfhistoryswitchoverentry <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            self.parent = None
            self.crfhistoryswitchoverentry = YList()
            self.crfhistoryswitchoverentry.parent = self
            self.crfhistoryswitchoverentry.name = 'crfhistoryswitchoverentry'


        class Crfhistoryswitchoverentry(object):
            """
            The entries in this table contain the switchover
            information. Each entry in the table is indexed by
            cRFHistorySwitchOverIndex. The index wraps around to 1
            after reaching the maximum value.
            
            .. attribute:: crfhistoryswitchoverindex  <key>
            
            	A monotonically increasing integer for the purpose of indexing history table. After reaching maximum value, it wraps around to 1
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: crfhistorycurractiveunitid
            
            	Indicates the secondary redundant unit that took over as active
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: crfhistoryprevactiveunitid
            
            	Indicates the primary redundant unit that went down
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: crfhistoryswacttime
            
            	Indicates the Date & Time when switchover occurred
            	**type**\:  str
            
            .. attribute:: crfhistoryswitchoverreason
            
            	Indicates the reason for the switchover
            	**type**\:   :py:class:`RfswactreasontypeEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfswactreasontypeEnum>`
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                self.parent = None
                self.crfhistoryswitchoverindex = None
                self.crfhistorycurractiveunitid = None
                self.crfhistoryprevactiveunitid = None
                self.crfhistoryswacttime = None
                self.crfhistoryswitchoverreason = None

            @property
            def _common_path(self):
                if self.crfhistoryswitchoverindex is None:
                    raise YPYModelError('Key property crfhistoryswitchoverindex is None')

                return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFHistorySwitchOverTable/CISCO-RF-MIB:cRFHistorySwitchOverEntry[CISCO-RF-MIB:cRFHistorySwitchOverIndex = ' + str(self.crfhistoryswitchoverindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.crfhistoryswitchoverindex is not None:
                    return True

                if self.crfhistorycurractiveunitid is not None:
                    return True

                if self.crfhistoryprevactiveunitid is not None:
                    return True

                if self.crfhistoryswacttime is not None:
                    return True

                if self.crfhistoryswitchoverreason is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
                return meta._meta_table['CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFHistorySwitchOverTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crfhistoryswitchoverentry is not None:
                for child_ref in self.crfhistoryswitchoverentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
            return meta._meta_table['CiscoRfMib.Crfhistoryswitchovertable']['meta_info']


    class Crfstatusrfclienttable(object):
        """
        This table contains a list of RF clients that are
        registered on the device. 
        
        RF clients are applications that have registered with 
        the Redundancy Facility (RF) to receive RF events and 
        notifications. The purpose of RF clients is to synchronize 
        any relevant data with the standby unit.
        
        .. attribute:: crfstatusrfcliententry
        
        	An entry containing information on various clients registered with the Redundancy Facility (RF). Entries in this table are always created by the system.  An entry is created in this table when a redundancy aware  application registers with the Redundancy Facility. The entry  is destroyed when that application deregisters from the  Redundancy Facility
        	**type**\: list of    :py:class:`Crfstatusrfcliententry <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            self.parent = None
            self.crfstatusrfcliententry = YList()
            self.crfstatusrfcliententry.parent = self
            self.crfstatusrfcliententry.name = 'crfstatusrfcliententry'


        class Crfstatusrfcliententry(object):
            """
            An entry containing information on various clients
            registered with the Redundancy Facility (RF). Entries in
            this table are always created by the system.
            
            An entry is created in this table when a redundancy aware 
            application registers with the Redundancy Facility. The entry 
            is destroyed when that application deregisters from the 
            Redundancy Facility.
            
            .. attribute:: crfstatusrfclientid  <key>
            
            	A unique identifier for the client which registered with the Redundancy Facility
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: crfstatusrfclientdescr
            
            	The description of the client which has registered with the Redundancy Facility
            	**type**\:  str
            
            .. attribute:: crfstatusrfclientredtime
            
            	Time taken for this client to become Redundant. This value is meaningful when the value of cRFStatusRFClientStatus is not 'noStatus'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: crfstatusrfclientseq
            
            	The sequence number of the client. The system assigns the sequence numbers based on the order of registration of the Redundancy Facility clients.  This is used for deciding order of RF events sent to clients
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: crfstatusrfclientstatus
            
            	This object provides the status of the Redundancy Facility client
            	**type**\:   :py:class:`RfclientstatusEnum <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RfclientstatusEnum>`
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                self.parent = None
                self.crfstatusrfclientid = None
                self.crfstatusrfclientdescr = None
                self.crfstatusrfclientredtime = None
                self.crfstatusrfclientseq = None
                self.crfstatusrfclientstatus = None

            @property
            def _common_path(self):
                if self.crfstatusrfclientid is None:
                    raise YPYModelError('Key property crfstatusrfclientid is None')

                return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFStatusRFClientTable/CISCO-RF-MIB:cRFStatusRFClientEntry[CISCO-RF-MIB:cRFStatusRFClientID = ' + str(self.crfstatusrfclientid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.crfstatusrfclientid is not None:
                    return True

                if self.crfstatusrfclientdescr is not None:
                    return True

                if self.crfstatusrfclientredtime is not None:
                    return True

                if self.crfstatusrfclientseq is not None:
                    return True

                if self.crfstatusrfclientstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
                return meta._meta_table['CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-RF-MIB:CISCO-RF-MIB/CISCO-RF-MIB:cRFStatusRFClientTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crfstatusrfcliententry is not None:
                for child_ref in self.crfstatusrfcliententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
            return meta._meta_table['CiscoRfMib.Crfstatusrfclienttable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-RF-MIB:CISCO-RF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.crfcfg is not None and self.crfcfg._has_data():
            return True

        if self.crfhistory is not None and self.crfhistory._has_data():
            return True

        if self.crfhistoryswitchovertable is not None and self.crfhistoryswitchovertable._has_data():
            return True

        if self.crfstatus is not None and self.crfstatus._has_data():
            return True

        if self.crfstatusrfclienttable is not None and self.crfstatusrfclienttable._has_data():
            return True

        if self.crfstatusrfmodecapstable is not None and self.crfstatusrfmodecapstable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_RF_MIB as meta
        return meta._meta_table['CiscoRfMib']['meta_info']


