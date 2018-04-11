""" CISCO_ENTITY_FRU_CONTROL_MIB 

The CISCO\-ENTITY\-FRU\-CONTROL\-MIB is used to monitor
and configure operational status of 
Field Replaceable Units (FRUs) and other managable 
physical entities of the system listed in the 
Entity\-MIB (RFC 2737) entPhysicalTable. 

FRUs include assemblies such as power supplies, fans, 
processor modules, interface modules, etc.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class FRUCoolingUnit(Enum):
    """
    FRUCoolingUnit (Enum Class)

    The unit for the cooling capacity and requirement.

    cfm(1)    Cubic feet per minute

    watts(2)  Watts

    .. data:: cfm = 1

    .. data:: watts = 2

    """

    cfm = Enum.YLeaf(1, "cfm")

    watts = Enum.YLeaf(2, "watts")


class ModuleAdminType(Enum):
    """
    ModuleAdminType (Enum Class)

    Administratively desired module states.  Valid values are\:

    enabled(1)     module is operational.

    disabled(2)    module is not operational.

    reset(3)       module is reset. This value may be specified

                   in a management protocol set operation, it will

                   not be returned in response to a management 

                   protocol retrieval operation. 

    outOfServiceAdmin(4)   module is powered on but out of 

                           service, set by CLI.

    .. data:: enabled = 1

    .. data:: disabled = 2

    .. data:: reset = 3

    .. data:: outOfServiceAdmin = 4

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")

    reset = Enum.YLeaf(3, "reset")

    outOfServiceAdmin = Enum.YLeaf(4, "outOfServiceAdmin")


class ModuleOperType(Enum):
    """
    ModuleOperType (Enum Class)

    Operational module states.  Valid values are \:

    unknown(1)           Module is not in one of other states

     normal operational states\:

    ok(2)                 Module is operational.

    disabled(3)           Module is administratively disabled.

    okButDiagFailed(4)    Module is operational but there is some

                         diagnostic information available.

     transitional states\:

    boot(5)               Module is currently in the process of

                         bringing up image.  After boot, it starts

                         its operational software and transitions

                         to the appropriate state.

    selfTest(6)           Module is performing selfTest.

     failure states\:

    failed(7)              Module has failed due to some condition

                          not stated above.

    missing(8)             Module has been provisioned, but it is

                          missing

    mismatchWithParent(9)  Module is not compatible with parent

                          entity. Module has not been provisioned

                          and wrong type of module is plugged in.

                          This state can be cleared by plugging

                          in the appropriate module.

    mismatchConfig(10)     Module is not compatible with the

    current

                          configuration. Module was correctly

                          provisioned earlier, however the module

                          was replaced by an incompatible module.

                          This state can be resolved by clearing

                          the configuration, or replacing with the

                          appropriate module.

    diagFailed(11)         Module diagnostic test failed due to

    some

                          hardware failure.

    dormant(12)            Module is waiting for an external or

                          internal event to become operational.

    outOfServiceAdmin(13)  module is administratively set to be

                          powered on but out of service.

    outOfServiceEnvTemp(14)Module is powered on but out of service,

                          due to environmental temperature problem.

                          An out\-o\-service module consumes less

                          power thus will cool down the board.

    poweredDown(15)       Module is in powered down state.

    poweredUp(16)         Module is in powered up state.

    powerDenied(17)       System does not have enough power in

                          power budget to power on this module.

    powerCycled(18)       Module is being power cycled.

    okButPowerOverWarning(19) Module is drawing more power than 

                          allocated to this module. The module

                          is still operational but may go into

                          a failure state. This state may be

                          caused by misconfiguration of power 

                          requirements (especially for inline 

                          power). 

    okButPowerOverCritical(20) Module is drawing more power

                          than this module is designed to 

                          handle. The module is still 

                          operational but may go into a 

                          failure state and could potentially

                          take the system down. This state

                          may be caused by gross misconfi\-

                          guration of power requirements      

                          (especially for inline power). 

    syncInProgress(21)    Synchronization in progress.

                          In a high availability system there 

                          will be 2 control modules, active and 

                          standby. 

                          This transitional state specifies the

                          synchronization of data between the

                          active and standby modules.

    upgrading(22)         Module is upgrading.

    okButAuthFailed(23)   Module is operational but did not pass 

                          hardware integrity verification.

    mdr(24)               Module is undergoing a Minimum 

                          Disruptive Restart (MDR) upgrade.

     firmware download states\:

    fwMismatchFound(25)   Mistmatch found between current firmware 

                          version and the firmware version in the 

                          system image.

    fwDownloadSuccess(26) Module firmware download succeeded.

    fwDownloadFailure(27) Module firmware download failed.

    .. data:: unknown = 1

    .. data:: ok = 2

    .. data:: disabled = 3

    .. data:: okButDiagFailed = 4

    .. data:: boot = 5

    .. data:: selfTest = 6

    .. data:: failed = 7

    .. data:: missing = 8

    .. data:: mismatchWithParent = 9

    .. data:: mismatchConfig = 10

    .. data:: diagFailed = 11

    .. data:: dormant = 12

    .. data:: outOfServiceAdmin = 13

    .. data:: outOfServiceEnvTemp = 14

    .. data:: poweredDown = 15

    .. data:: poweredUp = 16

    .. data:: powerDenied = 17

    .. data:: powerCycled = 18

    .. data:: okButPowerOverWarning = 19

    .. data:: okButPowerOverCritical = 20

    .. data:: syncInProgress = 21

    .. data:: upgrading = 22

    .. data:: okButAuthFailed = 23

    .. data:: mdr = 24

    .. data:: fwMismatchFound = 25

    .. data:: fwDownloadSuccess = 26

    .. data:: fwDownloadFailure = 27

    """

    unknown = Enum.YLeaf(1, "unknown")

    ok = Enum.YLeaf(2, "ok")

    disabled = Enum.YLeaf(3, "disabled")

    okButDiagFailed = Enum.YLeaf(4, "okButDiagFailed")

    boot = Enum.YLeaf(5, "boot")

    selfTest = Enum.YLeaf(6, "selfTest")

    failed = Enum.YLeaf(7, "failed")

    missing = Enum.YLeaf(8, "missing")

    mismatchWithParent = Enum.YLeaf(9, "mismatchWithParent")

    mismatchConfig = Enum.YLeaf(10, "mismatchConfig")

    diagFailed = Enum.YLeaf(11, "diagFailed")

    dormant = Enum.YLeaf(12, "dormant")

    outOfServiceAdmin = Enum.YLeaf(13, "outOfServiceAdmin")

    outOfServiceEnvTemp = Enum.YLeaf(14, "outOfServiceEnvTemp")

    poweredDown = Enum.YLeaf(15, "poweredDown")

    poweredUp = Enum.YLeaf(16, "poweredUp")

    powerDenied = Enum.YLeaf(17, "powerDenied")

    powerCycled = Enum.YLeaf(18, "powerCycled")

    okButPowerOverWarning = Enum.YLeaf(19, "okButPowerOverWarning")

    okButPowerOverCritical = Enum.YLeaf(20, "okButPowerOverCritical")

    syncInProgress = Enum.YLeaf(21, "syncInProgress")

    upgrading = Enum.YLeaf(22, "upgrading")

    okButAuthFailed = Enum.YLeaf(23, "okButAuthFailed")

    mdr = Enum.YLeaf(24, "mdr")

    fwMismatchFound = Enum.YLeaf(25, "fwMismatchFound")

    fwDownloadSuccess = Enum.YLeaf(26, "fwDownloadSuccess")

    fwDownloadFailure = Enum.YLeaf(27, "fwDownloadFailure")


class ModuleResetReasonType(Enum):
    """
    ModuleResetReasonType (Enum Class)

    Describes the reason for the last module reset operation.

    unknown(1)                      source of the reset is not 

                                    identified

    powerUp(2)                      system power up operation

    parityError(3)                  parity error during system 

                                    bring up operation

    clearConfigReset(4)             reset due to clear 

                                    configuration operation

    manualReset(5)                  reset due to administrative 

                                    request

    watchDogTimeoutReset(6)         reset due to watchdog timeout

    resourceOverflowReset(7)        reset due to resource overflow

    missingTaskReset(8)             reset due to missing task

    lowVoltageReset(9)              reset due to low voltage

    controllerReset(10)             reset by controller

    systemReset(11)                 system reset

    switchoverReset(12)             reset due to user initiated 

                                    graceful switchover

    upgradeReset(13)                reset due to upgrade

    downgradeReset(14)              reset due to downgrade

    cacheErrorReset(15)             reset due to cache error

    deviceDriverReset(16)           reset due to device driver 

                                    error

    softwareExceptionReset(17)      reset due to software 

                                    exception

    restoreConfigReset(18)          reset due to configuration

                                    restoration

    abortRevReset(19)               reset due to revision change 

                                    abort

    burnBootReset(20)               reset due to boot image 

                                    change

    standbyCdHealthierReset(21)     reset to switch to healthier 

                                    standby card

    nonNativeConfigClearReset(22)   reset due clearing of 

                                    non\-native configuration

    memoryProtectionErrorReset(23)  reset due to memory protection 

                                    violation.

    .. data:: unknown = 1

    .. data:: powerUp = 2

    .. data:: parityError = 3

    .. data:: clearConfigReset = 4

    .. data:: manualReset = 5

    .. data:: watchDogTimeoutReset = 6

    .. data:: resourceOverflowReset = 7

    .. data:: missingTaskReset = 8

    .. data:: lowVoltageReset = 9

    .. data:: controllerReset = 10

    .. data:: systemReset = 11

    .. data:: switchoverReset = 12

    .. data:: upgradeReset = 13

    .. data:: downgradeReset = 14

    .. data:: cacheErrorReset = 15

    .. data:: deviceDriverReset = 16

    .. data:: softwareExceptionReset = 17

    .. data:: restoreConfigReset = 18

    .. data:: abortRevReset = 19

    .. data:: burnBootReset = 20

    .. data:: standbyCdHealthierReset = 21

    .. data:: nonNativeConfigClearReset = 22

    .. data:: memoryProtectionErrorReset = 23

    """

    unknown = Enum.YLeaf(1, "unknown")

    powerUp = Enum.YLeaf(2, "powerUp")

    parityError = Enum.YLeaf(3, "parityError")

    clearConfigReset = Enum.YLeaf(4, "clearConfigReset")

    manualReset = Enum.YLeaf(5, "manualReset")

    watchDogTimeoutReset = Enum.YLeaf(6, "watchDogTimeoutReset")

    resourceOverflowReset = Enum.YLeaf(7, "resourceOverflowReset")

    missingTaskReset = Enum.YLeaf(8, "missingTaskReset")

    lowVoltageReset = Enum.YLeaf(9, "lowVoltageReset")

    controllerReset = Enum.YLeaf(10, "controllerReset")

    systemReset = Enum.YLeaf(11, "systemReset")

    switchoverReset = Enum.YLeaf(12, "switchoverReset")

    upgradeReset = Enum.YLeaf(13, "upgradeReset")

    downgradeReset = Enum.YLeaf(14, "downgradeReset")

    cacheErrorReset = Enum.YLeaf(15, "cacheErrorReset")

    deviceDriverReset = Enum.YLeaf(16, "deviceDriverReset")

    softwareExceptionReset = Enum.YLeaf(17, "softwareExceptionReset")

    restoreConfigReset = Enum.YLeaf(18, "restoreConfigReset")

    abortRevReset = Enum.YLeaf(19, "abortRevReset")

    burnBootReset = Enum.YLeaf(20, "burnBootReset")

    standbyCdHealthierReset = Enum.YLeaf(21, "standbyCdHealthierReset")

    nonNativeConfigClearReset = Enum.YLeaf(22, "nonNativeConfigClearReset")

    memoryProtectionErrorReset = Enum.YLeaf(23, "memoryProtectionErrorReset")


