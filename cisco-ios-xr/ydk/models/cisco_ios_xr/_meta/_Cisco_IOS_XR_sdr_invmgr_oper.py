


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SdrInventory.Racks.Rack.Slot.Card.Attributes' : {
        'meta_info' : _MetaInfoClass('SdrInventory.Racks.Rack.Slot.Card.Attributes',
            False, 
            [
            _MetaInfoClassMember('card-admin-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Card Admin State
                ''',
                'card_admin_state',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('card-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                CardState
                ''',
                'card_state',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('card-state-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card State String
                ''',
                'card_state_string',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                CardType
                ''',
                'card_type',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('card-type-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card Type String
                ''',
                'card_type_string',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('config-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ConfigState
                ''',
                'config_state',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('config-state-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Config State String
                ''',
                'config_state_string',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('ctype', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                CType
                ''',
                'ctype',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('monitor', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Monitor
                ''',
                'monitor',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('node-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name String
                ''',
                'node_name_string',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('pi-slot-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Pi Slot Number
                ''',
                'pi_slot_number',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Power
                ''',
                'power',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Shutdown
                ''',
                'shutdown',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            _MetaInfoClassMember('vm-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VM State information
                ''',
                'vm_state',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-sdr-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-sdr-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper'
        ),
    },
    'SdrInventory.Racks.Rack.Slot.Card' : {
        'meta_info' : _MetaInfoClass('SdrInventory.Racks.Rack.Slot.Card',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Card
                ''',
                'name',
                'Cisco-IOS-XR-sdr-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper', 'SdrInventory.Racks.Rack.Slot.Card.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-sdr-invmgr-oper',
            'card',
            _yang_ns._namespaces['Cisco-IOS-XR-sdr-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper'
        ),
    },
    'SdrInventory.Racks.Rack.Slot' : {
        'meta_info' : _MetaInfoClass('SdrInventory.Racks.Rack.Slot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Slot name
                ''',
                'name',
                'Cisco-IOS-XR-sdr-invmgr-oper', True),
            _MetaInfoClassMember('card', REFERENCE_LIST, 'Card' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper', 'SdrInventory.Racks.Rack.Slot.Card', 
                [], [], 
                '''                Card
                ''',
                'card',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-sdr-invmgr-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-sdr-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper'
        ),
    },
    'SdrInventory.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('SdrInventory.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Rack name
                ''',
                'name',
                'Cisco-IOS-XR-sdr-invmgr-oper', True),
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper', 'SdrInventory.Racks.Rack.Slot', 
                [], [], 
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-sdr-invmgr-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-sdr-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper'
        ),
    },
    'SdrInventory.Racks' : {
        'meta_info' : _MetaInfoClass('SdrInventory.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper', 'SdrInventory.Racks.Rack', 
                [], [], 
                '''                Rack name
                ''',
                'rack',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-sdr-invmgr-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-sdr-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper'
        ),
    },
    'SdrInventory' : {
        'meta_info' : _MetaInfoClass('SdrInventory',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper', 'SdrInventory.Racks', 
                [], [], 
                '''                RackTable
                ''',
                'racks',
                'Cisco-IOS-XR-sdr-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-sdr-invmgr-oper',
            'sdr-inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-sdr-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper'
        ),
    },
}
_meta_table['SdrInventory.Racks.Rack.Slot.Card.Attributes']['meta_info'].parent =_meta_table['SdrInventory.Racks.Rack.Slot.Card']['meta_info']
_meta_table['SdrInventory.Racks.Rack.Slot.Card']['meta_info'].parent =_meta_table['SdrInventory.Racks.Rack.Slot']['meta_info']
_meta_table['SdrInventory.Racks.Rack.Slot']['meta_info'].parent =_meta_table['SdrInventory.Racks.Rack']['meta_info']
_meta_table['SdrInventory.Racks.Rack']['meta_info'].parent =_meta_table['SdrInventory.Racks']['meta_info']
_meta_table['SdrInventory.Racks']['meta_info'].parent =_meta_table['SdrInventory']['meta_info']
