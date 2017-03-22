


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VlanModeTypeEnum' : _MetaInfoEnum('VlanModeTypeEnum', 'ydk.models.openconfig.openconfig_vlan',
        {
            'ACCESS':'ACCESS',
            'TRUNK':'TRUNK',
        }, 'openconfig-vlan', _yang_ns._namespaces['openconfig-vlan']),
    'Vlans.Vlan.Config.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.openconfig.openconfig_vlan',
        {
            'ACTIVE':'ACTIVE',
            'SUSPENDED':'SUSPENDED',
        }, 'openconfig-vlan', _yang_ns._namespaces['openconfig-vlan']),
    'Vlans.Vlan.Config' : {
        'meta_info' : _MetaInfoClass('Vlans.Vlan.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface VLAN name.
                ''',
                'name',
                'openconfig-vlan', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.openconfig.openconfig_vlan', 'Vlans.Vlan.Config.StatusEnum', 
                [], [], 
                '''                Admin state of the VLAN
                ''',
                'status',
                'openconfig-vlan', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Interface VLAN id.
                ''',
                'vlan_id',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'config',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_vlan'
        ),
    },
    'Vlans.Vlan.State.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.openconfig.openconfig_vlan',
        {
            'ACTIVE':'ACTIVE',
            'SUSPENDED':'SUSPENDED',
        }, 'openconfig-vlan', _yang_ns._namespaces['openconfig-vlan']),
    'Vlans.Vlan.State' : {
        'meta_info' : _MetaInfoClass('Vlans.Vlan.State',
            False, 
            [
            _MetaInfoClassMember('member-ports', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of current member ports including access ports
                and trunk ports that support this vlan
                ''',
                'member_ports',
                'openconfig-vlan', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface VLAN name.
                ''',
                'name',
                'openconfig-vlan', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.openconfig.openconfig_vlan', 'Vlans.Vlan.State.StatusEnum', 
                [], [], 
                '''                Admin state of the VLAN
                ''',
                'status',
                'openconfig-vlan', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Interface VLAN id.
                ''',
                'vlan_id',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'state',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_vlan'
        ),
    },
    'Vlans.Vlan' : {
        'meta_info' : _MetaInfoClass('Vlans.Vlan',
            False, 
            [
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                references the configured vlan-id
                ''',
                'vlan_id',
                'openconfig-vlan', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_vlan', 'Vlans.Vlan.Config', 
                [], [], 
                '''                Configuration parameters for VLANs
                ''',
                'config',
                'openconfig-vlan', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_vlan', 'Vlans.Vlan.State', 
                [], [], 
                '''                State variables for VLANs
                ''',
                'state',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'vlan',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_vlan'
        ),
    },
    'Vlans' : {
        'meta_info' : _MetaInfoClass('Vlans',
            False, 
            [
            _MetaInfoClassMember('vlan', REFERENCE_LIST, 'Vlan' , 'ydk.models.openconfig.openconfig_vlan', 'Vlans.Vlan', 
                [], [], 
                '''                Configured VLANs keyed by id
                ''',
                'vlan',
                'openconfig-vlan', False),
            ],
            'openconfig-vlan',
            'vlans',
            _yang_ns._namespaces['openconfig-vlan'],
        'ydk.models.openconfig.openconfig_vlan'
        ),
    },
}
_meta_table['Vlans.Vlan.Config']['meta_info'].parent =_meta_table['Vlans.Vlan']['meta_info']
_meta_table['Vlans.Vlan.State']['meta_info'].parent =_meta_table['Vlans.Vlan']['meta_info']
_meta_table['Vlans.Vlan']['meta_info'].parent =_meta_table['Vlans']['meta_info']
