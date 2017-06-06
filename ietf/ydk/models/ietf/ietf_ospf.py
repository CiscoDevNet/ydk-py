""" ietf_ospf 

This YANG module defines the generic configuration
data for OSPF, which is common across all of the vendor
implementations of the protocol. It is intended that the module
will be extended by vendors to define vendor\-specific
OSPF configuration parameters and policies,
for example route maps or route policies.

Terms and Acronyms

OSPF (ospf)\: Open Shortest Path First

IP (ip)\: Internet Protocol

IPv4 (ipv4)\:Internet Protocol Version 4

IPv6 (ipv6)\: Internet Protocol Version 6

MTU (mtu) Maximum Transmission Unit


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_routing import RoutingProtocolIdentity

class IfStateTypeEnum(Enum):
    """
    IfStateTypeEnum

    OSPF interface state type.

    .. data:: Down = 1

    	Interface down state

    .. data:: Loopback = 2

    	Interface loopback state

    .. data:: Waiting = 3

    	Interface waiting state

    .. data:: Point_to_Point = 4

    	Interface point-to-point state

    .. data:: DR = 5

    	Interface Designated Router (DR) state

    .. data:: BDR = 6

    	Interface Backup Designated Router (BDR) state

    .. data:: DR_Other = 7

    	Interface Other Designated Router state

    """

    Down = 1

    Loopback = 2

    Waiting = 3

    Point_to_Point = 4

    DR = 5

    BDR = 6

    DR_Other = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['IfStateTypeEnum']


class NbrStateTypeEnum(Enum):
    """
    NbrStateTypeEnum

    OSPF neighbor state type.

    .. data:: Down = 1

    	Neighbor down state

    .. data:: Attempt = 2

    	Neighbor attempt state

    .. data:: Init = 3

    	Neighbor init state

    .. data:: Y_2_Way = 4

    	Neighbor 2-Way state

    .. data:: ExStart = 5

    	Neighbor exchange start state

    .. data:: Exchange = 6

    	Neighbor exchange state

    .. data:: Loading = 7

    	Neighbor loading state

    .. data:: Full = 8

    	Neighbor full state

    """

    Down = 1

    Attempt = 2

    Init = 3

    Y_2_Way = 4

    ExStart = 5

    Exchange = 6

    Loading = 7

    Full = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['NbrStateTypeEnum']


class NssaTranslatorStateTypeEnum(Enum):
    """
    NssaTranslatorStateTypeEnum

    OSPF NSSA translator state type.

    .. data:: Enabled = 1

    	NSSA translator enabled state.

    .. data:: Elected = 2

    	NSSA translator elected state.

    .. data:: Disabled = 3

    	NSSA translator disabled state.

    """

    Enabled = 1

    Elected = 2

    Disabled = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['NssaTranslatorStateTypeEnum']


class PacketTypeEnum(Enum):
    """
    PacketTypeEnum

    OSPF packet type.

    .. data:: Hello = 1

    	OSPF hello packet.

    .. data:: Database_Descripton = 2

    	OSPF database description packet.

    .. data:: Link_State_Request = 3

    	OSPF link state request packet.

    .. data:: Link_State_Update = 4

    	OSPF link state update packet.

    .. data:: Link_State_Ack = 5

    	OSPF link state acknowlegement packet.

    """

    Hello = 1

    Database_Descripton = 2

    Link_State_Request = 3

    Link_State_Update = 4

    Link_State_Ack = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['PacketTypeEnum']


class RestartExitReasonTypeEnum(Enum):
    """
    RestartExitReasonTypeEnum

    Describes the outcome of the last attempt at a

    graceful restart, either by itself or acting

    as a helper.

    .. data:: None_ = 1

    	Not attempted.

    .. data:: InProgress = 2

    	Restart in progress.

    .. data:: Completed = 3

    	Successfully completed.

    .. data:: TimedOut = 4

    	Timed out.

    .. data:: TopologyChanged = 5

    	Aborted due to topology change.

    """

    None_ = 1

    InProgress = 2

    Completed = 3

    TimedOut = 4

    TopologyChanged = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['RestartExitReasonTypeEnum']


class RestartHelperStatusTypeEnum(Enum):
    """
    RestartHelperStatusTypeEnum

    Restart helper status type.

    .. data:: Not_Helping = 1

    	Restart helper status not helping.

    .. data:: Helping = 2

    	Restart helper status helping.

    """

    Not_Helping = 1

    Helping = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['RestartHelperStatusTypeEnum']


class RestartStatusTypeEnum(Enum):
    """
    RestartStatusTypeEnum

    OSPF graceful restart status type.

    .. data:: Not_Restarting = 1

    	Router is not restarting.

    .. data:: Planned_Restart = 2

    	Router is going through planned restart.

    .. data:: Unplanned_Restart = 3

    	Router is going through unplanned restart.

    """

    Not_Restarting = 1

    Planned_Restart = 2

    Unplanned_Restart = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['RestartStatusTypeEnum']



class Ospfv3Identity(RoutingProtocolIdentity):
    """
    OSPFv3
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['Ospfv3Identity']['meta_info']


class OperationModeIdentity(object):
    """
    OSPF operation mode.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['OperationModeIdentity']['meta_info']


class Ospfv2Identity(RoutingProtocolIdentity):
    """
    OSPFv2
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['Ospfv2Identity']['meta_info']


class IfLinkTypeIdentity(object):
    """
    Base identity for OSPF interface link type.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['IfLinkTypeIdentity']['meta_info']


class OspfIdentity(RoutingProtocolIdentity):
    """
    OSPF Protocol
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['OspfIdentity']['meta_info']


class AreaTypeIdentity(object):
    """
    Base identity for OSPF area type.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['AreaTypeIdentity']['meta_info']


class IfLinkTypeShamLinkIdentity(IfLinkTypeIdentity):
    """
    OSPF interface link type sham link.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        IfLinkTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['IfLinkTypeShamLinkIdentity']['meta_info']


class ShipsInTheNightIdentity(OperationModeIdentity):
    """
    Ships\-in\-the\-night operation mode in which
    each OSPF instance carries only one address family
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        OperationModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['ShipsInTheNightIdentity']['meta_info']


class NormalIdentity(AreaTypeIdentity):
    """
    OSPF normal area.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        AreaTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['NormalIdentity']['meta_info']


class StubIdentity(AreaTypeIdentity):
    """
    OSPF stub area.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        AreaTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['StubIdentity']['meta_info']


class NssaIdentity(AreaTypeIdentity):
    """
    OSPF NSSA area.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        AreaTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['NssaIdentity']['meta_info']


class IfLinkTypeNormalIdentity(IfLinkTypeIdentity):
    """
    OSPF interface link type normal.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        IfLinkTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['IfLinkTypeNormalIdentity']['meta_info']


class IfLinkTypeVirtualLinkIdentity(IfLinkTypeIdentity):
    """
    OSPF interface link type virtual link.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self):
        IfLinkTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ospf as meta
        return meta._meta_table['IfLinkTypeVirtualLinkIdentity']['meta_info']


