


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'AssigmentRanges' : {
        'meta_info' : _MetaInfoClass('AssigmentRanges',
            False, 
            [
            _MetaInfoClassMember('entry-point', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest SID available for assignment.
                ''',
                'entry_point',
                'ietf-sid-file', True),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of SIDs available for assignment.
                ''',
                'size',
                'ietf-sid-file', False),
            ],
            'ietf-sid-file',
            'assigment-ranges',
            _yang_ns._namespaces['ietf-sid-file'],
        'ydk.models.ietf.ietf_sid_file'
        ),
    },
    'Items' : {
        'meta_info' : _MetaInfoClass('Items',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label associated to this item, can be set to:
                 - a module name
                 - a submodule name
                 - a feature name
                 - a base identity encoded as '/<base identity name>'
                 - an identity encoded as '/<base identity name>/<identity name>'
                 - a schema node path
                ''',
                'label',
                'ietf-sid-file', True),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], ['Module|Submodule|feature|identity$|node$|notification$|rpc$|action$'], 
                '''                Item type assigned, this field can be set to:
                 - 'Module'
                 - 'Submodule'
                 - 'feature'
                 - 'identity'
                 - 'node'
                 - 'notification'
                 - 'rpc'
                 - 'action'
                ''',
                'type',
                'ietf-sid-file', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier assigned to this YANG item.
                ''',
                'sid',
                'ietf-sid-file', False),
            ],
            'ietf-sid-file',
            'items',
            _yang_ns._namespaces['ietf-sid-file'],
        'ydk.models.ietf.ietf_sid_file'
        ),
    },
}
