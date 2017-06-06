""" CISCO_SUBSCRIBER_SESSION_TC_MIB 

This MIB module defines textual conventions describing
subscriber sessions.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SubsessionredundancymodeEnum(Enum):
    """
    SubsessionredundancymodeEnum

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

    none = 1

    other = 2

    active = 3

    standby = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SUBSCRIBER_SESSION_TC_MIB as meta
        return meta._meta_table['SubsessionredundancymodeEnum']


class SubsessionstateEnum(Enum):
    """
    SubsessionstateEnum

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

    other = 1

    pending = 2

    up = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SUBSCRIBER_SESSION_TC_MIB as meta
        return meta._meta_table['SubsessionstateEnum']


class SubsessiontypeEnum(Enum):
    """
    SubsessiontypeEnum

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

    all = 1

    other = 2

    pppSubscriber = 3

    pppoeSubscriber = 4

    l2tpSubscriber = 5

    l2fSubscriber = 6

    ipInterfaceSubscriber = 7

    ipPktSubscriber = 8

    ipDhcpv4Subscriber = 9

    ipRadiusSubscriber = 10

    l2MacSubscriber = 11

    l2Dhcpv4Subscriber = 12

    l2RadiusSubscriber = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SUBSCRIBER_SESSION_TC_MIB as meta
        return meta._meta_table['SubsessiontypeEnum']


class Subsessiontypes(FixedBitsDict):
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
    Keys are:- l2fSubscriber , l2RadiusSubscriber , pppSubscriber , ipPktSubscriber , ipInterfaceSubscriber , ipDhcpv4Subscriber , l2Dhcpv4Subscriber , pppoeSubscriber , l2MacSubscriber , l2tpSubscriber , ipRadiusSubscriber

    """

    def __init__(self):
        self._dictionary = { 
            'l2fSubscriber':False,
            'l2RadiusSubscriber':False,
            'pppSubscriber':False,
            'ipPktSubscriber':False,
            'ipInterfaceSubscriber':False,
            'ipDhcpv4Subscriber':False,
            'l2Dhcpv4Subscriber':False,
            'pppoeSubscriber':False,
            'l2MacSubscriber':False,
            'l2tpSubscriber':False,
            'ipRadiusSubscriber':False,
        }
        self._pos_map = { 
            'l2fSubscriber':3,
            'l2RadiusSubscriber':10,
            'pppSubscriber':0,
            'ipPktSubscriber':5,
            'ipInterfaceSubscriber':4,
            'ipDhcpv4Subscriber':6,
            'l2Dhcpv4Subscriber':9,
            'pppoeSubscriber':1,
            'l2MacSubscriber':8,
            'l2tpSubscriber':2,
            'ipRadiusSubscriber':7,
        }


