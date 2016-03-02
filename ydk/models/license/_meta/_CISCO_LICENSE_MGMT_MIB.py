


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ClmgmtLicenseActionState_Enum' : _MetaInfoEnum('ClmgmtLicenseActionState_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'none':'NONE',
            'pending':'PENDING',
            'inProgress':'INPROGRESS',
            'successful':'SUCCESSFUL',
            'partiallySuccessful':'PARTIALLYSUCCESSFUL',
            'failed':'FAILED',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'ClmgmtLicenseActionFailCause_Enum' : _MetaInfoEnum('ClmgmtLicenseActionFailCause_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'none':'NONE',
            'generalFailure':'GENERALFAILURE',
            'transferProtocolNotSupported':'TRANSFERPROTOCOLNOTSUPPORTED',
            'fileServerNotReachable':'FILESERVERNOTREACHABLE',
            'unrecognizedEntPhysicalIndex':'UNRECOGNIZEDENTPHYSICALINDEX',
            'invalidLicenseFilePath':'INVALIDLICENSEFILEPATH',
            'invalidLicenseFile':'INVALIDLICENSEFILE',
            'invalidLicenseLine':'INVALIDLICENSELINE',
            'licenseAlreadyExists':'LICENSEALREADYEXISTS',
            'licenseNotValidForDevice':'LICENSENOTVALIDFORDEVICE',
            'invalidLicenseCount':'INVALIDLICENSECOUNT',
            'invalidLicensePeriod':'INVALIDLICENSEPERIOD',
            'licenseInUse':'LICENSEINUSE',
            'invalidLicenseStore':'INVALIDLICENSESTORE',
            'licenseStorageFull':'LICENSESTORAGEFULL',
            'invalidPermissionTicketFile':'INVALIDPERMISSIONTICKETFILE',
            'invalidPermissionTicket':'INVALIDPERMISSIONTICKET',
            'invalidRehostTicketFile':'INVALIDREHOSTTICKETFILE',
            'invalidRehostTicket':'INVALIDREHOSTTICKET',
            'invalidLicenseBackupFile':'INVALIDLICENSEBACKUPFILE',
            'licenseClearInProgress':'LICENSECLEARINPROGRESS',
            'invalidLicenseEULAFile':'INVALIDLICENSEEULAFILE',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'ClmgmtLicenseTransferProtocol_Enum' : _MetaInfoEnum('ClmgmtLicenseTransferProtocol_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'none':'NONE',
            'local':'LOCAL',
            'tftp':'TFTP',
            'ftp':'FTP',
            'rcp':'RCP',
            'http':'HTTP',
            'scp':'SCP',
            'sftp':'SFTP',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry.ClmgmtDevCredCommandFailCause_Enum' : _MetaInfoEnum('ClmgmtDevCredCommandFailCause_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'none':'NONE',
            'unknownError':'UNKNOWNERROR',
            'transferProtocolNotSupported':'TRANSFERPROTOCOLNOTSUPPORTED',
            'fileServerNotReachable':'FILESERVERNOTREACHABLE',
            'unrecognizedEntPhysicalIndex':'UNRECOGNIZEDENTPHYSICALINDEX',
            'invalidFile':'INVALIDFILE',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry.ClmgmtDevCredCommand_Enum' : _MetaInfoEnum('ClmgmtDevCredCommand_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'noOp':'NOOP',
            'getDeviceCredentials':'GETDEVICECREDENTIALS',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry',
            False, 
            [
            _MetaInfoClassMember('clmgmtDevCredExportActionIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object uniquely identifies a row in
                clmgmtDevCredExportActionTable. The management application
                chooses this value by reading
                clmgmtNextFreeDevCredExportActionIndex while creating an
                entry in this table. If an entry already exists with this
                index, the creation of the entry will not continue and
                error will be returned. The management application should
                read the value of clmgmtNextFreeDevCredExportActionIndex
                again and retry with the new value for this object.
                ''',
                'clmgmtdevcredexportactionindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtDevCredCommand', REFERENCE_ENUM_CLASS, 'ClmgmtDevCredCommand_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry.ClmgmtDevCredCommand_Enum', 
                [], [], 
                '''                This object indicates the the command to be executed.
                
                Command                          Remarks
                -------                          -------
                noOp(1)                         No operation will be
                                                performed.
                
                getDeviceCredentials(2)         Exports device credentials
                ''',
                'clmgmtdevcredcommand',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredCommandFailCause', REFERENCE_ENUM_CLASS, 'ClmgmtDevCredCommandFailCause_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry.ClmgmtDevCredCommandFailCause_Enum', 
                [], [], 
                '''                This object indicates the the reason for device
                credentials export operation failure.
                
                The value of this object is valid only when
                clmgmtDevCredCommandState is failed(6).
                
                none(1)         - action execution has not started yet.
                                  If the action is completed and the 
                                  action is successful, then also
                                  none(1) is returned to indicate that
                                  there are no errors.
                unknownError(2) - reason for failure is unknown,
                                  operation failed, no operation is
                                  performed
                transferProtocolNotSupported(3) - clmgmtDevCredTransferProtocol
                                                  given is not supported.
                fileServerNotReachable(4)       - file server is not reachable.
                unrecognizedEntPhysicalIndex(5) - entPhysicalIndex is not
                                                  valid
                invalidFile(6)  - The target file specified is not valid.
                ''',
                'clmgmtdevcredcommandfailcause',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredCommandState', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseActionState_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseActionState_Enum', 
                [], [], 
                '''                This object indicates the state of the action that is
                executed as a result of setting clmgmtDevCredRowStatus
                to active(1).
                ''',
                'clmgmtdevcredcommandstate',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredEntPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object represents the entPhysicalIndex of the device
                for which the device credentials are being retrieved. This
                object is mainly used in devices where one device is acting
                as a master and rest of the devices as slaves. The master
                device is responsible for SNMP communication with the
                manager. Examples include stackable switches, devices with
                router processor and line cards.
                
                Note: This object need not be set if it is a stand alone
                device
                ''',
                'clmgmtdevcredentphysicalindex',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredExportFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object represents file where device credentials needs
                to be exported to.
                ''',
                'clmgmtdevcredexportfile',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object indicates the the status of this table entry.
                Once the entry status is set to active(1), the associated
                entry cannot be modified until the action completes
                (clmgmtDevCredCommandStatus is set to a value
                other than inProgress(3)). Once the action completes
                the only operation possible after this is to delete
                the row.
                
                clmgmtDevCredExportFile is a mandatory object to be
                set when creating this entry.
                ''',
                'clmgmtdevcredrowstatus',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredServerAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the the ip address of the server
                from which the files must be read or written to if 
                clmgmtDevCredTransferProtocol is not none(1) or local(2).
                
                All bits as 0s or 1s for clmgmtDevCredServerAddress are not
                allowed.
                
                The format of this address depends on the value of the
                clmgmtDevCredServerAddressType object
                ''',
                'clmgmtdevcredserveraddress',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredServerAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object indicates the transport type of the
                address contained in clmgmtDevCredServerAddress object.
                This must be set when clmgmtDevCredTransferProtocol
                is not none(1) or local(2).
                ''',
                'clmgmtdevcredserveraddresstype',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredServerPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 96)], [], 
                '''                This object indicates the password used by ftp, sftp or
                scp for copying a file to/from an ftp/sftp/scp server. 
                This object must be set when the
                clmgmtDevCredTransferProtocol is ftp(4) or scp(7) or
                sftp(8). Reading it returns a zero-length string for 
                security reasons.
                ''',
                'clmgmtdevcredserverpassword',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredServerUsername', ATTRIBUTE, 'str' , None, None, 
                [(0, 96)], [], 
                '''                This object indicates the remote user name for accessing
                files via ftp, rcp, sftp or scp protocols. This object
                must be set when the clmgmtDevCredTransferProtocol is
                ftp(4), rcp(5), scp(7) or sftp(8). If
                clmgmtDevCredTransferProtocol is rcp(5), the remote
                username is sent as the server username in an rcp command
                request sent by the system to a remote rcp server.
                ''',
                'clmgmtdevcredserverusername',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object indicates the storage type for this conceptual
                row. Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'clmgmtdevcredstoragetype',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtDevCredTransferProtocol', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseTransferProtocol_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseTransferProtocol_Enum', 
                [], [], 
                '''                This object indicates the transfer protocol to be used when
                copying files as specified in the following objects.
                1. clmgmtDevCredExportFile
                .
                ''',
                'clmgmtdevcredtransferprotocol',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtDevCredExportActionEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtDevCredExportActionEntry', REFERENCE_LIST, 'ClmgmtDevCredExportActionEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry', 
                [], [], 
                '''                An entry for each device credential export action that
                is being executed or was executed recently. The management
                application triggers the export by creating an entry in this
                table. This can be done in the following 2 methods
                
                1. CREATE-AND-GO method
                    Management application sets clmgmtDevCredExportActionStatus
                    to createAndGo(4) and all other required objects to valid
                    values in a single SNMP SET request. If all the values
                    are valid, the device creates the entry and executes the
                    action. If the SET request fails, the entry will not be
                    created.
                2. CREATE-AND-WAIT method
                    Management application sets clmgmtDevCredExportActionStatus to
                    createAndWait(5) to create an entry. Management application
                    can set all other required objects to valid
                    values in more than one SNMP SET request. If SET request
                    for any of the objects fails, management application can set
                    just only that object. Once all the required objects
                    are set to valid values, management application triggers action
                    execution by setting clmgmtDevCredExportActionStatus to
                    active(1).
                
                To stop the action from being executed, the management application
                can delete the entry by setting clmgmtDevCredExportActionStatus
                to destroy(6) when clmgmtDevCredCommandState is pending(2).
                
                The status of action execution can be known by querying
                clmgmtDevCredCommandState. If the action is still in
                pending(2) or inProgress(3), the management application need to
                check back again after few seconds. Once the action completes
                and if status of the action is failed(6), the reason for
                failure can be retrieved from clmgmtDevCredCommandFailCause.
                
                Entry can be deleted except when clmgmtLicenseAction is set
                to inProgress(3). All entries in this table are volatile
                and are cleared on agent reset.
                ''',
                'clmgmtdevcredexportactionentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtDevCredExportActionTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable.ClmgmtLicensableFeatureEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable.ClmgmtLicensableFeatureEntry',
            False, 
            [
            _MetaInfoClassMember('clmgmtFeatureIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object uniquely identifies a licensable feature in
                the device.
                ''',
                'clmgmtfeatureindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtFeatureEndDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the license end date of the feature.
                This object is applicable if at least one of the licenses used
                for this feature has a valid end date. The end date will
                be the latest of the valid end dates of all the licenses
                used for this feature. If none of the licenses used for this
                feature have a valid end date then this object will contain an
                octet string of length 0.
                ''',
                'clmgmtfeatureenddate',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtFeatureName', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object indicates the name of the licensable feature
                in the device. Examples of feature names are: 'IPBASE',
                'ADVIPSERVICE'
                ''',
                'clmgmtfeaturename',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtFeaturePeriodUsed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the license period used for the feature.
                ''',
                'clmgmtfeatureperiodused',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtFeatureStartDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the license start date of the feature.
                This object is applicable if at least one of the licenses used
                for this feature has a valid start date. The start date will
                be the earliest of the valid start dates of all the licenses
                used for this feature. If none of the licenses used for this
                feature have a valid start date then this object will contain an
                octet string of length 0.
                ''',
                'clmgmtfeaturestartdate',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtFeatureValidityPeriodRemaining', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the time period remaining before
                the feature's license expires or transitions. This object is
                applicable only if clmgmtLicenseType of the license used by
                this feature is demo(1), or extension(2) or gracePeriod(3) or
                evalRightToUse(8).
                
                The object will contain 0 if other types of license is used
                or if the feature does not use any license. If the
                feature is using multiple licenses, this period will
                represent the cumulative period remaining from all the
                licenses used by this feature.
                ''',
                'clmgmtfeaturevalidityperiodremaining',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtFeatureVersion', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This object indicates the version of the licensable
                feature in the device. Examples of feature versions
                are: '1.0' or '2.0'
                ''',
                'clmgmtfeatureversion',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtFeatureWhatIsCounted', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object represents the entity that is being counted
                by this feature. Examples of entities are IP Phones, number
                of sessions etc. This object is only applicable for
                features that use counting licenses. For other features,
                this object will return empty string.
                ''',
                'clmgmtfeaturewhatiscounted',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicensableFeatureEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicensableFeatureEntry', REFERENCE_LIST, 'ClmgmtLicensableFeatureEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable.ClmgmtLicensableFeatureEntry', 
                [], [], 
                '''                An entry in clmgmtLicensableFeatureTable. Each entry represents
                a licensable feature.
                ''',
                'clmgmtlicensablefeatureentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicensableFeatureTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable.ClmgmtLicenseActionResultEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable.ClmgmtLicenseActionResultEntry',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseActionIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'clmgmtlicenseactionindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtLicenseNumber', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates the sequence number of this license
                in the list of licenses on which the action is executed.
                For example, if there are 3 licenses in a license file
                when executing license install action, this object will
                have values 1, 2 and 3 respectively as ordered in the
                license file.
                ''',
                'clmgmtlicensenumber',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtLicenseIndivActionFailCause', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseActionFailCause_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseActionFailCause_Enum', 
                [], [], 
                '''                This object indicates the reason for action failure on this
                individual license
                ''',
                'clmgmtlicenseindivactionfailcause',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseIndivActionState', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseActionState_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseActionState_Enum', 
                [], [], 
                '''                This object indicates the state of action on this
                individual license.
                ''',
                'clmgmtlicenseindivactionstate',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseActionResultEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseActionResultEntry', REFERENCE_LIST, 'ClmgmtLicenseActionResultEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable.ClmgmtLicenseActionResultEntry', 
                [], [], 
                '''                An entry in clmgmtLicenseActionResultTable. Each entry
                contains result of the action for a single license.
                These entries are created immediately after action
                execution when the action involves multiple licenses.
                These entries get automatically deleted when the
                corresponding entry in clmgmtLicenseActionTable
                is deleted.
                ''',
                'clmgmtlicenseactionresultentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseActionResultTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable.ClmgmtLicenseActionEntry.ClmgmtLicenseAction_Enum' : _MetaInfoEnum('ClmgmtLicenseAction_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'noOp':'NOOP',
            'install':'INSTALL',
            'clear':'CLEAR',
            'processPermissionTicket':'PROCESSPERMISSIONTICKET',
            'regenerateLastRehostTicket':'REGENERATELASTREHOSTTICKET',
            'backup':'BACKUP',
            'generateEULA':'GENERATEEULA',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable.ClmgmtLicenseActionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable.ClmgmtLicenseActionEntry',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseActionIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object uniquely identifies a row in
                clmgmtLicenseActionTable. The management application should choose
                this value by reading clmgmtNextFreeLicenseActionIndex
                while creating an entry in this table. If an entry already
                exists with this index, the creation of the entry will not
                continue and error will be returned. The management application
                should read the value of clmgmtNextFreeLicenseActionIndex
                again and retry with the new value for this object.
                ''',
                'clmgmtlicenseactionindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtLicenseAcceptEULA', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the End User License Agreement
                needed for installing the licenses is accepted.
                
                true(1) - EULA is read and accepted
                false(2) - EULA is not accepted
                
                Management application should set this object to true(1) when
                installing licenses that need EULA acceptance.
                ''',
                'clmgmtlicenseaccepteula',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseAction', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseAction_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable.ClmgmtLicenseActionEntry.ClmgmtLicenseAction_Enum', 
                [], [], 
                '''                This object indicates the the command/action to be executed.
                
                Command                        Remarks
                -------                        -------
                noOp(1)                        No operation will be
                                               performed.
                
                install(2)                     Installs the license.
                
                clear(3)                       Clears the license.
                
                processPermissionTicket(4)     Processes thee permission
                                               ticket and generates and
                                               exports rehost ticket.
                
                regenerateLastRehostTicket(5)  Generates and exports the
                                               last generated rehost
                                               ticket.
                
                backup(6)                      Backs up all the licenses
                                               installed currently onto a
                                               backup store.
                
                generateEULA(7)                Checks whether the licenses
                                               in the license file need EULA
                                               acceptance and uploads the
                                               needed EULA contents to a file.
                ''',
                'clmgmtlicenseaction',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionEntPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object represents the entPhysicalIndex of the device
                where the action is being executed. This object is mainly
                used in devices where one device is acting as a master and
                rest of the devices as slaves. The master device is
                responsible for SNMP communication with the management
                application. Examples include stackable switches, devices
                with route processor and line card configuration. If this
                object is not set, the license action will be executed on
                the master device. Note: This object need not be set if
                there is a stand alone device
                ''',
                'clmgmtlicenseactionentphysicalindex',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionFailCause', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseActionFailCause_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseActionFailCause_Enum', 
                [], [], 
                '''                This object indicates the reason for this license action
                failure. The value of this object is valid only when
                clmgmtLicenseActionState is failed(6).
                ''',
                'clmgmtlicenseactionfailcause',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionLicenseIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the the license index of the license
                that is the subject of this action. This is used for
                identifying a license for performing actions specific to
                that license. This object need to be set only if
                clmgmtLicenseAction is set to clear(4). The value of this
                object is same as the clmgmtLicenseIndex object in
                clmgmtLicenseInfoEntry for license that is subject of this
                action.
                ''',
                'clmgmtlicenseactionlicenseindex',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object indicates the the status of this table entry.
                Once the entry status is set to active(1), the associated
                entry cannot be modified until the action completes
                (clmgmtLicenseConfigCommandStatus is set to a value
                other than inProgress(3)). Once the action completes
                the only operation possible after this is to delete
                the row. It is recommended that the management application
                should delete entries in this table after reading
                the result. In order to prevent old entries from
                clogging the table, entries will be aged out, but an
                entry will never be deleted within 5 minutes of
                completion
                ''',
                'clmgmtlicenseactionrowstatus',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionState', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseActionState_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseActionState_Enum', 
                [], [], 
                '''                This object indicates the state of this license action.
                ''',
                'clmgmtlicenseactionstate',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object indicates the storage type for this conceptual
                row. Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'clmgmtlicenseactionstoragetype',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionTransferProtocol', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseTransferProtocol_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'ClmgmtLicenseTransferProtocol_Enum', 
                [], [], 
                '''                This object represents the transfer protocol to be used
                when copying files as specified in the following objects.
                1. clmgmtLicenseFile
                2. clmgmtLicensePermissionTicketFile
                3. clmgmtLicenseRehostTicketFile
                4. clmgmtLicenseBackupFile
                
                Note: This object need not be set if the all the files
                required for the action are in device's local file system.
                ''',
                'clmgmtlicenseactiontransferprotocol',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseBackupFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the file where all the licenses in
                the device need to be backed up. This object need to be set
                only if clmgmtLicenseAction is set to backup(6) and the
                management application must set the value of this  object
                to valid value before invoking action.
                ''',
                'clmgmtlicensebackupfile',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseEULAFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the file where all the End User License
                Agreements (EULAs) need to be exported to. This object need to
                be set only if clmgmtLicenseAction is set to generateEULA(7) and
                the management application must set the value of this object to
                valid value before invoking action.
                ''',
                'clmgmtlicenseeulafile',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object represents the location of the license file
                on the server identified by clmgmtLicenseServerAddress. This
                object MUST be set to a valid value before or concurrently
                with setting the value of the clmgmtLicenseAction object to
                install(2). For other operations, the value of this
                object is not considered, it is irrelevant.
                ''',
                'clmgmtlicensefile',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseJobQPosition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the position of the action
                in the license action job queue that is maintained
                internally. Only actions in pending(2) state will
                be put in the queue until they are executed. By
                reading this object, the management application can make
                intelligent decision on whether to execute another
                action that it is planning on. For example, if there
                is already a license clear action in the queue in
                pending(2) state, management application can choose to
                defer its license back up action to a later time. This
                object will return a value of 0 if the action is not in
                pending(2) state.
                ''',
                'clmgmtlicensejobqposition',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicensePermissionTicketFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the file name of the permission
                ticket. This object need to be set only if
                clmgmtLicenseAction is set to processPermissionTicket(4)
                or regenerateLastRehostTicket(5) actions. The permission
                ticket is obtained from Cisco licensing portal to revoke
                a license. The management application must set this object
                to valid value before invoking the action.
                ''',
                'clmgmtlicensepermissionticketfile',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseRehostTicketFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the file where the rehost ticket
                generated by the device need to be exported to. The rehost
                ticket is generated as a result of processPermissionTicket
                and regenerateLastRehostTicket actions. After generating
                the rehost ticket, the device exports the rehost ticket
                contents to this file. This object need to be set only
                if clmgmtLicenseAction is set to processPermissionTicket(4)
                or regenerateLastRehostTicket(5) actions.
                ''',
                'clmgmtlicenserehostticketfile',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseServerAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the ip address of the server from
                which the files must be read or written to if
                clmgmtLicenseActionTransferProtocol is not none(1) or
                local(2).
                
                All bits as 0s or 1s for clmgmtLicenseServerAddress are not
                allowed.
                
                The format of this address depends on the value of the
                clmgmtLicenseServerAddressType object
                ''',
                'clmgmtlicenseserveraddress',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseServerAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object indicates the transport type of the
                address contained in clmgmtLicenseServerAddress object.
                This must be set when clmgmtLicenseActionTransferProtocol
                is not none(1) or local(2).
                ''',
                'clmgmtlicenseserveraddresstype',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseServerPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 96)], [], 
                '''                This object indicates the password used by ftp, sftp or
                scp for copying a file to/from an ftp/sftp/scp server.
                This object must be set when the
                clmgmtLicenseActionTransferProtocol is ftp(4) or scp(7)
                or sftp(8). Reading it returns a zero-length string for
                security reasons.
                ''',
                'clmgmtlicenseserverpassword',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseServerUsername', ATTRIBUTE, 'str' , None, None, 
                [(0, 96)], [], 
                '''                This object indicates the remote user name for accessing
                files via ftp, rcp, sftp or scp protocols. This object must
                be set when the clmgmtLicenseActionTransferProtocol is
                ftp(4), rcp(5), scp(7) or sftp(8). If
                clmgmtLicenseActionTransferProtocol is rcp(5), the remote
                username is sent as the server username in an rcp command
                request sent by the system to a remote rcp server.
                ''',
                'clmgmtlicenseserverusername',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStopOnFailure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the license action should
                stop if the action on a license fails. This object is
                applicable only if there are more than one licenses
                involved in an action.
                ''',
                'clmgmtlicensestoponfailure',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStore', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the clmgmtLicenseStoreIndex of the
                license store to use within the device. The license store
                can be a local disk or flash. A device can have more than
                one license stores. If this object is not set, the license
                will be stored in the default license store as exposed by
                clmgmtDefaultLicenseStore object.
                ''',
                'clmgmtlicensestore',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseActionEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseActionEntry', REFERENCE_LIST, 'ClmgmtLicenseActionEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable.ClmgmtLicenseActionEntry', 
                [], [], 
                '''                An entry for each action that is being executed or was
                executed recently. The management application executes an
                action
                by creating this entry. This can be done in the following
                2 methods
                
                1. CREATE-AND-GO method
                    Management application sets clmgmtLicenseActionRowStatus to
                    createAndGo(4) and all other required objects to valid
                    values in a single SNMP SET request. If all the values
                    are valid, the device creates the entry and executes the
                    action. If the SET request fails, the entry will not be
                    created.
                2. CREATE-AND-WAIT method
                    Management application sets clmgmtLicenseActionRowStatus to
                    createAndWait(5) to create an entry. Management application
                    can set all other required objects to valid
                    values in more than one SNMP SET request. If SET request
                    for any of the objects fails, management application can
                set
                    just only that object. Once all the required objects
                    are set to valid values, management application triggers
                action
                    execution by setting clmgmtLicenseActionRowStatus to
                    active(1).
                
                To stop the action from being executed, the management
                application
                can delete the entry by setting clmgmtLicenseActionRowStatus
                to destroy(6) when clmgmtLicenseActionState is pending(2).
                
                The status of action execution can be known by querying
                clmgmtLicenseActionState. If the action is still in
                pending(2) or in inProgress(3) state, the management
                application need to check back again after few seconds.
                Once the action completes and status of the action is
                failed(6), the reason for failure can be retrieved
                from clmgmtLicenseActionFailCause. If the status of the
                action is partiallySuccessful(5), results of individual
                licenses can be queried from clmgmtLicenseActionResultTable.
                
                Not all objects in the entry are needed to execute every
                action. Below is the list of actions and the required
                objects that are needed to be set for executing that
                action.
                
                1. Installing a license
                   The following MIB objects need to be set for installing a
                   license
                     a. clmgmtLicenseActionTransferProtocol
                     b. clmgmtLicenseServerAddressType
                     c. clmgmtLicenseServerAddress
                     d. clmgmtLicenseServerUsername
                     e. clmgmtLicenseServerPassword
                     f. clmgmtLicenseFile
                     g. clmgmtLicenseStore
                     h. clmgmtLicenseStopOnFailure
                     i. clmgmtLicenseAcceptEULA
                     j. clmgmtLicenseAction
                
                   clmgmtLicenseActionEntPhysicalIndex need not be set
                   explicitly for license installs. License itself identifes
                   the device where the license needs to be installed.
                
                   clmgmtLicenseStore need to be set to store the licenses
                   in a non-default license store. But, if a license file
                   has more than one license and licenses need to be
                   installed on multiple devices (for example to multiple
                   members with in a stack), then value of clmgmtLicenseStore
                   is ignored and the licenses will be installed in default
                   license stores of the respective devices.
                
                2. Clearing a license
                   The following MIB objects need to be set for clearing a
                   license
                     a. clmgmtLicenseActionEntPhysicalIndex
                     b. clmgmtLicenseActionLicenseIndex
                     c. clmgmtLicenseStore
                     d. clmgmtLicenseAction
                
                3. Revoking a license
                   The following MIB objects need to be set for revoking a
                   license
                     a. clmgmtLicenseActionTransferProtocol
                     b. clmgmtLicenseServerAddressType
                     c. clmgmtLicenseServerAddress
                     d. clmgmtLicenseServerUsername
                     e. clmgmtLicenseServerPassword
                     f. clmgmtLicensePermissionTicketFile
                     g. clmgmtLicenseRehostTicketFile
                     h. clmgmtLicenseStopOnFailure
                     i. clmgmtLicenseAction
                
                4. Regenerate last rehost ticket
                   The following MIB objects need to be set for regenerating
                   last rehost ticket
                     a. clmgmtLicenseActionTransferProtocol
                     b. clmgmtLicenseServerAddressType
                     c. clmgmtLicenseServerAddress
                     d. clmgmtLicenseServerUsername
                     e. clmgmtLicenseServerPassword
                     f. clmgmtLicensePermissionTicketFile
                     g. clmgmtLicenseRehostTicketFile
                     h. clmgmtLicenseStopOnFailure
                     i. clmgmtLicenseAction
                
                
                5. Save all licenses to a backup storage
                   The following MIB objects need to be set for storing all
                   licenses to a backup store
                     a. clmgmtLicenseActionEntPhysicalIndex
                     b. clmgmtLicenseActionTransferProtocol
                     c. clmgmtLicenseServerAddressType
                     d. clmgmtLicenseServerAddress
                     e. clmgmtLicenseServerUsername
                     f. clmgmtLicenseServerPassword
                     g. clmgmtLicenseBackupFile
                     h. clmgmtLicenseAction
                
                6. Generate and export EULA if the licenses need EULA to be
                   accepted for installing.
                   The following MIB objects need to be set exporting required
                   EULAs
                     a. clmgmtLicenseActionTransferProtocol
                     b. clmgmtLicenseServerAddressType
                     c. clmgmtLicenseServerAddress
                     d. clmgmtLicenseServerUsername
                     e. clmgmtLicenseServerPassword
                     f. clmgmtLicenseFile
                     g. clmgmtLicenseEULAFile
                     h. clmgmtLicenseAction
                
                For any action, if clmgmtLicenseActionTransferProtocol
                is set to local(2), the following objects need not be set.
                     a. clmgmtLicenseServerAddressType
                     b. clmgmtLicenseServerAddress
                     c. clmgmtLicenseServerUsername
                     d. clmgmtLicenseServerPassword
                
                Entry can be deleted except when clmgmtLicenseAction is set
                to pending(2). All entries are volatile and are cleared
                on agent reset.
                ''',
                'clmgmtlicenseactionentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseActionTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseConfiguration' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseConfiguration',
            False, 
            [
            _MetaInfoClassMember('clmgmtNextFreeLicenseActionIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object contains appropriate value for
                clmgmtLicenseActionIndex that can be used to create
                an entry in clmgmtLicenseActionTable. The management application
                should read this object first and then use this as the
                value for clmgmtLicenseActionIndex to avoid collisions
                when creating entries in clmgmtLicenseActionTable.
                Following this approach does not guarantee collision free
                row creation, but will reduce the probability. The
                collision will happen if two management applications read this
                object at the same time and attempt to create an entry
                with this value at the same time. In this case, the
                management application whose request is processed after the first
                request will get an error and the process of reading this object
                and entry creation needs to be repeated.
                ''',
                'clmgmtnextfreelicenseactionindex',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseConfiguration',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable.ClmgmtLicenseDeviceInfoEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable.ClmgmtLicenseDeviceInfoEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtDefaultLicenseStore', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates the clmgmtLicenseStoreIndex of
                default store in the device. There will be only one
                default license store per device. If no license store
                is specified during license install, this default license
                store will be used.
                ''',
                'clmgmtdefaultlicensestore',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseDeviceInfoEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseDeviceInfoEntry', REFERENCE_LIST, 'ClmgmtLicenseDeviceInfoEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable.ClmgmtLicenseDeviceInfoEntry', 
                [], [], 
                '''                An entry in clmgmtLicenseDeviceInfoTable. Each entry
                contains device level licensing information for a device.
                ''',
                'clmgmtlicensedeviceinfoentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseDeviceInfoTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInformation' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInformation',
            False, 
            [
            _MetaInfoClassMember('clmgmtNextFreeDevCredExportActionIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object contains appropriate value for
                clmgmtDevCredExportActionIndex that can be used to create
                an entry in clmgmtDevCredExportActionTable. The management
                application should read this object first and then use this
                as the value for clmgmtDevCredExportActionIndex to avoid
                collisions when creating entries in
                clmgmtDevCredExportActionTable. Following this approach does
                not guarantee collision free row creation, but will reduce
                the probability. The collision will happen if two
                management applications read this object at the same time and
                attempt to create an entry with this value at the same time.
                In this case, the management application whose request is
                processed after the first request will get an error and the
                process of reading this object and entry creation needs to be
                repeated.
                ''',
                'clmgmtnextfreedevcredexportactionindex',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseDeviceInformation',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry.ClmgmtLicenseStatus_Enum' : _MetaInfoEnum('ClmgmtLicenseStatus_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'inactive':'INACTIVE',
            'notInUse':'NOTINUSE',
            'inUse':'INUSE',
            'expiredInUse':'EXPIREDINUSE',
            'expiredNotInUse':'EXPIREDNOTINUSE',
            'usageCountConsumed':'USAGECOUNTCONSUMED',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry.ClmgmtLicenseType_Enum' : _MetaInfoEnum('ClmgmtLicenseType_Enum', 'ydk.models.license.CISCO_LICENSE_MGMT_MIB',
        {
            'demo':'DEMO',
            'extension':'EXTENSION',
            'gracePeriod':'GRACEPERIOD',
            'permanent':'PERMANENT',
            'paidSubscription':'PAIDSUBSCRIPTION',
            'evaluationSubscription':'EVALUATIONSUBSCRIPTION',
            'extensionSubscription':'EXTENSIONSUBSCRIPTION',
            'evalRightToUse':'EVALRIGHTTOUSE',
            'rightToUse':'RIGHTTOUSE',
            'permanentRightToUse':'PERMANENTRIGHTTOUSE',
        }, 'CISCO-LICENSE-MGMT-MIB', _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB']),
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object uniquely identifies a license within
                the device.
                ''',
                'clmgmtlicenseindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtLicenseStoreUsed', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object represents the license store that is used for
                storing this license. This object will have the same value
                as clmgmtLicenseStoreIndex in clmgmtLicenseStoreInfoEntry
                of the license store used.
                ''',
                'clmgmtlicensestoreused',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtLicenseComments', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object represents the user modifiable comments
                about the license. This object is initially populated
                with comments from the license file.
                ''',
                'clmgmtlicensecomments',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseCounted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the license is counted
                license.
                true(1)  - counted license
                false(2) - uncounted license
                ''',
                'clmgmtlicensecounted',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseEndDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the end date for a subscription license.
                This object is applicable only when clmgmtLicenseType is
                paidSubscription(5), evaluationSubscription(6) or
                extensionSubscription (7). The object will contain an octet
                string of length 0 when it is not applicable.
                ''',
                'clmgmtlicenseenddate',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseEULAStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the user accepted
                End User License Agreement for this license.
                
                true(1)  - EULA accpeted
                false(2) - EULA not accepted
                ''',
                'clmgmtlicenseeulastatus',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseExpiredPeriod', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the elapsed time period since the license
                expired. This object is applicable only if clmgmtLicenseType
                is demo(1), or extension(2) or gracePeriod(3). Also, this
                value of this object will be valid only after the license
                expires. The object will return 0 for other license types
                or before the license expiry.
                ''',
                'clmgmtlicenseexpiredperiod',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseFeatureName', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object indicates the name of the feature that is
                using or can use this license. A license can be used by
                only one feature. Examples of feature name are: 'IPBASE',
                'ADVIPSERVICE'.
                ''',
                'clmgmtlicensefeaturename',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseFeatureVersion', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object indicates the version of the feature that is
                using or can use this license. Examples of feature version
                are: '1.0', '2.0'
                ''',
                'clmgmtlicensefeatureversion',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseMaxUsageCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the maximum number of entities that
                can use this license. This object is applicable only if
                clmgmtLicenseCounted is true(1). The entity that is being
                counted can be anything and it depends on the licensable
                feature.
                ''',
                'clmgmtlicensemaxusagecount',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicensePeriodUsed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the time period used for the
                Right to use (RTU) licenses. This object is applicable for all
                RTU licenses.
                ''',
                'clmgmtlicenseperiodused',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStartDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the start date for a subscription
                license. It is optional for subscription linceses to have a
                start date associated with them, they may only have an end
                date associated with them. This object may be applicable only
                when clmgmtLicenseType is paidSubscription(5),
                evaluationSubscription(6) or extensionSubscription (7).      
                The object will contain an octet string of length 0 when it is
                not applicable.
                ''',
                'clmgmtlicensestartdate',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStatus', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseStatus_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry.ClmgmtLicenseStatus_Enum', 
                [], [], 
                '''                This object represents status of the license.
                
                inactive(1)           - license is installed, but
                                        not active.
                notInUse(2)           - license is installed and
                                        available for use.
                inUse(3)              - the license is being used (by
                                        a feature).
                expiredInUse(4)       - license is expired but still
                                        being held by the feature.
                expiredNotInUse(5)    - license is expired and not being
                                        held by any feature.
                usageCountConsumed(6) - number of entities using this
                                        licenses has reached the allowed
                                        limit, no new entities are allowed
                                        to use this license.
                ''',
                'clmgmtlicensestatus',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseType', REFERENCE_ENUM_CLASS, 'ClmgmtLicenseType_Enum' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry.ClmgmtLicenseType_Enum', 
                [], [], 
                '''                This object identifies type of license. Licenses may have
                validity period defined in terms of time duration that the
                license is valid for or it may be defined in terms of actual
                calendar dates. Subscription licenses are licenses that have
                validity period defined in terms of calendar dates.
                
                demo(1)               - demo(evaluation license) license.
                extension(2)          - Extension(expiring) license.
                gracePeriod(3)        - Grace period license.
                permanent(4)          - permanent license, the license has no
                                        expiry date.
                paidSubscription(5)   - Paid subscription licenses are the
                licenses
                                        which are purchased by customers. These
                                        licenses have a start date  and end date
                                        associated with them.
                evaluationSubscription(6)-Evaluation subscription licenses are
                                          the trial licenses. These licenses
                                          are node locked and it can be obtained
                                          only once for an UDI. They are valid
                                          based on calendar days. These licenses
                                          have a start date and an end date
                                          associated with them and are issued
                                          once per UDI.
                extensionSubscription(7)- Extension subscription licenses are
                                          similar to evaluation subscription
                                          licenses but these licenses are issued
                                          based on customer request. There are
                                          no restrictions on the number of
                                          licenses available for a UDI.
                evalRightToUse(8)       - Evaluation Right to use (RTU)
                license.
                rightToUse(9)           - Right to use (RTU) license.
                permanentRightToUse(10) ? Right To Use license right after it is configured 
                                          and is valid for the lifetime of the product. 
                                          This is a Right To Use license which is not in 
                                          evaluation mode for a limited time.
                ''',
                'clmgmtlicensetype',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseUsageCountRemaining', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the number of entities that can
                still use this license. This object is applicable only
                if clmgmtLicenseCounted is true(1).
                ''',
                'clmgmtlicenseusagecountremaining',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseValidityPeriod', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the time period the license is valid for.
                This object is applicable only if clmgmtLicenseType is demo(1),
                or extension(2) or gracePeriod(3) or evalRightToUse(8). The
                object will return 0 for other license types.
                ''',
                'clmgmtlicensevalidityperiod',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseValidityPeriodRemaining', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the time period remaining before the
                license expires or transitions to rightToUse(9) license. This
                object is applicable only if clmgmtLicenseType is demo(1), or
                extension(2) or gracePeriod(3) or evalRightToUse(8). The object
                will contain 0 for other license types.
                ''',
                'clmgmtlicensevalidityperiodremaining',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseInfoEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseInfoEntry', REFERENCE_LIST, 'ClmgmtLicenseInfoEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry', 
                [], [], 
                '''                An entry in clmgmtLicenseInfoTable. Each entry contains
                information about a license installed on the device. This
                entry gets created when a license is installed successfully.
                Management application can not create these entries directly, but
                will do so indirectly by executing license install action.
                Some of these entries may already exist that correspond to
                demo licenses even before management application installs any
                licenses.
                ''',
                'clmgmtlicenseinfoentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseInfoTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseNotifObjects' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseNotifObjects',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseDeploymentNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the device should generate
                notifications related to license deployment. This object
                enables/disables sending following notifications:
                    clmgmtLicenseInstalled
                    clmgmtLicenseCleared
                    clmgmtLicenseRevoked
                    clmgmtLicenseEULAAccepted
                ''',
                'clmgmtlicensedeploymentnotifenable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseErrorNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the device should generate
                notifications related to error conditions in enforcing
                licensing. This object enables/disables sending following
                notifications:
                    clmgmtLicenseNotEnforced
                ''',
                'clmgmtlicenseerrornotifenable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseUsageNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the device should generate
                the notifications related to usage of licenses. This object
                enables/disables sending following notifications:
                    clmgmtLicenseExpired 
                    clmgmtLicenseExpiryWarning
                    clmgmtLicenseUsageCountExceeded
                    clmgmtLicenseUsageCountAboutToExceed
                    clmgmtLicenseSubscriptionExpiryWarning
                    clmgmtLicenseSubscriptionExtExpiryWarning
                    clmgmtLicenseSubscriptionExpired
                    clmgmtLicenseEvalRTUTransitionWarning
                    clmgmtLicenseEvalRTUTransition
                ''',
                'clmgmtlicenseusagenotifenable',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseNotifObjects',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable.ClmgmtLicenseStoreInfoEntry' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable.ClmgmtLicenseStoreInfoEntry',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseStoreIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object uniquely identifies a license store within
                the device.
                ''',
                'clmgmtlicensestoreindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-LICENSE-MGMT-MIB', True),
            _MetaInfoClassMember('clmgmtLicenseStoreName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the name of the license store
                within the device. It is a file in device's local file
                system i.e., either on a local disk or flash or some
                other storage media. For example, the value of this
                object can be 'disk1:lic_store_1.txt' or
                'flash:lic_store_2.txt
                ''',
                'clmgmtlicensestorename',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStoreSizeRemaining', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the number of bytes still remaining
                to be used for new license installations in the license
                store.
                ''',
                'clmgmtlicensestoresizeremaining',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStoreTotalSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the total number of bytes that are
                allocated to the license store.
                ''',
                'clmgmtlicensestoretotalsize',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseStoreInfoEntry',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable',
            False, 
            [
            _MetaInfoClassMember('clmgmtLicenseStoreInfoEntry', REFERENCE_LIST, 'ClmgmtLicenseStoreInfoEntry' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable.ClmgmtLicenseStoreInfoEntry', 
                [], [], 
                '''                An entry in clmgmtLicenseStoreInfoTable. Each entry
                contains information about a license store allocated
                on the device
                ''',
                'clmgmtlicensestoreinfoentry',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'clmgmtLicenseStoreInfoTable',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
    'CISCOLICENSEMGMTMIB' : {
        'meta_info' : _MetaInfoClass('CISCOLICENSEMGMTMIB',
            False, 
            [
            _MetaInfoClassMember('clmgmtDevCredExportActionTable', REFERENCE_CLASS, 'ClmgmtDevCredExportActionTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable', 
                [], [], 
                '''                A table for triggering device credentials export action.
                Management application must create this entry to trigger the
                export of device credentials from the device to a file.
                
                Once the request completes, the management application should
                retrieve the values of the objects of interest, and then
                delete the entry.  In order to prevent old entries from
                clogging the table, entries will be aged out, but an entry
                will never be deleted within 5 minutes of completion.
                ''',
                'clmgmtdevcredexportactiontable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicensableFeatureTable', REFERENCE_CLASS, 'ClmgmtLicensableFeatureTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable', 
                [], [], 
                '''                This table contains list of licensable features in the
                image. All the licensable features will have an entry each
                in this table irrespective of whether they are using any
                licenses currently. Entries in this table are created by
                the agent one for each licensable feature in the image.
                These entries remain in the table permanently and can not
                be deleted. Management application can not create or delete
                entries from this table.
                ''',
                'clmgmtlicensablefeaturetable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionResultTable', REFERENCE_CLASS, 'ClmgmtLicenseActionResultTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable', 
                [], [], 
                '''                This table contains results of license action if the
                license action involves multiple licenses. Entries in this
                table are not created for actions where there is
                only license that is subject of the action. For
                example, if there are 3 licenses in a license file
                when executing license install action, 3 entries will
                be created in this table, one for each license.
                ''',
                'clmgmtlicenseactionresulttable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseActionTable', REFERENCE_CLASS, 'ClmgmtLicenseActionTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable', 
                [], [], 
                '''                A table for invoking license management actions. Management
                application must create a row in this table to trigger any of
                the license management actions. The following are different
                actions that can be executed using this table.
                    1. install
                    2. clear
                    3. processPermissionTicket
                    4. regenerateLastRehostTicket
                    5. backup
                    6. generateEULA
                
                Refer to the description of clmgmtLicenseAction for more
                information on what these actions do on the device.
                Once the request completes, the management application should
                retrieve the values of the objects of interest, and then
                delete the entry.  In order to prevent old entries from
                clogging the table, entries will be aged out, but an entry
                will never be deleted within 5 minutes of completion.
                ''',
                'clmgmtlicenseactiontable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseConfiguration', REFERENCE_CLASS, 'ClmgmtLicenseConfiguration' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseConfiguration', 
                [], [], 
                '''                ''',
                'clmgmtlicenseconfiguration',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseDeviceInformation', REFERENCE_CLASS, 'ClmgmtLicenseDeviceInformation' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInformation', 
                [], [], 
                '''                ''',
                'clmgmtlicensedeviceinformation',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseDeviceInfoTable', REFERENCE_CLASS, 'ClmgmtLicenseDeviceInfoTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable', 
                [], [], 
                '''                This table contains objects that provide licensing related
                information at the device level. Entries will exist
                only for entities that support licensing. For example,
                if it is a stand alone device and supports licensing,
                then there will be only one entry in this table. If
                it is stackable switch then there will be multiple
                entries with one entry for each device in the stack.
                ''',
                'clmgmtlicensedeviceinfotable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseInfoTable', REFERENCE_CLASS, 'ClmgmtLicenseInfoTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable', 
                [], [], 
                '''                This table contains information about all the licenses
                installed on the device.
                ''',
                'clmgmtlicenseinfotable',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseNotifObjects', REFERENCE_CLASS, 'ClmgmtLicenseNotifObjects' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseNotifObjects', 
                [], [], 
                '''                ''',
                'clmgmtlicensenotifobjects',
                'CISCO-LICENSE-MGMT-MIB', False),
            _MetaInfoClassMember('clmgmtLicenseStoreInfoTable', REFERENCE_CLASS, 'ClmgmtLicenseStoreInfoTable' , 'ydk.models.license.CISCO_LICENSE_MGMT_MIB', 'CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable', 
                [], [], 
                '''                This table contains information about all the license
                stores allocated on the device.
                ''',
                'clmgmtlicensestoreinfotable',
                'CISCO-LICENSE-MGMT-MIB', False),
            ],
            'CISCO-LICENSE-MGMT-MIB',
            'CISCO-LICENSE-MGMT-MIB',
            _yang_ns._namespaces['CISCO-LICENSE-MGMT-MIB'],
        'ydk.models.license.CISCO_LICENSE_MGMT_MIB'
        ),
    },
}
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable.ClmgmtDevCredExportActionEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable.ClmgmtLicensableFeatureEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable.ClmgmtLicenseActionResultEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable.ClmgmtLicenseActionEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable.ClmgmtLicenseDeviceInfoEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable.ClmgmtLicenseInfoEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable.ClmgmtLicenseStoreInfoEntry']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtDevCredExportActionTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicensableFeatureTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseActionResultTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseActionTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseConfiguration']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInfoTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseDeviceInformation']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseInfoTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseNotifObjects']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
_meta_table['CISCOLICENSEMGMTMIB.ClmgmtLicenseStoreInfoTable']['meta_info'].parent =_meta_table['CISCOLICENSEMGMTMIB']['meta_info']
