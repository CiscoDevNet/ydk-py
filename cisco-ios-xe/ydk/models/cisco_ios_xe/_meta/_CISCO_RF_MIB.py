


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RfstateEnum' : _MetaInfoEnum('RfstateEnum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'notKnown':'notKnown',
            'disabled':'disabled',
            'initialization':'initialization',
            'negotiation':'negotiation',
            'standbyCold':'standbyCold',
            'standbyColdConfig':'standbyColdConfig',
            'standbyColdFileSys':'standbyColdFileSys',
            'standbyColdBulk':'standbyColdBulk',
            'standbyHot':'standbyHot',
            'activeFast':'activeFast',
            'activeDrain':'activeDrain',
            'activePreconfig':'activePreconfig',
            'activePostconfig':'activePostconfig',
            'active':'active',
            'activeExtraload':'activeExtraload',
            'activeHandback':'activeHandback',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RfclientstatusEnum' : _MetaInfoEnum('RfclientstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'noStatus':'noStatus',
            'clientNotRedundant':'clientNotRedundant',
            'clientRedundancyInProgress':'clientRedundancyInProgress',
            'clientRedundant':'clientRedundant',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RfswactreasontypeEnum' : _MetaInfoEnum('RfswactreasontypeEnum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'unsupported':'unsupported',
            'none':'none',
            'notKnown':'notKnown',
            'userInitiated':'userInitiated',
            'userForced':'userForced',
            'activeUnitFailed':'activeUnitFailed',
            'activeUnitRemoved':'activeUnitRemoved',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'Rfissustaterev1Enum' : _MetaInfoEnum('Rfissustaterev1Enum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'init':'init',
            'systemReset':'systemReset',
            'loadVersion':'loadVersion',
            'loadVersionSwitchover':'loadVersionSwitchover',
            'runVersion':'runVersion',
            'runVersionSwitchover':'runVersionSwitchover',
            'commitVersion':'commitVersion',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RfactionEnum' : _MetaInfoEnum('RfactionEnum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'noAction':'noAction',
            'reloadPeer':'reloadPeer',
            'reloadShelf':'reloadShelf',
            'switchActivity':'switchActivity',
            'forceSwitchActivity':'forceSwitchActivity',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RfissustateEnum' : _MetaInfoEnum('RfissustateEnum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'unset':'unset',
            'init':'init',
            'loadVersion':'loadVersion',
            'runVersion':'runVersion',
            'commitVersion':'commitVersion',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RfmodeEnum' : _MetaInfoEnum('RfmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_RF_MIB',
        {
            'nonRedundant':'nonRedundant',
            'staticLoadShareNonRedundant':'staticLoadShareNonRedundant',
            'dynamicLoadShareNonRedundant':'dynamicLoadShareNonRedundant',
            'staticLoadShareRedundant':'staticLoadShareRedundant',
            'dynamicLoadShareRedundant':'dynamicLoadShareRedundant',
            'coldStandbyRedundant':'coldStandbyRedundant',
            'warmStandbyRedundant':'warmStandbyRedundant',
            'hotStandbyRedundant':'hotStandbyRedundant',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'CiscoRfMib.Crfstatus' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfstatus',
            False, 
            [
            _MetaInfoClassMember('cRFStatusDuplexMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the redundant peer unit has been detected
                or not. If the redundant peer unit is detected, this object is
                true. If the redundant peer unit is not detected, this object
                is false.
                ''',
                'crfstatusduplexmode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusFailoverTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the primary redundant unit took over
                as active. The value of this object will be 0 till the first
                switchover.
                ''',
                'crfstatusfailovertime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuFromVersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The IOS version from with the user is upgrading
                ''',
                'crfstatusissufromversion',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuState', REFERENCE_ENUM_CLASS, 'RfissustateEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfissustateEnum', 
                [], [], 
                '''                The current ISSU state of the system.
                ''',
                'crfstatusissustate',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuStateRev1', REFERENCE_ENUM_CLASS, 'Rfissustaterev1Enum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'Rfissustaterev1Enum', 
                [], [], 
                '''                The current ISSU state of the system.
                ''',
                'crfstatusissustaterev1',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuToVersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The IOS version to with the user is upgrading
                ''',
                'crfstatusissutoversion',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusLastSwactReasonCode', REFERENCE_ENUM_CLASS, 'RfswactreasontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfswactreasontypeEnum', 
                [], [], 
                '''                The reason for the last switch of activity.
                ''',
                'crfstatuslastswactreasoncode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusManualSwactInhibit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether a manual switch of activity is
                permitted. If a manual switch of activity is allowed, this
                object is false. If a manual switch of activity is not
                allowed, this object is true. Note that the value of this
                object is the inverse of the status of manual SWACTs.
                
                This object does not indicate whether a switch of activity is
                or has occurred. This object only indicates if the
                user-controllable capability is enabled or not.
                
                A switch of activity is the event in which the standby
                redundant unit becomes active and the previously active unit
                becomes standby.
                ''',
                'crfstatusmanualswactinhibit',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusPeerStandByEntryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the peer redundant unit entered the
                standbyHot state. The value will be 0 on system initialization.
                ''',
                'crfstatuspeerstandbyentrytime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusPeerUnitId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                A unique identifier for the redundant peer unit. This
                identifier is implementation-specific but the method for
                selecting the id must remain consistent throughout the
                redundant system.
                
                Some example identifiers include: slot id, physical or logical
                entity id, or a unique id assigned internally by the RF
                subsystem.
                ''',
                'crfstatuspeerunitid',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusPeerUnitState', REFERENCE_ENUM_CLASS, 'RfstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfstateEnum', 
                [], [], 
                '''                The current state of RF on the peer unit.
                ''',
                'crfstatuspeerunitstate',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusPrimaryMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this is the primary redundant unit or
                not. If this unit is the primary unit, this object is true. If
                this unit is the secondary unit, this object is false.
                
                Note that the terms 'primary/secondary' are not synonymous
                with the terms 'active/standby'. At any given time, the
                primary unit may be the active unit, or the primary unit may
                be the standby unit. Likewise,   the secondary unit, at any
                given time, may be the active unit, or the secondary unit may
                be the standby unit.
                
                The primary unit is given a higher priority or precedence over
                the secondary unit. In a race condition (usually at
                initialization time) or any situation where the redundant
                units are unable to successfully negotiate activity between
                themselves, the primary unit will always become the active
                unit and the secondary unit will fall back to standby. Only
                one redundant unit can be the primary unit at any given time.
                
                The algorithm for determining the primary unit is system
                dependent, such as 'the redundant unit with the lower numeric
                unit id is always the primary unit.'
                ''',
                'crfstatusprimarymode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusUnitId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                A unique identifier for this redundant unit. This identifier
                is implementation-specific but the method for selecting the id
                must remain consistent throughout the redundant system.
                
                Some example identifiers include: slot id, physical or logical
                entity id, or a unique id assigned internally by the RF
                subsystem.
                ''',
                'crfstatusunitid',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusUnitState', REFERENCE_ENUM_CLASS, 'RfstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfstateEnum', 
                [], [], 
                '''                The current state of RF on this unit.
                ''',
                'crfstatusunitstate',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatus',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfcfg' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfcfg',
            False, 
            [
            _MetaInfoClassMember('cRFCfgAdminAction', REFERENCE_ENUM_CLASS, 'RfactionEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfactionEnum', 
                [], [], 
                '''                This variable is set to invoke RF subsystem action commands.
                The commands are useful for maintenance and software upgrade
                activities.
                ''',
                'crfcfgadminaction',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                On platforms that support keep-alives, the keep-alive
                threshold value designates the number of lost keep-alives
                tolerated before a failure condition is declared. If this
                occurs, a SWACT notification is sent.
                
                On platforms that do not support keep-alives, this object has
                no purpose or effect.
                ''',
                'crfcfgkeepalivethresh',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveThreshMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum acceptable value for the cRFCfgKeepaliveThresh
                object.
                ''',
                'crfcfgkeepalivethreshmax',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveThreshMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum acceptable value for the cRFCfgKeepaliveThresh
                object.
                ''',
                'crfcfgkeepalivethreshmin',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                On platforms that support keep-alives, the keep-alive timer
                value is used to guard against lost keep-alives. The RF
                subsystem expects to receive a keep-alive within this period.
                If a keep-alive is not received within this time period, a
                SWACT notification is sent.
                
                On platforms that do not support keep-alives, this object has
                no purpose or effect.
                ''',
                'crfcfgkeepalivetimer',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveTimerMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum acceptable value for the cRFCfgKeepaliveTimer
                object.
                ''',
                'crfcfgkeepalivetimermax',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveTimerMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum acceptable value for the cRFCfgKeepaliveTimer
                object.
                ''',
                'crfcfgkeepalivetimermin',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgMaintenanceMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether redundant units may communicate
                synchronization messages with each other. If communication is
                not permitted, this object is set to 'true'. If communication
                is permitted, this object is set to 'false'.
                
                If the value of this object is 'true', the redundant system is
                considered to be in a maintenance mode of operation. If the
                value of this object is 'false', the redundant system is
                considered to be in a normal (non-maintenance) mode of
                operation.
                
                In maintenance mode (true), the active unit will not
                communicate with the standby unit. The standby unit
                progression will not occur. When maintenance mode is disabled
                (false), the standby unit is reset to recover.
                
                Maintenance mode (true) is useful for maintenance-type
                operations.
                ''',
                'crfcfgmaintenancemode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgNotifsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allows enabling/disabling of RF subsystem notifications.
                ''',
                'crfcfgnotifsenabled',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgNotifTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Note that the term 'notification' here refers to an RF
                notification and not an SNMP notification.
                
                As the standby unit progresses to the 'standbyHot' state,
                asynchronous messages are sent from the active unit to the
                standby unit which must then be acknowledged by the standby
                unit. If the active unit receives the acknowledgement during
                the time period specified by this object, progression proceeds
                as normal. If the timer expires and an acknowledgement was not
                received by the active unit, a switch of activity occurs.
                ''',
                'crfcfgnotiftimer',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgNotifTimerMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum acceptable value for the cRFCfgNotifTimer
                object.
                ''',
                'crfcfgnotiftimermax',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgNotifTimerMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The minimum acceptable value for the cRFCfgNotifTimer
                object.
                ''',
                'crfcfgnotiftimermin',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgRedundancyMode', REFERENCE_ENUM_CLASS, 'RfmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfmodeEnum', 
                [], [], 
                '''                Indicates the redundancy mode configured on the device.
                ''',
                'crfcfgredundancymode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgRedundancyModeDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Further clarifies or describes the redundancy mode indicated
                by cRFCfgRedundancyMode. Implementation-specific terminology
                associated with the current redundancy mode may be presented
                here.
                ''',
                'crfcfgredundancymodedescr',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgRedundancyOperMode', REFERENCE_ENUM_CLASS, 'RfmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfmodeEnum', 
                [], [], 
                '''                Indicate the operational redundancy mode of the device.
                ''',
                'crfcfgredundancyopermode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgSplitMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether redundant units may communicate
                synchronization messages with each other. If communication is
                not permitted, this object is set to true. If communication is
                permitted, this object is set to false.
                
                In split mode (true), the active unit will not communicate
                with the standby unit. The standby unit progression will not
                occur. When split mode is disabled (false), the standby unit
                is reset to recover.
                
                Split mode (true) is useful for maintenance operations.
                ''',
                'crfcfgsplitmode',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFCfg',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfhistory' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfhistory',
            False, 
            [
            _MetaInfoClassMember('cRFHistoryColdStarts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of system cold starts. This includes
                the number of system cold starts due to switchover failure
                and the number of manual restarts.
                ''',
                'crfhistorycoldstarts',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistoryStandByAvailTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Indicates the cumulative time that a standby redundant
                unit has been available since last system initialization.
                ''',
                'crfhistorystandbyavailtime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistoryTableMaxLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '50')], [], 
                '''                Maximum number of entries permissible in the history
                table. A value of 0 will result in no history being
                maintained.
                ''',
                'crfhistorytablemaxlength',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFHistory',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFModeCapsMode', REFERENCE_ENUM_CLASS, 'RfmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfmodeEnum', 
                [], [], 
                '''                The redundancy mode that can be supported on the device.
                ''',
                'crfstatusrfmodecapsmode',
                'CISCO-RF-MIB', True),
            _MetaInfoClassMember('cRFStatusRFModeCapsModeDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The description of the device implementation specific
                terminology associated with its supported redundancy mode.
                ''',
                'crfstatusrfmodecapsmodedescr',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatusRFModeCapsEntry',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfstatusrfmodecapstable' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfstatusrfmodecapstable',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFModeCapsEntry', REFERENCE_LIST, 'Crfstatusrfmodecapsentry' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry', 
                [], [], 
                '''                An entry containing the device implementation specific
                terminology associated with the redundancy mode that can be
                supported on the device.
                ''',
                'crfstatusrfmodecapsentry',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatusRFModeCapsTable',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry',
            False, 
            [
            _MetaInfoClassMember('cRFHistorySwitchOverIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A monotonically increasing integer for the purpose of
                indexing history table. After reaching maximum value,
                it wraps around to 1.
                ''',
                'crfhistoryswitchoverindex',
                'CISCO-RF-MIB', True),
            _MetaInfoClassMember('cRFHistoryCurrActiveUnitId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Indicates the secondary redundant unit that took
                over as active.
                ''',
                'crfhistorycurractiveunitid',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistoryPrevActiveUnitId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Indicates the primary redundant unit that went down.
                ''',
                'crfhistoryprevactiveunitid',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistorySwactTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicates the Date & Time when switchover occurred.
                ''',
                'crfhistoryswacttime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistorySwitchOverReason', REFERENCE_ENUM_CLASS, 'RfswactreasontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfswactreasontypeEnum', 
                [], [], 
                '''                Indicates the reason for the switchover.
                ''',
                'crfhistoryswitchoverreason',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFHistorySwitchOverEntry',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfhistoryswitchovertable' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfhistoryswitchovertable',
            False, 
            [
            _MetaInfoClassMember('cRFHistorySwitchOverEntry', REFERENCE_LIST, 'Crfhistoryswitchoverentry' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry', 
                [], [], 
                '''                The entries in this table contain the switchover
                information. Each entry in the table is indexed by
                cRFHistorySwitchOverIndex. The index wraps around to 1
                after reaching the maximum value.
                ''',
                'crfhistoryswitchoverentry',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFHistorySwitchOverTable',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFClientID', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A unique identifier for the client which registered with the
                Redundancy Facility.
                ''',
                'crfstatusrfclientid',
                'CISCO-RF-MIB', True),
            _MetaInfoClassMember('cRFStatusRFClientDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The description of the client which has registered with the
                Redundancy Facility.
                ''',
                'crfstatusrfclientdescr',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientRedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time taken for this client to become Redundant. This value
                is meaningful when the value of cRFStatusRFClientStatus is
                not 'noStatus'.
                ''',
                'crfstatusrfclientredtime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientSeq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The sequence number of the client. The system assigns the
                sequence numbers based on the order of registration of
                the Redundancy Facility clients. 
                This is used for deciding order of RF events sent to clients.
                ''',
                'crfstatusrfclientseq',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientStatus', REFERENCE_ENUM_CLASS, 'RfclientstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'RfclientstatusEnum', 
                [], [], 
                '''                This object provides the status of the Redundancy Facility
                client.
                ''',
                'crfstatusrfclientstatus',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatusRFClientEntry',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib.Crfstatusrfclienttable' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib.Crfstatusrfclienttable',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFClientEntry', REFERENCE_LIST, 'Crfstatusrfcliententry' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry', 
                [], [], 
                '''                An entry containing information on various clients
                registered with the Redundancy Facility (RF). Entries in
                this table are always created by the system.
                
                An entry is created in this table when a redundancy aware 
                application registers with the Redundancy Facility. The entry 
                is destroyed when that application deregisters from the 
                Redundancy Facility.
                ''',
                'crfstatusrfcliententry',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatusRFClientTable',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
    'CiscoRfMib' : {
        'meta_info' : _MetaInfoClass('CiscoRfMib',
            False, 
            [
            _MetaInfoClassMember('cRFCfg', REFERENCE_CLASS, 'Crfcfg' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfcfg', 
                [], [], 
                '''                ''',
                'crfcfg',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistory', REFERENCE_CLASS, 'Crfhistory' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfhistory', 
                [], [], 
                '''                ''',
                'crfhistory',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistorySwitchOverTable', REFERENCE_CLASS, 'Crfhistoryswitchovertable' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfhistoryswitchovertable', 
                [], [], 
                '''                A table that tracks the history of all switchovers that
                have occurred since system initialization. The maximum
                number of entries permissible in this table is defined by
                cRFHistoryTableMaxLength. When the number of entries in
                the table reaches the maximum limit, the next entry
                would replace the oldest existing entry in the table.
                ''',
                'crfhistoryswitchovertable',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatus', REFERENCE_CLASS, 'Crfstatus' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfstatus', 
                [], [], 
                '''                ''',
                'crfstatus',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientTable', REFERENCE_CLASS, 'Crfstatusrfclienttable' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfstatusrfclienttable', 
                [], [], 
                '''                This table contains a list of RF clients that are
                registered on the device. 
                
                RF clients are applications that have registered with 
                the Redundancy Facility (RF) to receive RF events and 
                notifications. The purpose of RF clients is to synchronize 
                any relevant data with the standby unit.
                ''',
                'crfstatusrfclienttable',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFModeCapsTable', REFERENCE_CLASS, 'Crfstatusrfmodecapstable' , 'ydk.models.cisco_ios_xe.CISCO_RF_MIB', 'CiscoRfMib.Crfstatusrfmodecapstable', 
                [], [], 
                '''                This table containing a list of redundancy modes that can be
                supported on the device.
                ''',
                'crfstatusrfmodecapstable',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'CISCO-RF-MIB',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_RF_MIB'
        ),
    },
}
_meta_table['CiscoRfMib.Crfstatusrfmodecapstable.Crfstatusrfmodecapsentry']['meta_info'].parent =_meta_table['CiscoRfMib.Crfstatusrfmodecapstable']['meta_info']
_meta_table['CiscoRfMib.Crfhistoryswitchovertable.Crfhistoryswitchoverentry']['meta_info'].parent =_meta_table['CiscoRfMib.Crfhistoryswitchovertable']['meta_info']
_meta_table['CiscoRfMib.Crfstatusrfclienttable.Crfstatusrfcliententry']['meta_info'].parent =_meta_table['CiscoRfMib.Crfstatusrfclienttable']['meta_info']
_meta_table['CiscoRfMib.Crfstatus']['meta_info'].parent =_meta_table['CiscoRfMib']['meta_info']
_meta_table['CiscoRfMib.Crfcfg']['meta_info'].parent =_meta_table['CiscoRfMib']['meta_info']
_meta_table['CiscoRfMib.Crfhistory']['meta_info'].parent =_meta_table['CiscoRfMib']['meta_info']
_meta_table['CiscoRfMib.Crfstatusrfmodecapstable']['meta_info'].parent =_meta_table['CiscoRfMib']['meta_info']
_meta_table['CiscoRfMib.Crfhistoryswitchovertable']['meta_info'].parent =_meta_table['CiscoRfMib']['meta_info']
_meta_table['CiscoRfMib.Crfstatusrfclienttable']['meta_info'].parent =_meta_table['CiscoRfMib']['meta_info']
