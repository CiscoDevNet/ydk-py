


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoImageMib.Ciscoimagetable.Ciscoimageentry' : {
        'meta_info' : _MetaInfoClass('CiscoImageMib.Ciscoimagetable.Ciscoimageentry',
            False, 
            [
            _MetaInfoClassMember('ciscoImageIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                A sequence number for each string stored
                in the IOS image.
                ''',
                'ciscoimageindex',
                'CISCO-IMAGE-MIB', True),
            _MetaInfoClassMember('ciscoImageString', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The string of this entry.
                ''',
                'ciscoimagestring',
                'CISCO-IMAGE-MIB', False),
            ],
            'CISCO-IMAGE-MIB',
            'ciscoImageEntry',
            _yang_ns._namespaces['CISCO-IMAGE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB'
        ),
    },
    'CiscoImageMib.Ciscoimagetable' : {
        'meta_info' : _MetaInfoClass('CiscoImageMib.Ciscoimagetable',
            False, 
            [
            _MetaInfoClassMember('ciscoImageEntry', REFERENCE_LIST, 'Ciscoimageentry' , 'ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB', 'CiscoImageMib.Ciscoimagetable.Ciscoimageentry', 
                [], [], 
                '''                A image characteristic string entry.
                ''',
                'ciscoimageentry',
                'CISCO-IMAGE-MIB', False),
            ],
            'CISCO-IMAGE-MIB',
            'ciscoImageTable',
            _yang_ns._namespaces['CISCO-IMAGE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB'
        ),
    },
    'CiscoImageMib' : {
        'meta_info' : _MetaInfoClass('CiscoImageMib',
            False, 
            [
            _MetaInfoClassMember('ciscoImageTable', REFERENCE_CLASS, 'Ciscoimagetable' , 'ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB', 'CiscoImageMib.Ciscoimagetable', 
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
        'ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB'
        ),
    },
}
_meta_table['CiscoImageMib.Ciscoimagetable.Ciscoimageentry']['meta_info'].parent =_meta_table['CiscoImageMib.Ciscoimagetable']['meta_info']
_meta_table['CiscoImageMib.Ciscoimagetable']['meta_info'].parent =_meta_table['CiscoImageMib']['meta_info']
