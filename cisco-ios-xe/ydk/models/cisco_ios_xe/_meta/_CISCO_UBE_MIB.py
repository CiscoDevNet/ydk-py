


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoUbeMib.Ciscoubemibobjects' : {
        'meta_info' : _MetaInfoClass('CiscoUbeMib.Ciscoubemibobjects',
            False, 
            [
            _MetaInfoClassMember('cubeEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object represents, whether the Cisco
                Unified Border Element (CUBE) is enabled 
                on the device or not.
                
                The value 'true' means that the CUBE feature 
                is enabled on the device.
                
                The value 'false' means that the CUBE feature 
                is disabled.
                ''',
                'cubeenabled',
                'CISCO-UBE-MIB', False),
            _MetaInfoClassMember('cubeTotalSessionAllowed', ATTRIBUTE, 'int' , None, None, 
                [('0', '999999')], [], 
                '''                This object provides the total number of CUBE
                session allowed on the device. The value zero 
                means no sessions are allowed with CUBE.
                ''',
                'cubetotalsessionallowed',
                'CISCO-UBE-MIB', False),
            _MetaInfoClassMember('cubeVersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object represents the version of Cisco
                Unified Border Element on the device.
                ''',
                'cubeversion',
                'CISCO-UBE-MIB', False),
            ],
            'CISCO-UBE-MIB',
            'ciscoUbeMIBObjects',
            _yang_ns._namespaces['CISCO-UBE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_UBE_MIB'
        ),
    },
    'CiscoUbeMib' : {
        'meta_info' : _MetaInfoClass('CiscoUbeMib',
            False, 
            [
            _MetaInfoClassMember('ciscoUbeMIBObjects', REFERENCE_CLASS, 'Ciscoubemibobjects' , 'ydk.models.cisco_ios_xe.CISCO_UBE_MIB', 'CiscoUbeMib.Ciscoubemibobjects', 
                [], [], 
                '''                ''',
                'ciscoubemibobjects',
                'CISCO-UBE-MIB', False),
            ],
            'CISCO-UBE-MIB',
            'CISCO-UBE-MIB',
            _yang_ns._namespaces['CISCO-UBE-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_UBE_MIB'
        ),
    },
}
_meta_table['CiscoUbeMib.Ciscoubemibobjects']['meta_info'].parent =_meta_table['CiscoUbeMib']['meta_info']
