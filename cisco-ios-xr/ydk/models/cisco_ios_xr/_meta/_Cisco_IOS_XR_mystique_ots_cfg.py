


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OtsPsmManualSwitchEnum' : _MetaInfoEnum('OtsPsmManualSwitchEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg',
        {
            'working':'working',
            'protected':'protected',
        }, 'Cisco-IOS-XR-mystique-ots-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg']),
    'OtsAmplifierNodeEnum' : _MetaInfoEnum('OtsAmplifierNodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg',
        {
            'term':'term',
            'ila':'ila',
            'roadm':'roadm',
        }, 'Cisco-IOS-XR-mystique-ots-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg']),
    'OtsPsmLockoutFromEnum' : _MetaInfoEnum('OtsPsmLockoutFromEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg',
        {
            'working':'working',
            'protected':'protected',
        }, 'Cisco-IOS-XR-mystique-ots-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg']),
    'OtsAmplifierGridModeEnum' : _MetaInfoEnum('OtsAmplifierGridModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg',
        {
            '100g-hz':'Y_100g_hz',
            '50g-hz':'Y_50g_hz',
            'gr-idle-ss':'gr_idle_ss',
        }, 'Cisco-IOS-XR-mystique-ots-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg']),
    'HardwareModule.Node.Slot.Amplifier' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Slot.Amplifier',
            False, 
            [
            _MetaInfoClassMember('grid-mode', REFERENCE_ENUM_CLASS, 'OtsAmplifierGridModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'OtsAmplifierGridModeEnum', 
                [], [], 
                '''                Define the working mode for the optical
                module
                ''',
                'grid_mode',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            _MetaInfoClassMember('node-type', REFERENCE_ENUM_CLASS, 'OtsAmplifierNodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'OtsAmplifierNodeEnum', 
                [], [], 
                '''                Define the type of node in which the
                amplifier is set to work
                ''',
                'node_type',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            _MetaInfoClassMember('udc-vlan', ATTRIBUTE, 'int' , None, None, 
                [('2', '4080')], [], 
                '''                Define the VLAN ID in range <2-4080>
                ''',
                'udc_vlan',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            ],
            'Cisco-IOS-XR-mystique-ots-cfg',
            'amplifier',
            _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg'
        ),
    },
    'HardwareModule.Node.Slot.Psm' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Slot.Psm',
            False, 
            [
            _MetaInfoClassMember('lockout-from', REFERENCE_ENUM_CLASS, 'OtsPsmLockoutFromEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'OtsPsmLockoutFromEnum', 
                [], [], 
                '''                Exclude selected port from protection
                ''',
                'lockout_from',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            _MetaInfoClassMember('manual-switch-to', REFERENCE_ENUM_CLASS, 'OtsPsmManualSwitchEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'OtsPsmManualSwitchEnum', 
                [], [], 
                '''                Switch active path on selected port
                ''',
                'manual_switch_to',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            ],
            'Cisco-IOS-XR-mystique-ots-cfg',
            'psm',
            _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg'
        ),
    },
    'HardwareModule.Node.Slot' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Slot',
            False, 
            [
            _MetaInfoClassMember('slot-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set Slot
                ''',
                'slot_id',
                'Cisco-IOS-XR-mystique-ots-cfg', True),
            _MetaInfoClassMember('amplifier', REFERENCE_CLASS, 'Amplifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'HardwareModule.Node.Slot.Amplifier', 
                [], [], 
                '''                Amplifier Configs
                ''',
                'amplifier',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            _MetaInfoClassMember('psm', REFERENCE_CLASS, 'Psm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'HardwareModule.Node.Slot.Psm', 
                [], [], 
                '''                PSM Configs
                ''',
                'psm',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            ],
            'Cisco-IOS-XR-mystique-ots-cfg',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg'
        ),
    },
    'HardwareModule.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Fully qualified line card specification
                ''',
                'location',
                'Cisco-IOS-XR-mystique-ots-cfg', True),
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'HardwareModule.Node.Slot', 
                [], [], 
                '''                Slot Id
                ''',
                'slot',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            ],
            'Cisco-IOS-XR-mystique-ots-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg'
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg', 'HardwareModule.Node', 
                [], [], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-mystique-ots-cfg', False),
            ],
            'Cisco-IOS-XR-mystique-ots-cfg',
            'hardware-module',
            _yang_ns._namespaces['Cisco-IOS-XR-mystique-ots-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mystique_ots_cfg'
        ),
    },
}
_meta_table['HardwareModule.Node.Slot.Amplifier']['meta_info'].parent =_meta_table['HardwareModule.Node.Slot']['meta_info']
_meta_table['HardwareModule.Node.Slot.Psm']['meta_info'].parent =_meta_table['HardwareModule.Node.Slot']['meta_info']
_meta_table['HardwareModule.Node.Slot']['meta_info'].parent =_meta_table['HardwareModule.Node']['meta_info']
_meta_table['HardwareModule.Node']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
