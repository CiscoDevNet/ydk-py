


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOFTPCLIENTMIB.CfcRequest' : {
        'meta_info' : _MetaInfoClass('CISCOFTPCLIENTMIB.CfcRequest',
            False, 
            [
            _MetaInfoClassMember('cfcRequestMaximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum number of requests this system can hold in
                cfcRequestTable.  A value of 0 indicates no configured limit.
                
                This object may be read-only on some systems.
                
                When an attempt is made to create a new entry but the table
                is full, the oldest completed entry is bumped out and
                cfcRequestsBumped is incremented.
                
                Changing this number does not disturb existing requests that
                are not completed and bumps completed requests as necessary.
                ''',
                'cfcrequestmaximum',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of requests in cfcRequestTable.
                ''',
                'cfcrequests',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestsBumped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of requests in cfcRequestTable that were bumped
                out to make room for a new request.
                ''',
                'cfcrequestsbumped',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestsHigh', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The highest number of requests in cfcRequestTable since this
                system was last initialized.
                ''',
                'cfcrequestshigh',
                'CISCO-FTP-CLIENT-MIB', False),
            ],
            'CISCO-FTP-CLIENT-MIB',
            'cfcRequest',
            _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB'],
        'ydk.models.ftp.CISCO_FTP_CLIENT_MIB'
        ),
    },
    'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperationState_Enum' : _MetaInfoEnum('CfcRequestOperationState_Enum', 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB',
        {
            'running':'RUNNING',
            'stopping':'STOPPING',
            'stopped':'STOPPED',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperation_Enum' : _MetaInfoEnum('CfcRequestOperation_Enum', 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB',
        {
            'putBinary':'PUTBINARY',
            'putASCII':'PUTASCII',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestResult_Enum' : _MetaInfoEnum('CfcRequestResult_Enum', 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB',
        {
            'pending':'PENDING',
            'success':'SUCCESS',
            'aborted':'ABORTED',
            'fileOpenFailLocal':'FILEOPENFAILLOCAL',
            'fileOpenFailRemote':'FILEOPENFAILREMOTE',
            'badDomainName':'BADDOMAINNAME',
            'unreachableIpAddress':'UNREACHABLEIPADDRESS',
            'linkFailed':'LINKFAILED',
            'fileReadFailed':'FILEREADFAILED',
            'fileWriteFailed':'FILEWRITEFAILED',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestStop_Enum' : _MetaInfoEnum('CfcRequestStop_Enum', 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB',
        {
            'ready':'READY',
            'stop':'STOP',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry',
            False, 
            [
            _MetaInfoClassMember('cfcRequestIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An arbitrary integer to uniquely identify this entry.  To
                create an entry a management application should pick a
                random number.
                ''',
                'cfcrequestindex',
                'CISCO-FTP-CLIENT-MIB', True),
            _MetaInfoClassMember('cfcRequestCompletionTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the operation completed.  For
                an incomplete operation this value is zero.
                ''',
                'cfcrequestcompletiontime',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestEntryStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The control that allows modification, creation, and deletion
                of entries.  For detailed rules see the DESCRIPTION for
                cfcRequestEntry.
                ''',
                'cfcrequestentrystatus',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestLocalFile', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The local file on which the operation is to be performed.
                ''',
                'cfcrequestlocalfile',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestOperation', REFERENCE_ENUM_CLASS, 'CfcRequestOperation_Enum' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperation_Enum', 
                [], [], 
                '''                The FTP operation to be performed.
                ''',
                'cfcrequestoperation',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestOperationState', REFERENCE_ENUM_CLASS, 'CfcRequestOperationState_Enum' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperationState_Enum', 
                [], [], 
                '''                The operational state of the file transfer.  To short-terminate
                the transfer set cfcRequestStop to 'stop'.
                ''',
                'cfcrequestoperationstate',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The password to use at the FTP server.
                
                When read this object always returns a zero-length string.
                ''',
                'cfcrequestpassword',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestRemoteFile', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The remote file on which the operation is to be performed.
                ''',
                'cfcrequestremotefile',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestResult', REFERENCE_ENUM_CLASS, 'CfcRequestResult_Enum' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestResult_Enum', 
                [], [], 
                '''                The result of the FTP operation.
                ''',
                'cfcrequestresult',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestServer', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The domain name or IP address of the FTP server to use.
                ''',
                'cfcrequestserver',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestStop', REFERENCE_ENUM_CLASS, 'CfcRequestStop_Enum' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestStop_Enum', 
                [], [], 
                '''                The action control to stop a running request.  Setting this to
                'stop' will begin the process of stopping the request.  Setting
                it to 'ready' or setting it to 'stop' more than once have no
                effect.  When read this object always returns ready.
                ''',
                'cfcrequeststop',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestUser', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The user name to use at the FTP server.
                ''',
                'cfcrequestuser',
                'CISCO-FTP-CLIENT-MIB', False),
            ],
            'CISCO-FTP-CLIENT-MIB',
            'cfcRequestEntry',
            _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB'],
        'ydk.models.ftp.CISCO_FTP_CLIENT_MIB'
        ),
    },
    'CISCOFTPCLIENTMIB.CfcRequestTable' : {
        'meta_info' : _MetaInfoClass('CISCOFTPCLIENTMIB.CfcRequestTable',
            False, 
            [
            _MetaInfoClassMember('cfcRequestEntry', REFERENCE_LIST, 'CfcRequestEntry' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry', 
                [], [], 
                '''                Information about an FTP client request.  Management applications
                use cfcRequestEntryStatus to control entry modification, creation,
                and deletion.
                
                Setting cfcRequestEntryStatus to 'active' from any state including
                'active' causes the operation to be started.
                
                The entry may be modified only when cfcRequestOperationState is
                'stopped'.
                
                The value of cfcRequestEntryStatus may be set to 'destroy' at any
                time.  Doing so will abort a running request.
                
                Entries may not be created without explicitly setting
                cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'.
                ''',
                'cfcrequestentry',
                'CISCO-FTP-CLIENT-MIB', False),
            ],
            'CISCO-FTP-CLIENT-MIB',
            'cfcRequestTable',
            _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB'],
        'ydk.models.ftp.CISCO_FTP_CLIENT_MIB'
        ),
    },
    'CISCOFTPCLIENTMIB' : {
        'meta_info' : _MetaInfoClass('CISCOFTPCLIENTMIB',
            False, 
            [
            _MetaInfoClassMember('cfcRequest', REFERENCE_CLASS, 'CfcRequest' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequest', 
                [], [], 
                '''                ''',
                'cfcrequest',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestTable', REFERENCE_CLASS, 'CfcRequestTable' , 'ydk.models.ftp.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB.CfcRequestTable', 
                [], [], 
                '''                A table of FTP client requests.
                ''',
                'cfcrequesttable',
                'CISCO-FTP-CLIENT-MIB', False),
            ],
            'CISCO-FTP-CLIENT-MIB',
            'CISCO-FTP-CLIENT-MIB',
            _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB'],
        'ydk.models.ftp.CISCO_FTP_CLIENT_MIB'
        ),
    },
}
_meta_table['CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry']['meta_info'].parent =_meta_table['CISCOFTPCLIENTMIB.CfcRequestTable']['meta_info']
_meta_table['CISCOFTPCLIENTMIB.CfcRequest']['meta_info'].parent =_meta_table['CISCOFTPCLIENTMIB']['meta_info']
_meta_table['CISCOFTPCLIENTMIB.CfcRequestTable']['meta_info'].parent =_meta_table['CISCOFTPCLIENTMIB']['meta_info']
