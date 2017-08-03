""" Cisco_IOS_XR_icpe_sdacp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-sdacp package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-icpe\-infra\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DpmProtoHostState(Enum):
    """
    DpmProtoHostState

    Dpm proto host state

    .. data:: dpm_proto_host_state_idle = 0

    	Idle

    .. data:: dpm_proto_host_state_discovered = 1

    	Discovered

    .. data:: dpm_proto_host_state_rejecting = 2

    	Rejecting

    """

    dpm_proto_host_state_idle = Enum.YLeaf(0, "dpm-proto-host-state-idle")

    dpm_proto_host_state_discovered = Enum.YLeaf(1, "dpm-proto-host-state-discovered")

    dpm_proto_host_state_rejecting = Enum.YLeaf(2, "dpm-proto-host-state-rejecting")


class DpmProtoState(Enum):
    """
    DpmProtoState

    Dpm proto state

    .. data:: dpm_proto_state_idle = 0

    	Idle

    .. data:: dpm_proto_state_probing = 1

    	Probing

    .. data:: dpm_proto_state_legacy = 2

    	Legacy

    .. data:: dpm_proto_state_configuring = 3

    	Configuring

    .. data:: dpm_proto_state_discovered = 4

    	Discovered

    .. data:: dpm_proto_state_rejecting = 5

    	Rejecting

    .. data:: dpm_proto_state_seen = 6

    	Seen

    """

    dpm_proto_state_idle = Enum.YLeaf(0, "dpm-proto-state-idle")

    dpm_proto_state_probing = Enum.YLeaf(1, "dpm-proto-state-probing")

    dpm_proto_state_legacy = Enum.YLeaf(2, "dpm-proto-state-legacy")

    dpm_proto_state_configuring = Enum.YLeaf(3, "dpm-proto-state-configuring")

    dpm_proto_state_discovered = Enum.YLeaf(4, "dpm-proto-state-discovered")

    dpm_proto_state_rejecting = Enum.YLeaf(5, "dpm-proto-state-rejecting")

    dpm_proto_state_seen = Enum.YLeaf(6, "dpm-proto-state-seen")


class IcpeCpmChanFsmState(Enum):
    """
    IcpeCpmChanFsmState

    Icpe cpm chan fsm state

    .. data:: icpe_cpm_chan_fsm_state_down = 0

    	Down

    .. data:: icpe_cpm_chan_fsm_state_not_supported = 1

    	Not supported

    .. data:: icpe_cpm_chan_fsm_state_closed = 2

    	Closed

    .. data:: icpe_cpm_chan_fsm_state_opening = 3

    	Opening

    .. data:: icpe_cpm_chan_fsm_state_opened = 4

    	Opened

    .. data:: icpe_cpm_chan_fsm_state_open = 5

    	Open

    """

    icpe_cpm_chan_fsm_state_down = Enum.YLeaf(0, "icpe-cpm-chan-fsm-state-down")

    icpe_cpm_chan_fsm_state_not_supported = Enum.YLeaf(1, "icpe-cpm-chan-fsm-state-not-supported")

    icpe_cpm_chan_fsm_state_closed = Enum.YLeaf(2, "icpe-cpm-chan-fsm-state-closed")

    icpe_cpm_chan_fsm_state_opening = Enum.YLeaf(3, "icpe-cpm-chan-fsm-state-opening")

    icpe_cpm_chan_fsm_state_opened = Enum.YLeaf(4, "icpe-cpm-chan-fsm-state-opened")

    icpe_cpm_chan_fsm_state_open = Enum.YLeaf(5, "icpe-cpm-chan-fsm-state-open")


class IcpeCpmChannelResyncState(Enum):
    """
    IcpeCpmChannelResyncState

    Icpe cpm channel resync state

    .. data:: icpe_cpm_channel_resync_state_unknown = 0

    	Unknown

    .. data:: icpe_cpm_channel_resync_state_not_in_resync = 1

    	Not in resync

    .. data:: icpe_cpm_channel_resync_state_in_client_resync = 2

    	In client resync

    .. data:: icpe_cpm_channel_resync_state_in_satellite_resync = 3

    	In satellite resync

    """

    icpe_cpm_channel_resync_state_unknown = Enum.YLeaf(0, "icpe-cpm-channel-resync-state-unknown")

    icpe_cpm_channel_resync_state_not_in_resync = Enum.YLeaf(1, "icpe-cpm-channel-resync-state-not-in-resync")

    icpe_cpm_channel_resync_state_in_client_resync = Enum.YLeaf(2, "icpe-cpm-channel-resync-state-in-client-resync")

    icpe_cpm_channel_resync_state_in_satellite_resync = Enum.YLeaf(3, "icpe-cpm-channel-resync-state-in-satellite-resync")


class IcpeCpmControlFsmState(Enum):
    """
    IcpeCpmControlFsmState

    Icpe cpm control fsm state

    .. data:: icpe_cpm_control_fsm_state_disconnected = 0

    	Disconnected

    .. data:: icpe_cpm_control_fsm_state_connecting = 1

    	Connecting

    .. data:: icpe_cpm_control_fsm_state_authenticating = 2

    	Authenticating

    .. data:: icpe_cpm_control_fsm_state_check_ing_ver = 3

    	Checking Version

    .. data:: icpe_cpm_control_fsm_state_connected = 4

    	Connected

    .. data:: icpe_cpm_control_fsm_state_issu = 5

    	ISSU In Progress

    """

    icpe_cpm_control_fsm_state_disconnected = Enum.YLeaf(0, "icpe-cpm-control-fsm-state-disconnected")

    icpe_cpm_control_fsm_state_connecting = Enum.YLeaf(1, "icpe-cpm-control-fsm-state-connecting")

    icpe_cpm_control_fsm_state_authenticating = Enum.YLeaf(2, "icpe-cpm-control-fsm-state-authenticating")

    icpe_cpm_control_fsm_state_check_ing_ver = Enum.YLeaf(3, "icpe-cpm-control-fsm-state-check-ing-ver")

    icpe_cpm_control_fsm_state_connected = Enum.YLeaf(4, "icpe-cpm-control-fsm-state-connected")

    icpe_cpm_control_fsm_state_issu = Enum.YLeaf(5, "icpe-cpm-control-fsm-state-issu")