class PowerAdminType(Enum):
    """
    PowerAdminType (Enum Class)

    Administratively desired FRU power state types.  valid values

    are\:

    on(1)\:  Turn FRU on.

    off(2)\: Turn FRU off.

    The inline power means that the FRU itself won't cost any power,

    but the external device connecting to the FRU will drain the

    power from FRU.  For example, the IP phone device.  The FRU is a

    port of a switch with voice ability and IP phone will cost power

    from the port once it connects to the port.

    inlineAuto(3)\: Turn FRU inline power to auto mode. It means that

    the FRU will try to detect whether the connecting device needs

    power or not.  If it needs power, the FRU will supply power.  If

    it doesn't, the FRU will treat the device as a regular network

    device.

    inlineOn(4)\: Turn FRU inline power to on mode.  It means that

    once the device connects to the FRU, the FRU will always supply

    power to the device no matter the device needs the power or not.

    powerCycle(5)\: Power cycle the FRU.  This value may be specified

    in a management protocol set operation, it will not be returned 

    in response to a management protocol retrieval operation.

    .. data:: on = 1

    .. data:: off = 2

    .. data:: inlineAuto = 3

    .. data:: inlineOn = 4

    .. data:: powerCycle = 5

    """

    on = Enum.YLeaf(1, "on")

    off = Enum.YLeaf(2, "off")

    inlineAuto = Enum.YLeaf(3, "inlineAuto")

    inlineOn = Enum.YLeaf(4, "inlineOn")

    powerCycle = Enum.YLeaf(5, "powerCycle")


class PowerOperType(Enum):
    """
    PowerOperType (Enum Class)

    Operational FRU Status types.  valid values are\:

    offEnvOther(1)   FRU is powered off because of a problem not

                     listed below.

    on(2)\:           FRU is powered on.

    offAdmin(3)\:     Administratively off.

    offDenied(4)\:    FRU is powered off because available

                     system power is insufficient.

    offEnvPower(5)\:  FRU is powered off because of power problem in

                     the FRU.  for example, the FRU's power

                     translation (DC\-DC converter) or distribution

                     failed.

    offEnvTemp(6)\:   FRU is powered off because of temperature

                     problem.

    offEnvFan(7)\:    FRU is powered off because of fan problems.

    failed(8)\:       FRU is in failed state. 

    onButFanFail(9)\: FRU is on, but fan has failed.

    offCooling(10)\:  FRU is powered off because of the system's 

                     insufficient cooling capacity.

    offConnectorRating(11)\: FRU is powered off because of the 

                            system's connector rating exceeded.

    onButInlinePowerFail(12)\: The FRU on, but no inline power

                              is being delivered as the

                              data/inline power component of the

                              FRU has failed.

    .. data:: offEnvOther = 1

    .. data:: on = 2

    .. data:: offAdmin = 3

    .. data:: offDenied = 4

    .. data:: offEnvPower = 5

    .. data:: offEnvTemp = 6

    .. data:: offEnvFan = 7

    .. data:: failed = 8

    .. data:: onButFanFail = 9

    .. data:: offCooling = 10

    .. data:: offConnectorRating = 11

    .. data:: onButInlinePowerFail = 12

    """

    offEnvOther = Enum.YLeaf(1, "offEnvOther")

    on = Enum.YLeaf(2, "on")

    offAdmin = Enum.YLeaf(3, "offAdmin")

    offDenied = Enum.YLeaf(4, "offDenied")

    offEnvPower = Enum.YLeaf(5, "offEnvPower")

    offEnvTemp = Enum.YLeaf(6, "offEnvTemp")

    offEnvFan = Enum.YLeaf(7, "offEnvFan")

    failed = Enum.YLeaf(8, "failed")

    onButFanFail = Enum.YLeaf(9, "onButFanFail")

    offCooling = Enum.YLeaf(10, "offCooling")

    offConnectorRating = Enum.YLeaf(11, "offConnectorRating")

    onButInlinePowerFail = Enum.YLeaf(12, "onButInlinePowerFail")


class PowerRedundancyType(Enum):
    """
    PowerRedundancyType (Enum Class)

    power supply redundancy modes.  valid values are\:

    notsupported(1)\: Read\-only operational state, indicates

        that the requested administrative state (redundant(2),

        combined(3), psRedundant(5), inPwrSrcRedundant(6)

        or psRedundantSingleInput(7)) is not supported

        by the system.

    redundant(2)\: A single power supply output can power

        the entire system, although there are more than

        one matched supply in the system.

        In the systems which support multiple level of

        redundancy, such as input power redundancy, this

        state indicates that redundancy is enabled on

        all levels.

    combined(3)\: The combined output of the power supplies

        are available to operate the system when there are

        more than one matched power supply in the system.

        In the platforms which support multiple level of

        redundancy, such as input redundancy, this state

        indicates that no redundancy on all levels.

    nonRedundant(4)\: Read\-only operational state, indicates

        that there is only one power supply or there are

        unmatched power supplies in the system.

    psRedundant(5)\: Only the power output redundancy

        is enabled in the systems which support multiple

        levels of redundancy.  All other types of redundancy,

        such as input power redundancy, are disabled.

        This value is only supported by the systems which

        support multiple levels of redundancy.

    inPwrSrcRedundant(6)\: Only the input power redundancy

        is enabled in the systems which support multiple

        levels of redundancy.  All other types of redundancy,

        such as output power redundancy, are disabled.

        This value is only supported by the systems which

        support input power redundancy.

     psRedundantSingleInput(7)\: Only the power redundancy with

        single input is enabled in the systems which support

        multiple levels of redundancy.  All other types of

        redundancy, such as output power redundancy, are disabled.

        This value is only supported by the systems which

        support power redundancy with single input.

    .. data:: notsupported = 1

    .. data:: redundant = 2

    .. data:: combined = 3

    .. data:: nonRedundant = 4

    .. data:: psRedundant = 5

    .. data:: inPwrSrcRedundant = 6

    .. data:: psRedundantSingleInput = 7

    """

    notsupported = Enum.YLeaf(1, "notsupported")

    redundant = Enum.YLeaf(2, "redundant")

    combined = Enum.YLeaf(3, "combined")

    nonRedundant = Enum.YLeaf(4, "nonRedundant")

    psRedundant = Enum.YLeaf(5, "psRedundant")

    inPwrSrcRedundant = Enum.YLeaf(6, "inPwrSrcRedundant")

    psRedundantSingleInput = Enum.YLeaf(7, "psRedundantSingleInput")



