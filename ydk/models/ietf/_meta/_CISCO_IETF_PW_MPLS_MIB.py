


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsInboundIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Arbitrary index for enabling multiple rows per VC in 
                this table. Next available free index can be retrieved 
                using cpwVcMplsInboundIndexNext. 
                ''',
                'cpwvcmplsinboundindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsInboundIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                In case of VC only (no outer tunnel), this object holds the 
                ifIndex of the inbound port, otherwise set to zero.
                ''',
                'cpwvcmplsinboundifindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundLsrXcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If the outer label is defined in the MPL-LSR-MIB, i.e. set  
                by LDP or manually, this object points to the XC index  
                of the outer tunnel. Otherwise, it is set to zero.
                ''',
                'cpwvcmplsinboundlsrxcindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                ''',
                'cpwvcmplsinboundrowstatus',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this row.
                ''',
                'cpwvcmplsinboundstoragetype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsinboundtunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsinboundtunnelinstance',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundTunnelLclLSR', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsinboundtunnellcllsr',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundTunnelPeerLSR', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsinboundtunnelpeerlsr',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsInboundEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsInboundEntry', REFERENCE_LIST, 'CpwVcMplsInboundEntry' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry', 
                [], [], 
                '''                A row in this table represents a link between PW VCs (that 
                require MPLS tunnels) and MPLS tunnel for packets arriving 
                from the PSN. 
                This table is indexed by the set of indexes used to 
                identify the VC - cpwVcIndex and an additional 
                index enabling multiple rows for the same VC index. 
                
                Note that the first entry for each VC can be indexed by  
                cpwVcMplsOutboundIndex equal zero without a need for  
                retrieval of cpwVcMplsInboundIndexNext. 
                
                An entry is created in this table either automatically by  
                the local agent or created manually by the operator in  
                cases that strict mode is required. 
                
                Note that the control messages contain VC ID and VC type,  
                which together with the remote IP address identify the 
                cpwVcIndex in the local node. 
                This table points to the appropriate MPLS MIB. In the case  
                of MPLS-TE, the 4 variables relevant to the indexing of a 
                TE MPLS tunnel are set as in Srinivasan, et al, <draft- 
                ietf-mpls-te-mib>. 
                
                In case of non-TE MPLS tunnel (an outer tunnel label  
                assigned by LDP or manually) the table points to the XC  
                entry in the MPLS-LSR-MIB as in Srinivasan, et al, <draft- 
                ietf-mpls-lsr-mib>. 
                
                Each VC may have multiple rows in this tables if protection  
                is available at the outer tunnel level, each row may be of 
                different type except for VC only, on which only rows with 
                ifIndex of the port are allowed. 
                ''',
                'cpwvcmplsinboundentry',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsInboundTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry.CpwVcMplsNonTeMappingTunnelDirection_Enum' : _MetaInfoEnum('CpwVcMplsNonTeMappingTunnelDirection_Enum', 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB',
        {
            'outbound':'OUTBOUND',
            'inbound':'INBOUND',
        }, 'CISCO-IETF-PW-MPLS-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB']),
    'CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsNonTeMappingIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Identify the port on which the VC is carried for VC only  
                case.
                ''',
                'cpwvcmplsnontemappingifindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingTunnelDirection', REFERENCE_ENUM_CLASS, 'CpwVcMplsNonTeMappingTunnelDirection_Enum' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry.CpwVcMplsNonTeMappingTunnelDirection_Enum', 
                [], [], 
                '''                Identifies if the row represent an outbound or inbound  
                mapping.
                ''',
                'cpwvcmplsnontemappingtunneldirection',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingVcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value that represent the VC in the cpwVcTable.
                ''',
                'cpwvcmplsnontemappingvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingXcTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index for the conceptual XC row identifying Tunnel to VC  
                mappings when the outer tunnel is created by the MPLS-LSR- 
                MIB, Zero otherwise.
                ''',
                'cpwvcmplsnontemappingxctunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsNonTeMappingEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsNonTeMappingEntry', REFERENCE_LIST, 'CpwVcMplsNonTeMappingEntry' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry', 
                [], [], 
                '''                A row in this table represents the association 
                between the PW VC and it's non TE MPLS outer Tunnel 
                it's physical interface if there is no outer tunnel  
                (VC only). 
                
                An application can use this table to quickly retrieve the  
                PW carried over specific non-TE MPLS outer tunnel or  
                physical interface. 
                
                The table in indexed by the XC index for MPLS Non-TE  
                tunnel, or ifIndex of the port in VC only case, the  
                direction of the VC in the specific entry and the VCIndex. 
                
                The same table is used in both inbound and outbound 
                directions, but in a different row for each direction. If  
                the inbound association is not known, no rows should exist  
                for it. 
                
                Rows are created by the local agent when all the  
                association data is available for display.
                ''',
                'cpwvcmplsnontemappingentry',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsNonTeMappingTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsObjects' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsObjects',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsInboundIndexNext', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object contains an appropriate value to 
                be used for cpwVcMplsInboundIndex when creating 
                entries in the cpwVcMplsInboundTable. The value 
                0 indicates that no unassigned entries are 
                available. To obtain the cpwVcMplsInboundIndex 
                value for a new entry, the manager issues a 
                management protocol retrieval operation to obtain 
                the current value of this object.  After each 
                retrieval, the agent should modify the value to 
                the next unassigned index, however the agent MUST 
                NOT assume such retrieval will be done for each  
                row created.
                ''',
                'cpwvcmplsinboundindexnext',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundIndexNext', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object contains an appropriate value to 
                be used for cpwVcMplsOutboundIndex when creating 
                entries in the cpwVcMplsOutboundTable. The value 
                0 indicates that no unassigned entries are 
                available. To obtain the cpwVcMplsOutboundIndex 
                value for a new entry, the manager issues a 
                management protocol retrieval operation to obtain 
                the current value of this object.  After each 
                retrieval, the agent should modify the value to 
                the next unassigned index, however the agent MUST 
                NOT assume such retrieval will be done for each  
                row created.
                ''',
                'cpwvcmplsoutboundindexnext',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsObjects',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsOutboundIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Arbitrary index for enabling multiple rows per VC in 
                this table. Next available free index can be retrieved  
                using cpwVcMplsOutboundIndexNext. 
                ''',
                'cpwvcmplsoutboundindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsOutboundIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                In case of VC only (no outer tunnel), this object holds 
                the ifIndex of the outbound port, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundifindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundLsrXcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object will be set by the operator. If the outer 
                label is defined in the MPL-LSR-MIB, i.e. set by LDP 
                or manually, this object points to the XC index  
                of the outer tunnel. Otherwise, it is set to zero.
                ''',
                'cpwvcmplsoutboundlsrxcindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                ''',
                'cpwvcmplsoutboundrowstatus',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this object.
                ''',
                'cpwvcmplsoutboundstoragetype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundtunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundtunnelinstance',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTunnelLclLSR', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundtunnellcllsr',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTunnelPeerLSR', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundtunnelpeerlsr',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsOutboundEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsOutboundEntry', REFERENCE_LIST, 'CpwVcMplsOutboundEntry' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry', 
                [], [], 
                '''                A row in this table represents a link between PW VC (that 
                require MPLS tunnels) and MPLS tunnel toward the PSN. 
                In the case of VC only, it associate the VC with the  
                interface that shall carry the VC. 
                This table is indexed by the pwVcIndex and an additional 
                index enabling multiple rows for the same VC index. 
                
                At least one entry is created in this table by the operator  
                for each PW VC that requires MPLS PSN. Note that the first 
                entry for each VC can be indexed by cpwVcMplsOutboundIndex  
                equal zero without a need for retrieval of  
                cpwVcMplsOutboundIndexNext. 
                
                This table points to the appropriate MPLS MIB. In the case  
                of MPLS-TE, the 4 variables relevant to the indexing of  
                a TE MPLS tunnel are set as in Srinivasan, et al, <draft- 
                ietf-mpls-te-mib>. 
                In case of Non-TE MPLS (an outer tunnel label assigned by  
                LDP or manually) the table points to the XC entry in the  
                LSR MIB as in Srinivasan, et al, <draft-ietf-mpls-lsr-mib>. 
                In case of VC only (no outer tunnel) the ifIndex of the 
                port to carry the VC is configured.  
                
                Each VC may have multiple rows in this tables if protection  
                is available at the outer tunnel level, each row may be of 
                different type except for VC only, on which only rows with 
                ifIndex of the port are allowed. 
                ''',
                'cpwvcmplsoutboundentry',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsOutboundTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsExpBitsMode_Enum' : _MetaInfoEnum('CpwVcMplsExpBitsMode_Enum', 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB',
        {
            'outerTunnel':'OUTERTUNNEL',
            'specifiedValue':'SPECIFIEDVALUE',
            'serviceDependant':'SERVICEDEPENDANT',
        }, 'CISCO-IETF-PW-MPLS-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB']),
    'CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsExpBits', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Set by the operator to indicate the MPLS EXP bits to be  
                used on the VC shim label if cpwVcMplsExpBitsMode is   
                specifiedValue(2), zero otherwise.
                ''',
                'cpwvcmplsexpbits',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsExpBitsMode', REFERENCE_ENUM_CLASS, 'CpwVcMplsExpBitsMode_Enum' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsExpBitsMode_Enum', 
                [], [], 
                '''                Set by the operator to indicate the way the VC shim label 
                EXP bits are to be determined. The value of outerTunnel(1) 
                is used where there is an outer tunnel - cpwVcMplsMplsType  
                is mplsTe or mplsNonTe. Note that in this case there is no 
                need to mark the VC label with the EXP bits since the VC  
                label is not visible to the intermediate nodes. 
                If there is no outer tunnel, specifiedValue(2) indicate  
                that the value is specified by cpwVcMplsExpBits, and  
                serviceDependant(3) indicate that the EXP bits are setup  
                based on a rule specified in the emulated service specific  
                tables, for example when the EXP bits are a function of  
                802.1p marking for Ethernet emulated service.
                ''',
                'cpwvcmplsexpbitsmode',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsLocalLdpEntityID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The local LDP Entity index of the LDP entity to be used  
                for this VC on the local node. Should be set to all zeros  
                if not used.
                ''',
                'cpwvcmplslocalldpentityid',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsLocalLdpID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The local LDP identifier of the LDP entity creating 
                this VC in the local node. As the VC labels are always 
                set from the per platform label space, the last two octets  
                in the LDP ID MUST be always both zeros.
                ''',
                'cpwvcmplslocalldpid',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsMplsType', REFERENCE_BITS, 'CpwVcMplsMplsType_Bits' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry.CpwVcMplsMplsType_Bits', 
                [], [], 
                '''                Set by the operator to indicate the outer tunnel types, if 
                exists. mplsTe is used if the outer tunnel was set-up by  
                MPLS-TE, and mplsNonTe is used the outer tunnel was set up 
                by LDP or manually. Combination of mplsTe and mplsNonTe  
                may exist in case of outer tunnel protection. 
                vcOnly is used if there is no outer tunnel label. vcOnly  
                cannot be combined with mplsNonTe or mplsTe.
                ''',
                'cpwvcmplsmplstype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsPeerLdpID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The peer LDP identifier as identified from the LDP  
                session. Should be zero if not relevant or not known yet.
                ''',
                'cpwvcmplspeerldpid',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this row.
                ''',
                'cpwvcmplsstoragetype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsTtl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Set by the operator to indicate the VC TTL bits to be used 
                on the VC shim label.
                ''',
                'cpwvcmplsttl',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsTable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsEntry', REFERENCE_LIST, 'CpwVcMplsEntry' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry', 
                [], [], 
                '''                A row in this table represents parameters specific to MPLS  
                PSN for a pseudo wire connection (VC). The row is created  
                automatically by the local agent if the cpwVcPsnType is  
                MPLS. It is indexed by cpwVcIndex, which uniquely  
                identifying a singular connection. 
                ''',
                'cpwvcmplsentry',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry.CpwVcMplsTeMappingTunnelDirection_Enum' : _MetaInfoEnum('CpwVcMplsTeMappingTunnelDirection_Enum', 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB',
        {
            'outbound':'OUTBOUND',
            'inbound':'INBOUND',
        }, 'CISCO-IETF-PW-MPLS-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB']),
    'CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelDirection', REFERENCE_ENUM_CLASS, 'CpwVcMplsTeMappingTunnelDirection_Enum' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry.CpwVcMplsTeMappingTunnelDirection_Enum', 
                [], [], 
                '''                Identifies if the row represent an outbound or inbound  
                mapping.
                ''',
                'cpwvcmplstemappingtunneldirection',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Primary index for the conceptual row identifying the  
                MPLS-TE tunnel.
                ''',
                'cpwvcmplstemappingtunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Identifies an instance of the MPLS-TE tunnel.
                ''',
                'cpwvcmplstemappingtunnelinstance',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelLocalLsrID', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Identifies the local LSR.
                ''',
                'cpwvcmplstemappingtunnellocallsrid',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelPeerLsrID', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Identifies an Peer LSR when the outer tunnel is MPLS-TE  
                based.
                ''',
                'cpwvcmplstemappingtunnelpeerlsrid',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingVcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value that represent the VC in the cpwVcTable.
                ''',
                'cpwvcmplstemappingvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsTeMappingEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsTeMappingEntry', REFERENCE_LIST, 'CpwVcMplsTeMappingEntry' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry', 
                [], [], 
                '''                A row in this table represents the association 
                between a PW VC and it's MPLS-TE outer Tunnel. 
                
                An application can use this table to quickly retrieve the  
                PW carried over specific TE MPLS outer tunnel. 
                
                The table in indexed by the 4 indexes of a TE tunnel, 
                the direction of the VC specific entry and the VcIndex. 
                
                The same table is used in both inbound and outbound 
                directions, a different row for each direction. If the  
                inbound association is not known, no rows should exist for  
                it. 
                
                Rows are created by the local agent when all the  
                association data is available for display.
                ''',
                'cpwvcmplstemappingentry',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsTeMappingTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CISCOIETFPWMPLSMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIETFPWMPLSMIB',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsInboundTable', REFERENCE_CLASS, 'CpwVcMplsInboundTable' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable', 
                [], [], 
                '''                This table associates VCs using MPLS PSN with the inbound 
                MPLS tunnels (i.e. for packets coming from the PSN),  
                if such association is desired (mainly for security  
                reasons).
                ''',
                'cpwvcmplsinboundtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingTable', REFERENCE_CLASS, 'CpwVcMplsNonTeMappingTable' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable', 
                [], [], 
                '''                This table maps an inbound/outbound Tunnel to a VC in non- 
                TE applications.
                ''',
                'cpwvcmplsnontemappingtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsObjects', REFERENCE_CLASS, 'CpwVcMplsObjects' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsObjects', 
                [], [], 
                '''                ''',
                'cpwvcmplsobjects',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTable', REFERENCE_CLASS, 'CpwVcMplsOutboundTable' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable', 
                [], [], 
                '''                This table associates VCs using MPLS PSN with the outbound 
                MPLS tunnels (i.e. toward the PSN) or the physical  
                interface in case of VC only.
                ''',
                'cpwvcmplsoutboundtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsTable', REFERENCE_CLASS, 'CpwVcMplsTable' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTable', 
                [], [], 
                '''                This table specifies information for VC to be carried over  
                MPLS PSN.
                ''',
                'cpwvcmplstable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsTeMappingTable', REFERENCE_CLASS, 'CpwVcMplsTeMappingTable' , 'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB', 'CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable', 
                [], [], 
                '''                This table maps an inbound/outbound Tunnel to a VC in  
                MPLS-TE applications.
                ''',
                'cpwvcmplstemappingtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'CISCO-IETF-PW-MPLS-MIB',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.ietf.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
}
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable.CpwVcMplsInboundEntry']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable.CpwVcMplsNonTeMappingEntry']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable.CpwVcMplsOutboundEntry']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTable.CpwVcMplsEntry']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTable']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable.CpwVcMplsTeMappingEntry']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsInboundTable']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsNonTeMappingTable']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsObjects']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsOutboundTable']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTable']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB']['meta_info']
_meta_table['CISCOIETFPWMPLSMIB.CpwVcMplsTeMappingTable']['meta_info'].parent =_meta_table['CISCOIETFPWMPLSMIB']['meta_info']
