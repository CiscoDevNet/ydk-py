


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfMplsIdStd03Mib.Cmplsidobjects' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsIdStd03Mib.Cmplsidobjects',
            False, 
            [
            _MetaInfoClassMember('cmplsGlobalId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                This object allows the administrator to assign a unique
                operator identifier also called MPLS-TP Global_ID.
                ''',
                'cmplsglobalid',
                'CISCO-IETF-MPLS-ID-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsIcc', ATTRIBUTE, 'str' , None, None, 
                [(1, 6)], [], 
                '''                This object allows the operator or service provider to
                assign a unique MPLS-TP ITU-T Carrier Code (ICC) to a
                network.
                ''',
                'cmplsicc',
                'CISCO-IETF-MPLS-ID-STD-03-MIB', False),
            _MetaInfoClassMember('cmplsNodeId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object allows the operator or service provider to
                assign a unique MPLS-TP Node_ID.
                
                The Node_ID is assigned within the scope of
                the Global_ID.
                ''',
                'cmplsnodeid',
                'CISCO-IETF-MPLS-ID-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-ID-STD-03-MIB',
            'cmplsIdObjects',
            _yang_ns._namespaces['CISCO-IETF-MPLS-ID-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_ID_STD_03_MIB'
        ),
    },
    'CiscoIetfMplsIdStd03Mib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfMplsIdStd03Mib',
            False, 
            [
            _MetaInfoClassMember('cmplsIdObjects', REFERENCE_CLASS, 'Cmplsidobjects' , 'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_ID_STD_03_MIB', 'CiscoIetfMplsIdStd03Mib.Cmplsidobjects', 
                [], [], 
                '''                ''',
                'cmplsidobjects',
                'CISCO-IETF-MPLS-ID-STD-03-MIB', False),
            ],
            'CISCO-IETF-MPLS-ID-STD-03-MIB',
            'CISCO-IETF-MPLS-ID-STD-03-MIB',
            _yang_ns._namespaces['CISCO-IETF-MPLS-ID-STD-03-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_ID_STD_03_MIB'
        ),
    },
}
_meta_table['CiscoIetfMplsIdStd03Mib.Cmplsidobjects']['meta_info'].parent =_meta_table['CiscoIetfMplsIdStd03Mib']['meta_info']
