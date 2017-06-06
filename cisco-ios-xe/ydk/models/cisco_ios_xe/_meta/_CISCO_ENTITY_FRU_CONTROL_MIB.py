


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PoweropertypeEnum' : _MetaInfoEnum('PoweropertypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'offEnvOther':'offEnvOther',
            'on':'on',
            'offAdmin':'offAdmin',
            'offDenied':'offDenied',
            'offEnvPower':'offEnvPower',
            'offEnvTemp':'offEnvTemp',
            'offEnvFan':'offEnvFan',
            'failed':'failed',
            'onButFanFail':'onButFanFail',
            'offCooling':'offCooling',
            'offConnectorRating':'offConnectorRating',
            'onButInlinePowerFail':'onButInlinePowerFail',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'ModuleopertypeEnum' : _MetaInfoEnum('ModuleopertypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'unknown',
            'ok':'ok',
            'disabled':'disabled',
            'okButDiagFailed':'okButDiagFailed',
            'boot':'boot',
            'selfTest':'selfTest',
            'failed':'failed',
            'missing':'missing',
            'mismatchWithParent':'mismatchWithParent',
            'mismatchConfig':'mismatchConfig',
            'diagFailed':'diagFailed',
            'dormant':'dormant',
            'outOfServiceAdmin':'outOfServiceAdmin',
            'outOfServiceEnvTemp':'outOfServiceEnvTemp',
            'poweredDown':'poweredDown',
            'poweredUp':'poweredUp',
            'powerDenied':'powerDenied',
            'powerCycled':'powerCycled',
            'okButPowerOverWarning':'okButPowerOverWarning',
            'okButPowerOverCritical':'okButPowerOverCritical',
            'syncInProgress':'syncInProgress',
            'upgrading':'upgrading',
            'okButAuthFailed':'okButAuthFailed',
            'mdr':'mdr',
            'fwMismatchFound':'fwMismatchFound',
            'fwDownloadSuccess':'fwDownloadSuccess',
            'fwDownloadFailure':'fwDownloadFailure',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'FrucoolingunitEnum' : _MetaInfoEnum('FrucoolingunitEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'cfm':'cfm',
            'watts':'watts',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'ModuleadmintypeEnum' : _MetaInfoEnum('ModuleadmintypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
            'reset':'reset',
            'outOfServiceAdmin':'outOfServiceAdmin',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'PowerredundancytypeEnum' : _MetaInfoEnum('PowerredundancytypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'notsupported':'notsupported',
            'redundant':'redundant',
            'combined':'combined',
            'nonRedundant':'nonRedundant',
            'psRedundant':'psRedundant',
            'inPwrSrcRedundant':'inPwrSrcRedundant',
            'psRedundantSingleInput':'psRedundantSingleInput',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'PoweradmintypeEnum' : _MetaInfoEnum('PoweradmintypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'on':'on',
            'off':'off',
            'inlineAuto':'inlineAuto',
            'inlineOn':'inlineOn',
            'powerCycle':'powerCycle',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'ModuleresetreasontypeEnum' : _MetaInfoEnum('ModuleresetreasontypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'unknown',
            'powerUp':'powerUp',
            'parityError':'parityError',
            'clearConfigReset':'clearConfigReset',
            'manualReset':'manualReset',
            'watchDogTimeoutReset':'watchDogTimeoutReset',
            'resourceOverflowReset':'resourceOverflowReset',
            'missingTaskReset':'missingTaskReset',
            'lowVoltageReset':'lowVoltageReset',
            'controllerReset':'controllerReset',
            'systemReset':'systemReset',
            'switchoverReset':'switchoverReset',
            'upgradeReset':'upgradeReset',
            'downgradeReset':'downgradeReset',
            'cacheErrorReset':'cacheErrorReset',
            'deviceDriverReset':'deviceDriverReset',
            'softwareExceptionReset':'softwareExceptionReset',
            'restoreConfigReset':'restoreConfigReset',
            'abortRevReset':'abortRevReset',
            'burnBootReset':'burnBootReset',
            'standbyCdHealthierReset':'standbyCdHealthierReset',
            'nonNativeConfigClearReset':'nonNativeConfigClearReset',
            'memoryProtectionErrorReset':'memoryProtectionErrorReset',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CiscoEntityFruControlMib.Cefcfrupower' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupower',
            False, 
            [
            _MetaInfoClassMember('cefcMaxDefaultHighInLinePower', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The system will provide power to the device connecting
                to the FRU if the device needs power, like an IP Phone.
                We call the providing power inline power.
                
                This MIB object controls the maximum default inline power
                for the device connecting to the FRU in the system.
                ''',
                'cefcmaxdefaulthighinlinepower',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcMaxDefaultInLinePower', ATTRIBUTE, 'int' , None, None, 
                [('0', '12500')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmibnotificationenables' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmibnotificationenables',
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry.CefcpowernonredundantreasonEnum' : _MetaInfoEnum('CefcpowernonredundantreasonEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'notApplicable':'notApplicable',
            'unknown':'unknown',
            'singleSupply':'singleSupply',
            'mismatchedSupplies':'mismatchedSupplies',
            'supplyError':'supplyError',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPowerNonRedundantReason', REFERENCE_ENUM_CLASS, 'CefcpowernonredundantreasonEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry.CefcpowernonredundantreasonEnum', 
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
            _MetaInfoClassMember('cefcPowerRedundancyMode', REFERENCE_ENUM_CLASS, 'PowerredundancytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerredundancytypeEnum', 
                [], [], 
                '''                The administratively desired power supply redundancy
                mode.
                ''',
                'cefcpowerredundancymode',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerRedundancyOperMode', REFERENCE_ENUM_CLASS, 'PowerredundancytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PowerredundancytypeEnum', 
                [], [], 
                '''                The power supply redundancy operational mode.
                ''',
                'cefcpowerredundancyopermode',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerUnits', ATTRIBUTE, 'str' , None, None, 
                [], [], 
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
                [('-1000000000', '1000000000')], [], 
                '''                Total current available for FRU usage.
                ''',
                'cefctotalavailablecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcTotalDrawnCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Total current drawn by powered-on FRUs.
                ''',
                'cefctotaldrawncurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcTotalDrawnInlineCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Total inline current drawn for inline operation.
                ''',
                'cefctotaldrawninlinecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerSupplyGroupEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable',
            False, 
            [
            _MetaInfoClassMember('cefcFRUPowerSupplyGroupEntry', REFERENCE_LIST, 'Cefcfrupowersupplygroupentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFRUCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Current supplied by the FRU (positive values)
                or current required to operate the FRU (negative values).
                ''',
                'cefcfrucurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerAdminStatus', REFERENCE_ENUM_CLASS, 'PoweradmintypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PoweradmintypeEnum', 
                [], [], 
                '''                Administratively desired FRU power state.
                ''',
                'cefcfrupoweradminstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerCapability', REFERENCE_BITS, 'Cefcfrupowercapability' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry.Cefcfrupowercapability', 
                [], [], 
                '''                This object indicates the set of supported power capabilities
                of the FRU.
                
                realTimeCurrent(0) -
                    cefcFRURealTimeCurrent is supported by the FRU.
                ''',
                'cefcfrupowercapability',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerOperStatus', REFERENCE_ENUM_CLASS, 'PoweropertypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'PoweropertypeEnum', 
                [], [], 
                '''                Operational FRU power state.
                ''',
                'cefcfrupoweroperstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRURealTimeCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfrupowerstatustable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupowerstatustable',
            False, 
            [
            _MetaInfoClassMember('cefcFRUPowerStatusEntry', REFERENCE_LIST, 'Cefcfrupowerstatusentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFRUDrawnInlineCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Amount of current that is being drawn from this FRU for inline
                operation.
                ''',
                'cefcfrudrawninlinecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUDrawnSystemCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Amount of current drawn by the FRU's in the system towards
                system operations from this FRU
                ''',
                'cefcfrudrawnsystemcurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUTotalInlineCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Total current supplied by the FRU (positive values) for
                inline operations.
                ''',
                'cefcfrutotalinlinecurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUTotalSystemCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                Total current that could be supplied by the FRU (positive
                values) for system operations.
                ''',
                'cefcfrutotalsystemcurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFRUPowerSupplyValueEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable',
            False, 
            [
            _MetaInfoClassMember('cefcFRUPowerSupplyValueEntry', REFERENCE_LIST, 'Cefcfrupowersupplyvalueentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModuleAdminStatus', REFERENCE_ENUM_CLASS, 'ModuleadmintypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleadmintypeEnum', 
                [], [], 
                '''                This object provides administrative control of the
                module.
                ''',
                'cefcmoduleadminstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleLastClearConfigTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the
                configuration was most recently cleared.
                ''',
                'cefcmodulelastclearconfigtime',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleOperStatus', REFERENCE_ENUM_CLASS, 'ModuleopertypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleopertypeEnum', 
                [], [], 
                '''                This object shows the module's operational state.
                ''',
                'cefcmoduleoperstatus',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleResetReason', REFERENCE_ENUM_CLASS, 'ModuleresetreasontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'ModuleresetreasontypeEnum', 
                [], [], 
                '''                This object identifies the reason for the last reset performed
                on the module.
                ''',
                'cefcmoduleresetreason',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleResetReasonDescription', ATTRIBUTE, 'str' , None, None, 
                [], [], 
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
                [], [], 
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
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time the cefcModuleOperStatus
                is changed.
                ''',
                'cefcmodulestatuslastchangetime',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmoduletable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmoduletable',
            False, 
            [
            _MetaInfoClassMember('cefcModuleEntry', REFERENCE_LIST, 'Cefcmoduleentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
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
            _MetaInfoClassMember('cefcIntelliModuleIPAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcintellimoduletable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcintellimoduletable',
            False, 
            [
            _MetaInfoClassMember('cefcIntelliModuleEntry', REFERENCE_LIST, 'Cefcintellimoduleentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry.CefcmodulelocalswitchingmodeEnum' : _MetaInfoEnum('CefcmodulelocalswitchingmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModuleLocalSwitchingMode', REFERENCE_ENUM_CLASS, 'CefcmodulelocalswitchingmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry.CefcmodulelocalswitchingmodeEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable',
            False, 
            [
            _MetaInfoClassMember('cefcModuleLocalSwitchingEntry', REFERENCE_LIST, 'Cefcmodulelocalswitchingentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry.CefcfantrayoperstatusEnum' : _MetaInfoEnum('CefcfantrayoperstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'unknown',
            'up':'up',
            'down':'down',
            'warning':'warning',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanTrayOperStatus', REFERENCE_ENUM_CLASS, 'CefcfantrayoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry.CefcfantrayoperstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfantraystatustable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfantraystatustable',
            False, 
            [
            _MetaInfoClassMember('cefcFanTrayStatusEntry', REFERENCE_LIST, 'Cefcfantraystatusentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry.CefcphysicalstatusEnum' : _MetaInfoEnum('CefcphysicalstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'other':'other',
            'supported':'supported',
            'unsupported':'unsupported',
            'incompatible':'incompatible',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPhysicalStatus', REFERENCE_ENUM_CLASS, 'CefcphysicalstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry.CefcphysicalstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcphysicaltable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcphysicaltable',
            False, 
            [
            _MetaInfoClassMember('cefcPhysicalEntry', REFERENCE_LIST, 'Cefcphysicalentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry', 
                [], [], 
                '''                Information about a particular physical entity.
                ''',
                'cefcphysicalentry',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcPhysicalTable',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry.CefcpowersupplyinputtypeEnum' : _MetaInfoEnum('CefcpowersupplyinputtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB',
        {
            'unknown':'unknown',
            'acLow':'acLow',
            'acHigh':'acHigh',
            'dcLow':'dcLow',
            'dcHigh':'dcHigh',
        }, 'CISCO-ENTITY-FRU-CONTROL-MIB', _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB']),
    'CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPowerSupplyInputIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique value, greater than zero, for each input on
                a power supply.
                ''',
                'cefcpowersupplyinputindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPowerSupplyInputType', REFERENCE_ENUM_CLASS, 'CefcpowersupplyinputtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry.CefcpowersupplyinputtypeEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcpowersupplyinputtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcpowersupplyinputtable',
            False, 
            [
            _MetaInfoClassMember('cefcPowerSupplyInputEntry', REFERENCE_LIST, 'Cefcpowersupplyinputentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPSOutputModeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique value, greater than zero, for each
                possible output mode on a power supply.
                ''',
                'cefcpsoutputmodeindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcPSOutputModeCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcpowersupplyoutputtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcpowersupplyoutputtable',
            False, 
            [
            _MetaInfoClassMember('cefcPowerSupplyOutputEntry', REFERENCE_LIST, 'Cefcpowersupplyoutputentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcChassisPerSlotCoolingCap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum cooling capacity that could be provided
                for any slot in this chassis.
                
                The default unit of the cooling capacity is 'cfm', if
                cefcChassisPerSlotCoolingUnit is not supported.
                ''',
                'cefcchassisperslotcoolingcap',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcChassisPerSlotCoolingUnit', REFERENCE_ENUM_CLASS, 'FrucoolingunitEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FrucoolingunitEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcchassiscoolingtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcchassiscoolingtable',
            False, 
            [
            _MetaInfoClassMember('cefcChassisCoolingEntry', REFERENCE_LIST, 'Cefcchassiscoolingentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanCoolingCapacity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cooling capacity that is provided by this fan.
                
                The default unit of the fan cooling capacity is 'cfm',
                if cefcFanCoolingCapacityUnit is not supported.
                ''',
                'cefcfancoolingcapacity',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapacityUnit', REFERENCE_ENUM_CLASS, 'FrucoolingunitEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FrucoolingunitEnum', 
                [], [], 
                '''                The unit of the fan cooling capacity.
                ''',
                'cefcfancoolingcapacityunit',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanCoolingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfancoolingtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfancoolingtable',
            False, 
            [
            _MetaInfoClassMember('cefcFanCoolingEntry', REFERENCE_LIST, 'Cefcfancoolingentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModuleCooling', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cooling requirement of the module and its daughter
                cards.
                
                The default unit of the module cooling requirement is
                'cfm', if cefcModuleCoolingUnit is not supported.
                ''',
                'cefcmodulecooling',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleCoolingUnit', REFERENCE_ENUM_CLASS, 'FrucoolingunitEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FrucoolingunitEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmodulecoolingtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmodulecoolingtable',
            False, 
            [
            _MetaInfoClassMember('cefcModuleCoolingEntry', REFERENCE_LIST, 'Cefcmodulecoolingentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanCoolingCapIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                An arbitrary value that uniquely identifies a
                cooling capacity mode for a fan.
                ''',
                'cefcfancoolingcapindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcFanCoolingCapCapacity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cooling capacity that could be provided
                when the fan is operating in this mode.
                
                The default unit of the cooling capacity is 'cfm',
                if cefcFanCoolingCapCapacityUnit is not supported.
                ''',
                'cefcfancoolingcapcapacity',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapCapacityUnit', REFERENCE_ENUM_CLASS, 'FrucoolingunitEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'FrucoolingunitEnum', 
                [], [], 
                '''                The unit of the fan cooling capacity when operating
                in this mode.
                ''',
                'cefcfancoolingcapcapacityunit',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapCurrent', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                The power consumption of the fan when operating in
                in this mode.
                ''',
                'cefcfancoolingcapcurrent',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapModeDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the cooling capacity
                mode of the fan.
                ''',
                'cefcfancoolingcapmodedescr',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcFanCoolingCapEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcfancoolingcaptable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcfancoolingcaptable',
            False, 
            [
            _MetaInfoClassMember('cefcFanCoolingCapEntry', REFERENCE_LIST, 'Cefcfancoolingcapentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcConnectorRating', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                The maximum power that the component's
                connector can withdraw.
                ''',
                'cefcconnectorrating',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcConnectorRatingEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcconnectorratingtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcconnectorratingtable',
            False, 
            [
            _MetaInfoClassMember('cefcConnectorRatingEntry', REFERENCE_LIST, 'Cefcconnectorratingentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-FRU-CONTROL-MIB', True),
            _MetaInfoClassMember('cefcModulePowerConsumption', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1000000000')], [], 
                '''                The combined power consumption to operate the module
                and its submodule(s) and inline-power device(s).
                ''',
                'cefcmodulepowerconsumption',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            ],
            'CISCO-ENTITY-FRU-CONTROL-MIB',
            'cefcModulePowerConsumptionEntry',
            _yang_ns._namespaces['CISCO-ENTITY-FRU-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable',
            False, 
            [
            _MetaInfoClassMember('cefcModulePowerConsumptionEntry', REFERENCE_LIST, 'Cefcmodulepowerconsumptionentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
    'CiscoEntityFruControlMib' : {
        'meta_info' : _MetaInfoClass('CiscoEntityFruControlMib',
            False, 
            [
            _MetaInfoClassMember('cefcChassisCoolingTable', REFERENCE_CLASS, 'Cefcchassiscoolingtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcchassiscoolingtable', 
                [], [], 
                '''                This table contains the cooling capacity
                information of the chassis whose ENTITY-MIB
                entPhysicalTable entries have an
                entPhysicalClass of 'chassis'.
                ''',
                'cefcchassiscoolingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcConnectorRatingTable', REFERENCE_CLASS, 'Cefcconnectorratingtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcconnectorratingtable', 
                [], [], 
                '''                This table contains the connector power
                ratings of FRUs. 
                
                Only components with power connector rating 
                management are listed in this table.
                ''',
                'cefcconnectorratingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingCapTable', REFERENCE_CLASS, 'Cefcfancoolingcaptable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfancoolingcaptable', 
                [], [], 
                '''                This table contains a list of the possible cooling
                capacity modes and properties of the fans, whose 
                ENTITY-MIB entPhysicalTable entries have an 
                entPhysicalClass of 'fan'.
                ''',
                'cefcfancoolingcaptable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanCoolingTable', REFERENCE_CLASS, 'Cefcfancoolingtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfancoolingtable', 
                [], [], 
                '''                This table contains the cooling capacity
                information of the fans whose ENTITY-MIB
                entPhysicalTable entries have an
                entPhysicalClass of 'fan'.
                ''',
                'cefcfancoolingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFanTrayStatusTable', REFERENCE_CLASS, 'Cefcfantraystatustable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfantraystatustable', 
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
            _MetaInfoClassMember('cefcFRUPower', REFERENCE_CLASS, 'Cefcfrupower' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupower', 
                [], [], 
                '''                ''',
                'cefcfrupower',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerStatusTable', REFERENCE_CLASS, 'Cefcfrupowerstatustable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowerstatustable', 
                [], [], 
                '''                This table lists the power-related administrative status
                and operational status of the manageable components
                in the system.
                ''',
                'cefcfrupowerstatustable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerSupplyGroupTable', REFERENCE_CLASS, 'Cefcfrupowersupplygrouptable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable', 
                [], [], 
                '''                This table lists the redundancy mode and the
                operational status of the power supply groups
                in the system.
                ''',
                'cefcfrupowersupplygrouptable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcFRUPowerSupplyValueTable', REFERENCE_CLASS, 'Cefcfrupowersupplyvaluetable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable', 
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
            _MetaInfoClassMember('cefcIntelliModuleTable', REFERENCE_CLASS, 'Cefcintellimoduletable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcintellimoduletable', 
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
            _MetaInfoClassMember('cefcMIBNotificationEnables', REFERENCE_CLASS, 'Cefcmibnotificationenables' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmibnotificationenables', 
                [], [], 
                '''                ''',
                'cefcmibnotificationenables',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleCoolingTable', REFERENCE_CLASS, 'Cefcmodulecoolingtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulecoolingtable', 
                [], [], 
                '''                This table contains the cooling requirement for
                all the manageable components of type entPhysicalClass
                'module'.
                ''',
                'cefcmodulecoolingtable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleLocalSwitchingTable', REFERENCE_CLASS, 'Cefcmodulelocalswitchingtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable', 
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
            _MetaInfoClassMember('cefcModulePowerConsumptionTable', REFERENCE_CLASS, 'Cefcmodulepowerconsumptiontable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable', 
                [], [], 
                '''                This table contains the total power consumption
                information for modules whose ENTITY-MIB 
                entPhysicalTable entries have an entPhysicalClass 
                of 'module'.
                ''',
                'cefcmodulepowerconsumptiontable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcModuleTable', REFERENCE_CLASS, 'Cefcmoduletable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcmoduletable', 
                [], [], 
                '''                A cefcModuleTable entry lists the operational and
                administrative status information for ENTITY-MIB
                entPhysicalTable entries for manageable components
                of type PhysicalClass module(9).
                ''',
                'cefcmoduletable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPhysicalTable', REFERENCE_CLASS, 'Cefcphysicaltable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcphysicaltable', 
                [], [], 
                '''                This table contains one row per physical entity.
                ''',
                'cefcphysicaltable',
                'CISCO-ENTITY-FRU-CONTROL-MIB', False),
            _MetaInfoClassMember('cefcPowerSupplyInputTable', REFERENCE_CLASS, 'Cefcpowersupplyinputtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcpowersupplyinputtable', 
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
            _MetaInfoClassMember('cefcPowerSupplyOutputTable', REFERENCE_CLASS, 'Cefcpowersupplyoutputtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB', 'CiscoEntityFruControlMib.Cefcpowersupplyoutputtable', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_FRU_CONTROL_MIB'
        ),
    },
}
_meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable.Cefcfrupowersupplygroupentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfrupowerstatustable.Cefcfrupowerstatusentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcfrupowerstatustable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable.Cefcfrupowersupplyvalueentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmoduletable.Cefcmoduleentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcmoduletable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcintellimoduletable.Cefcintellimoduleentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcintellimoduletable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable.Cefcmodulelocalswitchingentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfantraystatustable.Cefcfantraystatusentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcfantraystatustable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcphysicaltable.Cefcphysicalentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcphysicaltable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcpowersupplyinputtable.Cefcpowersupplyinputentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcpowersupplyinputtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcpowersupplyoutputtable.Cefcpowersupplyoutputentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcpowersupplyoutputtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcchassiscoolingtable.Cefcchassiscoolingentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcchassiscoolingtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfancoolingtable.Cefcfancoolingentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcfancoolingtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmodulecoolingtable.Cefcmodulecoolingentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcmodulecoolingtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfancoolingcaptable.Cefcfancoolingcapentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcfancoolingcaptable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcconnectorratingtable.Cefcconnectorratingentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcconnectorratingtable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable.Cefcmodulepowerconsumptionentry']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfrupower']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmibnotificationenables']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplygrouptable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfrupowerstatustable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfrupowersupplyvaluetable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmoduletable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcintellimoduletable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmodulelocalswitchingtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfantraystatustable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcphysicaltable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcpowersupplyinputtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcpowersupplyoutputtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcchassiscoolingtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfancoolingtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmodulecoolingtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcfancoolingcaptable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcconnectorratingtable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
_meta_table['CiscoEntityFruControlMib.Cefcmodulepowerconsumptiontable']['meta_info'].parent =_meta_table['CiscoEntityFruControlMib']['meta_info']
