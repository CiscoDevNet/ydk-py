


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ActionTypeEnum' : _MetaInfoEnum('ActionTypeEnum', 'ydk.models.ietf.ietf_netconf_acm',
        {
            'permit':'permit',
            'deny':'deny',
        }, 'ietf-netconf-acm', _yang_ns._namespaces['ietf-netconf-acm']),
    'Nacm.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Nacm.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[^\\*].*'], 
                '''                Group name associated with this entry.
                ''',
                'name',
                'ietf-netconf-acm', True),
            _MetaInfoClassMember('user-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, '18446744073709551615')], [], 
                '''                Each entry identifies the username of
                a member of the group associated with
                this entry.
                ''',
                'user_name',
                'ietf-netconf-acm', False),
            ],
            'ietf-netconf-acm',
            'group',
            _yang_ns._namespaces['ietf-netconf-acm'],
        'ydk.models.ietf.ietf_netconf_acm'
        ),
    },
    'Nacm.Groups' : {
        'meta_info' : _MetaInfoClass('Nacm.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.ietf.ietf_netconf_acm', 'Nacm.Groups.Group', 
                [], [], 
                '''                One NACM Group Entry.  This list will only contain
                configured entries, not any entries learned from
                any transport protocols.
                ''',
                'group',
                'ietf-netconf-acm', False),
            ],
            'ietf-netconf-acm',
            'groups',
            _yang_ns._namespaces['ietf-netconf-acm'],
        'ydk.models.ietf.ietf_netconf_acm'
        ),
    },
    'Nacm.RuleList.Rule' : {
        'meta_info' : _MetaInfoClass('Nacm.RuleList.Rule',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, '18446744073709551615')], [], 
                '''                Arbitrary name assigned to the rule.
                ''',
                'name',
                'ietf-netconf-acm', True),
            _MetaInfoClassMember('access-operations', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Access operations associated with this rule.
                
                This leaf matches if it has the value '*' or if the
                bit corresponding to the requested operation is set.
                ''',
                'access_operations',
                'ietf-netconf-acm', False, [
                    _MetaInfoClassMember('access-operations', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\*'], 
                        '''                        Access operations associated with this rule.
                        
                        This leaf matches if it has the value '*' or if the
                        bit corresponding to the requested operation is set.
                        ''',
                        'access_operations',
                        'ietf-netconf-acm', False),
                    _MetaInfoClassMember('access-operations', REFERENCE_BITS, 'AccessOperationsType' , 'ydk.models.ietf.ietf_netconf_acm', 'AccessOperationsType', 
                        [], [], 
                        '''                        Access operations associated with this rule.
                        
                        This leaf matches if it has the value '*' or if the
                        bit corresponding to the requested operation is set.
                        ''',
                        'access_operations',
                        'ietf-netconf-acm', False),
                ]),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'ActionTypeEnum' , 'ydk.models.ietf.ietf_netconf_acm', 'ActionTypeEnum', 
                [], [], 
                '''                The access control action associated with the
                rule.  If a rule is determined to match a
                particular request, then this object is used
                to determine whether to permit or deny the
                request.
                ''',
                'action',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the access rule.
                ''',
                'comment',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('module-name', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Name of the module associated with this rule.
                
                This leaf matches if it has the value '*' or if the
                object being accessed is defined in the module with the
                specified module name.
                ''',
                'module_name',
                'ietf-netconf-acm', False, [
                    _MetaInfoClassMember('module-name', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\*'], 
                        '''                        Name of the module associated with this rule.
                        
                        This leaf matches if it has the value '*' or if the
                        object being accessed is defined in the module with the
                        specified module name.
                        ''',
                        'module_name',
                        'ietf-netconf-acm', False),
                    _MetaInfoClassMember('module-name', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Name of the module associated with this rule.
                        
                        This leaf matches if it has the value '*' or if the
                        object being accessed is defined in the module with the
                        specified module name.
                        ''',
                        'module_name',
                        'ietf-netconf-acm', False),
                ]),
            _MetaInfoClassMember('notification-name', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This leaf matches if it has the value '*' or if its
                value equals the requested notification name.
                ''',
                'notification_name',
                'ietf-netconf-acm', False, [
                    _MetaInfoClassMember('notification-name', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\*'], 
                        '''                        This leaf matches if it has the value '*' or if its
                        value equals the requested notification name.
                        ''',
                        'notification_name',
                        'ietf-netconf-acm', False),
                    _MetaInfoClassMember('notification-name', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        This leaf matches if it has the value '*' or if its
                        value equals the requested notification name.
                        ''',
                        'notification_name',
                        'ietf-netconf-acm', False),
                ]),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Data Node Instance Identifier associated with the
                data node controlled by this rule.
                
                Configuration data or state data instance
                identifiers start with a top-level data node.  A
                complete instance identifier is required for this
                type of path value.
                
                The special value '/' refers to all possible
                datastore contents.
                ''',
                'path',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('rpc-name', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This leaf matches if it has the value '*' or if
                its value equals the requested protocol operation
                name.
                ''',
                'rpc_name',
                'ietf-netconf-acm', False, [
                    _MetaInfoClassMember('rpc-name', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\*'], 
                        '''                        This leaf matches if it has the value '*' or if
                        its value equals the requested protocol operation
                        name.
                        ''',
                        'rpc_name',
                        'ietf-netconf-acm', False),
                    _MetaInfoClassMember('rpc-name', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        This leaf matches if it has the value '*' or if
                        its value equals the requested protocol operation
                        name.
                        ''',
                        'rpc_name',
                        'ietf-netconf-acm', False),
                ]),
            ],
            'ietf-netconf-acm',
            'rule',
            _yang_ns._namespaces['ietf-netconf-acm'],
        'ydk.models.ietf.ietf_netconf_acm'
        ),
    },
    'Nacm.RuleList' : {
        'meta_info' : _MetaInfoClass('Nacm.RuleList',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, '18446744073709551615')], [], 
                '''                Arbitrary name assigned to the rule-list.
                ''',
                'name',
                'ietf-netconf-acm', True),
            _MetaInfoClassMember('group', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of administrative groups that will be
                assigned the associated access rights
                defined by the 'rule' list.
                
                The string '*' indicates that all groups apply to the
                entry.
                ''',
                'group',
                'ietf-netconf-acm', False, [
                    _MetaInfoClassMember('group', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'\\*'], 
                        '''                        List of administrative groups that will be
                        assigned the associated access rights
                        defined by the 'rule' list.
                        
                        The string '*' indicates that all groups apply to the
                        entry.
                        ''',
                        'group',
                        'ietf-netconf-acm', False),
                    _MetaInfoClassMember('group', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'[^\\*].*'], 
                        '''                        List of administrative groups that will be
                        assigned the associated access rights
                        defined by the 'rule' list.
                        
                        The string '*' indicates that all groups apply to the
                        entry.
                        ''',
                        'group',
                        'ietf-netconf-acm', False),
                ]),
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule' , 'ydk.models.ietf.ietf_netconf_acm', 'Nacm.RuleList.Rule', 
                [], [], 
                '''                One access control rule.
                
                Rules are processed in user-defined order until a match is
                found.  A rule matches if 'module-name', 'rule-type', and
                'access-operations' match the request.  If a rule
                matches, the 'action' leaf determines if access is granted
                or not.
                ''',
                'rule',
                'ietf-netconf-acm', False),
            ],
            'ietf-netconf-acm',
            'rule-list',
            _yang_ns._namespaces['ietf-netconf-acm'],
        'ydk.models.ietf.ietf_netconf_acm'
        ),
    },
    'Nacm' : {
        'meta_info' : _MetaInfoClass('Nacm',
            False, 
            [
            _MetaInfoClassMember('denied-data-writes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times since the server last restarted that a
                protocol operation request to alter
                a configuration datastore was denied.
                ''',
                'denied_data_writes',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('denied-notifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times since the server last restarted that
                a notification was dropped for a subscription because
                access to the event type was denied.
                ''',
                'denied_notifications',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('denied-operations', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times since the server last restarted that a
                protocol operation request was denied.
                ''',
                'denied_operations',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('enable-external-groups', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controls whether the server uses the groups reported by the
                NETCONF transport layer when it assigns the user to a set of
                NACM groups.  If this leaf has the value 'false', any group
                names reported by the transport layer are ignored by the
                server.
                ''',
                'enable_external_groups',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('enable-nacm', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables or disables all NETCONF access control
                enforcement.  If 'true', then enforcement
                is enabled.  If 'false', then enforcement
                is disabled.
                ''',
                'enable_nacm',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('exec-default', REFERENCE_ENUM_CLASS, 'ActionTypeEnum' , 'ydk.models.ietf.ietf_netconf_acm', 'ActionTypeEnum', 
                [], [], 
                '''                Controls whether exec access is granted if no appropriate
                rule is found for a particular protocol operation request.
                ''',
                'exec_default',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.ietf.ietf_netconf_acm', 'Nacm.Groups', 
                [], [], 
                '''                NETCONF Access Control Groups.
                ''',
                'groups',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('read-default', REFERENCE_ENUM_CLASS, 'ActionTypeEnum' , 'ydk.models.ietf.ietf_netconf_acm', 'ActionTypeEnum', 
                [], [], 
                '''                Controls whether read access is granted if
                no appropriate rule is found for a
                particular read request.
                ''',
                'read_default',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('rule-list', REFERENCE_LIST, 'RuleList' , 'ydk.models.ietf.ietf_netconf_acm', 'Nacm.RuleList', 
                [], [], 
                '''                An ordered collection of access control rules.
                ''',
                'rule_list',
                'ietf-netconf-acm', False),
            _MetaInfoClassMember('write-default', REFERENCE_ENUM_CLASS, 'ActionTypeEnum' , 'ydk.models.ietf.ietf_netconf_acm', 'ActionTypeEnum', 
                [], [], 
                '''                Controls whether create, update, or delete access
                is granted if no appropriate rule is found for a
                particular write request.
                ''',
                'write_default',
                'ietf-netconf-acm', False),
            ],
            'ietf-netconf-acm',
            'nacm',
            _yang_ns._namespaces['ietf-netconf-acm'],
        'ydk.models.ietf.ietf_netconf_acm'
        ),
    },
}
_meta_table['Nacm.Groups.Group']['meta_info'].parent =_meta_table['Nacm.Groups']['meta_info']
_meta_table['Nacm.RuleList.Rule']['meta_info'].parent =_meta_table['Nacm.RuleList']['meta_info']
_meta_table['Nacm.Groups']['meta_info'].parent =_meta_table['Nacm']['meta_info']
_meta_table['Nacm.RuleList']['meta_info'].parent =_meta_table['Nacm']['meta_info']
