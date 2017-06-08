


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Identifier.Alias.PortRange' : {
        'meta_info' : _MetaInfoClass('Identifier.Alias.PortRange',
            False, 
            [
            _MetaInfoClassMember('lower-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                lower port
                ''',
                'lower_port',
                'ietf-dots-data-channel-identifier', True),
            _MetaInfoClassMember('upper-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                upper port
                ''',
                'upper_port',
                'ietf-dots-data-channel-identifier', True),
            ],
            'ietf-dots-data-channel-identifier',
            'port-range',
            _yang_ns._namespaces['ietf-dots-data-channel-identifier'],
        'ydk.models.ietf.ietf_dots_data_channel_identifier'
        ),
    },
    'Identifier.Alias' : {
        'meta_info' : _MetaInfoClass('Identifier.Alias',
            False, 
            [
            _MetaInfoClassMember('alias-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                alias name
                ''',
                'alias_name',
                'ietf-dots-data-channel-identifier', True),
            _MetaInfoClassMember('E.164', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                E.164 number
                ''',
                'e_164',
                'ietf-dots-data-channel-identifier', False),
            _MetaInfoClassMember('FQDN', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                '''                FQDN
                ''',
                'fqdn',
                'ietf-dots-data-channel-identifier', False),
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address
                ''',
                'ip',
                'ietf-dots-data-channel-identifier', False, [
                    _MetaInfoClassMember('ip', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'ip',
                        'ietf-dots-data-channel-identifier', False),
                    _MetaInfoClassMember('ip', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'ip',
                        'ietf-dots-data-channel-identifier', False),
                ]),
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.ietf.ietf_dots_data_channel_identifier', 'Identifier.Alias.PortRange', 
                [], [], 
                '''                Port range. When only lower-port is present,
                it represents a single port.
                ''',
                'port_range',
                'ietf-dots-data-channel-identifier', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'prefix',
                'ietf-dots-data-channel-identifier', False, [
                    _MetaInfoClassMember('prefix', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix
                        ''',
                        'prefix',
                        'ietf-dots-data-channel-identifier', False),
                    _MetaInfoClassMember('prefix', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix
                        ''',
                        'prefix',
                        'ietf-dots-data-channel-identifier', False),
                ]),
            _MetaInfoClassMember('traffic-protocol', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Internet Protocol number
                ''',
                'traffic_protocol',
                'ietf-dots-data-channel-identifier', False),
            _MetaInfoClassMember('URI', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                URI
                ''',
                'uri',
                'ietf-dots-data-channel-identifier', False),
            ],
            'ietf-dots-data-channel-identifier',
            'alias',
            _yang_ns._namespaces['ietf-dots-data-channel-identifier'],
        'ydk.models.ietf.ietf_dots_data_channel_identifier'
        ),
    },
    'Identifier' : {
        'meta_info' : _MetaInfoClass('Identifier',
            False, 
            [
            _MetaInfoClassMember('alias', REFERENCE_LIST, 'Alias' , 'ydk.models.ietf.ietf_dots_data_channel_identifier', 'Identifier.Alias', 
                [], [], 
                '''                list of identifiers
                ''',
                'alias',
                'ietf-dots-data-channel-identifier', False),
            ],
            'ietf-dots-data-channel-identifier',
            'identifier',
            _yang_ns._namespaces['ietf-dots-data-channel-identifier'],
        'ydk.models.ietf.ietf_dots_data_channel_identifier'
        ),
    },
}
_meta_table['Identifier.Alias.PortRange']['meta_info'].parent =_meta_table['Identifier.Alias']['meta_info']
_meta_table['Identifier.Alias']['meta_info'].parent =_meta_table['Identifier']['meta_info']
