""" CISCO_ENTITY_FRU_CONTROL_MIB 

The CISCO\-ENTITY\-FRU\-CONTROL\-MIB is used to monitor
and configure operational status of 
Field Replaceable Units (FRUs) and other managable 
physical entities of the system listed in the 
Entity\-MIB (RFC 2737) entPhysicalTable. 

FRUs include assemblies such as power supplies, fans, 
processor modules, interface modules, etc.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class FrucoolingunitEnum(Enum):
    """
    FrucoolingunitEnum

    The unit for the cooling capacity and requirement.

    cfm(1)    Cubic feet per minute

    watts(2)  Watts

    .. data:: cfm = 1

    .. data:: watts = 2

    """

    cfm = 1

    watts = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['FrucoolingunitEnum']


class ModuleadmintypeEnum(Enum):
    """
    ModuleadmintypeEnum

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

    enabled = 1

    disabled = 2

    reset = 3

    outOfServiceAdmin = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleadmintypeEnum']


class ModuleopertypeEnum(Enum):
    """
    ModuleopertypeEnum

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

    unknown = 1

    ok = 2

    disabled = 3

    okButDiagFailed = 4

    boot = 5

    selfTest = 6

    failed = 7

    missing = 8

    mismatchWithParent = 9

    mismatchConfig = 10

    diagFailed = 11

    dormant = 12

    outOfServiceAdmin = 13

    outOfServiceEnvTemp = 14

    poweredDown = 15

    poweredUp = 16

    powerDenied = 17

    powerCycled = 18

    okButPowerOverWarning = 19

    okButPowerOverCritical = 20

    syncInProgress = 21

    upgrading = 22

    okButAuthFailed = 23

    mdr = 24

    fwMismatchFound = 25

    fwDownloadSuccess = 26

    fwDownloadFailure = 27


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleopertypeEnum']


class ModuleresetreasontypeEnum(Enum):
    """
    ModuleresetreasontypeEnum

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

    unknown = 1

    powerUp = 2

    parityError = 3

    clearConfigReset = 4

    manualReset = 5

    watchDogTimeoutReset = 6

    resourceOverflowReset = 7

    missingTaskReset = 8

    lowVoltageReset = 9

    controllerReset = 10

    systemReset = 11

    switchoverReset = 12

    upgradeReset = 13

    downgradeReset = 14

    cacheErrorReset = 15

    deviceDriverReset = 16

    softwareExceptionReset = 17

    restoreConfigReset = 18

    abortRevReset = 19

    burnBootReset = 20

    standbyCdHealthierReset = 21

    nonNativeConfigClearReset = 22

    memoryProtectionErrorReset = 23


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleresetreasontypeEnum']


class PoweradmintypeEnum(Enum):
    """
    PoweradmintypeEnum

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

    on = 1

    off = 2

    inlineAuto = 3

    inlineOn = 4

    powerCycle = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PoweradmintypeEnum']


class PoweropertypeEnum(Enum):
    """
    PoweropertypeEnum

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

    offEnvOther = 1

    on = 2

    offAdmin = 3

    offDenied = 4

    offEnvPower = 5

    offEnvTemp = 6

    offEnvFan = 7

    failed = 8

    onButFanFail = 9

    offCooling = 10

    offConnectorRating = 11

    onButInlinePowerFail = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PoweropertypeEnum']


