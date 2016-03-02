


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable.AtmCurrentlyFailingPVclEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable.AtmCurrentlyFailingPVclEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', True),
            _MetaInfoClassMember('atmCurrentlyFailingPVclTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time at which this PVCL began to fail.
                ''',
                'atmcurrentlyfailingpvcltimestamp',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            _MetaInfoClassMember('atmPreviouslyFailedPVclTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time at which this PVCL began to fail
                during the PVC Notification interval.
                ''',
                'atmpreviouslyfailedpvcltimestamp',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB',
            'atmCurrentlyFailingPVclEntry',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB'],
        'ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB'
        ),
    },
    'CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable',
            False, 
            [
            _MetaInfoClassMember('atmCurrentlyFailingPVclEntry', REFERENCE_LIST, 'AtmCurrentlyFailingPVclEntry' , 'ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB', 'CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable.AtmCurrentlyFailingPVclEntry', 
                [], [], 
                '''                Each entry in this table represents a VCL for which
                the atmVclRowStatus is `active', the atmVclConnKind is
                `pvc', and the atmVclOperStatus is other than `up'.
                ''',
                'atmcurrentlyfailingpvclentry',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB',
            'atmCurrentlyFailingPVclTable',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB'],
        'ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB'
        ),
    },
    'CISCOIETFATM2PVCTRAPMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIETFATM2PVCTRAPMIB',
            False, 
            [
            _MetaInfoClassMember('atmCurrentlyFailingPVclTable', REFERENCE_CLASS, 'AtmCurrentlyFailingPVclTable' , 'ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB', 'CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable', 
                [], [], 
                '''                A table indicating all VCLs for which there is an
                active row in the atmVclTable having an atmVclConnKind
                value of `pvc' and an atmVclOperStatus with a value
                other than `up'.
                ''',
                'atmcurrentlyfailingpvcltable',
                'CISCO-IETF-ATM2-PVCTRAP-MIB', False),
            ],
            'CISCO-IETF-ATM2-PVCTRAP-MIB',
            'CISCO-IETF-ATM2-PVCTRAP-MIB',
            _yang_ns._namespaces['CISCO-IETF-ATM2-PVCTRAP-MIB'],
        'ydk.models.ietf.CISCO_IETF_ATM2_PVCTRAP_MIB'
        ),
    },
}
_meta_table['CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable.AtmCurrentlyFailingPVclEntry']['meta_info'].parent =_meta_table['CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable']['meta_info']
_meta_table['CISCOIETFATM2PVCTRAPMIB.AtmCurrentlyFailingPVclTable']['meta_info'].parent =_meta_table['CISCOIETFATM2PVCTRAPMIB']['meta_info']