class CISCOENTITYFRUCONTROLMIB(Entity):
    """
    
    
    .. attribute:: cefcfrupower
    
    	
    	**type**\:  :py:class:`Cefcfrupower <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupower>`
    
    .. attribute:: cefcmibnotificationenables
    
    	
    	**type**\:  :py:class:`Cefcmibnotificationenables <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmibnotificationenables>`
    
    .. attribute:: cefcfrupowersupplygrouptable
    
    	This table lists the redundancy mode and the operational status of the power supply groups in the system
    	**type**\:  :py:class:`Cefcfrupowersupplygrouptable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable>`
    
    .. attribute:: cefcfrupowerstatustable
    
    	This table lists the power\-related administrative status and operational status of the manageable components in the system
    	**type**\:  :py:class:`Cefcfrupowerstatustable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable>`
    
    .. attribute:: cefcfrupowersupplyvaluetable
    
    	This table lists the power capacity of a power FRU in the system if it provides variable power. Power supplies usually provide either system or inline power. They cannot be  controlled by software to dictate how they distribute power. We can also have what are known as variable power supplies. They can provide both system and inline power and can be  varied within hardware defined ranges for system and inline limited by a total maximum combined output. They could be configured by the user via CLI or SNMP or be controlled by software internally. This table supplements the information in the cefcFRUPowerStatusTable for power supply FRUs. The  cefcFRUCurrent attribute in that table provides the overall current the power supply FRU can provide while this table  gives us the individual contribution towards system and  inline power
    	**type**\:  :py:class:`Cefcfrupowersupplyvaluetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable>`
    
    .. attribute:: cefcmoduletable
    
    	A cefcModuleTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components of type PhysicalClass module(9)
    	**type**\:  :py:class:`Cefcmoduletable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmoduletable>`
    
    .. attribute:: cefcintellimoduletable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcIntelliModuleTable entry lists the information specific to intelligent modules which cannot be provided by the cefcModuleTable
    	**type**\:  :py:class:`Cefcintellimoduletable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable>`
    
    .. attribute:: cefcmodulelocalswitchingtable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcModuleLocalSwitchingTable entry lists the information specific to local switching capable modules which cannot be provided by the cefcModuleTable
    	**type**\:  :py:class:`Cefcmodulelocalswitchingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable>`
    
    .. attribute:: cefcfantraystatustable
    
    	This table contains the operational status information for all ENTITY\-MIB entPhysicalTable entries which have  an entPhysicalClass of 'fan'; specifically, all   entPhysicalTable entries which represent either\: one  physical fan, or a single physical 'fan tray' which is a manufactured (inseparable in the field) combination of  multiple fans
    	**type**\:  :py:class:`Cefcfantraystatustable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable>`
    
    .. attribute:: cefcphysicaltable
    
    	This table contains one row per physical entity
    	**type**\:  :py:class:`Cefcphysicaltable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable>`
    
    .. attribute:: cefcpowersupplyinputtable
    
    	This table contains the power input information for all the power supplies that have entPhysicalTable entries with 'powerSupply' in the entPhysicalClass.   The entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries is determined by the number of power supplies and number of power inputs on the power  supply
    	**type**\:  :py:class:`Cefcpowersupplyinputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable>`
    
    .. attribute:: cefcpowersupplyoutputtable
    
    	This table contains a list of possible output mode for the power supplies, whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'powerSupply'. It also indicate which mode is the operational mode within the system
    	**type**\:  :py:class:`Cefcpowersupplyoutputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable>`
    
    .. attribute:: cefcchassiscoolingtable
    
    	This table contains the cooling capacity information of the chassis whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'chassis'
    	**type**\:  :py:class:`Cefcchassiscoolingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable>`
    
    .. attribute:: cefcfancoolingtable
    
    	This table contains the cooling capacity information of the fans whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'fan'
    	**type**\:  :py:class:`Cefcfancoolingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable>`
    
    .. attribute:: cefcmodulecoolingtable
    
    	This table contains the cooling requirement for all the manageable components of type entPhysicalClass 'module'
    	**type**\:  :py:class:`Cefcmodulecoolingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable>`
    
    .. attribute:: cefcfancoolingcaptable
    
    	This table contains a list of the possible cooling capacity modes and properties of the fans, whose  ENTITY\-MIB entPhysicalTable entries have an  entPhysicalClass of 'fan'
    	**type**\:  :py:class:`Cefcfancoolingcaptable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable>`
    
    .. attribute:: cefcconnectorratingtable
    
    	This table contains the connector power ratings of FRUs.   Only components with power connector rating  management are listed in this table
    	**type**\:  :py:class:`Cefcconnectorratingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable>`
    
    .. attribute:: cefcmodulepowerconsumptiontable
    
    	This table contains the total power consumption information for modules whose ENTITY\-MIB  entPhysicalTable entries have an entPhysicalClass  of 'module'
    	**type**\:  :py:class:`Cefcmodulepowerconsumptiontable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable>`
    
    

    """

    _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
    _revision = '2013-08-19'

    def __init__(self):
        super(CISCOENTITYFRUCONTROLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
        self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cefcFRUPower", ("cefcfrupower", CISCOENTITYFRUCONTROLMIB.Cefcfrupower)), ("cefcMIBNotificationEnables", ("cefcmibnotificationenables", CISCOENTITYFRUCONTROLMIB.Cefcmibnotificationenables)), ("cefcFRUPowerSupplyGroupTable", ("cefcfrupowersupplygrouptable", CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable)), ("cefcFRUPowerStatusTable", ("cefcfrupowerstatustable", CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable)), ("cefcFRUPowerSupplyValueTable", ("cefcfrupowersupplyvaluetable", CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable)), ("cefcModuleTable", ("cefcmoduletable", CISCOENTITYFRUCONTROLMIB.Cefcmoduletable)), ("cefcIntelliModuleTable", ("cefcintellimoduletable", CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable)), ("cefcModuleLocalSwitchingTable", ("cefcmodulelocalswitchingtable", CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable)), ("cefcFanTrayStatusTable", ("cefcfantraystatustable", CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable)), ("cefcPhysicalTable", ("cefcphysicaltable", CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable)), ("cefcPowerSupplyInputTable", ("cefcpowersupplyinputtable", CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable)), ("cefcPowerSupplyOutputTable", ("cefcpowersupplyoutputtable", CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable)), ("cefcChassisCoolingTable", ("cefcchassiscoolingtable", CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable)), ("cefcFanCoolingTable", ("cefcfancoolingtable", CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable)), ("cefcModuleCoolingTable", ("cefcmodulecoolingtable", CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable)), ("cefcFanCoolingCapTable", ("cefcfancoolingcaptable", CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable)), ("cefcConnectorRatingTable", ("cefcconnectorratingtable", CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable)), ("cefcModulePowerConsumptionTable", ("cefcmodulepowerconsumptiontable", CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cefcfrupower = CISCOENTITYFRUCONTROLMIB.Cefcfrupower()
        self.cefcfrupower.parent = self
        self._children_name_map["cefcfrupower"] = "cefcFRUPower"
        self._children_yang_names.add("cefcFRUPower")

        self.cefcmibnotificationenables = CISCOENTITYFRUCONTROLMIB.Cefcmibnotificationenables()
        self.cefcmibnotificationenables.parent = self
        self._children_name_map["cefcmibnotificationenables"] = "cefcMIBNotificationEnables"
        self._children_yang_names.add("cefcMIBNotificationEnables")

        self.cefcfrupowersupplygrouptable = CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable()
        self.cefcfrupowersupplygrouptable.parent = self
        self._children_name_map["cefcfrupowersupplygrouptable"] = "cefcFRUPowerSupplyGroupTable"
        self._children_yang_names.add("cefcFRUPowerSupplyGroupTable")

        self.cefcfrupowerstatustable = CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable()
        self.cefcfrupowerstatustable.parent = self
        self._children_name_map["cefcfrupowerstatustable"] = "cefcFRUPowerStatusTable"
        self._children_yang_names.add("cefcFRUPowerStatusTable")

        self.cefcfrupowersupplyvaluetable = CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable()
        self.cefcfrupowersupplyvaluetable.parent = self
        self._children_name_map["cefcfrupowersupplyvaluetable"] = "cefcFRUPowerSupplyValueTable"
        self._children_yang_names.add("cefcFRUPowerSupplyValueTable")

        self.cefcmoduletable = CISCOENTITYFRUCONTROLMIB.Cefcmoduletable()
        self.cefcmoduletable.parent = self
        self._children_name_map["cefcmoduletable"] = "cefcModuleTable"
        self._children_yang_names.add("cefcModuleTable")

        self.cefcintellimoduletable = CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable()
        self.cefcintellimoduletable.parent = self
        self._children_name_map["cefcintellimoduletable"] = "cefcIntelliModuleTable"
        self._children_yang_names.add("cefcIntelliModuleTable")

        self.cefcmodulelocalswitchingtable = CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable()
        self.cefcmodulelocalswitchingtable.parent = self
        self._children_name_map["cefcmodulelocalswitchingtable"] = "cefcModuleLocalSwitchingTable"
        self._children_yang_names.add("cefcModuleLocalSwitchingTable")

        self.cefcfantraystatustable = CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable()
        self.cefcfantraystatustable.parent = self
        self._children_name_map["cefcfantraystatustable"] = "cefcFanTrayStatusTable"
        self._children_yang_names.add("cefcFanTrayStatusTable")

        self.cefcphysicaltable = CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable()
        self.cefcphysicaltable.parent = self
        self._children_name_map["cefcphysicaltable"] = "cefcPhysicalTable"
        self._children_yang_names.add("cefcPhysicalTable")

        self.cefcpowersupplyinputtable = CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable()
        self.cefcpowersupplyinputtable.parent = self
        self._children_name_map["cefcpowersupplyinputtable"] = "cefcPowerSupplyInputTable"
        self._children_yang_names.add("cefcPowerSupplyInputTable")

        self.cefcpowersupplyoutputtable = CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable()
        self.cefcpowersupplyoutputtable.parent = self
        self._children_name_map["cefcpowersupplyoutputtable"] = "cefcPowerSupplyOutputTable"
        self._children_yang_names.add("cefcPowerSupplyOutputTable")

        self.cefcchassiscoolingtable = CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable()
        self.cefcchassiscoolingtable.parent = self
        self._children_name_map["cefcchassiscoolingtable"] = "cefcChassisCoolingTable"
        self._children_yang_names.add("cefcChassisCoolingTable")

        self.cefcfancoolingtable = CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable()
        self.cefcfancoolingtable.parent = self
        self._children_name_map["cefcfancoolingtable"] = "cefcFanCoolingTable"
        self._children_yang_names.add("cefcFanCoolingTable")

        self.cefcmodulecoolingtable = CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable()
        self.cefcmodulecoolingtable.parent = self
        self._children_name_map["cefcmodulecoolingtable"] = "cefcModuleCoolingTable"
        self._children_yang_names.add("cefcModuleCoolingTable")

        self.cefcfancoolingcaptable = CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable()
        self.cefcfancoolingcaptable.parent = self
        self._children_name_map["cefcfancoolingcaptable"] = "cefcFanCoolingCapTable"
        self._children_yang_names.add("cefcFanCoolingCapTable")

        self.cefcconnectorratingtable = CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable()
        self.cefcconnectorratingtable.parent = self
        self._children_name_map["cefcconnectorratingtable"] = "cefcConnectorRatingTable"
        self._children_yang_names.add("cefcConnectorRatingTable")

        self.cefcmodulepowerconsumptiontable = CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable()
        self.cefcmodulepowerconsumptiontable.parent = self
        self._children_name_map["cefcmodulepowerconsumptiontable"] = "cefcModulePowerConsumptionTable"
        self._children_yang_names.add("cefcModulePowerConsumptionTable")
        self._segment_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB"


    class Cefcfrupower(Entity):
        """
        
        
        .. attribute:: cefcmaxdefaultinlinepower
        
        	The system will provide power to the device connecting to the FRU if the device needs power, like an IP Phone. We call the providing power inline power.  This MIB object controls the maximum default inline power for the device connecting to the FRU in the system. If the maximum default inline power of the device is greater than the maximum value reportable by this object, then this object should report its maximum reportable value (12500) and cefcMaxDefaultHighInLinePower must be used to report the actual maximum default inline power
        	**type**\: int
        
        	**range:** 0..12500
        
        	**units**\: miliwatts
        
        	**status**\: deprecated
        
        .. attribute:: cefcmaxdefaulthighinlinepower
        
        	The system will provide power to the device connecting to the FRU if the device needs power, like an IP Phone. We call the providing power inline power.  This MIB object controls the maximum default inline power for the device connecting to the FRU in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: miliwatts
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfrupower, self).__init__()

            self.yang_name = "cefcFRUPower"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefcmaxdefaultinlinepower', YLeaf(YType.int32, 'cefcMaxDefaultInLinePower')),
                ('cefcmaxdefaulthighinlinepower', YLeaf(YType.uint32, 'cefcMaxDefaultHighInLinePower')),
            ])
            self.cefcmaxdefaultinlinepower = None
            self.cefcmaxdefaulthighinlinepower = None
            self._segment_path = lambda: "cefcFRUPower"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupower, ['cefcmaxdefaultinlinepower', 'cefcmaxdefaulthighinlinepower'], name, value)


    class Cefcmibnotificationenables(Entity):
        """
        
        
        .. attribute:: cefcmibenablestatusnotification
        
        	This variable indicates whether the system produces the following notifications\: cefcModuleStatusChange, cefcPowerStatusChange,  cefcFRUInserted, cefcFRURemoved,  cefcUnrecognizedFRU and cefcFanTrayStatusChange.  A false value will prevent these notifications from being generated
        	**type**\: bool
        
        .. attribute:: cefcenablepsoutputchangenotif
        
        	This variable indicates whether the system produces the cefcPowerSupplyOutputChange  notifications when the output capacity of  a power supply has changed. A false value  will prevent this notification to generated
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcmibnotificationenables, self).__init__()

            self.yang_name = "cefcMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefcmibenablestatusnotification', YLeaf(YType.boolean, 'cefcMIBEnableStatusNotification')),
                ('cefcenablepsoutputchangenotif', YLeaf(YType.boolean, 'cefcEnablePSOutputChangeNotif')),
            ])
            self.cefcmibenablestatusnotification = None
            self.cefcenablepsoutputchangenotif = None
            self._segment_path = lambda: "cefcMIBNotificationEnables"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmibnotificationenables, ['cefcmibenablestatusnotification', 'cefcenablepsoutputchangenotif'], name, value)


    class Cefcfrupowersupplygrouptable(Entity):
        """
        This table lists the redundancy mode and the
        operational status of the power supply groups
        in the system.
        
        .. attribute:: cefcfrupowersupplygroupentry
        
        	An cefcFRUPowerSupplyGroupTable entry lists the desired redundancy mode, the units of the power outputs and the  available and drawn current for the power supply group.  Entries are created by the agent when a power supply group is added to the entPhysicalTable. Entries are deleted by  the agent at power supply group removal
        	**type**\: list of  		 :py:class:`Cefcfrupowersupplygroupentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyGroupTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcFRUPowerSupplyGroupEntry", ("cefcfrupowersupplygroupentry", CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry))])
            self._leafs = OrderedDict()

            self.cefcfrupowersupplygroupentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerSupplyGroupTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable, [], name, value)


        class Cefcfrupowersupplygroupentry(Entity):
            """
            An cefcFRUPowerSupplyGroupTable entry lists the desired
            redundancy mode, the units of the power outputs and the 
            available and drawn current for the power supply group.
            
            Entries are created by the agent when a power supply group
            is added to the entPhysicalTable. Entries are deleted by 
            the agent at power supply group removal.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcpowerredundancymode
            
            	The administratively desired power supply redundancy mode
            	**type**\:  :py:class:`PowerRedundancyType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PowerRedundancyType>`
            
            .. attribute:: cefcpowerunits
            
            	The units of primary supply to interpret cefcTotalAvailableCurrent and cefcTotalDrawnCurrent as power.  For example, one 1000\-watt power supply could  deliver 100 amperes at 10 volts DC.  So the value of cefcPowerUnits would be 'at 10 volts DC'.  cefcPowerUnits is for display purposes only
            	**type**\: str
            
            .. attribute:: cefctotalavailablecurrent
            
            	Total current available for FRU usage
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefctotaldrawncurrent
            
            	Total current drawn by powered\-on FRUs
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcpowerredundancyopermode
            
            	The power supply redundancy operational mode
            	**type**\:  :py:class:`PowerRedundancyType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PowerRedundancyType>`
            
            .. attribute:: cefcpowernonredundantreason
            
            	This object has the value of notApplicable(1) when cefcPowerRedundancyOperMode of the instance does not have the value of nonRedundant(4).  The other values explain the reason why  cefcPowerRedundancyOperMode is nonRedundant(4), e.g.  unknown(2)             the reason is not identified.  singleSupply(3)        There is only one power supply                        in the group.  mismatchedSupplies(4)  There are more than one power                        supplies in the groups. However                        they are mismatched and can not                        work redundantly.  supplyError(5)         Some power supply or supplies                        does or do not working properly
            	**type**\:  :py:class:`Cefcpowernonredundantreason <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry.Cefcpowernonredundantreason>`
            
            .. attribute:: cefctotaldrawninlinecurrent
            
            	Total inline current drawn for inline operation
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyGroupEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcpowerredundancymode', YLeaf(YType.enumeration, 'cefcPowerRedundancyMode')),
                    ('cefcpowerunits', YLeaf(YType.str, 'cefcPowerUnits')),
                    ('cefctotalavailablecurrent', YLeaf(YType.int32, 'cefcTotalAvailableCurrent')),
                    ('cefctotaldrawncurrent', YLeaf(YType.int32, 'cefcTotalDrawnCurrent')),
                    ('cefcpowerredundancyopermode', YLeaf(YType.enumeration, 'cefcPowerRedundancyOperMode')),
                    ('cefcpowernonredundantreason', YLeaf(YType.enumeration, 'cefcPowerNonRedundantReason')),
                    ('cefctotaldrawninlinecurrent', YLeaf(YType.int32, 'cefcTotalDrawnInlineCurrent')),
                ])
                self.entphysicalindex = None
                self.cefcpowerredundancymode = None
                self.cefcpowerunits = None
                self.cefctotalavailablecurrent = None
                self.cefctotaldrawncurrent = None
                self.cefcpowerredundancyopermode = None
                self.cefcpowernonredundantreason = None
                self.cefctotaldrawninlinecurrent = None
                self._segment_path = lambda: "cefcFRUPowerSupplyGroupEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyGroupTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry, ['entphysicalindex', 'cefcpowerredundancymode', 'cefcpowerunits', 'cefctotalavailablecurrent', 'cefctotaldrawncurrent', 'cefcpowerredundancyopermode', 'cefcpowernonredundantreason', 'cefctotaldrawninlinecurrent'], name, value)

            class Cefcpowernonredundantreason(Enum):
                """
                Cefcpowernonredundantreason (Enum Class)

                This object has the value of notApplicable(1) when

                cefcPowerRedundancyOperMode of the instance does not

                have the value of nonRedundant(4).

                The other values explain the reason why 

                cefcPowerRedundancyOperMode is nonRedundant(4), e.g.

                unknown(2)             the reason is not identified.

                singleSupply(3)        There is only one power supply

                                       in the group.

                mismatchedSupplies(4)  There are more than one power

                                       supplies in the groups. However

                                       they are mismatched and can not

                                       work redundantly.

                supplyError(5)         Some power supply or supplies

                                       does or do not working properly.

                .. data:: notApplicable = 1

                .. data:: unknown = 2

                .. data:: singleSupply = 3

                .. data:: mismatchedSupplies = 4

                .. data:: supplyError = 5

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                unknown = Enum.YLeaf(2, "unknown")

                singleSupply = Enum.YLeaf(3, "singleSupply")

                mismatchedSupplies = Enum.YLeaf(4, "mismatchedSupplies")

                supplyError = Enum.YLeaf(5, "supplyError")



    class Cefcfrupowerstatustable(Entity):
        """
        This table lists the power\-related administrative status
        and operational status of the manageable components
        in the system.
        
        .. attribute:: cefcfrupowerstatusentry
        
        	An cefcFRUPowerStatusTable entry lists the desired administrative status, the operational status of the  power manageable component, and the current required by  the component for operation.  Entries are created by the agent at system power\-up or  the insertion of the component.  Entries are deleted by the agent at the removal of the component.  Only components with power control are listed in the  table
        	**type**\: list of  		 :py:class:`Cefcfrupowerstatusentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable.Cefcfrupowerstatusentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable, self).__init__()

            self.yang_name = "cefcFRUPowerStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcFRUPowerStatusEntry", ("cefcfrupowerstatusentry", CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable.Cefcfrupowerstatusentry))])
            self._leafs = OrderedDict()

            self.cefcfrupowerstatusentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerStatusTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable, [], name, value)


        class Cefcfrupowerstatusentry(Entity):
            """
            An cefcFRUPowerStatusTable entry lists the desired
            administrative status, the operational status of the 
            power manageable component, and the current required by 
            the component for operation.
            
            Entries are created by the agent at system power\-up or 
            the insertion of the component.  Entries are deleted by
            the agent at the removal of the component.
            
            Only components with power control are listed in the 
            table.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfrupoweradminstatus
            
            	Administratively desired FRU power state
            	**type**\:  :py:class:`PowerAdminType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PowerAdminType>`
            
            .. attribute:: cefcfrupoweroperstatus
            
            	Operational FRU power state
            	**type**\:  :py:class:`PowerOperType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PowerOperType>`
            
            .. attribute:: cefcfrucurrent
            
            	Current supplied by the FRU (positive values) or current required to operate the FRU (negative values)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrupowercapability
            
            	This object indicates the set of supported power capabilities of the FRU.  realTimeCurrent(0) \-     cefcFRURealTimeCurrent is supported by the FRU
            	**type**\:  :py:class:`Cefcfrupowercapability <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable.Cefcfrupowerstatusentry.Cefcfrupowercapability>`
            
            .. attribute:: cefcfrurealtimecurrent
            
            	This object indicates the realtime value of current supplied by the FRU (positive values) or the realtime value of current drawn by the FRU (negative values)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable.Cefcfrupowerstatusentry, self).__init__()

                self.yang_name = "cefcFRUPowerStatusEntry"
                self.yang_parent_name = "cefcFRUPowerStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcfrupoweradminstatus', YLeaf(YType.enumeration, 'cefcFRUPowerAdminStatus')),
                    ('cefcfrupoweroperstatus', YLeaf(YType.enumeration, 'cefcFRUPowerOperStatus')),
                    ('cefcfrucurrent', YLeaf(YType.int32, 'cefcFRUCurrent')),
                    ('cefcfrupowercapability', YLeaf(YType.bits, 'cefcFRUPowerCapability')),
                    ('cefcfrurealtimecurrent', YLeaf(YType.int32, 'cefcFRURealTimeCurrent')),
                ])
                self.entphysicalindex = None
                self.cefcfrupoweradminstatus = None
                self.cefcfrupoweroperstatus = None
                self.cefcfrucurrent = None
                self.cefcfrupowercapability = Bits()
                self.cefcfrurealtimecurrent = None
                self._segment_path = lambda: "cefcFRUPowerStatusEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupowerstatustable.Cefcfrupowerstatusentry, ['entphysicalindex', 'cefcfrupoweradminstatus', 'cefcfrupoweroperstatus', 'cefcfrucurrent', 'cefcfrupowercapability', 'cefcfrurealtimecurrent'], name, value)


    class Cefcfrupowersupplyvaluetable(Entity):
        """
        This table lists the power capacity of a power FRU in the
        system if it provides variable power. Power supplies usually
        provide either system or inline power. They cannot be 
        controlled by software to dictate how they distribute power.
        We can also have what are known as variable power supplies.
        They can provide both system and inline power and can be 
        varied within hardware defined ranges for system and inline
        limited by a total maximum combined output. They could be
        configured by the user via CLI or SNMP or be controlled by
        software internally.
        This table supplements the information in the
        cefcFRUPowerStatusTable for power supply FRUs. The 
        cefcFRUCurrent attribute in that table provides the overall
        current the power supply FRU can provide while this table 
        gives us the individual contribution towards system and 
        inline power.
        
        .. attribute:: cefcfrupowersupplyvalueentry
        
        	An cefcFRUPowerSupplyValueTable entry lists the current provided by the FRU for operation.  Entries are created by the agent at system power\-up or  FRU insertion.  Entries are deleted by the agent at FRU removal.  Only power supply FRUs are listed in the table
        	**type**\: list of  		 :py:class:`Cefcfrupowersupplyvalueentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyValueTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcFRUPowerSupplyValueEntry", ("cefcfrupowersupplyvalueentry", CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry))])
            self._leafs = OrderedDict()

            self.cefcfrupowersupplyvalueentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerSupplyValueTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable, [], name, value)


        class Cefcfrupowersupplyvalueentry(Entity):
            """
            An cefcFRUPowerSupplyValueTable entry lists the current
            provided by the FRU for operation.
            
            Entries are created by the agent at system power\-up or 
            FRU insertion.  Entries are deleted by the agent at FRU
            removal.
            
            Only power supply FRUs are listed in the table.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfrutotalsystemcurrent
            
            	Total current that could be supplied by the FRU (positive values) for system operations
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrudrawnsystemcurrent
            
            	Amount of current drawn by the FRU's in the system towards system operations from this FRU
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrutotalinlinecurrent
            
            	Total current supplied by the FRU (positive values) for inline operations
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrudrawninlinecurrent
            
            	Amount of current that is being drawn from this FRU for inline operation
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyValueEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcfrutotalsystemcurrent', YLeaf(YType.int32, 'cefcFRUTotalSystemCurrent')),
                    ('cefcfrudrawnsystemcurrent', YLeaf(YType.int32, 'cefcFRUDrawnSystemCurrent')),
                    ('cefcfrutotalinlinecurrent', YLeaf(YType.int32, 'cefcFRUTotalInlineCurrent')),
                    ('cefcfrudrawninlinecurrent', YLeaf(YType.int32, 'cefcFRUDrawnInlineCurrent')),
                ])
                self.entphysicalindex = None
                self.cefcfrutotalsystemcurrent = None
                self.cefcfrudrawnsystemcurrent = None
                self.cefcfrutotalinlinecurrent = None
                self.cefcfrudrawninlinecurrent = None
                self._segment_path = lambda: "cefcFRUPowerSupplyValueEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyValueTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry, ['entphysicalindex', 'cefcfrutotalsystemcurrent', 'cefcfrudrawnsystemcurrent', 'cefcfrutotalinlinecurrent', 'cefcfrudrawninlinecurrent'], name, value)


    class Cefcmoduletable(Entity):
        """
        A cefcModuleTable entry lists the operational and
        administrative status information for ENTITY\-MIB
        entPhysicalTable entries for manageable components
        of type PhysicalClass module(9).
        
        .. attribute:: cefcmoduleentry
        
        	A cefcModuleStatusTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components  of type PhysicalClass module(9).  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of  		 :py:class:`Cefcmoduleentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmoduletable.Cefcmoduleentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcmoduletable, self).__init__()

            self.yang_name = "cefcModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcModuleEntry", ("cefcmoduleentry", CISCOENTITYFRUCONTROLMIB.Cefcmoduletable.Cefcmoduleentry))])
            self._leafs = OrderedDict()

            self.cefcmoduleentry = YList(self)
            self._segment_path = lambda: "cefcModuleTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmoduletable, [], name, value)


        class Cefcmoduleentry(Entity):
            """
            A cefcModuleStatusTable entry lists the operational and
            administrative status information for ENTITY\-MIB
            entPhysicalTable entries for manageable components 
            of type PhysicalClass module(9).
            
            Entries are created by the agent at the system power\-up or
            module insertion.
            
            Entries are deleted by the agent upon module removal.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmoduleadminstatus
            
            	This object provides administrative control of the module
            	**type**\:  :py:class:`ModuleAdminType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleAdminType>`
            
            .. attribute:: cefcmoduleoperstatus
            
            	This object shows the module's operational state
            	**type**\:  :py:class:`ModuleOperType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleOperType>`
            
            .. attribute:: cefcmoduleresetreason
            
            	This object identifies the reason for the last reset performed on the module
            	**type**\:  :py:class:`ModuleResetReasonType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleResetReasonType>`
            
            .. attribute:: cefcmodulestatuslastchangetime
            
            	The value of sysUpTime at the time the cefcModuleOperStatus is changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmodulelastclearconfigtime
            
            	The value of sysUpTime when the configuration was most recently cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmoduleresetreasondescription
            
            	A description qualifying the module reset reason specified in cefcModuleResetReason.   Examples\:   command xyz                 missing task   switch over   watchdog timeout       etc.  cefcModuleResetReasonDescription is for display purposes only. NMS applications must not parse
            	**type**\: str
            
            .. attribute:: cefcmodulestatechangereasondescr
            
            	This object displays human\-readable textual string which describes the cause of the last state change of the module. This object contains zero length string if no meaningful reason could be provided.  Examples\: 'Invalid software version' 'Software download failed' 'Software version mismatch' 'Module is in standby state' etc.  This object is for display purposes only. NMS applications must not parse this object and take any decision based on its value
            	**type**\: str
            
            .. attribute:: cefcmoduleuptime
            
            	This object provides the up time for the module since it was last re\-initialized.  This object is not persistent; if a module reset, restart, power off, the up time starts from zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcmoduletable.Cefcmoduleentry, self).__init__()

                self.yang_name = "cefcModuleEntry"
                self.yang_parent_name = "cefcModuleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcmoduleadminstatus', YLeaf(YType.enumeration, 'cefcModuleAdminStatus')),
                    ('cefcmoduleoperstatus', YLeaf(YType.enumeration, 'cefcModuleOperStatus')),
                    ('cefcmoduleresetreason', YLeaf(YType.enumeration, 'cefcModuleResetReason')),
                    ('cefcmodulestatuslastchangetime', YLeaf(YType.uint32, 'cefcModuleStatusLastChangeTime')),
                    ('cefcmodulelastclearconfigtime', YLeaf(YType.uint32, 'cefcModuleLastClearConfigTime')),
                    ('cefcmoduleresetreasondescription', YLeaf(YType.str, 'cefcModuleResetReasonDescription')),
                    ('cefcmodulestatechangereasondescr', YLeaf(YType.str, 'cefcModuleStateChangeReasonDescr')),
                    ('cefcmoduleuptime', YLeaf(YType.uint32, 'cefcModuleUpTime')),
                ])
                self.entphysicalindex = None
                self.cefcmoduleadminstatus = None
                self.cefcmoduleoperstatus = None
                self.cefcmoduleresetreason = None
                self.cefcmodulestatuslastchangetime = None
                self.cefcmodulelastclearconfigtime = None
                self.cefcmoduleresetreasondescription = None
                self.cefcmodulestatechangereasondescr = None
                self.cefcmoduleuptime = None
                self._segment_path = lambda: "cefcModuleEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmoduletable.Cefcmoduleentry, ['entphysicalindex', 'cefcmoduleadminstatus', 'cefcmoduleoperstatus', 'cefcmoduleresetreason', 'cefcmodulestatuslastchangetime', 'cefcmodulelastclearconfigtime', 'cefcmoduleresetreasondescription', 'cefcmodulestatechangereasondescr', 'cefcmoduleuptime'], name, value)


    class Cefcintellimoduletable(Entity):
        """
        This table sparsely augments the
        cefcModuleTable (i.e., every row in
        this table corresponds to a row in
        the cefcModuleTable but not necessarily
        vice\-versa).
        
        A cefcIntelliModuleTable entry lists the
        information specific to intelligent
        modules which cannot be provided by the
        cefcModuleTable.
        
        .. attribute:: cefcintellimoduleentry
        
        	A cefcIntelliModuleTable entry lists the information specific to an intelligent module which cannot be provided by this module's corresponding instance in the cefcModuleTable. Only an intelligent module with Internet address configured has its entry here.  An entry of this table is created if an  intelligent module is detected by the  managed system and its management Internet address is configured on the intelligent  module.  An entry of this table is deleted if the  removal of Internet address configuration of  this module or the module itself
        	**type**\: list of  		 :py:class:`Cefcintellimoduleentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable.Cefcintellimoduleentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable, self).__init__()

            self.yang_name = "cefcIntelliModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcIntelliModuleEntry", ("cefcintellimoduleentry", CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable.Cefcintellimoduleentry))])
            self._leafs = OrderedDict()

            self.cefcintellimoduleentry = YList(self)
            self._segment_path = lambda: "cefcIntelliModuleTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable, [], name, value)


        class Cefcintellimoduleentry(Entity):
            """
            A cefcIntelliModuleTable entry lists the
            information specific to an intelligent
            module which cannot be provided by
            this module's corresponding instance in
            the cefcModuleTable. Only an intelligent
            module with Internet address configured has
            its entry here.
            
            An entry of this table is created if an 
            intelligent module is detected by the 
            managed system and its management Internet
            address is configured on the intelligent 
            module.
            
            An entry of this table is deleted if the 
            removal of Internet address configuration of 
            this module or the module itself.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcintellimoduleipaddrtype
            
            	The type of Internet address by which the intelligent module is reachable
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cefcintellimoduleipaddr
            
            	The Internet address configured for the intelligent module. The type of this address is  determined by the value of the object  cefcIntelliModuleIPAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable.Cefcintellimoduleentry, self).__init__()

                self.yang_name = "cefcIntelliModuleEntry"
                self.yang_parent_name = "cefcIntelliModuleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcintellimoduleipaddrtype', YLeaf(YType.enumeration, 'cefcIntelliModuleIPAddrType')),
                    ('cefcintellimoduleipaddr', YLeaf(YType.str, 'cefcIntelliModuleIPAddr')),
                ])
                self.entphysicalindex = None
                self.cefcintellimoduleipaddrtype = None
                self.cefcintellimoduleipaddr = None
                self._segment_path = lambda: "cefcIntelliModuleEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcIntelliModuleTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcintellimoduletable.Cefcintellimoduleentry, ['entphysicalindex', 'cefcintellimoduleipaddrtype', 'cefcintellimoduleipaddr'], name, value)


    class Cefcmodulelocalswitchingtable(Entity):
        """
        This table sparsely augments the cefcModuleTable
        (i.e., every row in this table corresponds to a row in
        the cefcModuleTable but not necessarily vice\-versa).
        
        A cefcModuleLocalSwitchingTable entry lists the
        information specific to local switching capable
        modules which cannot be provided by the
        cefcModuleTable.
        
        .. attribute:: cefcmodulelocalswitchingentry
        
        	A cefcModuleLocalSwitchingTable entry lists the information specific to a local switching capable module which cannot be provided by this module's corresponding instance in the cefcModuleTable. Only a module which is capable of local switching has its entry here.  An entry of this table is created if a module which is capable of local switching is detected by the managed system.  An entry of this table is deleted if the removal of this module
        	**type**\: list of  		 :py:class:`Cefcmodulelocalswitchingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable, self).__init__()

            self.yang_name = "cefcModuleLocalSwitchingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcModuleLocalSwitchingEntry", ("cefcmodulelocalswitchingentry", CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry))])
            self._leafs = OrderedDict()

            self.cefcmodulelocalswitchingentry = YList(self)
            self._segment_path = lambda: "cefcModuleLocalSwitchingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable, [], name, value)


        class Cefcmodulelocalswitchingentry(Entity):
            """
            A cefcModuleLocalSwitchingTable entry lists the
            information specific to a local switching capable
            module which cannot be provided by this module's
            corresponding instance in the cefcModuleTable.
            Only a module which is capable of local switching
            has its entry here.
            
            An entry of this table is created if a module which
            is capable of local switching is detected by the
            managed system.
            
            An entry of this table is deleted if the
            removal of this module.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmodulelocalswitchingmode
            
            	This object specifies the mode of local switching.  enabled(1)  \- local switching is enabled. disabled(2) \- local switching is disabled
            	**type**\:  :py:class:`Cefcmodulelocalswitchingmode <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry.Cefcmodulelocalswitchingmode>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry, self).__init__()

                self.yang_name = "cefcModuleLocalSwitchingEntry"
                self.yang_parent_name = "cefcModuleLocalSwitchingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcmodulelocalswitchingmode', YLeaf(YType.enumeration, 'cefcModuleLocalSwitchingMode')),
                ])
                self.entphysicalindex = None
                self.cefcmodulelocalswitchingmode = None
                self._segment_path = lambda: "cefcModuleLocalSwitchingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleLocalSwitchingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry, ['entphysicalindex', 'cefcmodulelocalswitchingmode'], name, value)

            class Cefcmodulelocalswitchingmode(Enum):
                """
                Cefcmodulelocalswitchingmode (Enum Class)

                This object specifies the mode of local switching.

                enabled(1)  \- local switching is enabled.

                disabled(2) \- local switching is disabled.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")



    class Cefcfantraystatustable(Entity):
        """
        This table contains the operational status information
        for all ENTITY\-MIB entPhysicalTable entries which have 
        an entPhysicalClass of 'fan'; specifically, all  
        entPhysicalTable entries which represent either\: one 
        physical fan, or a single physical 'fan tray' which is a
        manufactured (inseparable in the field) combination of 
        multiple fans.
        
        .. attribute:: cefcfantraystatusentry
        
        	An cefcFanTrayStatusTable entry lists the operational status information for the ENTITY\-MIB entPhysicalTable  entry which is identified by the value of entPhysicalIndex. The value of entPhysicalClass for the identified entry will be 'fan', and the represented physical entity will be  either\: one physical fan, or a single physical 'fan tray'  which is a manufactured (inseparable in the field)  combination of multiple fans.  Entries are created by the agent at system power\-up or  fan or fan tray insertion.  Entries are deleted  by the agent at the fan or fan tray removal
        	**type**\: list of  		 :py:class:`Cefcfantraystatusentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable.Cefcfantraystatusentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable, self).__init__()

            self.yang_name = "cefcFanTrayStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcFanTrayStatusEntry", ("cefcfantraystatusentry", CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable.Cefcfantraystatusentry))])
            self._leafs = OrderedDict()

            self.cefcfantraystatusentry = YList(self)
            self._segment_path = lambda: "cefcFanTrayStatusTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable, [], name, value)


        class Cefcfantraystatusentry(Entity):
            """
            An cefcFanTrayStatusTable entry lists the operational
            status information for the ENTITY\-MIB entPhysicalTable 
            entry which is identified by the value of entPhysicalIndex.
            The value of entPhysicalClass for the identified entry will
            be 'fan', and the represented physical entity will be 
            either\: one physical fan, or a single physical 'fan tray' 
            which is a manufactured (inseparable in the field) 
            combination of multiple fans.
            
            Entries are created by the agent at system power\-up or 
            fan or fan tray insertion.  Entries are deleted 
            by the agent at the fan or fan tray removal.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfantrayoperstatus
            
            	The operational state of the fan or fan tray. unknown(1) \- unknown. up(2) \- powered on. down(3) \- powered down. warning(4) \- partial failure, needs replacement               as soon as possible
            	**type**\:  :py:class:`Cefcfantrayoperstatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable.Cefcfantraystatusentry.Cefcfantrayoperstatus>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable.Cefcfantraystatusentry, self).__init__()

                self.yang_name = "cefcFanTrayStatusEntry"
                self.yang_parent_name = "cefcFanTrayStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcfantrayoperstatus', YLeaf(YType.enumeration, 'cefcFanTrayOperStatus')),
                ])
                self.entphysicalindex = None
                self.cefcfantrayoperstatus = None
                self._segment_path = lambda: "cefcFanTrayStatusEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanTrayStatusTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfantraystatustable.Cefcfantraystatusentry, ['entphysicalindex', 'cefcfantrayoperstatus'], name, value)

            class Cefcfantrayoperstatus(Enum):
                """
                Cefcfantrayoperstatus (Enum Class)

                The operational state of the fan or fan tray.

                unknown(1) \- unknown.

                up(2) \- powered on.

                down(3) \- powered down.

                warning(4) \- partial failure, needs replacement 

                             as soon as possible.

                .. data:: unknown = 1

                .. data:: up = 2

                .. data:: down = 3

                .. data:: warning = 4

                """

                unknown = Enum.YLeaf(1, "unknown")

                up = Enum.YLeaf(2, "up")

                down = Enum.YLeaf(3, "down")

                warning = Enum.YLeaf(4, "warning")



    class Cefcphysicaltable(Entity):
        """
        This table contains one row per physical entity.
        
        .. attribute:: cefcphysicalentry
        
        	Information about a particular physical entity
        	**type**\: list of  		 :py:class:`Cefcphysicalentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable.Cefcphysicalentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable, self).__init__()

            self.yang_name = "cefcPhysicalTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcPhysicalEntry", ("cefcphysicalentry", CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable.Cefcphysicalentry))])
            self._leafs = OrderedDict()

            self.cefcphysicalentry = YList(self)
            self._segment_path = lambda: "cefcPhysicalTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable, [], name, value)


        class Cefcphysicalentry(Entity):
            """
            Information about a particular physical entity.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcphysicalstatus
            
            	The status of this physical entity. other(1) \- the status is not any of the listed below. supported(2) \- this entity is supported. unsupported(3) \- this entity is unsupported. incompatible(4) \- this entity is incompatible. It would be unsupported(3), if the ID read from Serial EPROM is not supported. It would be incompatible(4), if in the present configuration this FRU is not supported
            	**type**\:  :py:class:`Cefcphysicalstatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable.Cefcphysicalentry.Cefcphysicalstatus>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable.Cefcphysicalentry, self).__init__()

                self.yang_name = "cefcPhysicalEntry"
                self.yang_parent_name = "cefcPhysicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcphysicalstatus', YLeaf(YType.enumeration, 'cefcPhysicalStatus')),
                ])
                self.entphysicalindex = None
                self.cefcphysicalstatus = None
                self._segment_path = lambda: "cefcPhysicalEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPhysicalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcphysicaltable.Cefcphysicalentry, ['entphysicalindex', 'cefcphysicalstatus'], name, value)

            class Cefcphysicalstatus(Enum):
                """
                Cefcphysicalstatus (Enum Class)

                The status of this physical entity.

                other(1) \- the status is not any of the listed below.

                supported(2) \- this entity is supported.

                unsupported(3) \- this entity is unsupported.

                incompatible(4) \- this entity is incompatible.

                It would be unsupported(3), if the ID read from Serial

                EPROM is not supported. It would be incompatible(4), if

                in the present configuration this FRU is not supported.

                .. data:: other = 1

                .. data:: supported = 2

                .. data:: unsupported = 3

                .. data:: incompatible = 4

                """

                other = Enum.YLeaf(1, "other")

                supported = Enum.YLeaf(2, "supported")

                unsupported = Enum.YLeaf(3, "unsupported")

                incompatible = Enum.YLeaf(4, "incompatible")



    class Cefcpowersupplyinputtable(Entity):
        """
        This table contains the power input information
        for all the power supplies that have entPhysicalTable
        entries with 'powerSupply' in the entPhysicalClass. 
        
        The entries are created by the agent at the system
        power\-up or power supply insertion.
        
        Entries are deleted by the agent upon power supply
        removal.
        
        The number of entries is determined by the number of
        power supplies and number of power inputs on the power 
        supply.
        
        .. attribute:: cefcpowersupplyinputentry
        
        	An entry containing power input management information applicable to a particular power supply and input
        	**type**\: list of  		 :py:class:`Cefcpowersupplyinputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable, self).__init__()

            self.yang_name = "cefcPowerSupplyInputTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcPowerSupplyInputEntry", ("cefcpowersupplyinputentry", CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry))])
            self._leafs = OrderedDict()

            self.cefcpowersupplyinputentry = YList(self)
            self._segment_path = lambda: "cefcPowerSupplyInputTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable, [], name, value)


        class Cefcpowersupplyinputentry(Entity):
            """
            An entry containing power input management information
            applicable to a particular power supply and input.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcpowersupplyinputindex  (key)
            
            	A unique value, greater than zero, for each input on a power supply
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcpowersupplyinputtype
            
            	The type of an input power detected on the power supply.  unknown(1)\: No input power is detected.  acLow(2)\: Lower rating AC input power is detected.  acHigh(3)\: Higher rating AC input power is detected.  dcLow(4)\: Lower rating DC input power is detected.  dcHigh(5)\: Higher rating DC input power is detected
            	**type**\:  :py:class:`Cefcpowersupplyinputtype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry.Cefcpowersupplyinputtype>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry, self).__init__()

                self.yang_name = "cefcPowerSupplyInputEntry"
                self.yang_parent_name = "cefcPowerSupplyInputTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefcpowersupplyinputindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcpowersupplyinputindex', YLeaf(YType.uint32, 'cefcPowerSupplyInputIndex')),
                    ('cefcpowersupplyinputtype', YLeaf(YType.enumeration, 'cefcPowerSupplyInputType')),
                ])
                self.entphysicalindex = None
                self.cefcpowersupplyinputindex = None
                self.cefcpowersupplyinputtype = None
                self._segment_path = lambda: "cefcPowerSupplyInputEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefcPowerSupplyInputIndex='" + str(self.cefcpowersupplyinputindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPowerSupplyInputTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry, ['entphysicalindex', 'cefcpowersupplyinputindex', 'cefcpowersupplyinputtype'], name, value)

            class Cefcpowersupplyinputtype(Enum):
                """
                Cefcpowersupplyinputtype (Enum Class)

                The type of an input power detected on the power

                supply.

                unknown(1)\: No input power is detected.

                acLow(2)\: Lower rating AC input power is detected.

                acHigh(3)\: Higher rating AC input power is detected.

                dcLow(4)\: Lower rating DC input power is detected.

                dcHigh(5)\: Higher rating DC input power is detected.

                .. data:: unknown = 1

                .. data:: acLow = 2

                .. data:: acHigh = 3

                .. data:: dcLow = 4

                .. data:: dcHigh = 5

                """

                unknown = Enum.YLeaf(1, "unknown")

                acLow = Enum.YLeaf(2, "acLow")

                acHigh = Enum.YLeaf(3, "acHigh")

                dcLow = Enum.YLeaf(4, "dcLow")

                dcHigh = Enum.YLeaf(5, "dcHigh")



    class Cefcpowersupplyoutputtable(Entity):
        """
        This table contains a list of possible output
        mode for the power supplies, whose ENTITY\-MIB
        entPhysicalTable entries have an entPhysicalClass
        of 'powerSupply'. It also indicate which mode
        is the operational mode within the system.
        
        .. attribute:: cefcpowersupplyoutputentry
        
        	A cefcPowerSupplyOutputTable entry lists the power output capacity and its operational status for manageable components of type PhysicalClass 'powerSupply'.  Entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries of a power supply is determined by the power supply
        	**type**\: list of  		 :py:class:`Cefcpowersupplyoutputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable, self).__init__()

            self.yang_name = "cefcPowerSupplyOutputTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcPowerSupplyOutputEntry", ("cefcpowersupplyoutputentry", CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry))])
            self._leafs = OrderedDict()

            self.cefcpowersupplyoutputentry = YList(self)
            self._segment_path = lambda: "cefcPowerSupplyOutputTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable, [], name, value)


        class Cefcpowersupplyoutputentry(Entity):
            """
            A cefcPowerSupplyOutputTable entry lists the
            power output capacity and its operational status
            for manageable components of type PhysicalClass
            'powerSupply'.
            
            Entries are created by the agent at the system
            power\-up or power supply insertion.
            
            Entries are deleted by the agent upon power supply
            removal.
            
            The number of entries of a power supply is determined
            by the power supply.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcpsoutputmodeindex  (key)
            
            	A unique value, greater than zero, for each possible output mode on a power supply
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcpsoutputmodecurrent
            
            	The output capacity of the power supply
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcpsoutputmodeinoperation
            
            	A value of 'true' indicates that this mode is the operational mode of the power supply output capacity.  A value of 'false' indicates that this mode is not the operational mode of the power supply output capacity.  For a given power supply's entPhysicalIndex,  at most one instance of this object can have the value of true(1)
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry, self).__init__()

                self.yang_name = "cefcPowerSupplyOutputEntry"
                self.yang_parent_name = "cefcPowerSupplyOutputTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefcpsoutputmodeindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcpsoutputmodeindex', YLeaf(YType.uint32, 'cefcPSOutputModeIndex')),
                    ('cefcpsoutputmodecurrent', YLeaf(YType.int32, 'cefcPSOutputModeCurrent')),
                    ('cefcpsoutputmodeinoperation', YLeaf(YType.boolean, 'cefcPSOutputModeInOperation')),
                ])
                self.entphysicalindex = None
                self.cefcpsoutputmodeindex = None
                self.cefcpsoutputmodecurrent = None
                self.cefcpsoutputmodeinoperation = None
                self._segment_path = lambda: "cefcPowerSupplyOutputEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefcPSOutputModeIndex='" + str(self.cefcpsoutputmodeindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPowerSupplyOutputTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry, ['entphysicalindex', 'cefcpsoutputmodeindex', 'cefcpsoutputmodecurrent', 'cefcpsoutputmodeinoperation'], name, value)


    class Cefcchassiscoolingtable(Entity):
        """
        This table contains the cooling capacity
        information of the chassis whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'chassis'.
        
        .. attribute:: cefcchassiscoolingentry
        
        	A cefcChassisCoolingEntry lists the maximum cooling capacity that could be provided  for one slot on the manageable components of type PhysicalClass 'chassis'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of  		 :py:class:`Cefcchassiscoolingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable.Cefcchassiscoolingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable, self).__init__()

            self.yang_name = "cefcChassisCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcChassisCoolingEntry", ("cefcchassiscoolingentry", CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable.Cefcchassiscoolingentry))])
            self._leafs = OrderedDict()

            self.cefcchassiscoolingentry = YList(self)
            self._segment_path = lambda: "cefcChassisCoolingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable, [], name, value)


        class Cefcchassiscoolingentry(Entity):
            """
            A cefcChassisCoolingEntry lists the maximum
            cooling capacity that could be provided 
            for one slot on the manageable components of type
            PhysicalClass 'chassis'.
            
            Entries are created by the agent if the corresponding
            entry is created in ENTITY\-MIB entPhysicalTable.
            
            Entries are deleted by the agent if the corresponding
            entry is deleted in ENTITY\-MIB entPhysicalTable.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcchassisperslotcoolingcap
            
            	The maximum cooling capacity that could be provided for any slot in this chassis.  The default unit of the cooling capacity is 'cfm', if cefcChassisPerSlotCoolingUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcchassisperslotcoolingunit
            
            	The unit of the maximum cooling capacity for any slot in this chassis
            	**type**\:  :py:class:`FRUCoolingUnit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable.Cefcchassiscoolingentry, self).__init__()

                self.yang_name = "cefcChassisCoolingEntry"
                self.yang_parent_name = "cefcChassisCoolingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcchassisperslotcoolingcap', YLeaf(YType.uint32, 'cefcChassisPerSlotCoolingCap')),
                    ('cefcchassisperslotcoolingunit', YLeaf(YType.enumeration, 'cefcChassisPerSlotCoolingUnit')),
                ])
                self.entphysicalindex = None
                self.cefcchassisperslotcoolingcap = None
                self.cefcchassisperslotcoolingunit = None
                self._segment_path = lambda: "cefcChassisCoolingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcChassisCoolingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcchassiscoolingtable.Cefcchassiscoolingentry, ['entphysicalindex', 'cefcchassisperslotcoolingcap', 'cefcchassisperslotcoolingunit'], name, value)


    class Cefcfancoolingtable(Entity):
        """
        This table contains the cooling capacity
        information of the fans whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingentry
        
        	A cefcFanCoolingEntry lists the cooling capacity that is provided by the  manageable components of type PhysicalClass  'fan'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of  		 :py:class:`Cefcfancoolingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable.Cefcfancoolingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable, self).__init__()

            self.yang_name = "cefcFanCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcFanCoolingEntry", ("cefcfancoolingentry", CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable.Cefcfancoolingentry))])
            self._leafs = OrderedDict()

            self.cefcfancoolingentry = YList(self)
            self._segment_path = lambda: "cefcFanCoolingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable, [], name, value)


        class Cefcfancoolingentry(Entity):
            """
            A cefcFanCoolingEntry lists the cooling
            capacity that is provided by the 
            manageable components of type PhysicalClass 
            'fan'.
            
            Entries are created by the agent if the corresponding
            entry is created in ENTITY\-MIB entPhysicalTable.
            
            Entries are deleted by the agent if the corresponding
            entry is deleted in ENTITY\-MIB entPhysicalTable.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfancoolingcapacity
            
            	The cooling capacity that is provided by this fan.  The default unit of the fan cooling capacity is 'cfm', if cefcFanCoolingCapacityUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfancoolingcapacityunit
            
            	The unit of the fan cooling capacity
            	**type**\:  :py:class:`FRUCoolingUnit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable.Cefcfancoolingentry, self).__init__()

                self.yang_name = "cefcFanCoolingEntry"
                self.yang_parent_name = "cefcFanCoolingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcfancoolingcapacity', YLeaf(YType.uint32, 'cefcFanCoolingCapacity')),
                    ('cefcfancoolingcapacityunit', YLeaf(YType.enumeration, 'cefcFanCoolingCapacityUnit')),
                ])
                self.entphysicalindex = None
                self.cefcfancoolingcapacity = None
                self.cefcfancoolingcapacityunit = None
                self._segment_path = lambda: "cefcFanCoolingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanCoolingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingtable.Cefcfancoolingentry, ['entphysicalindex', 'cefcfancoolingcapacity', 'cefcfancoolingcapacityunit'], name, value)


    class Cefcmodulecoolingtable(Entity):
        """
        This table contains the cooling requirement for
        all the manageable components of type entPhysicalClass
        'module'.
        
        .. attribute:: cefcmodulecoolingentry
        
        	A cefcModuleCoolingEntry lists the cooling requirement for a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of  		 :py:class:`Cefcmodulecoolingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable.Cefcmodulecoolingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable, self).__init__()

            self.yang_name = "cefcModuleCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcModuleCoolingEntry", ("cefcmodulecoolingentry", CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable.Cefcmodulecoolingentry))])
            self._leafs = OrderedDict()

            self.cefcmodulecoolingentry = YList(self)
            self._segment_path = lambda: "cefcModuleCoolingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable, [], name, value)


        class Cefcmodulecoolingentry(Entity):
            """
            A cefcModuleCoolingEntry lists the cooling
            requirement for a manageable components of type
            entPhysicalClass 'module'.
            
            Entries are created by the agent at the system
            power\-up or module insertion.
            
            Entries are deleted by the agent upon module
            removal.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmodulecooling
            
            	The cooling requirement of the module and its daughter cards.  The default unit of the module cooling requirement is 'cfm', if cefcModuleCoolingUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmodulecoolingunit
            
            	The unit of the cooling requirement of the module and its daughter cards
            	**type**\:  :py:class:`FRUCoolingUnit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable.Cefcmodulecoolingentry, self).__init__()

                self.yang_name = "cefcModuleCoolingEntry"
                self.yang_parent_name = "cefcModuleCoolingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcmodulecooling', YLeaf(YType.uint32, 'cefcModuleCooling')),
                    ('cefcmodulecoolingunit', YLeaf(YType.enumeration, 'cefcModuleCoolingUnit')),
                ])
                self.entphysicalindex = None
                self.cefcmodulecooling = None
                self.cefcmodulecoolingunit = None
                self._segment_path = lambda: "cefcModuleCoolingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleCoolingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmodulecoolingtable.Cefcmodulecoolingentry, ['entphysicalindex', 'cefcmodulecooling', 'cefcmodulecoolingunit'], name, value)


    class Cefcfancoolingcaptable(Entity):
        """
        This table contains a list of the possible cooling
        capacity modes and properties of the fans, whose 
        ENTITY\-MIB entPhysicalTable entries have an 
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingcapentry
        
        	A cefcFanCoolingCapacityEntry lists the cooling capacity mode of a manageable components of type entPhysicalClass 'fan'. It also lists the corresponding cooling capacity provided and the power consumed by the fan on this mode.   Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of  		 :py:class:`Cefcfancoolingcapentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable.Cefcfancoolingcapentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable, self).__init__()

            self.yang_name = "cefcFanCoolingCapTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcFanCoolingCapEntry", ("cefcfancoolingcapentry", CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable.Cefcfancoolingcapentry))])
            self._leafs = OrderedDict()

            self.cefcfancoolingcapentry = YList(self)
            self._segment_path = lambda: "cefcFanCoolingCapTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable, [], name, value)


        class Cefcfancoolingcapentry(Entity):
            """
            A cefcFanCoolingCapacityEntry lists the cooling
            capacity mode of a manageable components of type
            entPhysicalClass 'fan'. It also lists the corresponding
            cooling capacity provided and the power consumed
            by the fan on this mode.
            
            
            Entries are created by the agent if the corresponding
            entry is created in ENTITY\-MIB entPhysicalTable.
            
            Entries are deleted by the agent if the corresponding
            entry is deleted in ENTITY\-MIB entPhysicalTable.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfancoolingcapindex  (key)
            
            	An arbitrary value that uniquely identifies a cooling capacity mode for a fan
            	**type**\: int
            
            	**range:** 1..4095
            
            .. attribute:: cefcfancoolingcapmodedescr
            
            	A textual description of the cooling capacity mode of the fan
            	**type**\: str
            
            .. attribute:: cefcfancoolingcapcapacity
            
            	The cooling capacity that could be provided when the fan is operating in this mode.  The default unit of the cooling capacity is 'cfm', if cefcFanCoolingCapCapacityUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfancoolingcapcurrent
            
            	The power consumption of the fan when operating in in this mode
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfancoolingcapcapacityunit
            
            	The unit of the fan cooling capacity when operating in this mode
            	**type**\:  :py:class:`FRUCoolingUnit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable.Cefcfancoolingcapentry, self).__init__()

                self.yang_name = "cefcFanCoolingCapEntry"
                self.yang_parent_name = "cefcFanCoolingCapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefcfancoolingcapindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcfancoolingcapindex', YLeaf(YType.uint32, 'cefcFanCoolingCapIndex')),
                    ('cefcfancoolingcapmodedescr', YLeaf(YType.str, 'cefcFanCoolingCapModeDescr')),
                    ('cefcfancoolingcapcapacity', YLeaf(YType.uint32, 'cefcFanCoolingCapCapacity')),
                    ('cefcfancoolingcapcurrent', YLeaf(YType.int32, 'cefcFanCoolingCapCurrent')),
                    ('cefcfancoolingcapcapacityunit', YLeaf(YType.enumeration, 'cefcFanCoolingCapCapacityUnit')),
                ])
                self.entphysicalindex = None
                self.cefcfancoolingcapindex = None
                self.cefcfancoolingcapmodedescr = None
                self.cefcfancoolingcapcapacity = None
                self.cefcfancoolingcapcurrent = None
                self.cefcfancoolingcapcapacityunit = None
                self._segment_path = lambda: "cefcFanCoolingCapEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefcFanCoolingCapIndex='" + str(self.cefcfancoolingcapindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanCoolingCapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcfancoolingcaptable.Cefcfancoolingcapentry, ['entphysicalindex', 'cefcfancoolingcapindex', 'cefcfancoolingcapmodedescr', 'cefcfancoolingcapcapacity', 'cefcfancoolingcapcurrent', 'cefcfancoolingcapcapacityunit'], name, value)


    class Cefcconnectorratingtable(Entity):
        """
        This table contains the connector power
        ratings of FRUs. 
        
        Only components with power connector rating 
        management are listed in this table.
        
        .. attribute:: cefcconnectorratingentry
        
        	A cefcConnectorRatingEntry lists the power connector rating information of a  component in the system.  An entry or entries are created by the agent when an physical entity with connector rating  management is added to the ENTITY\-MIB  entPhysicalTable. An entry is deleted  by the agent at the entity removal
        	**type**\: list of  		 :py:class:`Cefcconnectorratingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable.Cefcconnectorratingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable, self).__init__()

            self.yang_name = "cefcConnectorRatingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcConnectorRatingEntry", ("cefcconnectorratingentry", CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable.Cefcconnectorratingentry))])
            self._leafs = OrderedDict()

            self.cefcconnectorratingentry = YList(self)
            self._segment_path = lambda: "cefcConnectorRatingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable, [], name, value)


        class Cefcconnectorratingentry(Entity):
            """
            A cefcConnectorRatingEntry lists the
            power connector rating information of a 
            component in the system.
            
            An entry or entries are created by the agent
            when an physical entity with connector rating 
            management is added to the ENTITY\-MIB 
            entPhysicalTable. An entry is deleted 
            by the agent at the entity removal.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcconnectorrating
            
            	The maximum power that the component's connector can withdraw
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable.Cefcconnectorratingentry, self).__init__()

                self.yang_name = "cefcConnectorRatingEntry"
                self.yang_parent_name = "cefcConnectorRatingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcconnectorrating', YLeaf(YType.int32, 'cefcConnectorRating')),
                ])
                self.entphysicalindex = None
                self.cefcconnectorrating = None
                self._segment_path = lambda: "cefcConnectorRatingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcConnectorRatingTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcconnectorratingtable.Cefcconnectorratingentry, ['entphysicalindex', 'cefcconnectorrating'], name, value)


    class Cefcmodulepowerconsumptiontable(Entity):
        """
        This table contains the total power consumption
        information for modules whose ENTITY\-MIB 
        entPhysicalTable entries have an entPhysicalClass 
        of 'module'.
        
        .. attribute:: cefcmodulepowerconsumptionentry
        
        	A cefcModulePowerConsumptionEntry lists the total power consumption of a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of  		 :py:class:`Cefcmodulepowerconsumptionentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable, self).__init__()

            self.yang_name = "cefcModulePowerConsumptionTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefcModulePowerConsumptionEntry", ("cefcmodulepowerconsumptionentry", CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry))])
            self._leafs = OrderedDict()

            self.cefcmodulepowerconsumptionentry = YList(self)
            self._segment_path = lambda: "cefcModulePowerConsumptionTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable, [], name, value)


        class Cefcmodulepowerconsumptionentry(Entity):
            """
            A cefcModulePowerConsumptionEntry lists the total
            power consumption of a manageable components of type
            entPhysicalClass 'module'.
            
            Entries are created by the agent at the system
            power\-up or module insertion.
            
            Entries are deleted by the agent upon module
            removal.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmodulepowerconsumption
            
            	The combined power consumption to operate the module and its submodule(s) and inline\-power device(s)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry, self).__init__()

                self.yang_name = "cefcModulePowerConsumptionEntry"
                self.yang_parent_name = "cefcModulePowerConsumptionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefcmodulepowerconsumption', YLeaf(YType.int32, 'cefcModulePowerConsumption')),
                ])
                self.entphysicalindex = None
                self.cefcmodulepowerconsumption = None
                self._segment_path = lambda: "cefcModulePowerConsumptionEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModulePowerConsumptionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry, ['entphysicalindex', 'cefcmodulepowerconsumption'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOENTITYFRUCONTROLMIB()
        return self._top_entity