class PowerredundancytypeEnum(Enum):
    """
    PowerredundancytypeEnum

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

    notsupported = 1

    redundant = 2

    combined = 3

    nonRedundant = 4

    psRedundant = 5

    inPwrSrcRedundant = 6

    psRedundantSingleInput = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerredundancytypeEnum']



class CiscoEntityFruControlMib(object):
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
        self.cefcchassiscoolingtable = CiscoEntityFruControlMib.Cefcchassiscoolingtable()
        self.cefcchassiscoolingtable.parent = self
        self.cefcconnectorratingtable = CiscoEntityFruControlMib.Cefcconnectorratingtable()
        self.cefcconnectorratingtable.parent = self
        self.cefcfancoolingcaptable = CiscoEntityFruControlMib.Cefcfancoolingcaptable()
        self.cefcfancoolingcaptable.parent = self
        self.cefcfancoolingtable = CiscoEntityFruControlMib.Cefcfancoolingtable()
        self.cefcfancoolingtable.parent = self
        self.cefcfantraystatustable = CiscoEntityFruControlMib.Cefcfantraystatustable()
        self.cefcfantraystatustable.parent = self
        self.cefcfrupower = CiscoEntityFruControlMib.Cefcfrupower()
        self.cefcfrupower.parent = self
        self.cefcfrupowerstatustable = CiscoEntityFruControlMib.Cefcfrupowerstatustable()
        self.cefcfrupowerstatustable.parent = self
        self.cefcfrupowersupplygrouptable = CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable()
        self.cefcfrupowersupplygrouptable.parent = self
        self.cefcfrupowersupplyvaluetable = CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable()
        self.cefcfrupowersupplyvaluetable.parent = self
        self.cefcintellimoduletable = CiscoEntityFruControlMib.Cefcintellimoduletable()
        self.cefcintellimoduletable.parent = self
        self.cefcmibnotificationenables = CiscoEntityFruControlMib.Cefcmibnotificationenables()
        self.cefcmibnotificationenables.parent = self
        self.cefcmodulecoolingtable = CiscoEntityFruControlMib.Cefcmodulecoolingtable()
        self.cefcmodulecoolingtable.parent = self
        self.cefcmodulelocalswitchingtable = CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable()
        self.cefcmodulelocalswitchingtable.parent = self
        self.cefcmodulepowerconsumptiontable = CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable()
        self.cefcmodulepowerconsumptiontable.parent = self
        self.cefcmoduletable = CiscoEntityFruControlMib.Cefcmoduletable()
        self.cefcmoduletable.parent = self
        self.cefcphysicaltable = CiscoEntityFruControlMib.Cefcphysicaltable()
        self.cefcphysicaltable.parent = self
        self.cefcpowersupplyinputtable = CiscoEntityFruControlMib.Cefcpowersupplyinputtable()
        self.cefcpowersupplyinputtable.parent = self
        self.cefcpowersupplyoutputtable = CiscoEntityFruControlMib.Cefcpowersupplyoutputtable()
        self.cefcpowersupplyoutputtable.parent = self


    class Cefcfrupower(object):
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
            self.parent = None
            self.cefcmaxdefaulthighinlinepower = None
            self.cefcmaxdefaultinlinepower = None

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPower'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcmaxdefaulthighinlinepower is not None:
                return True

            if self.cefcmaxdefaultinlinepower is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupower']['meta_info']


    class Cefcmibnotificationenables(object):
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
            self.parent = None
            self.cefcenablepsoutputchangenotif = None
            self.cefcmibenablestatusnotification = None

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcMIBNotificationEnables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcenablepsoutputchangenotif is not None:
                return True

            if self.cefcmibenablestatusnotification is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcmibnotificationenables']['meta_info']


    class Cefcfrupowersupplygrouptable(object):
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
            self.parent = None
            self.cefcfrupowersupplygroupentry = YList()
            self.cefcfrupowersupplygroupentry.parent = self
            self.cefcfrupowersupplygroupentry.name = 'cefcfrupowersupplygroupentry'


        class Cefcfrupowersupplygroupentry(object):
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
            	**type**\:   :py:class:`CefcpowernonredundantreasonEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry.CefcpowernonredundantreasonEnum>`
            
            .. attribute:: cefcpowerredundancymode
            
            	The administratively desired power supply redundancy mode
            	**type**\:   :py:class:`PowerredundancytypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PowerredundancytypeEnum>`
            
            .. attribute:: cefcpowerredundancyopermode
            
            	The power supply redundancy operational mode
            	**type**\:   :py:class:`PowerredundancytypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PowerredundancytypeEnum>`
            
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcpowernonredundantreason = None
                self.cefcpowerredundancymode = None
                self.cefcpowerredundancyopermode = None
                self.cefcpowerunits = None
                self.cefctotalavailablecurrent = None
                self.cefctotaldrawncurrent = None
                self.cefctotaldrawninlinecurrent = None

            class CefcpowernonredundantreasonEnum(Enum):
                """
                CefcpowernonredundantreasonEnum

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

                notApplicable = 1

                unknown = 2

                singleSupply = 3

                mismatchedSupplies = 4

                supplyError = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry.CefcpowernonredundantreasonEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyGroupTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyGroupEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcpowernonredundantreason is not None:
                    return True

                if self.cefcpowerredundancymode is not None:
                    return True

                if self.cefcpowerredundancyopermode is not None:
                    return True

                if self.cefcpowerunits is not None:
                    return True

                if self.cefctotalavailablecurrent is not None:
                    return True

                if self.cefctotaldrawncurrent is not None:
                    return True

                if self.cefctotaldrawninlinecurrent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcfrupowersupplygroupentry is not None:
                for child_ref in self.cefcfrupowersupplygroupentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable']['meta_info']


    class Cefcfrupowerstatustable(object):
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
            self.parent = None
            self.cefcfrupowerstatusentry = YList()
            self.cefcfrupowerstatusentry.parent = self
            self.cefcfrupowerstatusentry.name = 'cefcfrupowerstatusentry'


        class Cefcfrupowerstatusentry(object):
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
            	**type**\:   :py:class:`PoweradmintypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PoweradmintypeEnum>`
            
            .. attribute:: cefcfrupowercapability
            
            	This object indicates the set of supported power capabilities of the FRU.  realTimeCurrent(0) \-     cefcFRURealTimeCurrent is supported by the FRU
            	**type**\:   :py:class:`Cefcfrupowercapability <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry.Cefcfrupowercapability>`
            
            .. attribute:: cefcfrupoweroperstatus
            
            	Operational FRU power state
            	**type**\:   :py:class:`PoweropertypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.PoweropertypeEnum>`
            
            .. attribute:: cefcfrurealtimecurrent
            
            	This object indicates the realtime value of current supplied by the FRU (positive values) or the realtime value of current drawn by the FRU (negative values)
            	**type**\:  int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcfrucurrent = None
                self.cefcfrupoweradminstatus = None
                self.cefcfrupowercapability = CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry.Cefcfrupowercapability()
                self.cefcfrupoweroperstatus = None
                self.cefcfrurealtimecurrent = None

            class Cefcfrupowercapability(FixedBitsDict):
                """
                Cefcfrupowercapability

                This object indicates the set of supported power capabilities
                of the FRU.
                
                realTimeCurrent(0) \-
                    cefcFRURealTimeCurrent is supported by the FRU.
                Keys are:- realTimeCurrent

                """

                def __init__(self):
                    self._dictionary = { 
                        'realTimeCurrent':False,
                    }
                    self._pos_map = { 
                        'realTimeCurrent':0,
                    }

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerStatusTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerStatusEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfrucurrent is not None:
                    return True

                if self.cefcfrupoweradminstatus is not None:
                    return True

                if self.cefcfrupowercapability is not None:
                    if self.cefcfrupowercapability._has_data():
                        return True

                if self.cefcfrupoweroperstatus is not None:
                    return True

                if self.cefcfrurealtimecurrent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcfrupowerstatusentry is not None:
                for child_ref in self.cefcfrupowerstatusentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowerstatustable']['meta_info']


    class Cefcfrupowersupplyvaluetable(object):
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
            self.parent = None
            self.cefcfrupowersupplyvalueentry = YList()
            self.cefcfrupowersupplyvalueentry.parent = self
            self.cefcfrupowersupplyvalueentry.name = 'cefcfrupowersupplyvalueentry'


        class Cefcfrupowersupplyvalueentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcfrudrawninlinecurrent = None
                self.cefcfrudrawnsystemcurrent = None
                self.cefcfrutotalinlinecurrent = None
                self.cefcfrutotalsystemcurrent = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyValueTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyValueEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfrudrawninlinecurrent is not None:
                    return True

                if self.cefcfrudrawnsystemcurrent is not None:
                    return True

                if self.cefcfrutotalinlinecurrent is not None:
                    return True

                if self.cefcfrutotalsystemcurrent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyValueTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcfrupowersupplyvalueentry is not None:
                for child_ref in self.cefcfrupowersupplyvalueentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable']['meta_info']


    class Cefcmoduletable(object):
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
            self.parent = None
            self.cefcmoduleentry = YList()
            self.cefcmoduleentry.parent = self
            self.cefcmoduleentry.name = 'cefcmoduleentry'


        class Cefcmoduleentry(object):
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
            	**type**\:   :py:class:`ModuleadmintypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleadmintypeEnum>`
            
            .. attribute:: cefcmodulelastclearconfigtime
            
            	The value of sysUpTime when the configuration was most recently cleared
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmoduleoperstatus
            
            	This object shows the module's operational state
            	**type**\:   :py:class:`ModuleopertypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleopertypeEnum>`
            
            .. attribute:: cefcmoduleresetreason
            
            	This object identifies the reason for the last reset performed on the module
            	**type**\:   :py:class:`ModuleresetreasontypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleresetreasontypeEnum>`
            
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcmoduleadminstatus = None
                self.cefcmodulelastclearconfigtime = None
                self.cefcmoduleoperstatus = None
                self.cefcmoduleresetreason = None
                self.cefcmoduleresetreasondescription = None
                self.cefcmodulestatechangereasondescr = None
                self.cefcmodulestatuslastchangetime = None
                self.cefcmoduleuptime = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmoduleadminstatus is not None:
                    return True

                if self.cefcmodulelastclearconfigtime is not None:
                    return True

                if self.cefcmoduleoperstatus is not None:
                    return True

                if self.cefcmoduleresetreason is not None:
                    return True

                if self.cefcmoduleresetreasondescription is not None:
                    return True

                if self.cefcmodulestatechangereasondescr is not None:
                    return True

                if self.cefcmodulestatuslastchangetime is not None:
                    return True

                if self.cefcmoduleuptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcmoduleentry is not None:
                for child_ref in self.cefcmoduleentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcmoduletable']['meta_info']


    class Cefcintellimoduletable(object):
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
            self.parent = None
            self.cefcintellimoduleentry = YList()
            self.cefcintellimoduleentry.parent = self
            self.cefcintellimoduleentry.name = 'cefcintellimoduleentry'


        class Cefcintellimoduleentry(object):
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
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcintellimoduleipaddr = None
                self.cefcintellimoduleipaddrtype = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcIntelliModuleTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcIntelliModuleEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcintellimoduleipaddr is not None:
                    return True

                if self.cefcintellimoduleipaddrtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcIntelliModuleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcintellimoduleentry is not None:
                for child_ref in self.cefcintellimoduleentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcintellimoduletable']['meta_info']


    class Cefcmodulelocalswitchingtable(object):
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
            self.parent = None
            self.cefcmodulelocalswitchingentry = YList()
            self.cefcmodulelocalswitchingentry.parent = self
            self.cefcmodulelocalswitchingentry.name = 'cefcmodulelocalswitchingentry'


        class Cefcmodulelocalswitchingentry(object):
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
            	**type**\:   :py:class:`CefcmodulelocalswitchingmodeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry.CefcmodulelocalswitchingmodeEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcmodulelocalswitchingmode = None

            class CefcmodulelocalswitchingmodeEnum(Enum):
                """
                CefcmodulelocalswitchingmodeEnum

                This object specifies the mode of local switching.

                enabled(1)  \- local switching is enabled.

                disabled(2) \- local switching is disabled.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry.CefcmodulelocalswitchingmodeEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleLocalSwitchingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleLocalSwitchingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmodulelocalswitchingmode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleLocalSwitchingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcmodulelocalswitchingentry is not None:
                for child_ref in self.cefcmodulelocalswitchingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable']['meta_info']


    class Cefcfantraystatustable(object):
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
            self.parent = None
            self.cefcfantraystatusentry = YList()
            self.cefcfantraystatusentry.parent = self
            self.cefcfantraystatusentry.name = 'cefcfantraystatusentry'


        class Cefcfantraystatusentry(object):
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
            	**type**\:   :py:class:`CefcfantrayoperstatusEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry.CefcfantrayoperstatusEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcfantrayoperstatus = None

            class CefcfantrayoperstatusEnum(Enum):
                """
                CefcfantrayoperstatusEnum

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

                unknown = 1

                up = 2

                down = 3

                warning = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry.CefcfantrayoperstatusEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanTrayStatusTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanTrayStatusEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfantrayoperstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanTrayStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcfantraystatusentry is not None:
                for child_ref in self.cefcfantraystatusentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfantraystatustable']['meta_info']


    class Cefcphysicaltable(object):
        """
        This table contains one row per physical entity.
        
        .. attribute:: cefcphysicalentry
        
        	Information about a particular physical entity
        	**type**\: list of    :py:class:`Cefcphysicalentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcphysicalentry = YList()
            self.cefcphysicalentry.parent = self
            self.cefcphysicalentry.name = 'cefcphysicalentry'


        class Cefcphysicalentry(object):
            """
            Information about a particular physical entity.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefcphysicalstatus
            
            	The status of this physical entity. other(1) \- the status is not any of the listed below. supported(2) \- this entity is supported. unsupported(3) \- this entity is unsupported. incompatible(4) \- this entity is incompatible. It would be unsupported(3), if the ID read from Serial EPROM is not supported. It would be incompatible(4), if in the present configuration this FRU is not supported
            	**type**\:   :py:class:`CefcphysicalstatusEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry.CefcphysicalstatusEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcphysicalstatus = None

            class CefcphysicalstatusEnum(Enum):
                """
                CefcphysicalstatusEnum

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

                other = 1

                supported = 2

                unsupported = 3

                incompatible = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry.CefcphysicalstatusEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPhysicalTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPhysicalEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcphysicalstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPhysicalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcphysicalentry is not None:
                for child_ref in self.cefcphysicalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcphysicaltable']['meta_info']


    class Cefcpowersupplyinputtable(object):
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
            self.parent = None
            self.cefcpowersupplyinputentry = YList()
            self.cefcpowersupplyinputentry.parent = self
            self.cefcpowersupplyinputentry.name = 'cefcpowersupplyinputentry'


        class Cefcpowersupplyinputentry(object):
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
            	**type**\:   :py:class:`CefcpowersupplyinputtypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry.CefcpowersupplyinputtypeEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcpowersupplyinputindex = None
                self.cefcpowersupplyinputtype = None

            class CefcpowersupplyinputtypeEnum(Enum):
                """
                CefcpowersupplyinputtypeEnum

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

                unknown = 1

                acLow = 2

                acHigh = 3

                dcLow = 4

                dcHigh = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry.CefcpowersupplyinputtypeEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cefcpowersupplyinputindex is None:
                    raise YPYModelError('Key property cefcpowersupplyinputindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputIndex = ' + str(self.cefcpowersupplyinputindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcpowersupplyinputindex is not None:
                    return True

                if self.cefcpowersupplyinputtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcpowersupplyinputentry is not None:
                for child_ref in self.cefcpowersupplyinputentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcpowersupplyinputtable']['meta_info']


    class Cefcpowersupplyoutputtable(object):
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
            self.parent = None
            self.cefcpowersupplyoutputentry = YList()
            self.cefcpowersupplyoutputentry.parent = self
            self.cefcpowersupplyoutputentry.name = 'cefcpowersupplyoutputentry'


        class Cefcpowersupplyoutputentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcpsoutputmodeindex = None
                self.cefcpsoutputmodecurrent = None
                self.cefcpsoutputmodeinoperation = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cefcpsoutputmodeindex is None:
                    raise YPYModelError('Key property cefcpsoutputmodeindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyOutputTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyOutputEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-FRU-CONTROL-MIB:cefcPSOutputModeIndex = ' + str(self.cefcpsoutputmodeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcpsoutputmodeindex is not None:
                    return True

                if self.cefcpsoutputmodecurrent is not None:
                    return True

                if self.cefcpsoutputmodeinoperation is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyOutputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcpowersupplyoutputentry is not None:
                for child_ref in self.cefcpowersupplyoutputentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcpowersupplyoutputtable']['meta_info']


    class Cefcchassiscoolingtable(object):
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
            self.parent = None
            self.cefcchassiscoolingentry = YList()
            self.cefcchassiscoolingentry.parent = self
            self.cefcchassiscoolingentry.name = 'cefcchassiscoolingentry'


        class Cefcchassiscoolingentry(object):
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
            	**type**\:   :py:class:`FrucoolingunitEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FrucoolingunitEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcchassisperslotcoolingcap = None
                self.cefcchassisperslotcoolingunit = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcChassisCoolingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcChassisCoolingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcchassisperslotcoolingcap is not None:
                    return True

                if self.cefcchassisperslotcoolingunit is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcChassisCoolingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcchassiscoolingentry is not None:
                for child_ref in self.cefcchassiscoolingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcchassiscoolingtable']['meta_info']


    class Cefcfancoolingtable(object):
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
            self.parent = None
            self.cefcfancoolingentry = YList()
            self.cefcfancoolingentry.parent = self
            self.cefcfancoolingentry.name = 'cefcfancoolingentry'


        class Cefcfancoolingentry(object):
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
            	**type**\:   :py:class:`FrucoolingunitEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FrucoolingunitEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcfancoolingcapacity = None
                self.cefcfancoolingcapacityunit = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfancoolingcapacity is not None:
                    return True

                if self.cefcfancoolingcapacityunit is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcfancoolingentry is not None:
                for child_ref in self.cefcfancoolingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfancoolingtable']['meta_info']


    class Cefcmodulecoolingtable(object):
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
            self.parent = None
            self.cefcmodulecoolingentry = YList()
            self.cefcmodulecoolingentry.parent = self
            self.cefcmodulecoolingentry.name = 'cefcmodulecoolingentry'


        class Cefcmodulecoolingentry(object):
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
            	**type**\:   :py:class:`FrucoolingunitEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FrucoolingunitEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-FRU-CONTROL-MIB'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcmodulecooling = None
                self.cefcmodulecoolingunit = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleCoolingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleCoolingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmodulecooling is not None:
                    return True

                if self.cefcmodulecoolingunit is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleCoolingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcmodulecoolingentry is not None:
                for child_ref in self.cefcmodulecoolingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulecoolingtable']['meta_info']


    class Cefcfancoolingcaptable(object):
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
            self.parent = None
            self.cefcfancoolingcapentry = YList()
            self.cefcfancoolingcapentry.parent = self
            self.cefcfancoolingcapentry.name = 'cefcfancoolingcapentry'


        class Cefcfancoolingcapentry(object):
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
            	**type**\:   :py:class:`FrucoolingunitEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB.FrucoolingunitEnum>`
            
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcfancoolingcapindex = None
                self.cefcfancoolingcapcapacity = None
                self.cefcfancoolingcapcapacityunit = None
                self.cefcfancoolingcapcurrent = None
                self.cefcfancoolingcapmodedescr = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cefcfancoolingcapindex is None:
                    raise YPYModelError('Key property cefcfancoolingcapindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapIndex = ' + str(self.cefcfancoolingcapindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfancoolingcapindex is not None:
                    return True

                if self.cefcfancoolingcapcapacity is not None:
                    return True

                if self.cefcfancoolingcapcapacityunit is not None:
                    return True

                if self.cefcfancoolingcapcurrent is not None:
                    return True

                if self.cefcfancoolingcapmodedescr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcfancoolingcapentry is not None:
                for child_ref in self.cefcfancoolingcapentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcfancoolingcaptable']['meta_info']


    class Cefcconnectorratingtable(object):
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
            self.parent = None
            self.cefcconnectorratingentry = YList()
            self.cefcconnectorratingentry.parent = self
            self.cefcconnectorratingentry.name = 'cefcconnectorratingentry'


        class Cefcconnectorratingentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcconnectorrating = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcConnectorRatingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcConnectorRatingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcconnectorrating is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcConnectorRatingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcconnectorratingentry is not None:
                for child_ref in self.cefcconnectorratingentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcconnectorratingtable']['meta_info']


    class Cefcmodulepowerconsumptiontable(object):
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
            self.parent = None
            self.cefcmodulepowerconsumptionentry = YList()
            self.cefcmodulepowerconsumptionentry.parent = self
            self.cefcmodulepowerconsumptionentry.name = 'cefcmodulepowerconsumptionentry'


        class Cefcmodulepowerconsumptionentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cefcmodulepowerconsumption = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModulePowerConsumptionTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModulePowerConsumptionEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmodulepowerconsumption is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModulePowerConsumptionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cefcmodulepowerconsumptionentry is not None:
                for child_ref in self.cefcmodulepowerconsumptionentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cefcchassiscoolingtable is not None and self.cefcchassiscoolingtable._has_data():
            return True

        if self.cefcconnectorratingtable is not None and self.cefcconnectorratingtable._has_data():
            return True

        if self.cefcfancoolingcaptable is not None and self.cefcfancoolingcaptable._has_data():
            return True

        if self.cefcfancoolingtable is not None and self.cefcfancoolingtable._has_data():
            return True

        if self.cefcfantraystatustable is not None and self.cefcfantraystatustable._has_data():
            return True

        if self.cefcfrupower is not None and self.cefcfrupower._has_data():
            return True

        if self.cefcfrupowerstatustable is not None and self.cefcfrupowerstatustable._has_data():
            return True

        if self.cefcfrupowersupplygrouptable is not None and self.cefcfrupowersupplygrouptable._has_data():
            return True

        if self.cefcfrupowersupplyvaluetable is not None and self.cefcfrupowersupplyvaluetable._has_data():
            return True

        if self.cefcintellimoduletable is not None and self.cefcintellimoduletable._has_data():
            return True

        if self.cefcmibnotificationenables is not None and self.cefcmibnotificationenables._has_data():
            return True

        if self.cefcmodulecoolingtable is not None and self.cefcmodulecoolingtable._has_data():
            return True

        if self.cefcmodulelocalswitchingtable is not None and self.cefcmodulelocalswitchingtable._has_data():
            return True

        if self.cefcmodulepowerconsumptiontable is not None and self.cefcmodulepowerconsumptiontable._has_data():
            return True

        if self.cefcmoduletable is not None and self.cefcmoduletable._has_data():
            return True

        if self.cefcphysicaltable is not None and self.cefcphysicaltable._has_data():
            return True

        if self.cefcpowersupplyinputtable is not None and self.cefcpowersupplyinputtable._has_data():
            return True

        if self.cefcpowersupplyoutputtable is not None and self.cefcpowersupplyoutputtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['CiscoEntityFruControlMib']['meta_info']


