


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'LogicalTribRateEnum' : _MetaInfoEnum('LogicalTribRateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'trib-rate1g':'trib_rate1g',
            'trib-rate2-5g':'trib_rate2_5g',
            'trib-rate10g':'trib_rate10g',
            'trib-rate40g':'trib_rate40g',
            'trib-rate100g':'trib_rate100g',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalLoopbackModeEnum' : _MetaInfoEnum('LogicalLoopbackModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'none':'none',
            'facility':'facility',
            'terminal':'terminal',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalChannelOtnTtiAutoEnum' : _MetaInfoEnum('LogicalChannelOtnTtiAutoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalAdminStateEnum' : _MetaInfoEnum('LogicalAdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'enable':'enable',
            'disable':'disable',
            'maintenance':'maintenance',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalChannelAssignmentEnum' : _MetaInfoEnum('LogicalChannelAssignmentEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'type-logical-channel':'type_logical_channel',
            'type-optical-channel':'type_optical_channel',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalTribProtocolEnum' : _MetaInfoEnum('LogicalTribProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'trib-proto-type1ge':'trib_proto_type1ge',
            'trib-proto-type-oc48':'trib_proto_type_oc48',
            'trib-proto-type-stm16':'trib_proto_type_stm16',
            'trib-proto-type10gelan':'trib_proto_type10gelan',
            'trib-proto-type10gewan':'trib_proto_type10gewan',
            'trib-proto-type-oc192':'trib_proto_type_oc192',
            'trib-proto-type-stm64':'trib_proto_type_stm64',
            'trib-proto-type-otu2':'trib_proto_type_otu2',
            'trib-proto-type-otu2e':'trib_proto_type_otu2e',
            'trib-proto-type-otu1e':'trib_proto_type_otu1e',
            'trib-proto-type-odu2':'trib_proto_type_odu2',
            'trib-proto-type-odu2e':'trib_proto_type_odu2e',
            'trib-proto-type40ge':'trib_proto_type40ge',
            'trib-proto-type-oc768':'trib_proto_type_oc768',
            'trib-proto-type-stm256':'trib_proto_type_stm256',
            'trib-proto-type-otu3':'trib_proto_type_otu3',
            'trib-proto-type-odu3':'trib_proto_type_odu3',
            'trib-proto-type100ge':'trib_proto_type100ge',
            'trib-proto-type100g-mlg':'trib_proto_type100g_mlg',
            'trib-proto-type-otu4':'trib_proto_type_otu4',
            'trib-proto-type-otu-cn':'trib_proto_type_otu_cn',
            'trib-proto-type-odu4':'trib_proto_type_odu4',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalProtocolEnum' : _MetaInfoEnum('LogicalProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg',
        {
            'type-ethernet':'type_ethernet',
            'type-otn':'type_otn',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-cfg', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg']),
    'LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment' : {
        'meta_info' : _MetaInfoClass('LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment',
            False, 
            [
            _MetaInfoClassMember('assignment-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Logical channel assignment index
                ''',
                'assignment_index',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', True),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Configure Allocation for this assignment(10,
                40 or 100G)
                ''',
                'allocation',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('assignment-type', REFERENCE_ENUM_CLASS, 'LogicalChannelAssignmentEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalChannelAssignmentEnum', 
                [], [], 
                '''                Type of assignment for logical channel
                ''',
                'assignment_type',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Configure description for this assignment
                ''',
                'description',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('logical-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Configure logical channel for this assignment
                ''',
                'logical_channel_id',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('optical-channel-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure optical channel for this assignment
                ''',
                'optical_channel_id',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'logical-channel-assignment',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
    'LogicalChannels.Channel.LogicalChannelAssignments' : {
        'meta_info' : _MetaInfoClass('LogicalChannels.Channel.LogicalChannelAssignments',
            False, 
            [
            _MetaInfoClassMember('logical-channel-assignment', REFERENCE_LIST, 'LogicalChannelAssignment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment', 
                [], [], 
                '''                Logical Channel Assignment id
                ''',
                'logical_channel_assignment',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'logical-channel-assignments',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
    'LogicalChannels.Channel.Otn' : {
        'meta_info' : _MetaInfoClass('LogicalChannels.Channel.Otn',
            False, 
            [
            _MetaInfoClassMember('tti-msg-auto', REFERENCE_ENUM_CLASS, 'LogicalChannelOtnTtiAutoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalChannelOtnTtiAutoEnum', 
                [], [], 
                '''                Trail trace identifier (TTI) transmit message
                automatically created. If True, then setting a
                custom transmit message would be invalid.
                Trail trace identifier (TTI) transmit message
                automatically created.
                ''',
                'tti_msg_auto',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('tti-msg-expected', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Trail trace identifier (TTI) message
                expectedTrail trace identifier (TTI) message
                expected
                ''',
                'tti_msg_expected',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('tti-msg-transmit', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Trail trace identifier (TTI) message
                transmittedTrail trace identifier (TTI)
                message transmitted
                ''',
                'tti_msg_transmit',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
    'LogicalChannels.Channel' : {
        'meta_info' : _MetaInfoClass('LogicalChannels.Channel',
            False, 
            [
            _MetaInfoClassMember('channel-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Logical Channel Index
                ''',
                'channel_index',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', True),
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'LogicalAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalAdminStateEnum', 
                [], [], 
                '''                Configure the admin-state 
                ''',
                'admin_state',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Description (Max 255 characters)
                ''',
                'description',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('ingress-client-port', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure ingress client port for this logical
                channel
                ''',
                'ingress_client_port',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('ingress-physical-channel', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Configure ingress physical channel for this
                logical channel
                ''',
                'ingress_physical_channel',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('logical-channel-assignments', REFERENCE_CLASS, 'LogicalChannelAssignments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalChannels.Channel.LogicalChannelAssignments', 
                [], [], 
                '''                Logical channel assignment for logical channel
                ''',
                'logical_channel_assignments',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('logical-channel-type', REFERENCE_ENUM_CLASS, 'LogicalProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalProtocolEnum', 
                [], [], 
                '''                Configure the logical-channel-type 
                ''',
                'logical_channel_type',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('loopback-mode', REFERENCE_ENUM_CLASS, 'LogicalLoopbackModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalLoopbackModeEnum', 
                [], [], 
                '''                Configure the loopback mode 
                ''',
                'loopback_mode',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalChannels.Channel.Otn', 
                [], [], 
                '''                Otn Related configs for Logical channel
                ''',
                'otn',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('rate-class', REFERENCE_ENUM_CLASS, 'LogicalTribRateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalTribRateEnum', 
                [], [], 
                '''                Rounded bit rate of the tributary signal
                ''',
                'rate_class',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_ENUM_CLASS, 'LogicalTribProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalTribProtocolEnum', 
                [], [], 
                '''                Protocol framing of the tributary signal
                ''',
                'trib_protocol',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'channel',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
    'LogicalChannels' : {
        'meta_info' : _MetaInfoClass('LogicalChannels',
            False, 
            [
            _MetaInfoClassMember('channel', REFERENCE_LIST, 'Channel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'LogicalChannels.Channel', 
                [], [], 
                '''                Logical channel index
                ''',
                'channel',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'logical-channels',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
    'OpticalChannels.OpticalChannel' : {
        'meta_info' : _MetaInfoClass('OpticalChannels.OpticalChannel',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Optical Channel Name
                ''',
                'ifname',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', True),
            _MetaInfoClassMember('line-port', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify R/S/I/P
                ''',
                'line_port',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            _MetaInfoClassMember('operational-mode', ATTRIBUTE, 'int' , None, None, 
                [('1', '100000')], [], 
                '''                Configure operational mode
                ''',
                'operational_mode',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'optical-channel',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
    'OpticalChannels' : {
        'meta_info' : _MetaInfoClass('OpticalChannels',
            False, 
            [
            _MetaInfoClassMember('optical-channel', REFERENCE_LIST, 'OpticalChannel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg', 'OpticalChannels.OpticalChannel', 
                [], [], 
                '''                Optical Channel index
                ''',
                'optical_channel',
                'Cisco-IOS-XR-openconfig-terminal-device-cfg', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-cfg',
            'optical-channels',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_cfg'
        ),
    },
}
_meta_table['LogicalChannels.Channel.LogicalChannelAssignments.LogicalChannelAssignment']['meta_info'].parent =_meta_table['LogicalChannels.Channel.LogicalChannelAssignments']['meta_info']
_meta_table['LogicalChannels.Channel.LogicalChannelAssignments']['meta_info'].parent =_meta_table['LogicalChannels.Channel']['meta_info']
_meta_table['LogicalChannels.Channel.Otn']['meta_info'].parent =_meta_table['LogicalChannels.Channel']['meta_info']
_meta_table['LogicalChannels.Channel']['meta_info'].parent =_meta_table['LogicalChannels']['meta_info']
_meta_table['OpticalChannels.OpticalChannel']['meta_info'].parent =_meta_table['OpticalChannels']['meta_info']
