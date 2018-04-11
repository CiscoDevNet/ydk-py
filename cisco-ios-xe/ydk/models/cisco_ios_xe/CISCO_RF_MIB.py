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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class RFAction(Enum):
    """
    RFAction (Enum Class)

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


class RFClientStatus(Enum):
    """
    RFClientStatus (Enum Class)

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


class RFIssuState(Enum):
    """
    RFIssuState (Enum Class)

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


class RFIssuStateRev1(Enum):
    """
    RFIssuStateRev1 (Enum Class)

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


class RFMode(Enum):
    """
    RFMode (Enum Class)

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


class RFState(Enum):
    """
    RFState (Enum Class)

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


class RFSwactReasonType(Enum):
    """
    RFSwactReasonType (Enum Class)

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



class CISCORFMIB(Entity):
    """
    
    
    .. attribute:: crfstatus
    
    	
    	**type**\:  :py:class:`Crfstatus <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfstatus>`
    
    .. attribute:: crfcfg
    
    	
    	**type**\:  :py:class:`Crfcfg <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfcfg>`
    
    .. attribute:: crfhistory
    
    	
    	**type**\:  :py:class:`Crfhistory <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfhistory>`
    
    .. attribute:: crfstatusrfmodecapstable
    
    	This table containing a list of redundancy modes that can be supported on the device
    	**type**\:  :py:class:`Crfstatusrfmodecapstable <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfstatusrfmodecapstable>`
    
    .. attribute:: crfhistoryswitchovertable
    
    	A table that tracks the history of all switchovers that have occurred since system initialization. The maximum number of entries permissible in this table is defined by cRFHistoryTableMaxLength. When the number of entries in the table reaches the maximum limit, the next entry would replace the oldest existing entry in the table
    	**type**\:  :py:class:`Crfhistoryswitchovertable <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfhistoryswitchovertable>`
    
    .. attribute:: crfstatusrfclienttable
    
    	This table contains a list of RF clients that are registered on the device.   RF clients are applications that have registered with  the Redundancy Facility (RF) to receive RF events and  notifications. The purpose of RF clients is to synchronize  any relevant data with the standby unit
    	**type**\:  :py:class:`Crfstatusrfclienttable <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfstatusrfclienttable>`
    
    

    """

    _prefix = 'CISCO-RF-MIB'
    _revision = '2005-09-01'

    def __init__(self):
        super(CISCORFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-RF-MIB"
        self.yang_parent_name = "CISCO-RF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cRFStatus", ("crfstatus", CISCORFMIB.Crfstatus)), ("cRFCfg", ("crfcfg", CISCORFMIB.Crfcfg)), ("cRFHistory", ("crfhistory", CISCORFMIB.Crfhistory)), ("cRFStatusRFModeCapsTable", ("crfstatusrfmodecapstable", CISCORFMIB.Crfstatusrfmodecapstable)), ("cRFHistorySwitchOverTable", ("crfhistoryswitchovertable", CISCORFMIB.Crfhistoryswitchovertable)), ("cRFStatusRFClientTable", ("crfstatusrfclienttable", CISCORFMIB.Crfstatusrfclienttable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.crfstatus = CISCORFMIB.Crfstatus()
        self.crfstatus.parent = self
        self._children_name_map["crfstatus"] = "cRFStatus"
        self._children_yang_names.add("cRFStatus")

        self.crfcfg = CISCORFMIB.Crfcfg()
        self.crfcfg.parent = self
        self._children_name_map["crfcfg"] = "cRFCfg"
        self._children_yang_names.add("cRFCfg")

        self.crfhistory = CISCORFMIB.Crfhistory()
        self.crfhistory.parent = self
        self._children_name_map["crfhistory"] = "cRFHistory"
        self._children_yang_names.add("cRFHistory")

        self.crfstatusrfmodecapstable = CISCORFMIB.Crfstatusrfmodecapstable()
        self.crfstatusrfmodecapstable.parent = self
        self._children_name_map["crfstatusrfmodecapstable"] = "cRFStatusRFModeCapsTable"
        self._children_yang_names.add("cRFStatusRFModeCapsTable")

        self.crfhistoryswitchovertable = CISCORFMIB.Crfhistoryswitchovertable()
        self.crfhistoryswitchovertable.parent = self
        self._children_name_map["crfhistoryswitchovertable"] = "cRFHistorySwitchOverTable"
        self._children_yang_names.add("cRFHistorySwitchOverTable")

        self.crfstatusrfclienttable = CISCORFMIB.Crfstatusrfclienttable()
        self.crfstatusrfclienttable.parent = self
        self._children_name_map["crfstatusrfclienttable"] = "cRFStatusRFClientTable"
        self._children_yang_names.add("cRFStatusRFClientTable")
        self._segment_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB"


    class Crfstatus(Entity):
        """
        
        
        .. attribute:: crfstatusunitid
        
        	A unique identifier for this redundant unit. This identifier is implementation\-specific but the method for selecting the id must remain consistent throughout the redundant system.  Some example identifiers include\: slot id, physical or logical entity id, or a unique id assigned internally by the RF subsystem
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: crfstatusunitstate
        
        	The current state of RF on this unit
        	**type**\:  :py:class:`RFState <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFState>`
        
        .. attribute:: crfstatuspeerunitid
        
        	A unique identifier for the redundant peer unit. This identifier is implementation\-specific but the method for selecting the id must remain consistent throughout the redundant system.  Some example identifiers include\: slot id, physical or logical entity id, or a unique id assigned internally by the RF subsystem
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: crfstatuspeerunitstate
        
        	The current state of RF on the peer unit
        	**type**\:  :py:class:`RFState <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFState>`
        
        .. attribute:: crfstatusprimarymode
        
        	Indicates whether this is the primary redundant unit or not. If this unit is the primary unit, this object is true. If this unit is the secondary unit, this object is false.  Note that the terms 'primary/secondary' are not synonymous with the terms 'active/standby'. At any given time, the primary unit may be the active unit, or the primary unit may be the standby unit. Likewise,   the secondary unit, at any given time, may be the active unit, or the secondary unit may be the standby unit.  The primary unit is given a higher priority or precedence over the secondary unit. In a race condition (usually at initialization time) or any situation where the redundant units are unable to successfully negotiate activity between themselves, the primary unit will always become the active unit and the secondary unit will fall back to standby. Only one redundant unit can be the primary unit at any given time.  The algorithm for determining the primary unit is system dependent, such as 'the redundant unit with the lower numeric unit id is always the primary unit.'
        	**type**\: bool
        
        .. attribute:: crfstatusduplexmode
        
        	Indicates whether the redundant peer unit has been detected or not. If the redundant peer unit is detected, this object is true. If the redundant peer unit is not detected, this object is false
        	**type**\: bool
        
        .. attribute:: crfstatusmanualswactinhibit
        
        	Indicates whether a manual switch of activity is permitted. If a manual switch of activity is allowed, this object is false. If a manual switch of activity is not allowed, this object is true. Note that the value of this object is the inverse of the status of manual SWACTs.  This object does not indicate whether a switch of activity is or has occurred. This object only indicates if the user\-controllable capability is enabled or not.  A switch of activity is the event in which the standby redundant unit becomes active and the previously active unit becomes standby
        	**type**\: bool
        
        .. attribute:: crfstatuslastswactreasoncode
        
        	The reason for the last switch of activity
        	**type**\:  :py:class:`RFSwactReasonType <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFSwactReasonType>`
        
        .. attribute:: crfstatusfailovertime
        
        	The value of sysUpTime when the primary redundant unit took over as active. The value of this object will be 0 till the first switchover
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfstatuspeerstandbyentrytime
        
        	The value of sysUpTime when the peer redundant unit entered the standbyHot state. The value will be 0 on system initialization
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfstatusissustate
        
        	The current ISSU state of the system
        	**type**\:  :py:class:`RFIssuState <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFIssuState>`
        
        	**status**\: deprecated
        
        .. attribute:: crfstatusissustaterev1
        
        	The current ISSU state of the system
        	**type**\:  :py:class:`RFIssuStateRev1 <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFIssuStateRev1>`
        
        .. attribute:: crfstatusissufromversion
        
        	The IOS version from with the user is upgrading
        	**type**\: str
        
        .. attribute:: crfstatusissutoversion
        
        	The IOS version to with the user is upgrading
        	**type**\: str
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CISCORFMIB.Crfstatus, self).__init__()

            self.yang_name = "cRFStatus"
            self.yang_parent_name = "CISCO-RF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('crfstatusunitid', YLeaf(YType.int32, 'cRFStatusUnitId')),
                ('crfstatusunitstate', YLeaf(YType.enumeration, 'cRFStatusUnitState')),
                ('crfstatuspeerunitid', YLeaf(YType.int32, 'cRFStatusPeerUnitId')),
                ('crfstatuspeerunitstate', YLeaf(YType.enumeration, 'cRFStatusPeerUnitState')),
                ('crfstatusprimarymode', YLeaf(YType.boolean, 'cRFStatusPrimaryMode')),
                ('crfstatusduplexmode', YLeaf(YType.boolean, 'cRFStatusDuplexMode')),
                ('crfstatusmanualswactinhibit', YLeaf(YType.boolean, 'cRFStatusManualSwactInhibit')),
                ('crfstatuslastswactreasoncode', YLeaf(YType.enumeration, 'cRFStatusLastSwactReasonCode')),
                ('crfstatusfailovertime', YLeaf(YType.uint32, 'cRFStatusFailoverTime')),
                ('crfstatuspeerstandbyentrytime', YLeaf(YType.uint32, 'cRFStatusPeerStandByEntryTime')),
                ('crfstatusissustate', YLeaf(YType.enumeration, 'cRFStatusIssuState')),
                ('crfstatusissustaterev1', YLeaf(YType.enumeration, 'cRFStatusIssuStateRev1')),
                ('crfstatusissufromversion', YLeaf(YType.str, 'cRFStatusIssuFromVersion')),
                ('crfstatusissutoversion', YLeaf(YType.str, 'cRFStatusIssuToVersion')),
            ])
            self.crfstatusunitid = None
            self.crfstatusunitstate = None
            self.crfstatuspeerunitid = None
            self.crfstatuspeerunitstate = None
            self.crfstatusprimarymode = None
            self.crfstatusduplexmode = None
            self.crfstatusmanualswactinhibit = None
            self.crfstatuslastswactreasoncode = None
            self.crfstatusfailovertime = None
            self.crfstatuspeerstandbyentrytime = None
            self.crfstatusissustate = None
            self.crfstatusissustaterev1 = None
            self.crfstatusissufromversion = None
            self.crfstatusissutoversion = None
            self._segment_path = lambda: "cRFStatus"
            self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORFMIB.Crfstatus, ['crfstatusunitid', 'crfstatusunitstate', 'crfstatuspeerunitid', 'crfstatuspeerunitstate', 'crfstatusprimarymode', 'crfstatusduplexmode', 'crfstatusmanualswactinhibit', 'crfstatuslastswactreasoncode', 'crfstatusfailovertime', 'crfstatuspeerstandbyentrytime', 'crfstatusissustate', 'crfstatusissustaterev1', 'crfstatusissufromversion', 'crfstatusissutoversion'], name, value)


    class Crfcfg(Entity):
        """
        
        
        .. attribute:: crfcfgsplitmode
        
        	Indicates whether redundant units may communicate synchronization messages with each other. If communication is not permitted, this object is set to true. If communication is permitted, this object is set to false.  In split mode (true), the active unit will not communicate with the standby unit. The standby unit progression will not occur. When split mode is disabled (false), the standby unit is reset to recover.  Split mode (true) is useful for maintenance operations
        	**type**\: bool
        
        	**status**\: deprecated
        
        .. attribute:: crfcfgkeepalivethresh
        
        	On platforms that support keep\-alives, the keep\-alive threshold value designates the number of lost keep\-alives tolerated before a failure condition is declared. If this occurs, a SWACT notification is sent.  On platforms that do not support keep\-alives, this object has no purpose or effect
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfcfgkeepalivethreshmin
        
        	The minimum acceptable value for the cRFCfgKeepaliveThresh object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfcfgkeepalivethreshmax
        
        	The maximum acceptable value for the cRFCfgKeepaliveThresh object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfcfgkeepalivetimer
        
        	On platforms that support keep\-alives, the keep\-alive timer value is used to guard against lost keep\-alives. The RF subsystem expects to receive a keep\-alive within this period. If a keep\-alive is not received within this time period, a SWACT notification is sent.  On platforms that do not support keep\-alives, this object has no purpose or effect
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgkeepalivetimermin
        
        	The minimum acceptable value for the cRFCfgKeepaliveTimer object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgkeepalivetimermax
        
        	The maximum acceptable value for the cRFCfgKeepaliveTimer object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgnotiftimer
        
        	Note that the term 'notification' here refers to an RF notification and not an SNMP notification.  As the standby unit progresses to the 'standbyHot' state, asynchronous messages are sent from the active unit to the standby unit which must then be acknowledged by the standby unit. If the active unit receives the acknowledgement during the time period specified by this object, progression proceeds as normal. If the timer expires and an acknowledgement was not received by the active unit, a switch of activity occurs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgnotiftimermin
        
        	The minimum acceptable value for the cRFCfgNotifTimer object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgnotiftimermax
        
        	The maximum acceptable value for the cRFCfgNotifTimer object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: milliseconds
        
        .. attribute:: crfcfgadminaction
        
        	This variable is set to invoke RF subsystem action commands. The commands are useful for maintenance and software upgrade activities
        	**type**\:  :py:class:`RFAction <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFAction>`
        
        .. attribute:: crfcfgnotifsenabled
        
        	Allows enabling/disabling of RF subsystem notifications
        	**type**\: bool
        
        .. attribute:: crfcfgmaintenancemode
        
        	Indicates whether redundant units may communicate synchronization messages with each other. If communication is not permitted, this object is set to 'true'. If communication is permitted, this object is set to 'false'.  If the value of this object is 'true', the redundant system is considered to be in a maintenance mode of operation. If the value of this object is 'false', the redundant system is considered to be in a normal (non\-maintenance) mode of operation.  In maintenance mode (true), the active unit will not communicate with the standby unit. The standby unit progression will not occur. When maintenance mode is disabled (false), the standby unit is reset to recover.  Maintenance mode (true) is useful for maintenance\-type operations
        	**type**\: bool
        
        .. attribute:: crfcfgredundancymode
        
        	Indicates the redundancy mode configured on the device
        	**type**\:  :py:class:`RFMode <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFMode>`
        
        .. attribute:: crfcfgredundancymodedescr
        
        	Further clarifies or describes the redundancy mode indicated by cRFCfgRedundancyMode. Implementation\-specific terminology associated with the current redundancy mode may be presented here
        	**type**\: str
        
        .. attribute:: crfcfgredundancyopermode
        
        	Indicate the operational redundancy mode of the device
        	**type**\:  :py:class:`RFMode <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFMode>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CISCORFMIB.Crfcfg, self).__init__()

            self.yang_name = "cRFCfg"
            self.yang_parent_name = "CISCO-RF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('crfcfgsplitmode', YLeaf(YType.boolean, 'cRFCfgSplitMode')),
                ('crfcfgkeepalivethresh', YLeaf(YType.uint32, 'cRFCfgKeepaliveThresh')),
                ('crfcfgkeepalivethreshmin', YLeaf(YType.uint32, 'cRFCfgKeepaliveThreshMin')),
                ('crfcfgkeepalivethreshmax', YLeaf(YType.uint32, 'cRFCfgKeepaliveThreshMax')),
                ('crfcfgkeepalivetimer', YLeaf(YType.uint32, 'cRFCfgKeepaliveTimer')),
                ('crfcfgkeepalivetimermin', YLeaf(YType.uint32, 'cRFCfgKeepaliveTimerMin')),
                ('crfcfgkeepalivetimermax', YLeaf(YType.uint32, 'cRFCfgKeepaliveTimerMax')),
                ('crfcfgnotiftimer', YLeaf(YType.uint32, 'cRFCfgNotifTimer')),
                ('crfcfgnotiftimermin', YLeaf(YType.uint32, 'cRFCfgNotifTimerMin')),
                ('crfcfgnotiftimermax', YLeaf(YType.uint32, 'cRFCfgNotifTimerMax')),
                ('crfcfgadminaction', YLeaf(YType.enumeration, 'cRFCfgAdminAction')),
                ('crfcfgnotifsenabled', YLeaf(YType.boolean, 'cRFCfgNotifsEnabled')),
                ('crfcfgmaintenancemode', YLeaf(YType.boolean, 'cRFCfgMaintenanceMode')),
                ('crfcfgredundancymode', YLeaf(YType.enumeration, 'cRFCfgRedundancyMode')),
                ('crfcfgredundancymodedescr', YLeaf(YType.str, 'cRFCfgRedundancyModeDescr')),
                ('crfcfgredundancyopermode', YLeaf(YType.enumeration, 'cRFCfgRedundancyOperMode')),
            ])
            self.crfcfgsplitmode = None
            self.crfcfgkeepalivethresh = None
            self.crfcfgkeepalivethreshmin = None
            self.crfcfgkeepalivethreshmax = None
            self.crfcfgkeepalivetimer = None
            self.crfcfgkeepalivetimermin = None
            self.crfcfgkeepalivetimermax = None
            self.crfcfgnotiftimer = None
            self.crfcfgnotiftimermin = None
            self.crfcfgnotiftimermax = None
            self.crfcfgadminaction = None
            self.crfcfgnotifsenabled = None
            self.crfcfgmaintenancemode = None
            self.crfcfgredundancymode = None
            self.crfcfgredundancymodedescr = None
            self.crfcfgredundancyopermode = None
            self._segment_path = lambda: "cRFCfg"
            self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORFMIB.Crfcfg, ['crfcfgsplitmode', 'crfcfgkeepalivethresh', 'crfcfgkeepalivethreshmin', 'crfcfgkeepalivethreshmax', 'crfcfgkeepalivetimer', 'crfcfgkeepalivetimermin', 'crfcfgkeepalivetimermax', 'crfcfgnotiftimer', 'crfcfgnotiftimermin', 'crfcfgnotiftimermax', 'crfcfgadminaction', 'crfcfgnotifsenabled', 'crfcfgmaintenancemode', 'crfcfgredundancymode', 'crfcfgredundancymodedescr', 'crfcfgredundancyopermode'], name, value)


    class Crfhistory(Entity):
        """
        
        
        .. attribute:: crfhistorytablemaxlength
        
        	Maximum number of entries permissible in the history table. A value of 0 will result in no history being maintained
        	**type**\: int
        
        	**range:** 0..50
        
        .. attribute:: crfhistorycoldstarts
        
        	Indicates the number of system cold starts. This includes the number of system cold starts due to switchover failure and the number of manual restarts
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: crfhistorystandbyavailtime
        
        	Indicates the cumulative time that a standby redundant unit has been available since last system initialization
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CISCORFMIB.Crfhistory, self).__init__()

            self.yang_name = "cRFHistory"
            self.yang_parent_name = "CISCO-RF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('crfhistorytablemaxlength', YLeaf(YType.uint32, 'cRFHistoryTableMaxLength')),
                ('crfhistorycoldstarts', YLeaf(YType.uint32, 'cRFHistoryColdStarts')),
                ('crfhistorystandbyavailtime', YLeaf(YType.int32, 'cRFHistoryStandByAvailTime')),
            ])
            self.crfhistorytablemaxlength = None
            self.crfhistorycoldstarts = None
            self.crfhistorystandbyavailtime = None
            self._segment_path = lambda: "cRFHistory"
            self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORFMIB.Crfhistory, ['crfhistorytablemaxlength', 'crfhistorycoldstarts', 'crfhistorystandbyavailtime'], name, value)


    class Crfstatusrfmodecapstable(Entity):
        """
        This table containing a list of redundancy modes that can be
        supported on the device.
        
        .. attribute:: crfstatusrfmodecapsentry
        
        	An entry containing the device implementation specific terminology associated with the redundancy mode that can be supported on the device
        	**type**\: list of  		 :py:class:`Crfstatusrfmodecapsentry <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CISCORFMIB.Crfstatusrfmodecapstable, self).__init__()

            self.yang_name = "cRFStatusRFModeCapsTable"
            self.yang_parent_name = "CISCO-RF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cRFStatusRFModeCapsEntry", ("crfstatusrfmodecapsentry", CISCORFMIB.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry))])
            self._leafs = OrderedDict()

            self.crfstatusrfmodecapsentry = YList(self)
            self._segment_path = lambda: "cRFStatusRFModeCapsTable"
            self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORFMIB.Crfstatusrfmodecapstable, [], name, value)


        class Crfstatusrfmodecapsentry(Entity):
            """
            An entry containing the device implementation specific
            terminology associated with the redundancy mode that can be
            supported on the device.
            
            .. attribute:: crfstatusrfmodecapsmode  (key)
            
            	The redundancy mode that can be supported on the device
            	**type**\:  :py:class:`RFMode <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFMode>`
            
            .. attribute:: crfstatusrfmodecapsmodedescr
            
            	The description of the device implementation specific terminology associated with its supported redundancy mode
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                super(CISCORFMIB.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry, self).__init__()

                self.yang_name = "cRFStatusRFModeCapsEntry"
                self.yang_parent_name = "cRFStatusRFModeCapsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['crfstatusrfmodecapsmode']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('crfstatusrfmodecapsmode', YLeaf(YType.enumeration, 'cRFStatusRFModeCapsMode')),
                    ('crfstatusrfmodecapsmodedescr', YLeaf(YType.str, 'cRFStatusRFModeCapsModeDescr')),
                ])
                self.crfstatusrfmodecapsmode = None
                self.crfstatusrfmodecapsmodedescr = None
                self._segment_path = lambda: "cRFStatusRFModeCapsEntry" + "[cRFStatusRFModeCapsMode='" + str(self.crfstatusrfmodecapsmode) + "']"
                self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/cRFStatusRFModeCapsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORFMIB.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry, ['crfstatusrfmodecapsmode', 'crfstatusrfmodecapsmodedescr'], name, value)


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
        	**type**\: list of  		 :py:class:`Crfhistoryswitchoverentry <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfhistoryswitchovertable.Crfhistoryswitchoverentry>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CISCORFMIB.Crfhistoryswitchovertable, self).__init__()

            self.yang_name = "cRFHistorySwitchOverTable"
            self.yang_parent_name = "CISCO-RF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cRFHistorySwitchOverEntry", ("crfhistoryswitchoverentry", CISCORFMIB.Crfhistoryswitchovertable.Crfhistoryswitchoverentry))])
            self._leafs = OrderedDict()

            self.crfhistoryswitchoverentry = YList(self)
            self._segment_path = lambda: "cRFHistorySwitchOverTable"
            self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORFMIB.Crfhistoryswitchovertable, [], name, value)


        class Crfhistoryswitchoverentry(Entity):
            """
            The entries in this table contain the switchover
            information. Each entry in the table is indexed by
            cRFHistorySwitchOverIndex. The index wraps around to 1
            after reaching the maximum value.
            
            .. attribute:: crfhistoryswitchoverindex  (key)
            
            	A monotonically increasing integer for the purpose of indexing history table. After reaching maximum value, it wraps around to 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: crfhistoryprevactiveunitid
            
            	Indicates the primary redundant unit that went down
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: crfhistorycurractiveunitid
            
            	Indicates the secondary redundant unit that took over as active
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: crfhistoryswitchoverreason
            
            	Indicates the reason for the switchover
            	**type**\:  :py:class:`RFSwactReasonType <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFSwactReasonType>`
            
            .. attribute:: crfhistoryswacttime
            
            	Indicates the Date & Time when switchover occurred
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                super(CISCORFMIB.Crfhistoryswitchovertable.Crfhistoryswitchoverentry, self).__init__()

                self.yang_name = "cRFHistorySwitchOverEntry"
                self.yang_parent_name = "cRFHistorySwitchOverTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['crfhistoryswitchoverindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('crfhistoryswitchoverindex', YLeaf(YType.uint32, 'cRFHistorySwitchOverIndex')),
                    ('crfhistoryprevactiveunitid', YLeaf(YType.int32, 'cRFHistoryPrevActiveUnitId')),
                    ('crfhistorycurractiveunitid', YLeaf(YType.int32, 'cRFHistoryCurrActiveUnitId')),
                    ('crfhistoryswitchoverreason', YLeaf(YType.enumeration, 'cRFHistorySwitchOverReason')),
                    ('crfhistoryswacttime', YLeaf(YType.str, 'cRFHistorySwactTime')),
                ])
                self.crfhistoryswitchoverindex = None
                self.crfhistoryprevactiveunitid = None
                self.crfhistorycurractiveunitid = None
                self.crfhistoryswitchoverreason = None
                self.crfhistoryswacttime = None
                self._segment_path = lambda: "cRFHistorySwitchOverEntry" + "[cRFHistorySwitchOverIndex='" + str(self.crfhistoryswitchoverindex) + "']"
                self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/cRFHistorySwitchOverTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORFMIB.Crfhistoryswitchovertable.Crfhistoryswitchoverentry, ['crfhistoryswitchoverindex', 'crfhistoryprevactiveunitid', 'crfhistorycurractiveunitid', 'crfhistoryswitchoverreason', 'crfhistoryswacttime'], name, value)


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
        	**type**\: list of  		 :py:class:`Crfstatusrfcliententry <ydk.models.cisco_ios_xe.CISCO_RF_MIB.CISCORFMIB.Crfstatusrfclienttable.Crfstatusrfcliententry>`
        
        

        """

        _prefix = 'CISCO-RF-MIB'
        _revision = '2005-09-01'

        def __init__(self):
            super(CISCORFMIB.Crfstatusrfclienttable, self).__init__()

            self.yang_name = "cRFStatusRFClientTable"
            self.yang_parent_name = "CISCO-RF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cRFStatusRFClientEntry", ("crfstatusrfcliententry", CISCORFMIB.Crfstatusrfclienttable.Crfstatusrfcliententry))])
            self._leafs = OrderedDict()

            self.crfstatusrfcliententry = YList(self)
            self._segment_path = lambda: "cRFStatusRFClientTable"
            self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCORFMIB.Crfstatusrfclienttable, [], name, value)


        class Crfstatusrfcliententry(Entity):
            """
            An entry containing information on various clients
            registered with the Redundancy Facility (RF). Entries in
            this table are always created by the system.
            
            An entry is created in this table when a redundancy aware 
            application registers with the Redundancy Facility. The entry 
            is destroyed when that application deregisters from the 
            Redundancy Facility.
            
            .. attribute:: crfstatusrfclientid  (key)
            
            	A unique identifier for the client which registered with the Redundancy Facility
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: crfstatusrfclientdescr
            
            	The description of the client which has registered with the Redundancy Facility
            	**type**\: str
            
            .. attribute:: crfstatusrfclientseq
            
            	The sequence number of the client. The system assigns the sequence numbers based on the order of registration of the Redundancy Facility clients.  This is used for deciding order of RF events sent to clients
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: crfstatusrfclientredtime
            
            	Time taken for this client to become Redundant. This value is meaningful when the value of cRFStatusRFClientStatus is not 'noStatus'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: crfstatusrfclientstatus
            
            	This object provides the status of the Redundancy Facility client
            	**type**\:  :py:class:`RFClientStatus <ydk.models.cisco_ios_xe.CISCO_RF_MIB.RFClientStatus>`
            
            

            """

            _prefix = 'CISCO-RF-MIB'
            _revision = '2005-09-01'

            def __init__(self):
                super(CISCORFMIB.Crfstatusrfclienttable.Crfstatusrfcliententry, self).__init__()

                self.yang_name = "cRFStatusRFClientEntry"
                self.yang_parent_name = "cRFStatusRFClientTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['crfstatusrfclientid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('crfstatusrfclientid', YLeaf(YType.uint32, 'cRFStatusRFClientID')),
                    ('crfstatusrfclientdescr', YLeaf(YType.str, 'cRFStatusRFClientDescr')),
                    ('crfstatusrfclientseq', YLeaf(YType.uint32, 'cRFStatusRFClientSeq')),
                    ('crfstatusrfclientredtime', YLeaf(YType.uint32, 'cRFStatusRFClientRedTime')),
                    ('crfstatusrfclientstatus', YLeaf(YType.enumeration, 'cRFStatusRFClientStatus')),
                ])
                self.crfstatusrfclientid = None
                self.crfstatusrfclientdescr = None
                self.crfstatusrfclientseq = None
                self.crfstatusrfclientredtime = None
                self.crfstatusrfclientstatus = None
                self._segment_path = lambda: "cRFStatusRFClientEntry" + "[cRFStatusRFClientID='" + str(self.crfstatusrfclientid) + "']"
                self._absolute_path = lambda: "CISCO-RF-MIB:CISCO-RF-MIB/cRFStatusRFClientTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCORFMIB.Crfstatusrfclienttable.Crfstatusrfcliententry, ['crfstatusrfclientid', 'crfstatusrfclientdescr', 'crfstatusrfclientseq', 'crfstatusrfclientredtime', 'crfstatusrfclientstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCORFMIB()
        return self._top_entity

