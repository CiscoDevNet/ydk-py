


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ConfigcopystateEnum' : _MetaInfoEnum('ConfigcopystateEnum', 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB',
        {
            'waiting':'waiting',
            'running':'running',
            'successful':'successful',
            'failed':'failed',
        }, 'CISCO-CONFIG-COPY-MIB', _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB']),
    'ConfigcopyfailcauseEnum' : _MetaInfoEnum('ConfigcopyfailcauseEnum', 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB',
        {
            'unknown':'unknown',
            'badFileName':'badFileName',
            'timeout':'timeout',
            'noMem':'noMem',
            'noConfig':'noConfig',
            'unsupportedProtocol':'unsupportedProtocol',
            'someConfigApplyFailed':'someConfigApplyFailed',
            'systemNotReady':'systemNotReady',
            'requestAborted':'requestAborted',
        }, 'CISCO-CONFIG-COPY-MIB', _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB']),
    'ConfigfiletypeEnum' : _MetaInfoEnum('ConfigfiletypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB',
        {
            'networkFile':'networkFile',
            'iosFile':'iosFile',
            'startupConfig':'startupConfig',
            'runningConfig':'runningConfig',
            'terminal':'terminal',
            'fabricStartupConfig':'fabricStartupConfig',
        }, 'CISCO-CONFIG-COPY-MIB', _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB']),
    'ConfigcopyprotocolEnum' : _MetaInfoEnum('ConfigcopyprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB',
        {
            'tftp':'tftp',
            'ftp':'ftp',
            'rcp':'rcp',
            'scp':'scp',
            'sftp':'sftp',
        }, 'CISCO-CONFIG-COPY-MIB', _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB']),
    'CiscoConfigCopyMib.Cccopytable.Cccopyentry' : {
        'meta_info' : _MetaInfoClass('CiscoConfigCopyMib.Cccopytable.Cccopyentry',
            False, 
            [
            _MetaInfoClassMember('ccCopyIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Object which specifies a unique entry in the
                ccCopyTable.  A management station wishing
                to initiate a config-copy operation should use a
                random value for this object when creating
                or modifying an instance of a ccCopyEntry.
                The RowStatus semantics of the ccCopyEntryRowStatus
                object will prevent access conflicts.
                ''',
                'cccopyindex',
                'CISCO-CONFIG-COPY-MIB', True),
            _MetaInfoClassMember('ccCopyDestFileType', REFERENCE_ENUM_CLASS, 'ConfigfiletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'ConfigfiletypeEnum', 
                [], [], 
                '''                specifies the type of file to copy to. Either the
                ccCopySourceFileType or the ccCopyDestFileType 
                (or both) must be of type 'runningConfig' or 
                'startupConfig'. Also, the ccCopySourceFileType 
                must be different from the ccCopyDestFileType.
                
                If the ccCopyDestFileType has the value of 
                'networkFile', the 
                ccCopyServerAddress/ccCopyServerAddressType and
                ccCopyServerAddressRev1 and ccCopyFileName must
                also be created, and 3 objects together
                (ccCopyDestFileType, ccCopyServerAddressRev1,  
                ccCopyFileName) will uniquely identify the 
                destination file. If ccCopyServerAddress is created
                then ccCopyServerAddressRev1 will store the same IP
                address and ccCopyServerAddressType will take the 
                value 'ipv4'. 
                
                If the ccCopyDestFileType is 'iosFile', the 
                ccCopyFileName must also be created, and the 2
                objects together (ccCopyDestFileType, 
                ccCopyFileName) will uniquely identify the 
                destination file.
                ''',
                'cccopydestfiletype',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyEntryRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry. Once the entry
                status is set to active, the associated entry cannot 
                be modified until the request completes 
                (ccCopyState transitions to 'successful'
                or 'failed' state).
                ''',
                'cccopyentryrowstatus',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyFailCause', REFERENCE_ENUM_CLASS, 'ConfigcopyfailcauseEnum' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'ConfigcopyfailcauseEnum', 
                [], [], 
                '''                The reason why the config-copy operation failed.
                This object is instantiated only when the 
                ccCopyState for this entry is in the 
                'failed' state.
                ''',
                'cccopyfailcause',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyFileName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The file name (including the path, if applicable)
                of the file. This object must be created when either
                the ccCopySourceFileType or ccCopyDestFileType has
                the value 'networkFile' or 'iosFile'.
                ''',
                'cccopyfilename',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyNotificationOnCompletion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a ccCopyCompletion
                notification should be issued on completion of the
                TFTP transfer. If such a notification is desired, 
                it is the responsibility of the management entity to
                ensure that the SNMP administrative model is 
                configured in such a way as to allow the 
                notification to be delivered.
                ''',
                'cccopynotificationoncompletion',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyProtocol', REFERENCE_ENUM_CLASS, 'ConfigcopyprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'ConfigcopyprotocolEnum', 
                [], [], 
                '''                The protocol to be used for any copy.
                
                If the copy operation occurs locally on the SNMP 
                agent (e.g. 'runningConfig' to 'startupConfig'),
                this object may be ignored by the implementation.
                ''',
                'cccopyprotocol',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyServerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the TFTP server from (or to)
                which to copy the configuration file. This object 
                must be created when either the 
                ccCopySourceFileType or ccCopyDestFileType has the
                value 'networkFile'. 
                Values of 0.0.0.0 or FF.FF.FF.FF for
                ccCopyServerAddress are not allowed.
                
                Since this object can just hold only IPv4 Transport
                type, it is deprecated and replaced by 
                ccCopyServerAddressRev1.
                ''',
                'cccopyserveraddress',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyServerAddressRev1', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of the TFTP server from (or to)
                which to copy the configuration file. This object
                must be created when either the 
                ccCopySourceFileType or ccCopyDestFileType has the
                value 'networkFile'.  
                
                All bits as 0s or 1s for ccCopyServerAddressRev1 are
                not allowed.
                
                The format of this address depends on the value of 
                the ccCopyServerAddressType object.
                ''',
                'cccopyserveraddressrev1',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyServerAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object indicates the transport type of the
                address contained in ccCopyServerAddressRev1 object.
                
                This must be created when either the
                ccCopySourceFileType or ccCopyDestFileType has the
                value 'networkFile'.
                ''',
                'cccopyserveraddresstype',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopySourceFileType', REFERENCE_ENUM_CLASS, 'ConfigfiletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'ConfigfiletypeEnum', 
                [], [], 
                '''                Specifies the type of file to copy from. Either the
                ccCopySourceFileType or the ccCopyDestFileType 
                (or both) must be of type 'runningConfig' or 
                'startupConfig'. Also, the ccCopySourceFileType
                must be different from the ccCopyDestFileType.
                
                If the ccCopySourceFileType has the value of 
                'networkFile', the ccCopyServerAddress/
                ccCopyServerAddressRev1 and ccCopyServerAddressType
                and ccCopyFileName must also be created, and 3 
                objects together (ccCopySourceFileType,
                ccCopyServerAddressRev1, ccCopyFileName) will 
                uniquely identify the source file. If 
                ccCopyServerAddress is created then 
                ccCopyServerAddressRev1 will store the
                same IP address and ccCopyServerAddressType will 
                take the value 'ipv4'. 
                
                If the ccCopySourceFileType is 'iosFile', the 
                ccCopyFileName must also be created, and the 
                2 objects together (ccCopySourceFileType,
                ccCopyFileName) will uniquely identify the source 
                file.
                ''',
                'cccopysourcefiletype',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyState', REFERENCE_ENUM_CLASS, 'ConfigcopystateEnum' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'ConfigcopystateEnum', 
                [], [], 
                '''                Specifies the state of this config-copy request.
                This value of this object is instantiated only after 
                the row has been instantiated, i.e. after the 
                ccCopyEntryRowStatus has been made active.
                ''',
                'cccopystate',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyTimeCompleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the time the ccCopyState last
                transitioned from 'running' to 'successful' or 
                'failed' states. This object is instantiated only 
                after the row has been instantiated.
                Its value will remain 0 until the request has 
                completed.
                ''',
                'cccopytimecompleted',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyTimeStarted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the time the ccCopyState last
                transitioned to 'running', or 0 if the state has 
                never transitioned to 'running'(e.g., stuck in
                'waiting' state).
                
                This object is instantiated only after the row has 
                been instantiated.
                ''',
                'cccopytimestarted',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyUserName', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Remote username for copy via FTP, RCP, SFTP or
                SCP protocol.
                This object must be created when the ccCopyProtocol
                is 'rcp', 'scp', 'ftp', or 'sftp'.
                If the protocol is RCP, it will override the remote 
                username configured through the 
                        rcmd remote-username <username>
                configuration command. 
                The remote username is sent as the server username 
                in an RCP command request sent by the system to a
                remote RCP server.
                ''',
                'cccopyusername',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyUserPassword', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Password used by FTP, SFTP or SCP for copying a
                file to/from an FTP/SFTP/SCP server. This object 
                must be created when the ccCopyProtocol is FTP or
                SCP. 
                Reading it returns a zero-length string for security 
                reasons.
                ''',
                'cccopyuserpassword',
                'CISCO-CONFIG-COPY-MIB', False),
            ],
            'CISCO-CONFIG-COPY-MIB',
            'ccCopyEntry',
            _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB'
        ),
    },
    'CiscoConfigCopyMib.Cccopytable' : {
        'meta_info' : _MetaInfoClass('CiscoConfigCopyMib.Cccopytable',
            False, 
            [
            _MetaInfoClassMember('ccCopyEntry', REFERENCE_LIST, 'Cccopyentry' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'CiscoConfigCopyMib.Cccopytable.Cccopyentry', 
                [], [], 
                '''                A config-copy request.
                
                A management station wishing to create an entry 
                should first generate a random serial number to be
                used as the index to this sparse table. The station 
                should then create the associated instance of the
                row status and row index objects.  It must also, 
                either in the same or in successive PDUs, create an
                instance of ccCopySourceFileType and 
                ccCopyDestFileType.
                
                At least one of the file types defined in 
                ConfigFileType TC must be an agent-config file type
                (i.e. 'startupConfig' or 'runningConfig').
                If one of the file types is a 'networkFile', a valid
                ccCopyFileName and ccCopyServerAddressType and 
                ccCopyServerAddressRev1 or just ccCopyServerAddress
                must be created as well. If ccCopyServerAddress is
                created then ccCopyServerAddressRev1 will store the
                same IP address and ccCopyServerAddressType will 
                take the value 'ipv4'.
                
                For a file type of 'iosFile', only
                a valid ccCopyFileName needs to be created as an 
                extra parameter.
                
                It should also modify the default values for the 
                other configuration objects if the defaults are not
                appropriate.
                
                Once the appropriate instance of all the 
                configuration objects have been created, either by
                an explicit SNMP set request or by default, the row 
                status should be set to active to initiate the 
                request. Note that this entire procedure may be 
                initiated via a single set request which specifies
                a row status of createAndGo as well as
                specifies valid values for the non-defaulted 
                configuration objects.
                
                Once the config-copy request has been created 
                (i.e. the ccCopyEntryRowStatus has been made 
                active), the entry cannot be modified - the only 
                operation possible after this is to delete the row.
                
                Once the request completes, the management station 
                should retrieve the values of the status objects of 
                interest, and should then delete the entry.  In
                order to prevent old entries from clogging the 
                table, entries will be aged out, but an entry will 
                ever be deleted within 5 minutes of completing.
                ''',
                'cccopyentry',
                'CISCO-CONFIG-COPY-MIB', False),
            ],
            'CISCO-CONFIG-COPY-MIB',
            'ccCopyTable',
            _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB'
        ),
    },
    'CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry' : {
        'meta_info' : _MetaInfoClass('CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry',
            False, 
            [
            _MetaInfoClassMember('ccCopyIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cccopyindex',
                'CISCO-CONFIG-COPY-MIB', True),
            _MetaInfoClassMember('ccCopyErrorIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A monotonically increasing integer for the sole
                purpose of indexing entries in this table.
                When a config copy operation has multiple 
                destinations, then this index value is used to 
                distinguish between those multiple destinations.
                ''',
                'cccopyerrorindex',
                'CISCO-CONFIG-COPY-MIB', True),
            _MetaInfoClassMember('ccCopyErrorDescription', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The error description for the error happened
                for this destination of this config copy 
                operation.
                ''',
                'cccopyerrordescription',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyErrorDeviceIpAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of this destination device on which
                config copy operation is performed.
                The object value has to be consistent with the type
                specified in ccCopyErrorDeviceIpAddressType.
                ''',
                'cccopyerrordeviceipaddress',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyErrorDeviceIpAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of Internet address for this destination
                device on which config copy operation is performed.
                ''',
                'cccopyerrordeviceipaddresstype',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyErrorDeviceWWN', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (8, None), (16, None)], [], 
                '''                The World Wide Name (WWN) of this destination
                device on which config copy operation is performed.
                The value of this object is zero-length string if 
                WWN is unassigned or unknown. For example, devices 
                which do not support fibre channel would not
                have WWN.
                ''',
                'cccopyerrordevicewwn',
                'CISCO-CONFIG-COPY-MIB', False),
            ],
            'CISCO-CONFIG-COPY-MIB',
            'ccCopyErrorEntry',
            _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB'
        ),
    },
    'CiscoConfigCopyMib.Cccopyerrortable' : {
        'meta_info' : _MetaInfoClass('CiscoConfigCopyMib.Cccopyerrortable',
            False, 
            [
            _MetaInfoClassMember('ccCopyErrorEntry', REFERENCE_LIST, 'Cccopyerrorentry' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry', 
                [], [], 
                '''                An entry containing information about the
                outcome at one destination of a failed config
                copy operation.
                ''',
                'cccopyerrorentry',
                'CISCO-CONFIG-COPY-MIB', False),
            ],
            'CISCO-CONFIG-COPY-MIB',
            'ccCopyErrorTable',
            _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB'
        ),
    },
    'CiscoConfigCopyMib' : {
        'meta_info' : _MetaInfoClass('CiscoConfigCopyMib',
            False, 
            [
            _MetaInfoClassMember('ccCopyErrorTable', REFERENCE_CLASS, 'Cccopyerrortable' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'CiscoConfigCopyMib.Cccopyerrortable', 
                [], [], 
                '''                A table containing information about the failure
                cause of the config copy operation. An entry is
                created only when the value of ccCopyState changes
                to 'failed' for a config copy operation.
                
                Not all combinations of ccCopySourceFileType and
                ccCopyDestFileType need to be supported.  For
                example, an implementation may choose to support
                only the following combination:
                ccCopySourceFileType = 'runningConfig'
                ccCopyDestFileType = 'fabricStartupConfig'. 
                
                In the case where a fabric wide config copy 
                operation is being performed, for example by
                selecting ccCopyDestFileType value to be
                'fabricStartupConfig', it is possible that the
                fabric could have more than one device. In such
                cases this table would have one entry for each
                device in the fabric. In this case even if the 
                operation succeeded in one device and failed in 
                another, the operation as such has failed, so the
                global state  represented by ccCopyState 'failed',
                but for the device on which it was success, 
                ccCopyErrorDescription would have the 
                distinguished value, 'success'. 
                
                Once the config copy operation completes and if an
                entry gets instantiated, the management station 
                should retrieve the values of the status objects of 
                interest. Once an entry in ccCopyTable is deleted
                by management station, all the corresponding entries
                with the same ccCopyIndex in this table are also 
                deleted. 
                
                In order to prevent old entries from clogging the 
                table, entries age out at the same time as the 
                corresponding entry with same ccCopyIndex in 
                ccCopyTable ages out.
                ''',
                'cccopyerrortable',
                'CISCO-CONFIG-COPY-MIB', False),
            _MetaInfoClassMember('ccCopyTable', REFERENCE_CLASS, 'Cccopytable' , 'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB', 'CiscoConfigCopyMib.Cccopytable', 
                [], [], 
                '''                A table of config-copy requests.
                ''',
                'cccopytable',
                'CISCO-CONFIG-COPY-MIB', False),
            ],
            'CISCO-CONFIG-COPY-MIB',
            'CISCO-CONFIG-COPY-MIB',
            _yang_ns._namespaces['CISCO-CONFIG-COPY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB'
        ),
    },
}
_meta_table['CiscoConfigCopyMib.Cccopytable.Cccopyentry']['meta_info'].parent =_meta_table['CiscoConfigCopyMib.Cccopytable']['meta_info']
_meta_table['CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry']['meta_info'].parent =_meta_table['CiscoConfigCopyMib.Cccopyerrortable']['meta_info']
_meta_table['CiscoConfigCopyMib.Cccopytable']['meta_info'].parent =_meta_table['CiscoConfigCopyMib']['meta_info']
_meta_table['CiscoConfigCopyMib.Cccopyerrortable']['meta_info'].parent =_meta_table['CiscoConfigCopyMib']['meta_info']
