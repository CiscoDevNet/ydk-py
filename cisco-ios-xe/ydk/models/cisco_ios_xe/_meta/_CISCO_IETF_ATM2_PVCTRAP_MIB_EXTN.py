


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', True),
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', True),
            _MetaInfoClassMember('atmPVclStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last notification interval.
                ''',
                'atmpvclstatuschangeend',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmPVclStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last notification interval.
                ''',
                'atmpvclstatuschangestart',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmPVclStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last notification interval.
                ''',
                'atmpvclstatustransition',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN',
            'atmCurrentStatusChangePVclEntry',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN'
        ),
    },
    'CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable',
            False, 
            [
            _MetaInfoClassMember('atmCurrentStatusChangePVclEntry', REFERENCE_LIST, 'Atmcurrentstatuschangepvclentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN', 'CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry', 
                [], [], 
                '''                Each entry in the table represents a VCL for which
                there is an active row in the atmVclTable having an
                atmVclConnKind value of `pvc' and atmVclOperStatus
                to have changed in the last PVC notification interval.
                ''',
                'atmcurrentstatuschangepvclentry',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN',
            'atmCurrentStatusChangePVclTable',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN'
        ),
    },
    'CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', True),
            _MetaInfoClassMember('rangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index to represent different ranges, the first range is 
                indexed by value 0, the second by 1 and so on...
                ''',
                'rangeindex',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', True),
            _MetaInfoClassMember('atmPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVcls for which the 
                atmOperStatus to have changed in the last 
                notification interval.
                ''',
                'atmpvclhigherrangevalue',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVcls for which the 
                atmVclOperStatus to have changed in the last 
                notification interval.
                ''',
                'atmpvcllowerrangevalue',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmPVclRangeStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last notification interval.
                ''',
                'atmpvclrangestatuschangeend',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmPVclRangeStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first PVCL in the range
                changed state in the last notification interval.
                ''',
                'atmpvclrangestatuschangestart',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN',
            'atmStatusChangePVclRangeEntry',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN'
        ),
    },
    'CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable',
            False, 
            [
            _MetaInfoClassMember('atmStatusChangePVclRangeEntry', REFERENCE_LIST, 'Atmstatuschangepvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN', 'CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
                changed in the same direction in the last notification 
                interval.
                ''',
                'atmstatuschangepvclrangeentry',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN',
            'atmStatusChangePVclRangeTable',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN'
        ),
    },
    'CiscoIetfAtm2PvctrapMibExtn' : {
        'meta_info' : _MetaInfoClass('CiscoIetfAtm2PvctrapMibExtn',
            False, 
            [
            _MetaInfoClassMember('atmCurrentStatusChangePVclTable', REFERENCE_CLASS, 'Atmcurrentstatuschangepvcltable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN', 'CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable', 
                [], [], 
                '''                A table indicating all VCLs for which there is an
                active row in the atmVclTable having an atmVclConnKind
                value of `pvc' and atmVclOperStatus to have changed in the
                last PVC notification interval.
                ''',
                'atmcurrentstatuschangepvcltable',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            _MetaInfoClassMember('atmStatusChangePVclRangeTable', REFERENCE_CLASS, 'Atmstatuschangepvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN', 'CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have changed in the same
                direction in the last PVC notification interval.
                ''',
                'atmstatuschangepvclrangetable',
                'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN',
            'CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_ATM2_PVCTRAP_MIB_EXTN'
        ),
    },
}
_meta_table['CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable.Atmcurrentstatuschangepvclentry']['meta_info'].parent =_meta_table['CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable']['meta_info']
_meta_table['CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable.Atmstatuschangepvclrangeentry']['meta_info'].parent =_meta_table['CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable']['meta_info']
_meta_table['CiscoIetfAtm2PvctrapMibExtn.Atmcurrentstatuschangepvcltable']['meta_info'].parent =_meta_table['CiscoIetfAtm2PvctrapMibExtn']['meta_info']
_meta_table['CiscoIetfAtm2PvctrapMibExtn.Atmstatuschangepvclrangetable']['meta_info'].parent =_meta_table['CiscoIetfAtm2PvctrapMibExtn']['meta_info']
