


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoImageIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                A sequence number for each string stored
                in the IOS image.
                ''',
                'ciscoimageindex',
                'CISCO-IMAGE-MIB', True),
            _MetaInfoClassMember('ciscoImageString', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The string of this entry.
                ''',
                'ciscoimagestring',
                'CISCO-IMAGE-MIB', False),
            ],
            'CISCO-IMAGE-MIB',
            'ciscoImageEntry',
            _yang_ns._namespaces['CISCO-IMAGE-MIB'],
        'ydk.models.image.CISCO_IMAGE_MIB'
        ),
    },
    'CISCOIMAGEMIB.CiscoImageTable' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGEMIB.CiscoImageTable',
            False, 
            [
            _MetaInfoClassMember('ciscoImageEntry', REFERENCE_LIST, 'CiscoImageEntry' , 'ydk.models.image.CISCO_IMAGE_MIB', 'CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry', 
                [], [], 
                '''                A image characteristic string entry.
                ''',
                'ciscoimageentry',
                'CISCO-IMAGE-MIB', False),
            ],
            'CISCO-IMAGE-MIB',
            'ciscoImageTable',
            _yang_ns._namespaces['CISCO-IMAGE-MIB'],
        'ydk.models.image.CISCO_IMAGE_MIB'
        ),
    },
    'CISCOIMAGEMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIMAGEMIB',
            False, 
            [
            _MetaInfoClassMember('ciscoImageTable', REFERENCE_CLASS, 'CiscoImageTable' , 'ydk.models.image.CISCO_IMAGE_MIB', 'CISCOIMAGEMIB.CiscoImageTable', 
                [], [], 
                '''                A table provides content information describing the
                executing IOS image.
                ''',
                'ciscoimagetable',
                'CISCO-IMAGE-MIB', False),
            ],
            'CISCO-IMAGE-MIB',
            'CISCO-IMAGE-MIB',
            _yang_ns._namespaces['CISCO-IMAGE-MIB'],
        'ydk.models.image.CISCO_IMAGE_MIB'
        ),
    },
}
_meta_table['CISCOIMAGEMIB.CiscoImageTable.CiscoImageEntry']['meta_info'].parent =_meta_table['CISCOIMAGEMIB.CiscoImageTable']['meta_info']
_meta_table['CISCOIMAGEMIB.CiscoImageTable']['meta_info'].parent =_meta_table['CISCOIMAGEMIB']['meta_info']
