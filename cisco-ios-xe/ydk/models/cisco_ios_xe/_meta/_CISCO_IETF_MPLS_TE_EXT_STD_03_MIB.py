


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeConfigLocalId', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                This object allows the administrator to assign a unique
                local identifier to map Global_Node_ID or ICC.
                ''',
                'cmplsnodeconfiglocalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('cmplsNodeConfigGlobalId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                This object indicates the Global Operator Identifier.
                This object value should be zero when
                mplsNodeConfigIccId is configured with non-null value.
                ''',
                'cmplsnodeconfigglobalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeConfigIccId', ATTRIBUTE, 'str' , None, None, 
                [(1, 6)], [], 
                '''                This object allows the operator or service provider to
                configure a unique MPLS-TP ITU-T Carrier Code (ICC)
                either for Ingress ID or Egress ID.
                
                This object value should be zero when
                mplsNodeConfigGlobalId and mplsNodeConfigNodeId are
                assigned with non-zero value.
                ''',
                'cmplsnodeconfigiccid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeConfigNodeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the Node_ID within the operator.
                This object value should be zero when mplsNodeConfigIccId
                is configured with non-null value.
                ''',
                'cmplsnodeconfignodeid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeConfigRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object allows the administrator to create, modify,
                and/or delete a row in this table.
                ''',
                'cmplsnodeconfigrowstatus',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeConfigStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object.
                Conceptual rows having the value 'permanent'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'cmplsnodeconfigstoragetype',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsNodeConfigEntry',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeConfigEntry', REFERENCE_LIST, 'Cmplsnodeconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry', 
                [], [], 
                '''                An entry in this table represents a mapping
                identification for the operator or service provider
                with node or LSR.
                
                As per [RFC6370], this mapping is
                
                represented as Global_Node_ID or ICC.
                
                Note: Each entry in this table should have a unique
                Global_ID and Node_ID combination.
                ''',
                'cmplsnodeconfigentry',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsNodeConfigTable',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeIpMapGlobalId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                This object indicates the Global_ID.
                ''',
                'cmplsnodeipmapglobalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('cmplsNodeIpMapNodeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the Node_ID within the
                operator.
                ''',
                'cmplsnodeipmapnodeid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('cmplsNodeIpMapLocalId', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                This object contains an IP compatible local identifier
                which is defined in mplsNodeConfigTable.
                ''',
                'cmplsnodeipmaplocalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsNodeIpMapEntry',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeIpMapEntry', REFERENCE_LIST, 'Cmplsnodeipmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry', 
                [], [], 
                '''                An entry in this table represents a mapping of
                Global_Node_ID with the local identifier.
                
                An entry in this table is created automatically when
                the Local identifier is associated with Global_ID and
                Node_Id in the mplsNodeConfigTable.
                Note: Each entry in this table should have a unique
                Global_ID and Node_ID combination.
                ''',
                'cmplsnodeipmapentry',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsNodeIpMapTable',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeIccMapIccId', ATTRIBUTE, 'str' , None, None, 
                [(1, 6)], [], 
                '''                This object allows the operator or service provider to
                configure a unique MPLS-TP ITU-T Carrier Code (ICC)
                either for Ingress or Egress LSR ID.
                
                The ICC is a string of one to six characters, each
                character being either alphabetic (i.e.  A-Z) or
                numeric (i.e. 0-9) characters. Alphabetic characters
                in the ICC should be represented with upper case
                letters.
                ''',
                'cmplsnodeiccmapiccid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('cmplsNodeIccMapLocalId', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                This object contains an ICC based local identifier
                which is defined in mplsNodeConfigTable.
                ''',
                'cmplsnodeiccmaplocalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsNodeIccMapEntry',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeIccMapEntry', REFERENCE_LIST, 'Cmplsnodeiccmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry', 
                [], [], 
                '''                An entry in this table represents a mapping of ICC with
                the local identifier.
                
                An entry in this table is created automatically when
                the Local identifier is associated with ICC in
                the mplsNodeConfigTable.
                ''',
                'cmplsnodeiccmapentry',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsNodeIccMapTable',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'mplstunnelindex',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('mplsTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'mplstunnelinstance',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('mplsTunnelIngressLSRId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'mplstunnelingresslsrid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('mplsTunnelEgressLSRId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'mplstunnelegresslsrid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('cmplsTunnelExtDestTnlIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object is applicable only for the bidirectional
                tunnel that has the forward and reverse LSPs in the
                same tunnel or in the different tunnels.
                
                This object holds the same value as that of the
                mplsTunnelIndex of mplsTunnelEntry if the forward and
                reverse LSPs are in the same tunnel. Otherwise,
                this object holds the value of the other direction
                associated LSP's mplsTunnelIndex from a different
                tunnel.
                
                The values of this object and the
                mplsTunnelExtDestTnlLspIndex object together can be used
                to identify an opposite direction LSP i.e. if the
                mplsTunnelIndex and mplsTunnelInstance hold the value
                for forward LSP, this object and
                mplsTunnelExtDestTnlLspIndex can be used to retrieve
                the reverse direction LSP and vice versa.
                
                This object and mplsTunnelExtDestTnlLspIndex values
                provide the first two indices of tunnel entry and
                the remaining indices can be derived as follows,
                if both the forward and reverse LSPs are present in
                the same tunnel, the opposite direction LSP's Ingress
                and Egress Identifier will be same for both the LSPs,
                else the Ingress and Egress Identifiers should be
                swapped in order to index the other direction tunnel.
                ''',
                'cmplstunnelextdesttnlindex',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelExtDestTnlLspIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object is applicable only for the bidirectional
                tunnel that has the forward and reverse LSPs in the
                same tunnel or in the different tunnels.
                
                This object should contain different value if both the
                forward and reverse LSPs present in the same tunnel.
                
                This object can contain same value or different values
                if the forward and reverse LSPs present in the different
                tunnels.
                ''',
                'cmplstunnelextdesttnllspindex',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelExtDestTnlValid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Denotes whether or not this tunnel uses
                mplsTunnelExtDestTnlIndex and
                mplsTunnelExtDestTnlLspIndex for identifying
                the opposite direction tunnel information. Note that if
                this variable is set to true then the
                mplsTunnelExtDestTnlIndex and
                mplsTunnelExtDestTnlLspIndex objects should have
                the valid opposite direction tunnel indices.
                ''',
                'cmplstunnelextdesttnlvalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelExtOppositeDirTnlValid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Denotes whether or not this tunnel uses
                mplsTunnelOppositeDirPtr for identifying the opposite
                direction tunnel information. Note that if this variable
                is set to true then the mplsTunnelOppositeDirPtr should
                point to the first accessible row of the opposite
                direction tunnel.
                ''',
                'cmplstunnelextoppositedirtnlvalid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelOppositeDirPtr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object is applicable only for the bidirectional
                tunnel that has the forward and reverse LSPs in the
                same tunnel or in the different tunnels.
                
                This object holds the opposite direction tunnel entry
                if the bidirectional tunnel is setup by configuring two
                tunnel entries in mplsTunnelTable.
                
                The value of zeroDotZero indicates single tunnel entry
                is used for bidirectional tunnel setup.
                ''',
                'cmplstunneloppositedirptr',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsTunnelExtEntry',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable',
            False, 
            [
            _MetaInfoClassMember('cmplsTunnelExtEntry', REFERENCE_LIST, 'Cmplstunnelextentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry', 
                [], [], 
                '''                An entry in this table represents MPLS-TP
                specific additional tunnel configurations.
                ''',
                'cmplstunnelextentry',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsTunnelExtTable',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'mplstunnelindex',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('mplsTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'mplstunnelinstance',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('mplsTunnelIngressLSRId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'mplstunnelingresslsrid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('mplsTunnelEgressLSRId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'mplstunnelegresslsrid',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', True),
            _MetaInfoClassMember('cmplsTunnelReversePerfBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bytes forwarded on the tunnel in the reverse
                direction if it is bidirectional.
                
                This object represents the 32-bit value of the least
                significant part of the 64-bit value if both
                mplsTunnelReversePerfHCBytes and this object are returned.
                
                For links that do not transport packets, this packet
                counter cannot be maintained.  For such links, this value
                will return noSuchInstance.
                ''',
                'cmplstunnelreverseperfbytes',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelReversePerfErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of errored packets received on the tunnel in
                the reverse direction if it is bidirectional.  For links
                that do not transport packets, this packet counter cannot
                be maintained.  For such links, this value will return
                noSuchInstance.
                ''',
                'cmplstunnelreverseperferrors',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelReversePerfHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High-capacity counter for number of bytes forwarded on the
                tunnel in the reverse direction if it is bidirectional.
                
                For links that do not transport packets, this packet
                counter cannot be maintained.  For such links, this value
                will return noSuchInstance.
                ''',
                'cmplstunnelreverseperfhcbytes',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelReversePerfHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High-capacity counter for number of packets forwarded on
                the tunnel in the reverse direction if it is
                bidirectional.
                
                For links that do not transport packets, this packet
                counter cannot be maintained.  For such links, this value
                will return noSuchInstance.
                ''',
                'cmplstunnelreverseperfhcpackets',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelReversePerfPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets forwarded on the tunnel in the reverse
                direction if it is bidirectional.
                
                This object represents the 32-bit value of the least
                significant part of the 64-bit value if both
                mplsTunnelReversePerfHCPackets and this object
                are returned.
                
                For links that do not transport packets, this packet
                counter cannot be maintained.  For such links, this value
                will return noSuchInstance.
                ''',
                'cmplstunnelreverseperfpackets',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsTunnelReversePerfEntry',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable',
            False, 
            [
            _MetaInfoClassMember('cmplsTunnelReversePerfEntry', REFERENCE_LIST, 'Cmplstunnelreverseperfentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry', 
                [], [], 
                '''                An entry in this table is created by the LSR for every
                bidirectional MPLS tunnel where packets are visible to the
                LSR.
                ''',
                'cmplstunnelreverseperfentry',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'cmplsTunnelReversePerfTable',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsTeExtStd03Mib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsTeExtStd03Mib',
            False, 
            [
            _MetaInfoClassMember('cmplsNodeConfigTable', REFERENCE_CLASS, 'Cmplsnodeconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable', 
                [], [], 
                '''                This table allows the administrator to map a node or
                LSR Identifier (IP compatible [Global_Node_ID] or ICC)
                with a local identifier.
                
                
                This table is created to reuse the existing
                mplsTunnelTable for MPLS based transport network
                tunnels also.
                Since the MPLS tunnel's Ingress/Egress LSR identifiers'
                size (Unsigned32) value is not compatible for
                MPLS-TP tunnel i.e. Global_Node_Id of size 8 bytes and
                ICC of size 6 bytes, there exists a need to map the
                Global_Node_ID or ICC with the local identifier of size
                4 bytes (Unsigned32) value in order
                to index (Ingress/Egress LSR identifier)
                the existing mplsTunnelTable.
                ''',
                'cmplsnodeconfigtable',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeIccMapTable', REFERENCE_CLASS, 'Cmplsnodeiccmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable', 
                [], [], 
                '''                This read-only table allows the administrator to retrieve
                the local identifier for a given ICC operator in an ICC
                operator environment.
                
                This table MAY be used in on-demand and/or proactive
                OAM operations to get the Ingress/Egress LSR
                identifier (Local Identifier) from Src-ICC
                or Dst-ICC and the Ingress and Egress LSR
                identifiers are used to retrieve the tunnel entry.
                This table returns nothing when the associated entry
                is not defined in mplsNodeConfigTable.
                ''',
                'cmplsnodeiccmaptable',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeIpMapTable', REFERENCE_CLASS, 'Cmplsnodeipmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable', 
                [], [], 
                '''                This read-only table allows the administrator to retrieve
                the local identifier for a given Global_Node_ID in an IP
                compatible operator environment.
                
                This table MAY be used in on-demand and/or proactive
                OAM operations to get the Ingress/Egress LSR identifier
                (Local Identifier) from Src-Global_Node_ID
                or Dst-Global_Node_ID and the Ingress and Egress LSR
                identifiers are used to retrieve the tunnel entry.
                
                This table returns nothing when the associated entry
                is not defined in mplsNodeConfigTable.
                ''',
                'cmplsnodeipmaptable',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelExtTable', REFERENCE_CLASS, 'Cmplstunnelexttable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable', 
                [], [], 
                '''                This table represents MPLS-TP specific extensions to
                mplsTunnelTable.
                
                As per MPLS-TP Identifiers [RFC6370], LSP_ID for IP based
                co-routed bidirectional tunnel,
                
                A1-{Global_ID::Node_ID::Tunnel_Num}::Z9-{Global_ID::
                Node_ID::Tunnel_Num}::LSP_Num
                
                LSP_ID for IP based associated bidirectional tunnel,
                A1-{Global_ID::Node_ID::Tunnel_Num::LSP_Num}::
                Z9-{Global_ID::Node_ID::Tunnel_Num::LSP_Num}
                
                mplsTunnelTable is reused for forming the LSP_ID
                as follows,
                
                Source Tunnel_Num is mapped with mplsTunnelIndex,
                Source Node_ID is mapped with
                mplsTunnelIngressLSRId, Destination Node_ID is
                mapped with mplsTunnelEgressLSRId LSP_Num is mapped with
                mplsTunnelInstance.
                
                Source Global_Node_ID and/or ICC and Destination
                Global_Node_ID and/or ICC are maintained in the
                mplsNodeConfigTable and mplsNodeConfigLocalId is
                used to create an entry in mplsTunnelTable.
                ''',
                'cmplstunnelexttable',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsTunnelReversePerfTable', REFERENCE_CLASS, 'Cmplstunnelreverseperftable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB', 'CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable', 
                [], [], 
                '''                This table extends the mplsTunnelTable to provide
                per-tunnel packet performance information for the reverse
                direction of a bidirectional tunnel.  It can be seen as
                supplementing the mplsTunnelPerfTable, which augments the
                mplsTunnelTable.
                
                For links that do not transport packets, these packet
                counters cannot be maintained.  For such links, attempts
                to read the objects in this table will return
                noSuchInstance.
                ''',
                'cmplstunnelreverseperftable',
                'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB',
            _yang_ns._namespaces['CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB'
        ),
    },
}
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib']['meta_info']
_meta_table['CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable']['meta_info'].parent =_meta_table['CiscoIetfMplsTeExtStd03Mib']['meta_info']
