""" CISCO_SUBSCRIBER_SESSION_TC_MIB 

This MIB module defines textual conventions describing
subscriber sessions.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Subsessionredundancymode(Enum):
    """
    Subsessionredundancymode

    An enumerated integer\-value describing the redundancy mode in

    which a subscriber session is operating\:

        'none'

            The subscriber session is not part of a redundant

            configuration.

        'other'

            The subscriber session is part of a redundant

            configuration and is in a state not recognized by this

            MIB module.

        'active'

            The subscriber session is part of a redundant

            configuration and is forwarding traffic from the

            subscriber.

        'standby'

            The subscriber session is part of a redundant

            configuration and ready to become active in the case of

            a fail\-over event (e.g., linecard failure).

    .. data:: none = 1

    .. data:: other = 2

    .. data:: active = 3

    .. data:: standby = 4

    """

    none = Enum.YLeaf(1, "none")

    other = Enum.YLeaf(2, "other")

    active = Enum.YLeaf(3, "active")

    standby = Enum.YLeaf(4, "standby")


class Subsessionstate(Enum):
    """
    Subsessionstate

    An enumerated integer\-value describing the state of a

    subscriber session\:

        'other'

            The subscriber session is in a state not recognized by

            the implementation of a MIB module using this textual

            convention.

        'pending'

            The subscriber session is in the PENDING state;

            that is, the subscriber session has been initiated and

            the system is in the process of establishing the

            subscriber session.

        'up'

            The subscriber session is in the UP state; that is, the

            system has established the subscriber session.

    .. data:: other = 1

    .. data:: pending = 2

    .. data:: up = 3

    """

    other = Enum.YLeaf(1, "other")

    pending = Enum.YLeaf(2, "pending")

    up = Enum.YLeaf(3, "up")


class Subsessiontype(Enum):
    """
    Subsessiontype

    An enumerated integer\-value describing the type of subscriber

    session.  This value has the intent of refining the interface

    type assigned to a subscriber session.  The interface type

    assigned to a subscriber session groups those types of

    subscriber sessions with similar interface semantics.

    A PPP subscriber session consists of a PPP connection

    (RFC\-1661)

    and has an interface type of 'ppp'.  The following subscriber

    types refine PPP subscriber sessions\:

        'pppSubscriber'

            A PPP connection initiated over a circuit (e.g., an

    ISDN

            line or ATM VC) using the LCP (RFC\-1661).

        'pppoeSubscriber'

            A PPP connection over Ethernet (RFC\-2516), initiated

            by a PADI (PPPoE Active Discovery Initiation) packet.

        'l2tpSubscriber'

            A PPP connection over an L2TP tunnel (RFC\-2661),

            initiated by an Incoming\-Call\-Request control message.

        'l2fSubscriber'

            A PPP connection over an L2F tunnel (RFC\-2341),

            initiated by a L2F\_OPEN message with a non\-zero MID.

    An IP subscriber session consists of the routed traffic

    associated with a subscriber IP address having an interface

    type of 'ipSubscriber'.  Routed traffic describes IP traffic

    that transits at least one router.  If a subscriber's IP

    address

    is not unique to the system, further distinguishing

    characteristics, such as VRF or MAC address, form part of the

    subscriber's identity.  The following subscriber types refine

    IP

    subscriber sessions\:

        'ipInterfaceSubscriber'

            An IP subcriber session provisioned by the system's

            configuration which consists of all traffic received by

            the interface to which the provisioning applies.

        'ipPktSubscriber'

            An IP subscriber session initiated by the receipt of

    the

            first packet received with an unclassified source IP

            address.

        'ipDhcpv4Subscriber'

            An IP subscriber session initiated by the receipt of a

            DHCPv4 DISCOVER packet (RFC\-2131).

        'ipRadiusSubscriber'

            An IP subscriber session initiated by the receipt of a

            RADIUS Access\-Request packet (RFC\-2865).

    An L2 subscriber session consists of the non\-routed traffic

    associated with a subscriber IP address having an interface

    type of 'l2Subscriber'.  Non\-routed traffic describes IP

    traffic

    that doesn't transit a router, meaning that the subscriber must

    be directly connected to the system or have a connection

    through

    an L2 access network (e.g., bridges, switches, and tunnels).

    The

    following subscriber types refine L2 subscriber sessions\:

        'l2MacPacketSubscriber'

            An L2 subscriber session initiated by the receipt of

    the

            first layer 2 packet with an unclassified source MAC

            address.

        'l2Dhcpv4Subscriber'

            An L2 subscriber session initiated by the receipt of a

            DHCPv4 DISCOVER packet (RFC\-2131).

        'l2RadiusSucriber'

            An L2 subscriber session initiated by the receipt of a

            RADIUS Access\-Request packet (RFC\-2865).

    The system should assign the value 'other' to any subscriber

    session not recognized by the implementation of a MIB module

    using this textual convention.

    The value 'all' represents a special value used to indicate all

    subscriber session types.  For example, a scope of aggregation

    that includes all subscriber session types uses this value to

    indicate this fact.

    .. data:: all = 1

    .. data:: other = 2

    .. data:: pppSubscriber = 3

    .. data:: pppoeSubscriber = 4

    .. data:: l2tpSubscriber = 5

    .. data:: l2fSubscriber = 6

    .. data:: ipInterfaceSubscriber = 7

    .. data:: ipPktSubscriber = 8

    .. data:: ipDhcpv4Subscriber = 9

    .. data:: ipRadiusSubscriber = 10

    .. data:: l2MacSubscriber = 11

    .. data:: l2Dhcpv4Subscriber = 12

    .. data:: l2RadiusSubscriber = 13

    """

    all = Enum.YLeaf(1, "all")

    other = Enum.YLeaf(2, "other")

    pppSubscriber = Enum.YLeaf(3, "pppSubscriber")

    pppoeSubscriber = Enum.YLeaf(4, "pppoeSubscriber")

    l2tpSubscriber = Enum.YLeaf(5, "l2tpSubscriber")

    l2fSubscriber = Enum.YLeaf(6, "l2fSubscriber")

    ipInterfaceSubscriber = Enum.YLeaf(7, "ipInterfaceSubscriber")

    ipPktSubscriber = Enum.YLeaf(8, "ipPktSubscriber")

    ipDhcpv4Subscriber = Enum.YLeaf(9, "ipDhcpv4Subscriber")

    ipRadiusSubscriber = Enum.YLeaf(10, "ipRadiusSubscriber")

    l2MacSubscriber = Enum.YLeaf(11, "l2MacSubscriber")

    l2Dhcpv4Subscriber = Enum.YLeaf(12, "l2Dhcpv4Subscriber")

    l2RadiusSubscriber = Enum.YLeaf(13, "l2RadiusSubscriber")


class Subsessiontypes(Bits):
    """
    Subsessiontypes

    A bit string describing a set of subscriber session types\:
    
    'pppSubscriber'
        A PPP connection initiated over a circuit (e.g., an ISDN
        line or ATM VC) using the LCP (RFC\-1661).
    
    'pppoeSubscriber'
        A PPP connection over Ethernet (RFC\-2516), initiated
        by a PADI (PPPoE Active Discovery Initiation) packet.
    
    'l2tpSubscriber'
        A PPP connection over an L2TP tunnel (RFC\-2661),
        initiated by an Incoming\-Call\-Request control message.
    
    'l2fSubscriber'
        A PPP connection over an L2F tunnel (RFC\-2341),
        initiated by a L2F\_OPEN message with a non\-zero MID.
    
    'ipInterfaceSubscriber'
        An IP subcriber session provisioned by the system's
        configuration which consists of all traffic received by
        the interface the provisioning applies.
    
    'ipPktSubscriber'
        An IP subscriber session initiated by the receipt of
        the first packet received with an unclassified source IP
        address.
    
    'ipDhcpv4Subscriber'
        An IP subscriber session initiated by the receipt of a
        DHCPv4 DISCOVER packet (RFC\-2131).
    
    'ipRadiusSubscriber'
        An IP subscriber session initiated by the receipt of a
        RADIUS Access\-Request packet (RFC\-2865).
    
    'l2MacSubscriber'
        An L2 subscriber session initiated by the receipt of the
        first layer 2 packet with an unclassified source MAC
        address.
    
    'l2Dhcpv4Subscriber'
        An L2 subscriber session initiated by the receipt of a
        DHCPv4 DISCOVER packet (RFC\-2131).
    
    'l2RadiusSubscriber'
        An L2 subscriber session initiated by the receipt of a
        RADIUS Access\-Request packet (RFC\-2865).
    
    For more details regarding subscriber session types, see the
    descriptive text associated with the SubSessionType textual
    convention.
    Keys are:- ipInterfaceSubscriber , l2tpSubscriber , l2fSubscriber , pppoeSubscriber , l2RadiusSubscriber , l2MacSubscriber , ipPktSubscriber , pppSubscriber , l2Dhcpv4Subscriber , ipRadiusSubscriber , ipDhcpv4Subscriber

    """

    def __init__(self):
        super(Subsessiontypes, self).__init__()


