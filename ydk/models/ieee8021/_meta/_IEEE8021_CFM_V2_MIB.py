


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable.Ieee8021CfmConfigErrorListEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable.Ieee8021CfmConfigErrorListEntry',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmConfigErrorListIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object is the IfIndex of the interface.
                
                Upon a restart of the system, the system SHALL, if necessary,
                change the value of this variable so that it indexes the
                entry in the interface table with the same value of ifAlias
                that it indexed before the system restart.  If no such
                entry exists, then the system SHALL delete any entries in
                ieee8021CfmConfigErrorListTable indexed by that
                InterfaceIndex value.
                ''',
                'ieee8021cfmconfigerrorlistifindex',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmConfigErrorListSelector', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The Service Selector Identifier of the Service with interfaces
                in error. See IEEE8021ServiceSelectorValue for details.
                ''',
                'ieee8021cfmconfigerrorlistselector',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmConfigErrorListSelectorType', REFERENCE_ENUM_CLASS, 'IEEE8021ServiceSelectorType_Enum' , 'ydk.models.ieee8021.IEEE8021_TC_MIB', 'IEEE8021ServiceSelectorType_Enum', 
                [], [], 
                '''                Type of the Service Selector identifier indicated by
                ieee8021CfmConfigErrorListSelector. See textual 
                convention IEEE8021ServiceSelectorType for details.
                ''',
                'ieee8021cfmconfigerrorlistselectortype',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmConfigErrorListErrorType', REFERENCE_BITS, 'Dot1agCfmConfigErrors_Bits' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmConfigErrors_Bits', 
                [], [], 
                '''                A vector of Boolean error conditions from 22.2.4, any of
                which may be true:
                
                0) CFMleak;
                1) ConflictingVids;
                2) ExcessiveLevels;
                3) OverlappedLevels.
                ''',
                'ieee8021cfmconfigerrorlisterrortype',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmConfigErrorListEntry',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmConfigErrorListEntry', REFERENCE_LIST, 'Ieee8021CfmConfigErrorListEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable.Ieee8021CfmConfigErrorListEntry', 
                [], [], 
                '''                The Config Error List Table  entry
                ''',
                'ieee8021cfmconfigerrorlistentry',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmConfigErrorListTable',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable.Ieee8021CfmDefaultMdEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable.Ieee8021CfmDefaultMdEntry',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmDefaultMdComponentId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The bridge component within the system to which the information
                in this ieee8021CfmDefaultMdEntry applies.  If the system is not
                a Bridge, or if only one component is present in the Bridge,
                then this variable (index) MUST be equal to 1.
                ''',
                'ieee8021cfmdefaultmdcomponentid',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmDefaultMdPrimarySelector', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Primary Service Selector identifier of a Service Instance with 
                no MA configured. See IEEE8021ServiceSelectorValue for details.
                ''',
                'ieee8021cfmdefaultmdprimaryselector',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmDefaultMdPrimarySelectorType', REFERENCE_ENUM_CLASS, 'IEEE8021ServiceSelectorType_Enum' , 'ydk.models.ieee8021.IEEE8021_TC_MIB', 'IEEE8021ServiceSelectorType_Enum', 
                [], [], 
                '''                Type of the Primary Service Selector identifier indicated by 
                ieee8021CfmDefaultMdPrimarySelector. See textual
                convention IEEE8021ServiceSelectorType for details.
                ''',
                'ieee8021cfmdefaultmdprimaryselectortype',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmDefaultMdIdPermission', REFERENCE_ENUM_CLASS, 'Dot1agCfmIdPermission_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIdPermission_Enum', 
                [], [], 
                '''                Enumerated value indicating what, if anything, is to be
                included in the Sender ID TLV (21.5.3) transmitted by MHFs
                created by the Default Maintenance Domain.  If this object
                has the value sendIdDefer, Sender ID TLV transmission for
                this VLAN is controlled by ieee8021CfmDefaultMdDefIdPermission.
                
                The value of this variable is meaningless if the values of
                ieee8021CfmDefaultMdStatus is false.
                ''',
                'ieee8021cfmdefaultmdidpermission',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmDefaultMdLevel', ATTRIBUTE, 'int' , None, None, 
                [(-1, 7)], [], 
                '''                A value indicating the MD Level at which MHFs are to be
                created, and Sender ID TLV transmission by those MHFs is to
                be controlled, for the VLAN to which this entry's objects
                apply.  If this object has the value -1, the MD Level for MHF
                creation for this VLAN is controlled by
                ieee8021CfmDefaultMdDefLevel.
                ''',
                'ieee8021cfmdefaultmdlevel',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmDefaultMdMhfCreation', REFERENCE_ENUM_CLASS, 'Dot1agCfmMhfCreation_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMhfCreation_Enum', 
                [], [], 
                '''                A value indicating if the Management entity can create MHFs
                (MIP Half Function) for this VID at this MD Level.  If this
                object has the value defMHFdefer, MHF creation for this VLAN
                is controlled by ieee8021CfmDefaultMdDefMhfCreation.
                
                The value of this variable is meaningless if the values of
                ieee8021CfmDefaultMdStatus is false.
                ''',
                'ieee8021cfmdefaultmdmhfcreation',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmDefaultMdStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State of this Default MD Level table entry.  True if there is
                no entry in the Maintenance Association table defining an MA
                for the same VLAN ID and MD Level as this table's entry, and
                on which MA an Up MEP is defined, else false.
                ''',
                'ieee8021cfmdefaultmdstatus',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmDefaultMdEntry',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmDefaultMdEntry', REFERENCE_LIST, 'Ieee8021CfmDefaultMdEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable.Ieee8021CfmDefaultMdEntry', 
                [], [], 
                '''                The Default MD Level table entry.
                ''',
                'ieee8021cfmdefaultmdentry',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmDefaultMdTable',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable.Ieee8021CfmMaCompEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable.Ieee8021CfmMaCompEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmMaComponentId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The bridge component within the system to which the information
                in this ieee8021CfmMaCompEntry applies.  If the system is not a
                Bridge, or if only one component is present in the Bridge, then
                this variable (index) MUST be equal to 1.
                ''',
                'ieee8021cfmmacomponentid',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmMaCompIdPermission', REFERENCE_ENUM_CLASS, 'Dot1agCfmIdPermission_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIdPermission_Enum', 
                [], [], 
                '''                Enumerated value indicating what, if anything, is to be
                included in the Sender ID TLV (21.5.3) transmitted by MPs
                configured in this MA.
                ''',
                'ieee8021cfmmacompidpermission',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmMaCompMhfCreation', REFERENCE_ENUM_CLASS, 'Dot1agCfmMhfCreation_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMhfCreation_Enum', 
                [], [], 
                '''                Indicates if the Management entity can create MHFs (MIP Half
                Function) for this MA.
                ''',
                'ieee8021cfmmacompmhfcreation',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmMaCompNumberOfVids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of VIDs associated with the MA.
                ''',
                'ieee8021cfmmacompnumberofvids',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmMaCompPrimarySelectorOrNone', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Service Selector identifier to which the MP is attached, or 0, if none.
                If the MA is associated with more than one Service Selectors Identifiers, the
                ieee8021CfmVlanTable lists them.
                ''',
                'ieee8021cfmmacompprimaryselectorornone',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmMaCompPrimarySelectorType', REFERENCE_ENUM_CLASS, 'IEEE8021ServiceSelectorType_Enum' , 'ydk.models.ieee8021.IEEE8021_TC_MIB', 'IEEE8021ServiceSelectorType_Enum', 
                [], [], 
                '''                Type of the Service Selector identifiers indicated by 
                ieee8021CfmMaCompPrimarySelectorOrNone. If the service instance is defined by more 
                than one Service Selector, this parameter also indicates the type of the 
                ieee8021CfmVlanPrimarySelector and ieee8021CfmVlanSelector in the ieee8021CfmVlanTable. 
                In Services instances made of multiple Service Selector identifiers, ensures that the
                type of the Service selector identifiers is the same. See textual convention 
                Dot1agCfmServiceSelectorType for details.
                ''',
                'ieee8021cfmmacompprimaryselectortype',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmMaCompRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                ''',
                'ieee8021cfmmacomprowstatus',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmMaCompEntry',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmMaCompEntry', REFERENCE_LIST, 'Ieee8021CfmMaCompEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable.Ieee8021CfmMaCompEntry', 
                [], [], 
                '''                The MA table entry.
                ''',
                'ieee8021cfmmacompentry',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmMaCompTable',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmStackTable.Ieee8021CfmStackEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmStackTable.Ieee8021CfmStackEntry',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmStackDirection', REFERENCE_ENUM_CLASS, 'Dot1agCfmMpDirection_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMpDirection_Enum', 
                [], [], 
                '''                Direction in which the MP faces on the Bridge Port
                ''',
                'ieee8021cfmstackdirection',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmStackifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object represents the  Bridge Port or aggregated port
                on which MEPs or MHFs might be configured.
                
                Upon a restart of the system, the system SHALL, if necessary,
                change the value of this variable, and  rearrange the
                ieee8021CfmStackTable, so that it indexes the entry in the
                interface table with the same value of ifAlias that it
                indexed before the system restart.  If no such entry exists,
                then the system SHALL delete all entries in the
                ieee8021CfmStackTable with the interface index.
                ''',
                'ieee8021cfmstackifindex',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmStackMdLevel', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                MD Level of the Maintenance Point.
                ''',
                'ieee8021cfmstackmdlevel',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmStackServiceSelectorOrNone', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Service Selector identifier to which the MP is attached, or 0, if none.
                See textual convention IEEE8021ServiceSelectorValue for details.
                ''',
                'ieee8021cfmstackserviceselectorornone',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmStackServiceSelectorType', REFERENCE_ENUM_CLASS, 'IEEE8021ServiceSelectorType_Enum' , 'ydk.models.ieee8021.IEEE8021_TC_MIB', 'IEEE8021ServiceSelectorType_Enum', 
                [], [], 
                '''                Type of the Service Selector identifier indicated by ieee8021CfmStackServiceSelectorOrNone.
                See textual convention IEEE8021ServiceSelectorType for details.
                ''',
                'ieee8021cfmstackserviceselectortype',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmStackMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the MP.
                ''',
                'ieee8021cfmstackmacaddress',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmStackMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index of the MA in the ieee8021CfmMaNetTable and
                ieee8021CfmMaCompTable to which the MP is associated, or 0, if
                none.
                ''',
                'ieee8021cfmstackmaindex',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmStackMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index of the Maintenance Domain in the ieee8021CfmMdTable
                to which the MP is associated, or 0, if none.
                ''',
                'ieee8021cfmstackmdindex',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmStackMepId', ATTRIBUTE, 'int' , None, None, 
                [(0, 8191)], [], 
                '''                If an MEP is configured, the MEPID, else 0
                ''',
                'ieee8021cfmstackmepid',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmStackEntry',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmStackTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmStackTable',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmStackEntry', REFERENCE_LIST, 'Ieee8021CfmStackEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmStackTable.Ieee8021CfmStackEntry', 
                [], [], 
                '''                The Stack table entry
                ''',
                'ieee8021cfmstackentry',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmStackTable',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmVlanTable.Ieee8021CfmVlanEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmVlanTable.Ieee8021CfmVlanEntry',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmVlanComponentId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The bridge component within the system to which the information
                in this ieee8021CfmVlanEntry applies.  If the system is not a
                Bridge, or if only one component is present in the Bridge, then
                this variable (index) MUST be equal to 1.
                ''',
                'ieee8021cfmvlancomponentid',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmVlanSelector', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This is a service ID belonging to a service that is associated
                with more than one Service Selector identifiers, and this is not the Primary 
                Service ID of the service. The type of this Service Selector is the same
                as the primary Service Selector's type defined by ieee8021CfmMaCompPrimarySelectorType 
                in the ieee8021CfmMaCompTable.
                ''',
                'ieee8021cfmvlanselector',
                'IEEE8021-CFM-V2-MIB', True),
            _MetaInfoClassMember('ieee8021CfmVlanPrimarySelector', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This is the Primary Service selector for a Service that is associated
                with more than one Service Selector identifiers. This value MUST not
                equal the value of ieee8021CfmVlanSelector. The type of this Service Selector is the same
                as the primary Service Selector's type defined by ieee8021CfmMaCompPrimarySelectorType 
                in the ieee8021CfmMaCompTable.
                ''',
                'ieee8021cfmvlanprimaryselector',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmVlanRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                ''',
                'ieee8021cfmvlanrowstatus',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmVlanEntry',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB.Ieee8021CfmVlanTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB.Ieee8021CfmVlanTable',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmVlanEntry', REFERENCE_LIST, 'Ieee8021CfmVlanEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmVlanTable.Ieee8021CfmVlanEntry', 
                [], [], 
                '''                The VLAN table entry.
                ''',
                'ieee8021cfmvlanentry',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'ieee8021CfmVlanTable',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
    'IEEE8021CFMV2MIB' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMV2MIB',
            False, 
            [
            _MetaInfoClassMember('ieee8021CfmConfigErrorListTable', REFERENCE_CLASS, 'Ieee8021CfmConfigErrorListTable' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable', 
                [], [], 
                '''                The CFM Configuration Error List table provides a list of
                Interfaces and VIDs that are incorrectly configured.
                ''',
                'ieee8021cfmconfigerrorlisttable',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmDefaultMdTable', REFERENCE_CLASS, 'Ieee8021CfmDefaultMdTable' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable', 
                [], [], 
                '''                For each bridge component, the Default MD Level Managed Object
                controls MHF creation for VIDs that are not attached to a
                specific Maintenance Association Managed Object, and Sender ID
                TLV transmission by those MHFs.
                
                For each Bridge Port, and for each VLAN ID whose data can
                pass through that Bridge Port, an entry in this table is
                used by the algorithm in subclause 22.2.3 only if there is no
                entry in the Maintenance Association table defining an MA
                for the same VLAN ID and MD Level as this table's entry, and
                on which MA an Up MEP is defined.  If there exists such an
                MA, that MA's objects are used by the algorithm in
                subclause 22.2.3 in place of this table entry's objects.  The
                agent maintains the value of ieee8021CfmDefaultMdStatus to
                indicate whether this entry is overridden by an MA.
                
                When first initialized, the agent creates this table
                automatically with entries for all VLAN IDs,
                with the default values specified for each object.
                
                After this initialization, the writable objects in this
                table need to be persistent upon reboot or restart of a
                device.
                ''',
                'ieee8021cfmdefaultmdtable',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmMaCompTable', REFERENCE_CLASS, 'Ieee8021CfmMaCompTable' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable', 
                [], [], 
                '''                The Maintenance Association table.  Each row in the table
                represents an MA.  An MA is a set of MEPs, each configured
                with a single service instance.
                
                This is the part of the complete MA table that is variable
                across the Bridges in a Maintenance Domain, or across the
                components of a single Bridge.  That part of the MA table that
                is constant across the Bridges and their components in a
                Maintenance Domain is contained in the ieee8021CfmMaNetTable.
                
                This table uses three indices, first index is the
                IEEE8021PbbComponentIdentifier that identifies the component
                within the Bridge for which the information in the
                ieee8021CfmMaCompEntry applies.  The second is the index of the
                Maintenance Domain table.  The third index is the same as the
                index of the ieee8021CfmMaNetEntry for the same MA.
                
                The writable objects in this table need to be persistent
                upon reboot or restart of a device.
                ''',
                'ieee8021cfmmacomptable',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmStackTable', REFERENCE_CLASS, 'Ieee8021CfmStackTable' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmStackTable', 
                [], [], 
                '''                There is one CFM Stack table per bridge. It permits
                the retrieval of information about the Maintenance Points
                configured on any given interface.
                ''',
                'ieee8021cfmstacktable',
                'IEEE8021-CFM-V2-MIB', False),
            _MetaInfoClassMember('ieee8021CfmVlanTable', REFERENCE_CLASS, 'Ieee8021CfmVlanTable' , 'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB', 'IEEE8021CFMV2MIB.Ieee8021CfmVlanTable', 
                [], [], 
                '''                This table defines the association of VIDs into VLANs.  There
                is an entry in this table, for each component of the bridge,
                for each VID that is:
                    a) a VID belonging to a VLAN associated with more than
                       one VID; and
                    b) not the Primary VLAN of that VID.
                The entry in this table contains the Primary VID of the VLAN.
                
                By default, this table is empty, meaning that every VID is
                the Primary VID of a single-VID VLAN.
                
                VLANs that are associated with only one VID SHOULD NOT have
                an entry in this table.
                
                The writable objects in this table need to be persistent
                upon reboot or restart of a device.
                ''',
                'ieee8021cfmvlantable',
                'IEEE8021-CFM-V2-MIB', False),
            ],
            'IEEE8021-CFM-V2-MIB',
            'IEEE8021-CFM-V2-MIB',
            _yang_ns._namespaces['IEEE8021-CFM-V2-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_V2_MIB'
        ),
    },
}
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable.Ieee8021CfmConfigErrorListEntry']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable.Ieee8021CfmDefaultMdEntry']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable.Ieee8021CfmMaCompEntry']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmStackTable.Ieee8021CfmStackEntry']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmStackTable']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmVlanTable.Ieee8021CfmVlanEntry']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmVlanTable']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmConfigErrorListTable']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmDefaultMdTable']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmMaCompTable']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmStackTable']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB']['meta_info']
_meta_table['IEEE8021CFMV2MIB.Ieee8021CfmVlanTable']['meta_info'].parent =_meta_table['IEEE8021CFMV2MIB']['meta_info']
