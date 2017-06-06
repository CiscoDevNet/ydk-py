


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscopddatatypeEnum' : _MetaInfoEnum('CiscopddatatypeEnum', 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB',
        {
            'bitRateIn':'bitRateIn',
            'bitRateOut':'bitRateOut',
            'bitRateSum':'bitRateSum',
            'byteCountIn':'byteCountIn',
            'byteCountOut':'byteCountOut',
            'byteCountSum':'byteCountSum',
            'packetCountIn':'packetCountIn',
            'packetCountOut':'packetCountOut',
            'packetCountSum':'packetCountSum',
        }, 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB']),
    'CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig',
            False, 
            [
            _MetaInfoClassMember('cnpdNotificationsEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is used to enable or disable 
                Notifications on a global basis. 
                
                If set to 'true' - Notifications are
                enabled.
                If set to 'false' - Notifications are
                disabled.
                ''',
                'cnpdnotificationsenable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdNotificationsConfig',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdStatusLastUpdateTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time Protocol 
                Discovery was last enabled  on an interface.
                If the interface does not have Protocol
                Discovery enabled this value is zero.
                ''',
                'cnpdstatuslastupdatetime',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdStatusPdEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is used to enable or disable 
                Protocol Discovery on an interface. 
                
                If set to 'true' - Protocol Discovery is 
                enabled on this Interface. 
                If set to 'false' - Protocol Discovery is 
                disabled on this Interface.
                ''',
                'cnpdstatuspdenable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdStatusEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdstatustable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdstatustable',
            False, 
            [
            _MetaInfoClassMember('cnpdStatusEntry', REFERENCE_LIST, 'Cnpdstatusentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry', 
                [], [], 
                '''                An entry in the cnpdStatusTable contains objects
                for enabling or disabling Protocol Discovery on a
                per interface basis.
                ''',
                'cnpdstatusentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdStatusTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdAllStatsProtocolsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '1024')], [], 
                '''                An object which represents a unique 
                identifier for a protocol or application 
                which NBAR currently recognizes.
                
                This object is an index into the 
                SupportedProtocolsTable where details
                of the protocol can be found.
                ''',
                'cnpdallstatsprotocolsindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdAllStatsHCInBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The byte count of inbound octets as 
                determined by Protocol Discovery.
                This is the 64-bit (High Capacity)
                version of cnpdAllStatsInBytes.
                ''',
                'cnpdallstatshcinbytes',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsHCInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The packet count of inbound packets as 
                determined by Protocol Discovery.
                This is the 64-bit (High Capacity)
                version of cnpdAllStatsInPkts.
                ''',
                'cnpdallstatshcinpkts',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsHCOutBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The byte count of outbound octets as 
                determined by Protocol Discovery.
                This is the 64-bit (High Capacity)
                version of cnpdAllStatsOutBytes.
                ''',
                'cnpdallstatshcoutbytes',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsHCOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The packet count of outbound packets as 
                determined by Protocol Discovery.
                This is the 64-bit (High Capacity)
                version of cnpdAllStatsOutPkts.
                ''',
                'cnpdallstatshcoutpkts',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsInBitRate', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The inbound bit rate as determined 
                by Protocol Discovery.
                ''',
                'cnpdallstatsinbitrate',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsInBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The byte count of inbound octets as 
                determined by Protocol Discovery.
                ''',
                'cnpdallstatsinbytes',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The packet count of inbound packets as 
                determined by Protocol Discovery.
                ''',
                'cnpdallstatsinpkts',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsOutBitRate', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The outbound bit rate as determined 
                by Protocol Discovery.
                ''',
                'cnpdallstatsoutbitrate',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsOutBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The byte count of outbound octets as
                determined by Protocol Discovery.
                ''',
                'cnpdallstatsoutbytes',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The packet count of outbound packets as 
                determined by Protocol Discovery.
                ''',
                'cnpdallstatsoutpkts',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdAllStatsProtocolName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Name of the application or protocol, a 
                unique textual string, assigned in the
                cnpdSupportedProtocolsTable.
                ''',
                'cnpdallstatsprotocolname',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdAllStatsEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable',
            False, 
            [
            _MetaInfoClassMember('cnpdAllStatsEntry', REFERENCE_LIST, 'Cnpdallstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry', 
                [], [], 
                '''                An entry in the cnpdAllStatsTable table. This entry 
                contains the statistics collected on all the protocols 
                which NBAR classifies for a particular interface.
                ''',
                'cnpdallstatsentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdAllStatsTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry',
            False, 
            [
            _MetaInfoClassMember('cnpdTopNConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                A monotonically increasing integer which
                uniquely identifies a cnpdTopNConfigEntry 
                in the cnpdTopNConfigTable.
                ''',
                'cnpdtopnconfigindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdTopNConfigGrantedSize', ATTRIBUTE, 'int' , None, None, 
                [('1', '500')], [], 
                '''                The actual size of the associated 	
                cnpdTopNStatsTable entry.
                
                The reason this may differ from 
                cnpdTopNConfigRequestedSize is because a 
                management station may request a number of 
                protocols that is greater than the number of 
                protocols actually found by Protocol Discovery.
                ''',
                'cnpdtopnconfiggrantedsize',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object allows the management station
                to select the interface, which Protocol Discovery
                is running on, to be used to create this 
                cnpdTopNConfigEntry.
                ''',
                'cnpdtopnconfigifindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigRequestedSize', ATTRIBUTE, 'int' , None, None, 
                [('1', '500')], [], 
                '''                The requested size of the associated 
                cnpdTopNStatsTable entry.
                
                For example a cnpdTopNConfigRequestedSize of
                20 indicates the management station wants
                to create an associated  cnpdTopNStatsTable 
                entry of 20 protocol/application's
                ''',
                'cnpdtopnconfigrequestedsize',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigSampleTime', ATTRIBUTE, 'int' , None, None, 
                [('1', '2048')], [], 
                '''                If the cnpdTopNConfigStatsSelect is
                bitRateIn, bitRateOut or bitRateSum, then
                this value is the interval in seconds that 
                the bitrate is sampled.
                
                This has no effect if the cnpdTopNConfigStatsSelect
                is byte or packet based.
                
                When this object is modified by the management 
                station, a new sample period is started regardless
                of whether the original cnpdTopNConfigSampleTime
                was finished.
                ''',
                'cnpdtopnconfigsampletime',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigStatsSelect', REFERENCE_ENUM_CLASS, 'CiscopddatatypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscopddatatypeEnum', 
                [], [], 
                '''                This object allows the management station to
                select the statistic used to base the order
                of the top-n table on.
                
                For example: a cnpdTopNConfigStatsSelect of
                bitRateSum means order this table based
                on each applications/protocols combined
                in and out bitrate.
                ''',
                'cnpdtopnconfigstatsselect',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create or delete 
                the row entry in cnpdTopNConfigTable.
                
                When creating a row entry the management
                station is required to specify a value
                for cnpdTopNConfigIfIndex only.
                
                'notReady' means that a row exists but 
                either it has no valid IfIndex or it has 
                not been set to createAndGo or active.
                
                'active' means that a createAndGo or active 
                has been issued, AND a valid ifIndex exists. 
                Therefore if a row is 'active' it means a 
                TopNStats entry has been generated.
                
                If you set an 'active' row to createAndWait 
                it will get the status 'notReady'. 
                
                If you set any row to 'notReady' - it will go 
                to the 'notReadystate'.
                
                If you set any row to 'notInService' - it will 
                go to the 'notInService' state and the corresponding 
                TopNStatsEntry will be deleted.
                
                The same TopNConfig entry can be re-used without 
                changes by setting it to 'active'. The corresponding 
                TopStatsTable entry will be regenerated. This can 
                be used by the NMS to poll a particular TopNConfig 
                Entry.
                
                Changes to an existing TopNConfig entry can be made
                by setting the status to 'createAndWait' and changing
                the necessary objects. Setting it to 'createAndGo' or
                'active' will cause the corresponding TopNStats entry
                to be regenerated.
                ''',
                'cnpdtopnconfigstatus',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the associated
                cnpdTopNStatsTable entry was created.
                ''',
                'cnpdtopnconfigtime',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdTopNConfigEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable',
            False, 
            [
            _MetaInfoClassMember('cnpdTopNConfigEntry', REFERENCE_LIST, 'Cnpdtopnconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry', 
                [], [], 
                '''                This entry provides the objects to configure and thus
                initiate the generation of a cnpdTopNStatsTable..
                ''',
                'cnpdtopnconfigentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdTopNConfigTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry',
            False, 
            [
            _MetaInfoClassMember('cnpdTopNConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                ''',
                'cnpdtopnconfigindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdTopNStatsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '500')], [], 
                '''                A monotonically increasing integer which 
                uniquely identifies a cnpdTopNStatsEntry 
                in the cnpdTopNStatsTable.
                ''',
                'cnpdtopnstatsindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdTopNStatsHCRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The amount of change in the selected statistic
                during this sampling interval. The selected
                statistic is the cnpdTopNConfigStatsSelect
                from the associated cnpdTopNConfigStatsEntry.	
                
                This is the 64-bit (High Capacity) version of 
                cnpdTopNStatsRate.
                ''',
                'cnpdtopnstatshcrate',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNStatsProtocolName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Name of the application or protocol, 
                a unique textual string, assigned in the
                cnpdSupportedProtocolsTable.
                ''',
                'cnpdtopnstatsprotocolname',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNStatsRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The amount of change in the selected statistic
                during this sampling interval. The selected
                statistic is the cnpdTopNConfigStatsSelect
                from the associated cnpdTopNConfigStatsEntry.
                ''',
                'cnpdtopnstatsrate',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdTopNStatsEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable',
            False, 
            [
            _MetaInfoClassMember('cnpdTopNStatsEntry', REFERENCE_LIST, 'Cnpdtopnstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry', 
                [], [], 
                '''                This entry is used to store a set of objects which 
                describe a cnpdTopNStatsTable. A cnpdTopNStatsTable 
                is a number of protocols and statistics sorted 
                according to the criteria in the associated
                cnpdTopNConfigEntry.
                
                Therefore a cnpdTopNStatsTable can differ in content 
                and size according to what was configured in the associated
                cnpdTopNConfigTableEntry.
                ''',
                'cnpdtopnstatsentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdTopNStatsTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.CnpdthresholdconfigsampletypeEnum' : _MetaInfoEnum('CnpdthresholdconfigsampletypeEnum', 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB',
        {
            'absoluteValue':'absoluteValue',
            'deltaValue':'deltaValue',
        }, 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB']),
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.CnpdthresholdconfigstartupEnum' : _MetaInfoEnum('CnpdthresholdconfigstartupEnum', 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB',
        {
            'rising':'rising',
            'falling':'falling',
            'risingOrFalling':'risingOrFalling',
        }, 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB']),
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry',
            False, 
            [
            _MetaInfoClassMember('cnpdThresholdConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                A monotonically increasing integer which 
                uniquely identifies an entry in the 
                cnpdThresholdConfigTable.
                ''',
                'cnpdthresholdconfigindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdThresholdConfigFalling', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This is the threshold object which the management 
                station sets to determine if it gets breached. It 
                indicates the statistic being sampled was
                falling. 
                
                When current sample is less than or equal 
                to this object, and the value at the last sampling
                interval was greater than this object (in other 
                words the value is falling), an entry in the 
                cnpdThresholdHistoryTable will be created. 
                		
                After a falling event is generated, another 
                such event will not be generated until the sampled 
                value rises above this object and reaches the
                cnpdThresholdConfigRising value.
                ''',
                'cnpdthresholdconfigfalling',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object allows the management station to 
                select the interface, which Protocol Discovery is 
                running on, to be used to create this 
                cnpdThresholdConfigTable entry.
                ''',
                'cnpdthresholdconfigifindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '2048')], [], 
                '''                The interval in seconds over which the data is
                sampled and compared with cnpdThresholdConfigRising
                and cnpdThresholdConfigFalling thresholds.
                ''',
                'cnpdthresholdconfiginterval',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '1024')], [], 
                '''                The application or protocol which the
                management station wishes to configure a
                threshold on.
                
                This object is an index into the 
                SupportedProtocolsTable where details
                of the protocol can be found.
                
                If cnpdThresholdConfigProtocolAny is set
                to TRUE this value will be ignored. If it
                is set to FALSE, then cnpdThresholdConfigProtocol
                will be the only protocol that is checked
                to see if it has breached the threshold.
                ''',
                'cnpdthresholdconfigprotocol',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigProtocolAny', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to 'true' - this threshold is configured
                to check for any protocol which meets the threshold
                criteria. This means that multiple protocols can
                generate ThresholdHistoryTable entries. Each
                protocol is subject to the hysterisis mechanism.
                
                If set to 'false' - this threshold is configured
                to check for the protocol which meets the threshold
                criteria referred to by cnpdThresholdConfigProtocol.
                ''',
                'cnpdthresholdconfigprotocolany',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigRising', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This is the threshold object which the managment
                station sets to determine if it gets breached. It 
                indicates the statistic being sampled was
                rising.
                
                When the current sample is greater than or 
                equal to this object, and the value at the last 
                sampling interval was less than this object (in 
                other words the value is rising), an entry in the 
                cnpdThresholdHistoryTable will be created.
                
                After a rising event is generated, another such 
                event will not be generated until the sampled value
                falls below this threshold and reaches the
                cnpdThresholdConfigFalling value.
                
                This ensures that samples which are taken
                after a cnpdThresholdConfigRising threshold event
                has been created, do not create further thresholds
                and therefore notifications, until the 
                cnpdThresholdConfigFalling threshold has been met.
                
                Thus a very short cnpdThresholdConfigInterval can be
                chosen without risk of multiple notifications for
                the same threshold breach condition.
                ''',
                'cnpdthresholdconfigrising',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigSampleType', REFERENCE_ENUM_CLASS, 'CnpdthresholdconfigsampletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.CnpdthresholdconfigsampletypeEnum', 
                [], [], 
                '''                The method of sampling the selected statistic and
                calculating the value to be compared against 
                cnpdThresholdConfigRising or 
                cnpdThresholdConfigFalling thresholds. 
                		
                If the value of this object is absoluteValue(1), 
                the value at the end of the sampling interval 
                cnpdThresholdConfigInterval, will be compared 
                with the cnpdThresholdConfigRising and 
                cnpdThresholdConfigFalling thresholds. 
                
                In this mode, when cnpdThresholdConfigStatsSelect is
                byte or packet based, a maximum of two 
                cnpdThresholdHistory entries will be created per
                application, as these byte and packet counts 
                monotonically increase from zero.
                		
                If the value of this object is deltaValue(2), 
                the difference between the samples at the 
                beginning and end of the cnpdThresholdConfigInterval 
                will be compared with the cnpdThresholdConfigRising 
                and cnpdThresholdConfigFalling thresholds.
                		
                Because the difference in the previous and current
                samples are compared over the sample period
                cnpdThresholdConfigInterval, this mode provides 
                more granularity to the thresholds because the NMS 
                is now provided with the gradient or change in the 
                cnpdThresholdConfigStatsSelect.
                
                Note that even though the sample value is monotonically
                increasing for byte and packet counts, 
                cnpdThresholdConfigSampleType set to deltaValue, can 
                generate falling cnpdThresholdHistory entries, because
                the gradient can be lower than the 
                cnpdThresholdConfigFalling value.
                ''',
                'cnpdthresholdconfigsampletype',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigStartup', REFERENCE_ENUM_CLASS, 'CnpdthresholdconfigstartupEnum' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry.CnpdthresholdconfigstartupEnum', 
                [], [], 
                '''                This controls the type of notification that is 
                sent when this threshold entry is first enabled. 
                
                Because there is no previous sampling history,
                choosing one of these options determines the type
                of notification generated - Rising or Falling.
                
                If the first sample after this entry is enabled 
                is greater than or equal to cnpdThresholdConfigRising and
                this object is equal to rising(1) or risingOrFalling(3), 
                then a single rising notification will be generated. 
                
                If the first sample after this entry is enabled
                is less than or equal to cnpdThresholdConfigFalling
                and this object is equal to falling(2) or 
                risingOrFalling(3), then a single falling notification 
                will be generated.
                ''',
                'cnpdthresholdconfigstartup',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigStatsSelect', REFERENCE_ENUM_CLASS, 'CiscopddatatypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscopddatatypeEnum', 
                [], [], 
                '''                This object allows the management station to
                select the statistic used to base the threshold
                on.
                
                For example a cnpdThresholdConfigStatsSelect of
                bitRateSum means cnpdThresholdConfigRising and
                cnpdThresholdConfigFalling are values based on
                the combined value of in and out bitrates.
                ''',
                'cnpdthresholdconfigstatsselect',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create or delete 
                the row entry in cnpdThresholdConfigTable.
                 
                When creating a row entry the management station 
                is required to specify a value for 
                cnpdThresholdConfigIfIndex, cnpdThresholdConfigRising 
                and cnpdThresholdConfigFalling.
                
                'active' means that a createAndGo or active has 
                been issued, AND a valid ifIndex exists. And therefore 
                if a row is 'active' it means a ThresholdHistory entry 
                may have been generated if the value was breached.
                
                If you set an 'active' row to 'createAndWait' - it will 
                in fact get the status 'notReady'. 
                
                Likewise if you set any row to 'notInService' or 'notReady' 
                it will go to the 'notReady' state.
                ''',
                'cnpdthresholdconfigstatus',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdThresholdConfigEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable',
            False, 
            [
            _MetaInfoClassMember('cnpdThresholdConfigEntry', REFERENCE_LIST, 'Cnpdthresholdconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry', 
                [], [], 
                '''                This entry contains configuration information to 
                set thresholds for the purpose of notifications.
                
                The management station is allowed to set thresholds
                on individual statistics for individual protocols
                on an interface. If the threshold is breached by
                the protocol statistic, a new event is written to
                the cnpdThresholdHistoryTable, which in turn will 
                generate a Notification Event.
                
                This function has a hysteresis mechanism to limit
                the generation of events. This mechanism generates
                one event as a threshold is crossed in the
                appropriate direction. No more events are generated
                for that threshold until the opposite threshold is
                crossed. This stops repeated Notification events
                being generated each time the value is sampled,
                when the value is above the threshold. Instead one
                notification is sent when the threshold is breached
                and one notification when the statistic drops below
                the threshold value again.
                ''',
                'cnpdthresholdconfigentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdThresholdConfigTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry.CnpdthresholdhistorytypeEnum' : _MetaInfoEnum('CnpdthresholdhistorytypeEnum', 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB',
        {
            'risingBreach':'risingBreach',
            'fallingBreach':'fallingBreach',
        }, 'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB']),
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry',
            False, 
            [
            _MetaInfoClassMember('cnpdThresholdHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                A monotonically increasing integer
                which uniquely identifies this 
                cnpdThresholdHistoryEntry in the 
                cnpdThresholdHistory table.
                ''',
                'cnpdthresholdhistoryindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdThresholdHistoryConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                The cnpdThresholdConfigTable entry 
                which generated this entry. Using this 
                object the management station can backtrack 
                to the appropriate cnpdThresholdConfigEntry.
                ''',
                'cnpdthresholdhistoryconfigindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdHistoryProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '1024')], [], 
                '''                The application or protocol which the
                management station configured a
                threshold on.
                
                This object is an index into the 
                SupportedProtocolsTable where details
                of the protocol can be found.
                ''',
                'cnpdthresholdhistoryprotocol',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdHistoryStatsSelect', REFERENCE_ENUM_CLASS, 'CiscopddatatypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscopddatatypeEnum', 
                [], [], 
                '''                This is the statistic used to base the threshold
                on.
                ''',
                'cnpdthresholdhistorystatsselect',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdHistoryTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime of the running 
                configuration when the event occurred.
                ''',
                'cnpdthresholdhistorytime',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdHistoryType', REFERENCE_ENUM_CLASS, 'CnpdthresholdhistorytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry.CnpdthresholdhistorytypeEnum', 
                [], [], 
                '''                Describes whether this is an
                event caused by a rising
                or falling threshold breach.
                ''',
                'cnpdthresholdhistorytype',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdHistoryValue', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The actual value of the statistic when 
                the sampling was made.
                ''',
                'cnpdthresholdhistoryvalue',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdThresholdHistoryEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable',
            False, 
            [
            _MetaInfoClassMember('cnpdThresholdHistoryEntry', REFERENCE_LIST, 'Cnpdthresholdhistoryentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry', 
                [], [], 
                '''                This entry is created each time a threshold 
                is breached. 
                
                Thus there is not necessarily a one to one 
                relationship to cnpdThresholdConfigTable 
                as not every Threshold configured will 
                be breached.
                ''',
                'cnpdthresholdhistoryentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdThresholdHistoryTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry',
            False, 
            [
            _MetaInfoClassMember('cnpdSupportedProtocolsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '1024')], [], 
                '''                A unique identifier of a row in this table.
                
                Thus it also represents a unique identifier for a
                protocol or application which NBAR currently
                recognizes.
                ''',
                'cnpdsupportedprotocolsindex',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', True),
            _MetaInfoClassMember('cnpdSupportedProtocolsName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object reflects the valid string of a
                protocol or application which NBAR currently
                recognizes.
                ''',
                'cnpdsupportedprotocolsname',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdSupportedProtocolsEntry',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable',
            False, 
            [
            _MetaInfoClassMember('cnpdSupportedProtocolsEntry', REFERENCE_LIST, 'Cnpdsupportedprotocolsentry' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry', 
                [], [], 
                '''                A entry in the Supported Protocols table reflecting
                key information about a protocol.
                ''',
                'cnpdsupportedprotocolsentry',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'cnpdSupportedProtocolsTable',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
    'CiscoNbarProtocolDiscoveryMib' : {
        'meta_info' : _MetaInfoClass('CiscoNbarProtocolDiscoveryMib',
            False, 
            [
            _MetaInfoClassMember('cnpdAllStatsTable', REFERENCE_CLASS, 'Cnpdallstatstable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable', 
                [], [], 
                '''                The cnpdAllStatsTable contains all the statistics
                available for all the protocols/applications currently
                recognized by NBAR Protocol Discovery for a particular 
                interface.
                
                In the event of an overflow, the 32 bit counters are not 
                valid. There is no overflow support.
                ''',
                'cnpdallstatstable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdNotificationsConfig', REFERENCE_CLASS, 'Cnpdnotificationsconfig' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig', 
                [], [], 
                '''                ''',
                'cnpdnotificationsconfig',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdStatusTable', REFERENCE_CLASS, 'Cnpdstatustable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdstatustable', 
                [], [], 
                '''                The cnpdStatusTable is used to enable and
                disable Protocol Discovery on an interface.
                ''',
                'cnpdstatustable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdSupportedProtocolsTable', REFERENCE_CLASS, 'Cnpdsupportedprotocolstable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable', 
                [], [], 
                '''                The Supported Protocols table lists all the 
                protocols and applications which NBAR is currently
                capable of recognizing.
                ''',
                'cnpdsupportedprotocolstable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdConfigTable', REFERENCE_CLASS, 'Cnpdthresholdconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable', 
                [], [], 
                '''                The cnpdThresholdConfigTable allows the management
                station to create thresholds for the purpose of
                sending notifications if breached, and creating a
                history of breached thresholds.
                ''',
                'cnpdthresholdconfigtable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdThresholdHistoryTable', REFERENCE_CLASS, 'Cnpdthresholdhistorytable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable', 
                [], [], 
                '''                The Threshold History table. Notifications
                are unreliable so this table provides a
                history of the last 5000 threshold breached
                events. A notification can be traced back to
                its cnpdThresholdHistoryEntry.
                ''',
                'cnpdthresholdhistorytable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNConfigTable', REFERENCE_CLASS, 'Cnpdtopnconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable', 
                [], [], 
                '''                The cnpdTopNConfigTable is used to configure
                cnpdTopNStatsTable's.
                ''',
                'cnpdtopnconfigtable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            _MetaInfoClassMember('cnpdTopNStatsTable', REFERENCE_CLASS, 'Cnpdtopnstatstable' , 'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB', 'CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable', 
                [], [], 
                '''                A cnpdTopNStatsTable describes an ordered
                list of protocols.
                ''',
                'cnpdtopnstatstable',
                'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB', False),
            ],
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            'CISCO-NBAR-PROTOCOL-DISCOVERY-MIB',
            _yang_ns._namespaces['CISCO-NBAR-PROTOCOL-DISCOVERY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_NBAR_PROTOCOL_DISCOVERY_MIB'
        ),
    },
}
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdstatustable.Cnpdstatusentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdstatustable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable.Cnpdallstatsentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable.Cnpdtopnconfigentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable.Cnpdtopnstatsentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable.Cnpdthresholdconfigentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable.Cnpdthresholdhistoryentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable.Cnpdsupportedprotocolsentry']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdnotificationsconfig']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdstatustable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdallstatstable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdtopnconfigtable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdtopnstatstable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdthresholdconfigtable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdthresholdhistorytable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
_meta_table['CiscoNbarProtocolDiscoveryMib.Cnpdsupportedprotocolstable']['meta_info'].parent =_meta_table['CiscoNbarProtocolDiscoveryMib']['meta_info']
