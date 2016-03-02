


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry',
            False, 
            [
            _MetaInfoClassMember('mplsXCIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                ''',
                'mplsxcindex',
                'CISCO-MPLS-LSR-EXT-STD-MIB', True),
            _MetaInfoClassMember('mplsXCInSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                ''',
                'mplsxcinsegmentindex',
                'CISCO-MPLS-LSR-EXT-STD-MIB', True),
            _MetaInfoClassMember('mplsXCOutSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                ''',
                'mplsxcoutsegmentindex',
                'CISCO-MPLS-LSR-EXT-STD-MIB', True),
            _MetaInfoClassMember('cmplsXCExtTunnelPointer', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object indicates the back pointer to the tunnel
                entry segment.  This object cannot be modified if
                mplsXCRowStatus for the corresponding entry in the
                mplsXCTable is active(1).
                ''',
                'cmplsxcexttunnelpointer',
                'CISCO-MPLS-LSR-EXT-STD-MIB', False),
            _MetaInfoClassMember('cmplsXCOppositeDirXCPtr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object indicates the pointer to the opposite
                direction XC entry.  This object cannot be modified if
                mplsXCRowStatus for the corresponding entry in the
                mplsXCTable is active(1).
                ''',
                'cmplsxcoppositedirxcptr',
                'CISCO-MPLS-LSR-EXT-STD-MIB', False),
            ],
            'CISCO-MPLS-LSR-EXT-STD-MIB',
            'cmplsXCExtEntry',
            _yang_ns._namespaces['CISCO-MPLS-LSR-EXT-STD-MIB'],
        'ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB'
        ),
    },
    'CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable' : {
        'meta_info' : _MetaInfoClass('CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable',
            False, 
            [
            _MetaInfoClassMember('cmplsXCExtEntry', REFERENCE_LIST, 'CmplsXCExtEntry' , 'ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB', 'CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry', 
                [], [], 
                '''                An entry in this table extends the cross connect
                information represented by an entry in
                the mplsXCTable in MPLS-LSR-STD-MIB [RFC3813] through
                a sparse augmentation.  An entry can be created by
                a network administrator via SNMP SET commands, or in
                response to signaling protocol events.
                ''',
                'cmplsxcextentry',
                'CISCO-MPLS-LSR-EXT-STD-MIB', False),
            ],
            'CISCO-MPLS-LSR-EXT-STD-MIB',
            'cmplsXCExtTable',
            _yang_ns._namespaces['CISCO-MPLS-LSR-EXT-STD-MIB'],
        'ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB'
        ),
    },
    'CISCOMPLSLSREXTSTDMIB' : {
        'meta_info' : _MetaInfoClass('CISCOMPLSLSREXTSTDMIB',
            False, 
            [
            _MetaInfoClassMember('cmplsXCExtTable', REFERENCE_CLASS, 'CmplsXCExtTable' , 'ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB', 'CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable', 
                [], [], 
                '''                This table sparse augments the mplsXCTable of
                MPLS-LSR-STD-MIB [RFC3813] to provide MPLS-TP specific
                information about associated tunnel information
                ''',
                'cmplsxcexttable',
                'CISCO-MPLS-LSR-EXT-STD-MIB', False),
            ],
            'CISCO-MPLS-LSR-EXT-STD-MIB',
            'CISCO-MPLS-LSR-EXT-STD-MIB',
            _yang_ns._namespaces['CISCO-MPLS-LSR-EXT-STD-MIB'],
        'ydk.models.mpls.CISCO_MPLS_LSR_EXT_STD_MIB'
        ),
    },
}
_meta_table['CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable.CmplsXCExtEntry']['meta_info'].parent =_meta_table['CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable']['meta_info']
_meta_table['CISCOMPLSLSREXTSTDMIB.CmplsXCExtTable']['meta_info'].parent =_meta_table['CISCOMPLSLSREXTSTDMIB']['meta_info']
