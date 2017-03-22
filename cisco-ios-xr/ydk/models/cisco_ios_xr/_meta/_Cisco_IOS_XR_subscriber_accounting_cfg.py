


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration',
            False, 
            [
            _MetaInfoClassMember('prepaid-config-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Prepaid configuration name or default
                ''',
                'prepaid_config_name',
                'Cisco-IOS-XR-subscriber-accounting-cfg', True),
            _MetaInfoClassMember('accounting-method-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Method list to be used when placing prepaid
                accounting requests
                ''',
                'accounting_method_list',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('author-method-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Method list to be used when placing prepaid
                (re)authorization requests
                ''',
                'author_method_list',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Password to be used when placing prepaid
                (re)authorization requests
                ''',
                'password',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('time-hold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Idle Threshold for which prepaid quota is
                valid
                ''',
                'time_hold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('time-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold at which to send prepaid time quota
                request
                ''',
                'time_threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('time-valid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold for which prepaid quota is valid
                ''',
                'time_valid',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('traffic-direction', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prepaid quota traffic direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            _MetaInfoClassMember('volume-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold at which to send prepaid volume
                quota request
                ''',
                'volume_threshold',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'prepaid-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg'
        ),
    },
    'SubscriberAccounting.PrepaidConfigurations' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.PrepaidConfigurations',
            False, 
            [
            _MetaInfoClassMember('prepaid-configuration', REFERENCE_LIST, 'PrepaidConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg', 'SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration', 
                [], [], 
                '''                Prepaid configuration name or default
                ''',
                'prepaid_configuration',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'prepaid-configurations',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg'
        ),
    },
    'SubscriberAccounting' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting',
            False, 
            [
            _MetaInfoClassMember('prepaid-configurations', REFERENCE_CLASS, 'PrepaidConfigurations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg', 'SubscriberAccounting.PrepaidConfigurations', 
                [], [], 
                '''                Subscriber Prepaid Feature Configuration
                ''',
                'prepaid_configurations',
                'Cisco-IOS-XR-subscriber-accounting-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-cfg',
            'subscriber-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_cfg'
        ),
    },
}
_meta_table['SubscriberAccounting.PrepaidConfigurations.PrepaidConfiguration']['meta_info'].parent =_meta_table['SubscriberAccounting.PrepaidConfigurations']['meta_info']
_meta_table['SubscriberAccounting.PrepaidConfigurations']['meta_info'].parent =_meta_table['SubscriberAccounting']['meta_info']
