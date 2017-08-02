""" CISCO_ENTITY_FRU_CONTROL_MIB 

The CISCO\-ENTITY\-FRU\-CONTROL\-MIB is used to monitor
and configure operational status of 
Field Replaceable Units (FRUs) and other managable 
physical entities of the system listed in the 
Entity\-MIB (RFC 2737) entPhysicalTable. 

FRUs include assemblies such as power supplies, fans, 
processor modules, interface modules, etc.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Frucoolingunit(Enum):
    """
    Frucoolingunit

    The unit for the cooling capacity and requirement.

    cfm(1)    Cubic feet per minute

    watts(2)  Watts

    .. data:: cfm = 1

    .. data:: watts = 2

    """

    cfm = Enum.YLeaf(1, "cfm")

    watts = Enum.YLeaf(2, "watts")


class Moduleadmintype(Enum):
    """
    Moduleadmintype

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


class Moduleopertype(Enum):
    """
    Moduleopertype

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


class Moduleresetreasontype(Enum):
    """
    Moduleresetreasontype

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


class Poweradmintype(Enum):
    """
    Poweradmintype

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


class Poweropertype(Enum):
    """
    Poweropertype

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


class Powerredundancytype(Enum):
    """
    Powerredundancytype

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



class CiscoEntityFruControlMib(Entity):
    """
    
    
    .. attribute:: cefcchassiscoolingtable
    
    	This table contains the cooling capacity information of the chassis whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'chassis'
    	**type**\:   :py:class:`Cefcchassiscoolingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcchassiscoolingtable>`
    
    .. attribute:: cefcconnectorratingtable
    
    	This table contains the connector power ratings of FRUs.   Only components with power connector rating  management are listed in this table
    	**type**\:   :py:class:`Cefcconnectorratingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcconnectorratingtable>`
    
    .. attribute:: cefcfancoolingcaptable
    
    	This table contains a list of the possible cooling capacity modes and properties of the fans, whose  ENTITY\-MIB entPhysicalTable entries have an  entPhysicalClass of 'fan'
    	**type**\:   :py:class:`Cefcfancoolingcaptable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfancoolingcaptable>`
    
    .. attribute:: cefcfancoolingtable
    
    	This table contains the cooling capacity information of the fans whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'fan'
    	**type**\:   :py:class:`Cefcfancoolingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfancoolingtable>`
    
    .. attribute:: cefcfantraystatustable
    
    	This table contains the operational status information for all ENTITY\-MIB entPhysicalTable entries which have  an entPhysicalClass of 'fan'; specifically, all   entPhysicalTable entries which represent either\: one  physical fan, or a single physical 'fan tray' which is a manufactured (inseparable in the field) combination of  multiple fans
    	**type**\:   :py:class:`Cefcfantraystatustable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfantraystatustable>`
    
    .. attribute:: cefcfrupower
    
    	
    	**type**\:   :py:class:`Cefcfrupower <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupower>`
    
    .. attribute:: cefcfrupowerstatustable
    
    	This table lists the power\-related administrative status and operational status of the manageable components in the system
    	**type**\:   :py:class:`Cefcfrupowerstatustable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowerstatustable>`
    
    .. attribute:: cefcfrupowersupplygrouptable
    
    	This table lists the redundancy mode and the operational status of the power supply groups in the system
    	**type**\:   :py:class:`Cefcfrupowersupplygrouptable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable>`
    
    .. attribute:: cefcfrupowersupplyvaluetable
    
    	This table lists the power capacity of a power FRU in the system if it provides variable power. Power supplies usually provide either system or inline power. They cannot be  controlled by software to dictate how they distribute power. We can also have what are known as variable power supplies. They can provide both system and inline power and can be  varied within hardware defined ranges for system and inline limited by a total maximum combined output. They could be configured by the user via CLI or SNMP or be controlled by software internally. This table supplements the information in the cefcFRUPowerStatusTable for power supply FRUs. The  cefcFRUCurrent attribute in that table provides the overall current the power supply FRU can provide while this table  gives us the individual contribution towards system and  inline power
    	**type**\:   :py:class:`Cefcfrupowersupplyvaluetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable>`
    
    .. attribute:: cefcintellimoduletable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcIntelliModuleTable entry lists the information specific to intelligent modules which cannot be provided by the cefcModuleTable
    	**type**\:   :py:class:`Cefcintellimoduletable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcintellimoduletable>`
    
    .. attribute:: cefcmibnotificationenables
    
    	
    	**type**\:   :py:class:`Cefcmibnotificationenables <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmibnotificationenables>`
    
    .. attribute:: cefcmodulecoolingtable
    
    	This table contains the cooling requirement for all the manageable components of type entPhysicalClass 'module'
    	**type**\:   :py:class:`Cefcmodulecoolingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulecoolingtable>`
    
    .. attribute:: cefcmodulelocalswitchingtable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcModuleLocalSwitchingTable entry lists the information specific to local switching capable modules which cannot be provided by the cefcModuleTable
    	**type**\:   :py:class:`Cefcmodulelocalswitchingtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable>`
    
    .. attribute:: cefcmodulepowerconsumptiontable
    
    	This table contains the total power consumption information for modules whose ENTITY\-MIB  entPhysicalTable entries have an entPhysicalClass  of 'module'
    	**type**\:   :py:class:`Cefcmodulepowerconsumptiontable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable>`
    
    .. attribute:: cefcmoduletable
    
    	A cefcModuleTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components of type PhysicalClass module(9)
    	**type**\:   :py:class:`Cefcmoduletable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmoduletable>`
    
    .. attribute:: cefcphysicaltable
    
    	This table contains one row per physical entity
    	**type**\:   :py:class:`Cefcphysicaltable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcphysicaltable>`
    
    .. attribute:: cefcpowersupplyinputtable
    
    	This table contains the power input information for all the power supplies that have entPhysicalTable entries with 'powerSupply' in the entPhysicalClass.   The entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries is determined by the number of power supplies and number of power inputs on the power  supply
    	**type**\:   :py:class:`Cefcpowersupplyinputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcpowersupplyinputtable>`
    
    .. attribute:: cefcpowersupplyoutputtable
    
    	This table contains a list of possible output mode for the power supplies, whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'powerSupply'. It also indicate which mode is the operational mode within the system
    	**type**\:   :py:class:`Cefcpowersupplyoutputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcpowersupplyoutputtable>`
    
    

    """

    _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
    _revision = '2013-08-19'

    def __init__(self):
        super(CiscoEntityFruControlMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-FRU-CONTROL-MIB"
        self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

        self.cefcchassiscoolingtable = CiscoEntityFruControlMib.Cefcchassiscoolingtable()
        self.cefcchassiscoolingtable.parent = self
        self._children_name_map["cefcchassiscoolingtable"] = "cefcChassisCoolingTable"
        self._children_yang_names.add("cefcChassisCoolingTable")

        self.cefcconnectorratingtable = CiscoEntityFruControlMib.Cefcconnectorratingtable()
        self.cefcconnectorratingtable.parent = self
        self._children_name_map["cefcconnectorratingtable"] = "cefcConnectorRatingTable"
        self._children_yang_names.add("cefcConnectorRatingTable")

        self.cefcfancoolingcaptable = CiscoEntityFruControlMib.Cefcfancoolingcaptable()
        self.cefcfancoolingcaptable.parent = self
        self._children_name_map["cefcfancoolingcaptable"] = "cefcFanCoolingCapTable"
        self._children_yang_names.add("cefcFanCoolingCapTable")

        self.cefcfancoolingtable = CiscoEntityFruControlMib.Cefcfancoolingtable()
        self.cefcfancoolingtable.parent = self
        self._children_name_map["cefcfancoolingtable"] = "cefcFanCoolingTable"
        self._children_yang_names.add("cefcFanCoolingTable")

        self.cefcfantraystatustable = CiscoEntityFruControlMib.Cefcfantraystatustable()
        self.cefcfantraystatustable.parent = self
        self._children_name_map["cefcfantraystatustable"] = "cefcFanTrayStatusTable"
        self._children_yang_names.add("cefcFanTrayStatusTable")

        self.cefcfrupower = CiscoEntityFruControlMib.Cefcfrupower()
        self.cefcfrupower.parent = self
        self._children_name_map["cefcfrupower"] = "cefcFRUPower"
        self._children_yang_names.add("cefcFRUPower")

        self.cefcfrupowerstatustable = CiscoEntityFruControlMib.Cefcfrupowerstatustable()
        self.cefcfrupowerstatustable.parent = self
        self._children_name_map["cefcfrupowerstatustable"] = "cefcFRUPowerStatusTable"
        self._children_yang_names.add("cefcFRUPowerStatusTable")

        self.cefcfrupowersupplygrouptable = CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable()
        self.cefcfrupowersupplygrouptable.parent = self
        self._children_name_map["cefcfrupowersupplygrouptable"] = "cefcFRUPowerSupplyGroupTable"
        self._children_yang_names.add("cefcFRUPowerSupplyGroupTable")

        self.cefcfrupowersupplyvaluetable = CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable()
        self.cefcfrupowersupplyvaluetable.parent = self
        self._children_name_map["cefcfrupowersupplyvaluetable"] = "cefcFRUPowerSupplyValueTable"
        self._children_yang_names.add("cefcFRUPowerSupplyValueTable")

        self.cefcintellimoduletable = CiscoEntityFruControlMib.Cefcintellimoduletable()
        self.cefcintellimoduletable.parent = self
        self._children_name_map["cefcintellimoduletable"] = "cefcIntelliModuleTable"
        self._children_yang_names.add("cefcIntelliModuleTable")

        self.cefcmibnotificationenables = CiscoEntityFruControlMib.Cefcmibnotificationenables()
        self.cefcmibnotificationenables.parent = self
        self._children_name_map["cefcmibnotificationenables"] = "cefcMIBNotificationEnables"
        self._children_yang_names.add("cefcMIBNotificationEnables")

        self.cefcmodulecoolingtable = CiscoEntityFruControlMib.Cefcmodulecoolingtable()
        self.cefcmodulecoolingtable.parent = self
        self._children_name_map["cefcmodulecoolingtable"] = "cefcModuleCoolingTable"
        self._children_yang_names.add("cefcModuleCoolingTable")

        self.cefcmodulelocalswitchingtable = CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable()
        self.cefcmodulelocalswitchingtable.parent = self
        self._children_name_map["cefcmodulelocalswitchingtable"] = "cefcModuleLocalSwitchingTable"
        self._children_yang_names.add("cefcModuleLocalSwitchingTable")

        self.cefcmodulepowerconsumptiontable = CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable()
        self.cefcmodulepowerconsumptiontable.parent = self
        self._children_name_map["cefcmodulepowerconsumptiontable"] = "cefcModulePowerConsumptionTable"
        self._children_yang_names.add("cefcModulePowerConsumptionTable")

        self.cefcmoduletable = CiscoEntityFruControlMib.Cefcmoduletable()
        self.cefcmoduletable.parent = self
        self._children_name_map["cefcmoduletable"] = "cefcModuleTable"
        self._children_yang_names.add("cefcModuleTable")

        self.cefcphysicaltable = CiscoEntityFruControlMib.Cefcphysicaltable()
        self.cefcphysicaltable.parent = self
        self._children_name_map["cefcphysicaltable"] = "cefcPhysicalTable"
        self._children_yang_names.add("cefcPhysicalTable")

        self.cefcpowersupplyinputtable = CiscoEntityFruControlMib.Cefcpowersupplyinputtable()
        self.cefcpowersupplyinputtable.parent = self
        self._children_name_map["cefcpowersupplyinputtable"] = "cefcPowerSupplyInputTable"
        self._children_yang_names.add("cefcPowerSupplyInputTable")

        self.cefcpowersupplyoutputtable = CiscoEntityFruControlMib.Cefcpowersupplyoutputtable()
        self.cefcpowersupplyoutputtable.parent = self
        self._children_name_map["cefcpowersupplyoutputtable"] = "cefcPowerSupplyOutputTable"
        self._children_yang_names.add("cefcPowerSupplyOutputTable")


    class Cefcfrupower(Entity):
        """
        
        
        .. attribute:: cefcmaxdefaulthighinlinepower
        
        	The system will provide power to the device connecting to the FRU if the device needs power, like an IP Phone. We call the providing power inline power.  This MIB object controls the maximum default inline power for the device connecting to the FRU in the system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: miliwatts
        
        .. attribute:: cefcmaxdefaultinlinepower
        
        	The system will provide power to the device connecting to the FRU if the device needs power, like an IP Phone. We call the providing power inline power.  This MIB object controls the maximum default inline power for the device connecting to the FRU in the system. If the maximum default inline power of the device is greater than the maximum value reportable by this object, then this object should report its maximum reportable value (12500) and cefcMaxDefaultHighInLinePower must be used to report the actual maximum default inline power
        	**type**\:  int
        
        	**range:** 0..12500
        
        	**units**\: miliwatts
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfrupower, self).__init__()

            self.yang_name = "cefcFRUPower"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcmaxdefaulthighinlinepower = YLeaf(YType.uint32, "cefcMaxDefaultHighInLinePower")

            self.cefcmaxdefaultinlinepower = YLeaf(YType.int32, "cefcMaxDefaultInLinePower")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cefcmaxdefaulthighinlinepower",
                            "cefcmaxdefaultinlinepower") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntityFruControlMib.Cefcfrupower, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfrupower, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cefcmaxdefaulthighinlinepower.is_set or
                self.cefcmaxdefaultinlinepower.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cefcmaxdefaulthighinlinepower.yfilter != YFilter.not_set or
                self.cefcmaxdefaultinlinepower.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFRUPower" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cefcmaxdefaulthighinlinepower.is_set or self.cefcmaxdefaulthighinlinepower.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefcmaxdefaulthighinlinepower.get_name_leafdata())
            if (self.cefcmaxdefaultinlinepower.is_set or self.cefcmaxdefaultinlinepower.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefcmaxdefaultinlinepower.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcMaxDefaultHighInLinePower" or name == "cefcMaxDefaultInLinePower"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cefcMaxDefaultHighInLinePower"):
                self.cefcmaxdefaulthighinlinepower = value
                self.cefcmaxdefaulthighinlinepower.value_namespace = name_space
                self.cefcmaxdefaulthighinlinepower.value_namespace_prefix = name_space_prefix
            if(value_path == "cefcMaxDefaultInLinePower"):
                self.cefcmaxdefaultinlinepower = value
                self.cefcmaxdefaultinlinepower.value_namespace = name_space
                self.cefcmaxdefaultinlinepower.value_namespace_prefix = name_space_prefix


    class Cefcmibnotificationenables(Entity):
        """
        
        
        .. attribute:: cefcenablepsoutputchangenotif
        
        	This variable indicates whether the system produces the cefcPowerSupplyOutputChange  notifications when the output capacity of  a power supply has changed. A false value  will prevent this notification to generated
        	**type**\:  bool
        
        .. attribute:: cefcmibenablestatusnotification
        
        	This variable indicates whether the system produces the following notifications\: cefcModuleStatusChange, cefcPowerStatusChange,  cefcFRUInserted, cefcFRURemoved,  cefcUnrecognizedFRU and cefcFanTrayStatusChange.  A false value will prevent these notifications from being generated
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcmibnotificationenables, self).__init__()

            self.yang_name = "cefcMIBNotificationEnables"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcenablepsoutputchangenotif = YLeaf(YType.boolean, "cefcEnablePSOutputChangeNotif")

            self.cefcmibenablestatusnotification = YLeaf(YType.boolean, "cefcMIBEnableStatusNotification")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cefcenablepsoutputchangenotif",
                            "cefcmibenablestatusnotification") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntityFruControlMib.Cefcmibnotificationenables, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcmibnotificationenables, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cefcenablepsoutputchangenotif.is_set or
                self.cefcmibenablestatusnotification.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cefcenablepsoutputchangenotif.yfilter != YFilter.not_set or
                self.cefcmibenablestatusnotification.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcMIBNotificationEnables" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cefcenablepsoutputchangenotif.is_set or self.cefcenablepsoutputchangenotif.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefcenablepsoutputchangenotif.get_name_leafdata())
            if (self.cefcmibenablestatusnotification.is_set or self.cefcmibenablestatusnotification.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefcmibenablestatusnotification.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcEnablePSOutputChangeNotif" or name == "cefcMIBEnableStatusNotification"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cefcEnablePSOutputChangeNotif"):
                self.cefcenablepsoutputchangenotif = value
                self.cefcenablepsoutputchangenotif.value_namespace = name_space
                self.cefcenablepsoutputchangenotif.value_namespace_prefix = name_space_prefix
            if(value_path == "cefcMIBEnableStatusNotification"):
                self.cefcmibenablestatusnotification = value
                self.cefcmibenablestatusnotification.value_namespace = name_space
                self.cefcmibenablestatusnotification.value_namespace_prefix = name_space_prefix


    class Cefcfrupowersupplygrouptable(Entity):
        """
        This table lists the redundancy mode and the
        operational status of the power supply groups
        in the system.
        
        .. attribute:: cefcfrupowersupplygroupentry
        
        	An cefcFRUPowerSupplyGroupTable entry lists the desired redundancy mode, the units of the power outputs and the  available and drawn current for the power supply group.  Entries are created by the agent when a power supply group is added to the entPhysicalTable. Entries are deleted by  the agent at power supply group removal
        	**type**\: list of    :py:class:`Cefcfrupowersupplygroupentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyGroupTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcfrupowersupplygroupentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable, self).__setattr__(name, value)


        class Cefcfrupowersupplygroupentry(Entity):
            """
            An cefcFRUPowerSupplyGroupTable entry lists the desired
            redundancy mode, the units of the power outputs and the 
            available and drawn current for the power supply group.
            
            Entries are created by the agent when a power supply group
            is added to the entPhysicalTable. Entries are deleted by 
            the agent at power supply group removal.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcpowernonredundantreason
            
            	This object has the value of notApplicable(1) when cefcPowerRedundancyOperMode of the instance does not have the value of nonRedundant(4).  The other values explain the reason why  cefcPowerRedundancyOperMode is nonRedundant(4), e.g.  unknown(2)             the reason is not identified.  singleSupply(3)        There is only one power supply                        in the group.  mismatchedSupplies(4)  There are more than one power                        supplies in the groups. However                        they are mismatched and can not                        work redundantly.  supplyError(5)         Some power supply or supplies                        does or do not working properly
            	**type**\:   :py:class:`Cefcpowernonredundantreason <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry.Cefcpowernonredundantreason>`
            
            .. attribute:: cefcpowerredundancymode
            
            	The administratively desired power supply redundancy mode
            	**type**\:   :py:class:`Powerredundancytype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Powerredundancytype>`
            
            .. attribute:: cefcpowerredundancyopermode
            
            	The power supply redundancy operational mode
            	**type**\:   :py:class:`Powerredundancytype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Powerredundancytype>`
            
            .. attribute:: cefcpowerunits
            
            	The units of primary supply to interpret cefcTotalAvailableCurrent and cefcTotalDrawnCurrent as power.  For example, one 1000\-watt power supply could  deliver 100 amperes at 10 volts DC.  So the value of cefcPowerUnits would be 'at 10 volts DC'.  cefcPowerUnits is for display purposes only
            	**type**\:  str
            
            .. attribute:: cefctotalavailablecurrent
            
            	Total current available for FRU usage
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefctotaldrawncurrent
            
            	Total current drawn by powered\-on FRUs
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefctotaldrawninlinecurrent
            
            	Total inline current drawn for inline operation
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyGroupEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyGroupTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcpowernonredundantreason = YLeaf(YType.enumeration, "cefcPowerNonRedundantReason")

                self.cefcpowerredundancymode = YLeaf(YType.enumeration, "cefcPowerRedundancyMode")

                self.cefcpowerredundancyopermode = YLeaf(YType.enumeration, "cefcPowerRedundancyOperMode")

                self.cefcpowerunits = YLeaf(YType.str, "cefcPowerUnits")

                self.cefctotalavailablecurrent = YLeaf(YType.int32, "cefcTotalAvailableCurrent")

                self.cefctotaldrawncurrent = YLeaf(YType.int32, "cefcTotalDrawnCurrent")

                self.cefctotaldrawninlinecurrent = YLeaf(YType.int32, "cefcTotalDrawnInlineCurrent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcpowernonredundantreason",
                                "cefcpowerredundancymode",
                                "cefcpowerredundancyopermode",
                                "cefcpowerunits",
                                "cefctotalavailablecurrent",
                                "cefctotaldrawncurrent",
                                "cefctotaldrawninlinecurrent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry, self).__setattr__(name, value)

            class Cefcpowernonredundantreason(Enum):
                """
                Cefcpowernonredundantreason

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcpowernonredundantreason.is_set or
                    self.cefcpowerredundancymode.is_set or
                    self.cefcpowerredundancyopermode.is_set or
                    self.cefcpowerunits.is_set or
                    self.cefctotalavailablecurrent.is_set or
                    self.cefctotaldrawncurrent.is_set or
                    self.cefctotaldrawninlinecurrent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcpowernonredundantreason.yfilter != YFilter.not_set or
                    self.cefcpowerredundancymode.yfilter != YFilter.not_set or
                    self.cefcpowerredundancyopermode.yfilter != YFilter.not_set or
                    self.cefcpowerunits.yfilter != YFilter.not_set or
                    self.cefctotalavailablecurrent.yfilter != YFilter.not_set or
                    self.cefctotaldrawncurrent.yfilter != YFilter.not_set or
                    self.cefctotaldrawninlinecurrent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcFRUPowerSupplyGroupEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyGroupTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcpowernonredundantreason.is_set or self.cefcpowernonredundantreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpowernonredundantreason.get_name_leafdata())
                if (self.cefcpowerredundancymode.is_set or self.cefcpowerredundancymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpowerredundancymode.get_name_leafdata())
                if (self.cefcpowerredundancyopermode.is_set or self.cefcpowerredundancyopermode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpowerredundancyopermode.get_name_leafdata())
                if (self.cefcpowerunits.is_set or self.cefcpowerunits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpowerunits.get_name_leafdata())
                if (self.cefctotalavailablecurrent.is_set or self.cefctotalavailablecurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefctotalavailablecurrent.get_name_leafdata())
                if (self.cefctotaldrawncurrent.is_set or self.cefctotaldrawncurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefctotaldrawncurrent.get_name_leafdata())
                if (self.cefctotaldrawninlinecurrent.is_set or self.cefctotaldrawninlinecurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefctotaldrawninlinecurrent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcPowerNonRedundantReason" or name == "cefcPowerRedundancyMode" or name == "cefcPowerRedundancyOperMode" or name == "cefcPowerUnits" or name == "cefcTotalAvailableCurrent" or name == "cefcTotalDrawnCurrent" or name == "cefcTotalDrawnInlineCurrent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPowerNonRedundantReason"):
                    self.cefcpowernonredundantreason = value
                    self.cefcpowernonredundantreason.value_namespace = name_space
                    self.cefcpowernonredundantreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPowerRedundancyMode"):
                    self.cefcpowerredundancymode = value
                    self.cefcpowerredundancymode.value_namespace = name_space
                    self.cefcpowerredundancymode.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPowerRedundancyOperMode"):
                    self.cefcpowerredundancyopermode = value
                    self.cefcpowerredundancyopermode.value_namespace = name_space
                    self.cefcpowerredundancyopermode.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPowerUnits"):
                    self.cefcpowerunits = value
                    self.cefcpowerunits.value_namespace = name_space
                    self.cefcpowerunits.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcTotalAvailableCurrent"):
                    self.cefctotalavailablecurrent = value
                    self.cefctotalavailablecurrent.value_namespace = name_space
                    self.cefctotalavailablecurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcTotalDrawnCurrent"):
                    self.cefctotaldrawncurrent = value
                    self.cefctotaldrawncurrent.value_namespace = name_space
                    self.cefctotaldrawncurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcTotalDrawnInlineCurrent"):
                    self.cefctotaldrawninlinecurrent = value
                    self.cefctotaldrawninlinecurrent.value_namespace = name_space
                    self.cefctotaldrawninlinecurrent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfrupowersupplygroupentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfrupowersupplygroupentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFRUPowerSupplyGroupTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcFRUPowerSupplyGroupEntry"):
                for c in self.cefcfrupowersupplygroupentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfrupowersupplygroupentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcFRUPowerSupplyGroupEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcfrupowerstatustable(Entity):
        """
        This table lists the power\-related administrative status
        and operational status of the manageable components
        in the system.
        
        .. attribute:: cefcfrupowerstatusentry
        
        	An cefcFRUPowerStatusTable entry lists the desired administrative status, the operational status of the  power manageable component, and the current required by  the component for operation.  Entries are created by the agent at system power\-up or  the insertion of the component.  Entries are deleted by the agent at the removal of the component.  Only components with power control are listed in the  table
        	**type**\: list of    :py:class:`Cefcfrupowerstatusentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfrupowerstatustable, self).__init__()

            self.yang_name = "cefcFRUPowerStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcfrupowerstatusentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcfrupowerstatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfrupowerstatustable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfrucurrent
            
            	Current supplied by the FRU (positive values) or current required to operate the FRU (negative values)
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrupoweradminstatus
            
            	Administratively desired FRU power state
            	**type**\:   :py:class:`Poweradmintype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Poweradmintype>`
            
            .. attribute:: cefcfrupowercapability
            
            	This object indicates the set of supported power capabilities of the FRU.  realTimeCurrent(0) \-     cefcFRURealTimeCurrent is supported by the FRU
            	**type**\:   :py:class:`Cefcfrupowercapability <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry.Cefcfrupowercapability>`
            
            .. attribute:: cefcfrupoweroperstatus
            
            	Operational FRU power state
            	**type**\:   :py:class:`Poweropertype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Poweropertype>`
            
            .. attribute:: cefcfrurealtimecurrent
            
            	This object indicates the realtime value of current supplied by the FRU (positive values) or the realtime value of current drawn by the FRU (negative values)
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry, self).__init__()

                self.yang_name = "cefcFRUPowerStatusEntry"
                self.yang_parent_name = "cefcFRUPowerStatusTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcfrucurrent = YLeaf(YType.int32, "cefcFRUCurrent")

                self.cefcfrupoweradminstatus = YLeaf(YType.enumeration, "cefcFRUPowerAdminStatus")

                self.cefcfrupowercapability = YLeaf(YType.bits, "cefcFRUPowerCapability")

                self.cefcfrupoweroperstatus = YLeaf(YType.enumeration, "cefcFRUPowerOperStatus")

                self.cefcfrurealtimecurrent = YLeaf(YType.int32, "cefcFRURealTimeCurrent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcfrucurrent",
                                "cefcfrupoweradminstatus",
                                "cefcfrupowercapability",
                                "cefcfrupoweroperstatus",
                                "cefcfrurealtimecurrent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcfrucurrent.is_set or
                    self.cefcfrupoweradminstatus.is_set or
                    self.cefcfrupowercapability.is_set or
                    self.cefcfrupoweroperstatus.is_set or
                    self.cefcfrurealtimecurrent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcfrucurrent.yfilter != YFilter.not_set or
                    self.cefcfrupoweradminstatus.yfilter != YFilter.not_set or
                    self.cefcfrupowercapability.yfilter != YFilter.not_set or
                    self.cefcfrupoweroperstatus.yfilter != YFilter.not_set or
                    self.cefcfrurealtimecurrent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcFRUPowerStatusEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcfrucurrent.is_set or self.cefcfrucurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrucurrent.get_name_leafdata())
                if (self.cefcfrupoweradminstatus.is_set or self.cefcfrupoweradminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrupoweradminstatus.get_name_leafdata())
                if (self.cefcfrupowercapability.is_set or self.cefcfrupowercapability.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrupowercapability.get_name_leafdata())
                if (self.cefcfrupoweroperstatus.is_set or self.cefcfrupoweroperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrupoweroperstatus.get_name_leafdata())
                if (self.cefcfrurealtimecurrent.is_set or self.cefcfrurealtimecurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrurealtimecurrent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcFRUCurrent" or name == "cefcFRUPowerAdminStatus" or name == "cefcFRUPowerCapability" or name == "cefcFRUPowerOperStatus" or name == "cefcFRURealTimeCurrent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUCurrent"):
                    self.cefcfrucurrent = value
                    self.cefcfrucurrent.value_namespace = name_space
                    self.cefcfrucurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUPowerAdminStatus"):
                    self.cefcfrupoweradminstatus = value
                    self.cefcfrupoweradminstatus.value_namespace = name_space
                    self.cefcfrupoweradminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUPowerCapability"):
                    self.cefcfrupowercapability[value] = True
                if(value_path == "cefcFRUPowerOperStatus"):
                    self.cefcfrupoweroperstatus = value
                    self.cefcfrupoweroperstatus.value_namespace = name_space
                    self.cefcfrupoweroperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRURealTimeCurrent"):
                    self.cefcfrurealtimecurrent = value
                    self.cefcfrurealtimecurrent.value_namespace = name_space
                    self.cefcfrurealtimecurrent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfrupowerstatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfrupowerstatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFRUPowerStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcFRUPowerStatusEntry"):
                for c in self.cefcfrupowerstatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfrupowerstatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcFRUPowerStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cefcfrupowersupplyvalueentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable, self).__init__()

            self.yang_name = "cefcFRUPowerSupplyValueTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcfrupowersupplyvalueentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable, self).__setattr__(name, value)


        class Cefcfrupowersupplyvalueentry(Entity):
            """
            An cefcFRUPowerSupplyValueTable entry lists the current
            provided by the FRU for operation.
            
            Entries are created by the agent at system power\-up or 
            FRU insertion.  Entries are deleted by the agent at FRU
            removal.
            
            Only power supply FRUs are listed in the table.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfrudrawninlinecurrent
            
            	Amount of current that is being drawn from this FRU for inline operation
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrudrawnsystemcurrent
            
            	Amount of current drawn by the FRU's in the system towards system operations from this FRU
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrutotalinlinecurrent
            
            	Total current supplied by the FRU (positive values) for inline operations
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrutotalsystemcurrent
            
            	Total current that could be supplied by the FRU (positive values) for system operations
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry, self).__init__()

                self.yang_name = "cefcFRUPowerSupplyValueEntry"
                self.yang_parent_name = "cefcFRUPowerSupplyValueTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcfrudrawninlinecurrent = YLeaf(YType.int32, "cefcFRUDrawnInlineCurrent")

                self.cefcfrudrawnsystemcurrent = YLeaf(YType.int32, "cefcFRUDrawnSystemCurrent")

                self.cefcfrutotalinlinecurrent = YLeaf(YType.int32, "cefcFRUTotalInlineCurrent")

                self.cefcfrutotalsystemcurrent = YLeaf(YType.int32, "cefcFRUTotalSystemCurrent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcfrudrawninlinecurrent",
                                "cefcfrudrawnsystemcurrent",
                                "cefcfrutotalinlinecurrent",
                                "cefcfrutotalsystemcurrent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcfrudrawninlinecurrent.is_set or
                    self.cefcfrudrawnsystemcurrent.is_set or
                    self.cefcfrutotalinlinecurrent.is_set or
                    self.cefcfrutotalsystemcurrent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcfrudrawninlinecurrent.yfilter != YFilter.not_set or
                    self.cefcfrudrawnsystemcurrent.yfilter != YFilter.not_set or
                    self.cefcfrutotalinlinecurrent.yfilter != YFilter.not_set or
                    self.cefcfrutotalsystemcurrent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcFRUPowerSupplyValueEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFRUPowerSupplyValueTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcfrudrawninlinecurrent.is_set or self.cefcfrudrawninlinecurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrudrawninlinecurrent.get_name_leafdata())
                if (self.cefcfrudrawnsystemcurrent.is_set or self.cefcfrudrawnsystemcurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrudrawnsystemcurrent.get_name_leafdata())
                if (self.cefcfrutotalinlinecurrent.is_set or self.cefcfrutotalinlinecurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrutotalinlinecurrent.get_name_leafdata())
                if (self.cefcfrutotalsystemcurrent.is_set or self.cefcfrutotalsystemcurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfrutotalsystemcurrent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcFRUDrawnInlineCurrent" or name == "cefcFRUDrawnSystemCurrent" or name == "cefcFRUTotalInlineCurrent" or name == "cefcFRUTotalSystemCurrent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUDrawnInlineCurrent"):
                    self.cefcfrudrawninlinecurrent = value
                    self.cefcfrudrawninlinecurrent.value_namespace = name_space
                    self.cefcfrudrawninlinecurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUDrawnSystemCurrent"):
                    self.cefcfrudrawnsystemcurrent = value
                    self.cefcfrudrawnsystemcurrent.value_namespace = name_space
                    self.cefcfrudrawnsystemcurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUTotalInlineCurrent"):
                    self.cefcfrutotalinlinecurrent = value
                    self.cefcfrutotalinlinecurrent.value_namespace = name_space
                    self.cefcfrutotalinlinecurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFRUTotalSystemCurrent"):
                    self.cefcfrutotalsystemcurrent = value
                    self.cefcfrutotalsystemcurrent.value_namespace = name_space
                    self.cefcfrutotalsystemcurrent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfrupowersupplyvalueentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfrupowersupplyvalueentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFRUPowerSupplyValueTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcFRUPowerSupplyValueEntry"):
                for c in self.cefcfrupowersupplyvalueentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfrupowersupplyvalueentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcFRUPowerSupplyValueEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcmoduletable(Entity):
        """
        A cefcModuleTable entry lists the operational and
        administrative status information for ENTITY\-MIB
        entPhysicalTable entries for manageable components
        of type PhysicalClass module(9).
        
        .. attribute:: cefcmoduleentry
        
        	A cefcModuleStatusTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components  of type PhysicalClass module(9).  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of    :py:class:`Cefcmoduleentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcmoduletable, self).__init__()

            self.yang_name = "cefcModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcmoduleentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcmoduletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcmoduletable, self).__setattr__(name, value)


        class Cefcmoduleentry(Entity):
            """
            A cefcModuleStatusTable entry lists the operational and
            administrative status information for ENTITY\-MIB
            entPhysicalTable entries for manageable components 
            of type PhysicalClass module(9).
            
            Entries are created by the agent at the system power\-up or
            module insertion.
            
            Entries are deleted by the agent upon module removal.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmoduleadminstatus
            
            	This object provides administrative control of the module
            	**type**\:   :py:class:`Moduleadmintype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Moduleadmintype>`
            
            .. attribute:: cefcmodulelastclearconfigtime
            
            	The value of sysUpTime when the configuration was most recently cleared
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmoduleoperstatus
            
            	This object shows the module's operational state
            	**type**\:   :py:class:`Moduleopertype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Moduleopertype>`
            
            .. attribute:: cefcmoduleresetreason
            
            	This object identifies the reason for the last reset performed on the module
            	**type**\:   :py:class:`Moduleresetreasontype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Moduleresetreasontype>`
            
            .. attribute:: cefcmoduleresetreasondescription
            
            	A description qualifying the module reset reason specified in cefcModuleResetReason.   Examples\:   command xyz                 missing task   switch over   watchdog timeout       etc.  cefcModuleResetReasonDescription is for display purposes only. NMS applications must not parse
            	**type**\:  str
            
            .. attribute:: cefcmodulestatechangereasondescr
            
            	This object displays human\-readable textual string which describes the cause of the last state change of the module. This object contains zero length string if no meaningful reason could be provided.  Examples\: 'Invalid software version' 'Software download failed' 'Software version mismatch' 'Module is in standby state' etc.  This object is for display purposes only. NMS applications must not parse this object and take any decision based on its value
            	**type**\:  str
            
            .. attribute:: cefcmodulestatuslastchangetime
            
            	The value of sysUpTime at the time the cefcModuleOperStatus is changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmoduleuptime
            
            	This object provides the up time for the module since it was last re\-initialized.  This object is not persistent; if a module reset, restart, power off, the up time starts from zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry, self).__init__()

                self.yang_name = "cefcModuleEntry"
                self.yang_parent_name = "cefcModuleTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcmoduleadminstatus = YLeaf(YType.enumeration, "cefcModuleAdminStatus")

                self.cefcmodulelastclearconfigtime = YLeaf(YType.uint32, "cefcModuleLastClearConfigTime")

                self.cefcmoduleoperstatus = YLeaf(YType.enumeration, "cefcModuleOperStatus")

                self.cefcmoduleresetreason = YLeaf(YType.enumeration, "cefcModuleResetReason")

                self.cefcmoduleresetreasondescription = YLeaf(YType.str, "cefcModuleResetReasonDescription")

                self.cefcmodulestatechangereasondescr = YLeaf(YType.str, "cefcModuleStateChangeReasonDescr")

                self.cefcmodulestatuslastchangetime = YLeaf(YType.uint32, "cefcModuleStatusLastChangeTime")

                self.cefcmoduleuptime = YLeaf(YType.uint32, "cefcModuleUpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcmoduleadminstatus",
                                "cefcmodulelastclearconfigtime",
                                "cefcmoduleoperstatus",
                                "cefcmoduleresetreason",
                                "cefcmoduleresetreasondescription",
                                "cefcmodulestatechangereasondescr",
                                "cefcmodulestatuslastchangetime",
                                "cefcmoduleuptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcmoduleadminstatus.is_set or
                    self.cefcmodulelastclearconfigtime.is_set or
                    self.cefcmoduleoperstatus.is_set or
                    self.cefcmoduleresetreason.is_set or
                    self.cefcmoduleresetreasondescription.is_set or
                    self.cefcmodulestatechangereasondescr.is_set or
                    self.cefcmodulestatuslastchangetime.is_set or
                    self.cefcmoduleuptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcmoduleadminstatus.yfilter != YFilter.not_set or
                    self.cefcmodulelastclearconfigtime.yfilter != YFilter.not_set or
                    self.cefcmoduleoperstatus.yfilter != YFilter.not_set or
                    self.cefcmoduleresetreason.yfilter != YFilter.not_set or
                    self.cefcmoduleresetreasondescription.yfilter != YFilter.not_set or
                    self.cefcmodulestatechangereasondescr.yfilter != YFilter.not_set or
                    self.cefcmodulestatuslastchangetime.yfilter != YFilter.not_set or
                    self.cefcmoduleuptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcModuleEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcmoduleadminstatus.is_set or self.cefcmoduleadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmoduleadminstatus.get_name_leafdata())
                if (self.cefcmodulelastclearconfigtime.is_set or self.cefcmodulelastclearconfigtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulelastclearconfigtime.get_name_leafdata())
                if (self.cefcmoduleoperstatus.is_set or self.cefcmoduleoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmoduleoperstatus.get_name_leafdata())
                if (self.cefcmoduleresetreason.is_set or self.cefcmoduleresetreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmoduleresetreason.get_name_leafdata())
                if (self.cefcmoduleresetreasondescription.is_set or self.cefcmoduleresetreasondescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmoduleresetreasondescription.get_name_leafdata())
                if (self.cefcmodulestatechangereasondescr.is_set or self.cefcmodulestatechangereasondescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulestatechangereasondescr.get_name_leafdata())
                if (self.cefcmodulestatuslastchangetime.is_set or self.cefcmodulestatuslastchangetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulestatuslastchangetime.get_name_leafdata())
                if (self.cefcmoduleuptime.is_set or self.cefcmoduleuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmoduleuptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcModuleAdminStatus" or name == "cefcModuleLastClearConfigTime" or name == "cefcModuleOperStatus" or name == "cefcModuleResetReason" or name == "cefcModuleResetReasonDescription" or name == "cefcModuleStateChangeReasonDescr" or name == "cefcModuleStatusLastChangeTime" or name == "cefcModuleUpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleAdminStatus"):
                    self.cefcmoduleadminstatus = value
                    self.cefcmoduleadminstatus.value_namespace = name_space
                    self.cefcmoduleadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleLastClearConfigTime"):
                    self.cefcmodulelastclearconfigtime = value
                    self.cefcmodulelastclearconfigtime.value_namespace = name_space
                    self.cefcmodulelastclearconfigtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleOperStatus"):
                    self.cefcmoduleoperstatus = value
                    self.cefcmoduleoperstatus.value_namespace = name_space
                    self.cefcmoduleoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleResetReason"):
                    self.cefcmoduleresetreason = value
                    self.cefcmoduleresetreason.value_namespace = name_space
                    self.cefcmoduleresetreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleResetReasonDescription"):
                    self.cefcmoduleresetreasondescription = value
                    self.cefcmoduleresetreasondescription.value_namespace = name_space
                    self.cefcmoduleresetreasondescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleStateChangeReasonDescr"):
                    self.cefcmodulestatechangereasondescr = value
                    self.cefcmodulestatechangereasondescr.value_namespace = name_space
                    self.cefcmodulestatechangereasondescr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleStatusLastChangeTime"):
                    self.cefcmodulestatuslastchangetime = value
                    self.cefcmodulestatuslastchangetime.value_namespace = name_space
                    self.cefcmodulestatuslastchangetime.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleUpTime"):
                    self.cefcmoduleuptime = value
                    self.cefcmoduleuptime.value_namespace = name_space
                    self.cefcmoduleuptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcmoduleentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcmoduleentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcModuleTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcModuleEntry"):
                for c in self.cefcmoduleentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcmoduleentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcModuleEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cefcintellimoduleentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcintellimoduletable, self).__init__()

            self.yang_name = "cefcIntelliModuleTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcintellimoduleentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcintellimoduletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcintellimoduletable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcintellimoduleipaddr
            
            	The Internet address configured for the intelligent module. The type of this address is  determined by the value of the object  cefcIntelliModuleIPAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cefcintellimoduleipaddrtype
            
            	The type of Internet address by which the intelligent module is reachable
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry, self).__init__()

                self.yang_name = "cefcIntelliModuleEntry"
                self.yang_parent_name = "cefcIntelliModuleTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcintellimoduleipaddr = YLeaf(YType.str, "cefcIntelliModuleIPAddr")

                self.cefcintellimoduleipaddrtype = YLeaf(YType.enumeration, "cefcIntelliModuleIPAddrType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcintellimoduleipaddr",
                                "cefcintellimoduleipaddrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcintellimoduleipaddr.is_set or
                    self.cefcintellimoduleipaddrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcintellimoduleipaddr.yfilter != YFilter.not_set or
                    self.cefcintellimoduleipaddrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcIntelliModuleEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcIntelliModuleTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcintellimoduleipaddr.is_set or self.cefcintellimoduleipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcintellimoduleipaddr.get_name_leafdata())
                if (self.cefcintellimoduleipaddrtype.is_set or self.cefcintellimoduleipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcintellimoduleipaddrtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcIntelliModuleIPAddr" or name == "cefcIntelliModuleIPAddrType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcIntelliModuleIPAddr"):
                    self.cefcintellimoduleipaddr = value
                    self.cefcintellimoduleipaddr.value_namespace = name_space
                    self.cefcintellimoduleipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcIntelliModuleIPAddrType"):
                    self.cefcintellimoduleipaddrtype = value
                    self.cefcintellimoduleipaddrtype.value_namespace = name_space
                    self.cefcintellimoduleipaddrtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcintellimoduleentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcintellimoduleentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcIntelliModuleTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcIntelliModuleEntry"):
                for c in self.cefcintellimoduleentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcintellimoduleentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcIntelliModuleEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cefcmodulelocalswitchingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable, self).__init__()

            self.yang_name = "cefcModuleLocalSwitchingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcmodulelocalswitchingentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmodulelocalswitchingmode
            
            	This object specifies the mode of local switching.  enabled(1)  \- local switching is enabled. disabled(2) \- local switching is disabled
            	**type**\:   :py:class:`Cefcmodulelocalswitchingmode <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry.Cefcmodulelocalswitchingmode>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry, self).__init__()

                self.yang_name = "cefcModuleLocalSwitchingEntry"
                self.yang_parent_name = "cefcModuleLocalSwitchingTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcmodulelocalswitchingmode = YLeaf(YType.enumeration, "cefcModuleLocalSwitchingMode")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcmodulelocalswitchingmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry, self).__setattr__(name, value)

            class Cefcmodulelocalswitchingmode(Enum):
                """
                Cefcmodulelocalswitchingmode

                This object specifies the mode of local switching.

                enabled(1)  \- local switching is enabled.

                disabled(2) \- local switching is disabled.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcmodulelocalswitchingmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcmodulelocalswitchingmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcModuleLocalSwitchingEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleLocalSwitchingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcmodulelocalswitchingmode.is_set or self.cefcmodulelocalswitchingmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulelocalswitchingmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcModuleLocalSwitchingMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleLocalSwitchingMode"):
                    self.cefcmodulelocalswitchingmode = value
                    self.cefcmodulelocalswitchingmode.value_namespace = name_space
                    self.cefcmodulelocalswitchingmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcmodulelocalswitchingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcmodulelocalswitchingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcModuleLocalSwitchingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcModuleLocalSwitchingEntry"):
                for c in self.cefcmodulelocalswitchingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcmodulelocalswitchingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcModuleLocalSwitchingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cefcfantraystatusentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfantraystatustable, self).__init__()

            self.yang_name = "cefcFanTrayStatusTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcfantraystatusentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcfantraystatustable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfantraystatustable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfantrayoperstatus
            
            	The operational state of the fan or fan tray. unknown(1) \- unknown. up(2) \- powered on. down(3) \- powered down. warning(4) \- partial failure, needs replacement               as soon as possible
            	**type**\:   :py:class:`Cefcfantrayoperstatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry.Cefcfantrayoperstatus>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry, self).__init__()

                self.yang_name = "cefcFanTrayStatusEntry"
                self.yang_parent_name = "cefcFanTrayStatusTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcfantrayoperstatus = YLeaf(YType.enumeration, "cefcFanTrayOperStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcfantrayoperstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry, self).__setattr__(name, value)

            class Cefcfantrayoperstatus(Enum):
                """
                Cefcfantrayoperstatus

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcfantrayoperstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcfantrayoperstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcFanTrayStatusEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanTrayStatusTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcfantrayoperstatus.is_set or self.cefcfantrayoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfantrayoperstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcFanTrayOperStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanTrayOperStatus"):
                    self.cefcfantrayoperstatus = value
                    self.cefcfantrayoperstatus.value_namespace = name_space
                    self.cefcfantrayoperstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfantraystatusentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfantraystatusentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFanTrayStatusTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcFanTrayStatusEntry"):
                for c in self.cefcfantraystatusentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfantraystatusentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcFanTrayStatusEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcphysicaltable(Entity):
        """
        This table contains one row per physical entity.
        
        .. attribute:: cefcphysicalentry
        
        	Information about a particular physical entity
        	**type**\: list of    :py:class:`Cefcphysicalentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcphysicaltable, self).__init__()

            self.yang_name = "cefcPhysicalTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcphysicalentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcphysicaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcphysicaltable, self).__setattr__(name, value)


        class Cefcphysicalentry(Entity):
            """
            Information about a particular physical entity.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcphysicalstatus
            
            	The status of this physical entity. other(1) \- the status is not any of the listed below. supported(2) \- this entity is supported. unsupported(3) \- this entity is unsupported. incompatible(4) \- this entity is incompatible. It would be unsupported(3), if the ID read from Serial EPROM is not supported. It would be incompatible(4), if in the present configuration this FRU is not supported
            	**type**\:   :py:class:`Cefcphysicalstatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry.Cefcphysicalstatus>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry, self).__init__()

                self.yang_name = "cefcPhysicalEntry"
                self.yang_parent_name = "cefcPhysicalTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcphysicalstatus = YLeaf(YType.enumeration, "cefcPhysicalStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcphysicalstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry, self).__setattr__(name, value)

            class Cefcphysicalstatus(Enum):
                """
                Cefcphysicalstatus

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcphysicalstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcphysicalstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcPhysicalEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPhysicalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcphysicalstatus.is_set or self.cefcphysicalstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcphysicalstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcPhysicalStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPhysicalStatus"):
                    self.cefcphysicalstatus = value
                    self.cefcphysicalstatus.value_namespace = name_space
                    self.cefcphysicalstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcphysicalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcphysicalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcPhysicalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcPhysicalEntry"):
                for c in self.cefcphysicalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcphysicalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcPhysicalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cefcpowersupplyinputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcpowersupplyinputtable, self).__init__()

            self.yang_name = "cefcPowerSupplyInputTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcpowersupplyinputentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcpowersupplyinputtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcpowersupplyinputtable, self).__setattr__(name, value)


        class Cefcpowersupplyinputentry(Entity):
            """
            An entry containing power input management information
            applicable to a particular power supply and input.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcpowersupplyinputindex  <key>
            
            	A unique value, greater than zero, for each input on a power supply
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcpowersupplyinputtype
            
            	The type of an input power detected on the power supply.  unknown(1)\: No input power is detected.  acLow(2)\: Lower rating AC input power is detected.  acHigh(3)\: Higher rating AC input power is detected.  dcLow(4)\: Lower rating DC input power is detected.  dcHigh(5)\: Higher rating DC input power is detected
            	**type**\:   :py:class:`Cefcpowersupplyinputtype <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry.Cefcpowersupplyinputtype>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry, self).__init__()

                self.yang_name = "cefcPowerSupplyInputEntry"
                self.yang_parent_name = "cefcPowerSupplyInputTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcpowersupplyinputindex = YLeaf(YType.uint32, "cefcPowerSupplyInputIndex")

                self.cefcpowersupplyinputtype = YLeaf(YType.enumeration, "cefcPowerSupplyInputType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcpowersupplyinputindex",
                                "cefcpowersupplyinputtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry, self).__setattr__(name, value)

            class Cefcpowersupplyinputtype(Enum):
                """
                Cefcpowersupplyinputtype

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcpowersupplyinputindex.is_set or
                    self.cefcpowersupplyinputtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcpowersupplyinputindex.yfilter != YFilter.not_set or
                    self.cefcpowersupplyinputtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcPowerSupplyInputEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefcPowerSupplyInputIndex='" + self.cefcpowersupplyinputindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPowerSupplyInputTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcpowersupplyinputindex.is_set or self.cefcpowersupplyinputindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpowersupplyinputindex.get_name_leafdata())
                if (self.cefcpowersupplyinputtype.is_set or self.cefcpowersupplyinputtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpowersupplyinputtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcPowerSupplyInputIndex" or name == "cefcPowerSupplyInputType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPowerSupplyInputIndex"):
                    self.cefcpowersupplyinputindex = value
                    self.cefcpowersupplyinputindex.value_namespace = name_space
                    self.cefcpowersupplyinputindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPowerSupplyInputType"):
                    self.cefcpowersupplyinputtype = value
                    self.cefcpowersupplyinputtype.value_namespace = name_space
                    self.cefcpowersupplyinputtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcpowersupplyinputentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcpowersupplyinputentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcPowerSupplyInputTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcPowerSupplyInputEntry"):
                for c in self.cefcpowersupplyinputentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcpowersupplyinputentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcPowerSupplyInputEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcpowersupplyoutputtable(Entity):
        """
        This table contains a list of possible output
        mode for the power supplies, whose ENTITY\-MIB
        entPhysicalTable entries have an entPhysicalClass
        of 'powerSupply'. It also indicate which mode
        is the operational mode within the system.
        
        .. attribute:: cefcpowersupplyoutputentry
        
        	A cefcPowerSupplyOutputTable entry lists the power output capacity and its operational status for manageable components of type PhysicalClass 'powerSupply'.  Entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries of a power supply is determined by the power supply
        	**type**\: list of    :py:class:`Cefcpowersupplyoutputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcpowersupplyoutputtable, self).__init__()

            self.yang_name = "cefcPowerSupplyOutputTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcpowersupplyoutputentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcpowersupplyoutputtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcpowersupplyoutputtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcpsoutputmodeindex  <key>
            
            	A unique value, greater than zero, for each possible output mode on a power supply
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcpsoutputmodecurrent
            
            	The output capacity of the power supply
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcpsoutputmodeinoperation
            
            	A value of 'true' indicates that this mode is the operational mode of the power supply output capacity.  A value of 'false' indicates that this mode is not the operational mode of the power supply output capacity.  For a given power supply's entPhysicalIndex,  at most one instance of this object can have the value of true(1)
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry, self).__init__()

                self.yang_name = "cefcPowerSupplyOutputEntry"
                self.yang_parent_name = "cefcPowerSupplyOutputTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcpsoutputmodeindex = YLeaf(YType.uint32, "cefcPSOutputModeIndex")

                self.cefcpsoutputmodecurrent = YLeaf(YType.int32, "cefcPSOutputModeCurrent")

                self.cefcpsoutputmodeinoperation = YLeaf(YType.boolean, "cefcPSOutputModeInOperation")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcpsoutputmodeindex",
                                "cefcpsoutputmodecurrent",
                                "cefcpsoutputmodeinoperation") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcpsoutputmodeindex.is_set or
                    self.cefcpsoutputmodecurrent.is_set or
                    self.cefcpsoutputmodeinoperation.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcpsoutputmodeindex.yfilter != YFilter.not_set or
                    self.cefcpsoutputmodecurrent.yfilter != YFilter.not_set or
                    self.cefcpsoutputmodeinoperation.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcPowerSupplyOutputEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefcPSOutputModeIndex='" + self.cefcpsoutputmodeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcPowerSupplyOutputTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcpsoutputmodeindex.is_set or self.cefcpsoutputmodeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpsoutputmodeindex.get_name_leafdata())
                if (self.cefcpsoutputmodecurrent.is_set or self.cefcpsoutputmodecurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpsoutputmodecurrent.get_name_leafdata())
                if (self.cefcpsoutputmodeinoperation.is_set or self.cefcpsoutputmodeinoperation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcpsoutputmodeinoperation.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcPSOutputModeIndex" or name == "cefcPSOutputModeCurrent" or name == "cefcPSOutputModeInOperation"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPSOutputModeIndex"):
                    self.cefcpsoutputmodeindex = value
                    self.cefcpsoutputmodeindex.value_namespace = name_space
                    self.cefcpsoutputmodeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPSOutputModeCurrent"):
                    self.cefcpsoutputmodecurrent = value
                    self.cefcpsoutputmodecurrent.value_namespace = name_space
                    self.cefcpsoutputmodecurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcPSOutputModeInOperation"):
                    self.cefcpsoutputmodeinoperation = value
                    self.cefcpsoutputmodeinoperation.value_namespace = name_space
                    self.cefcpsoutputmodeinoperation.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcpowersupplyoutputentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcpowersupplyoutputentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcPowerSupplyOutputTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcPowerSupplyOutputEntry"):
                for c in self.cefcpowersupplyoutputentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcpowersupplyoutputentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcPowerSupplyOutputEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcchassiscoolingtable(Entity):
        """
        This table contains the cooling capacity
        information of the chassis whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'chassis'.
        
        .. attribute:: cefcchassiscoolingentry
        
        	A cefcChassisCoolingEntry lists the maximum cooling capacity that could be provided  for one slot on the manageable components of type PhysicalClass 'chassis'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of    :py:class:`Cefcchassiscoolingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcchassiscoolingtable, self).__init__()

            self.yang_name = "cefcChassisCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcchassiscoolingentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcchassiscoolingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcchassiscoolingtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcchassisperslotcoolingcap
            
            	The maximum cooling capacity that could be provided for any slot in this chassis.  The default unit of the cooling capacity is 'cfm', if cefcChassisPerSlotCoolingUnit is not supported
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcchassisperslotcoolingunit
            
            	The unit of the maximum cooling capacity for any slot in this chassis
            	**type**\:   :py:class:`Frucoolingunit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Frucoolingunit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry, self).__init__()

                self.yang_name = "cefcChassisCoolingEntry"
                self.yang_parent_name = "cefcChassisCoolingTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcchassisperslotcoolingcap = YLeaf(YType.uint32, "cefcChassisPerSlotCoolingCap")

                self.cefcchassisperslotcoolingunit = YLeaf(YType.enumeration, "cefcChassisPerSlotCoolingUnit")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcchassisperslotcoolingcap",
                                "cefcchassisperslotcoolingunit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcchassisperslotcoolingcap.is_set or
                    self.cefcchassisperslotcoolingunit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcchassisperslotcoolingcap.yfilter != YFilter.not_set or
                    self.cefcchassisperslotcoolingunit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcChassisCoolingEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcChassisCoolingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcchassisperslotcoolingcap.is_set or self.cefcchassisperslotcoolingcap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcchassisperslotcoolingcap.get_name_leafdata())
                if (self.cefcchassisperslotcoolingunit.is_set or self.cefcchassisperslotcoolingunit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcchassisperslotcoolingunit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcChassisPerSlotCoolingCap" or name == "cefcChassisPerSlotCoolingUnit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcChassisPerSlotCoolingCap"):
                    self.cefcchassisperslotcoolingcap = value
                    self.cefcchassisperslotcoolingcap.value_namespace = name_space
                    self.cefcchassisperslotcoolingcap.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcChassisPerSlotCoolingUnit"):
                    self.cefcchassisperslotcoolingunit = value
                    self.cefcchassisperslotcoolingunit.value_namespace = name_space
                    self.cefcchassisperslotcoolingunit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcchassiscoolingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcchassiscoolingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcChassisCoolingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcChassisCoolingEntry"):
                for c in self.cefcchassiscoolingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcchassiscoolingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcChassisCoolingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcfancoolingtable(Entity):
        """
        This table contains the cooling capacity
        information of the fans whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingentry
        
        	A cefcFanCoolingEntry lists the cooling capacity that is provided by the  manageable components of type PhysicalClass  'fan'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of    :py:class:`Cefcfancoolingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfancoolingtable, self).__init__()

            self.yang_name = "cefcFanCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcfancoolingentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcfancoolingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfancoolingtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfancoolingcapacity
            
            	The cooling capacity that is provided by this fan.  The default unit of the fan cooling capacity is 'cfm', if cefcFanCoolingCapacityUnit is not supported
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfancoolingcapacityunit
            
            	The unit of the fan cooling capacity
            	**type**\:   :py:class:`Frucoolingunit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Frucoolingunit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry, self).__init__()

                self.yang_name = "cefcFanCoolingEntry"
                self.yang_parent_name = "cefcFanCoolingTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcfancoolingcapacity = YLeaf(YType.uint32, "cefcFanCoolingCapacity")

                self.cefcfancoolingcapacityunit = YLeaf(YType.enumeration, "cefcFanCoolingCapacityUnit")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcfancoolingcapacity",
                                "cefcfancoolingcapacityunit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcfancoolingcapacity.is_set or
                    self.cefcfancoolingcapacityunit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapacity.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapacityunit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcFanCoolingEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanCoolingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcfancoolingcapacity.is_set or self.cefcfancoolingcapacity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapacity.get_name_leafdata())
                if (self.cefcfancoolingcapacityunit.is_set or self.cefcfancoolingcapacityunit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapacityunit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcFanCoolingCapacity" or name == "cefcFanCoolingCapacityUnit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapacity"):
                    self.cefcfancoolingcapacity = value
                    self.cefcfancoolingcapacity.value_namespace = name_space
                    self.cefcfancoolingcapacity.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapacityUnit"):
                    self.cefcfancoolingcapacityunit = value
                    self.cefcfancoolingcapacityunit.value_namespace = name_space
                    self.cefcfancoolingcapacityunit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfancoolingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfancoolingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFanCoolingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcFanCoolingEntry"):
                for c in self.cefcfancoolingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfancoolingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcFanCoolingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcmodulecoolingtable(Entity):
        """
        This table contains the cooling requirement for
        all the manageable components of type entPhysicalClass
        'module'.
        
        .. attribute:: cefcmodulecoolingentry
        
        	A cefcModuleCoolingEntry lists the cooling requirement for a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of    :py:class:`Cefcmodulecoolingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcmodulecoolingtable, self).__init__()

            self.yang_name = "cefcModuleCoolingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcmodulecoolingentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcmodulecoolingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcmodulecoolingtable, self).__setattr__(name, value)


        class Cefcmodulecoolingentry(Entity):
            """
            A cefcModuleCoolingEntry lists the cooling
            requirement for a manageable components of type
            entPhysicalClass 'module'.
            
            Entries are created by the agent at the system
            power\-up or module insertion.
            
            Entries are deleted by the agent upon module
            removal.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmodulecooling
            
            	The cooling requirement of the module and its daughter cards.  The default unit of the module cooling requirement is 'cfm', if cefcModuleCoolingUnit is not supported
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmodulecoolingunit
            
            	The unit of the cooling requirement of the module and its daughter cards
            	**type**\:   :py:class:`Frucoolingunit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Frucoolingunit>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry, self).__init__()

                self.yang_name = "cefcModuleCoolingEntry"
                self.yang_parent_name = "cefcModuleCoolingTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcmodulecooling = YLeaf(YType.uint32, "cefcModuleCooling")

                self.cefcmodulecoolingunit = YLeaf(YType.enumeration, "cefcModuleCoolingUnit")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcmodulecooling",
                                "cefcmodulecoolingunit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcmodulecooling.is_set or
                    self.cefcmodulecoolingunit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcmodulecooling.yfilter != YFilter.not_set or
                    self.cefcmodulecoolingunit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcModuleCoolingEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModuleCoolingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcmodulecooling.is_set or self.cefcmodulecooling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulecooling.get_name_leafdata())
                if (self.cefcmodulecoolingunit.is_set or self.cefcmodulecoolingunit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulecoolingunit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcModuleCooling" or name == "cefcModuleCoolingUnit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleCooling"):
                    self.cefcmodulecooling = value
                    self.cefcmodulecooling.value_namespace = name_space
                    self.cefcmodulecooling.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModuleCoolingUnit"):
                    self.cefcmodulecoolingunit = value
                    self.cefcmodulecoolingunit.value_namespace = name_space
                    self.cefcmodulecoolingunit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcmodulecoolingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcmodulecoolingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcModuleCoolingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcModuleCoolingEntry"):
                for c in self.cefcmodulecoolingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcmodulecoolingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcModuleCoolingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcfancoolingcaptable(Entity):
        """
        This table contains a list of the possible cooling
        capacity modes and properties of the fans, whose 
        ENTITY\-MIB entPhysicalTable entries have an 
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingcapentry
        
        	A cefcFanCoolingCapacityEntry lists the cooling capacity mode of a manageable components of type entPhysicalClass 'fan'. It also lists the corresponding cooling capacity provided and the power consumed by the fan on this mode.   Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of    :py:class:`Cefcfancoolingcapentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcfancoolingcaptable, self).__init__()

            self.yang_name = "cefcFanCoolingCapTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcfancoolingcapentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcfancoolingcaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcfancoolingcaptable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcfancoolingcapindex  <key>
            
            	An arbitrary value that uniquely identifies a cooling capacity mode for a fan
            	**type**\:  int
            
            	**range:** 1..4095
            
            .. attribute:: cefcfancoolingcapcapacity
            
            	The cooling capacity that could be provided when the fan is operating in this mode.  The default unit of the cooling capacity is 'cfm', if cefcFanCoolingCapCapacityUnit is not supported
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfancoolingcapcapacityunit
            
            	The unit of the fan cooling capacity when operating in this mode
            	**type**\:   :py:class:`Frucoolingunit <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.Frucoolingunit>`
            
            .. attribute:: cefcfancoolingcapcurrent
            
            	The power consumption of the fan when operating in in this mode
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfancoolingcapmodedescr
            
            	A textual description of the cooling capacity mode of the fan
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry, self).__init__()

                self.yang_name = "cefcFanCoolingCapEntry"
                self.yang_parent_name = "cefcFanCoolingCapTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcfancoolingcapindex = YLeaf(YType.uint32, "cefcFanCoolingCapIndex")

                self.cefcfancoolingcapcapacity = YLeaf(YType.uint32, "cefcFanCoolingCapCapacity")

                self.cefcfancoolingcapcapacityunit = YLeaf(YType.enumeration, "cefcFanCoolingCapCapacityUnit")

                self.cefcfancoolingcapcurrent = YLeaf(YType.int32, "cefcFanCoolingCapCurrent")

                self.cefcfancoolingcapmodedescr = YLeaf(YType.str, "cefcFanCoolingCapModeDescr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcfancoolingcapindex",
                                "cefcfancoolingcapcapacity",
                                "cefcfancoolingcapcapacityunit",
                                "cefcfancoolingcapcurrent",
                                "cefcfancoolingcapmodedescr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcfancoolingcapindex.is_set or
                    self.cefcfancoolingcapcapacity.is_set or
                    self.cefcfancoolingcapcapacityunit.is_set or
                    self.cefcfancoolingcapcurrent.is_set or
                    self.cefcfancoolingcapmodedescr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapindex.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapcapacity.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapcapacityunit.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapcurrent.yfilter != YFilter.not_set or
                    self.cefcfancoolingcapmodedescr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcFanCoolingCapEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefcFanCoolingCapIndex='" + self.cefcfancoolingcapindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcFanCoolingCapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcfancoolingcapindex.is_set or self.cefcfancoolingcapindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapindex.get_name_leafdata())
                if (self.cefcfancoolingcapcapacity.is_set or self.cefcfancoolingcapcapacity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapcapacity.get_name_leafdata())
                if (self.cefcfancoolingcapcapacityunit.is_set or self.cefcfancoolingcapcapacityunit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapcapacityunit.get_name_leafdata())
                if (self.cefcfancoolingcapcurrent.is_set or self.cefcfancoolingcapcurrent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapcurrent.get_name_leafdata())
                if (self.cefcfancoolingcapmodedescr.is_set or self.cefcfancoolingcapmodedescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfancoolingcapmodedescr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcFanCoolingCapIndex" or name == "cefcFanCoolingCapCapacity" or name == "cefcFanCoolingCapCapacityUnit" or name == "cefcFanCoolingCapCurrent" or name == "cefcFanCoolingCapModeDescr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapIndex"):
                    self.cefcfancoolingcapindex = value
                    self.cefcfancoolingcapindex.value_namespace = name_space
                    self.cefcfancoolingcapindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapCapacity"):
                    self.cefcfancoolingcapcapacity = value
                    self.cefcfancoolingcapcapacity.value_namespace = name_space
                    self.cefcfancoolingcapcapacity.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapCapacityUnit"):
                    self.cefcfancoolingcapcapacityunit = value
                    self.cefcfancoolingcapcapacityunit.value_namespace = name_space
                    self.cefcfancoolingcapcapacityunit.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapCurrent"):
                    self.cefcfancoolingcapcurrent = value
                    self.cefcfancoolingcapcurrent.value_namespace = name_space
                    self.cefcfancoolingcapcurrent.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcFanCoolingCapModeDescr"):
                    self.cefcfancoolingcapmodedescr = value
                    self.cefcfancoolingcapmodedescr.value_namespace = name_space
                    self.cefcfancoolingcapmodedescr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfancoolingcapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfancoolingcapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcFanCoolingCapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcFanCoolingCapEntry"):
                for c in self.cefcfancoolingcapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfancoolingcapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcFanCoolingCapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcconnectorratingtable(Entity):
        """
        This table contains the connector power
        ratings of FRUs. 
        
        Only components with power connector rating 
        management are listed in this table.
        
        .. attribute:: cefcconnectorratingentry
        
        	A cefcConnectorRatingEntry lists the power connector rating information of a  component in the system.  An entry or entries are created by the agent when an physical entity with connector rating  management is added to the ENTITY\-MIB  entPhysicalTable. An entry is deleted  by the agent at the entity removal
        	**type**\: list of    :py:class:`Cefcconnectorratingentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcconnectorratingtable, self).__init__()

            self.yang_name = "cefcConnectorRatingTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcconnectorratingentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcconnectorratingtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcconnectorratingtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcconnectorrating
            
            	The maximum power that the component's connector can withdraw
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry, self).__init__()

                self.yang_name = "cefcConnectorRatingEntry"
                self.yang_parent_name = "cefcConnectorRatingTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcconnectorrating = YLeaf(YType.int32, "cefcConnectorRating")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcconnectorrating") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcconnectorrating.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcconnectorrating.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcConnectorRatingEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcConnectorRatingTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcconnectorrating.is_set or self.cefcconnectorrating.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcconnectorrating.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcConnectorRating"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcConnectorRating"):
                    self.cefcconnectorrating = value
                    self.cefcconnectorrating.value_namespace = name_space
                    self.cefcconnectorrating.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcconnectorratingentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcconnectorratingentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcConnectorRatingTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcConnectorRatingEntry"):
                for c in self.cefcconnectorratingentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcconnectorratingentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcConnectorRatingEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcmodulepowerconsumptiontable(Entity):
        """
        This table contains the total power consumption
        information for modules whose ENTITY\-MIB 
        entPhysicalTable entries have an entPhysicalClass 
        of 'module'.
        
        .. attribute:: cefcmodulepowerconsumptionentry
        
        	A cefcModulePowerConsumptionEntry lists the total power consumption of a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of    :py:class:`Cefcmodulepowerconsumptionentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            super(CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable, self).__init__()

            self.yang_name = "cefcModulePowerConsumptionTable"
            self.yang_parent_name = "CISCO-ENTITY-FRU-CONTROL-MIB"

            self.cefcmodulepowerconsumptionentry = YList(self)

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
                        super(CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable, self).__setattr__(name, value)


        class Cefcmodulepowerconsumptionentry(Entity):
            """
            A cefcModulePowerConsumptionEntry lists the total
            power consumption of a manageable components of type
            entPhysicalClass 'module'.
            
            Entries are created by the agent at the system
            power\-up or module insertion.
            
            Entries are deleted by the agent upon module
            removal.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcmodulepowerconsumption
            
            	The combined power consumption to operate the module and its submodule(s) and inline\-power device(s)
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                super(CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry, self).__init__()

                self.yang_name = "cefcModulePowerConsumptionEntry"
                self.yang_parent_name = "cefcModulePowerConsumptionTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefcmodulepowerconsumption = YLeaf(YType.int32, "cefcModulePowerConsumption")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefcmodulepowerconsumption") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefcmodulepowerconsumption.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefcmodulepowerconsumption.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefcModulePowerConsumptionEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/cefcModulePowerConsumptionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefcmodulepowerconsumption.is_set or self.cefcmodulepowerconsumption.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcmodulepowerconsumption.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefcModulePowerConsumption"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefcModulePowerConsumption"):
                    self.cefcmodulepowerconsumption = value
                    self.cefcmodulepowerconsumption.value_namespace = name_space
                    self.cefcmodulepowerconsumption.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcmodulepowerconsumptionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcmodulepowerconsumptionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefcModulePowerConsumptionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefcModulePowerConsumptionEntry"):
                for c in self.cefcmodulepowerconsumptionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcmodulepowerconsumptionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefcModulePowerConsumptionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cefcchassiscoolingtable is not None and self.cefcchassiscoolingtable.has_data()) or
            (self.cefcconnectorratingtable is not None and self.cefcconnectorratingtable.has_data()) or
            (self.cefcfancoolingcaptable is not None and self.cefcfancoolingcaptable.has_data()) or
            (self.cefcfancoolingtable is not None and self.cefcfancoolingtable.has_data()) or
            (self.cefcfantraystatustable is not None and self.cefcfantraystatustable.has_data()) or
            (self.cefcfrupower is not None and self.cefcfrupower.has_data()) or
            (self.cefcfrupowerstatustable is not None and self.cefcfrupowerstatustable.has_data()) or
            (self.cefcfrupowersupplygrouptable is not None and self.cefcfrupowersupplygrouptable.has_data()) or
            (self.cefcfrupowersupplyvaluetable is not None and self.cefcfrupowersupplyvaluetable.has_data()) or
            (self.cefcintellimoduletable is not None and self.cefcintellimoduletable.has_data()) or
            (self.cefcmibnotificationenables is not None and self.cefcmibnotificationenables.has_data()) or
            (self.cefcmodulecoolingtable is not None and self.cefcmodulecoolingtable.has_data()) or
            (self.cefcmodulelocalswitchingtable is not None and self.cefcmodulelocalswitchingtable.has_data()) or
            (self.cefcmodulepowerconsumptiontable is not None and self.cefcmodulepowerconsumptiontable.has_data()) or
            (self.cefcmoduletable is not None and self.cefcmoduletable.has_data()) or
            (self.cefcphysicaltable is not None and self.cefcphysicaltable.has_data()) or
            (self.cefcpowersupplyinputtable is not None and self.cefcpowersupplyinputtable.has_data()) or
            (self.cefcpowersupplyoutputtable is not None and self.cefcpowersupplyoutputtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cefcchassiscoolingtable is not None and self.cefcchassiscoolingtable.has_operation()) or
            (self.cefcconnectorratingtable is not None and self.cefcconnectorratingtable.has_operation()) or
            (self.cefcfancoolingcaptable is not None and self.cefcfancoolingcaptable.has_operation()) or
            (self.cefcfancoolingtable is not None and self.cefcfancoolingtable.has_operation()) or
            (self.cefcfantraystatustable is not None and self.cefcfantraystatustable.has_operation()) or
            (self.cefcfrupower is not None and self.cefcfrupower.has_operation()) or
            (self.cefcfrupowerstatustable is not None and self.cefcfrupowerstatustable.has_operation()) or
            (self.cefcfrupowersupplygrouptable is not None and self.cefcfrupowersupplygrouptable.has_operation()) or
            (self.cefcfrupowersupplyvaluetable is not None and self.cefcfrupowersupplyvaluetable.has_operation()) or
            (self.cefcintellimoduletable is not None and self.cefcintellimoduletable.has_operation()) or
            (self.cefcmibnotificationenables is not None and self.cefcmibnotificationenables.has_operation()) or
            (self.cefcmodulecoolingtable is not None and self.cefcmodulecoolingtable.has_operation()) or
            (self.cefcmodulelocalswitchingtable is not None and self.cefcmodulelocalswitchingtable.has_operation()) or
            (self.cefcmodulepowerconsumptiontable is not None and self.cefcmodulepowerconsumptiontable.has_operation()) or
            (self.cefcmoduletable is not None and self.cefcmoduletable.has_operation()) or
            (self.cefcphysicaltable is not None and self.cefcphysicaltable.has_operation()) or
            (self.cefcpowersupplyinputtable is not None and self.cefcpowersupplyinputtable.has_operation()) or
            (self.cefcpowersupplyoutputtable is not None and self.cefcpowersupplyoutputtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB" + path_buffer

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

        if (child_yang_name == "cefcChassisCoolingTable"):
            if (self.cefcchassiscoolingtable is None):
                self.cefcchassiscoolingtable = CiscoEntityFruControlMib.Cefcchassiscoolingtable()
                self.cefcchassiscoolingtable.parent = self
                self._children_name_map["cefcchassiscoolingtable"] = "cefcChassisCoolingTable"
            return self.cefcchassiscoolingtable

        if (child_yang_name == "cefcConnectorRatingTable"):
            if (self.cefcconnectorratingtable is None):
                self.cefcconnectorratingtable = CiscoEntityFruControlMib.Cefcconnectorratingtable()
                self.cefcconnectorratingtable.parent = self
                self._children_name_map["cefcconnectorratingtable"] = "cefcConnectorRatingTable"
            return self.cefcconnectorratingtable

        if (child_yang_name == "cefcFanCoolingCapTable"):
            if (self.cefcfancoolingcaptable is None):
                self.cefcfancoolingcaptable = CiscoEntityFruControlMib.Cefcfancoolingcaptable()
                self.cefcfancoolingcaptable.parent = self
                self._children_name_map["cefcfancoolingcaptable"] = "cefcFanCoolingCapTable"
            return self.cefcfancoolingcaptable

        if (child_yang_name == "cefcFanCoolingTable"):
            if (self.cefcfancoolingtable is None):
                self.cefcfancoolingtable = CiscoEntityFruControlMib.Cefcfancoolingtable()
                self.cefcfancoolingtable.parent = self
                self._children_name_map["cefcfancoolingtable"] = "cefcFanCoolingTable"
            return self.cefcfancoolingtable

        if (child_yang_name == "cefcFanTrayStatusTable"):
            if (self.cefcfantraystatustable is None):
                self.cefcfantraystatustable = CiscoEntityFruControlMib.Cefcfantraystatustable()
                self.cefcfantraystatustable.parent = self
                self._children_name_map["cefcfantraystatustable"] = "cefcFanTrayStatusTable"
            return self.cefcfantraystatustable

        if (child_yang_name == "cefcFRUPower"):
            if (self.cefcfrupower is None):
                self.cefcfrupower = CiscoEntityFruControlMib.Cefcfrupower()
                self.cefcfrupower.parent = self
                self._children_name_map["cefcfrupower"] = "cefcFRUPower"
            return self.cefcfrupower

        if (child_yang_name == "cefcFRUPowerStatusTable"):
            if (self.cefcfrupowerstatustable is None):
                self.cefcfrupowerstatustable = CiscoEntityFruControlMib.Cefcfrupowerstatustable()
                self.cefcfrupowerstatustable.parent = self
                self._children_name_map["cefcfrupowerstatustable"] = "cefcFRUPowerStatusTable"
            return self.cefcfrupowerstatustable

        if (child_yang_name == "cefcFRUPowerSupplyGroupTable"):
            if (self.cefcfrupowersupplygrouptable is None):
                self.cefcfrupowersupplygrouptable = CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable()
                self.cefcfrupowersupplygrouptable.parent = self
                self._children_name_map["cefcfrupowersupplygrouptable"] = "cefcFRUPowerSupplyGroupTable"
            return self.cefcfrupowersupplygrouptable

        if (child_yang_name == "cefcFRUPowerSupplyValueTable"):
            if (self.cefcfrupowersupplyvaluetable is None):
                self.cefcfrupowersupplyvaluetable = CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable()
                self.cefcfrupowersupplyvaluetable.parent = self
                self._children_name_map["cefcfrupowersupplyvaluetable"] = "cefcFRUPowerSupplyValueTable"
            return self.cefcfrupowersupplyvaluetable

        if (child_yang_name == "cefcIntelliModuleTable"):
            if (self.cefcintellimoduletable is None):
                self.cefcintellimoduletable = CiscoEntityFruControlMib.Cefcintellimoduletable()
                self.cefcintellimoduletable.parent = self
                self._children_name_map["cefcintellimoduletable"] = "cefcIntelliModuleTable"
            return self.cefcintellimoduletable

        if (child_yang_name == "cefcMIBNotificationEnables"):
            if (self.cefcmibnotificationenables is None):
                self.cefcmibnotificationenables = CiscoEntityFruControlMib.Cefcmibnotificationenables()
                self.cefcmibnotificationenables.parent = self
                self._children_name_map["cefcmibnotificationenables"] = "cefcMIBNotificationEnables"
            return self.cefcmibnotificationenables

        if (child_yang_name == "cefcModuleCoolingTable"):
            if (self.cefcmodulecoolingtable is None):
                self.cefcmodulecoolingtable = CiscoEntityFruControlMib.Cefcmodulecoolingtable()
                self.cefcmodulecoolingtable.parent = self
                self._children_name_map["cefcmodulecoolingtable"] = "cefcModuleCoolingTable"
            return self.cefcmodulecoolingtable

        if (child_yang_name == "cefcModuleLocalSwitchingTable"):
            if (self.cefcmodulelocalswitchingtable is None):
                self.cefcmodulelocalswitchingtable = CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable()
                self.cefcmodulelocalswitchingtable.parent = self
                self._children_name_map["cefcmodulelocalswitchingtable"] = "cefcModuleLocalSwitchingTable"
            return self.cefcmodulelocalswitchingtable

        if (child_yang_name == "cefcModulePowerConsumptionTable"):
            if (self.cefcmodulepowerconsumptiontable is None):
                self.cefcmodulepowerconsumptiontable = CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable()
                self.cefcmodulepowerconsumptiontable.parent = self
                self._children_name_map["cefcmodulepowerconsumptiontable"] = "cefcModulePowerConsumptionTable"
            return self.cefcmodulepowerconsumptiontable

        if (child_yang_name == "cefcModuleTable"):
            if (self.cefcmoduletable is None):
                self.cefcmoduletable = CiscoEntityFruControlMib.Cefcmoduletable()
                self.cefcmoduletable.parent = self
                self._children_name_map["cefcmoduletable"] = "cefcModuleTable"
            return self.cefcmoduletable

        if (child_yang_name == "cefcPhysicalTable"):
            if (self.cefcphysicaltable is None):
                self.cefcphysicaltable = CiscoEntityFruControlMib.Cefcphysicaltable()
                self.cefcphysicaltable.parent = self
                self._children_name_map["cefcphysicaltable"] = "cefcPhysicalTable"
            return self.cefcphysicaltable

        if (child_yang_name == "cefcPowerSupplyInputTable"):
            if (self.cefcpowersupplyinputtable is None):
                self.cefcpowersupplyinputtable = CiscoEntityFruControlMib.Cefcpowersupplyinputtable()
                self.cefcpowersupplyinputtable.parent = self
                self._children_name_map["cefcpowersupplyinputtable"] = "cefcPowerSupplyInputTable"
            return self.cefcpowersupplyinputtable

        if (child_yang_name == "cefcPowerSupplyOutputTable"):
            if (self.cefcpowersupplyoutputtable is None):
                self.cefcpowersupplyoutputtable = CiscoEntityFruControlMib.Cefcpowersupplyoutputtable()
                self.cefcpowersupplyoutputtable.parent = self
                self._children_name_map["cefcpowersupplyoutputtable"] = "cefcPowerSupplyOutputTable"
            return self.cefcpowersupplyoutputtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cefcChassisCoolingTable" or name == "cefcConnectorRatingTable" or name == "cefcFanCoolingCapTable" or name == "cefcFanCoolingTable" or name == "cefcFanTrayStatusTable" or name == "cefcFRUPower" or name == "cefcFRUPowerStatusTable" or name == "cefcFRUPowerSupplyGroupTable" or name == "cefcFRUPowerSupplyValueTable" or name == "cefcIntelliModuleTable" or name == "cefcMIBNotificationEnables" or name == "cefcModuleCoolingTable" or name == "cefcModuleLocalSwitchingTable" or name == "cefcModulePowerConsumptionTable" or name == "cefcModuleTable" or name == "cefcPhysicalTable" or name == "cefcPowerSupplyInputTable" or name == "cefcPowerSupplyOutputTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEntityFruControlMib()
        return self._top_entity

