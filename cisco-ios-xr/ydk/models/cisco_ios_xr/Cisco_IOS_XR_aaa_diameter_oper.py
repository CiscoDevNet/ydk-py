""" Cisco_IOS_XR_aaa_diameter_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-diameter package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-oper
module with state data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DisconnectCause(Enum):
    """
    DisconnectCause (Enum Class)

    Disconnect cause values

    .. data:: reboot = 0

    	Disconnect caused by reboot

    .. data:: busy = 1

    	Disconnect due to server busy

    .. data:: do_not_wait_to_talk = 2

    	Disconnect as server does not want to talk

    """

    reboot = Enum.YLeaf(0, "reboot")

    busy = Enum.YLeaf(1, "busy")

    do_not_wait_to_talk = Enum.YLeaf(2, "do-not-wait-to-talk")


class Peer(Enum):
    """
    Peer (Enum Class)

     Peer type values

    .. data:: undefined = 0

    	Peer not defined

    .. data:: server = 1

    	Server type

    """

    undefined = Enum.YLeaf(0, "undefined")

    server = Enum.YLeaf(1, "server")


class PeerStateValue(Enum):
    """
    PeerStateValue (Enum Class)

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

    state_none = Enum.YLeaf(0, "state-none")

    closed = Enum.YLeaf(1, "closed")

    wait_connection_ack = Enum.YLeaf(2, "wait-connection-ack")

    wait_cea = Enum.YLeaf(3, "wait-cea")

    state_open = Enum.YLeaf(4, "state-open")

    closing = Enum.YLeaf(5, "closing")

    suspect = Enum.YLeaf(6, "suspect")


class ProtocolTypeValue(Enum):
    """
    ProtocolTypeValue (Enum Class)

    Protocol type values

    .. data:: protocol_none = 0

    	No protocol used

    .. data:: tcp = 1

    	TCP protocol

    """

    protocol_none = Enum.YLeaf(0, "protocol-none")

    tcp = Enum.YLeaf(1, "tcp")


class SecurityTypeValue(Enum):
    """
    SecurityTypeValue (Enum Class)

    Security type values

    .. data:: security_type_none = 0

    	No security type

    .. data:: type = 1

    	TLS security

    .. data:: ipsec = 2

    	IPSEC security

    """

    security_type_none = Enum.YLeaf(0, "security-type-none")

    type = Enum.YLeaf(1, "type")

    ipsec = Enum.YLeaf(2, "ipsec")


class WhoInitiatedDisconnect(Enum):
    """
    WhoInitiatedDisconnect (Enum Class)

    Who initiated to disconnect

    .. data:: none = 0

    	None

    .. data:: host = 1

    	Disconnected by host

    .. data:: peer = 2

    	Disconnected by peer

    """

    none = Enum.YLeaf(0, "none")

    host = Enum.YLeaf(1, "host")

    peer = Enum.YLeaf(2, "peer")



