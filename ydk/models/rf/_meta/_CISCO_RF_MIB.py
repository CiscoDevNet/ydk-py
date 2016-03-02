


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RFState_Enum' : _MetaInfoEnum('RFState_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'notKnown':'NOTKNOWN',
            'disabled':'DISABLED',
            'initialization':'INITIALIZATION',
            'negotiation':'NEGOTIATION',
            'standbyCold':'STANDBYCOLD',
            'standbyColdConfig':'STANDBYCOLDCONFIG',
            'standbyColdFileSys':'STANDBYCOLDFILESYS',
            'standbyColdBulk':'STANDBYCOLDBULK',
            'standbyHot':'STANDBYHOT',
            'activeFast':'ACTIVEFAST',
            'activeDrain':'ACTIVEDRAIN',
            'activePreconfig':'ACTIVEPRECONFIG',
            'activePostconfig':'ACTIVEPOSTCONFIG',
            'active':'ACTIVE',
            'activeExtraload':'ACTIVEEXTRALOAD',
            'activeHandback':'ACTIVEHANDBACK',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RFIssuState_Enum' : _MetaInfoEnum('RFIssuState_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'unset':'UNSET',
            'init':'INIT',
            'loadVersion':'LOADVERSION',
            'runVersion':'RUNVERSION',
            'commitVersion':'COMMITVERSION',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RFAction_Enum' : _MetaInfoEnum('RFAction_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'noAction':'NOACTION',
            'reloadPeer':'RELOADPEER',
            'reloadShelf':'RELOADSHELF',
            'switchActivity':'SWITCHACTIVITY',
            'forceSwitchActivity':'FORCESWITCHACTIVITY',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RFMode_Enum' : _MetaInfoEnum('RFMode_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'nonRedundant':'NONREDUNDANT',
            'staticLoadShareNonRedundant':'STATICLOADSHARENONREDUNDANT',
            'dynamicLoadShareNonRedundant':'DYNAMICLOADSHARENONREDUNDANT',
            'staticLoadShareRedundant':'STATICLOADSHAREREDUNDANT',
            'dynamicLoadShareRedundant':'DYNAMICLOADSHAREREDUNDANT',
            'coldStandbyRedundant':'COLDSTANDBYREDUNDANT',
            'warmStandbyRedundant':'WARMSTANDBYREDUNDANT',
            'hotStandbyRedundant':'HOTSTANDBYREDUNDANT',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RFClientStatus_Enum' : _MetaInfoEnum('RFClientStatus_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'noStatus':'NOSTATUS',
            'clientNotRedundant':'CLIENTNOTREDUNDANT',
            'clientRedundancyInProgress':'CLIENTREDUNDANCYINPROGRESS',
            'clientRedundant':'CLIENTREDUNDANT',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RFSwactReasonType_Enum' : _MetaInfoEnum('RFSwactReasonType_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'unsupported':'UNSUPPORTED',
            'none':'NONE',
            'notKnown':'NOTKNOWN',
            'userInitiated':'USERINITIATED',
            'userForced':'USERFORCED',
            'activeUnitFailed':'ACTIVEUNITFAILED',
            'activeUnitRemoved':'ACTIVEUNITREMOVED',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'RFIssuStateRev1_Enum' : _MetaInfoEnum('RFIssuStateRev1_Enum', 'ydk.models.rf.CISCO_RF_MIB',
        {
            'init':'INIT',
            'systemReset':'SYSTEMRESET',
            'loadVersion':'LOADVERSION',
            'loadVersionSwitchover':'LOADVERSIONSWITCHOVER',
            'runVersion':'RUNVERSION',
            'runVersionSwitchover':'RUNVERSIONSWITCHOVER',
            'commitVersion':'COMMITVERSION',
        }, 'CISCO-RF-MIB', _yang_ns._namespaces['CISCO-RF-MIB']),
    'CISCORFMIB.CRFCfg' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFCfg',
            False, 
            [
            _MetaInfoClassMember('cRFCfgAdminAction', REFERENCE_ENUM_CLASS, 'RFAction_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFAction_Enum', 
                [], [], 
                '''                This variable is set to invoke RF subsystem action commands.
                The commands are useful for maintenance and software upgrade
                activities.
                ''',
                'crfcfgadminaction',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveThresh', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The maximum acceptable value for the cRFCfgKeepaliveThresh
                object.
                ''',
                'crfcfgkeepalivethreshmax',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveThreshMin', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum acceptable value for the cRFCfgKeepaliveThresh
                object.
                ''',
                'crfcfgkeepalivethreshmin',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveTimer', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The maximum acceptable value for the cRFCfgKeepaliveTimer
                object.
                ''',
                'crfcfgkeepalivetimermax',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgKeepaliveTimerMin', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The maximum acceptable value for the cRFCfgNotifTimer
                object.
                ''',
                'crfcfgnotiftimermax',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgNotifTimerMin', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum acceptable value for the cRFCfgNotifTimer
                object.
                ''',
                'crfcfgnotiftimermin',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgRedundancyMode', REFERENCE_ENUM_CLASS, 'RFMode_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFMode_Enum', 
                [], [], 
                '''                Indicates the redundancy mode configured on the device.
                ''',
                'crfcfgredundancymode',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgRedundancyModeDescr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                Further clarifies or describes the redundancy mode indicated
                by cRFCfgRedundancyMode. Implementation-specific terminology
                associated with the current redundancy mode may be presented
                here.
                ''',
                'crfcfgredundancymodedescr',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFCfgRedundancyOperMode', REFERENCE_ENUM_CLASS, 'RFMode_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFMode_Enum', 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFHistory' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFHistory',
            False, 
            [
            _MetaInfoClassMember('cRFHistoryColdStarts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of system cold starts. This includes
                the number of system cold starts due to switchover failure
                and the number of manual restarts.
                ''',
                'crfhistorycoldstarts',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistoryStandByAvailTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Indicates the cumulative time that a standby redundant
                unit has been available since last system initialization.
                ''',
                'crfhistorystandbyavailtime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistoryTableMaxLength', ATTRIBUTE, 'int' , None, None, 
                [(0, 50)], [], 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFHistorySwitchOverTable.CRFHistorySwitchOverEntry' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFHistorySwitchOverTable.CRFHistorySwitchOverEntry',
            False, 
            [
            _MetaInfoClassMember('cRFHistorySwitchOverIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                A monotonically increasing integer for the purpose of
                indexing history table. After reaching maximum value,
                it wraps around to 1.
                ''',
                'crfhistoryswitchoverindex',
                'CISCO-RF-MIB', True),
            _MetaInfoClassMember('cRFHistoryCurrActiveUnitId', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Indicates the secondary redundant unit that took
                over as active.
                ''',
                'crfhistorycurractiveunitid',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistoryPrevActiveUnitId', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
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
            _MetaInfoClassMember('cRFHistorySwitchOverReason', REFERENCE_ENUM_CLASS, 'RFSwactReasonType_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFSwactReasonType_Enum', 
                [], [], 
                '''                Indicates the reason for the switchover.
                ''',
                'crfhistoryswitchoverreason',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFHistorySwitchOverEntry',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFHistorySwitchOverTable' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFHistorySwitchOverTable',
            False, 
            [
            _MetaInfoClassMember('cRFHistorySwitchOverEntry', REFERENCE_LIST, 'CRFHistorySwitchOverEntry' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFHistorySwitchOverTable.CRFHistorySwitchOverEntry', 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFStatus' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFStatus',
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
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the primary redundant unit took over
                as active. The value of this object will be 0 till the first
                switchover.
                ''',
                'crfstatusfailovertime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuFromVersion', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The IOS version from with the user is upgrading
                ''',
                'crfstatusissufromversion',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuState', REFERENCE_ENUM_CLASS, 'RFIssuState_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFIssuState_Enum', 
                [], [], 
                '''                The current ISSU state of the system.
                ''',
                'crfstatusissustate',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuStateRev1', REFERENCE_ENUM_CLASS, 'RFIssuStateRev1_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFIssuStateRev1_Enum', 
                [], [], 
                '''                The current ISSU state of the system.
                ''',
                'crfstatusissustaterev1',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusIssuToVersion', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The IOS version to with the user is upgrading
                ''',
                'crfstatusissutoversion',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusLastSwactReasonCode', REFERENCE_ENUM_CLASS, 'RFSwactReasonType_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFSwactReasonType_Enum', 
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
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the peer redundant unit entered the
                standbyHot state. The value will be 0 on system initialization.
                ''',
                'crfstatuspeerstandbyentrytime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusPeerUnitId', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
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
            _MetaInfoClassMember('cRFStatusPeerUnitState', REFERENCE_ENUM_CLASS, 'RFState_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFState_Enum', 
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
                [(0, 2147483647)], [], 
                '''                A unique identifier for this redundant unit. This identifier
                is implementation-specific but the method for selecting the id
                must remain consistent throughout the redundant system.
                
                Some example identifiers include: slot id, physical or logical
                entity id, or a unique id assigned internally by the RF
                subsystem.
                ''',
                'crfstatusunitid',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusUnitState', REFERENCE_ENUM_CLASS, 'RFState_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFState_Enum', 
                [], [], 
                '''                The current state of RF on this unit.
                ''',
                'crfstatusunitstate',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatus',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFStatusRFClientTable.CRFStatusRFClientEntry' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFStatusRFClientTable.CRFStatusRFClientEntry',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFClientID', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                A unique identifier for the client which registered with the
                Redundancy Facility.
                ''',
                'crfstatusrfclientid',
                'CISCO-RF-MIB', True),
            _MetaInfoClassMember('cRFStatusRFClientDescr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The description of the client which has registered with the
                Redundancy Facility.
                ''',
                'crfstatusrfclientdescr',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientRedTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time taken for this client to become Redundant. This value
                is meaningful when the value of cRFStatusRFClientStatus is
                not 'noStatus'.
                ''',
                'crfstatusrfclientredtime',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientSeq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sequence number of the client. The system assigns the
                sequence numbers based on the order of registration of
                the Redundancy Facility clients. 
                This is used for deciding order of RF events sent to clients.
                ''',
                'crfstatusrfclientseq',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientStatus', REFERENCE_ENUM_CLASS, 'RFClientStatus_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFClientStatus_Enum', 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFStatusRFClientTable' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFStatusRFClientTable',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFClientEntry', REFERENCE_LIST, 'CRFStatusRFClientEntry' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFStatusRFClientTable.CRFStatusRFClientEntry', 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFStatusRFModeCapsTable.CRFStatusRFModeCapsEntry' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFStatusRFModeCapsTable.CRFStatusRFModeCapsEntry',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFModeCapsMode', REFERENCE_ENUM_CLASS, 'RFMode_Enum' , 'ydk.models.rf.CISCO_RF_MIB', 'RFMode_Enum', 
                [], [], 
                '''                The redundancy mode that can be supported on the device.
                ''',
                'crfstatusrfmodecapsmode',
                'CISCO-RF-MIB', True),
            _MetaInfoClassMember('cRFStatusRFModeCapsModeDescr', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The description of the device implementation specific
                terminology associated with its supported redundancy mode.
                ''',
                'crfstatusrfmodecapsmodedescr',
                'CISCO-RF-MIB', False),
            ],
            'CISCO-RF-MIB',
            'cRFStatusRFModeCapsEntry',
            _yang_ns._namespaces['CISCO-RF-MIB'],
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB.CRFStatusRFModeCapsTable' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB.CRFStatusRFModeCapsTable',
            False, 
            [
            _MetaInfoClassMember('cRFStatusRFModeCapsEntry', REFERENCE_LIST, 'CRFStatusRFModeCapsEntry' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFStatusRFModeCapsTable.CRFStatusRFModeCapsEntry', 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
    'CISCORFMIB' : {
        'meta_info' : _MetaInfoClass('CISCORFMIB',
            False, 
            [
            _MetaInfoClassMember('cRFCfg', REFERENCE_CLASS, 'CRFCfg' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFCfg', 
                [], [], 
                '''                ''',
                'crfcfg',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistory', REFERENCE_CLASS, 'CRFHistory' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFHistory', 
                [], [], 
                '''                ''',
                'crfhistory',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFHistorySwitchOverTable', REFERENCE_CLASS, 'CRFHistorySwitchOverTable' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFHistorySwitchOverTable', 
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
            _MetaInfoClassMember('cRFStatus', REFERENCE_CLASS, 'CRFStatus' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFStatus', 
                [], [], 
                '''                ''',
                'crfstatus',
                'CISCO-RF-MIB', False),
            _MetaInfoClassMember('cRFStatusRFClientTable', REFERENCE_CLASS, 'CRFStatusRFClientTable' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFStatusRFClientTable', 
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
            _MetaInfoClassMember('cRFStatusRFModeCapsTable', REFERENCE_CLASS, 'CRFStatusRFModeCapsTable' , 'ydk.models.rf.CISCO_RF_MIB', 'CISCORFMIB.CRFStatusRFModeCapsTable', 
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
        'ydk.models.rf.CISCO_RF_MIB'
        ),
    },
}
_meta_table['CISCORFMIB.CRFHistorySwitchOverTable.CRFHistorySwitchOverEntry']['meta_info'].parent =_meta_table['CISCORFMIB.CRFHistorySwitchOverTable']['meta_info']
_meta_table['CISCORFMIB.CRFStatusRFClientTable.CRFStatusRFClientEntry']['meta_info'].parent =_meta_table['CISCORFMIB.CRFStatusRFClientTable']['meta_info']
_meta_table['CISCORFMIB.CRFStatusRFModeCapsTable.CRFStatusRFModeCapsEntry']['meta_info'].parent =_meta_table['CISCORFMIB.CRFStatusRFModeCapsTable']['meta_info']
_meta_table['CISCORFMIB.CRFCfg']['meta_info'].parent =_meta_table['CISCORFMIB']['meta_info']
_meta_table['CISCORFMIB.CRFHistory']['meta_info'].parent =_meta_table['CISCORFMIB']['meta_info']
_meta_table['CISCORFMIB.CRFHistorySwitchOverTable']['meta_info'].parent =_meta_table['CISCORFMIB']['meta_info']
_meta_table['CISCORFMIB.CRFStatus']['meta_info'].parent =_meta_table['CISCORFMIB']['meta_info']
_meta_table['CISCORFMIB.CRFStatusRFClientTable']['meta_info'].parent =_meta_table['CISCORFMIB']['meta_info']
_meta_table['CISCORFMIB.CRFStatusRFModeCapsTable']['meta_info'].parent =_meta_table['CISCORFMIB']['meta_info']
