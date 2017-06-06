


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfPwMplsMib.Cpwvcmplsobjects' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsobjects',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsInboundIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.CpwvcmplsexpbitsmodeEnum' : _MetaInfoEnum('CpwvcmplsexpbitsmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB',
        {
            'outerTunnel':'outerTunnel',
            'specifiedValue':'specifiedValue',
            'serviceDependant':'serviceDependant',
        }, 'CISCO-IETF-PW-MPLS-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB']),
    'CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsExpBits', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Set by the operator to indicate the MPLS EXP bits to be  
                used on the VC shim label if cpwVcMplsExpBitsMode is   
                specifiedValue(2), zero otherwise.
                ''',
                'cpwvcmplsexpbits',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsExpBitsMode', REFERENCE_ENUM_CLASS, 'CpwvcmplsexpbitsmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.CpwvcmplsexpbitsmodeEnum', 
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
                [('0', '4294967295')], [], 
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
            _MetaInfoClassMember('cpwVcMplsMplsType', REFERENCE_BITS, 'Cpwvcmplsmplstype' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry.Cpwvcmplsmplstype', 
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
            _MetaInfoClassMember('cpwVcMplsStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this row.
                ''',
                'cpwvcmplsstoragetype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsTtl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Set by the operator to indicate the VC TTL bits to be used 
                on the VC shim label.
                ''',
                'cpwvcmplsttl',
                'CISCO-IETF-PW-MPLS-MIB', False),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplstable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplstable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsEntry', REFERENCE_LIST, 'Cpwvcmplsentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsOutboundIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Arbitrary index for enabling multiple rows per VC in 
                this table. Next available free index can be retrieved  
                using cpwVcMplsOutboundIndexNext. 
                ''',
                'cpwvcmplsoutboundindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsOutboundIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                In case of VC only (no outer tunnel), this object holds 
                the ifIndex of the outbound port, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundifindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundLsrXcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object will be set by the operator. If the outer 
                label is defined in the MPL-LSR-MIB, i.e. set by LDP 
                or manually, this object points to the XC index  
                of the outer tunnel. Otherwise, it is set to zero.
                ''',
                'cpwvcmplsoutboundlsrxcindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                ''',
                'cpwvcmplsoutboundrowstatus',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this object.
                ''',
                'cpwvcmplsoutboundstoragetype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsoutboundtunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsOutboundEntry', REFERENCE_LIST, 'Cpwvcmplsoutboundentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsInboundIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Arbitrary index for enabling multiple rows per VC in 
                this table. Next available free index can be retrieved 
                using cpwVcMplsInboundIndexNext. 
                ''',
                'cpwvcmplsinboundindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsInboundIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                In case of VC only (no outer tunnel), this object holds the 
                ifIndex of the inbound port, otherwise set to zero.
                ''',
                'cpwvcmplsinboundifindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundLsrXcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the outer label is defined in the MPL-LSR-MIB, i.e. set  
                by LDP or manually, this object points to the XC index  
                of the outer tunnel. Otherwise, it is set to zero.
                ''',
                'cpwvcmplsinboundlsrxcindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                ''',
                'cpwvcmplsinboundrowstatus',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this row.
                ''',
                'cpwvcmplsinboundstoragetype',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Part of set of indexes for outbound tunnel in the case of  
                MPLS-TE outer tunnel, otherwise set to zero.
                ''',
                'cpwvcmplsinboundtunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsInboundTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplsinboundtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsinboundtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsInboundEntry', REFERENCE_LIST, 'Cpwvcmplsinboundentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry.CpwvcmplsnontemappingtunneldirectionEnum' : _MetaInfoEnum('CpwvcmplsnontemappingtunneldirectionEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB',
        {
            'outbound':'outbound',
            'inbound':'inbound',
        }, 'CISCO-IETF-PW-MPLS-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB']),
    'CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsNonTeMappingTunnelDirection', REFERENCE_ENUM_CLASS, 'CpwvcmplsnontemappingtunneldirectionEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry.CpwvcmplsnontemappingtunneldirectionEnum', 
                [], [], 
                '''                Identifies if the row represent an outbound or inbound  
                mapping.
                ''',
                'cpwvcmplsnontemappingtunneldirection',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingXcTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index for the conceptual XC row identifying Tunnel to VC  
                mappings when the outer tunnel is created by the MPLS-LSR- 
                MIB, Zero otherwise.
                ''',
                'cpwvcmplsnontemappingxctunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Identify the port on which the VC is carried for VC only  
                case.
                ''',
                'cpwvcmplsnontemappingifindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value that represent the VC in the cpwVcTable.
                ''',
                'cpwvcmplsnontemappingvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsNonTeMappingEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsNonTeMappingEntry', REFERENCE_LIST, 'Cpwvcmplsnontemappingentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry.CpwvcmplstemappingtunneldirectionEnum' : _MetaInfoEnum('CpwvcmplstemappingtunneldirectionEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB',
        {
            'outbound':'outbound',
            'inbound':'inbound',
        }, 'CISCO-IETF-PW-MPLS-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB']),
    'CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelDirection', REFERENCE_ENUM_CLASS, 'CpwvcmplstemappingtunneldirectionEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry.CpwvcmplstemappingtunneldirectionEnum', 
                [], [], 
                '''                Identifies if the row represent an outbound or inbound  
                mapping.
                ''',
                'cpwvcmplstemappingtunneldirection',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Primary index for the conceptual row identifying the  
                MPLS-TE tunnel.
                ''',
                'cpwvcmplstemappingtunnelindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifies an instance of the MPLS-TE tunnel.
                ''',
                'cpwvcmplstemappingtunnelinstance',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelPeerLsrID', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Identifies an Peer LSR when the outer tunnel is MPLS-TE  
                based.
                ''',
                'cpwvcmplstemappingtunnelpeerlsrid',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingTunnelLocalLsrID', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Identifies the local LSR.
                ''',
                'cpwvcmplstemappingtunnellocallsrid',
                'CISCO-IETF-PW-MPLS-MIB', True),
            _MetaInfoClassMember('cpwVcMplsTeMappingVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value that represent the VC in the cpwVcTable.
                ''',
                'cpwvcmplstemappingvcindex',
                'CISCO-IETF-PW-MPLS-MIB', True),
            ],
            'CISCO-IETF-PW-MPLS-MIB',
            'cpwVcMplsTeMappingEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MPLS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib.Cpwvcmplstemappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib.Cpwvcmplstemappingtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsTeMappingEntry', REFERENCE_LIST, 'Cpwvcmplstemappingentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
    'CiscoIetfPwMplsMib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMplsMib',
            False, 
            [
            _MetaInfoClassMember('cpwVcMplsInboundTable', REFERENCE_CLASS, 'Cpwvcmplsinboundtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsinboundtable', 
                [], [], 
                '''                This table associates VCs using MPLS PSN with the inbound 
                MPLS tunnels (i.e. for packets coming from the PSN),  
                if such association is desired (mainly for security  
                reasons).
                ''',
                'cpwvcmplsinboundtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsNonTeMappingTable', REFERENCE_CLASS, 'Cpwvcmplsnontemappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable', 
                [], [], 
                '''                This table maps an inbound/outbound Tunnel to a VC in non- 
                TE applications.
                ''',
                'cpwvcmplsnontemappingtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsObjects', REFERENCE_CLASS, 'Cpwvcmplsobjects' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsobjects', 
                [], [], 
                '''                ''',
                'cpwvcmplsobjects',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsOutboundTable', REFERENCE_CLASS, 'Cpwvcmplsoutboundtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable', 
                [], [], 
                '''                This table associates VCs using MPLS PSN with the outbound 
                MPLS tunnels (i.e. toward the PSN) or the physical  
                interface in case of VC only.
                ''',
                'cpwvcmplsoutboundtable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsTable', REFERENCE_CLASS, 'Cpwvcmplstable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstable', 
                [], [], 
                '''                This table specifies information for VC to be carried over  
                MPLS PSN.
                ''',
                'cpwvcmplstable',
                'CISCO-IETF-PW-MPLS-MIB', False),
            _MetaInfoClassMember('cpwVcMplsTeMappingTable', REFERENCE_CLASS, 'Cpwvcmplstemappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB', 'CiscoIetfPwMplsMib.Cpwvcmplstemappingtable', 
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
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MPLS_MIB'
        ),
    },
}
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplstable.Cpwvcmplsentry']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib.Cpwvcmplstable']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable.Cpwvcmplsoutboundentry']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsinboundtable.Cpwvcmplsinboundentry']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsinboundtable']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable.Cpwvcmplsnontemappingentry']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplstemappingtable.Cpwvcmplstemappingentry']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib.Cpwvcmplstemappingtable']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsobjects']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplstable']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsoutboundtable']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsinboundtable']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplsnontemappingtable']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib']['meta_info']
_meta_table['CiscoIetfPwMplsMib.Cpwvcmplstemappingtable']['meta_info'].parent =_meta_table['CiscoIetfPwMplsMib']['meta_info']
