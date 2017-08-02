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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Rfaction(Enum):
    """
    Rfaction

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

    noAction = Enum.YLeaf(0, "noAction")

    reloadPeer = Enum.YLeaf(1, "reloadPeer")

    reloadShelf = Enum.YLeaf(2, "reloadShelf")

    switchActivity = Enum.YLeaf(3, "switchActivity")

    forceSwitchActivity = Enum.YLeaf(4, "forceSwitchActivity")


class Rfclientstatus(Enum):
    """
    Rfclientstatus

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

    noStatus = Enum.YLeaf(1, "noStatus")

    clientNotRedundant = Enum.YLeaf(2, "clientNotRedundant")

    clientRedundancyInProgress = Enum.YLeaf(3, "clientRedundancyInProgress")

    clientRedundant = Enum.YLeaf(4, "clientRedundant")


class Rfissustate(Enum):
    """
    Rfissustate

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

    unset = Enum.YLeaf(0, "unset")

    init = Enum.YLeaf(1, "init")

    loadVersion = Enum.YLeaf(2, "loadVersion")

    runVersion = Enum.YLeaf(3, "runVersion")

    commitVersion = Enum.YLeaf(4, "commitVersion")


class Rfissustaterev1(Enum):
    """
    Rfissustaterev1

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

    init = Enum.YLeaf(0, "init")

    systemReset = Enum.YLeaf(1, "systemReset")

    loadVersion = Enum.YLeaf(3, "loadVersion")

    loadVersionSwitchover = Enum.YLeaf(4, "loadVersionSwitchover")

    runVersion = Enum.YLeaf(6, "runVersion")

    runVersionSwitchover = Enum.YLeaf(7, "runVersionSwitchover")

    commitVersion = Enum.YLeaf(9, "commitVersion")


class Rfmode(Enum):
    """
    Rfmode

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

    nonRedundant = Enum.YLeaf(1, "nonRedundant")

    staticLoadShareNonRedundant = Enum.YLeaf(2, "staticLoadShareNonRedundant")

    dynamicLoadShareNonRedundant = Enum.YLeaf(3, "dynamicLoadShareNonRedundant")

    staticLoadShareRedundant = Enum.YLeaf(4, "staticLoadShareRedundant")

    dynamicLoadShareRedundant = Enum.YLeaf(5, "dynamicLoadShareRedundant")

    coldStandbyRedundant = Enum.YLeaf(6, "coldStandbyRedundant")

    warmStandbyRedundant = Enum.YLeaf(7, "warmStandbyRedundant")

    hotStandbyRedundant = Enum.YLeaf(8, "hotStandbyRedundant")


class Rfstate(Enum):
    """
    Rfstate

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

    notKnown = Enum.YLeaf(1, "notKnown")

    disabled = Enum.YLeaf(2, "disabled")

    initialization = Enum.YLeaf(3, "initialization")

    negotiation = Enum.YLeaf(4, "negotiation")

    standbyCold = Enum.YLeaf(5, "standbyCold")

    standbyColdConfig = Enum.YLeaf(6, "standbyColdConfig")

    standbyColdFileSys = Enum.YLeaf(7, "standbyColdFileSys")

    standbyColdBulk = Enum.YLeaf(8, "standbyColdBulk")

    standbyHot = Enum.YLeaf(9, "standbyHot")

    activeFast = Enum.YLeaf(10, "activeFast")

    activeDrain = Enum.YLeaf(11, "activeDrain")

    activePreconfig = Enum.YLeaf(12, "activePreconfig")

    activePostconfig = Enum.YLeaf(13, "activePostconfig")

    active = Enum.YLeaf(14, "active")

    activeExtraload = Enum.YLeaf(15, "activeExtraload")

    activeHandback = Enum.YLeaf(16, "activeHandback")


