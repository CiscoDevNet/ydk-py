


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ModuleAdminType_Enum' : _MetaInfoEnum('ModuleAdminType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
            'reset':'RESET',
            'outOfServiceAdmin':'OUTOFSERVICEADMIN',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'FRUCoolingUnit_Enum' : _MetaInfoEnum('FRUCoolingUnit_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'cfm':'CFM',
            'watts':'WATTS',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'PowerAdminType_Enum' : _MetaInfoEnum('PowerAdminType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'on':'ON',
            'off':'OFF',
            'inlineAuto':'INLINEAUTO',
            'inlineOn':'INLINEON',
            'powerCycle':'POWERCYCLE',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'ModuleOperType_Enum' : _MetaInfoEnum('ModuleOperType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'UNKNOWN',
            'ok':'OK',
            'disabled':'DISABLED',
            'okButDiagFailed':'OKBUTDIAGFAILED',
            'boot':'BOOT',
            'selfTest':'SELFTEST',
            'failed':'FAILED',
            'missing':'MISSING',
            'mismatchWithParent':'MISMATCHWITHPARENT',
            'mismatchConfig':'MISMATCHCONFIG',
            'diagFailed':'DIAGFAILED',
            'dormant':'DORMANT',
            'outOfServiceAdmin':'OUTOFSERVICEADMIN',
            'outOfServiceEnvTemp':'OUTOFSERVICEENVTEMP',
            'poweredDown':'POWEREDDOWN',
            'poweredUp':'POWEREDUP',
            'powerDenied':'POWERDENIED',
            'powerCycled':'POWERCYCLED',
            'okButPowerOverWarning':'OKBUTPOWEROVERWARNING',
            'okButPowerOverCritical':'OKBUTPOWEROVERCRITICAL',
            'syncInProgress':'SYNCINPROGRESS',
            'upgrading':'UPGRADING',
            'okButAuthFailed':'OKBUTAUTHFAILED',
            'mdr':'MDR',
            'fwMismatchFound':'FWMISMATCHFOUND',
            'fwDownloadSuccess':'FWDOWNLOADSUCCESS',
            'fwDownloadFailure':'FWDOWNLOADFAILURE',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'ModuleResetReasonType_Enum' : _MetaInfoEnum('ModuleResetReasonType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'UNKNOWN',
            'powerUp':'POWERUP',
            'parityError':'PARITYERROR',
            'clearConfigReset':'CLEARCONFIGRESET',
            'manualReset':'MANUALRESET',
            'watchDogTimeoutReset':'WATCHDOGTIMEOUTRESET',
            'resourceOverflowReset':'RESOURCEOVERFLOWRESET',
            'missingTaskReset':'MISSINGTASKRESET',
            'lowVoltageReset':'LOWVOLTAGERESET',
            'controllerReset':'CONTROLLERRESET',
            'systemReset':'SYSTEMRESET',
            'switchoverReset':'SWITCHOVERRESET',
            'upgradeReset':'UPGRADERESET',
            'downgradeReset':'DOWNGRADERESET',
            'cacheErrorReset':'CACHEERRORRESET',
            'deviceDriverReset':'DEVICEDRIVERRESET',
            'softwareExceptionReset':'SOFTWAREEXCEPTIONRESET',
            'restoreConfigReset':'RESTORECONFIGRESET',
            'abortRevReset':'ABORTREVRESET',
            'burnBootReset':'BURNBOOTRESET',
            'standbyCdHealthierReset':'STANDBYCDHEALTHIERRESET',
            'nonNativeConfigClearReset':'NONNATIVECONFIGCLEARRESET',
            'memoryProtectionErrorReset':'MEMORYPROTECTIONERRORRESET',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'PowerRedundancyType_Enum' : _MetaInfoEnum('PowerRedundancyType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'notsupported':'NOTSUPPORTED',
            'redundant':'REDUNDANT',
            'combined':'COMBINED',
            'nonRedundant':'NONREDUNDANT',
            'psRedundant':'PSREDUNDANT',
            'inPwrSrcRedundant':'INPWRSRCREDUNDANT',
            'psRedundantSingleInput':'PSREDUNDANTSINGLEINPUT',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'PowerOperType_Enum' : _MetaInfoEnum('PowerOperType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'offEnvOther':'OFFENVOTHER',
            'on':'ON',
            'offAdmin':'OFFADMIN',
            'offDenied':'OFFDENIED',
            'offEnvPower':'OFFENVPOWER',
            'offEnvTemp':'OFFENVTEMP',
            'offEnvFan':'OFFENVFAN',
            'failed':'FAILED',
            'onButFanFail':'ONBUTFANFAIL',
            'offCooling':'OFFCOOLING',
            'offConnectorRating':'OFFCONNECTORRATING',
            'onButInlinePowerFail':'ONBUTINLINEPOWERFAIL',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcChassisPerSlotCoolingCap', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum cooling capacity that could be provided
                for any slot in this chassis.
                
                The default unit of the cooling capacity is 'cfm', if
                cefcChassisPerSlotCoolingUnit is not supported.
                ''',
                'cefcchassisperslotcoolingcap',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcChassisPerSlotCoolingUnit', REFERENCE_ENUM_CLASS, 'FRUCoolingUnit_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit_Enum', 
                [], [], 
                '''                The unit of the maximum cooling capacity for any slot
                in this chassis.
                ''',
                'cefcchassisperslotcoolingunit',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcChassisCoolingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable',
            False, 
            [
            _MetaInfoClassMember('cefcChassisCoolingEntry', REFERENCE_LIST, 'CefcChassisCoolingEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry', 
                [], [], 
                '''                A cefcChassisCoolingEntry lists the maximum
                cooling capacity that could be provided 
                for one slot on the manageable components of type
                PhysicalClass 'chassis'.
                
                Entries are created by the agent if the corresponding
                entry is created in ENTITY-MIB entPhysicalTable.
                
                Entries are deleted by the agent if the corresponding
                entry is deleted in ENTITY-MIB entPhysicalTable.
                ''',
                'cefcchassiscoolingentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcChassisCoolingTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcConnectorRating', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                The maximum power that the component's
                connector can withdraw.
                ''',
                'cefcconnectorrating',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcConnectorRatingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable',
            False, 
            [
            _MetaInfoClassMember('cefcConnectorRatingEntry', REFERENCE_LIST, 'CefcConnectorRatingEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry', 
                [], [], 
                '''                A cefcConnectorRatingEntry lists the
                power connector rating information of a 
                component in the system.
                
                An entry or entries are created by the agent
                when an physical entity with connector rating 
                management is added to the ENTITY-MIB 
                entPhysicalTable. An entry is deleted 
                by the agent at the entity removal.
                ''',
                'cefcconnectorratingentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcConnectorRatingTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPower' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPower',
            False, 
            [
            _MetaInfoClassMember('cefcMaxDefaultHighInLinePower', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The system will provide power to the device connecting
                to the FRU if the device needs power, like an IP Phone.
                We call the providing power inline power.
                
                This MIB object controls the maximum default inline power
                for the device connecting to the FRU in the system.
                ''',
                'cefcmaxdefaulthighinlinepower',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcMaxDefaultInLinePower', ATTRIBUTE, 'int' , None, None, 
                [(0, 12500)], [], 
                '''                The system will provide power to the device connecting
                to the FRU if the device needs power, like an IP Phone.
                We call the providing power inline power.
                
                This MIB object controls the maximum default inline power
                for the device connecting to the FRU in the system. If the
                maximum default inline power of the device is greater than
                the maximum value reportable by this object, then this
                object should report its maximum reportable value (12500)
                and cefcMaxDefaultHighInLinePower must be used to report
                the actual maximum default inline power.
                ''',
                'cefcmaxdefaultinlinepower',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPower',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFRUCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Current supplied by the FRU (positive values)
                or current required to operate the FRU (negative values).
                ''',
                'cefcfrucurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerAdminStatus', REFERENCE_ENUM_CLASS, 'PowerAdminType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerAdminType_Enum', 
                [], [], 
                '''                Administratively desired FRU power state.
                ''',
                'cefcfrupoweradminstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerCapability', REFERENCE_BITS, 'CefcFRUPowerCapability_Bits' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry.CefcFRUPowerCapability_Bits', 
                [], [], 
                '''                This object indicates the set of supported power capabilities
                of the FRU.
                
                realTimeCurrent(0) -
                    cefcFRURealTimeCurrent is supported by the FRU.
                ''',
                'cefcfrupowercapability',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerOperStatus', REFERENCE_ENUM_CLASS, 'PowerOperType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerOperType_Enum', 
                [], [], 
                '''                Operational FRU power state.
                ''',
                'cefcfrupoweroperstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRURealTimeCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                This object indicates the realtime value of current supplied
                by the FRU (positive values) or the realtime value of current
                drawn by the FRU (negative values).
                ''',
                'cefcfrurealtimecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerStatusEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable',
            False, 
            [
            _MetaInfoClassMember('cefcFRUPowerStatusEntry', REFERENCE_LIST, 'CefcFRUPowerStatusEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry', 
                [], [], 
                '''                An cefcFRUPowerStatusTable entry lists the desired
                administrative status, the operational status of the 
                power manageable component, and the current required by 
                the component for operation.
                
                Entries are created by the agent at system power-up or 
                the insertion of the component.  Entries are deleted by
                the agent at the removal of the component.
                
                Only components with power control are listed in the 
                table.
                ''',
                'cefcfrupowerstatusentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerStatusTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry.CefcPowerNonRedundantReason_Enum' : _MetaInfoEnum('CefcPowerNonRedundantReason_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'unknown':'UNKNOWN',
            'singleSupply':'SINGLESUPPLY',
            'mismatchedSupplies':'MISMATCHEDSUPPLIES',
            'supplyError':'SUPPLYERROR',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPowerNonRedundantReason', REFERENCE_ENUM_CLASS, 'CefcPowerNonRedundantReason_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry.CefcPowerNonRedundantReason_Enum', 
                [], [], 
                '''                This object has the value of notApplicable(1) when
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
                ''',
                'cefcpowernonredundantreason',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerRedundancyMode', REFERENCE_ENUM_CLASS, 'PowerRedundancyType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerRedundancyType_Enum', 
                [], [], 
                '''                The administratively desired power supply redundancy
                mode.
                ''',
                'cefcpowerredundancymode',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerRedundancyOperMode', REFERENCE_ENUM_CLASS, 'PowerRedundancyType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerRedundancyType_Enum', 
                [], [], 
                '''                The power supply redundancy operational mode.
                ''',
                'cefcpowerredundancyopermode',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerUnits', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The units of primary supply to interpret
                cefcTotalAvailableCurrent and cefcTotalDrawnCurrent
                as power.
                
                For example, one 1000-watt power supply could 
                deliver 100 amperes at 10 volts DC.  So the value
                of cefcPowerUnits would be 'at 10 volts DC'.
                
                cefcPowerUnits is for display purposes only.
                ''',
                'cefcpowerunits',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcTotalAvailableCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Total current available for FRU usage.
                ''',
                'cefctotalavailablecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcTotalDrawnCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Total current drawn by powered-on FRUs.
                ''',
                'cefctotaldrawncurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcTotalDrawnInlineCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Total inline current drawn for inline operation.
                ''',
                'cefctotaldrawninlinecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerSupplyGroupEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable',
            False, 
            [
            _MetaInfoClassMember('cefcFRUPowerSupplyGroupEntry', REFERENCE_LIST, 'CefcFRUPowerSupplyGroupEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry', 
                [], [], 
                '''                An cefcFRUPowerSupplyGroupTable entry lists the desired
                redundancy mode, the units of the power outputs and the 
                available and drawn current for the power supply group.
                
                Entries are created by the agent when a power supply group
                is added to the entPhysicalTable. Entries are deleted by 
                the agent at power supply group removal.
                ''',
                'cefcfrupowersupplygroupentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerSupplyGroupTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFRUDrawnInlineCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Amount of current that is being drawn from this FRU for inline
                operation.
                ''',
                'cefcfrudrawninlinecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUDrawnSystemCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Amount of current drawn by the FRU's in the system towards
                system operations from this FRU
                ''',
                'cefcfrudrawnsystemcurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUTotalInlineCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Total current supplied by the FRU (positive values) for
                inline operations.
                ''',
                'cefcfrutotalinlinecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUTotalSystemCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                Total current that could be supplied by the FRU (positive
                values) for system operations.
                ''',
                'cefcfrutotalsystemcurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerSupplyValueEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable',
            False, 
            [
            _MetaInfoClassMember('cefcFRUPowerSupplyValueEntry', REFERENCE_LIST, 'CefcFRUPowerSupplyValueEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry', 
                [], [], 
                '''                An cefcFRUPowerSupplyValueTable entry lists the current
                provided by the FRU for operation.
                
                Entries are created by the agent at system power-up or 
                FRU insertion.  Entries are deleted by the agent at FRU
                removal.
                
                Only power supply FRUs are listed in the table.
                ''',
                'cefcfrupowersupplyvalueentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerSupplyValueTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry',
            False, 
            [
            _MetaInfoClassMember('cefcFanCoolingCapIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4095)], [], 
                '''                An arbitrary value that uniquely identifies a
                cooling capacity mode for a fan.
                ''',
                'cefcfancoolingcapindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanCoolingCapCapacity', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The cooling capacity that could be provided
                when the fan is operating in this mode.
                
                The default unit of the cooling capacity is 'cfm',
                if cefcFanCoolingCapCapacityUnit is not supported.
                ''',
                'cefcfancoolingcapcapacity',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapCapacityUnit', REFERENCE_ENUM_CLASS, 'FRUCoolingUnit_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit_Enum', 
                [], [], 
                '''                The unit of the fan cooling capacity when operating
                in this mode.
                ''',
                'cefcfancoolingcapcapacityunit',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                The power consumption of the fan when operating in
                in this mode.
                ''',
                'cefcfancoolingcapcurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapModeDescr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                A textual description of the cooling capacity
                mode of the fan.
                ''',
                'cefcfancoolingcapmodedescr',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanCoolingCapEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable',
            False, 
            [
            _MetaInfoClassMember('cefcFanCoolingCapEntry', REFERENCE_LIST, 'CefcFanCoolingCapEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry', 
                [], [], 
                '''                A cefcFanCoolingCapacityEntry lists the cooling
                capacity mode of a manageable components of type
                entPhysicalClass 'fan'. It also lists the corresponding
                cooling capacity provided and the power consumed
                by the fan on this mode.
                
                
                Entries are created by the agent if the corresponding
                entry is created in ENTITY-MIB entPhysicalTable.
                
                Entries are deleted by the agent if the corresponding
                entry is deleted in ENTITY-MIB entPhysicalTable.
                ''',
                'cefcfancoolingcapentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanCoolingCapTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanCoolingCapacity', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The cooling capacity that is provided by this fan.
                
                The default unit of the fan cooling capacity is 'cfm',
                if cefcFanCoolingCapacityUnit is not supported.
                ''',
                'cefcfancoolingcapacity',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapacityUnit', REFERENCE_ENUM_CLASS, 'FRUCoolingUnit_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit_Enum', 
                [], [], 
                '''                The unit of the fan cooling capacity.
                ''',
                'cefcfancoolingcapacityunit',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanCoolingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable',
            False, 
            [
            _MetaInfoClassMember('cefcFanCoolingEntry', REFERENCE_LIST, 'CefcFanCoolingEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry', 
                [], [], 
                '''                A cefcFanCoolingEntry lists the cooling
                capacity that is provided by the 
                manageable components of type PhysicalClass 
                'fan'.
                
                Entries are created by the agent if the corresponding
                entry is created in ENTITY-MIB entPhysicalTable.
                
                Entries are deleted by the agent if the corresponding
                entry is deleted in ENTITY-MIB entPhysicalTable.
                ''',
                'cefcfancoolingentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanCoolingTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry.CefcFanTrayOperStatus_Enum' : _MetaInfoEnum('CefcFanTrayOperStatus_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'UNKNOWN',
            'up':'UP',
            'down':'DOWN',
            'warning':'WARNING',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanTrayOperStatus', REFERENCE_ENUM_CLASS, 'CefcFanTrayOperStatus_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry.CefcFanTrayOperStatus_Enum', 
                [], [], 
                '''                The operational state of the fan or fan tray.
                unknown(1) - unknown.
                up(2) - powered on.
                down(3) - powered down.
                warning(4) - partial failure, needs replacement 
                             as soon as possible.
                ''',
                'cefcfantrayoperstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanTrayStatusEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable',
            False, 
            [
            _MetaInfoClassMember('cefcFanTrayStatusEntry', REFERENCE_LIST, 'CefcFanTrayStatusEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry', 
                [], [], 
                '''                An cefcFanTrayStatusTable entry lists the operational
                status information for the ENTITY-MIB entPhysicalTable 
                entry which is identified by the value of entPhysicalIndex.
                The value of entPhysicalClass for the identified entry will
                be 'fan', and the represented physical entity will be 
                either: one physical fan, or a single physical 'fan tray' 
                which is a manufactured (inseparable in the field) 
                combination of multiple fans.
                
                Entries are created by the agent at system power-up or 
                fan or fan tray insertion.  Entries are deleted 
                by the agent at the fan or fan tray removal.
                ''',
                'cefcfantraystatusentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanTrayStatusTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcIntelliModuleIPAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Internet address configured
                for the intelligent module.
                The type of this address is 
                determined by the value of the object 
                cefcIntelliModuleIPAddrType.
                ''',
                'cefcintellimoduleipaddr',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcIntelliModuleIPAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of Internet address by which the
                intelligent module is reachable.
                ''',
                'cefcintellimoduleipaddrtype',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcIntelliModuleEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable',
            False, 
            [
            _MetaInfoClassMember('cefcIntelliModuleEntry', REFERENCE_LIST, 'CefcIntelliModuleEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry', 
                [], [], 
                '''                A cefcIntelliModuleTable entry lists the
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
                ''',
                'cefcintellimoduleentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcIntelliModuleTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables',
            False, 
            [
            _MetaInfoClassMember('cefcEnablePSOutputChangeNotif', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates whether the system
                produces the cefcPowerSupplyOutputChange 
                notifications when the output capacity of 
                a power supply has changed. A false value 
                will prevent this notification to generated.
                ''',
                'cefcenablepsoutputchangenotif',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcMIBEnableStatusNotification', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates whether the system
                produces the following notifications:
                cefcModuleStatusChange, cefcPowerStatusChange, 
                cefcFRUInserted, cefcFRURemoved, 
                cefcUnrecognizedFRU and cefcFanTrayStatusChange.
                
                A false value will prevent these notifications
                from being generated.
                ''',
                'cefcmibenablestatusnotification',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcMIBNotificationEnables',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModuleCooling', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The cooling requirement of the module and its daughter
                cards.
                
                The default unit of the module cooling requirement is
                'cfm', if cefcModuleCoolingUnit is not supported.
                ''',
                'cefcmodulecooling',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleCoolingUnit', REFERENCE_ENUM_CLASS, 'FRUCoolingUnit_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'FRUCoolingUnit_Enum', 
                [], [], 
                '''                The unit of the cooling requirement of the module and its
                daughter cards.
                ''',
                'cefcmodulecoolingunit',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModuleCoolingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable',
            False, 
            [
            _MetaInfoClassMember('cefcModuleCoolingEntry', REFERENCE_LIST, 'CefcModuleCoolingEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry', 
                [], [], 
                '''                A cefcModuleCoolingEntry lists the cooling
                requirement for a manageable components of type
                entPhysicalClass 'module'.
                
                Entries are created by the agent at the system
                power-up or module insertion.
                
                Entries are deleted by the agent upon module
                removal.
                ''',
                'cefcmodulecoolingentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModuleCoolingTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry.CefcModuleLocalSwitchingMode_Enum' : _MetaInfoEnum('CefcModuleLocalSwitchingMode_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModuleLocalSwitchingMode', REFERENCE_ENUM_CLASS, 'CefcModuleLocalSwitchingMode_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry.CefcModuleLocalSwitchingMode_Enum', 
                [], [], 
                '''                This object specifies the mode of local switching.
                
                enabled(1)  - local switching is enabled.
                disabled(2) - local switching is disabled.
                ''',
                'cefcmodulelocalswitchingmode',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModuleLocalSwitchingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable',
            False, 
            [
            _MetaInfoClassMember('cefcModuleLocalSwitchingEntry', REFERENCE_LIST, 'CefcModuleLocalSwitchingEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry', 
                [], [], 
                '''                A cefcModuleLocalSwitchingTable entry lists the
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
                ''',
                'cefcmodulelocalswitchingentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModuleLocalSwitchingTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModulePowerConsumption', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                The combined power consumption to operate the module
                and its submodule(s) and inline-power device(s).
                ''',
                'cefcmodulepowerconsumption',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModulePowerConsumptionEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable',
            False, 
            [
            _MetaInfoClassMember('cefcModulePowerConsumptionEntry', REFERENCE_LIST, 'CefcModulePowerConsumptionEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry', 
                [], [], 
                '''                A cefcModulePowerConsumptionEntry lists the total
                power consumption of a manageable components of type
                entPhysicalClass 'module'.
                
                Entries are created by the agent at the system
                power-up or module insertion.
                
                Entries are deleted by the agent upon module
                removal.
                ''',
                'cefcmodulepowerconsumptionentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModulePowerConsumptionTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModuleAdminStatus', REFERENCE_ENUM_CLASS, 'ModuleAdminType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleAdminType_Enum', 
                [], [], 
                '''                This object provides administrative control of the
                module.
                ''',
                'cefcmoduleadminstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleLastClearConfigTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the
                configuration was most recently cleared.
                ''',
                'cefcmodulelastclearconfigtime',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleOperStatus', REFERENCE_ENUM_CLASS, 'ModuleOperType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleOperType_Enum', 
                [], [], 
                '''                This object shows the module's operational state.
                ''',
                'cefcmoduleoperstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleResetReason', REFERENCE_ENUM_CLASS, 'ModuleResetReasonType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleResetReasonType_Enum', 
                [], [], 
                '''                This object identifies the reason for the last reset performed
                on the module.
                ''',
                'cefcmoduleresetreason',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleResetReasonDescription', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                A description qualifying the module reset reason
                specified in cefcModuleResetReason. 
                
                Examples:
                  command xyz              
                  missing task
                  switch over
                  watchdog timeout    
                  etc.
                
                cefcModuleResetReasonDescription is for display purposes only.
                NMS applications must not parse.
                ''',
                'cefcmoduleresetreasondescription',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleStateChangeReasonDescr', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                This object displays human-readable textual string which
                describes the cause of the last state change of the
                module. This object contains zero length string
                if no meaningful reason could be provided.
                
                Examples:
                'Invalid software version'
                'Software download failed'
                'Software version mismatch'
                'Module is in standby state'
                etc.
                
                This object is for display purposes only.
                NMS applications must not parse this object
                and take any decision based on its value.
                ''',
                'cefcmodulestatechangereasondescr',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleStatusLastChangeTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time the cefcModuleOperStatus
                is changed.
                ''',
                'cefcmodulestatuslastchangetime',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the up time for the module
                since it was last re-initialized.
                
                This object is not persistent; if a module reset,
                restart, power off, the up time starts from zero.
                ''',
                'cefcmoduleuptime',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModuleEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcModuleTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcModuleTable',
            False, 
            [
            _MetaInfoClassMember('cefcModuleEntry', REFERENCE_LIST, 'CefcModuleEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry', 
                [], [], 
                '''                A cefcModuleStatusTable entry lists the operational and
                administrative status information for ENTITY-MIB
                entPhysicalTable entries for manageable components 
                of type PhysicalClass module(9).
                
                Entries are created by the agent at the system power-up or
                module insertion.
                
                Entries are deleted by the agent upon module removal.
                ''',
                'cefcmoduleentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModuleTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry.CefcPhysicalStatus_Enum' : _MetaInfoEnum('CefcPhysicalStatus_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'other':'OTHER',
            'supported':'SUPPORTED',
            'unsupported':'UNSUPPORTED',
            'incompatible':'INCOMPATIBLE',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPhysicalStatus', REFERENCE_ENUM_CLASS, 'CefcPhysicalStatus_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry.CefcPhysicalStatus_Enum', 
                [], [], 
                '''                The status of this physical entity.
                other(1) - the status is not any of the listed below.
                supported(2) - this entity is supported.
                unsupported(3) - this entity is unsupported.
                incompatible(4) - this entity is incompatible.
                It would be unsupported(3), if the ID read from Serial
                EPROM is not supported. It would be incompatible(4), if
                in the present configuration this FRU is not supported.
                ''',
                'cefcphysicalstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPhysicalEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable',
            False, 
            [
            _MetaInfoClassMember('cefcPhysicalEntry', REFERENCE_LIST, 'CefcPhysicalEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry', 
                [], [], 
                '''                Information about a particular physical entity.
                ''',
                'cefcphysicalentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPhysicalTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry.CefcPowerSupplyInputType_Enum' : _MetaInfoEnum('CefcPowerSupplyInputType_Enum', 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'UNKNOWN',
            'acLow':'ACLOW',
            'acHigh':'ACHIGH',
            'dcLow':'DCLOW',
            'dcHigh':'DCHIGH',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry',
            False, 
            [
            _MetaInfoClassMember('cefcPowerSupplyInputIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A unique value, greater than zero, for each input on
                a power supply.
                ''',
                'cefcpowersupplyinputindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPowerSupplyInputType', REFERENCE_ENUM_CLASS, 'CefcPowerSupplyInputType_Enum' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry.CefcPowerSupplyInputType_Enum', 
                [], [], 
                '''                The type of an input power detected on the power
                supply.
                
                unknown(1): No input power is detected.
                
                acLow(2): Lower rating AC input power is detected.
                
                acHigh(3): Higher rating AC input power is detected.
                
                dcLow(4): Lower rating DC input power is detected.
                
                dcHigh(5): Higher rating DC input power is detected.
                ''',
                'cefcpowersupplyinputtype',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPowerSupplyInputEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable',
            False, 
            [
            _MetaInfoClassMember('cefcPowerSupplyInputEntry', REFERENCE_LIST, 'CefcPowerSupplyInputEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry', 
                [], [], 
                '''                An entry containing power input management information
                applicable to a particular power supply and input.
                ''',
                'cefcpowersupplyinputentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPowerSupplyInputTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry',
            False, 
            [
            _MetaInfoClassMember('cefcPSOutputModeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A unique value, greater than zero, for each
                possible output mode on a power supply.
                ''',
                'cefcpsoutputmodeindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPSOutputModeCurrent', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                The output capacity of the power supply.
                ''',
                'cefcpsoutputmodecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPSOutputModeInOperation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A value of 'true' indicates that this mode is the
                operational mode of the power supply output
                capacity.
                
                A value of 'false' indicates that this mode is not
                the operational mode of the power supply output
                capacity.
                
                For a given power supply's entPhysicalIndex, 
                at most one instance of this object can have the
                value of true(1).
                ''',
                'cefcpsoutputmodeinoperation',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPowerSupplyOutputEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable',
            False, 
            [
            _MetaInfoClassMember('cefcPowerSupplyOutputEntry', REFERENCE_LIST, 'CefcPowerSupplyOutputEntry' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry', 
                [], [], 
                '''                A cefcPowerSupplyOutputTable entry lists the
                power output capacity and its operational status
                for manageable components of type PhysicalClass
                'powerSupply'.
                
                Entries are created by the agent at the system
                power-up or power supply insertion.
                
                Entries are deleted by the agent upon power supply
                removal.
                
                The number of entries of a power supply is determined
                by the power supply.
                ''',
                'cefcpowersupplyoutputentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPowerSupplyOutputTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CISCOENTITYFRUCONTROLMIB' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYFRUCONTROLMIB',
            False, 
            [
            _MetaInfoClassMember('cefcChassisCoolingTable', REFERENCE_CLASS, 'CefcChassisCoolingTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable', 
                [], [], 
                '''                This table contains the cooling capacity
                information of the chassis whose ENTITY-MIB
                entPhysicalTable entries have an
                entPhysicalClass of 'chassis'.
                ''',
                'cefcchassiscoolingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcConnectorRatingTable', REFERENCE_CLASS, 'CefcConnectorRatingTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable', 
                [], [], 
                '''                This table contains the connector power
                ratings of FRUs. 
                
                Only components with power connector rating 
                management are listed in this table.
                ''',
                'cefcconnectorratingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapTable', REFERENCE_CLASS, 'CefcFanCoolingCapTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable', 
                [], [], 
                '''                This table contains a list of the possible cooling
                capacity modes and properties of the fans, whose 
                ENTITY-MIB entPhysicalTable entries have an 
                entPhysicalClass of 'fan'.
                ''',
                'cefcfancoolingcaptable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingTable', REFERENCE_CLASS, 'CefcFanCoolingTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable', 
                [], [], 
                '''                This table contains the cooling capacity
                information of the fans whose ENTITY-MIB
                entPhysicalTable entries have an
                entPhysicalClass of 'fan'.
                ''',
                'cefcfancoolingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanTrayStatusTable', REFERENCE_CLASS, 'CefcFanTrayStatusTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable', 
                [], [], 
                '''                This table contains the operational status information
                for all ENTITY-MIB entPhysicalTable entries which have 
                an entPhysicalClass of 'fan'; specifically, all  
                entPhysicalTable entries which represent either: one 
                physical fan, or a single physical 'fan tray' which is a
                manufactured (inseparable in the field) combination of 
                multiple fans.
                ''',
                'cefcfantraystatustable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPower', REFERENCE_CLASS, 'CefcFRUPower' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPower', 
                [], [], 
                '''                ''',
                'cefcfrupower',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerStatusTable', REFERENCE_CLASS, 'CefcFRUPowerStatusTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable', 
                [], [], 
                '''                This table lists the power-related administrative status
                and operational status of the manageable components
                in the system.
                ''',
                'cefcfrupowerstatustable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerSupplyGroupTable', REFERENCE_CLASS, 'CefcFRUPowerSupplyGroupTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable', 
                [], [], 
                '''                This table lists the redundancy mode and the
                operational status of the power supply groups
                in the system.
                ''',
                'cefcfrupowersupplygrouptable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerSupplyValueTable', REFERENCE_CLASS, 'CefcFRUPowerSupplyValueTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable', 
                [], [], 
                '''                This table lists the power capacity of a power FRU in the
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
                ''',
                'cefcfrupowersupplyvaluetable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcIntelliModuleTable', REFERENCE_CLASS, 'CefcIntelliModuleTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable', 
                [], [], 
                '''                This table sparsely augments the
                cefcModuleTable (i.e., every row in
                this table corresponds to a row in
                the cefcModuleTable but not necessarily
                vice-versa).
                
                A cefcIntelliModuleTable entry lists the
                information specific to intelligent
                modules which cannot be provided by the
                cefcModuleTable.
                ''',
                'cefcintellimoduletable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcMIBNotificationEnables', REFERENCE_CLASS, 'CefcMIBNotificationEnables' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables', 
                [], [], 
                '''                ''',
                'cefcmibnotificationenables',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleCoolingTable', REFERENCE_CLASS, 'CefcModuleCoolingTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable', 
                [], [], 
                '''                This table contains the cooling requirement for
                all the manageable components of type entPhysicalClass
                'module'.
                ''',
                'cefcmodulecoolingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleLocalSwitchingTable', REFERENCE_CLASS, 'CefcModuleLocalSwitchingTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable', 
                [], [], 
                '''                This table sparsely augments the cefcModuleTable
                (i.e., every row in this table corresponds to a row in
                the cefcModuleTable but not necessarily vice-versa).
                
                A cefcModuleLocalSwitchingTable entry lists the
                information specific to local switching capable
                modules which cannot be provided by the
                cefcModuleTable.
                ''',
                'cefcmodulelocalswitchingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModulePowerConsumptionTable', REFERENCE_CLASS, 'CefcModulePowerConsumptionTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable', 
                [], [], 
                '''                This table contains the total power consumption
                information for modules whose ENTITY-MIB 
                entPhysicalTable entries have an entPhysicalClass 
                of 'module'.
                ''',
                'cefcmodulepowerconsumptiontable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleTable', REFERENCE_CLASS, 'CefcModuleTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcModuleTable', 
                [], [], 
                '''                A cefcModuleTable entry lists the operational and
                administrative status information for ENTITY-MIB
                entPhysicalTable entries for manageable components
                of type PhysicalClass module(9).
                ''',
                'cefcmoduletable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPhysicalTable', REFERENCE_CLASS, 'CefcPhysicalTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable', 
                [], [], 
                '''                This table contains one row per physical entity.
                ''',
                'cefcphysicaltable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerSupplyInputTable', REFERENCE_CLASS, 'CefcPowerSupplyInputTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable', 
                [], [], 
                '''                This table contains the power input information
                for all the power supplies that have entPhysicalTable
                entries with 'powerSupply' in the entPhysicalClass. 
                
                The entries are created by the agent at the system
                power-up or power supply insertion.
                
                Entries are deleted by the agent upon power supply
                removal.
                
                The number of entries is determined by the number of
                power supplies and number of power inputs on the power 
                supply.
                ''',
                'cefcpowersupplyinputtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerSupplyOutputTable', REFERENCE_CLASS, 'CefcPowerSupplyOutputTable' , 'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB', 'CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable', 
                [], [], 
                '''                This table contains a list of possible output
                mode for the power supplies, whose ENTITY-MIB
                entPhysicalTable entries have an entPhysicalClass
                of 'powerSupply'. It also indicate which mode
                is the operational mode within the system.
                ''',
                'cefcpowersupplyoutputtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.entity.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
}
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable.CefcChassisCoolingEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable.CefcConnectorRatingEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable.CefcFRUPowerStatusEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable.CefcFRUPowerSupplyGroupEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable.CefcFRUPowerSupplyValueEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable.CefcFanCoolingCapEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable.CefcFanCoolingEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable.CefcFanTrayStatusEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable.CefcIntelliModuleEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable.CefcModuleCoolingEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable.CefcModuleLocalSwitchingEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable.CefcModulePowerConsumptionEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable.CefcModuleEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable.CefcPhysicalEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable.CefcPowerSupplyInputEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable.CefcPowerSupplyOutputEntry']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcChassisCoolingTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcConnectorRatingTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPower']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerStatusTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyGroupTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFRUPowerSupplyValueTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingCapTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanCoolingTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcFanTrayStatusTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcIntelliModuleTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcMIBNotificationEnables']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleCoolingTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleLocalSwitchingTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModulePowerConsumptionTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcModuleTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPhysicalTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyInputTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
_meta_table['CISCOENTITYFRUCONTROLMIB.CefcPowerSupplyOutputTable']['meta_info'].parent =_meta_table['CISCOENTITYFRUCONTROLMIB']['meta_info']
