


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData' : {
        'meta_info' : _MetaInfoClass('AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData',
            False, 
            [
            _MetaInfoClassMember('match-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of matches for an access list entry
                ''',
                'match_counter',
                'Cisco-IOS-XE-acl-oper', False),
            ],
            'Cisco-IOS-XE-acl-oper',
            'access-list-entries-oper-data',
            _yang_ns._namespaces['Cisco-IOS-XE-acl-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper'
        ),
    },
    'AccessLists.AccessList.AccessListEntries.AccessListEntry' : {
        'meta_info' : _MetaInfoClass('AccessLists.AccessList.AccessListEntries.AccessListEntry',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Entry number.
                ''',
                'rule_name',
                'Cisco-IOS-XE-acl-oper', True),
            _MetaInfoClassMember('access-list-entries-oper-data', REFERENCE_CLASS, 'AccessListEntriesOperData' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper', 'AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData', 
                [], [], 
                '''                Per access list entries operational data
                ''',
                'access_list_entries_oper_data',
                'Cisco-IOS-XE-acl-oper', False),
            ],
            'Cisco-IOS-XE-acl-oper',
            'access-list-entry',
            _yang_ns._namespaces['Cisco-IOS-XE-acl-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper'
        ),
    },
    'AccessLists.AccessList.AccessListEntries' : {
        'meta_info' : _MetaInfoClass('AccessLists.AccessList.AccessListEntries',
            False, 
            [
            _MetaInfoClassMember('access-list-entry', REFERENCE_LIST, 'AccessListEntry' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper', 'AccessLists.AccessList.AccessListEntries.AccessListEntry', 
                [], [], 
                '''                List of access list entries(ACE)
                ''',
                'access_list_entry',
                'Cisco-IOS-XE-acl-oper', False),
            ],
            'Cisco-IOS-XE-acl-oper',
            'access-list-entries',
            _yang_ns._namespaces['Cisco-IOS-XE-acl-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper'
        ),
    },
    'AccessLists.AccessList' : {
        'meta_info' : _MetaInfoClass('AccessLists.AccessList',
            False, 
            [
            _MetaInfoClassMember('access-control-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of access-list. A device MAY restrict the length
                and value of this name, possibly space and special characters are not
                allowed
                ''',
                'access_control_list_name',
                'Cisco-IOS-XE-acl-oper', True),
            _MetaInfoClassMember('access-list-entries', REFERENCE_CLASS, 'AccessListEntries' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper', 'AccessLists.AccessList.AccessListEntries', 
                [], [], 
                '''                A list of access-list-entry(ACE)
                ''',
                'access_list_entries',
                'Cisco-IOS-XE-acl-oper', False),
            ],
            'Cisco-IOS-XE-acl-oper',
            'access-list',
            _yang_ns._namespaces['Cisco-IOS-XE-acl-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper'
        ),
    },
    'AccessLists' : {
        'meta_info' : _MetaInfoClass('AccessLists',
            False, 
            [
            _MetaInfoClassMember('access-list', REFERENCE_LIST, 'AccessList' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper', 'AccessLists.AccessList', 
                [], [], 
                '''                An access list (acl) is an ordered list of
                access list entries (ACE). Each access control entries has a
                list of match criteria, and a list of actions.
                Since there are several kinds of access control lists
                implemented with different attributes for
                each and different for each vendor, this
                model accommodates customizing access control lists for
                each kind and for each vendor.
                ''',
                'access_list',
                'Cisco-IOS-XE-acl-oper', False),
            ],
            'Cisco-IOS-XE-acl-oper',
            'access-lists',
            _yang_ns._namespaces['Cisco-IOS-XE-acl-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper'
        ),
    },
}
_meta_table['AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData']['meta_info'].parent =_meta_table['AccessLists.AccessList.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['AccessLists.AccessList.AccessListEntries.AccessListEntry']['meta_info'].parent =_meta_table['AccessLists.AccessList.AccessListEntries']['meta_info']
_meta_table['AccessLists.AccessList.AccessListEntries']['meta_info'].parent =_meta_table['AccessLists.AccessList']['meta_info']
_meta_table['AccessLists.AccessList']['meta_info'].parent =_meta_table['AccessLists']['meta_info']
