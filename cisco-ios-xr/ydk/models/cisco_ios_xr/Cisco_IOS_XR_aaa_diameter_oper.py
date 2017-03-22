""" Cisco_IOS_XR_aaa_diameter_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-diameter package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DisconnectCauseEnum(Enum):
    """
    DisconnectCauseEnum

    Disconnect cause values

    .. data:: reboot = 0

    	Disconnect caused by reboot

    .. data:: busy = 1

    	Disconnect due to server busy

    .. data:: do_not_wait_to_talk = 2

    	Disconnect as server does not want to talk

    """

    reboot = 0

    busy = 1

    do_not_wait_to_talk = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_diameter_oper as meta
        return meta._meta_table['DisconnectCauseEnum']


class PeerEnum(Enum):
    """
    PeerEnum

     Peer type values

    .. data:: undefined = 0

    	Peer not defined

    .. data:: server = 1

    	Server type

    """

    undefined = 0

    server = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_diameter_oper as meta
        return meta._meta_table['PeerEnum']


class PeerStateValueEnum(Enum):
    """
    PeerStateValueEnum

    Peer State Values

    .. data:: state_none = 0

    	No Peer states

    .. data:: closed = 1

    	Peer closed

    .. data:: wait_connection_ack = 2

    	Waiting for ACK

    .. data:: wait_cea = 3

    	Waiting for CEA

    .. data:: state_open = 4

    	Peer open

    .. data:: closing = 5

    	Peer closed

    .. data:: suspect = 6

    	Peer in suspect state

    """

    state_none = 0

    closed = 1

    wait_connection_ack = 2

    wait_cea = 3

    state_open = 4

    closing = 5

    suspect = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_diameter_oper as meta
        return meta._meta_table['PeerStateValueEnum']


class ProtocolTypeValueEnum(Enum):
    """
    ProtocolTypeValueEnum

    Protocol type values

    .. data:: protocol_none = 0

    	No protocol used

    .. data:: tcp = 1

    	TCP protocol

    """

    protocol_none = 0

    tcp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_diameter_oper as meta
        return meta._meta_table['ProtocolTypeValueEnum']


class SecurityTypeValueEnum(Enum):
    """
    SecurityTypeValueEnum

    Security type values

    .. data:: security_type_none = 0

    	No security type

    .. data:: type = 1

    	TLS security

    .. data:: ipsec = 2

    	IPSEC security

    """

    security_type_none = 0

    type = 1

    ipsec = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_diameter_oper as meta
        return meta._meta_table['SecurityTypeValueEnum']


class WhoInitiatedDisconnectEnum(Enum):
    """
    WhoInitiatedDisconnectEnum

    Who initiated to disconnect

    .. data:: none = 0

    	None

    .. data:: host = 1

    	Disconnected by host

    .. data:: peer = 2

    	Disconnected by peer

    """

    none = 0

    host = 1

    peer = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_diameter_oper as meta
        return meta._meta_table['WhoInitiatedDisconnectEnum']



