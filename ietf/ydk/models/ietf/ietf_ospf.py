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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_routing import RoutingProtocol


class IfStateType(Enum):
    """
    IfStateType (Enum Class)

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

    Down = Enum.YLeaf(1, "Down")

    Loopback = Enum.YLeaf(2, "Loopback")

    Waiting = Enum.YLeaf(3, "Waiting")

    Point_to_Point = Enum.YLeaf(4, "Point-to-Point")

    DR = Enum.YLeaf(5, "DR")

    BDR = Enum.YLeaf(6, "BDR")

    DR_Other = Enum.YLeaf(7, "DR-Other")


class NbrStateType(Enum):
    """
    NbrStateType (Enum Class)

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

    Down = Enum.YLeaf(1, "Down")

    Attempt = Enum.YLeaf(2, "Attempt")

    Init = Enum.YLeaf(3, "Init")

    Y_2_Way = Enum.YLeaf(4, "2-Way")

    ExStart = Enum.YLeaf(5, "ExStart")

    Exchange = Enum.YLeaf(6, "Exchange")

    Loading = Enum.YLeaf(7, "Loading")

    Full = Enum.YLeaf(8, "Full")


class NssaTranslatorStateType(Enum):
    """
    NssaTranslatorStateType (Enum Class)

    OSPF NSSA translator state type.

    .. data:: Enabled = 1

    	NSSA translator enabled state.

    .. data:: Elected = 2

    	NSSA translator elected state.

    .. data:: Disabled = 3

    	NSSA translator disabled state.

    """

    Enabled = Enum.YLeaf(1, "Enabled")

    Elected = Enum.YLeaf(2, "Elected")

    Disabled = Enum.YLeaf(3, "Disabled")


class PacketType(Enum):
    """
    PacketType (Enum Class)

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

    Hello = Enum.YLeaf(1, "Hello")

    Database_Descripton = Enum.YLeaf(2, "Database-Descripton")

    Link_State_Request = Enum.YLeaf(3, "Link-State-Request")

    Link_State_Update = Enum.YLeaf(4, "Link-State-Update")

    Link_State_Ack = Enum.YLeaf(5, "Link-State-Ack")


class RestartExitReasonType(Enum):
    """
    RestartExitReasonType (Enum Class)

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

    None_ = Enum.YLeaf(1, "None")

    InProgress = Enum.YLeaf(2, "InProgress")

    Completed = Enum.YLeaf(3, "Completed")

    TimedOut = Enum.YLeaf(4, "TimedOut")

    TopologyChanged = Enum.YLeaf(5, "TopologyChanged")


class RestartHelperStatusType(Enum):
    """
    RestartHelperStatusType (Enum Class)

    Restart helper status type.

    .. data:: Not_Helping = 1

    	Restart helper status not helping.

    .. data:: Helping = 2

    	Restart helper status helping.

    """

    Not_Helping = Enum.YLeaf(1, "Not-Helping")

    Helping = Enum.YLeaf(2, "Helping")


class RestartStatusType(Enum):
    """
    RestartStatusType (Enum Class)

    OSPF graceful restart status type.

    .. data:: Not_Restarting = 1

    	Router is not restarting.

    .. data:: Planned_Restart = 2

    	Router is going through planned restart.

    .. data:: Unplanned_Restart = 3

    	Router is going through unplanned restart.

    """

    Not_Restarting = Enum.YLeaf(1, "Not-Restarting")

    Planned_Restart = Enum.YLeaf(2, "Planned-Restart")

    Unplanned_Restart = Enum.YLeaf(3, "Unplanned-Restart")



class IfLinkType(Identity):
    """
    Base identity for OSPF interface link type.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:if-link-type"):
        super(IfLinkType, self).__init__(ns, pref, tag)


class AreaType(Identity):
    """
    Base identity for OSPF area type.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:area-type"):
        super(AreaType, self).__init__(ns, pref, tag)


class Ospfv3(RoutingProtocol):
    """
    OSPFv3
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:ospfv3"):
        super(Ospfv3, self).__init__(ns, pref, tag)


class Ospfv2(RoutingProtocol):
    """
    OSPFv2
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:ospfv2"):
        super(Ospfv2, self).__init__(ns, pref, tag)


class OperationMode(Identity):
    """
    OSPF operation mode.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:operation-mode"):
        super(OperationMode, self).__init__(ns, pref, tag)


class Ospf(RoutingProtocol):
    """
    OSPF Protocol
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:ospf"):
        super(Ospf, self).__init__(ns, pref, tag)


class Normal(AreaType):
    """
    OSPF normal area.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:normal"):
        super(Normal, self).__init__(ns, pref, tag)


class Nssa(AreaType):
    """
    OSPF NSSA area.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:nssa"):
        super(Nssa, self).__init__(ns, pref, tag)


class ShipsInTheNight(OperationMode):
    """
    Ships\-in\-the\-night operation mode in which
    each OSPF instance carries only one address family
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:ships-in-the-night"):
        super(ShipsInTheNight, self).__init__(ns, pref, tag)


class Stub(AreaType):
    """
    OSPF stub area.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:stub"):
        super(Stub, self).__init__(ns, pref, tag)


class IfLinkTypeVirtualLink(IfLinkType):
    """
    OSPF interface link type virtual link.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:if-link-type-virtual-link"):
        super(IfLinkTypeVirtualLink, self).__init__(ns, pref, tag)


class IfLinkTypeNormal(IfLinkType):
    """
    OSPF interface link type normal.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:if-link-type-normal"):
        super(IfLinkTypeNormal, self).__init__(ns, pref, tag)


class IfLinkTypeShamLink(IfLinkType):
    """
    OSPF interface link type sham link.
    
    

    """

    _prefix = 'ospf'
    _revision = '2015-03-09'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-ospf", pref="ietf-ospf", tag="ietf-ospf:if-link-type-sham-link"):
        super(IfLinkTypeShamLink, self).__init__(ns, pref, tag)


