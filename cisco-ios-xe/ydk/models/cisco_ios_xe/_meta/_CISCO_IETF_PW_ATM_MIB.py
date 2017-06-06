


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry.CpwatmencapEnum' : _MetaInfoEnum('CpwatmencapEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB',
        {
            'mpls':'mpls',
            'l2tpv3':'l2tpv3',
            'unknown':'unknown',
        }, 'CISCO-IETF-PW-ATM-MIB', _yang_ns._namespaces['CISCO-IETF-PW-ATM-MIB']),
    'CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-ATM-MIB', True),
            _MetaInfoClassMember('cpwAtmAvgCellsPacked', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                It indicates the Average number of cells that
                were received in one packet.
                ''',
                'cpwatmavgcellspacked',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmCellPacking', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is used to identify if the VC is configured to do
                Cell Packing.
                ''',
                'cpwatmcellpacking',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmCellsReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object can be used to obtain the information on the
                number of cells that were received and sent to the PSN.
                ''',
                'cpwatmcellsreceived',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmCellsRejected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This Object indicates the number of cells that were rejected by
                this VC because of policing.
                ''',
                'cpwatmcellsrejected',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmCellsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object can be used to obtain the information on the
                number of cells that were received from the PSN and sent
                over the ATM network.
                ''',
                'cpwatmcellssent',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmCellsTagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This Object indicates the number of cells that were Tagged.
                ''',
                'cpwatmcellstagged',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmClpQosMapping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This Object indicates whether the CLP bits are considered when
                determining the value placed in the Quality of Service fields
                (e.g. EXP fields of the MPLS Label Stack) of the encapsulating
                protocol.
                ''',
                'cpwatmclpqosmapping',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmEncap', REFERENCE_ENUM_CLASS, 'CpwatmencapEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB', 'CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry.CpwatmencapEnum', 
                [], [], 
                '''                This object indicates if the packet going on the pseudowire
                is mpls or l2tpv3 encapsulated.
                ''',
                'cpwatmencap',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmHCCellsReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High Capacity counter for the number of cells that were
                received by this VC.
                ''',
                'cpwatmhccellsreceived',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmHCCellsRejected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High Capacity counter for the number of cells that were
                rejected by this VC because of policing.
                ''',
                'cpwatmhccellsrejected',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmHCCellsTagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High Capacity counter for the number of cells that were tagged
                ''',
                'cpwatmhccellstagged',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmIf', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ATM Interface that receives cells from the ATM network.
                ''',
                'cpwatmif',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmMcptTimeout', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This Object represents which MCPT timeout value.
                ''',
                'cpwatmmcpttimeout',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmMncp', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object indicates the maximum number of cells that get
                packed in one packet.
                ''',
                'cpwatmmncp',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmOamCellSupported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This Object indicates whether OAM Cells are transported on this
                VC.
                ''',
                'cpwatmoamcellsupported',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmPeerMncp', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This Object represents the maximum number of cell
                that can be packed in one packet for peer interface.
                ''',
                'cpwatmpeermncp',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmPktsReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object can be used to obtain the information on the
                number of packets that were received and sent to the PSN.
                ''',
                'cpwatmpktsreceived',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmPktsRejected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of packets that were rejected
                because of Policing.
                ''',
                'cpwatmpktsrejected',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmPktsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of packets that were sent
                to the atm network.
                ''',
                'cpwatmpktssent',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmQosScalingFactor', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This Object represents the scaling factor (% value) to be
                applied to ATM QoS rates when calculating QoS rates for the
                PSN domain . For example, in the cell transport mode the
                bandwidth needed in the PSN domain will be higher (since PSN
                Transport header, PW header, and optional control word have
                to transmitted with every cell), whereas in the AAL5 mode
                the bandwidth needed in PSN domain will be less since cell
                headers will be removed after reassembly.
                ''',
                'cpwatmqosscalingfactor',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This Object is used to create, modify or delete a row in this
                table.
                ''',
                'cpwatmrowstatus',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VCI value of this ATM VC.
                ''',
                'cpwatmvci',
                'CISCO-IETF-PW-ATM-MIB', False),
            _MetaInfoClassMember('cpwAtmVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                VPI value of this ATM VC.
                ''',
                'cpwatmvpi',
                'CISCO-IETF-PW-ATM-MIB', False),
            ],
            'CISCO-IETF-PW-ATM-MIB',
            'cpwVcAtmEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-ATM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB'
        ),
    },
    'CiscoIetfPwAtmMib.Cpwvcatmtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwAtmMib.Cpwvcatmtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcAtmEntry', REFERENCE_LIST, 'Cpwvcatmentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB', 'CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry', 
                [], [], 
                '''                A row in this table represents an ATM interface, VC, VP
                that needs to be adapted and carried over PSN. This table
                is indexed by CpwVcIndex in CISCO-IETF-PW-MIB.
                ''',
                'cpwvcatmentry',
                'CISCO-IETF-PW-ATM-MIB', False),
            ],
            'CISCO-IETF-PW-ATM-MIB',
            'cpwVcAtmTable',
            _yang_ns._namespaces['CISCO-IETF-PW-ATM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB'
        ),
    },
    'CiscoIetfPwAtmMib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwAtmMib',
            False, 
            [
            _MetaInfoClassMember('cpwVcAtmTable', REFERENCE_CLASS, 'Cpwvcatmtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB', 'CiscoIetfPwAtmMib.Cpwvcatmtable', 
                [], [], 
                '''                This table specifies the information for an ATM interface, VC,
                VP to be carried over PSN.
                ''',
                'cpwvcatmtable',
                'CISCO-IETF-PW-ATM-MIB', False),
            ],
            'CISCO-IETF-PW-ATM-MIB',
            'CISCO-IETF-PW-ATM-MIB',
            _yang_ns._namespaces['CISCO-IETF-PW-ATM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_ATM_MIB'
        ),
    },
}
_meta_table['CiscoIetfPwAtmMib.Cpwvcatmtable.Cpwvcatmentry']['meta_info'].parent =_meta_table['CiscoIetfPwAtmMib.Cpwvcatmtable']['meta_info']
_meta_table['CiscoIetfPwAtmMib.Cpwvcatmtable']['meta_info'].parent =_meta_table['CiscoIetfPwAtmMib']['meta_info']
