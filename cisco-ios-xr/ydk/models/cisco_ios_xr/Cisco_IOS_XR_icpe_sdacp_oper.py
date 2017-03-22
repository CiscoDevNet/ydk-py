""" Cisco_IOS_XR_icpe_sdacp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-sdacp package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-icpe\-infra\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DpmProtoHostStateEnum(Enum):
    """
    DpmProtoHostStateEnum

    Dpm proto host state

    .. data:: dpm_proto_host_state_idle = 0

    	Idle

    .. data:: dpm_proto_host_state_discovered = 1

    	Discovered

    .. data:: dpm_proto_host_state_rejecting = 2

    	Rejecting

    """

    dpm_proto_host_state_idle = 0

    dpm_proto_host_state_discovered = 1

    dpm_proto_host_state_rejecting = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_sdacp_oper as meta
        return meta._meta_table['DpmProtoHostStateEnum']


class DpmProtoStateEnum(Enum):
    """
    DpmProtoStateEnum

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

    dpm_proto_state_idle = 0

    dpm_proto_state_probing = 1

    dpm_proto_state_legacy = 2

    dpm_proto_state_configuring = 3

    dpm_proto_state_discovered = 4

    dpm_proto_state_rejecting = 5

    dpm_proto_state_seen = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_sdacp_oper as meta
        return meta._meta_table['DpmProtoStateEnum']


class IcpeCpmChanFsmStateEnum(Enum):
    """
    IcpeCpmChanFsmStateEnum

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

    icpe_cpm_chan_fsm_state_down = 0

    icpe_cpm_chan_fsm_state_not_supported = 1

    icpe_cpm_chan_fsm_state_closed = 2

    icpe_cpm_chan_fsm_state_opening = 3

    icpe_cpm_chan_fsm_state_opened = 4

    icpe_cpm_chan_fsm_state_open = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_sdacp_oper as meta
        return meta._meta_table['IcpeCpmChanFsmStateEnum']


class IcpeCpmChannelResyncStateEnum(Enum):
    """
    IcpeCpmChannelResyncStateEnum

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

    icpe_cpm_channel_resync_state_unknown = 0

    icpe_cpm_channel_resync_state_not_in_resync = 1

    icpe_cpm_channel_resync_state_in_client_resync = 2

    icpe_cpm_channel_resync_state_in_satellite_resync = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_sdacp_oper as meta
        return meta._meta_table['IcpeCpmChannelResyncStateEnum']


class IcpeCpmControlFsmStateEnum(Enum):
    """
    IcpeCpmControlFsmStateEnum

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

    icpe_cpm_control_fsm_state_disconnected = 0

    icpe_cpm_control_fsm_state_connecting = 1

    icpe_cpm_control_fsm_state_authenticating = 2

    icpe_cpm_control_fsm_state_check_ing_ver = 3

    icpe_cpm_control_fsm_state_connected = 4

    icpe_cpm_control_fsm_state_issu = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_icpe_sdacp_oper as meta
        return meta._meta_table['IcpeCpmControlFsmStateEnum']



