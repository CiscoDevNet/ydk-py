


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DpmProtoStateEnum' : _MetaInfoEnum('DpmProtoStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper',
        {
            'dpm-proto-state-idle':'dpm_proto_state_idle',
            'dpm-proto-state-probing':'dpm_proto_state_probing',
            'dpm-proto-state-legacy':'dpm_proto_state_legacy',
            'dpm-proto-state-configuring':'dpm_proto_state_configuring',
            'dpm-proto-state-discovered':'dpm_proto_state_discovered',
            'dpm-proto-state-rejecting':'dpm_proto_state_rejecting',
            'dpm-proto-state-seen':'dpm_proto_state_seen',
        }, 'Cisco-IOS-XR-icpe-sdacp-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper']),
    'IcpeCpmControlFsmStateEnum' : _MetaInfoEnum('IcpeCpmControlFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper',
        {
            'icpe-cpm-control-fsm-state-disconnected':'icpe_cpm_control_fsm_state_disconnected',
            'icpe-cpm-control-fsm-state-connecting':'icpe_cpm_control_fsm_state_connecting',
            'icpe-cpm-control-fsm-state-authenticating':'icpe_cpm_control_fsm_state_authenticating',
            'icpe-cpm-control-fsm-state-check-ing-ver':'icpe_cpm_control_fsm_state_check_ing_ver',
            'icpe-cpm-control-fsm-state-connected':'icpe_cpm_control_fsm_state_connected',
            'icpe-cpm-control-fsm-state-issu':'icpe_cpm_control_fsm_state_issu',
        }, 'Cisco-IOS-XR-icpe-sdacp-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper']),
    'DpmProtoHostStateEnum' : _MetaInfoEnum('DpmProtoHostStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper',
        {
            'dpm-proto-host-state-idle':'dpm_proto_host_state_idle',
            'dpm-proto-host-state-discovered':'dpm_proto_host_state_discovered',
            'dpm-proto-host-state-rejecting':'dpm_proto_host_state_rejecting',
        }, 'Cisco-IOS-XR-icpe-sdacp-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper']),
    'IcpeCpmChannelResyncStateEnum' : _MetaInfoEnum('IcpeCpmChannelResyncStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper',
        {
            'icpe-cpm-channel-resync-state-unknown':'icpe_cpm_channel_resync_state_unknown',
            'icpe-cpm-channel-resync-state-not-in-resync':'icpe_cpm_channel_resync_state_not_in_resync',
            'icpe-cpm-channel-resync-state-in-client-resync':'icpe_cpm_channel_resync_state_in_client_resync',
            'icpe-cpm-channel-resync-state-in-satellite-resync':'icpe_cpm_channel_resync_state_in_satellite_resync',
        }, 'Cisco-IOS-XR-icpe-sdacp-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper']),
    'IcpeCpmChanFsmStateEnum' : _MetaInfoEnum('IcpeCpmChanFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_sdacp_oper',
        {
            'icpe-cpm-chan-fsm-state-down':'icpe_cpm_chan_fsm_state_down',
            'icpe-cpm-chan-fsm-state-not-supported':'icpe_cpm_chan_fsm_state_not_supported',
            'icpe-cpm-chan-fsm-state-closed':'icpe_cpm_chan_fsm_state_closed',
            'icpe-cpm-chan-fsm-state-opening':'icpe_cpm_chan_fsm_state_opening',
            'icpe-cpm-chan-fsm-state-opened':'icpe_cpm_chan_fsm_state_opened',
            'icpe-cpm-chan-fsm-state-open':'icpe_cpm_chan_fsm_state_open',
        }, 'Cisco-IOS-XR-icpe-sdacp-oper', _yang_ns._namespaces['Cisco-IOS-XR-icpe-sdacp-oper']),
}
