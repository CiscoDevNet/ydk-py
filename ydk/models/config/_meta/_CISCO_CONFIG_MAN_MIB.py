


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'HistoryEventMedium_Enum' : _MetaInfoEnum('HistoryEventMedium_Enum', 'ydk.models.config.CISCO_CONFIG_MAN_MIB',
        {
            'erase':'ERASE',
            'commandSource':'COMMANDSOURCE',
            'running':'RUNNING',
            'startup':'STARTUP',
            'local':'LOCAL',
            'networkTftp':'NETWORKTFTP',
            'networkRcp':'NETWORKRCP',
            'networkFtp':'NETWORKFTP',
            'networkScp':'NETWORKSCP',
        }, 'CISCO-CONFIG-MAN-MIB', _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB']),
    'CISCOCONFIGMANMIB.CcmCLICfg' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmCLICfg',
            False, 
            [
            _MetaInfoClassMember('ccmCLICfgRunConfNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates whether the system produces
                the ccmCLIRunningConfigChanged notification. A false 
                value will prevent notifications from being generated 
                by this system.
                ''',
                'ccmclicfgrunconfnotifenable',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmCLICfg',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmCLIHistory' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmCLIHistory',
            False, 
            [
            _MetaInfoClassMember('ccmCLIHistoryCmdEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of entries in
                ccmCLIHistoryCommandTable.
                ''',
                'ccmclihistorycmdentries',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCLIHistoryCmdEntriesAllowed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the upper limit on the
                number of entries allowed in 
                ccmCLIHistoryCommandTable by the managed system.
                ''',
                'ccmclihistorycmdentriesallowed',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCLIHistoryMaxCmdEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum number of entries that can be held in
                ccmCLIHistoryCommandTable.
                
                The recommended value for implementations is 100.
                
                If the number of entries in ccmCLIHistoryCommandTable 
                exceeds the value of this object, old entries will be 
                bumped to make room for new entries.
                
                The ccmCLIHistoryCommandTable will not be populated
                if the value of this object is 0.
                ''',
                'ccmclihistorymaxcmdentries',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmCLIHistory',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry',
            False, 
            [
            _MetaInfoClassMember('ccmCLIHistoryCommandIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                A monotonically increasing integer for the
                purpose of indexing CLI commands which took effect
                during a configuration event.
                ''',
                'ccmclihistorycommandindex',
                'CISCO-CONFIG-MAN-MIB', True),
            _MetaInfoClassMember('ccmHistoryEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ccmhistoryeventindex',
                'CISCO-CONFIG-MAN-MIB', True),
            _MetaInfoClassMember('ccmCLIHistoryCommand', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The CLI command entered which took effect
                during the configuration event pointed by 
                ccmHistoryEventIndex.
                ''',
                'ccmclihistorycommand',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmCLIHistoryCommandEntry',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable',
            False, 
            [
            _MetaInfoClassMember('ccmCLIHistoryCommandEntry', REFERENCE_LIST, 'CcmCLIHistoryCommandEntry' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry', 
                [], [], 
                '''                Information about the CLI commands that took effect
                during the configuration event pointed by 
                ccmCLIHistoryEventIndex.
                
                A set of rows in this table having the first
                index as ccmHistoryEventIndex will store the
                CLI commands entered during the corresponding 
                configuration event in ccmHistoryEventTable.
                
                An entry will be created in this table only if 
                the corresponding entry in ccmHistoryEventTable has 
                a value of 'commandLine' for 
                ccmHistoryEventCommandSource.
                ''',
                'ccmclihistorycommandentry',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmCLIHistoryCommandTable',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmCTIDObjects' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmCTIDObjects',
            False, 
            [
            _MetaInfoClassMember('ccmCTID', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the Config Change Tracking ID which
                uniquely represents version-incrementing changes to the IOS 
                running configuration.
                ''',
                'ccmctid',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCTIDLastChangeTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the time when the Config Change Tracking
                ID last changed.
                ''',
                'ccmctidlastchangetime',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCTIDRolledOverNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates whether the system produces the
                ccmCTIDRolledOver notification. A false value will prevent
                notifications from being generated by this system.
                ''',
                'ccmctidrolledovernotifenable',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCTIDWhoChanged', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object indicates the user who last reset the Config Change
                Tracking ID.
                ''',
                'ccmctidwhochanged',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmCTIDObjects',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmHistory' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmHistory',
            False, 
            [
            _MetaInfoClassMember('ccmHistoryEventEntriesBumped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the oldest entry in
                ccmHistoryEventTable was deleted to make room 
                for a new entry.
                ''',
                'ccmhistoryevententriesbumped',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryMaxEventEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The maximum number of entries that can be held in
                ccmHistoryEventTable.
                
                The recommended value for implementations is 10.
                ''',
                'ccmhistorymaxevententries',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryRunningLastChanged', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the running configuration
                was last changed.
                
                        If the value of ccmHistoryRunningLastChanged is
                        greater than ccmHistoryRunningLastSaved, the 
                        configuration has been changed but not saved.
                ''',
                'ccmhistoryrunninglastchanged',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryRunningLastSaved', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the running configuration
                was last saved (written).
                
                If the value of ccmHistoryRunningLastChanged is 
                greater than ccmHistoryRunningLastSaved, the 
                configuration has been changed but not saved.
                
                What constitutes a safe saving of the running
                configuration is a management policy issue beyond the
                scope of this MIB.  For some installations, writing the
                running configuration to a terminal may be a way of
                capturing and saving it.  Others may use local or
                remote storage.  Thus ANY write is considered saving
                for the purposes of the MIB.
                ''',
                'ccmhistoryrunninglastsaved',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryStartupLastChanged', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the startup configuration
                was last written to.  In general this is the
                default configuration used when cold starting the
                system.  It may have been changed by a save of the
                running configuration or by a copy from elsewhere.
                ''',
                'ccmhistorystartuplastchanged',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmHistory',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventCommandSource_Enum' : _MetaInfoEnum('CcmHistoryEventCommandSource_Enum', 'ydk.models.config.CISCO_CONFIG_MAN_MIB',
        {
            'commandLine':'COMMANDLINE',
            'snmp':'SNMP',
        }, 'CISCO-CONFIG-MAN-MIB', _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB']),
    'CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventTerminalType_Enum' : _MetaInfoEnum('CcmHistoryEventTerminalType_Enum', 'ydk.models.config.CISCO_CONFIG_MAN_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'unknown':'UNKNOWN',
            'console':'CONSOLE',
            'terminal':'TERMINAL',
            'virtual':'VIRTUAL',
            'auxiliary':'AUXILIARY',
        }, 'CISCO-CONFIG-MAN-MIB', _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB']),
    'CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry',
            False, 
            [
            _MetaInfoClassMember('ccmHistoryEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                A monotonically increasing integer for the sole
                purpose of indexing events.  When it reaches the 
                maximum value, an extremely unlikely event, the agent 
                wraps the value back to 1 and may flush existing 
                entries.
                ''',
                'ccmhistoryeventindex',
                'CISCO-CONFIG-MAN-MIB', True),
            _MetaInfoClassMember('ccmHistoryCLICmdEntriesBumped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the oldest entry in
                ccmCLIHistoryCommandTable with first index as 
                ccmHistoryEventIndex was deleted to make 
                room for a new entry.
                
                This object is applicable only if 
                ccmHistoryEventCommandSource has a value 
                of 'commandLine'.
                ''',
                'ccmhistoryclicmdentriesbumped',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventCommandSource', REFERENCE_ENUM_CLASS, 'CcmHistoryEventCommandSource_Enum' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventCommandSource_Enum', 
                [], [], 
                '''                The source of the command that instigated the event.
                ''',
                'ccmhistoryeventcommandsource',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventCommandSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                If ccmHistoryEventTerminalType is 'virtual', the
                internet address of the connected system.
                
                If ccmHistoryEventCommandSource is 'snmp', the internet
                address of the requester.
                
                The value is 0.0.0.0 if not available or not 
                applicable.
                
                This object is deprecated by
                ccmHistoryEventCommandSourceAddrRev1
                ''',
                'ccmhistoryeventcommandsourceaddress',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventCommandSourceAddrRev1', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                If ccmHistoryEventTerminalType is 'virtual', the
                internet address of the connected system.
                
                If ccmHistoryEventCommandSource is 'snmp', the
                internet address of the requester.
                
                The value of all bit's is zero  if not available or
                not applicable.
                
                The Format of this address depends on the value of the
                ccmHistoryEventCommandSourceAddrType object.
                
                This object deprecates
                ccmHistoryEventCommandSourceAddress
                ''',
                'ccmhistoryeventcommandsourceaddrrev1',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventCommandSourceAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object indicates the transport type of the
                address contained in
                ccmHistoryEventCommandSourceAddrRev1.
                
                The value will be zero if not available or not
                applicable.
                ''',
                'ccmhistoryeventcommandsourceaddrtype',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventConfigDestination', REFERENCE_ENUM_CLASS, 'HistoryEventMedium_Enum' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'HistoryEventMedium_Enum', 
                [], [], 
                '''                The configuration data destination for the event.
                ''',
                'ccmhistoryeventconfigdestination',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventConfigSource', REFERENCE_ENUM_CLASS, 'HistoryEventMedium_Enum' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'HistoryEventMedium_Enum', 
                [], [], 
                '''                The configuration data source for the event.
                ''',
                'ccmhistoryeventconfigsource',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                If ccmHistoryEventConfigSource or
                ccmHistoryEventConfigDestination is 'networkTftp' or
                'networkRcp', the configuration file name at the
                storage file server.  The length is zero if not
                available or not applicable.
                ''',
                'ccmhistoryeventfile',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventRcpUser', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                If ccmHistoryEventConfigSource or
                ccmHistoryEventConfigDestination is 'networkRcp', the
                remote user name.  The length is zero if not applicable
                or not available.
                ''',
                'ccmhistoryeventrcpuser',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventServerAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                If ccmHistoryEventConfigSource or
                ccmHistoryEventConfigDestination is 'networkTftp' or
                'networkRcp', the internet address of the storage file
                server.  The value is 0.0.0.0 if not applicable or not
                        available.
                        This object is deprecated by
                        ccmHistoryEventServerAddrRev1
                ''',
                'ccmhistoryeventserveraddress',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventServerAddrRev1', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                If ccmHistoryEventConfigSource or
                ccmHistoryEventConfigDestination is 'networkTftp' or
                'networkRcp', the internet address of the storage file
                server. 
                
                The value of all bits is 0s if not applicable or not
                available.
                
                The Format of this address depends on the value of the
                ccmHistoryEventServerAddrType object.
                
                This object deprecates ccmHistoryEventServerAddress.
                ''',
                'ccmhistoryeventserveraddrrev1',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventServerAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                This object indicates the transport type of the
                address contained in ccmHistoryEventServerAddrRev1.
                
                The value will be zero if not available or not
                aplicable.
                ''',
                'ccmhistoryeventserveraddrtype',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventTerminalLocation', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                If ccmHistoryEventCommandSource is 'commandLine',
                the hard-wired location of the terminal or the remote 
                host for an incoming connection.  The length is zero 
                if not available or not applicable.
                ''',
                'ccmhistoryeventterminallocation',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventTerminalNumber', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                If ccmHistoryEventCommandSource is 'commandLine',
                the terminal number.  The value is -1 if not available
                or not applicable.
                ''',
                'ccmhistoryeventterminalnumber',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventTerminalType', REFERENCE_ENUM_CLASS, 'CcmHistoryEventTerminalType_Enum' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventTerminalType_Enum', 
                [], [], 
                '''                If ccmHistoryEventCommandSource is 'commandLine',
                the terminal type, otherwise 'notApplicable'.
                ''',
                'ccmhistoryeventterminaltype',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventTerminalUser', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                If ccmHistoryEventCommandSource is 'commandLine',
                the name of the logged in user.  The length is zero if
                not available or not applicable.
                ''',
                'ccmhistoryeventterminaluser',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the event occurred.
                ''',
                'ccmhistoryeventtime',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventVirtualHostName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                If ccmHistoryEventTerminalType is 'virtual', the host
                name of the connected system.  The length is zero if
                not available or not applicable.
                ''',
                'ccmhistoryeventvirtualhostname',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmHistoryEventEntry',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB.CcmHistoryEventTable' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB.CcmHistoryEventTable',
            False, 
            [
            _MetaInfoClassMember('ccmHistoryEventEntry', REFERENCE_LIST, 'CcmHistoryEventEntry' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry', 
                [], [], 
                '''                Information about a configuration event on this
                router.
                ''',
                'ccmhistoryevententry',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'ccmHistoryEventTable',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
    'CISCOCONFIGMANMIB' : {
        'meta_info' : _MetaInfoClass('CISCOCONFIGMANMIB',
            False, 
            [
            _MetaInfoClassMember('ccmCLICfg', REFERENCE_CLASS, 'CcmCLICfg' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmCLICfg', 
                [], [], 
                '''                ''',
                'ccmclicfg',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCLIHistory', REFERENCE_CLASS, 'CcmCLIHistory' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmCLIHistory', 
                [], [], 
                '''                ''',
                'ccmclihistory',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCLIHistoryCommandTable', REFERENCE_CLASS, 'CcmCLIHistoryCommandTable' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable', 
                [], [], 
                '''                A table of CLI commands that took effect during
                configuration events.
                ''',
                'ccmclihistorycommandtable',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmCTIDObjects', REFERENCE_CLASS, 'CcmCTIDObjects' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmCTIDObjects', 
                [], [], 
                '''                ''',
                'ccmctidobjects',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistory', REFERENCE_CLASS, 'CcmHistory' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmHistory', 
                [], [], 
                '''                ''',
                'ccmhistory',
                'CISCO-CONFIG-MAN-MIB', False),
            _MetaInfoClassMember('ccmHistoryEventTable', REFERENCE_CLASS, 'CcmHistoryEventTable' , 'ydk.models.config.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB.CcmHistoryEventTable', 
                [], [], 
                '''                A table of configuration events on this router.
                ''',
                'ccmhistoryeventtable',
                'CISCO-CONFIG-MAN-MIB', False),
            ],
            'CISCO-CONFIG-MAN-MIB',
            'CISCO-CONFIG-MAN-MIB',
            _yang_ns._namespaces['CISCO-CONFIG-MAN-MIB'],
        'ydk.models.config.CISCO_CONFIG_MAN_MIB'
        ),
    },
}
_meta_table['CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmCLICfg']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmCLIHistory']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmCTIDObjects']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmHistory']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB']['meta_info']
_meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable']['meta_info'].parent =_meta_table['CISCOCONFIGMANMIB']['meta_info']
