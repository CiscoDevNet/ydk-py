
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Native.Interface.Fastethernet.Switchport.PortSecurity.Maximum.max_addresses' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('max-addresses', ATTRIBUTE, 'int' , None, None, 
                    [('1', '4096')], [], 
                    '''                    ''',
                    'max_addresses',
                    'Cisco-IOS-XE-switch', False),
            ),
        ]
    },
    'Native.Interface.Gigabitethernet.Switchport.PortSecurity.Maximum.max_addresses' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('max-addresses', ATTRIBUTE, 'int' , None, None, 
                    [('1', '4096')], [], 
                    '''                    ''',
                    'max_addresses',
                    'Cisco-IOS-XE-switch', False),
            ),
        ]
    },
    'Native.Interface.PortChannel.Switchport.PortSecurity.Maximum.max_addresses' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('max-addresses', ATTRIBUTE, 'int' , None, None, 
                    [('1', '4096')], [], 
                    '''                    ''',
                    'max_addresses',
                    'Cisco-IOS-XE-switch', False),
            ),
        ]
    },
    'Native.Interface.PortChannelSubinterface.PortChannel.Switchport.PortSecurity.Maximum.max_addresses' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('max-addresses', ATTRIBUTE, 'int' , None, None, 
                    [('1', '4096')], [], 
                    '''                    ''',
                    'max_addresses',
                    'Cisco-IOS-XE-switch', False),
            ),
        ]
    },
    'Native.Interface.Tengigabitethernet.Switchport.PortSecurity.Maximum.max_addresses' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('max-addresses', ATTRIBUTE, 'int' , None, None, 
                    [('1', '4096')], [], 
                    '''                    ''',
                    'max_addresses',
                    'Cisco-IOS-XE-switch', False),
            ),
        ]
    },
    'Native.Line.Vty.first' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('first', ATTRIBUTE, 'int' , None, None, 
                    [('0', '97')], [], 
                    '''                    ''',
                    'first',
                    'Cisco-IOS-XE-native', False),
            ),
        ]
    },
    'Native.Line.Vty.last' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                    [('1', '97')], [], 
                    '''                    ''',
                    'last',
                    'Cisco-IOS-XE-native', False),
            ),
        ]
    },
    'Native.Policy.ClassMap.Match.AccessGroup.index' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                    [('1', '2799')], [], 
                    '''                    ''',
                    'index',
                    'Cisco-IOS-XE-policy', False),
            ),
        ]
    },
    'Native.Policy.PolicyMap.Class_.ActionList.action_param.bandwidth_case.Bandwidth.bits' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('bits', ATTRIBUTE, 'int' , None, None, 
                    [('100', '40000000')], [], 
                    '''                    ''',
                    'bits',
                    'Cisco-IOS-XE-policy', False),
            ),
        ]
    },
    'Native.Policy.PolicyMap.Class_.ActionList.action_param.priority_case.Priority.priority_type.kilo_bits.kilo_bits' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('kilo-bits', ATTRIBUTE, 'int' , None, None, 
                    [('8', '40000000')], [], 
                    '''                    ''',
                    'kilo_bits',
                    'Cisco-IOS-XE-policy', False),
            ),
        ]
    },
}
