


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'NfInterfaceDirectionTypes_Enum' : _MetaInfoEnum('NfInterfaceDirectionTypes_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'interfaceDirNone':'INTERFACEDIRNONE',
            'interfaceDirIngress':'INTERFACEDIRINGRESS',
            'interfaceDirEgress':'INTERFACEDIREGRESS',
            'interfaceDirBoth':'INTERFACEDIRBOTH',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'NfTopFlowsSortTypes_Enum' : _MetaInfoEnum('NfTopFlowsSortTypes_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'noSort':'NOSORT',
            'byPackets':'BYPACKETS',
            'byBytes':'BYBYTES',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'NfTemplateTypes_Enum' : _MetaInfoEnum('NfTemplateTypes_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'template':'TEMPLATE',
            'optionTemplate':'OPTIONTEMPLATE',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'NfCacheTypes_Enum' : _MetaInfoEnum('NfCacheTypes_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'main':'MAIN',
            'as':'AS',
            'protocolPort':'PROTOCOLPORT',
            'sourcePrefix':'SOURCEPREFIX',
            'destinationPrefix':'DESTINATIONPREFIX',
            'prefix':'PREFIX',
            'destinationOnly':'DESTINATIONONLY',
            'sourceDestination':'SOURCEDESTINATION',
            'fullFlow':'FULLFLOW',
            'asTos':'ASTOS',
            'protocolPortTos':'PROTOCOLPORTTOS',
            'sourcePrefixTos':'SOURCEPREFIXTOS',
            'destinationPrefixTos':'DESTINATIONPREFIXTOS',
            'prefixTos':'PREFIXTOS',
            'prefixPort':'PREFIXPORT',
            'bgpNexthopTos':'BGPNEXTHOPTOS',
            'expBgpPrefix':'EXPBGPPREFIX',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'NfFlowDirectionTypes_Enum' : _MetaInfoEnum('NfFlowDirectionTypes_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'flowDirNone':'FLOWDIRNONE',
            'flowDirIngress':'FLOWDIRINGRESS',
            'flowDirEgress':'FLOWDIREGRESS',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'NfProtocolTypes_Enum' : _MetaInfoEnum('NfProtocolTypes_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'tcpTelnet':'TCPTELNET',
            'tcpFtp':'TCPFTP',
            'tcpFtpd':'TCPFTPD',
            'tcpWww':'TCPWWW',
            'tcpSmtp':'TCPSMTP',
            'tcpX':'TCPX',
            'tcpBgp':'TCPBGP',
            'tcpNntp':'TCPNNTP',
            'tcpFrag':'TCPFRAG',
            'tcpOther':'TCPOTHER',
            'udpDns':'UDPDNS',
            'udpNtp':'UDPNTP',
            'udpTftp':'UDPTFTP',
            'udpFrag':'UDPFRAG',
            'udpOther':'UDPOTHER',
            'icmp':'ICMP',
            'igmp':'IGMP',
            'ipInIp':'IPINIP',
            'ipv6InIp':'IPV6INIP',
            'gre':'GRE',
            'ipOther':'IPOTHER',
            'all':'ALL',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable.CnfCIBridgedFlowStatsCtrlEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable.CnfCIBridgedFlowStatsCtrlEntry',
            False, 
            [
            _MetaInfoClassMember('cnfCIBridgedFlowVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the Vlan number on which the reporting of
                bridged flow statistics is configured.
                ''',
                'cnfcibridgedflowvlan',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfCIBridgedFlowStatsCrtEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the bridged flow creation is enabled
                for this vlan.
                ''',
                'cnfcibridgedflowstatscrtenable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIBridgedFlowStatsExpEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the export of bridged flow statistics
                is enabled for this vlan.
                ''',
                'cnfcibridgedflowstatsexpenable',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCIBridgedFlowStatsCtrlEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable',
            False, 
            [
            _MetaInfoClassMember('cnfCIBridgedFlowStatsCtrlEntry', REFERENCE_LIST, 'CnfCIBridgedFlowStatsCtrlEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable.CnfCIBridgedFlowStatsCtrlEntry', 
                [], [], 
                '''                A conceptual row in the cnfCIBridgedFlowStatsCtrlTable,
                containing the configuration of bridged flow statistics
                per vlan. When a vlan is created in a device supporting
                this table, a corresponding entry will be added to this 
                table.
                ''',
                'cnfcibridgedflowstatsctrlentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCIBridgedFlowStatsCtrlTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfCICacheTable.CnfCICacheEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCICacheTable.CnfCICacheEntry',
            False, 
            [
            _MetaInfoClassMember('cnfCICacheType', REFERENCE_ENUM_CLASS, 'NfCacheTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfCacheTypes_Enum', 
                [], [], 
                '''                The type of netflow cache.
                
                NetFlow aggregation maintains one or more extra flow caches
                with different combinations of fields that determine
                which traditional flows are grouped together.
                ''',
                'cnfcicachetype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfCIActiveFlows', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of currently active flow entries.
                ''',
                'cnfciactiveflows',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIActiveTimeOut', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The timeout period (in minutes) for removing active flows
                from the cache.
                ''',
                'cnfciactivetimeout',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCICacheEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether netflow is enabled for this cache type.
                ''',
                'cnfcicacheenable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCICacheEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of entries that can be cached for this cache type.
                The accepted value could be limited based on the amount of
                memory available in the system.
                ''',
                'cnfcicacheentries',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIInactiveFlows', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of available flow entries.
                ''',
                'cnfciinactiveflows',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIInactiveTimeOut', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The timeout period (in seconds) for removing inactive flows
                from the cache.
                ''',
                'cnfciinactivetimeout',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIMinDestinationMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                Destination route's minimum configured mask bits. This is used
                to configure the minimum mask for Router Based Aggregation
                (RBA). Minimum masking capability is available only if RBA is
                enabled. A value of 0 indicates that this object is not
                applicable to this cache type.
                ''',
                'cnfcimindestinationmask',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIMinSourceMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                Source route's minimum configured mask bits. This is used to
                configure the minimum mask for Router Based Aggregation
                (RBA). Minimum masking capability is available only if RBA is
                enabled. A value of 0 indicates that this object is not
                applicable to this cache type.
                ''',
                'cnfciminsourcemask',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCICacheEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfCICacheTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCICacheTable',
            False, 
            [
            _MetaInfoClassMember('cnfCICacheEntry', REFERENCE_LIST, 'CnfCICacheEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCICacheTable.CnfCICacheEntry', 
                [], [], 
                '''                A conceptual row in the cnfCICacheEntry.
                ''',
                'cnfcicacheentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCICacheTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfCIInterfaceTable.CnfCIInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCIInterfaceTable.CnfCIInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfCIMcastNetflowEnable', REFERENCE_ENUM_CLASS, 'NfInterfaceDirectionTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfInterfaceDirectionTypes_Enum', 
                [], [], 
                '''                Indicates whether the multicast netflow accounting feature
                is enabled for this interface, and if so, in which 
                directions.
                ''',
                'cnfcimcastnetflowenable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCINetflowEnable', REFERENCE_ENUM_CLASS, 'NfInterfaceDirectionTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfInterfaceDirectionTypes_Enum', 
                [], [], 
                '''                Indicates whether the netflow feature is enabled for this
                interface, and if so, in which directions.
                ''',
                'cnfcinetflowenable',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCIInterfaceEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfCIInterfaceTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCIInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('cnfCIInterfaceEntry', REFERENCE_LIST, 'CnfCIInterfaceEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCIInterfaceTable.CnfCIInterfaceEntry', 
                [], [], 
                '''                A conceptual row in the cnfCIInterfaceEntry.
                ''',
                'cnfciinterfaceentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCIInterfaceTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfCacheInfo' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfCacheInfo',
            False, 
            [
            _MetaInfoClassMember('cnfCIMcastNetflowRPFFailedEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether netflow accounting for multicast data
                that fails the reverse path forwarding (RPF) check is
                enabled.
                ''',
                'cnfcimcastnetflowrpffailedenable',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfCacheInfo',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfEICollectorTable.CnfEICollectorEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfEICollectorTable.CnfEICollectorEntry',
            False, 
            [
            _MetaInfoClassMember('cnfCICacheType', REFERENCE_ENUM_CLASS, 'NfCacheTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfCacheTypes_Enum', 
                [], [], 
                '''                ''',
                'cnfcicachetype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfEICollectorAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Internet address of the collector. This is the
                address which the Netflow data is exported to.
                ''',
                'cnfeicollectoraddress',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfEICollectorAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of Internet address used by this entry.
                ''',
                'cnfeicollectoraddresstype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfEICollectorPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The transport port of the collector which the Netflow data is
                exported to.
                ''',
                'cnfeicollectorport',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfEICollectorStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object is used to create or delete an entry
                in the cnfEICollectorTable.
                
                * A row may be created using the 'CreateAndGo' option. When
                  the row is successfully created, the RowStatus would be
                  set to 'active' by the agent.
                
                * A row may be deleted by setting the RowStatus to 'destroy'.
                ''',
                'cnfeicollectorstatus',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfEICollectorEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfEICollectorTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfEICollectorTable',
            False, 
            [
            _MetaInfoClassMember('cnfEICollectorEntry', REFERENCE_LIST, 'CnfEICollectorEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfEICollectorTable.CnfEICollectorEntry', 
                [], [], 
                '''                A conceptual row in the cnfEICollectorEntry.
                ''',
                'cnfeicollectorentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfEICollectorTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfEIExportInfoTable.CnfEIExportInfoEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfEIExportInfoTable.CnfEIExportInfoEntry',
            False, 
            [
            _MetaInfoClassMember('cnfCICacheType', REFERENCE_ENUM_CLASS, 'NfCacheTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfCacheTypes_Enum', 
                [], [], 
                '''                ''',
                'cnfcicachetype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfEIBgpNextHop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object enables collection of BGP Next Hops. cnfEIPeerAS,
                cnfEIOriginAS and cnfEIBgpNextHop are interdependent.
                ''',
                'cnfeibgpnexthop',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfEIExportVersion', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The NetFlow data export version.
                ''',
                'cnfeiexportversion',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfEIOriginAS', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object enables collection of AS numbers from an origin
                autonomous system. cnfEIPeerAS, cnfEIOriginAS and
                cnfEIBgpNextHop are interdependent.
                ''',
                'cnfeioriginas',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfEIPeerAS', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object enables collection of AS numbers from a peer
                autonomous system. cnfEIPeerAS, cnfEIOriginAS and
                cnfEIBgpNextHop are interdependent.
                ''',
                'cnfeipeeras',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfEIExportInfoEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfEIExportInfoTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfEIExportInfoTable',
            False, 
            [
            _MetaInfoClassMember('cnfEIExportInfoEntry', REFERENCE_LIST, 'CnfEIExportInfoEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfEIExportInfoTable.CnfEIExportInfoEntry', 
                [], [], 
                '''                A conceptual row in the cnfEIExportInfoEntry.
                ''',
                'cnfeiexportinfoentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfEIExportInfoTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfExportInfo' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfExportInfo',
            False, 
            [
            _MetaInfoClassMember('cnfEIMaxCollectors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum number of entries allowed in the cnfEICollectorTable
                for each cache type.
                A zero indicates export is not supported in the device.
                The agent should set this value during initialization, and
                the value for this object cannot be changed during the
                system's operation.
                ''',
                'cnfeimaxcollectors',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfExportInfo',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfExportStatistics' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfExportStatistics',
            False, 
            [
            _MetaInfoClassMember('cnfESExportRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Bytes exported per second.
                ''',
                'cnfesexportrate',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfESPktsDropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of export packets which were dropped at the time of
                ipwrite operation. The reasons for this failure are no FIB,
                adjacency failure, MTU failed, enqueue failed, IPC failed etc.
                ''',
                'cnfespktsdropped',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfESPktsExported', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets (udp datagrams) which were exported.
                ''',
                'cnfespktsexported',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfESPktsFailed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times a flow record could not be exported because of
                a pak allocation failure.
                ''',
                'cnfespktsfailed',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfESRecordsExported', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of flow statistics records which were exported.
                ''',
                'cnfesrecordsexported',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfESSampledPacket', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Sampled Packet.
                ''',
                'cnfessampledpacket',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfExportStatistics',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfExportTemplate' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfExportTemplate',
            False, 
            [
            _MetaInfoClassMember('cnfTemplateOptionsFlag', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Object to indicate Sub- technologies in option template.
                ''',
                'cnftemplateoptionsflag',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfExportTemplate',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfPSProtocolStatTable.CnfPSProtocolStatEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfPSProtocolStatTable.CnfPSProtocolStatEntry',
            False, 
            [
            _MetaInfoClassMember('cnfPSProtocolType', REFERENCE_ENUM_CLASS, 'NfProtocolTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfProtocolTypes_Enum', 
                [], [], 
                '''                This object is used as INDEX for protocol statistic table.
                Protocol type consists of groups based on well known ports
                and protocols.
                ''',
                'cnfpsprotocoltype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfPSActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This is a summation of active time of all flows belonging to
                the same protocol and port in milliseconds. The time between
                first switched packet and last switched packet is measured as
                the active time of a flow.
                ''',
                'cnfpsactive',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfPSBytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of Bytes belonging to the same protocol and port,
                which were switched by netflow enabled interface(s).
                This counter contains the number of Packets switched by all
                netflow enabled line cards.
                ''',
                'cnfpsbytes',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfPSExpiredFlows', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of flows belonging to the same protocol and port
                that were expired. This counter is incremented when a flow
                expires due to some reason like time out of flows,
                event based aging etc.
                ''',
                'cnfpsexpiredflows',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfPSInactive', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This is a summation of inactive time of all flows belonging to
                the same protocol and port in milliseconds. The time between
                the last switched packet and expiry of a flow is measured as
                the inactive time of a flow.
                ''',
                'cnfpsinactive',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfPSPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of Packets belonging to the same protocol and port
                which were switched by netflow enabled interface(s).
                This counter contains the number of Packets switched by all
                netflow enabled line cards.
                ''',
                'cnfpspackets',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfPSProtocolStatEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfPSProtocolStatTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfPSProtocolStatTable',
            False, 
            [
            _MetaInfoClassMember('cnfPSProtocolStatEntry', REFERENCE_LIST, 'CnfPSProtocolStatEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfPSProtocolStatTable.CnfPSProtocolStatEntry', 
                [], [], 
                '''                A conceptual row in the CnfPSProtocolStatEntry.
                ''',
                'cnfpsprotocolstatentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfPSProtocolStatTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfProtocolStatistics' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfProtocolStatistics',
            False, 
            [
            _MetaInfoClassMember('cnfPSLastClearElapsedTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Object indicates time in millisecond since the last clearing
                time of protocol statistics.
                ''',
                'cnfpslastclearelapsedtime',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfPSPacketSizeDistribution', ATTRIBUTE, 'str' , None, None, 
                [(52, None)], [], 
                '''                A string contain IP Packet Size Distribution statistics.
                Distribution grouping are following :1-32   64   96  128
                160  192  224  256 288  320  352 384  416  448  480  512
                544  576 1024 1536 2048 2560 3072 3584 4096 4608. Value for
                each group will be expressed in 2 bytes (in Network byte
                order) and need to divide by 1000 to get the exact value
                given by CLI using show ip cache flow command.
                ''',
                'cnfpspacketsizedistribution',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfProtocolStatistics',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTemplateExportInfoTable.CnfTemplateExportInfoEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTemplateExportInfoTable.CnfTemplateExportInfoEntry',
            False, 
            [
            _MetaInfoClassMember('cnfCICacheType', REFERENCE_ENUM_CLASS, 'NfCacheTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfCacheTypes_Enum', 
                [], [], 
                '''                ''',
                'cnfcicachetype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfTemplateExportVer9Enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object to indicate whether version 9 export is configured
                or not.
                ''',
                'cnftemplateexportver9enable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateExportVer9OptRefreshRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Option refresh rate.
                Options are resent after this many packets.
                ''',
                'cnftemplateexportver9optrefreshrate',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateExportVer9OptTimeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Export option time out.
                Options are resent after this time.
                ''',
                'cnftemplateexportver9opttimeout',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateExportVer9TplRefreshRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Template refresh rate.
                Templates are resent after this many packets.
                ''',
                'cnftemplateexportver9tplrefreshrate',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateExportVer9TplTimeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Export template time out.
                Templates are resent after this time.
                ''',
                'cnftemplateexportver9tpltimeout',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTemplateExportInfoEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTemplateExportInfoTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTemplateExportInfoTable',
            False, 
            [
            _MetaInfoClassMember('cnfTemplateExportInfoEntry', REFERENCE_LIST, 'CnfTemplateExportInfoEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTemplateExportInfoTable.CnfTemplateExportInfoEntry', 
                [], [], 
                '''                A conceptual row in the cnfTemplateExportInfoEntry.
                ''',
                'cnftemplateexportinfoentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTemplateExportInfoTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTemplateTable.CnfTemplateEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTemplateTable.CnfTemplateEntry',
            False, 
            [
            _MetaInfoClassMember('cnfTemplateType', REFERENCE_ENUM_CLASS, 'NfTemplateTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfTemplateTypes_Enum', 
                [], [], 
                '''                Defines the structure and interpretation of fields in a data
                record and serves as an INDEX in this table. Version 9 has two
                types of Templates: Flow Templates and Option Templates.
                ''',
                'cnftemplatetype',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfTemplateActive', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of active templates.
                ''',
                'cnftemplateactive',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateAdded', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of templates added.
                ''',
                'cnftemplateadded',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateAgerPolls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of template ager polls.
                ''',
                'cnftemplateagerpolls',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTemplateEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTemplateTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTemplateTable',
            False, 
            [
            _MetaInfoClassMember('cnfTemplateEntry', REFERENCE_LIST, 'CnfTemplateEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTemplateTable.CnfTemplateEntry', 
                [], [], 
                '''                A conceptual row in the cnfTemplateEntry.
                ''',
                'cnftemplateentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTemplateTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsNextGenActionEffect_Enum' : _MetaInfoEnum('CnfTopFlowsNextGenActionEffect_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'noOp':'NOOP',
            'generate':'GENERATE',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsReportSource_Enum' : _MetaInfoEnum('CnfTopFlowsReportSource_Enum', 'ydk.models.netflow.CISCO_NETFLOW_MIB',
        {
            'other':'OTHER',
            'hardware':'HARDWARE',
            'software':'SOFTWARE',
            'both':'BOTH',
        }, 'CISCO-NETFLOW-MIB', _yang_ns._namespaces['CISCO-NETFLOW-MIB']),
    'CISCONETFLOWMIB.CnfTopFlows' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTopFlows',
            False, 
            [
            _MetaInfoClassMember('cnfTopFlowsAvailableFlows', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of entries currently available in cnfTopFlowsTable.
                ''',
                'cnftopflowsavailableflows',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsCacheTimeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Top Flows Cache timeout. Top flows are cached for this length
                of time and not recalculated. Configure a high value to ensure
                the cache does not change during long queries.
                Setting this object (to any value) will expire the cache.
                ''',
                'cnftopflowscachetimeout',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsGenerate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A control variable used to generate the Top Flows. 
                
                Setting this object to 'true' will generate the Top Flows 
                and populate the Top Flows report in cnfTopFlowsTable  
                unless cnfTopFlowsNextGenActionEffect is supported and the
                value of cnfTopFlowsNextGenActionEffect is 'noOp'.
                
                Setting this object to 'false' has no effect.
                
                When read, this object always returns 'false'.
                ''',
                'cnftopflowsgenerate',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchClass', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Class name to match.
                Leave blank to disable this match criteria.
                ''',
                'cnftopflowsmatchclass',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDirection', REFERENCE_ENUM_CLASS, 'NfFlowDirectionTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfFlowDirectionTypes_Enum', 
                [], [], 
                '''                Flow direction to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchdirection',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDstAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Destination address prefix to match.
                ''',
                'cnftopflowsmatchdstaddress',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDstAddressMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                The length of the match destination address prefix.
                This prefix length must be consistent with the address type
                specified in cnfTopFlowsMatchDstAddressType. A length of zero
                only matches the all-zero address of the specified type.
                ''',
                'cnftopflowsmatchdstaddressmask',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDstAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Destination address type to match.
                A value of 'unknown' (ie, 0) indicates the destination address
                is not used as a top flows match criteria, and clears the
                cnfTopFlowsMatchDstAddress and cnfTopFlowsMatchDstAddressMask
                configuration.
                ''',
                'cnftopflowsmatchdstaddresstype',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDstAS', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Destination AS number to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchdstas',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDstPortHi', ATTRIBUTE, 'int' , None, None, 
                [(-1, 65535)], [], 
                '''                The maximum value that the layer-4 destination port number in
                the flow must have in order to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchdstporthi',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchDstPortLo', ATTRIBUTE, 'int' , None, None, 
                [(-1, 65535)], [], 
                '''                The minimum value that the layer-4 destination port number in
                the flow must have in order to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchdstportlo',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchingFlows', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of matching flows in the netflow cache.
                ''',
                'cnftopflowsmatchingflows',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchInputIf', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Input interface to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchinputif',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchMaxBytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum bytes to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchmaxbytes',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchMaxPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum packets to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchmaxpackets',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchMinBytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum bytes to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchminbytes',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchMinPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum packets to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchminpackets',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchNhAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Nexthop address prefix to match.
                ''',
                'cnftopflowsmatchnhaddress',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchNhAddressMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                The length of the match nexthop address Prefix.
                This prefix length must be consistent with the address type
                specified in cnfTopFlowsMatchNhAddressType. A length of zero
                only matches the all-zero address of the specified type.
                ''',
                'cnftopflowsmatchnhaddressmask',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchNhAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Nexthop address type to match.
                A value of 'unknown' (ie, 0) indicates the nexthop address
                is not used as a top flows match criteria, and clears the
                cnfTopFlowsMatchNhAddress and cnfTopFlowsMatchNhAddressMask
                configuration.
                ''',
                'cnftopflowsmatchnhaddresstype',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchOutputIf', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Output interface to match.
                A value of 0 disables this match criteria.
                ''',
                'cnftopflowsmatchoutputif',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchProtocol', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Protocol to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchprotocol',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSampler', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Sampler name to match.
                Leave blank to disable this match criteria.
                ''',
                'cnftopflowsmatchsampler',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSrcAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Source address prefix to match.
                ''',
                'cnftopflowsmatchsrcaddress',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSrcAddressMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                The length of the match source address prefix.
                This prefix length must be consistent with the address type
                specified in cnfTopFlowsMatchSrcAddressType. A length of zero
                only matches the all-zero address of the specified type.
                ''',
                'cnftopflowsmatchsrcaddressmask',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSrcAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Source address type to match.
                A value of 'unknown' (ie, 0) indicates the source address
                is not used as a top flows match criteria, and clears the
                cnfTopFlowsMatchSrcAddress and cnfTopFlowsMatchSrcAddressMask
                configuration.
                ''',
                'cnftopflowsmatchsrcaddresstype',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSrcAS', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Source AS number to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchsrcas',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSrcPortHi', ATTRIBUTE, 'int' , None, None, 
                [(-1, 65535)], [], 
                '''                The maximum value that the layer-4 source port number in
                the flow must have in order to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchsrcporthi',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchSrcPortLo', ATTRIBUTE, 'int' , None, None, 
                [(-1, 65535)], [], 
                '''                The minimum value that the layer-4 source port number in
                the flow must have in order to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchsrcportlo',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsMatchTOSByte', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                TOS byte to match.
                A value of -1 disables this match criteria.
                ''',
                'cnftopflowsmatchtosbyte',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsNextGenActionEffect', REFERENCE_ENUM_CLASS, 'CnfTopFlowsNextGenActionEffect_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsNextGenActionEffect_Enum', 
                [], [], 
                '''                Indicates the action effect on the system when the 
                cnfTopFlowsGenerate is set to 'true'.  
                
                'noOp' -- indicate that the system will make no operation 
                          when the cnfTopFlowsGenerate is set to 'true'.
                        Examples when this object could return 'noOp' are:
                        1. the system is still in the top flow generation 
                           process. 
                        2. the system will not generate the top flows 
                           report when the value of 
                           cnfTopFlowsReportAvailable is 'true'.
                
                'generate' -- indicates that the system will start the top 
                              flows generation process if the 
                              cntTopFlowsGenerate is set to 'true'.
                        Examples when this object could return 'generate' 
                        are:
                        1. When the value of cnfTopFlowsReportAvailable is 
                           'false'.  
                        2. The system will always generate the top flow
                           report when cnfTopFlowsGenerate is set to 
                           'true'.
                ''',
                'cnftopflowsnextgenactioneffect',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsReportAvailable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the Top Flows report has been 
                successfully generated and is available in 
                cnfTopFlowsTable. 
                
                When the value of this object is 'true', the 
                top flows report is available in cnfTopFlowsTable.
                
                When the value of this object is 'false', there is no
                top flows report available in cnfTopFlowsTable. 
                For Example:
                    1. When top flows report has not been generated or 
                       is currently in the generation process.
                    2. When the top flows has been purged due to
                       the modification of a matching criteria or the
                       expiration of top flow cache timeout.
                ''',
                'cnftopflowsreportavailable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsReportSource', REFERENCE_ENUM_CLASS, 'CnfTopFlowsReportSource_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTopFlows.CnfTopFlowsReportSource_Enum', 
                [], [], 
                '''                Indicates the source of Top Flows report generation for 
                the entries populated in cnfTopFlowsTable.
                
                'other'    - The Top Flows are not available or the source 
                             of the Top Flows cannot be identified.
                
                'hardware' - The Top Flows report has been generated based 
                             on the flows detected by the hardware platform
                             with netflow capabilities.
                
                'software' - The Top Flows report has been generated based
                             on the flows detected by the software.
                
                'both'     - The Top Flows report is an integrated list of 
                             Top Flows detected by both the hardware
                             platform and the software.
                ''',
                'cnftopflowsreportsource',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSortBy', REFERENCE_ENUM_CLASS, 'NfTopFlowsSortTypes_Enum' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'NfTopFlowsSortTypes_Enum', 
                [], [], 
                '''                Indicates how the entries in cnfTopFLowsTable are to be sorted.
                A value of 'noSort' disables Top Flows.
                ''',
                'cnftopflowssortby',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the time when cnfTopFlowsTable was last updated.
                ''',
                'cnftopflowstimestamp',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsTopN', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum number of top flows to calculate.
                A value of 0 disables the Top Flows feature.
                ''',
                'cnftopflowstopn',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsTotalFlows', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of flows in the netflow cache.
                ''',
                'cnftopflowstotalflows',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTopFlows',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTopFlowsTable.CnfTopFlowsTableEntry' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTopFlowsTable.CnfTopFlowsTableEntry',
            False, 
            [
            _MetaInfoClassMember('cnfTopFlowsIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index to select top flows.
                A value of 1 selects the topmost flow.
                ''',
                'cnftopflowsindex',
                'CISCO-NETFLOW-MIB', True),
            _MetaInfoClassMember('cnfTopFlowsBytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bytes in the flow.
                ''',
                'cnftopflowsbytes',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsClassID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Netflow Class ID.
                ''',
                'cnftopflowsclassid',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsDstAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Destination address.
                ''',
                'cnftopflowsdstaddress',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsDstAddressMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                Number of bits in destination address mask.
                ''',
                'cnftopflowsdstaddressmask',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsDstAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Type of destination address.
                ''',
                'cnftopflowsdstaddresstype',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsDstAS', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Destination AS number.
                ''',
                'cnftopflowsdstas',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsDstPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Destination port number.
                ''',
                'cnftopflowsdstport',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsFirstSwitched', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time flow was first switched.
                ''',
                'cnftopflowsfirstswitched',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsFlags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Flow flags.
                ''',
                'cnftopflowsflags',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsInputIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                Input interface index.
                ''',
                'cnftopflowsinputifindex',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsLastSwitched', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time flow was last switched.
                ''',
                'cnftopflowslastswitched',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsNhAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Nexthop address.
                ''',
                'cnftopflowsnhaddress',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsNhAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of nexthop address.
                ''',
                'cnftopflowsnhaddresstype',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsOutputIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                Output interface index.
                ''',
                'cnftopflowsoutputifindex',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets in the flow.
                ''',
                'cnftopflowspackets',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsProtocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Protocol number.
                ''',
                'cnftopflowsprotocol',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSamplerID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Netflow Sampler ID.
                ''',
                'cnftopflowssamplerid',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSrcAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Source address.
                ''',
                'cnftopflowssrcaddress',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSrcAddressMask', ATTRIBUTE, 'int' , None, None, 
                [(0, 2040)], [], 
                '''                Number of bits in source address mask.
                ''',
                'cnftopflowssrcaddressmask',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSrcAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Type of source address.
                ''',
                'cnftopflowssrcaddresstype',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSrcAS', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Source AS number.
                ''',
                'cnftopflowssrcas',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsSrcPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Source port number.
                ''',
                'cnftopflowssrcport',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsTCPFlags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                TCP flags.
                ''',
                'cnftopflowstcpflags',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsTOS', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Type of service.
                ''',
                'cnftopflowstos',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The VLAN-ID of this flow.
                ''',
                'cnftopflowsvlan',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTopFlowsTableEntry',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB.CnfTopFlowsTable' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB.CnfTopFlowsTable',
            False, 
            [
            _MetaInfoClassMember('cnfTopFlowsTableEntry', REFERENCE_LIST, 'CnfTopFlowsTableEntry' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTopFlowsTable.CnfTopFlowsTableEntry', 
                [], [], 
                '''                A conceptual row in the cnfTopFlowsTable.
                ''',
                'cnftopflowstableentry',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'cnfTopFlowsTable',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
    'CISCONETFLOWMIB' : {
        'meta_info' : _MetaInfoClass('CISCONETFLOWMIB',
            False, 
            [
            _MetaInfoClassMember('cnfCacheInfo', REFERENCE_CLASS, 'CnfCacheInfo' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCacheInfo', 
                [], [], 
                '''                ''',
                'cnfcacheinfo',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIBridgedFlowStatsCtrlTable', REFERENCE_CLASS, 'CnfCIBridgedFlowStatsCtrlTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable', 
                [], [], 
                '''                This table controls the reporting of bridged flow statistics
                per vlan.
                ''',
                'cnfcibridgedflowstatsctrltable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCICacheTable', REFERENCE_CLASS, 'CnfCICacheTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCICacheTable', 
                [], [], 
                '''                A table containing configuration and statistics per cache.
                Cache may be main cache or an aggregation cache.
                ''',
                'cnfcicachetable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfCIInterfaceTable', REFERENCE_CLASS, 'CnfCIInterfaceTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfCIInterfaceTable', 
                [], [], 
                '''                This table provides Netflow Enable information per interface.
                ''',
                'cnfciinterfacetable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfEICollectorTable', REFERENCE_CLASS, 'CnfEICollectorTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfEICollectorTable', 
                [], [], 
                '''                A control table to configure the collectors that the netflow
                packets are exported to. The number of entries that can be
                configured for the cache type is limited by the value of
                cnfEIMaxCollectors.
                ''',
                'cnfeicollectortable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfEIExportInfoTable', REFERENCE_CLASS, 'CnfEIExportInfoTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfEIExportInfoTable', 
                [], [], 
                '''                A table containing information about export configuration per
                cache type.
                ''',
                'cnfeiexportinfotable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfExportInfo', REFERENCE_CLASS, 'CnfExportInfo' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfExportInfo', 
                [], [], 
                '''                ''',
                'cnfexportinfo',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfExportStatistics', REFERENCE_CLASS, 'CnfExportStatistics' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfExportStatistics', 
                [], [], 
                '''                ''',
                'cnfexportstatistics',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfExportTemplate', REFERENCE_CLASS, 'CnfExportTemplate' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfExportTemplate', 
                [], [], 
                '''                ''',
                'cnfexporttemplate',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfProtocolStatistics', REFERENCE_CLASS, 'CnfProtocolStatistics' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfProtocolStatistics', 
                [], [], 
                '''                ''',
                'cnfprotocolstatistics',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfPSProtocolStatTable', REFERENCE_CLASS, 'CnfPSProtocolStatTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfPSProtocolStatTable', 
                [], [], 
                '''                A table containing statistics per protocol.
                Information sorted in this table is global in nature (i.e. it's
                updated for all line cards where netflow is enabled) and
                follows the Counter64 semantics as described in RFC 2578.
                ''',
                'cnfpsprotocolstattable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateExportInfoTable', REFERENCE_CLASS, 'CnfTemplateExportInfoTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTemplateExportInfoTable', 
                [], [], 
                '''                A control table providing information about version 9.
                ''',
                'cnftemplateexportinfotable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTemplateTable', REFERENCE_CLASS, 'CnfTemplateTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTemplateTable', 
                [], [], 
                '''                A control table to provide statistics of version 9
                Flow and Option templates.
                ''',
                'cnftemplatetable',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlows', REFERENCE_CLASS, 'CnfTopFlows' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTopFlows', 
                [], [], 
                '''                ''',
                'cnftopflows',
                'CISCO-NETFLOW-MIB', False),
            _MetaInfoClassMember('cnfTopFlowsTable', REFERENCE_CLASS, 'CnfTopFlowsTable' , 'ydk.models.netflow.CISCO_NETFLOW_MIB', 'CISCONETFLOWMIB.CnfTopFlowsTable', 
                [], [], 
                '''                Table of flows which have accrued the highest packets or bytes.
                Each row in the table represents one flow from the cache.
                ''',
                'cnftopflowstable',
                'CISCO-NETFLOW-MIB', False),
            ],
            'CISCO-NETFLOW-MIB',
            'CISCO-NETFLOW-MIB',
            _yang_ns._namespaces['CISCO-NETFLOW-MIB'],
        'ydk.models.netflow.CISCO_NETFLOW_MIB'
        ),
    },
}
_meta_table['CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable.CnfCIBridgedFlowStatsCtrlEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfCICacheTable.CnfCICacheEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfCICacheTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfCIInterfaceTable.CnfCIInterfaceEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfCIInterfaceTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfEICollectorTable.CnfEICollectorEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfEICollectorTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfEIExportInfoTable.CnfEIExportInfoEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfEIExportInfoTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfPSProtocolStatTable.CnfPSProtocolStatEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfPSProtocolStatTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTemplateExportInfoTable.CnfTemplateExportInfoEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfTemplateExportInfoTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTemplateTable.CnfTemplateEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfTemplateTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTopFlowsTable.CnfTopFlowsTableEntry']['meta_info'].parent =_meta_table['CISCONETFLOWMIB.CnfTopFlowsTable']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfCIBridgedFlowStatsCtrlTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfCICacheTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfCIInterfaceTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfCacheInfo']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfEICollectorTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfEIExportInfoTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfExportInfo']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfExportStatistics']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfExportTemplate']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfPSProtocolStatTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfProtocolStatistics']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTemplateExportInfoTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTemplateTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTopFlows']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
_meta_table['CISCONETFLOWMIB.CnfTopFlowsTable']['meta_info'].parent =_meta_table['CISCONETFLOWMIB']['meta_info']
