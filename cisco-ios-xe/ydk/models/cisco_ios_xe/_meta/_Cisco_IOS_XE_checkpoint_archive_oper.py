


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CheckpointArchive.Archives.Archive' : {
        'meta_info' : _MetaInfoClass('CheckpointArchive.Archives.Archive',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The archive number
                ''',
                'number',
                'Cisco-IOS-XE-checkpoint-archive-oper', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                the name of the archive
                ''',
                'name',
                'Cisco-IOS-XE-checkpoint-archive-oper', False),
            ],
            'Cisco-IOS-XE-checkpoint-archive-oper',
            'archive',
            _yang_ns._namespaces['Cisco-IOS-XE-checkpoint-archive-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper'
        ),
    },
    'CheckpointArchive.Archives' : {
        'meta_info' : _MetaInfoClass('CheckpointArchive.Archives',
            False, 
            [
            _MetaInfoClassMember('archive', REFERENCE_LIST, 'Archive' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper', 'CheckpointArchive.Archives.Archive', 
                [], [], 
                '''                Archive information
                ''',
                'archive',
                'Cisco-IOS-XE-checkpoint-archive-oper', False),
            ],
            'Cisco-IOS-XE-checkpoint-archive-oper',
            'archives',
            _yang_ns._namespaces['Cisco-IOS-XE-checkpoint-archive-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper'
        ),
    },
    'CheckpointArchive' : {
        'meta_info' : _MetaInfoClass('CheckpointArchive',
            False, 
            [
            _MetaInfoClassMember('archives', REFERENCE_CLASS, 'Archives' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper', 'CheckpointArchive.Archives', 
                [], [], 
                '''                ''',
                'archives',
                'Cisco-IOS-XE-checkpoint-archive-oper', False),
            _MetaInfoClassMember('current', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The current number of archives
                ''',
                'current',
                'Cisco-IOS-XE-checkpoint-archive-oper', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The maxium number of archives
                ''',
                'max',
                'Cisco-IOS-XE-checkpoint-archive-oper', False),
            _MetaInfoClassMember('recent', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The most recent archive
                ''',
                'recent',
                'Cisco-IOS-XE-checkpoint-archive-oper', False),
            ],
            'Cisco-IOS-XE-checkpoint-archive-oper',
            'checkpoint-archive',
            _yang_ns._namespaces['Cisco-IOS-XE-checkpoint-archive-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper'
        ),
    },
}
_meta_table['CheckpointArchive.Archives.Archive']['meta_info'].parent =_meta_table['CheckpointArchive.Archives']['meta_info']
_meta_table['CheckpointArchive.Archives']['meta_info'].parent =_meta_table['CheckpointArchive']['meta_info']
