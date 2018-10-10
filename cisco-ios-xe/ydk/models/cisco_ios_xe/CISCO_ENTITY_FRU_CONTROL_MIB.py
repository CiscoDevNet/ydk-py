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
    
    	
    	**type**\:  :py:class:`CefcFRUPower <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPower>`
    
    .. attribute:: cefcmibnotificationenables
    
    	
    	**type**\:  :py:class:`CefcMIBNotificationEnables <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables>`
    
    .. attribute:: cefcfrupowersupplygrouptable
    
    	This table lists the redundancy mode and the operational status of the power supply groups in the system
    	**type**\:  :py:class:`CefcFRUPowerSupplyGroupTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable>`
    
    .. attribute:: cefcfrupowerstatustable
    
    	This table lists the power\-related administrative status and operational status of the manageable components in the system
    	**type**\:  :py:class:`CefcFRUPowerStatusTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable>`
    
    .. attribute:: cefcfrupowersupplyvaluetable
    
    	This table lists the power capacity of a power FRU in the system if it provides variable power. Power supplies usually provide either system or inline power. They cannot be  controlled by software to dictate how they distribute power. We can also have what are known as variable power supplies. They can provide both system and inline power and can be  varied within hardware defined ranges for system and inline limited by a total maximum combined output. They could be configured by the user via CLI or SNMP or be controlled by software internally. This table supplements the information in the cefcFRUPowerStatusTable for power supply FRUs. The  cefcFRUCurrent attribute in that table provides the overall current the power supply FRU can provide while this table  gives us the individual contribution towards system and  inline power
    	**type**\:  :py:class:`CefcFRUPowerSupplyValueTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable>`
    
    .. attribute:: cefcmoduletable
    
    	A cefcModuleTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components of type PhysicalClass module(9)
    	**type**\:  :py:class:`CefcModuleTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleTable>`
    
    .. attribute:: cefcintellimoduletable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcIntelliModuleTable entry lists the information specific to intelligent modules which cannot be provided by the cefcModuleTable
    	**type**\:  :py:class:`CefcIntelliModuleTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable>`
    
    .. attribute:: cefcmodulelocalswitchingtable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcModuleLocalSwitchingTable entry lists the information specific to local switching capable modules which cannot be provided by the cefcModuleTable
    	**type**\:  :py:class:`CefcModuleLocalSwitchingTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable>`
    
    .. attribute:: cefcfantraystatustable
    
    	This table contains the operational status information for all ENTITY\-MIB entPhysicalTable entries which have  an entPhysicalClass of 'fan'; specifically, all   entPhysicalTable entries which represent either\: one  physical fan, or a single physical 'fan tray' which is a manufactured (inseparable in the field) combination of  multiple fans
    	**type**\:  :py:class:`CefcFanTrayStatusTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable>`
    
    .. attribute:: cefcphysicaltable
    
    	This table contains one row per physical entity
    	**type**\:  :py:class:`CefcPhysicalTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable>`
    
    .. attribute:: cefcpowersupplyinputtable
    
    	This table contains the power input information for all the power supplies that have entPhysicalTable entries with 'powerSupply' in the entPhysicalClass.   The entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries is determined by the number of power supplies and number of power inputs on the power  supply
    	**type**\:  :py:class:`CefcPowerSupplyInputTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable>`
    
    .. attribute:: cefcpowersupplyoutputtable
    
    	This table contains a list of possible output mode for the power supplies, whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'powerSupply'. It also indicate which mode is the operational mode within the system
    	**type**\:  :py:class:`CefcPowerSupplyOutputTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable>`
    
    .. attribute:: cefcchassiscoolingtable
    
    	This table contains the cooling capacity information of the chassis whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'chassis'
    	**type**\:  :py:class:`CefcChassisCoolingTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable>`
    
    .. attribute:: cefcfancoolingtable
    
    	This table contains the cooling capacity information of the fans whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'fan'
    	**type**\:  :py:class:`CefcFanCoolingTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable>`
    
    .. attribute:: cefcmodulecoolingtable
    
    	This table contains the cooling requirement for all the manageable components of type entPhysicalClass 'module'
    	**type**\:  :py:class:`CefcModuleCoolingTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable>`
    
    .. attribute:: cefcfancoolingcaptable
    
    	This table contains a list of the possible cooling capacity modes and properties of the fans, whose  ENTITY\-MIB entPhysicalTable entries have an  entPhysicalClass of 'fan'
    	**type**\:  :py:class:`CefcFanCoolingCapTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable>`
    
    .. attribute:: cefcconnectorratingtable
    
    	This table contains the connector power ratings of FRUs.   Only components with power connector rating  management are listed in this table
    	**type**\:  :py:class:`CefcConnectorRatingTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable>`
    
    .. attribute:: cefcmodulepowerconsumptiontable
    
    	This table contains the total power consumption information for modules whose ENTITY\-MIB  entPhysicalTable entries have an entPhysicalClass  of 'module'
    	**type**\:  :py:class:`CefcModulePowerConsumptionTable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable>`
    
    

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
        self._child_classes = OrderedDict([("cefcFRUPower", ("cefcfrupower", CISCOENTITYFRUCONTROLMIB.CefcFRUPower)), ("cefcMIBNotificationEnables", ("cefcmibnotificationenables", CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables)), ("cefcFRUPowerSupplyGroupTable", ("cefcfrupowersupplygrouptable", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable)), ("cefcFRUPowerStatusTable", ("cefcfrupowerstatustable", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable)), ("cefcFRUPowerSupplyValueTable", ("cefcfrupowersupplyvaluetable", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable)), ("cefcModuleTable", ("cefcmoduletable", CISCOENTITYFRUCONTROLMIB.CefcModuleTable)), ("cefcIntelliModuleTable", ("cefcintellimoduletable", CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable)), ("cefcModuleLocalSwitchingTable", ("cefcmodulelocalswitchingtable", CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable)), ("cefcFanTrayStatusTable", ("cefcfantraystatustable", CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable)), ("cefcPhysicalTable", ("cefcphysicaltable", CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable)), ("cefcPowerSupplyInputTable", ("cefcpowersupplyinputtable", CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable)), ("cefcPowerSupplyOutputTable", ("cefcpowersupplyoutputtable", CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable)), ("cefcChassisCoolingTable", ("cefcchassiscoolingtable", CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable)), ("cefcFanCoolingTable", ("cefcfancoolingtable", CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable)), ("cefcModuleCoolingTable", ("cefcmodulecoolingtable", CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable)), ("cefcFanCoolingCapTable", ("cefcfancoolingcaptable", CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable)), ("cefcConnectorRatingTable", ("cefcconnectorratingtable", CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable)), ("cefcModulePowerConsumptionTable", ("cefcmodulepowerconsumptiontable", CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable))])
        self._leafs = OrderedDict()

        self.cefcfrupower = CISCOENTITYFRUCONTROLMIB.CefcFRUPower()
        self.cefcfrupower.parent = self
        self._children_name_map["cefcfrupower"] = "cefcFRUPower"

        self.cefcmibnotificationenables = CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables()
        self.cefcmibnotificationenables.parent = self
        self._children_name_map["cefcmibnotificationenables"] = "cefcMIBNotificationEnables"

        self.cefcfrupowersupplygrouptable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable()
        self.cefcfrupowersupplygrouptable.parent = self
        self._children_name_map["cefcfrupowersupplygrouptable"] = "cefcFRUPowerSupplyGroupTable"

        self.cefcfrupowerstatustable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable()
        self.cefcfrupowerstatustable.parent = self
        self._children_name_map["cefcfrupowerstatustable"] = "cefcFRUPowerStatusTable"

        self.cefcfrupowersupplyvaluetable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable()
        self.cefcfrupowersupplyvaluetable.parent = self
        self._children_name_map["cefcfrupowersupplyvaluetable"] = "cefcFRUPowerSupplyValueTable"

        self.cefcmoduletable = CISCOENTITYFRUCONTROLMIB.CefcModuleTable()
        self.cefcmoduletable.parent = self
        self._children_name_map["cefcmoduletable"] = "cefcModuleTable"

        self.cefcintellimoduletable = CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable()
        self.cefcintellimoduletable.parent = self
        self._children_name_map["cefcintellimoduletable"] = "cefcIntelliModuleTable"

        self.cefcmodulelocalswitchingtable = CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable()
        self.cefcmodulelocalswitchingtable.parent = self
        self._children_name_map["cefcmodulelocalswitchingtable"] = "cefcModuleLocalSwitchingTable"

        self.cefcfantraystatustable = CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable()
        self.cefcfantraystatustable.parent = self
        self._children_name_map["cefcfantraystatustable"] = "cefcFanTrayStatusTable"

        self.cefcphysicaltable = CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable()
        self.cefcphysicaltable.parent = self
        self._children_name_map["cefcphysicaltable"] = "cefcPhysicalTable"

        self.cefcpowersupplyinputtable = CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable()
        self.cefcpowersupplyinputtable.parent = self
        self._children_name_map["cefcpowersupplyinputtable"] = "cefcPowerSupplyInputTable"

        self.cefcpowersupplyoutputtable = CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable()
        self.cefcpowersupplyoutputtable.parent = self
        self._children_name_map["cefcpowersupplyoutputtable"] = "cefcPowerSupplyOutputTable"

        self.cefcchassiscoolingtable = CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable()
        self.cefcchassiscoolingtable.parent = self
        self._children_name_map["cefcchassiscoolingtable"] = "cefcChassisCoolingTable"

        self.cefcfancoolingtable = CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable()
        self.cefcfancoolingtable.parent = self
        self._children_name_map["cefcfancoolingtable"] = "cefcFanCoolingTable"

        self.cefcmodulecoolingtable = CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable()
        self.cefcmodulecoolingtable.parent = self
        self._children_name_map["cefcmodulecoolingtable"] = "cefcModuleCoolingTable"

        self.cefcfancoolingcaptable = CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable()
        self.cefcfancoolingcaptable.parent = self
        self._children_name_map["cefcfancoolingcaptable"] = "cefcFanCoolingCapTable"

        self.cefcconnectorratingtable = CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable()
        self.cefcconnectorratingtable.parent = self
        self._children_name_map["cefcconnectorratingtable"] = "cefcConnectorRatingTable"

        self.cefcmodulepowerconsumptiontable = CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable()
        self.cefcmodulepowerconsumptiontable.parent = self
        self._children_name_map["cefcmodulepowerconsumptiontable"] = "cefcModulePowerConsumptionTable"
        self._segment_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOENTITYFRUCONTROLMIB, [], name, value)


    class CefcFRUPower(Entity):
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
            super(CISCOENTITYFRUCONTROLMIB.CefcFRUPower, self).__init__()

            self.yang_name = "cefcFRUPower"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefcmaxdefaultinlinepower', (YLeaf(YType.int32, 'cefcMaxDefaultInLinePower'), ['int'])),
                ('cefcmaxdefaulthighinlinepower', (YLeaf(YType.uint32, 'cefcMaxDefaultHighInLinePower'), ['int'])),
            ])
            self.cefcmaxdefaultinlinepower = None
            self.cefcmaxdefaulthighinlinepower = None
            self._segment_path = lambda: "cefcFRUPower"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPower, ['cefcmaxdefaultinlinepower', 'cefcmaxdefaulthighinlinepower'], name, value)


    class CefcMIBNotificationEnables(Entity):
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
            super(CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables, self).__init__()

            self.yang_name = "cefcMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefcmibenablestatusnotification', (YLeaf(YType.boolean, 'cefcMIBEnableStatusNotification'), ['bool'])),
                ('cefcenablepsoutputchangenotif', (YLeaf(YType.boolean, 'cefcEnablePSOutputChangeNotif'), ['bool'])),
            ])
            self.cefcmibenablestatusnotification = None
            self.cefcenablepsoutputchangenotif = None
            self._segment_path = lambda: "cefcMIBNotificationEnables"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables, ['cefcmibenablestatusnotification', 'cefcenablepsoutputchangenotif'], name, value)


    class CefcFRUPowerSupplyGroupTable(Entity):
        """
        This table lists the redundancy mode and the
        operational status of the power supply groups
        in the system.
        
        .. attribute:: cefcfrupowersupplygroupentry
        
        	An cefcFRUPowerSupplyGroupTable entry lists the desired redundancy mode, the units of the power outputs and the  available and drawn current for the power supply group.  Entries are created by the agent when a power supply group is added to the entPhysicalTable. Entries are deleted by  the agent at power supply group removal
        	**type**\: list of  		 :py:class:`CefcFRUPowerSupplyGroupEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyGroupTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFRUPowerSupplyGroupEntry", ("cefcfrupowersupplygroupentry", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry))])
            self._leafs = OrderedDict()

            self.cefcfrupowersupplygroupentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerSupplyGroupTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable, [], name, value)


        class CefcFRUPowerSupplyGroupEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
            	**type**\:  :py:class:`CefcPowerNonRedundantReason <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry.CefcPowerNonRedundantReason>`
            
            .. attribute:: cefctotaldrawninlinecurrent
            
            	Total inline current drawn for inline operation
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyGroupEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcpowerredundancymode', (YLeaf(YType.enumeration, 'cefcPowerRedundancyMode'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerRedundancyType', '')])),
                    ('cefcpowerunits', (YLeaf(YType.str, 'cefcPowerUnits'), ['str'])),
                    ('cefctotalavailablecurrent', (YLeaf(YType.int32, 'cefcTotalAvailableCurrent'), ['int'])),
                    ('cefctotaldrawncurrent', (YLeaf(YType.int32, 'cefcTotalDrawnCurrent'), ['int'])),
                    ('cefcpowerredundancyopermode', (YLeaf(YType.enumeration, 'cefcPowerRedundancyOperMode'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerRedundancyType', '')])),
                    ('cefcpowernonredundantreason', (YLeaf(YType.enumeration, 'cefcPowerNonRedundantReason'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB', 'CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry.CefcPowerNonRedundantReason')])),
                    ('cefctotaldrawninlinecurrent', (YLeaf(YType.int32, 'cefcTotalDrawnInlineCurrent'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry, ['entphysicalindex', 'cefcpowerredundancymode', 'cefcpowerunits', 'cefctotalavailablecurrent', 'cefctotaldrawncurrent', 'cefcpowerredundancyopermode', 'cefcpowernonredundantreason', 'cefctotaldrawninlinecurrent'], name, value)

            class CefcPowerNonRedundantReason(Enum):
                """
                CefcPowerNonRedundantReason (Enum Class)

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



    class CefcFRUPowerStatusTable(Entity):
        """
        This table lists the power\-related administrative status
        and operational status of the manageable components
        in the system.
        
        .. attribute:: cefcfrupowerstatusentry
        
        	An cefcFRUPowerStatusTable entry lists the desired administrative status, the operational status of the  power manageable component, and the current required by  the component for operation.  Entries are created by the agent at system power\-up or  the insertion of the component.  Entries are deleted by the agent at the removal of the component.  Only components with power control are listed in the  table
        	**type**\: list of  		 :py:class:`CefcFRUPowerStatusEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable, self).__init__()

            self.yang_name = "cefcFRUPowerStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFRUPowerStatusEntry", ("cefcfrupowerstatusentry", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry))])
            self._leafs = OrderedDict()

            self.cefcfrupowerstatusentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerStatusTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable, [], name, value)


        class CefcFRUPowerStatusEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
            	**type**\:  :py:class:`CefcFRUPowerCapability <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry.CefcFRUPowerCapability>`
            
            .. attribute:: cefcfrurealtimecurrent
            
            	This object indicates the realtime value of current supplied by the FRU (positive values) or the realtime value of current drawn by the FRU (negative values)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry, self).__init__()

                self.yang_name = "cefcFRUPowerStatusEntry"
                self.yang_parent_name = "cefcFRUPowerStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcfrupoweradminstatus', (YLeaf(YType.enumeration, 'cefcFRUPowerAdminStatus'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerAdminType', '')])),
                    ('cefcfrupoweroperstatus', (YLeaf(YType.enumeration, 'cefcFRUPowerOperStatus'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerOperType', '')])),
                    ('cefcfrucurrent', (YLeaf(YType.int32, 'cefcFRUCurrent'), ['int'])),
                    ('cefcfrupowercapability', (YLeaf(YType.bits, 'cefcFRUPowerCapability'), ['Bits'])),
                    ('cefcfrurealtimecurrent', (YLeaf(YType.int32, 'cefcFRURealTimeCurrent'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcfrupoweradminstatus = None
                self.cefcfrupoweroperstatus = None
                self.cefcfrucurrent = None
                self.cefcfrupowercapability = Bits()
                self.cefcfrurealtimecurrent = None
                self._segment_path = lambda: "cefcFRUPowerStatusEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry, ['entphysicalindex', 'cefcfrupoweradminstatus', 'cefcfrupoweroperstatus', 'cefcfrucurrent', 'cefcfrupowercapability', 'cefcfrurealtimecurrent'], name, value)


    class CefcFRUPowerSupplyValueTable(Entity):
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
        	**type**\: list of  		 :py:class:`CefcFRUPowerSupplyValueEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyValueTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFRUPowerSupplyValueEntry", ("cefcfrupowersupplyvalueentry", CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry))])
            self._leafs = OrderedDict()

            self.cefcfrupowersupplyvalueentry = YList(self)
            self._segment_path = lambda: "cefcFRUPowerSupplyValueTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable, [], name, value)


        class CefcFRUPowerSupplyValueEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyValueEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcfrutotalsystemcurrent', (YLeaf(YType.int32, 'cefcFRUTotalSystemCurrent'), ['int'])),
                    ('cefcfrudrawnsystemcurrent', (YLeaf(YType.int32, 'cefcFRUDrawnSystemCurrent'), ['int'])),
                    ('cefcfrutotalinlinecurrent', (YLeaf(YType.int32, 'cefcFRUTotalInlineCurrent'), ['int'])),
                    ('cefcfrudrawninlinecurrent', (YLeaf(YType.int32, 'cefcFRUDrawnInlineCurrent'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcfrutotalsystemcurrent = None
                self.cefcfrudrawnsystemcurrent = None
                self.cefcfrutotalinlinecurrent = None
                self.cefcfrudrawninlinecurrent = None
                self._segment_path = lambda: "cefcFRUPowerSupplyValueEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyValueTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry, ['entphysicalindex', 'cefcfrutotalsystemcurrent', 'cefcfrudrawnsystemcurrent', 'cefcfrutotalinlinecurrent', 'cefcfrudrawninlinecurrent'], name, value)


    class CefcModuleTable(Entity):
        """
        A cefcModuleTable entry lists the operational and
        administrative status information for ENTITY\-MIB
        entPhysicalTable entries for manageable components
        of type PhysicalClass module(9).
        
        .. attribute:: cefcmoduleentry
        
        	A cefcModuleStatusTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components  of type PhysicalClass module(9).  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of  		 :py:class:`CefcModuleEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcModuleTable, self).__init__()

            self.yang_name = "cefcModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcModuleEntry", ("cefcmoduleentry", CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry))])
            self._leafs = OrderedDict()

            self.cefcmoduleentry = YList(self)
            self._segment_path = lambda: "cefcModuleTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleTable, [], name, value)


        class CefcModuleEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry, self).__init__()

                self.yang_name = "cefcModuleEntry"
                self.yang_parent_name = "cefcModuleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcmoduleadminstatus', (YLeaf(YType.enumeration, 'cefcModuleAdminStatus'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleAdminType', '')])),
                    ('cefcmoduleoperstatus', (YLeaf(YType.enumeration, 'cefcModuleOperStatus'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleOperType', '')])),
                    ('cefcmoduleresetreason', (YLeaf(YType.enumeration, 'cefcModuleResetReason'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleResetReasonType', '')])),
                    ('cefcmodulestatuslastchangetime', (YLeaf(YType.uint32, 'cefcModuleStatusLastChangeTime'), ['int'])),
                    ('cefcmodulelastclearconfigtime', (YLeaf(YType.uint32, 'cefcModuleLastClearConfigTime'), ['int'])),
                    ('cefcmoduleresetreasondescription', (YLeaf(YType.str, 'cefcModuleResetReasonDescription'), ['str'])),
                    ('cefcmodulestatechangereasondescr', (YLeaf(YType.str, 'cefcModuleStateChangeReasonDescr'), ['str'])),
                    ('cefcmoduleuptime', (YLeaf(YType.uint32, 'cefcModuleUpTime'), ['int'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry, ['entphysicalindex', 'cefcmoduleadminstatus', 'cefcmoduleoperstatus', 'cefcmoduleresetreason', 'cefcmodulestatuslastchangetime', 'cefcmodulelastclearconfigtime', 'cefcmoduleresetreasondescription', 'cefcmodulestatechangereasondescr', 'cefcmoduleuptime'], name, value)


    class CefcIntelliModuleTable(Entity):
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
        	**type**\: list of  		 :py:class:`CefcIntelliModuleEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable, self).__init__()

            self.yang_name = "cefcIntelliModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcIntelliModuleEntry", ("cefcintellimoduleentry", CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry))])
            self._leafs = OrderedDict()

            self.cefcintellimoduleentry = YList(self)
            self._segment_path = lambda: "cefcIntelliModuleTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable, [], name, value)


        class CefcIntelliModuleEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry, self).__init__()

                self.yang_name = "cefcIntelliModuleEntry"
                self.yang_parent_name = "cefcIntelliModuleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcintellimoduleipaddrtype', (YLeaf(YType.enumeration, 'cefcIntelliModuleIPAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cefcintellimoduleipaddr', (YLeaf(YType.str, 'cefcIntelliModuleIPAddr'), ['str'])),
                ])
                self.entphysicalindex = None
                self.cefcintellimoduleipaddrtype = None
                self.cefcintellimoduleipaddr = None
                self._segment_path = lambda: "cefcIntelliModuleEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcIntelliModuleTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry, ['entphysicalindex', 'cefcintellimoduleipaddrtype', 'cefcintellimoduleipaddr'], name, value)


    class CefcModuleLocalSwitchingTable(Entity):
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
        	**type**\: list of  		 :py:class:`CefcModuleLocalSwitchingEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable, self).__init__()

            self.yang_name = "cefcModuleLocalSwitchingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcModuleLocalSwitchingEntry", ("cefcmodulelocalswitchingentry", CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry))])
            self._leafs = OrderedDict()

            self.cefcmodulelocalswitchingentry = YList(self)
            self._segment_path = lambda: "cefcModuleLocalSwitchingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable, [], name, value)


        class CefcModuleLocalSwitchingEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            .. attribute:: cefcmodulelocalswitchingmode
            
            	This object specifies the mode of local switching.  enabled(1)  \- local switching is enabled. disabled(2) \- local switching is disabled
            	**type**\:  :py:class:`CefcModuleLocalSwitchingMode <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry.CefcModuleLocalSwitchingMode>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry, self).__init__()

                self.yang_name = "cefcModuleLocalSwitchingEntry"
                self.yang_parent_name = "cefcModuleLocalSwitchingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcmodulelocalswitchingmode', (YLeaf(YType.enumeration, 'cefcModuleLocalSwitchingMode'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB', 'CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry.CefcModuleLocalSwitchingMode')])),
                ])
                self.entphysicalindex = None
                self.cefcmodulelocalswitchingmode = None
                self._segment_path = lambda: "cefcModuleLocalSwitchingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleLocalSwitchingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry, ['entphysicalindex', 'cefcmodulelocalswitchingmode'], name, value)

            class CefcModuleLocalSwitchingMode(Enum):
                """
                CefcModuleLocalSwitchingMode (Enum Class)

                This object specifies the mode of local switching.

                enabled(1)  \- local switching is enabled.

                disabled(2) \- local switching is disabled.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")



    class CefcFanTrayStatusTable(Entity):
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
        	**type**\: list of  		 :py:class:`CefcFanTrayStatusEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable, self).__init__()

            self.yang_name = "cefcFanTrayStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFanTrayStatusEntry", ("cefcfantraystatusentry", CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry))])
            self._leafs = OrderedDict()

            self.cefcfantraystatusentry = YList(self)
            self._segment_path = lambda: "cefcFanTrayStatusTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable, [], name, value)


        class CefcFanTrayStatusEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            .. attribute:: cefcfantrayoperstatus
            
            	The operational state of the fan or fan tray. unknown(1) \- unknown. up(2) \- powered on. down(3) \- powered down. warning(4) \- partial failure, needs replacement               as soon as possible
            	**type**\:  :py:class:`CefcFanTrayOperStatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry.CefcFanTrayOperStatus>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry, self).__init__()

                self.yang_name = "cefcFanTrayStatusEntry"
                self.yang_parent_name = "cefcFanTrayStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcfantrayoperstatus', (YLeaf(YType.enumeration, 'cefcFanTrayOperStatus'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB', 'CefcFanTrayStatusTable.CefcFanTrayStatusEntry.CefcFanTrayOperStatus')])),
                ])
                self.entphysicalindex = None
                self.cefcfantrayoperstatus = None
                self._segment_path = lambda: "cefcFanTrayStatusEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanTrayStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry, ['entphysicalindex', 'cefcfantrayoperstatus'], name, value)

            class CefcFanTrayOperStatus(Enum):
                """
                CefcFanTrayOperStatus (Enum Class)

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



    class CefcPhysicalTable(Entity):
        """
        This table contains one row per physical entity.
        
        .. attribute:: cefcphysicalentry
        
        	Information about a particular physical entity
        	**type**\: list of  		 :py:class:`CefcPhysicalEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable, self).__init__()

            self.yang_name = "cefcPhysicalTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcPhysicalEntry", ("cefcphysicalentry", CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry))])
            self._leafs = OrderedDict()

            self.cefcphysicalentry = YList(self)
            self._segment_path = lambda: "cefcPhysicalTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable, [], name, value)


        class CefcPhysicalEntry(Entity):
            """
            Information about a particular physical entity.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            .. attribute:: cefcphysicalstatus
            
            	The status of this physical entity. other(1) \- the status is not any of the listed below. supported(2) \- this entity is supported. unsupported(3) \- this entity is unsupported. incompatible(4) \- this entity is incompatible. It would be unsupported(3), if the ID read from Serial EPROM is not supported. It would be incompatible(4), if in the present configuration this FRU is not supported
            	**type**\:  :py:class:`CefcPhysicalStatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry.CefcPhysicalStatus>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry, self).__init__()

                self.yang_name = "cefcPhysicalEntry"
                self.yang_parent_name = "cefcPhysicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcphysicalstatus', (YLeaf(YType.enumeration, 'cefcPhysicalStatus'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB', 'CefcPhysicalTable.CefcPhysicalEntry.CefcPhysicalStatus')])),
                ])
                self.entphysicalindex = None
                self.cefcphysicalstatus = None
                self._segment_path = lambda: "cefcPhysicalEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPhysicalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry, ['entphysicalindex', 'cefcphysicalstatus'], name, value)

            class CefcPhysicalStatus(Enum):
                """
                CefcPhysicalStatus (Enum Class)

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



    class CefcPowerSupplyInputTable(Entity):
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
        	**type**\: list of  		 :py:class:`CefcPowerSupplyInputEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable, self).__init__()

            self.yang_name = "cefcPowerSupplyInputTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcPowerSupplyInputEntry", ("cefcpowersupplyinputentry", CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry))])
            self._leafs = OrderedDict()

            self.cefcpowersupplyinputentry = YList(self)
            self._segment_path = lambda: "cefcPowerSupplyInputTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable, [], name, value)


        class CefcPowerSupplyInputEntry(Entity):
            """
            An entry containing power input management information
            applicable to a particular power supply and input.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            .. attribute:: cefcpowersupplyinputindex  (key)
            
            	A unique value, greater than zero, for each input on a power supply
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcpowersupplyinputtype
            
            	The type of an input power detected on the power supply.  unknown(1)\: No input power is detected.  acLow(2)\: Lower rating AC input power is detected.  acHigh(3)\: Higher rating AC input power is detected.  dcLow(4)\: Lower rating DC input power is detected.  dcHigh(5)\: Higher rating DC input power is detected
            	**type**\:  :py:class:`CefcPowerSupplyInputType <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry.CefcPowerSupplyInputType>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry, self).__init__()

                self.yang_name = "cefcPowerSupplyInputEntry"
                self.yang_parent_name = "cefcPowerSupplyInputTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefcpowersupplyinputindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcpowersupplyinputindex', (YLeaf(YType.uint32, 'cefcPowerSupplyInputIndex'), ['int'])),
                    ('cefcpowersupplyinputtype', (YLeaf(YType.enumeration, 'cefcPowerSupplyInputType'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB', 'CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry.CefcPowerSupplyInputType')])),
                ])
                self.entphysicalindex = None
                self.cefcpowersupplyinputindex = None
                self.cefcpowersupplyinputtype = None
                self._segment_path = lambda: "cefcPowerSupplyInputEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefcPowerSupplyInputIndex='" + str(self.cefcpowersupplyinputindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPowerSupplyInputTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry, ['entphysicalindex', 'cefcpowersupplyinputindex', 'cefcpowersupplyinputtype'], name, value)

            class CefcPowerSupplyInputType(Enum):
                """
                CefcPowerSupplyInputType (Enum Class)

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



    class CefcPowerSupplyOutputTable(Entity):
        """
        This table contains a list of possible output
        mode for the power supplies, whose ENTITY\-MIB
        entPhysicalTable entries have an entPhysicalClass
        of 'powerSupply'. It also indicate which mode
        is the operational mode within the system.
        
        .. attribute:: cefcpowersupplyoutputentry
        
        	A cefcPowerSupplyOutputTable entry lists the power output capacity and its operational status for manageable components of type PhysicalClass 'powerSupply'.  Entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries of a power supply is determined by the power supply
        	**type**\: list of  		 :py:class:`CefcPowerSupplyOutputEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable, self).__init__()

            self.yang_name = "cefcPowerSupplyOutputTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcPowerSupplyOutputEntry", ("cefcpowersupplyoutputentry", CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry))])
            self._leafs = OrderedDict()

            self.cefcpowersupplyoutputentry = YList(self)
            self._segment_path = lambda: "cefcPowerSupplyOutputTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable, [], name, value)


        class CefcPowerSupplyOutputEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry, self).__init__()

                self.yang_name = "cefcPowerSupplyOutputEntry"
                self.yang_parent_name = "cefcPowerSupplyOutputTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefcpsoutputmodeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcpsoutputmodeindex', (YLeaf(YType.uint32, 'cefcPSOutputModeIndex'), ['int'])),
                    ('cefcpsoutputmodecurrent', (YLeaf(YType.int32, 'cefcPSOutputModeCurrent'), ['int'])),
                    ('cefcpsoutputmodeinoperation', (YLeaf(YType.boolean, 'cefcPSOutputModeInOperation'), ['bool'])),
                ])
                self.entphysicalindex = None
                self.cefcpsoutputmodeindex = None
                self.cefcpsoutputmodecurrent = None
                self.cefcpsoutputmodeinoperation = None
                self._segment_path = lambda: "cefcPowerSupplyOutputEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefcPSOutputModeIndex='" + str(self.cefcpsoutputmodeindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPowerSupplyOutputTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry, ['entphysicalindex', 'cefcpsoutputmodeindex', 'cefcpsoutputmodecurrent', 'cefcpsoutputmodeinoperation'], name, value)


    class CefcChassisCoolingTable(Entity):
        """
        This table contains the cooling capacity
        information of the chassis whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'chassis'.
        
        .. attribute:: cefcchassiscoolingentry
        
        	A cefcChassisCoolingEntry lists the maximum cooling capacity that could be provided  for one slot on the manageable components of type PhysicalClass 'chassis'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of  		 :py:class:`CefcChassisCoolingEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable, self).__init__()

            self.yang_name = "cefcChassisCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcChassisCoolingEntry", ("cefcchassiscoolingentry", CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry))])
            self._leafs = OrderedDict()

            self.cefcchassiscoolingentry = YList(self)
            self._segment_path = lambda: "cefcChassisCoolingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable, [], name, value)


        class CefcChassisCoolingEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry, self).__init__()

                self.yang_name = "cefcChassisCoolingEntry"
                self.yang_parent_name = "cefcChassisCoolingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcchassisperslotcoolingcap', (YLeaf(YType.uint32, 'cefcChassisPerSlotCoolingCap'), ['int'])),
                    ('cefcchassisperslotcoolingunit', (YLeaf(YType.enumeration, 'cefcChassisPerSlotCoolingUnit'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit', '')])),
                ])
                self.entphysicalindex = None
                self.cefcchassisperslotcoolingcap = None
                self.cefcchassisperslotcoolingunit = None
                self._segment_path = lambda: "cefcChassisCoolingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcChassisCoolingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry, ['entphysicalindex', 'cefcchassisperslotcoolingcap', 'cefcchassisperslotcoolingunit'], name, value)


    class CefcFanCoolingTable(Entity):
        """
        This table contains the cooling capacity
        information of the fans whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingentry
        
        	A cefcFanCoolingEntry lists the cooling capacity that is provided by the  manageable components of type PhysicalClass  'fan'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of  		 :py:class:`CefcFanCoolingEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable, self).__init__()

            self.yang_name = "cefcFanCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFanCoolingEntry", ("cefcfancoolingentry", CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry))])
            self._leafs = OrderedDict()

            self.cefcfancoolingentry = YList(self)
            self._segment_path = lambda: "cefcFanCoolingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable, [], name, value)


        class CefcFanCoolingEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry, self).__init__()

                self.yang_name = "cefcFanCoolingEntry"
                self.yang_parent_name = "cefcFanCoolingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcfancoolingcapacity', (YLeaf(YType.uint32, 'cefcFanCoolingCapacity'), ['int'])),
                    ('cefcfancoolingcapacityunit', (YLeaf(YType.enumeration, 'cefcFanCoolingCapacityUnit'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit', '')])),
                ])
                self.entphysicalindex = None
                self.cefcfancoolingcapacity = None
                self.cefcfancoolingcapacityunit = None
                self._segment_path = lambda: "cefcFanCoolingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanCoolingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry, ['entphysicalindex', 'cefcfancoolingcapacity', 'cefcfancoolingcapacityunit'], name, value)


    class CefcModuleCoolingTable(Entity):
        """
        This table contains the cooling requirement for
        all the manageable components of type entPhysicalClass
        'module'.
        
        .. attribute:: cefcmodulecoolingentry
        
        	A cefcModuleCoolingEntry lists the cooling requirement for a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of  		 :py:class:`CefcModuleCoolingEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable, self).__init__()

            self.yang_name = "cefcModuleCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcModuleCoolingEntry", ("cefcmodulecoolingentry", CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry))])
            self._leafs = OrderedDict()

            self.cefcmodulecoolingentry = YList(self)
            self._segment_path = lambda: "cefcModuleCoolingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable, [], name, value)


        class CefcModuleCoolingEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry, self).__init__()

                self.yang_name = "cefcModuleCoolingEntry"
                self.yang_parent_name = "cefcModuleCoolingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcmodulecooling', (YLeaf(YType.uint32, 'cefcModuleCooling'), ['int'])),
                    ('cefcmodulecoolingunit', (YLeaf(YType.enumeration, 'cefcModuleCoolingUnit'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit', '')])),
                ])
                self.entphysicalindex = None
                self.cefcmodulecooling = None
                self.cefcmodulecoolingunit = None
                self._segment_path = lambda: "cefcModuleCoolingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleCoolingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry, ['entphysicalindex', 'cefcmodulecooling', 'cefcmodulecoolingunit'], name, value)


    class CefcFanCoolingCapTable(Entity):
        """
        This table contains a list of the possible cooling
        capacity modes and properties of the fans, whose 
        ENTITY\-MIB entPhysicalTable entries have an 
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingcapentry
        
        	A cefcFanCoolingCapacityEntry lists the cooling capacity mode of a manageable components of type entPhysicalClass 'fan'. It also lists the corresponding cooling capacity provided and the power consumed by the fan on this mode.   Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of  		 :py:class:`CefcFanCoolingCapEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable, self).__init__()

            self.yang_name = "cefcFanCoolingCapTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcFanCoolingCapEntry", ("cefcfancoolingcapentry", CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry))])
            self._leafs = OrderedDict()

            self.cefcfancoolingcapentry = YList(self)
            self._segment_path = lambda: "cefcFanCoolingCapTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable, [], name, value)


        class CefcFanCoolingCapEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
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
                super(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry, self).__init__()

                self.yang_name = "cefcFanCoolingCapEntry"
                self.yang_parent_name = "cefcFanCoolingCapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefcfancoolingcapindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcfancoolingcapindex', (YLeaf(YType.uint32, 'cefcFanCoolingCapIndex'), ['int'])),
                    ('cefcfancoolingcapmodedescr', (YLeaf(YType.str, 'cefcFanCoolingCapModeDescr'), ['str'])),
                    ('cefcfancoolingcapcapacity', (YLeaf(YType.uint32, 'cefcFanCoolingCapCapacity'), ['int'])),
                    ('cefcfancoolingcapcurrent', (YLeaf(YType.int32, 'cefcFanCoolingCapCurrent'), ['int'])),
                    ('cefcfancoolingcapcapacityunit', (YLeaf(YType.enumeration, 'cefcFanCoolingCapCapacityUnit'), [('ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit', '')])),
                ])
                self.entphysicalindex = None
                self.cefcfancoolingcapindex = None
                self.cefcfancoolingcapmodedescr = None
                self.cefcfancoolingcapcapacity = None
                self.cefcfancoolingcapcurrent = None
                self.cefcfancoolingcapcapacityunit = None
                self._segment_path = lambda: "cefcFanCoolingCapEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefcFanCoolingCapIndex='" + str(self.cefcfancoolingcapindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanCoolingCapTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry, ['entphysicalindex', 'cefcfancoolingcapindex', 'cefcfancoolingcapmodedescr', 'cefcfancoolingcapcapacity', 'cefcfancoolingcapcurrent', 'cefcfancoolingcapcapacityunit'], name, value)


    class CefcConnectorRatingTable(Entity):
        """
        This table contains the connector power
        ratings of FRUs. 
        
        Only components with power connector rating 
        management are listed in this table.
        
        .. attribute:: cefcconnectorratingentry
        
        	A cefcConnectorRatingEntry lists the power connector rating information of a  component in the system.  An entry or entries are created by the agent when an physical entity with connector rating  management is added to the ENTITY\-MIB  entPhysicalTable. An entry is deleted  by the agent at the entity removal
        	**type**\: list of  		 :py:class:`CefcConnectorRatingEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable, self).__init__()

            self.yang_name = "cefcConnectorRatingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcConnectorRatingEntry", ("cefcconnectorratingentry", CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry))])
            self._leafs = OrderedDict()

            self.cefcconnectorratingentry = YList(self)
            self._segment_path = lambda: "cefcConnectorRatingTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable, [], name, value)


        class CefcConnectorRatingEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            .. attribute:: cefcconnectorrating
            
            	The maximum power that the component's connector can withdraw
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry, self).__init__()

                self.yang_name = "cefcConnectorRatingEntry"
                self.yang_parent_name = "cefcConnectorRatingTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcconnectorrating', (YLeaf(YType.int32, 'cefcConnectorRating'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcconnectorrating = None
                self._segment_path = lambda: "cefcConnectorRatingEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcConnectorRatingTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry, ['entphysicalindex', 'cefcconnectorrating'], name, value)


    class CefcModulePowerConsumptionTable(Entity):
        """
        This table contains the total power consumption
        information for modules whose ENTITY\-MIB 
        entPhysicalTable entries have an entPhysicalClass 
        of 'module'.
        
        .. attribute:: cefcmodulepowerconsumptionentry
        
        	A cefcModulePowerConsumptionEntry lists the total power consumption of a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of  		 :py:class:`CefcModulePowerConsumptionEntry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable, self).__init__()

            self.yang_name = "cefcModulePowerConsumptionTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefcModulePowerConsumptionEntry", ("cefcmodulepowerconsumptionentry", CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry))])
            self._leafs = OrderedDict()

            self.cefcmodulepowerconsumptionentry = YList(self)
            self._segment_path = lambda: "cefcModulePowerConsumptionTable"
            self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable, [], name, value)


        class CefcModulePowerConsumptionEntry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            .. attribute:: cefcmodulepowerconsumption
            
            	The combined power consumption to operate the module and its submodule(s) and inline\-power device(s)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry, self).__init__()

                self.yang_name = "cefcModulePowerConsumptionEntry"
                self.yang_parent_name = "cefcModulePowerConsumptionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefcmodulepowerconsumption', (YLeaf(YType.int32, 'cefcModulePowerConsumption'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefcmodulepowerconsumption = None
                self._segment_path = lambda: "cefcModulePowerConsumptionEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModulePowerConsumptionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry, ['entphysicalindex', 'cefcmodulepowerconsumption'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOENTITYFRUCONTROLMIB()
        return self._top_entity

