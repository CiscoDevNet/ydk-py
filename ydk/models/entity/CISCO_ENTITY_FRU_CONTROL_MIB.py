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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum

class FRUCoolingUnit_Enum(Enum):
    """
    FRUCoolingUnit_Enum

    The unit for the cooling capacity and requirement.
    
    cfm(1)    Cubic feet per minute
    watts(2)  Watts

    """

    CFM = 1

    WATTS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['FRUCoolingUnit_Enum']


class ModuleAdminType_Enum(Enum):
    """
    ModuleAdminType_Enum

    Administratively desired module states.  Valid values are\:
    
    enabled(1)     module is operational.
    disabled(2)    module is not operational.
    reset(3)       module is reset. This value may be specified
                   in a management protocol set operation, it will
                   not be returned in response to a management 
                   protocol retrieval operation. 
    outOfServiceAdmin(4)   module is powered on but out of 
                           service, set by CLI.

    """

    ENABLED = 1

    DISABLED = 2

    RESET = 3

    OUTOFSERVICEADMIN = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleAdminType_Enum']


class ModuleOperType_Enum(Enum):
    """
    ModuleOperType_Enum

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

    """

    UNKNOWN = 1

    OK = 2

    DISABLED = 3

    OKBUTDIAGFAILED = 4

    BOOT = 5

    SELFTEST = 6

    FAILED = 7

    MISSING = 8

    MISMATCHWITHPARENT = 9

    MISMATCHCONFIG = 10

    DIAGFAILED = 11

    DORMANT = 12

    OUTOFSERVICEADMIN = 13

    OUTOFSERVICEENVTEMP = 14

    POWEREDDOWN = 15

    POWEREDUP = 16

    POWERDENIED = 17

    POWERCYCLED = 18

    OKBUTPOWEROVERWARNING = 19

    OKBUTPOWEROVERCRITICAL = 20

    SYNCINPROGRESS = 21

    UPGRADING = 22

    OKBUTAUTHFAILED = 23

    MDR = 24

    FWMISMATCHFOUND = 25

    FWDOWNLOADSUCCESS = 26

    FWDOWNLOADFAILURE = 27


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleOperType_Enum']


class ModuleResetReasonType_Enum(Enum):
    """
    ModuleResetReasonType_Enum

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

    """

    UNKNOWN = 1

    POWERUP = 2

    PARITYERROR = 3

    CLEARCONFIGRESET = 4

    MANUALRESET = 5

    WATCHDOGTIMEOUTRESET = 6

    RESOURCEOVERFLOWRESET = 7

    MISSINGTASKRESET = 8

    LOWVOLTAGERESET = 9

    CONTROLLERRESET = 10

    SYSTEMRESET = 11

    SWITCHOVERRESET = 12

    UPGRADERESET = 13

    DOWNGRADERESET = 14

    CACHEERRORRESET = 15

    DEVICEDRIVERRESET = 16

    SOFTWAREEXCEPTIONRESET = 17

    RESTORECONFIGRESET = 18

    ABORTREVRESET = 19

    BURNBOOTRESET = 20

    STANDBYCDHEALTHIERRESET = 21

    NONNATIVECONFIGCLEARRESET = 22

    MEMORYPROTECTIONERRORRESET = 23


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['ModuleResetReasonType_Enum']


class PowerAdminType_Enum(Enum):
    """
    PowerAdminType_Enum

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

    """

    ON = 1

    OFF = 2

    INLINEAUTO = 3

    INLINEON = 4

    POWERCYCLE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerAdminType_Enum']


class PowerOperType_Enum(Enum):
    """
    PowerOperType_Enum

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

    """

    OFFENVOTHER = 1

    ON = 2

    OFFADMIN = 3

    OFFDENIED = 4

    OFFENVPOWER = 5

    OFFENVTEMP = 6

    OFFENVFAN = 7

    FAILED = 8

    ONBUTFANFAIL = 9

    OFFCOOLING = 10

    OFFCONNECTORRATING = 11

    ONBUTINLINEPOWERFAIL = 12


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerOperType_Enum']


class PowerRedundancyType_Enum(Enum):
    """
    PowerRedundancyType_Enum

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

    """

    NOTSUPPORTED = 1

    REDUNDANT = 2

    COMBINED = 3

    NONREDUNDANT = 4

    PSREDUNDANT = 5

    INPWRSRCREDUNDANT = 6

    PSREDUNDANTSINGLEINPUT = 7


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['PowerRedundancyType_Enum']