class Rfswactreasontype(Enum):
    """
    Rfswactreasontype

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

    unsupported = Enum.YLeaf(1, "unsupported")

    none = Enum.YLeaf(2, "none")

    notKnown = Enum.YLeaf(3, "notKnown")

    userInitiated = Enum.YLeaf(4, "userInitiated")

    userForced = Enum.YLeaf(5, "userForced")

    activeUnitFailed = Enum.YLeaf(6, "activeUnitFailed")

    activeUnitRemoved = Enum.YLeaf(7, "activeUnitRemoved")



class CiscoRfMib(Entity):
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
        super(CiscoRfMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-RF-MIB"
        self.yang_parent_name = "CISCO-RF-MIB"

        self.crfcfg = CiscoRfMib.Crfcfg()
        self.crfcfg.parent = self
        self._children_name_map["crfcfg"] = "cRFCfg"
        self._children_yang_names.add("cRFCfg")

        self.crfhistory = CiscoRfMib.Crfhistory()
        self.crfhistory.parent = self
        self._children_name_map["crfhistory"] = "cRFHistory"
        self._children_yang_names.add("cRFHistory")

        self.crfhistoryswitchovertable = CiscoRfMib.Crfhistoryswitchovertable()
        self.crfhistoryswitchovertable.parent = self
        self._children_name_map["crfhistoryswitchovertable"] = "cRFHistorySwitchOverTable"
        self._children_yang_names.add("cRFHistorySwitchOverTable")

        self.crfstatus = CiscoRfMib.Crfstatus()
        self.crfstatus.parent = self
        self._children_name_map["crfstatus"] = "cRFStatus"
        self._children_yang_names.add("cRFStatus")

        self.crfstatusrfclienttable = CiscoRfMib.Crfstatusrfclienttable()
        self.crfstatusrfclienttable.parent = self
        self._children_name_map["crfstatusrfclienttable"] = "cRFStatusRFClientTable"
        self._children_yang_names.add("cRFStatusRFClientTable")

        self.crfstatusrfmodecapstable = CiscoRfMib.Crfstatusrfmodecapstable()
        self.crfstatusrfmodecapstable.parent = self
        self._children_name_map["crfstatusrfmodecapstable"] = "cRFStatusRFModeCapsTable"
        self._children_yang_names.add("cRFStatusRFModeCapsTable")


    class Crfstatus(Entity):
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
        	**type**\:   :py:class:`Rfissustate <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfissustate>`
        
        	**status**\: deprecated
        
        .. attribute:: crfstatusissustaterev1
        
        	The current ISSU state of the system
        	**type**\:   :py:class:`Rfissustaterev1 <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfissustaterev1>`
        
        .. attribute:: crfstatusissutoversion
        
        	The IOS version to with the user is upgrading
        	**type**\:  str
        
        .. attribute:: crfstatuslastswactreasoncode
        
        	The reason for the last switch of activity
        	**type**\:   :py:class:`Rfswactreasontype <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfswactreasontype>`
        
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
        	**type**\:   :py:class:`Rfstate <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfstate>`
        
        .. attribute:: crfstatusprimarymode
        
        	Indicates whether this is the primary redundant unit or not. If this unit is the primary unit, this object is true. If this unit is the secondary unit, this object is false.  Note that the terms 'primary/secondary' are not synonymous with the terms 'active/standby'. At any given time, the primary unit may be the active unit, or the primary unit may be the standby unit. Likewise,   the secondary unit, at any given time, may be the active unit, or the secondary unit may be the standby unit.  The primary unit is given a higher priority or precedence over the secondary unit. In a race condition (usually at initialization time) or any situation where the redundant units are unable to successfully negotiate activity between themselves, the primary unit will always become the active unit and the secondary unit will fall back to standby. Only one redundant unit can be the primary unit at any given time.  The algorithm for determining the primary unit is system dependent, such as 'the redundant unit with the lower numeric unit id is always the primary unit.'
        	**type**\:  bool
        
        .. attribute:: crfstatusunitid
        
        	A unique identifier for this redundant unit. This identifier is implementation\-specific but the method for selecting the id must remain consistent throughout the redundant system.  Some example identifiers include\: slot id, physical or logical entity id, or a unique id assigned internally by the RF subsystem
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: crfstatusunitstate
        
        	The current state of RF on this unit
        	**type**\:   :py:class:`Rfstate <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfstate>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CiscoRfMib.Crfstatus, self).__init__()

            self.yang_name = "cRFStatus"
            self.yang_parent_name = "CISCO-RF-MIB"

            self.crfstatusduplexmode = YLeaf(YType.boolean, "cRFStatusDuplexMode")

            self.crfstatusfailovertime = YLeaf(YType.uint32, "cRFStatusFailoverTime")

            self.crfstatusissufromversion = YLeaf(YType.str, "cRFStatusIssuFromVersion")

            self.crfstatusissustate = YLeaf(YType.enumeration, "cRFStatusIssuState")

            self.crfstatusissustaterev1 = YLeaf(YType.enumeration, "cRFStatusIssuStateRev1")

            self.crfstatusissutoversion = YLeaf(YType.str, "cRFStatusIssuToVersion")

            self.crfstatuslastswactreasoncode = YLeaf(YType.enumeration, "cRFStatusLastSwactReasonCode")

            self.crfstatusmanualswactinhibit = YLeaf(YType.boolean, "cRFStatusManualSwactInhibit")

            self.crfstatuspeerstandbyentrytime = YLeaf(YType.uint32, "cRFStatusPeerStandByEntryTime")

            self.crfstatuspeerunitid = YLeaf(YType.int32, "cRFStatusPeerUnitId")

            self.crfstatuspeerunitstate = YLeaf(YType.enumeration, "cRFStatusPeerUnitState")

            self.crfstatusprimarymode = YLeaf(YType.boolean, "cRFStatusPrimaryMode")

            self.crfstatusunitid = YLeaf(YType.int32, "cRFStatusUnitId")

            self.crfstatusunitstate = YLeaf(YType.enumeration, "cRFStatusUnitState")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("crfstatusduplexmode",
                            "crfstatusfailovertime",
                            "crfstatusissufromversion",
                            "crfstatusissustate",
                            "crfstatusissustaterev1",
                            "crfstatusissutoversion",
                            "crfstatuslastswactreasoncode",
                            "crfstatusmanualswactinhibit",
                            "crfstatuspeerstandbyentrytime",
                            "crfstatuspeerunitid",
                            "crfstatuspeerunitstate",
                            "crfstatusprimarymode",
                            "crfstatusunitid",
                            "crfstatusunitstate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRfMib.Crfstatus, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRfMib.Crfstatus, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.crfstatusduplexmode.is_set or
                self.crfstatusfailovertime.is_set or
                self.crfstatusissufromversion.is_set or
                self.crfstatusissustate.is_set or
                self.crfstatusissustaterev1.is_set or
                self.crfstatusissutoversion.is_set or
                self.crfstatuslastswactreasoncode.is_set or
                self.crfstatusmanualswactinhibit.is_set or
                self.crfstatuspeerstandbyentrytime.is_set or
                self.crfstatuspeerunitid.is_set or
                self.crfstatuspeerunitstate.is_set or
                self.crfstatusprimarymode.is_set or
                self.crfstatusunitid.is_set or
                self.crfstatusunitstate.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.crfstatusduplexmode.yfilter != YFilter.not_set or
                self.crfstatusfailovertime.yfilter != YFilter.not_set or
                self.crfstatusissufromversion.yfilter != YFilter.not_set or
                self.crfstatusissustate.yfilter != YFilter.not_set or
                self.crfstatusissustaterev1.yfilter != YFilter.not_set or
                self.crfstatusissutoversion.yfilter != YFilter.not_set or
                self.crfstatuslastswactreasoncode.yfilter != YFilter.not_set or
                self.crfstatusmanualswactinhibit.yfilter != YFilter.not_set or
                self.crfstatuspeerstandbyentrytime.yfilter != YFilter.not_set or
                self.crfstatuspeerunitid.yfilter != YFilter.not_set or
                self.crfstatuspeerunitstate.yfilter != YFilter.not_set or
                self.crfstatusprimarymode.yfilter != YFilter.not_set or
                self.crfstatusunitid.yfilter != YFilter.not_set or
                self.crfstatusunitstate.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cRFStatus" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.crfstatusduplexmode.is_set or self.crfstatusduplexmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusduplexmode.get_name_leafdata())
            if (self.crfstatusfailovertime.is_set or self.crfstatusfailovertime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusfailovertime.get_name_leafdata())
            if (self.crfstatusissufromversion.is_set or self.crfstatusissufromversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusissufromversion.get_name_leafdata())
            if (self.crfstatusissustate.is_set or self.crfstatusissustate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusissustate.get_name_leafdata())
            if (self.crfstatusissustaterev1.is_set or self.crfstatusissustaterev1.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusissustaterev1.get_name_leafdata())
            if (self.crfstatusissutoversion.is_set or self.crfstatusissutoversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusissutoversion.get_name_leafdata())
            if (self.crfstatuslastswactreasoncode.is_set or self.crfstatuslastswactreasoncode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatuslastswactreasoncode.get_name_leafdata())
            if (self.crfstatusmanualswactinhibit.is_set or self.crfstatusmanualswactinhibit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusmanualswactinhibit.get_name_leafdata())
            if (self.crfstatuspeerstandbyentrytime.is_set or self.crfstatuspeerstandbyentrytime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatuspeerstandbyentrytime.get_name_leafdata())
            if (self.crfstatuspeerunitid.is_set or self.crfstatuspeerunitid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatuspeerunitid.get_name_leafdata())
            if (self.crfstatuspeerunitstate.is_set or self.crfstatuspeerunitstate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatuspeerunitstate.get_name_leafdata())
            if (self.crfstatusprimarymode.is_set or self.crfstatusprimarymode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusprimarymode.get_name_leafdata())
            if (self.crfstatusunitid.is_set or self.crfstatusunitid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusunitid.get_name_leafdata())
            if (self.crfstatusunitstate.is_set or self.crfstatusunitstate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfstatusunitstate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cRFStatusDuplexMode" or name == "cRFStatusFailoverTime" or name == "cRFStatusIssuFromVersion" or name == "cRFStatusIssuState" or name == "cRFStatusIssuStateRev1" or name == "cRFStatusIssuToVersion" or name == "cRFStatusLastSwactReasonCode" or name == "cRFStatusManualSwactInhibit" or name == "cRFStatusPeerStandByEntryTime" or name == "cRFStatusPeerUnitId" or name == "cRFStatusPeerUnitState" or name == "cRFStatusPrimaryMode" or name == "cRFStatusUnitId" or name == "cRFStatusUnitState"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cRFStatusDuplexMode"):
                self.crfstatusduplexmode = value
                self.crfstatusduplexmode.value_namespace = name_space
                self.crfstatusduplexmode.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusFailoverTime"):
                self.crfstatusfailovertime = value
                self.crfstatusfailovertime.value_namespace = name_space
                self.crfstatusfailovertime.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusIssuFromVersion"):
                self.crfstatusissufromversion = value
                self.crfstatusissufromversion.value_namespace = name_space
                self.crfstatusissufromversion.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusIssuState"):
                self.crfstatusissustate = value
                self.crfstatusissustate.value_namespace = name_space
                self.crfstatusissustate.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusIssuStateRev1"):
                self.crfstatusissustaterev1 = value
                self.crfstatusissustaterev1.value_namespace = name_space
                self.crfstatusissustaterev1.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusIssuToVersion"):
                self.crfstatusissutoversion = value
                self.crfstatusissutoversion.value_namespace = name_space
                self.crfstatusissutoversion.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusLastSwactReasonCode"):
                self.crfstatuslastswactreasoncode = value
                self.crfstatuslastswactreasoncode.value_namespace = name_space
                self.crfstatuslastswactreasoncode.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusManualSwactInhibit"):
                self.crfstatusmanualswactinhibit = value
                self.crfstatusmanualswactinhibit.value_namespace = name_space
                self.crfstatusmanualswactinhibit.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusPeerStandByEntryTime"):
                self.crfstatuspeerstandbyentrytime = value
                self.crfstatuspeerstandbyentrytime.value_namespace = name_space
                self.crfstatuspeerstandbyentrytime.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusPeerUnitId"):
                self.crfstatuspeerunitid = value
                self.crfstatuspeerunitid.value_namespace = name_space
                self.crfstatuspeerunitid.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusPeerUnitState"):
                self.crfstatuspeerunitstate = value
                self.crfstatuspeerunitstate.value_namespace = name_space
                self.crfstatuspeerunitstate.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusPrimaryMode"):
                self.crfstatusprimarymode = value
                self.crfstatusprimarymode.value_namespace = name_space
                self.crfstatusprimarymode.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusUnitId"):
                self.crfstatusunitid = value
                self.crfstatusunitid.value_namespace = name_space
                self.crfstatusunitid.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFStatusUnitState"):
                self.crfstatusunitstate = value
                self.crfstatusunitstate.value_namespace = name_space
                self.crfstatusunitstate.value_namespace_prefix = name_space_prefix


    class Crfcfg(Entity):
        """
        
        
        .. attribute:: crfcfgadminaction
        
        	This variable is set to invoke RF subsystem action commands. The commands are useful for maintenance and software upgrade activities
        	**type**\:   :py:class:`Rfaction <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfaction>`
        
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
        	**type**\:   :py:class:`Rfmode <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfmode>`
        
        .. attribute:: crfcfgredundancymodedescr
        
        	Further clarifies or describes the redundancy mode indicated by cRFCfgRedundancyMode. Implementation\-specific terminology associated with the current redundancy mode may be presented here
        	**type**\:  str
        
        .. attribute:: crfcfgredundancyopermode
        
        	Indicate the operational redundancy mode of the device
        	**type**\:   :py:class:`Rfmode <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfmode>`
        
        .. attribute:: crfcfgsplitmode
        
        	Indicates whether redundant units may communicate synchronization messages with each other. If communication is not permitted, this object is set to true. If communication is permitted, this object is set to false.  In split mode (true), the active unit will not communicate with the standby unit. The standby unit progression will not occur. When split mode is disabled (false), the standby unit is reset to recover.  Split mode (true) is useful for maintenance operations
        	**type**\:  bool
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CiscoRfMib.Crfcfg, self).__init__()

            self.yang_name = "cRFCfg"
            self.yang_parent_name = "CISCO-RF-MIB"

            self.crfcfgadminaction = YLeaf(YType.enumeration, "cRFCfgAdminAction")

            self.crfcfgkeepalivethresh = YLeaf(YType.uint32, "cRFCfgKeepaliveThresh")

            self.crfcfgkeepalivethreshmax = YLeaf(YType.uint32, "cRFCfgKeepaliveThreshMax")

            self.crfcfgkeepalivethreshmin = YLeaf(YType.uint32, "cRFCfgKeepaliveThreshMin")

            self.crfcfgkeepalivetimer = YLeaf(YType.uint32, "cRFCfgKeepaliveTimer")

            self.crfcfgkeepalivetimermax = YLeaf(YType.uint32, "cRFCfgKeepaliveTimerMax")

            self.crfcfgkeepalivetimermin = YLeaf(YType.uint32, "cRFCfgKeepaliveTimerMin")

            self.crfcfgmaintenancemode = YLeaf(YType.boolean, "cRFCfgMaintenanceMode")

            self.crfcfgnotifsenabled = YLeaf(YType.boolean, "cRFCfgNotifsEnabled")

            self.crfcfgnotiftimer = YLeaf(YType.uint32, "cRFCfgNotifTimer")

            self.crfcfgnotiftimermax = YLeaf(YType.uint32, "cRFCfgNotifTimerMax")

            self.crfcfgnotiftimermin = YLeaf(YType.uint32, "cRFCfgNotifTimerMin")

            self.crfcfgredundancymode = YLeaf(YType.enumeration, "cRFCfgRedundancyMode")

            self.crfcfgredundancymodedescr = YLeaf(YType.str, "cRFCfgRedundancyModeDescr")

            self.crfcfgredundancyopermode = YLeaf(YType.enumeration, "cRFCfgRedundancyOperMode")

            self.crfcfgsplitmode = YLeaf(YType.boolean, "cRFCfgSplitMode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("crfcfgadminaction",
                            "crfcfgkeepalivethresh",
                            "crfcfgkeepalivethreshmax",
                            "crfcfgkeepalivethreshmin",
                            "crfcfgkeepalivetimer",
                            "crfcfgkeepalivetimermax",
                            "crfcfgkeepalivetimermin",
                            "crfcfgmaintenancemode",
                            "crfcfgnotifsenabled",
                            "crfcfgnotiftimer",
                            "crfcfgnotiftimermax",
                            "crfcfgnotiftimermin",
                            "crfcfgredundancymode",
                            "crfcfgredundancymodedescr",
                            "crfcfgredundancyopermode",
                            "crfcfgsplitmode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRfMib.Crfcfg, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRfMib.Crfcfg, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.crfcfgadminaction.is_set or
                self.crfcfgkeepalivethresh.is_set or
                self.crfcfgkeepalivethreshmax.is_set or
                self.crfcfgkeepalivethreshmin.is_set or
                self.crfcfgkeepalivetimer.is_set or
                self.crfcfgkeepalivetimermax.is_set or
                self.crfcfgkeepalivetimermin.is_set or
                self.crfcfgmaintenancemode.is_set or
                self.crfcfgnotifsenabled.is_set or
                self.crfcfgnotiftimer.is_set or
                self.crfcfgnotiftimermax.is_set or
                self.crfcfgnotiftimermin.is_set or
                self.crfcfgredundancymode.is_set or
                self.crfcfgredundancymodedescr.is_set or
                self.crfcfgredundancyopermode.is_set or
                self.crfcfgsplitmode.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.crfcfgadminaction.yfilter != YFilter.not_set or
                self.crfcfgkeepalivethresh.yfilter != YFilter.not_set or
                self.crfcfgkeepalivethreshmax.yfilter != YFilter.not_set or
                self.crfcfgkeepalivethreshmin.yfilter != YFilter.not_set or
                self.crfcfgkeepalivetimer.yfilter != YFilter.not_set or
                self.crfcfgkeepalivetimermax.yfilter != YFilter.not_set or
                self.crfcfgkeepalivetimermin.yfilter != YFilter.not_set or
                self.crfcfgmaintenancemode.yfilter != YFilter.not_set or
                self.crfcfgnotifsenabled.yfilter != YFilter.not_set or
                self.crfcfgnotiftimer.yfilter != YFilter.not_set or
                self.crfcfgnotiftimermax.yfilter != YFilter.not_set or
                self.crfcfgnotiftimermin.yfilter != YFilter.not_set or
                self.crfcfgredundancymode.yfilter != YFilter.not_set or
                self.crfcfgredundancymodedescr.yfilter != YFilter.not_set or
                self.crfcfgredundancyopermode.yfilter != YFilter.not_set or
                self.crfcfgsplitmode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cRFCfg" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.crfcfgadminaction.is_set or self.crfcfgadminaction.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgadminaction.get_name_leafdata())
            if (self.crfcfgkeepalivethresh.is_set or self.crfcfgkeepalivethresh.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgkeepalivethresh.get_name_leafdata())
            if (self.crfcfgkeepalivethreshmax.is_set or self.crfcfgkeepalivethreshmax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgkeepalivethreshmax.get_name_leafdata())
            if (self.crfcfgkeepalivethreshmin.is_set or self.crfcfgkeepalivethreshmin.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgkeepalivethreshmin.get_name_leafdata())
            if (self.crfcfgkeepalivetimer.is_set or self.crfcfgkeepalivetimer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgkeepalivetimer.get_name_leafdata())
            if (self.crfcfgkeepalivetimermax.is_set or self.crfcfgkeepalivetimermax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgkeepalivetimermax.get_name_leafdata())
            if (self.crfcfgkeepalivetimermin.is_set or self.crfcfgkeepalivetimermin.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgkeepalivetimermin.get_name_leafdata())
            if (self.crfcfgmaintenancemode.is_set or self.crfcfgmaintenancemode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgmaintenancemode.get_name_leafdata())
            if (self.crfcfgnotifsenabled.is_set or self.crfcfgnotifsenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgnotifsenabled.get_name_leafdata())
            if (self.crfcfgnotiftimer.is_set or self.crfcfgnotiftimer.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgnotiftimer.get_name_leafdata())
            if (self.crfcfgnotiftimermax.is_set or self.crfcfgnotiftimermax.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgnotiftimermax.get_name_leafdata())
            if (self.crfcfgnotiftimermin.is_set or self.crfcfgnotiftimermin.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgnotiftimermin.get_name_leafdata())
            if (self.crfcfgredundancymode.is_set or self.crfcfgredundancymode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgredundancymode.get_name_leafdata())
            if (self.crfcfgredundancymodedescr.is_set or self.crfcfgredundancymodedescr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgredundancymodedescr.get_name_leafdata())
            if (self.crfcfgredundancyopermode.is_set or self.crfcfgredundancyopermode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgredundancyopermode.get_name_leafdata())
            if (self.crfcfgsplitmode.is_set or self.crfcfgsplitmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfcfgsplitmode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cRFCfgAdminAction" or name == "cRFCfgKeepaliveThresh" or name == "cRFCfgKeepaliveThreshMax" or name == "cRFCfgKeepaliveThreshMin" or name == "cRFCfgKeepaliveTimer" or name == "cRFCfgKeepaliveTimerMax" or name == "cRFCfgKeepaliveTimerMin" or name == "cRFCfgMaintenanceMode" or name == "cRFCfgNotifsEnabled" or name == "cRFCfgNotifTimer" or name == "cRFCfgNotifTimerMax" or name == "cRFCfgNotifTimerMin" or name == "cRFCfgRedundancyMode" or name == "cRFCfgRedundancyModeDescr" or name == "cRFCfgRedundancyOperMode" or name == "cRFCfgSplitMode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cRFCfgAdminAction"):
                self.crfcfgadminaction = value
                self.crfcfgadminaction.value_namespace = name_space
                self.crfcfgadminaction.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgKeepaliveThresh"):
                self.crfcfgkeepalivethresh = value
                self.crfcfgkeepalivethresh.value_namespace = name_space
                self.crfcfgkeepalivethresh.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgKeepaliveThreshMax"):
                self.crfcfgkeepalivethreshmax = value
                self.crfcfgkeepalivethreshmax.value_namespace = name_space
                self.crfcfgkeepalivethreshmax.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgKeepaliveThreshMin"):
                self.crfcfgkeepalivethreshmin = value
                self.crfcfgkeepalivethreshmin.value_namespace = name_space
                self.crfcfgkeepalivethreshmin.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgKeepaliveTimer"):
                self.crfcfgkeepalivetimer = value
                self.crfcfgkeepalivetimer.value_namespace = name_space
                self.crfcfgkeepalivetimer.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgKeepaliveTimerMax"):
                self.crfcfgkeepalivetimermax = value
                self.crfcfgkeepalivetimermax.value_namespace = name_space
                self.crfcfgkeepalivetimermax.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgKeepaliveTimerMin"):
                self.crfcfgkeepalivetimermin = value
                self.crfcfgkeepalivetimermin.value_namespace = name_space
                self.crfcfgkeepalivetimermin.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgMaintenanceMode"):
                self.crfcfgmaintenancemode = value
                self.crfcfgmaintenancemode.value_namespace = name_space
                self.crfcfgmaintenancemode.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgNotifsEnabled"):
                self.crfcfgnotifsenabled = value
                self.crfcfgnotifsenabled.value_namespace = name_space
                self.crfcfgnotifsenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgNotifTimer"):
                self.crfcfgnotiftimer = value
                self.crfcfgnotiftimer.value_namespace = name_space
                self.crfcfgnotiftimer.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgNotifTimerMax"):
                self.crfcfgnotiftimermax = value
                self.crfcfgnotiftimermax.value_namespace = name_space
                self.crfcfgnotiftimermax.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgNotifTimerMin"):
                self.crfcfgnotiftimermin = value
                self.crfcfgnotiftimermin.value_namespace = name_space
                self.crfcfgnotiftimermin.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgRedundancyMode"):
                self.crfcfgredundancymode = value
                self.crfcfgredundancymode.value_namespace = name_space
                self.crfcfgredundancymode.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgRedundancyModeDescr"):
                self.crfcfgredundancymodedescr = value
                self.crfcfgredundancymodedescr.value_namespace = name_space
                self.crfcfgredundancymodedescr.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgRedundancyOperMode"):
                self.crfcfgredundancyopermode = value
                self.crfcfgredundancyopermode.value_namespace = name_space
                self.crfcfgredundancyopermode.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFCfgSplitMode"):
                self.crfcfgsplitmode = value
                self.crfcfgsplitmode.value_namespace = name_space
                self.crfcfgsplitmode.value_namespace_prefix = name_space_prefix


    class Crfhistory(Entity):
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
            super(CiscoRfMib.Crfhistory, self).__init__()

            self.yang_name = "cRFHistory"
            self.yang_parent_name = "CISCO-RF-MIB"

            self.crfhistorycoldstarts = YLeaf(YType.uint32, "cRFHistoryColdStarts")

            self.crfhistorystandbyavailtime = YLeaf(YType.int32, "cRFHistoryStandByAvailTime")

            self.crfhistorytablemaxlength = YLeaf(YType.uint32, "cRFHistoryTableMaxLength")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("crfhistorycoldstarts",
                            "crfhistorystandbyavailtime",
                            "crfhistorytablemaxlength") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoRfMib.Crfhistory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRfMib.Crfhistory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.crfhistorycoldstarts.is_set or
                self.crfhistorystandbyavailtime.is_set or
                self.crfhistorytablemaxlength.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.crfhistorycoldstarts.yfilter != YFilter.not_set or
                self.crfhistorystandbyavailtime.yfilter != YFilter.not_set or
                self.crfhistorytablemaxlength.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cRFHistory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.crfhistorycoldstarts.is_set or self.crfhistorycoldstarts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfhistorycoldstarts.get_name_leafdata())
            if (self.crfhistorystandbyavailtime.is_set or self.crfhistorystandbyavailtime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfhistorystandbyavailtime.get_name_leafdata())
            if (self.crfhistorytablemaxlength.is_set or self.crfhistorytablemaxlength.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crfhistorytablemaxlength.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cRFHistoryColdStarts" or name == "cRFHistoryStandByAvailTime" or name == "cRFHistoryTableMaxLength"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cRFHistoryColdStarts"):
                self.crfhistorycoldstarts = value
                self.crfhistorycoldstarts.value_namespace = name_space
                self.crfhistorycoldstarts.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFHistoryStandByAvailTime"):
                self.crfhistorystandbyavailtime = value
                self.crfhistorystandbyavailtime.value_namespace = name_space
                self.crfhistorystandbyavailtime.value_namespace_prefix = name_space_prefix
            if(value_path == "cRFHistoryTableMaxLength"):
                self.crfhistorytablemaxlength = value
                self.crfhistorytablemaxlength.value_namespace = name_space
                self.crfhistorytablemaxlength.value_namespace_prefix = name_space_prefix


    class Crfstatusrfmodecapstable(Entity):
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
            super(CiscoRfMib.Crfstatusrfmodecapstable, self).__init__()

            self.yang_name = "cRFStatusRFModeCapsTable"
            self.yang_parent_name = "CISCO-RF-MIB"

            self.crfstatusrfmodecapsentry = YList(self)

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
                        super(CiscoRfMib.Crfstatusrfmodecapstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRfMib.Crfstatusrfmodecapstable, self).__setattr__(name, value)


        class Crfstatusrfmodecapsentry(Entity):
            """
            An entry containing the device implementation specific
            terminology associated with the redundancy mode that can be
            supported on the device.
            
            .. attribute:: crfstatusrfmodecapsmode  <key>
            
            	The redundancy mode that can be supported on the device
            	**type**\:   :py:class:`Rfmode <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfmode>`
            
            .. attribute:: crfstatusrfmodecapsmodedescr
            
            	The description of the device implementation specific terminology associated with its supported redundancy mode
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                super(CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry, self).__init__()

                self.yang_name = "cRFStatusRFModeCapsEntry"
                self.yang_parent_name = "cRFStatusRFModeCapsTable"

                self.crfstatusrfmodecapsmode = YLeaf(YType.enumeration, "cRFStatusRFModeCapsMode")

                self.crfstatusrfmodecapsmodedescr = YLeaf(YType.str, "cRFStatusRFModeCapsModeDescr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("crfstatusrfmodecapsmode",
                                "crfstatusrfmodecapsmodedescr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.crfstatusrfmodecapsmode.is_set or
                    self.crfstatusrfmodecapsmodedescr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.crfstatusrfmodecapsmode.yfilter != YFilter.not_set or
                    self.crfstatusrfmodecapsmodedescr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cRFStatusRFModeCapsEntry" + "[cRFStatusRFModeCapsMode='" + self.crfstatusrfmodecapsmode.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/cRFStatusRFModeCapsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.crfstatusrfmodecapsmode.is_set or self.crfstatusrfmodecapsmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfmodecapsmode.get_name_leafdata())
                if (self.crfstatusrfmodecapsmodedescr.is_set or self.crfstatusrfmodecapsmodedescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfmodecapsmodedescr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cRFStatusRFModeCapsMode" or name == "cRFStatusRFModeCapsModeDescr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cRFStatusRFModeCapsMode"):
                    self.crfstatusrfmodecapsmode = value
                    self.crfstatusrfmodecapsmode.value_namespace = name_space
                    self.crfstatusrfmodecapsmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFStatusRFModeCapsModeDescr"):
                    self.crfstatusrfmodecapsmodedescr = value
                    self.crfstatusrfmodecapsmodedescr.value_namespace = name_space
                    self.crfstatusrfmodecapsmodedescr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.crfstatusrfmodecapsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.crfstatusrfmodecapsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cRFStatusRFModeCapsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cRFStatusRFModeCapsEntry"):
                for c in self.crfstatusrfmodecapsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.crfstatusrfmodecapsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cRFStatusRFModeCapsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Crfhistoryswitchovertable(Entity):
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
            super(CiscoRfMib.Crfhistoryswitchovertable, self).__init__()

            self.yang_name = "cRFHistorySwitchOverTable"
            self.yang_parent_name = "CISCO-RF-MIB"

            self.crfhistoryswitchoverentry = YList(self)

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
                        super(CiscoRfMib.Crfhistoryswitchovertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRfMib.Crfhistoryswitchovertable, self).__setattr__(name, value)


        class Crfhistoryswitchoverentry(Entity):
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
            	**type**\:   :py:class:`Rfswactreasontype <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfswactreasontype>`
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                super(CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry, self).__init__()

                self.yang_name = "cRFHistorySwitchOverEntry"
                self.yang_parent_name = "cRFHistorySwitchOverTable"

                self.crfhistoryswitchoverindex = YLeaf(YType.uint32, "cRFHistorySwitchOverIndex")

                self.crfhistorycurractiveunitid = YLeaf(YType.int32, "cRFHistoryCurrActiveUnitId")

                self.crfhistoryprevactiveunitid = YLeaf(YType.int32, "cRFHistoryPrevActiveUnitId")

                self.crfhistoryswacttime = YLeaf(YType.str, "cRFHistorySwactTime")

                self.crfhistoryswitchoverreason = YLeaf(YType.enumeration, "cRFHistorySwitchOverReason")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("crfhistoryswitchoverindex",
                                "crfhistorycurractiveunitid",
                                "crfhistoryprevactiveunitid",
                                "crfhistoryswacttime",
                                "crfhistoryswitchoverreason") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.crfhistoryswitchoverindex.is_set or
                    self.crfhistorycurractiveunitid.is_set or
                    self.crfhistoryprevactiveunitid.is_set or
                    self.crfhistoryswacttime.is_set or
                    self.crfhistoryswitchoverreason.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.crfhistoryswitchoverindex.yfilter != YFilter.not_set or
                    self.crfhistorycurractiveunitid.yfilter != YFilter.not_set or
                    self.crfhistoryprevactiveunitid.yfilter != YFilter.not_set or
                    self.crfhistoryswacttime.yfilter != YFilter.not_set or
                    self.crfhistoryswitchoverreason.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cRFHistorySwitchOverEntry" + "[cRFHistorySwitchOverIndex='" + self.crfhistoryswitchoverindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/cRFHistorySwitchOverTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.crfhistoryswitchoverindex.is_set or self.crfhistoryswitchoverindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfhistoryswitchoverindex.get_name_leafdata())
                if (self.crfhistorycurractiveunitid.is_set or self.crfhistorycurractiveunitid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfhistorycurractiveunitid.get_name_leafdata())
                if (self.crfhistoryprevactiveunitid.is_set or self.crfhistoryprevactiveunitid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfhistoryprevactiveunitid.get_name_leafdata())
                if (self.crfhistoryswacttime.is_set or self.crfhistoryswacttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfhistoryswacttime.get_name_leafdata())
                if (self.crfhistoryswitchoverreason.is_set or self.crfhistoryswitchoverreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfhistoryswitchoverreason.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cRFHistorySwitchOverIndex" or name == "cRFHistoryCurrActiveUnitId" or name == "cRFHistoryPrevActiveUnitId" or name == "cRFHistorySwactTime" or name == "cRFHistorySwitchOverReason"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cRFHistorySwitchOverIndex"):
                    self.crfhistoryswitchoverindex = value
                    self.crfhistoryswitchoverindex.value_namespace = name_space
                    self.crfhistoryswitchoverindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFHistoryCurrActiveUnitId"):
                    self.crfhistorycurractiveunitid = value
                    self.crfhistorycurractiveunitid.value_namespace = name_space
                    self.crfhistorycurractiveunitid.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFHistoryPrevActiveUnitId"):
                    self.crfhistoryprevactiveunitid = value
                    self.crfhistoryprevactiveunitid.value_namespace = name_space
                    self.crfhistoryprevactiveunitid.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFHistorySwactTime"):
                    self.crfhistoryswacttime = value
                    self.crfhistoryswacttime.value_namespace = name_space
                    self.crfhistoryswacttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFHistorySwitchOverReason"):
                    self.crfhistoryswitchoverreason = value
                    self.crfhistoryswitchoverreason.value_namespace = name_space
                    self.crfhistoryswitchoverreason.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.crfhistoryswitchoverentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.crfhistoryswitchoverentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cRFHistorySwitchOverTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cRFHistorySwitchOverEntry"):
                for c in self.crfhistoryswitchoverentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.crfhistoryswitchoverentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cRFHistorySwitchOverEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Crfstatusrfclienttable(Entity):
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
            super(CiscoRfMib.Crfstatusrfclienttable, self).__init__()

            self.yang_name = "cRFStatusRFClientTable"
            self.yang_parent_name = "CISCO-RF-MIB"

            self.crfstatusrfcliententry = YList(self)

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
                        super(CiscoRfMib.Crfstatusrfclienttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoRfMib.Crfstatusrfclienttable, self).__setattr__(name, value)


        class Crfstatusrfcliententry(Entity):
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
            	**type**\:   :py:class:`Rfclientstatus <ydk.models.cisco_ios_xe.CISCO_RF_MIB.Rfclientstatus>`
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                super(CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry, self).__init__()

                self.yang_name = "cRFStatusRFClientEntry"
                self.yang_parent_name = "cRFStatusRFClientTable"

                self.crfstatusrfclientid = YLeaf(YType.uint32, "cRFStatusRFClientID")

                self.crfstatusrfclientdescr = YLeaf(YType.str, "cRFStatusRFClientDescr")

                self.crfstatusrfclientredtime = YLeaf(YType.uint32, "cRFStatusRFClientRedTime")

                self.crfstatusrfclientseq = YLeaf(YType.uint32, "cRFStatusRFClientSeq")

                self.crfstatusrfclientstatus = YLeaf(YType.enumeration, "cRFStatusRFClientStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("crfstatusrfclientid",
                                "crfstatusrfclientdescr",
                                "crfstatusrfclientredtime",
                                "crfstatusrfclientseq",
                                "crfstatusrfclientstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.crfstatusrfclientid.is_set or
                    self.crfstatusrfclientdescr.is_set or
                    self.crfstatusrfclientredtime.is_set or
                    self.crfstatusrfclientseq.is_set or
                    self.crfstatusrfclientstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.crfstatusrfclientid.yfilter != YFilter.not_set or
                    self.crfstatusrfclientdescr.yfilter != YFilter.not_set or
                    self.crfstatusrfclientredtime.yfilter != YFilter.not_set or
                    self.crfstatusrfclientseq.yfilter != YFilter.not_set or
                    self.crfstatusrfclientstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cRFStatusRFClientEntry" + "[cRFStatusRFClientID='" + self.crfstatusrfclientid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/cRFStatusRFClientTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.crfstatusrfclientid.is_set or self.crfstatusrfclientid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfclientid.get_name_leafdata())
                if (self.crfstatusrfclientdescr.is_set or self.crfstatusrfclientdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfclientdescr.get_name_leafdata())
                if (self.crfstatusrfclientredtime.is_set or self.crfstatusrfclientredtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfclientredtime.get_name_leafdata())
                if (self.crfstatusrfclientseq.is_set or self.crfstatusrfclientseq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfclientseq.get_name_leafdata())
                if (self.crfstatusrfclientstatus.is_set or self.crfstatusrfclientstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crfstatusrfclientstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cRFStatusRFClientID" or name == "cRFStatusRFClientDescr" or name == "cRFStatusRFClientRedTime" or name == "cRFStatusRFClientSeq" or name == "cRFStatusRFClientStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cRFStatusRFClientID"):
                    self.crfstatusrfclientid = value
                    self.crfstatusrfclientid.value_namespace = name_space
                    self.crfstatusrfclientid.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFStatusRFClientDescr"):
                    self.crfstatusrfclientdescr = value
                    self.crfstatusrfclientdescr.value_namespace = name_space
                    self.crfstatusrfclientdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFStatusRFClientRedTime"):
                    self.crfstatusrfclientredtime = value
                    self.crfstatusrfclientredtime.value_namespace = name_space
                    self.crfstatusrfclientredtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFStatusRFClientSeq"):
                    self.crfstatusrfclientseq = value
                    self.crfstatusrfclientseq.value_namespace = name_space
                    self.crfstatusrfclientseq.value_namespace_prefix = name_space_prefix
                if(value_path == "cRFStatusRFClientStatus"):
                    self.crfstatusrfclientstatus = value
                    self.crfstatusrfclientstatus.value_namespace = name_space
                    self.crfstatusrfclientstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.crfstatusrfcliententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.crfstatusrfcliententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cRFStatusRFClientTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cRFStatusRFClientEntry"):
                for c in self.crfstatusrfcliententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.crfstatusrfcliententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cRFStatusRFClientEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.crfcfg is not None and self.crfcfg.has_data()) or
            (self.crfhistory is not None and self.crfhistory.has_data()) or
            (self.crfhistoryswitchovertable is not None and self.crfhistoryswitchovertable.has_data()) or
            (self.crfstatus is not None and self.crfstatus.has_data()) or
            (self.crfstatusrfclienttable is not None and self.crfstatusrfclienttable.has_data()) or
            (self.crfstatusrfmodecapstable is not None and self.crfstatusrfmodecapstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.crfcfg is not None and self.crfcfg.has_operation()) or
            (self.crfhistory is not None and self.crfhistory.has_operation()) or
            (self.crfhistoryswitchovertable is not None and self.crfhistoryswitchovertable.has_operation()) or
            (self.crfstatus is not None and self.crfstatus.has_operation()) or
            (self.crfstatusrfclienttable is not None and self.crfstatusrfclienttable.has_operation()) or
            (self.crfstatusrfmodecapstable is not None and self.crfstatusrfmodecapstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-RF-MIB:CISCO-RF-MIB" + path_buffer

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

        if (child_yang_name == "cRFCfg"):
            if (self.crfcfg is None):
                self.crfcfg = CiscoRfMib.Crfcfg()
                self.crfcfg.parent = self
                self._children_name_map["crfcfg"] = "cRFCfg"
            return self.crfcfg

        if (child_yang_name == "cRFHistory"):
            if (self.crfhistory is None):
                self.crfhistory = CiscoRfMib.Crfhistory()
                self.crfhistory.parent = self
                self._children_name_map["crfhistory"] = "cRFHistory"
            return self.crfhistory

        if (child_yang_name == "cRFHistorySwitchOverTable"):
            if (self.crfhistoryswitchovertable is None):
                self.crfhistoryswitchovertable = CiscoRfMib.Crfhistoryswitchovertable()
                self.crfhistoryswitchovertable.parent = self
                self._children_name_map["crfhistoryswitchovertable"] = "cRFHistorySwitchOverTable"
            return self.crfhistoryswitchovertable

        if (child_yang_name == "cRFStatus"):
            if (self.crfstatus is None):
                self.crfstatus = CiscoRfMib.Crfstatus()
                self.crfstatus.parent = self
                self._children_name_map["crfstatus"] = "cRFStatus"
            return self.crfstatus

        if (child_yang_name == "cRFStatusRFClientTable"):
            if (self.crfstatusrfclienttable is None):
                self.crfstatusrfclienttable = CiscoRfMib.Crfstatusrfclienttable()
                self.crfstatusrfclienttable.parent = self
                self._children_name_map["crfstatusrfclienttable"] = "cRFStatusRFClientTable"
            return self.crfstatusrfclienttable

        if (child_yang_name == "cRFStatusRFModeCapsTable"):
            if (self.crfstatusrfmodecapstable is None):
                self.crfstatusrfmodecapstable = CiscoRfMib.Crfstatusrfmodecapstable()
                self.crfstatusrfmodecapstable.parent = self
                self._children_name_map["crfstatusrfmodecapstable"] = "cRFStatusRFModeCapsTable"
            return self.crfstatusrfmodecapstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cRFCfg" or name == "cRFHistory" or name == "cRFHistorySwitchOverTable" or name == "cRFStatus" or name == "cRFStatusRFClientTable" or name == "cRFStatusRFModeCapsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoRfMib()
        return self._top_entity

