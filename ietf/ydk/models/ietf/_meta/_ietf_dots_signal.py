


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'MitigationScope.Scope.TargetPortRange' : {
        'meta_info' : _MetaInfoClass('MitigationScope.Scope.TargetPortRange',
            False, 
            [
            _MetaInfoClassMember('lower-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                lower port
                ''',
                'lower_port',
                'ietf-dots-signal', True),
            _MetaInfoClassMember('upper-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                upper port
                ''',
                'upper_port',
                'ietf-dots-signal', True),
            ],
            'ietf-dots-signal',
            'target-port-range',
            _yang_ns._namespaces['ietf-dots-signal'],
        'ydk.models.ietf.ietf_dots_signal'
        ),
    },
    'MitigationScope.Scope' : {
        'meta_info' : _MetaInfoClass('MitigationScope.Scope',
            False, 
            [
            _MetaInfoClassMember('policy-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                policy identifier
                ''',
                'policy_id',
                'ietf-dots-signal', True),
            _MetaInfoClassMember('alias', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                alias name
                ''',
                'alias',
                'ietf-dots-signal', False),
            _MetaInfoClassMember('E.164', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                E.164 number
                ''',
                'e_164',
                'ietf-dots-signal', False),
            _MetaInfoClassMember('FQDN', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                '''                FQDN
                ''',
                'fqdn',
                'ietf-dots-signal', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                lifetime
                ''',
                'lifetime',
                'ietf-dots-signal', False),
            _MetaInfoClassMember('target-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address
                ''',
                'target_ip',
                'ietf-dots-signal', False, [
                    _MetaInfoClassMember('target-ip', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'target_ip',
                        'ietf-dots-signal', False),
                    _MetaInfoClassMember('target-ip', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'target_ip',
                        'ietf-dots-signal', False),
                ]),
            _MetaInfoClassMember('target-port-range', REFERENCE_LIST, 'TargetPortRange' , 'ydk.models.ietf.ietf_dots_signal', 'MitigationScope.Scope.TargetPortRange', 
                [], [], 
                '''                Port range. When only lower-port is present,
                it represents a single port.
                ''',
                'target_port_range',
                'ietf-dots-signal', False),
            _MetaInfoClassMember('target-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'target_prefix',
                'ietf-dots-signal', False, [
                    _MetaInfoClassMember('target-prefix', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix
                        ''',
                        'target_prefix',
                        'ietf-dots-signal', False),
                    _MetaInfoClassMember('target-prefix', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix
                        ''',
                        'target_prefix',
                        'ietf-dots-signal', False),
                ]),
            _MetaInfoClassMember('target-protocol', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Internet Protocol number
                ''',
                'target_protocol',
                'ietf-dots-signal', False),
            _MetaInfoClassMember('URI', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                URI
                ''',
                'uri',
                'ietf-dots-signal', False),
            ],
            'ietf-dots-signal',
            'scope',
            _yang_ns._namespaces['ietf-dots-signal'],
        'ydk.models.ietf.ietf_dots_signal'
        ),
    },
    'MitigationScope' : {
        'meta_info' : _MetaInfoClass('MitigationScope',
            False, 
            [
            _MetaInfoClassMember('scope', REFERENCE_LIST, 'Scope' , 'ydk.models.ietf.ietf_dots_signal', 'MitigationScope.Scope', 
                [], [], 
                '''                Identifier for the mitigation request
                ''',
                'scope',
                'ietf-dots-signal', False),
            ],
            'ietf-dots-signal',
            'mitigation-scope',
            _yang_ns._namespaces['ietf-dots-signal'],
        'ydk.models.ietf.ietf_dots_signal'
        ),
    },
}
_meta_table['MitigationScope.Scope.TargetPortRange']['meta_info'].parent =_meta_table['MitigationScope.Scope']['meta_info']
_meta_table['MitigationScope.Scope']['meta_info'].parent =_meta_table['MitigationScope']['meta_info']
