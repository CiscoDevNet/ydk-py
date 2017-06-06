


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry.CpwvcenetvlanmodeEnum' : _MetaInfoEnum('CpwvcenetvlanmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB',
        {
            'other':'other',
            'portBased':'portBased',
            'noChange':'noChange',
            'changeVlan':'changeVlan',
            'addVlan':'addVlan',
            'removeVlan':'removeVlan',
        }, 'CISCO-IETF-PW-ENET-MIB', _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB']),
    'CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-ENET-MIB', True),
            _MetaInfoClassMember('cpwVcEnetPwVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4097')], [], 
                '''                This Object defines the VLAN on the VC. The value of 4097 
                is used if the object is not applicable, for example when 
                mapping all packets from an Ethernet port to this VC. 
                The value of 4096 is used to indicate untagged frames (at  
                least from the PW point of view), for example if  
                cpwVcEnetVlanMode is equal 'removeVLAN' or when  
                cpwVcEnetVlanMode equal 'noChange' and cpwVcEnetPortVlan 
                is equal 4096.
                ''',
                'cpwvcenetpwvlan',
                'CISCO-IETF-PW-ENET-MIB', True),
            _MetaInfoClassMember('cpwVcEnetPortIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object is used to specify the ifIndex of the ETHERNET 
                port associated with this VC for point-to-point Ethernet  
                service, or the ifIndex of the virtual interface of the VPLS  
                instance associated with the PW if the service is VPLS. Two  
                rows in this table can point to the same ifIndex only if: 
                
                1) It is required to support multiple COS on a MPLS PSN  
                   for the same service (i.e.: a combination of ports and  
                   VLANs) by the use of multiple VC, each with a different 
                   COS. 
                
                2) There is no overlap of VLAN values specified in  
                   cpwVcEnetPortVlan that are associated with this port. 
                
                A value of zero indicate that association to an ifIndex is 
                not yet known.
                ''',
                'cpwvcenetportifindex',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetPortVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4097')], [], 
                '''                This object define the VLAN value on the physical port (or  
                VPLS virtual port) if a change is required to the VLAN value 
                between the VC and the physical/virtual port. 
                
                The value of this object can be ignored if the whole traffic  
                from the port is forwarded to one VC independent of the  
                tagging on the port, but it is RECOMENDED that the value in 
                this case will be '4097' indicating not relevant. 
                
                It MUST be equal to cpwVcEnetPwVlan if 'noChange' mode 
                is used. 
                
                The value 4096 indicate that no VLAN (i.e. untagged  
                frames) on the port are associated to this VC. This  
                allows the same behaviors as assigning 'Default VLAN'  
                to un-tagged frames. 
                ''',
                'cpwvcenetportvlan',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                Enable creating, deleting and modifying this row.
                ''',
                'cpwvcenetrowstatus',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                Indicates the storage type of this row.
                ''',
                'cpwvcenetstoragetype',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetVcIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                It is sometimes convenient to model the VC PW as a  
                virtual interface in the ifTable. In these cases this  
                object hold the value of the ifIndex in the ifTable  
                representing this VC PW. A value of zero indicate no such  
                association or association is not yet known.
                ''',
                'cpwvcenetvcifindex',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetVlanMode', REFERENCE_ENUM_CLASS, 'CpwvcenetvlanmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry.CpwvcenetvlanmodeEnum', 
                [], [], 
                '''                Indicate the mode of VLAN handling between the port  
                associated to the VC and the VC encapsulation itself. 
                
                - 'other' indicate operation that is not defined by 
                  this MIB. 
                
                - 'portBased' indicates that the forwarder will forward 
                  packets between the port and the PW independent of their 
                  structure. 
                
                - 'noChange' indicates that the VC contains the original 
                   user VLAN, as specified in cpwVcEnetPortVlan. 
                
                - 'changeVlan' indicates that the VLAN field on the VC  
                  may be different than the VLAN field on the user's  
                  port. 
                
                - 'removeVlan' indicates that the encapsulation on the  
                  VC does not include the original VLAN field. Note  
                  that PRI bits transparency is lost in this case. 
                
                - 'addVlan' indicate that a VLAN field will be added 
                  on the PSN bound direction. cpwVcEnetPwVlan indicate 
                  the value that will be added.  
                
                - 'removeVlan', 'addVlan' and 'changeVlan' implementation 
                  is not required. 
                ''',
                'cpwvcenetvlanmode',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'cpwVcEnetEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
    'CiscoIetfPwEnetMib.Cpwvcenettable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib.Cpwvcenettable',
            False, 
            [
            _MetaInfoClassMember('cpwVcEnetEntry', REFERENCE_LIST, 'Cpwvcenetentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry', 
                [], [], 
                '''                This table is indexed by the same index that was created  
                for the associated entry in the PW VC Table in the 
                CISCO-IETF-PW-MIB.  The CpwVcIndex and the cpwVcEnetPwVlan 
                are used as indexes to allow multiple VLANs to exist on 
                the same PW. 
                
                An entry is created in this table by the agent for every  
                entry in the cpwVc table with a VcType of 'ethernetVLAN', 
                'ethernet' or 'ethernetVPLS'. Additional rows may be  
                created by the operator or the agent if multiple entries 
                are required for the same VC. 
                
                This table provides Ethernet port mapping and VLAN  
                configuration for each Ethernet VC.
                ''',
                'cpwvcenetentry',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'cpwVcEnetTable',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
    'CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-ENET-MIB', True),
            _MetaInfoClassMember('cpwVcEnetMplsPriMapping', REFERENCE_BITS, 'Cpwvcenetmplsprimapping' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry.Cpwvcenetmplsprimapping', 
                [], [], 
                '''                This object defines the groups of user PRI mapped into 
                this VC. Each bit set indicates that this user priority  
                is assigned to this VC. 
                
                The value 'untagged' is used to indicate that untagged  
                frames are also associated to this VC. 
                
                This object allow the use of different PSN COS based on  
                user marking of PRI bits in MPLS PSN with L-LSP or  
                E-LSP without multiple COS support. In all other cases,  
                the default value MUST be used. 
                
                It is REQUIRED that there is no overlap on this object  
                between rows serving the same service (port+ PW VLAN). 
                
                In case of missing BIT configuration between rows to  
                the same service, incoming packets with PRI marking not  
                configured should be handled by the VC with the lowest  
                COS. 
                ''',
                'cpwvcenetmplsprimapping',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetMplsPriMappingRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                Enable creating, deleting and modifying this row.
                ''',
                'cpwvcenetmplsprimappingrowstatus',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetMplsPriMappingStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                Indicates the storage type of this row.
                ''',
                'cpwvcenetmplsprimappingstoragetype',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'cpwVcEnetMplsPriMappingTableEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
    'CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcEnetMplsPriMappingTableEntry', REFERENCE_LIST, 'Cpwvcenetmplsprimappingtableentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry', 
                [], [], 
                '''                Each entry is created if special classification based on  
                the PRI bits is required for this VC.
                ''',
                'cpwvcenetmplsprimappingtableentry',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'cpwVcEnetMplsPriMappingTable',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
    'CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-ENET-MIB', True),
            _MetaInfoClassMember('cpwVcEnetStatsIllegalLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets that were received with an illegal  
                Ethernet packet length on this VC. An illegal length is defined 
                as being greater than the value in the advertised maximum MTU  
                supported, or shorter than the allowed Ethernet packet size.
                ''',
                'cpwvcenetstatsillegallength',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetStatsIllegalVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets received (from the PSN) on this VC with  
                an illegal VLAN field, missing VLAN field that was expected, or  
                A VLAN field when it was not expected. This counter is not  
                relevant if the VC type is 'ethernet' (i.e. raw mode), and  
                should be set to 0 by the agent to indicate this.
                ''',
                'cpwvcenetstatsillegalvlan',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'cpwVcEnetStatsEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
    'CiscoIetfPwEnetMib.Cpwvcenetstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib.Cpwvcenetstatstable',
            False, 
            [
            _MetaInfoClassMember('cpwVcEnetStatsEntry', REFERENCE_LIST, 'Cpwvcenetstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry', 
                [], [], 
                '''                Each entry represents the statistics gathered for the  
                VC carrying the Ethernet packets since this VC was  
                first created in the cpwVcEnetTable.
                ''',
                'cpwvcenetstatsentry',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'cpwVcEnetStatsTable',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
    'CiscoIetfPwEnetMib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwEnetMib',
            False, 
            [
            _MetaInfoClassMember('cpwVcEnetMplsPriMappingTable', REFERENCE_CLASS, 'Cpwvcenetmplsprimappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable', 
                [], [], 
                '''                This table may be used for MPLS PSNs if there is a need  
                to hold multiple VC, each with different COS, for the same 
                user service (port + PW VLAN). Such a need may arise if the 
                MPLS network is capable of L-LSP or E-LSP without multiple 
                COS capabilities.  Each row is indexed by the cpwVcIndex  
                and indicate the PRI bits on the packet recieved from the  
                user port (or VPLS virtual port) that are 
                classified to this VC. Note that the EXP bit value of the VC 
                is configured in the CISCO-IETF-PW-MPLS-MIB.
                ''',
                'cpwvcenetmplsprimappingtable',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetStatsTable', REFERENCE_CLASS, 'Cpwvcenetstatstable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenetstatstable', 
                [], [], 
                '''                This table contains statistical counters specific for  
                Ethernet PW.
                ''',
                'cpwvcenetstatstable',
                'CISCO-IETF-PW-ENET-MIB', False),
            _MetaInfoClassMember('cpwVcEnetTable', REFERENCE_CLASS, 'Cpwvcenettable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB', 'CiscoIetfPwEnetMib.Cpwvcenettable', 
                [], [], 
                '''                This table contains the index to the Ethernet tables  
                associated with this ETH VC, the VLAN configuration and  
                VLAN mode.
                ''',
                'cpwvcenettable',
                'CISCO-IETF-PW-ENET-MIB', False),
            ],
            'CISCO-IETF-PW-ENET-MIB',
            'CISCO-IETF-PW-ENET-MIB',
            _yang_ns._namespaces['CISCO-IETF-PW-ENET-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ENET_MIB'
        ),
    },
}
_meta_table['CiscoIetfPwEnetMib.Cpwvcenettable.Cpwvcenetentry']['meta_info'].parent =_meta_table['CiscoIetfPwEnetMib.Cpwvcenettable']['meta_info']
_meta_table['CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable.Cpwvcenetmplsprimappingtableentry']['meta_info'].parent =_meta_table['CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable']['meta_info']
_meta_table['CiscoIetfPwEnetMib.Cpwvcenetstatstable.Cpwvcenetstatsentry']['meta_info'].parent =_meta_table['CiscoIetfPwEnetMib.Cpwvcenetstatstable']['meta_info']
_meta_table['CiscoIetfPwEnetMib.Cpwvcenettable']['meta_info'].parent =_meta_table['CiscoIetfPwEnetMib']['meta_info']
_meta_table['CiscoIetfPwEnetMib.Cpwvcenetmplsprimappingtable']['meta_info'].parent =_meta_table['CiscoIetfPwEnetMib']['meta_info']
_meta_table['CiscoIetfPwEnetMib.Cpwvcenetstatstable']['meta_info'].parent =_meta_table['CiscoIetfPwEnetMib']['meta_info']