class CISCOENTITYFRUCONTROLMIB(object):
    """
    
    
    .. attribute:: cefcchassiscoolingtable
    
    	This table contains the cooling capacity information of the chassis whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'chassis'
    	**type**\: :py:class:`CefcChassisCoolingTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable>`
    
    .. attribute:: cefcconnectorratingtable
    
    	This table contains the connector power ratings of FRUs.   Only components with power connector rating  management are listed in this table
    	**type**\: :py:class:`CefcConnectorRatingTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable>`
    
    .. attribute:: cefcfancoolingcaptable
    
    	This table contains a list of the possible cooling capacity modes and properties of the fans, whose  ENTITY\-MIB entPhysicalTable entries have an  entPhysicalClass of 'fan'
    	**type**\: :py:class:`CefcFanCoolingCapTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable>`
    
    .. attribute:: cefcfancoolingtable
    
    	This table contains the cooling capacity information of the fans whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'fan'
    	**type**\: :py:class:`CefcFanCoolingTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable>`
    
    .. attribute:: cefcfantraystatustable
    
    	This table contains the operational status information for all ENTITY\-MIB entPhysicalTable entries which have  an entPhysicalClass of 'fan'; specifically, all   entPhysicalTable entries which represent either\: one  physical fan, or a single physical 'fan tray' which is a manufactured (inseparable in the field) combination of  multiple fans
    	**type**\: :py:class:`CefcFanTrayStatusTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable>`
    
    .. attribute:: cefcfrupower
    
    	
    	**type**\: :py:class:`CefcFRUPower <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPower>`
    
    .. attribute:: cefcfrupowerstatustable
    
    	This table lists the power\-related administrative status and operational status of the manageable components in the system
    	**type**\: :py:class:`CefcFRUPowerStatusTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable>`
    
    .. attribute:: cefcfrupowersupplygrouptable
    
    	This table lists the redundancy mode and the operational status of the power supply groups in the system
    	**type**\: :py:class:`CefcFRUPowerSupplyGroupTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable>`
    
    .. attribute:: cefcfrupowersupplyvaluetable
    
    	This table lists the power capacity of a power FRU in the system if it provides variable power. Power supplies usually provide either system or inline power. They cannot be  controlled by software to dictate how they distribute power. We can also have what are known as variable power supplies. They can provide both system and inline power and can be  varied within hardware defined ranges for system and inline limited by a total maximum combined output. They could be configured by the user via CLI or SNMP or be controlled by software internally. This table supplements the information in the cefcFRUPowerStatusTable for power supply FRUs. The  cefcFRUCurrent attribute in that table provides the overall current the power supply FRU can provide while this table  gives us the individual contribution towards system and  inline power
    	**type**\: :py:class:`CefcFRUPowerSupplyValueTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable>`
    
    .. attribute:: cefcintellimoduletable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcIntelliModuleTable entry lists the information specific to intelligent modules which cannot be provided by the cefcModuleTable
    	**type**\: :py:class:`CefcIntelliModuleTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable>`
    
    .. attribute:: cefcmibnotificationenables
    
    	
    	**type**\: :py:class:`CefcMIBNotificationEnables <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables>`
    
    .. attribute:: cefcmodulecoolingtable
    
    	This table contains the cooling requirement for all the manageable components of type entPhysicalClass 'module'
    	**type**\: :py:class:`CefcModuleCoolingTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable>`
    
    .. attribute:: cefcmodulelocalswitchingtable
    
    	This table sparsely augments the cefcModuleTable (i.e., every row in this table corresponds to a row in the cefcModuleTable but not necessarily vice\-versa).  A cefcModuleLocalSwitchingTable entry lists the information specific to local switching capable modules which cannot be provided by the cefcModuleTable
    	**type**\: :py:class:`CefcModuleLocalSwitchingTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable>`
    
    .. attribute:: cefcmodulepowerconsumptiontable
    
    	This table contains the total power consumption information for modules whose ENTITY\-MIB  entPhysicalTable entries have an entPhysicalClass  of 'module'
    	**type**\: :py:class:`CefcModulePowerConsumptionTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable>`
    
    .. attribute:: cefcmoduletable
    
    	A cefcModuleTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components of type PhysicalClass module(9)
    	**type**\: :py:class:`CefcModuleTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleTable>`
    
    .. attribute:: cefcphysicaltable
    
    	This table contains one row per physical entity
    	**type**\: :py:class:`CefcPhysicalTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable>`
    
    .. attribute:: cefcpowersupplyinputtable
    
    	This table contains the power input information for all the power supplies that have entPhysicalTable entries with 'powerSupply' in the entPhysicalClass.   The entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries is determined by the number of power supplies and number of power inputs on the power  supply
    	**type**\: :py:class:`CefcPowerSupplyInputTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable>`
    
    .. attribute:: cefcpowersupplyoutputtable
    
    	This table contains a list of possible output mode for the power supplies, whose ENTITY\-MIB entPhysicalTable entries have an entPhysicalClass of 'powerSupply'. It also indicate which mode is the operational mode within the system
    	**type**\: :py:class:`CefcPowerSupplyOutputTable <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable>`
    
    

    """

    _prefix = 'cisco-entity'
    _revision = '2013-08-19'

    def __init__(self):
        self.cefcchassiscoolingtable = CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable()
        self.cefcchassiscoolingtable.parent = self
        self.cefcconnectorratingtable = CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable()
        self.cefcconnectorratingtable.parent = self
        self.cefcfancoolingcaptable = CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable()
        self.cefcfancoolingcaptable.parent = self
        self.cefcfancoolingtable = CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable()
        self.cefcfancoolingtable.parent = self
        self.cefcfantraystatustable = CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable()
        self.cefcfantraystatustable.parent = self
        self.cefcfrupower = CISCOENTITYFRUCONTROLMIB.CefcFRUPower()
        self.cefcfrupower.parent = self
        self.cefcfrupowerstatustable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable()
        self.cefcfrupowerstatustable.parent = self
        self.cefcfrupowersupplygrouptable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable()
        self.cefcfrupowersupplygrouptable.parent = self
        self.cefcfrupowersupplyvaluetable = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable()
        self.cefcfrupowersupplyvaluetable.parent = self
        self.cefcintellimoduletable = CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable()
        self.cefcintellimoduletable.parent = self
        self.cefcmibnotificationenables = CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables()
        self.cefcmibnotificationenables.parent = self
        self.cefcmodulecoolingtable = CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable()
        self.cefcmodulecoolingtable.parent = self
        self.cefcmodulelocalswitchingtable = CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable()
        self.cefcmodulelocalswitchingtable.parent = self
        self.cefcmodulepowerconsumptiontable = CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable()
        self.cefcmodulepowerconsumptiontable.parent = self
        self.cefcmoduletable = CISCOENTITYFRUCONTROLMIB.CefcModuleTable()
        self.cefcmoduletable.parent = self
        self.cefcphysicaltable = CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable()
        self.cefcphysicaltable.parent = self
        self.cefcpowersupplyinputtable = CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable()
        self.cefcpowersupplyinputtable.parent = self
        self.cefcpowersupplyoutputtable = CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable()
        self.cefcpowersupplyoutputtable.parent = self


    class CefcChassisCoolingTable(object):
        """
        This table contains the cooling capacity
        information of the chassis whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'chassis'.
        
        .. attribute:: cefcchassiscoolingentry
        
        	A cefcChassisCoolingEntry lists the maximum cooling capacity that could be provided  for one slot on the manageable components of type PhysicalClass 'chassis'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of :py:class:`CefcChassisCoolingEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcchassiscoolingentry = YList()
            self.cefcchassiscoolingentry.parent = self
            self.cefcchassiscoolingentry.name = 'cefcchassiscoolingentry'


        class CefcChassisCoolingEntry(object):
            """
            A cefcChassisCoolingEntry lists the maximum
            cooling capacity that could be provided 
            for one slot on the manageable components of type
            PhysicalClass 'chassis'.
            
            Entries are created by the agent if the corresponding
            entry is created in ENTITY\-MIB entPhysicalTable.
            
            Entries are deleted by the agent if the corresponding
            entry is deleted in ENTITY\-MIB entPhysicalTable.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcchassisperslotcoolingcap
            
            	The maximum cooling capacity that could be provided for any slot in this chassis.  The default unit of the cooling capacity is 'cfm', if cefcChassisPerSlotCoolingUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcchassisperslotcoolingunit
            
            	The unit of the maximum cooling capacity for any slot in this chassis
            	**type**\: :py:class:`FRUCoolingUnit_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcchassisperslotcoolingcap = None
                self.cefcchassisperslotcoolingunit = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcChassisCoolingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcChassisCoolingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcchassisperslotcoolingcap is not None:
                    return True

                if self.cefcchassisperslotcoolingunit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcChassisCoolingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcchassiscoolingentry is not None:
                for child_ref in self.cefcchassiscoolingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable']['meta_info']


    class CefcConnectorRatingTable(object):
        """
        This table contains the connector power
        ratings of FRUs. 
        
        Only components with power connector rating 
        management are listed in this table.
        
        .. attribute:: cefcconnectorratingentry
        
        	A cefcConnectorRatingEntry lists the power connector rating information of a  component in the system.  An entry or entries are created by the agent when an physical entity with connector rating  management is added to the ENTITY\-MIB  entPhysicalTable. An entry is deleted  by the agent at the entity removal
        	**type**\: list of :py:class:`CefcConnectorRatingEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcconnectorratingentry = YList()
            self.cefcconnectorratingentry.parent = self
            self.cefcconnectorratingentry.name = 'cefcconnectorratingentry'


        class CefcConnectorRatingEntry(object):
            """
            A cefcConnectorRatingEntry lists the
            power connector rating information of a 
            component in the system.
            
            An entry or entries are created by the agent
            when an physical entity with connector rating 
            management is added to the ENTITY\-MIB 
            entPhysicalTable. An entry is deleted 
            by the agent at the entity removal.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcconnectorrating
            
            	The maximum power that the component's connector can withdraw
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcconnectorrating = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcConnectorRatingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcConnectorRatingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcconnectorrating is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcConnectorRatingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcconnectorratingentry is not None:
                for child_ref in self.cefcconnectorratingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable']['meta_info']


    class CefcFRUPower(object):
        """
        
        
        .. attribute:: cefcmaxdefaulthighinlinepower
        
        	The system will provide power to the device connecting to the FRU if the device needs power, like an IP Phone. We call the providing power inline power.  This MIB object controls the maximum default inline power for the device connecting to the FRU in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cefcmaxdefaultinlinepower
        
        	The system will provide power to the device connecting to the FRU if the device needs power, like an IP Phone. We call the providing power inline power.  This MIB object controls the maximum default inline power for the device connecting to the FRU in the system. If the maximum default inline power of the device is greater than the maximum value reportable by this object, then this object should report its maximum reportable value (12500) and cefcMaxDefaultHighInLinePower must be used to report the actual maximum default inline power
        	**type**\: int
        
        	**range:** 0..12500
        
        

        """

        _prefix = 'cisco-entity'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcmaxdefaulthighinlinepower is not None:
                return True

            if self.cefcmaxdefaultinlinepower is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPower']['meta_info']


    class CefcFRUPowerStatusTable(object):
        """
        This table lists the power\-related administrative status
        and operational status of the manageable components
        in the system.
        
        .. attribute:: cefcfrupowerstatusentry
        
        	An cefcFRUPowerStatusTable entry lists the desired administrative status, the operational status of the  power manageable component, and the current required by  the component for operation.  Entries are created by the agent at system power\-up or  the insertion of the component.  Entries are deleted by the agent at the removal of the component.  Only components with power control are listed in the  table
        	**type**\: list of :py:class:`CefcFRUPowerStatusEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcfrupowerstatusentry = YList()
            self.cefcfrupowerstatusentry.parent = self
            self.cefcfrupowerstatusentry.name = 'cefcfrupowerstatusentry'


        class CefcFRUPowerStatusEntry(object):
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
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcfrucurrent
            
            	Current supplied by the FRU (positive values) or current required to operate the FRU (negative values)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfrupoweradminstatus
            
            	Administratively desired FRU power state
            	**type**\: :py:class:`PowerAdminType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.PowerAdminType_Enum>`
            
            .. attribute:: cefcfrupowercapability
            
            	This object indicates the set of supported power capabilities of the FRU.  realTimeCurrent(0) \-     cefcFRURealTimeCurrent is supported by the FRU
            	**type**\: :py:class:`CefcFRUPowerCapability_Bits <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry.CefcFRUPowerCapability_Bits>`
            
            .. attribute:: cefcfrupoweroperstatus
            
            	Operational FRU power state
            	**type**\: :py:class:`PowerOperType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.PowerOperType_Enum>`
            
            .. attribute:: cefcfrurealtimecurrent
            
            	This object indicates the realtime value of current supplied by the FRU (positive values) or the realtime value of current drawn by the FRU (negative values)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcfrucurrent = None
                self.cefcfrupoweradminstatus = None
                self.cefcfrupowercapability = CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry.CefcFRUPowerCapability_Bits()
                self.cefcfrupoweroperstatus = None
                self.cefcfrurealtimecurrent = None

            class CefcFRUPowerCapability_Bits(FixedBitsDict):
                """
                CefcFRUPowerCapability_Bits

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
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerStatusTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerStatusEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfrupowerstatusentry is not None:
                for child_ref in self.cefcfrupowerstatusentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable']['meta_info']


    class CefcFRUPowerSupplyGroupTable(object):
        """
        This table lists the redundancy mode and the
        operational status of the power supply groups
        in the system.
        
        .. attribute:: cefcfrupowersupplygroupentry
        
        	An cefcFRUPowerSupplyGroupTable entry lists the desired redundancy mode, the units of the power outputs and the  available and drawn current for the power supply group.  Entries are created by the agent when a power supply group is added to the entPhysicalTable. Entries are deleted by  the agent at power supply group removal
        	**type**\: list of :py:class:`CefcFRUPowerSupplyGroupEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcfrupowersupplygroupentry = YList()
            self.cefcfrupowersupplygroupentry.parent = self
            self.cefcfrupowersupplygroupentry.name = 'cefcfrupowersupplygroupentry'


        class CefcFRUPowerSupplyGroupEntry(object):
            """
            An cefcFRUPowerSupplyGroupTable entry lists the desired
            redundancy mode, the units of the power outputs and the 
            available and drawn current for the power supply group.
            
            Entries are created by the agent when a power supply group
            is added to the entPhysicalTable. Entries are deleted by 
            the agent at power supply group removal.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcpowernonredundantreason
            
            	This object has the value of notApplicable(1) when cefcPowerRedundancyOperMode of the instance does not have the value of nonRedundant(4).  The other values explain the reason why  cefcPowerRedundancyOperMode is nonRedundant(4), e.g.  unknown(2)             the reason is not identified.  singleSupply(3)        There is only one power supply                        in the group.  mismatchedSupplies(4)  There are more than one power                        supplies in the groups. However                        they are mismatched and can not                        work redundantly.  supplyError(5)         Some power supply or supplies                        does or do not working properly
            	**type**\: :py:class:`CefcPowerNonRedundantReason_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry.CefcPowerNonRedundantReason_Enum>`
            
            .. attribute:: cefcpowerredundancymode
            
            	The administratively desired power supply redundancy mode
            	**type**\: :py:class:`PowerRedundancyType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.PowerRedundancyType_Enum>`
            
            .. attribute:: cefcpowerredundancyopermode
            
            	The power supply redundancy operational mode
            	**type**\: :py:class:`PowerRedundancyType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.PowerRedundancyType_Enum>`
            
            .. attribute:: cefcpowerunits
            
            	The units of primary supply to interpret cefcTotalAvailableCurrent and cefcTotalDrawnCurrent as power.  For example, one 1000\-watt power supply could  deliver 100 amperes at 10 volts DC.  So the value of cefcPowerUnits would be 'at 10 volts DC'.  cefcPowerUnits is for display purposes only
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cefctotalavailablecurrent
            
            	Total current available for FRU usage
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefctotaldrawncurrent
            
            	Total current drawn by powered\-on FRUs
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefctotaldrawninlinecurrent
            
            	Total inline current drawn for inline operation
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'cisco-entity'
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

            class CefcPowerNonRedundantReason_Enum(Enum):
                """
                CefcPowerNonRedundantReason_Enum

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

                """

                NOTAPPLICABLE = 1

                UNKNOWN = 2

                SINGLESUPPLY = 3

                MISMATCHEDSUPPLIES = 4

                SUPPLYERROR = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry.CefcPowerNonRedundantReason_Enum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyGroupTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyGroupEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfrupowersupplygroupentry is not None:
                for child_ref in self.cefcfrupowersupplygroupentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable']['meta_info']


    class CefcFRUPowerSupplyValueTable(object):
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
        	**type**\: list of :py:class:`CefcFRUPowerSupplyValueEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcfrupowersupplyvalueentry = YList()
            self.cefcfrupowersupplyvalueentry.parent = self
            self.cefcfrupowersupplyvalueentry.name = 'cefcfrupowersupplyvalueentry'


        class CefcFRUPowerSupplyValueEntry(object):
            """
            An cefcFRUPowerSupplyValueTable entry lists the current
            provided by the FRU for operation.
            
            Entries are created by the agent at system power\-up or 
            FRU insertion.  Entries are deleted by the agent at FRU
            removal.
            
            Only power supply FRUs are listed in the table.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcfrudrawninlinecurrent
            
            	Amount of current that is being drawn from this FRU for inline operation
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
            
            .. attribute:: cefcfrutotalsystemcurrent
            
            	Total current that could be supplied by the FRU (positive values) for system operations
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'cisco-entity'
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
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyValueTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyValueEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFRUPowerSupplyValueTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfrupowersupplyvalueentry is not None:
                for child_ref in self.cefcfrupowersupplyvalueentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable']['meta_info']


    class CefcFanCoolingCapTable(object):
        """
        This table contains a list of the possible cooling
        capacity modes and properties of the fans, whose 
        ENTITY\-MIB entPhysicalTable entries have an 
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingcapentry
        
        	A cefcFanCoolingCapacityEntry lists the cooling capacity mode of a manageable components of type entPhysicalClass 'fan'. It also lists the corresponding cooling capacity provided and the power consumed by the fan on this mode.   Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of :py:class:`CefcFanCoolingCapEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcfancoolingcapentry = YList()
            self.cefcfancoolingcapentry.parent = self
            self.cefcfancoolingcapentry.name = 'cefcfancoolingcapentry'


        class CefcFanCoolingCapEntry(object):
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
            
            .. attribute:: cefcfancoolingcapindex
            
            	An arbitrary value that uniquely identifies a cooling capacity mode for a fan
            	**type**\: int
            
            	**range:** 1..4095
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcfancoolingcapcapacity
            
            	The cooling capacity that could be provided when the fan is operating in this mode.  The default unit of the cooling capacity is 'cfm', if cefcFanCoolingCapCapacityUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfancoolingcapcapacityunit
            
            	The unit of the fan cooling capacity when operating in this mode
            	**type**\: :py:class:`FRUCoolingUnit_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit_Enum>`
            
            .. attribute:: cefcfancoolingcapcurrent
            
            	The power consumption of the fan when operating in in this mode
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcfancoolingcapmodedescr
            
            	A textual description of the cooling capacity mode of the fan
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.cefcfancoolingcapindex = None
                self.entphysicalindex = None
                self.cefcfancoolingcapcapacity = None
                self.cefcfancoolingcapcapacityunit = None
                self.cefcfancoolingcapcurrent = None
                self.cefcfancoolingcapmodedescr = None

            @property
            def _common_path(self):
                if self.cefcfancoolingcapindex is None:
                    raise YPYDataValidationError('Key property cefcfancoolingcapindex is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapEntry[CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapIndex = ' + str(self.cefcfancoolingcapindex) + '][CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefcfancoolingcapindex is not None:
                    return True

                if self.entphysicalindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingCapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfancoolingcapentry is not None:
                for child_ref in self.cefcfancoolingcapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable']['meta_info']


    class CefcFanCoolingTable(object):
        """
        This table contains the cooling capacity
        information of the fans whose ENTITY\-MIB
        entPhysicalTable entries have an
        entPhysicalClass of 'fan'.
        
        .. attribute:: cefcfancoolingentry
        
        	A cefcFanCoolingEntry lists the cooling capacity that is provided by the  manageable components of type PhysicalClass  'fan'.  Entries are created by the agent if the corresponding entry is created in ENTITY\-MIB entPhysicalTable.  Entries are deleted by the agent if the corresponding entry is deleted in ENTITY\-MIB entPhysicalTable
        	**type**\: list of :py:class:`CefcFanCoolingEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcfancoolingentry = YList()
            self.cefcfancoolingentry.parent = self
            self.cefcfancoolingentry.name = 'cefcfancoolingentry'


        class CefcFanCoolingEntry(object):
            """
            A cefcFanCoolingEntry lists the cooling
            capacity that is provided by the 
            manageable components of type PhysicalClass 
            'fan'.
            
            Entries are created by the agent if the corresponding
            entry is created in ENTITY\-MIB entPhysicalTable.
            
            Entries are deleted by the agent if the corresponding
            entry is deleted in ENTITY\-MIB entPhysicalTable.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcfancoolingcapacity
            
            	The cooling capacity that is provided by this fan.  The default unit of the fan cooling capacity is 'cfm', if cefcFanCoolingCapacityUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfancoolingcapacityunit
            
            	The unit of the fan cooling capacity
            	**type**\: :py:class:`FRUCoolingUnit_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcfancoolingcapacity = None
                self.cefcfancoolingcapacityunit = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfancoolingcapacity is not None:
                    return True

                if self.cefcfancoolingcapacityunit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanCoolingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfancoolingentry is not None:
                for child_ref in self.cefcfancoolingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable']['meta_info']


    class CefcFanTrayStatusTable(object):
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
        	**type**\: list of :py:class:`CefcFanTrayStatusEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcfantraystatusentry = YList()
            self.cefcfantraystatusentry.parent = self
            self.cefcfantraystatusentry.name = 'cefcfantraystatusentry'


        class CefcFanTrayStatusEntry(object):
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
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcfantrayoperstatus
            
            	The operational state of the fan or fan tray. unknown(1) \- unknown. up(2) \- powered on. down(3) \- powered down. warning(4) \- partial failure, needs replacement               as soon as possible
            	**type**\: :py:class:`CefcFanTrayOperStatus_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry.CefcFanTrayOperStatus_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcfantrayoperstatus = None

            class CefcFanTrayOperStatus_Enum(Enum):
                """
                CefcFanTrayOperStatus_Enum

                The operational state of the fan or fan tray.
                unknown(1) \- unknown.
                up(2) \- powered on.
                down(3) \- powered down.
                warning(4) \- partial failure, needs replacement 
                             as soon as possible.

                """

                UNKNOWN = 1

                UP = 2

                DOWN = 3

                WARNING = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry.CefcFanTrayOperStatus_Enum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanTrayStatusTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanTrayStatusEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcfantrayoperstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcFanTrayStatusTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfantraystatusentry is not None:
                for child_ref in self.cefcfantraystatusentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable']['meta_info']


    class CefcIntelliModuleTable(object):
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
        	**type**\: list of :py:class:`CefcIntelliModuleEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcintellimoduleentry = YList()
            self.cefcintellimoduleentry.parent = self
            self.cefcintellimoduleentry.name = 'cefcintellimoduleentry'


        class CefcIntelliModuleEntry(object):
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
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcintellimoduleipaddr
            
            	The Internet address configured for the intelligent module. The type of this address is  determined by the value of the object  cefcIntelliModuleIPAddrType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefcintellimoduleipaddrtype
            
            	The type of Internet address by which the intelligent module is reachable
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcintellimoduleipaddr = None
                self.cefcintellimoduleipaddrtype = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcIntelliModuleTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcIntelliModuleEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcintellimoduleipaddr is not None:
                    return True

                if self.cefcintellimoduleipaddrtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcIntelliModuleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcintellimoduleentry is not None:
                for child_ref in self.cefcintellimoduleentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable']['meta_info']


    class CefcMIBNotificationEnables(object):
        """
        
        
        .. attribute:: cefcenablepsoutputchangenotif
        
        	This variable indicates whether the system produces the cefcPowerSupplyOutputChange  notifications when the output capacity of  a power supply has changed. A false value  will prevent this notification to generated
        	**type**\: bool
        
        .. attribute:: cefcmibenablestatusnotification
        
        	This variable indicates whether the system produces the following notifications\: cefcModuleStatusChange, cefcPowerStatusChange,  cefcFRUInserted, cefcFRURemoved,  cefcUnrecognizedFRU and cefcFanTrayStatusChange.  A false value will prevent these notifications from being generated
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-entity'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcenablepsoutputchangenotif is not None:
                return True

            if self.cefcmibenablestatusnotification is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables']['meta_info']


    class CefcModuleCoolingTable(object):
        """
        This table contains the cooling requirement for
        all the manageable components of type entPhysicalClass
        'module'.
        
        .. attribute:: cefcmodulecoolingentry
        
        	A cefcModuleCoolingEntry lists the cooling requirement for a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of :py:class:`CefcModuleCoolingEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcmodulecoolingentry = YList()
            self.cefcmodulecoolingentry.parent = self
            self.cefcmodulecoolingentry.name = 'cefcmodulecoolingentry'


        class CefcModuleCoolingEntry(object):
            """
            A cefcModuleCoolingEntry lists the cooling
            requirement for a manageable components of type
            entPhysicalClass 'module'.
            
            Entries are created by the agent at the system
            power\-up or module insertion.
            
            Entries are deleted by the agent upon module
            removal.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcmodulecooling
            
            	The cooling requirement of the module and its daughter cards.  The default unit of the module cooling requirement is 'cfm', if cefcModuleCoolingUnit is not supported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmodulecoolingunit
            
            	The unit of the cooling requirement of the module and its daughter cards
            	**type**\: :py:class:`FRUCoolingUnit_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.FRUCoolingUnit_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcmodulecooling = None
                self.cefcmodulecoolingunit = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleCoolingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleCoolingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmodulecooling is not None:
                    return True

                if self.cefcmodulecoolingunit is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleCoolingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcmodulecoolingentry is not None:
                for child_ref in self.cefcmodulecoolingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable']['meta_info']


    class CefcModuleLocalSwitchingTable(object):
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
        	**type**\: list of :py:class:`CefcModuleLocalSwitchingEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcmodulelocalswitchingentry = YList()
            self.cefcmodulelocalswitchingentry.parent = self
            self.cefcmodulelocalswitchingentry.name = 'cefcmodulelocalswitchingentry'


        class CefcModuleLocalSwitchingEntry(object):
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
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcmodulelocalswitchingmode
            
            	This object specifies the mode of local switching.  enabled(1)  \- local switching is enabled. disabled(2) \- local switching is disabled
            	**type**\: :py:class:`CefcModuleLocalSwitchingMode_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry.CefcModuleLocalSwitchingMode_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcmodulelocalswitchingmode = None

            class CefcModuleLocalSwitchingMode_Enum(Enum):
                """
                CefcModuleLocalSwitchingMode_Enum

                This object specifies the mode of local switching.
                
                enabled(1)  \- local switching is enabled.
                disabled(2) \- local switching is disabled.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry.CefcModuleLocalSwitchingMode_Enum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleLocalSwitchingTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleLocalSwitchingEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmodulelocalswitchingmode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleLocalSwitchingTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcmodulelocalswitchingentry is not None:
                for child_ref in self.cefcmodulelocalswitchingentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable']['meta_info']


    class CefcModulePowerConsumptionTable(object):
        """
        This table contains the total power consumption
        information for modules whose ENTITY\-MIB 
        entPhysicalTable entries have an entPhysicalClass 
        of 'module'.
        
        .. attribute:: cefcmodulepowerconsumptionentry
        
        	A cefcModulePowerConsumptionEntry lists the total power consumption of a manageable components of type entPhysicalClass 'module'.  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of :py:class:`CefcModulePowerConsumptionEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcmodulepowerconsumptionentry = YList()
            self.cefcmodulepowerconsumptionentry.parent = self
            self.cefcmodulepowerconsumptionentry.name = 'cefcmodulepowerconsumptionentry'


        class CefcModulePowerConsumptionEntry(object):
            """
            A cefcModulePowerConsumptionEntry lists the total
            power consumption of a manageable components of type
            entPhysicalClass 'module'.
            
            Entries are created by the agent at the system
            power\-up or module insertion.
            
            Entries are deleted by the agent upon module
            removal.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcmodulepowerconsumption
            
            	The combined power consumption to operate the module and its submodule(s) and inline\-power device(s)
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcmodulepowerconsumption = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModulePowerConsumptionTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModulePowerConsumptionEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcmodulepowerconsumption is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModulePowerConsumptionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcmodulepowerconsumptionentry is not None:
                for child_ref in self.cefcmodulepowerconsumptionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable']['meta_info']


    class CefcModuleTable(object):
        """
        A cefcModuleTable entry lists the operational and
        administrative status information for ENTITY\-MIB
        entPhysicalTable entries for manageable components
        of type PhysicalClass module(9).
        
        .. attribute:: cefcmoduleentry
        
        	A cefcModuleStatusTable entry lists the operational and administrative status information for ENTITY\-MIB entPhysicalTable entries for manageable components  of type PhysicalClass module(9).  Entries are created by the agent at the system power\-up or module insertion.  Entries are deleted by the agent upon module removal
        	**type**\: list of :py:class:`CefcModuleEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcmoduleentry = YList()
            self.cefcmoduleentry.parent = self
            self.cefcmoduleentry.name = 'cefcmoduleentry'


        class CefcModuleEntry(object):
            """
            A cefcModuleStatusTable entry lists the operational and
            administrative status information for ENTITY\-MIB
            entPhysicalTable entries for manageable components 
            of type PhysicalClass module(9).
            
            Entries are created by the agent at the system power\-up or
            module insertion.
            
            Entries are deleted by the agent upon module removal.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcmoduleadminstatus
            
            	This object provides administrative control of the module
            	**type**\: :py:class:`ModuleAdminType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleAdminType_Enum>`
            
            .. attribute:: cefcmodulelastclearconfigtime
            
            	The value of sysUpTime when the configuration was most recently cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmoduleoperstatus
            
            	This object shows the module's operational state
            	**type**\: :py:class:`ModuleOperType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleOperType_Enum>`
            
            .. attribute:: cefcmoduleresetreason
            
            	This object identifies the reason for the last reset performed on the module
            	**type**\: :py:class:`ModuleResetReasonType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.ModuleResetReasonType_Enum>`
            
            .. attribute:: cefcmoduleresetreasondescription
            
            	A description qualifying the module reset reason specified in cefcModuleResetReason.   Examples\:   command xyz                 missing task   switch over   watchdog timeout       etc.  cefcModuleResetReasonDescription is for display purposes only. NMS applications must not parse
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cefcmodulestatechangereasondescr
            
            	This object displays human\-readable textual string which describes the cause of the last state change of the module. This object contains zero length string if no meaningful reason could be provided.  Examples\: 'Invalid software version' 'Software download failed' 'Software version mismatch' 'Module is in standby state' etc.  This object is for display purposes only. NMS applications must not parse this object and take any decision based on its value
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cefcmodulestatuslastchangetime
            
            	The value of sysUpTime at the time the cefcModuleOperStatus is changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcmoduleuptime
            
            	This object provides the up time for the module since it was last re\-initialized.  This object is not persistent; if a module reset, restart, power off, the up time starts from zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-entity'
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
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcModuleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcmoduleentry is not None:
                for child_ref in self.cefcmoduleentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable']['meta_info']


    class CefcPhysicalTable(object):
        """
        This table contains one row per physical entity.
        
        .. attribute:: cefcphysicalentry
        
        	Information about a particular physical entity
        	**type**\: list of :py:class:`CefcPhysicalEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcphysicalentry = YList()
            self.cefcphysicalentry.parent = self
            self.cefcphysicalentry.name = 'cefcphysicalentry'


        class CefcPhysicalEntry(object):
            """
            Information about a particular physical entity.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcphysicalstatus
            
            	The status of this physical entity. other(1) \- the status is not any of the listed below. supported(2) \- this entity is supported. unsupported(3) \- this entity is unsupported. incompatible(4) \- this entity is incompatible. It would be unsupported(3), if the ID read from Serial EPROM is not supported. It would be incompatible(4), if in the present configuration this FRU is not supported
            	**type**\: :py:class:`CefcPhysicalStatus_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry.CefcPhysicalStatus_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefcphysicalstatus = None

            class CefcPhysicalStatus_Enum(Enum):
                """
                CefcPhysicalStatus_Enum

                The status of this physical entity.
                other(1) \- the status is not any of the listed below.
                supported(2) \- this entity is supported.
                unsupported(3) \- this entity is unsupported.
                incompatible(4) \- this entity is incompatible.
                It would be unsupported(3), if the ID read from Serial
                EPROM is not supported. It would be incompatible(4), if
                in the present configuration this FRU is not supported.

                """

                OTHER = 1

                SUPPORTED = 2

                UNSUPPORTED = 3

                INCOMPATIBLE = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry.CefcPhysicalStatus_Enum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPhysicalTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPhysicalEntry[CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cefcphysicalstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPhysicalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcphysicalentry is not None:
                for child_ref in self.cefcphysicalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable']['meta_info']


    class CefcPowerSupplyInputTable(object):
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
        	**type**\: list of :py:class:`CefcPowerSupplyInputEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcpowersupplyinputentry = YList()
            self.cefcpowersupplyinputentry.parent = self
            self.cefcpowersupplyinputentry.name = 'cefcpowersupplyinputentry'


        class CefcPowerSupplyInputEntry(object):
            """
            An entry containing power input management information
            applicable to a particular power supply and input.
            
            .. attribute:: cefcpowersupplyinputindex
            
            	A unique value, greater than zero, for each input on a power supply
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcpowersupplyinputtype
            
            	The type of an input power detected on the power supply.  unknown(1)\: No input power is detected.  acLow(2)\: Lower rating AC input power is detected.  acHigh(3)\: Higher rating AC input power is detected.  dcLow(4)\: Lower rating DC input power is detected.  dcHigh(5)\: Higher rating DC input power is detected
            	**type**\: :py:class:`CefcPowerSupplyInputType_Enum <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry.CefcPowerSupplyInputType_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.cefcpowersupplyinputindex = None
                self.entphysicalindex = None
                self.cefcpowersupplyinputtype = None

            class CefcPowerSupplyInputType_Enum(Enum):
                """
                CefcPowerSupplyInputType_Enum

                The type of an input power detected on the power
                supply.
                
                unknown(1)\: No input power is detected.
                
                acLow(2)\: Lower rating AC input power is detected.
                
                acHigh(3)\: Higher rating AC input power is detected.
                
                dcLow(4)\: Lower rating DC input power is detected.
                
                dcHigh(5)\: Higher rating DC input power is detected.

                """

                UNKNOWN = 1

                ACLOW = 2

                ACHIGH = 3

                DCLOW = 4

                DCHIGH = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                    return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry.CefcPowerSupplyInputType_Enum']


            @property
            def _common_path(self):
                if self.cefcpowersupplyinputindex is None:
                    raise YPYDataValidationError('Key property cefcpowersupplyinputindex is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputEntry[CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputIndex = ' + str(self.cefcpowersupplyinputindex) + '][CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefcpowersupplyinputindex is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefcpowersupplyinputtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyInputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcpowersupplyinputentry is not None:
                for child_ref in self.cefcpowersupplyinputentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable']['meta_info']


    class CefcPowerSupplyOutputTable(object):
        """
        This table contains a list of possible output
        mode for the power supplies, whose ENTITY\-MIB
        entPhysicalTable entries have an entPhysicalClass
        of 'powerSupply'. It also indicate which mode
        is the operational mode within the system.
        
        .. attribute:: cefcpowersupplyoutputentry
        
        	A cefcPowerSupplyOutputTable entry lists the power output capacity and its operational status for manageable components of type PhysicalClass 'powerSupply'.  Entries are created by the agent at the system power\-up or power supply insertion.  Entries are deleted by the agent upon power supply removal.  The number of entries of a power supply is determined by the power supply
        	**type**\: list of :py:class:`CefcPowerSupplyOutputEntry <ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB.CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2013-08-19'

        def __init__(self):
            self.parent = None
            self.cefcpowersupplyoutputentry = YList()
            self.cefcpowersupplyoutputentry.parent = self
            self.cefcpowersupplyoutputentry.name = 'cefcpowersupplyoutputentry'


        class CefcPowerSupplyOutputEntry(object):
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
            
            .. attribute:: cefcpsoutputmodeindex
            
            	A unique value, greater than zero, for each possible output mode on a power supply
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcpsoutputmodecurrent
            
            	The output capacity of the power supply
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: cefcpsoutputmodeinoperation
            
            	A value of 'true' indicates that this mode is the operational mode of the power supply output capacity.  A value of 'false' indicates that this mode is not the operational mode of the power supply output capacity.  For a given power supply's entPhysicalIndex,  at most one instance of this object can have the value of true(1)
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2013-08-19'

            def __init__(self):
                self.parent = None
                self.cefcpsoutputmodeindex = None
                self.entphysicalindex = None
                self.cefcpsoutputmodecurrent = None
                self.cefcpsoutputmodeinoperation = None

            @property
            def _common_path(self):
                if self.cefcpsoutputmodeindex is None:
                    raise YPYDataValidationError('Key property cefcpsoutputmodeindex is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyOutputTable/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyOutputEntry[CISCO-ENTITY-FRU-CONTROL-MIB:cefcPSOutputModeIndex = ' + str(self.cefcpsoutputmodeindex) + '][CISCO-ENTITY-FRU-CONTROL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefcpsoutputmodeindex is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefcpsoutputmodecurrent is not None:
                    return True

                if self.cefcpsoutputmodeinoperation is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
                return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB/CISCO-ENTITY-FRU-CONTROL-MIB:cefcPowerSupplyOutputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcpowersupplyoutputentry is not None:
                for child_ref in self.cefcpowersupplyoutputentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
            return meta._meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-FRU-CONTROL-MIB:CISCO-ENTITY-FRU-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cefcchassiscoolingtable is not None and self.cefcchassiscoolingtable._has_data():
            return True

        if self.cefcchassiscoolingtable is not None and self.cefcchassiscoolingtable.is_presence():
            return True

        if self.cefcconnectorratingtable is not None and self.cefcconnectorratingtable._has_data():
            return True

        if self.cefcconnectorratingtable is not None and self.cefcconnectorratingtable.is_presence():
            return True

        if self.cefcfancoolingcaptable is not None and self.cefcfancoolingcaptable._has_data():
            return True

        if self.cefcfancoolingcaptable is not None and self.cefcfancoolingcaptable.is_presence():
            return True

        if self.cefcfancoolingtable is not None and self.cefcfancoolingtable._has_data():
            return True

        if self.cefcfancoolingtable is not None and self.cefcfancoolingtable.is_presence():
            return True

        if self.cefcfantraystatustable is not None and self.cefcfantraystatustable._has_data():
            return True

        if self.cefcfantraystatustable is not None and self.cefcfantraystatustable.is_presence():
            return True

        if self.cefcfrupower is not None and self.cefcfrupower._has_data():
            return True

        if self.cefcfrupower is not None and self.cefcfrupower.is_presence():
            return True

        if self.cefcfrupowerstatustable is not None and self.cefcfrupowerstatustable._has_data():
            return True

        if self.cefcfrupowerstatustable is not None and self.cefcfrupowerstatustable.is_presence():
            return True

        if self.cefcfrupowersupplygrouptable is not None and self.cefcfrupowersupplygrouptable._has_data():
            return True

        if self.cefcfrupowersupplygrouptable is not None and self.cefcfrupowersupplygrouptable.is_presence():
            return True

        if self.cefcfrupowersupplyvaluetable is not None and self.cefcfrupowersupplyvaluetable._has_data():
            return True

        if self.cefcfrupowersupplyvaluetable is not None and self.cefcfrupowersupplyvaluetable.is_presence():
            return True

        if self.cefcintellimoduletable is not None and self.cefcintellimoduletable._has_data():
            return True

        if self.cefcintellimoduletable is not None and self.cefcintellimoduletable.is_presence():
            return True

        if self.cefcmibnotificationenables is not None and self.cefcmibnotificationenables._has_data():
            return True

        if self.cefcmibnotificationenables is not None and self.cefcmibnotificationenables.is_presence():
            return True

        if self.cefcmodulecoolingtable is not None and self.cefcmodulecoolingtable._has_data():
            return True

        if self.cefcmodulecoolingtable is not None and self.cefcmodulecoolingtable.is_presence():
            return True

        if self.cefcmodulelocalswitchingtable is not None and self.cefcmodulelocalswitchingtable._has_data():
            return True

        if self.cefcmodulelocalswitchingtable is not None and self.cefcmodulelocalswitchingtable.is_presence():
            return True

        if self.cefcmodulepowerconsumptiontable is not None and self.cefcmodulepowerconsumptiontable._has_data():
            return True

        if self.cefcmodulepowerconsumptiontable is not None and self.cefcmodulepowerconsumptiontable.is_presence():
            return True

        if self.cefcmoduletable is not None and self.cefcmoduletable._has_data():
            return True

        if self.cefcmoduletable is not None and self.cefcmoduletable.is_presence():
            return True

        if self.cefcphysicaltable is not None and self.cefcphysicaltable._has_data():
            return True

        if self.cefcphysicaltable is not None and self.cefcphysicaltable.is_presence():
            return True

        if self.cefcpowersupplyinputtable is not None and self.cefcpowersupplyinputtable._has_data():
            return True

        if self.cefcpowersupplyinputtable is not None and self.cefcpowersupplyinputtable.is_presence():
            return True

        if self.cefcpowersupplyoutputtable is not None and self.cefcpowersupplyoutputtable._has_data():
            return True

        if self.cefcpowersupplyoutputtable is not None and self.cefcpowersupplyoutputtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_FRU_CONTROL_MIB as meta
        return meta._meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']


