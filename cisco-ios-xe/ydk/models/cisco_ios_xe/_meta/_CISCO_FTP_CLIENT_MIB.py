


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoFtpClientMib.Cfcrequest' : {
        'meta_info' : _MetaInfoClass('CiscoFtpClientMib.Cfcrequest',
            False, 
            [
            _MetaInfoClassMember('cfcRequestMaximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                The current number of requests in cfcRequestTable.
                ''',
                'cfcrequests',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestsBumped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of requests in cfcRequestTable that were bumped
                out to make room for a new request.
                ''',
                'cfcrequestsbumped',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestsHigh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The highest number of requests in cfcRequestTable since this
                system was last initialized.
                ''',
                'cfcrequestshigh',
                'CISCO-FTP-CLIENT-MIB', False),
            ],
            'CISCO-FTP-CLIENT-MIB',
            'cfcRequest',
            _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB'
        ),
    },
    'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationEnum' : _MetaInfoEnum('CfcrequestoperationEnum', 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB',
        {
            'putBinary':'putBinary',
            'putASCII':'putASCII',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationstateEnum' : _MetaInfoEnum('CfcrequestoperationstateEnum', 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB',
        {
            'running':'running',
            'stopping':'stopping',
            'stopped':'stopped',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestresultEnum' : _MetaInfoEnum('CfcrequestresultEnum', 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB',
        {
            'pending':'pending',
            'success':'success',
            'aborted':'aborted',
            'fileOpenFailLocal':'fileOpenFailLocal',
            'fileOpenFailRemote':'fileOpenFailRemote',
            'badDomainName':'badDomainName',
            'unreachableIpAddress':'unreachableIpAddress',
            'linkFailed':'linkFailed',
            'fileReadFailed':'fileReadFailed',
            'fileWriteFailed':'fileWriteFailed',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequeststopEnum' : _MetaInfoEnum('CfcrequeststopEnum', 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB',
        {
            'ready':'ready',
            'stop':'stop',
        }, 'CISCO-FTP-CLIENT-MIB', _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB']),
    'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry' : {
        'meta_info' : _MetaInfoClass('CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry',
            False, 
            [
            _MetaInfoClassMember('cfcRequestIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An arbitrary integer to uniquely identify this entry.  To
                create an entry a management application should pick a
                random number.
                ''',
                'cfcrequestindex',
                'CISCO-FTP-CLIENT-MIB', True),
            _MetaInfoClassMember('cfcRequestCompletionTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the operation completed.  For
                an incomplete operation this value is zero.
                ''',
                'cfcrequestcompletiontime',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
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
            _MetaInfoClassMember('cfcRequestOperation', REFERENCE_ENUM_CLASS, 'CfcrequestoperationEnum' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationEnum', 
                [], [], 
                '''                The FTP operation to be performed.
                ''',
                'cfcrequestoperation',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestOperationState', REFERENCE_ENUM_CLASS, 'CfcrequestoperationstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationstateEnum', 
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
            _MetaInfoClassMember('cfcRequestResult', REFERENCE_ENUM_CLASS, 'CfcrequestresultEnum' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestresultEnum', 
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
            _MetaInfoClassMember('cfcRequestStop', REFERENCE_ENUM_CLASS, 'CfcrequeststopEnum' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequeststopEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB'
        ),
    },
    'CiscoFtpClientMib.Cfcrequesttable' : {
        'meta_info' : _MetaInfoClass('CiscoFtpClientMib.Cfcrequesttable',
            False, 
            [
            _MetaInfoClassMember('cfcRequestEntry', REFERENCE_LIST, 'Cfcrequestentry' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB'
        ),
    },
    'CiscoFtpClientMib' : {
        'meta_info' : _MetaInfoClass('CiscoFtpClientMib',
            False, 
            [
            _MetaInfoClassMember('cfcRequest', REFERENCE_CLASS, 'Cfcrequest' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequest', 
                [], [], 
                '''                ''',
                'cfcrequest',
                'CISCO-FTP-CLIENT-MIB', False),
            _MetaInfoClassMember('cfcRequestTable', REFERENCE_CLASS, 'Cfcrequesttable' , 'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CiscoFtpClientMib.Cfcrequesttable', 
                [], [], 
                '''                A table of FTP client requests.
                ''',
                'cfcrequesttable',
                'CISCO-FTP-CLIENT-MIB', False),
            ],
            'CISCO-FTP-CLIENT-MIB',
            'CISCO-FTP-CLIENT-MIB',
            _yang_ns._namespaces['CISCO-FTP-CLIENT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB'
        ),
    },
}
_meta_table['CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry']['meta_info'].parent =_meta_table['CiscoFtpClientMib.Cfcrequesttable']['meta_info']
_meta_table['CiscoFtpClientMib.Cfcrequest']['meta_info'].parent =_meta_table['CiscoFtpClientMib']['meta_info']
_meta_table['CiscoFtpClientMib.Cfcrequesttable']['meta_info'].parent =_meta_table['CiscoFtpClientMib']['meta_info']
