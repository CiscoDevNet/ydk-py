""" CISCO_SUBSCRIBER_IDENTITY_TC_MIB 

This MIB module defines textual conventions describing
subscriber session identities.  A subscriber session identity
consists of data associated with a subscriber session serving as
credentials used to determine authority, status, rights, or
entitlement to privileges.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SubscribermediatypeEnum(Enum):
    """
    SubscribermediatypeEnum

    An enumerated integer\-value describing the type of media

    providing access to the subscriber\:

        'other'

            The implementation of the MIB module using this textual

            convention does not recognize the type of media

            providing access to the subscriber.

        'async'

            An asynchronous serial line provides access to the

            subscriber.

        'atm'

            An ATM network provides access to the subscriber.

        'ethernet'

            An Ethernet\-based network provides access to the

            subscriber.

        'ip'

            An IP network provides access to the subscriber.

        'isdn'

            An ISDN line provides access to the subscriber.

        'mpls'

            An MPLS network provides access to the subscriber.

        'sync'

            A synchronous serial line provides access to the

            subscriber.

    The value 'other' cannot be written to an instance of an object.

    However, it serves as a convenient value when an instance of an

    object using this textual convention is not valid.

    .. data:: other = 1

    .. data:: async = 2

    .. data:: atm = 3

    .. data:: ethernet = 4

    .. data:: ip = 5

    .. data:: isdn = 6

    .. data:: mpls = 7

    .. data:: sync = 8

    """

    other = 1

    async = 2

    atm = 3

    ethernet = 4

    ip = 5

    isdn = 6

    mpls = 7

    sync = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SUBSCRIBER_IDENTITY_TC_MIB as meta
        return meta._meta_table['SubscribermediatypeEnum']


class SubscriberprotocoltypeEnum(Enum):
    """
    SubscriberprotocoltypeEnum

    An enumerated integer\-value describing the type of protocol

    providing access to the subscriber\:

        'other'

            The implementation of the MIB module using this textual

            convention does not recognize the type of protocol

            providing access to the subscriber.

        'atom'

            Any Transport over MPLS (AToM) provides access to the

            subscriber.

        'ip'

            The Internet Protocol (IP) provides access to the

            subscriber.

        'psdn'

            A Public Switched Data Network (PSDN) provides access to

            the subscriber.

        'ppp'

            The Point\-to\-Point Protocol (PPP) provides access to the

            subscriber.

        'vpdn'

            A Virtual Private Data Network (VPDN) provides access to

            the subscriber.

    The value 'other' cannot be written to an instance of an object.

    However, it serves as a convenient value when an instance of an

    object using this textual convention is not valid.

    .. data:: other = 1

    .. data:: atom = 2

    .. data:: ip = 3

    .. data:: psdn = 4

    .. data:: ppp = 5

    .. data:: vpdn = 6

    """

    other = 1

    atom = 2

    ip = 3

    psdn = 4

    ppp = 5

    vpdn = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SUBSCRIBER_IDENTITY_TC_MIB as meta
        return meta._meta_table['SubscriberprotocoltypeEnum']


class SubsessionidentityEnum(Enum):
    """
    SubsessionidentityEnum

    An enumerated integer\-value describing a subscriber session

    identity\:

        'other'

            The implementation of the MIB module using this textual

            convention does not recognize the subscriber session

            identity.

        'ifIndex'

            The ifIndex assigned to the interface representing the

            subscriber session.

        'subscriberLabel'

            The arbitrary integer\-value assigned by the system

            to uniquely identify the subscriber session within the

            scope of the system.

        'macAddress'

            The subscriber's MAC address.

        'nativeVrf'

            The name of the VRF on which the subscriber session

            originates.

        'nativeIpAddress'

            The IP address assigned to the subscriber session on

    the

            customer\-facing side of the system.

        'domainVrf'

            The name of the VRF to which the system transfers the

            subscriber session traffic.

        'domainIpAddress'

            The IP address assigned to the subscriber session on

    the

            service\-facing side of the system.

        'pbhk'

            The Port\-Bundle Host Key (PBHK) uniquely identifying

    the

            subscriber session.  A PBHK consists of a source IP

            address and a TCP port number.

        'remoteId'

            The name identifying the 'calling station', access

            multiplexor, or access switch providing access to the

            subscriber.

        'circuitId'

            The name identifying the circuit on the 'calling

            station', access multiplexor, or access switch that

            provides access to the subscriber.

        'nasPort'

            An octet string identifying the port on the Network

            Access Server (NAS) that provides access to the

            subscriber.

        'domain'

            The subscriber's domain name.

        'username'

            The subscriber's username.

        'acctSessionId'

            The subscriber's accounting session identifier.

        'dnis'

            The Dialed Number Identification Service (DNIS) number

            (or called\-party number) dialed by the subscriber.

        'media'

            The type of media providing access to the subscriber.

        'mlpNegotiated'

            Indicates whether the subscriber session was

    established

            using multi\-link PPP negotiation.

        'protocol'

            The type of protocol providing access to the

    subscriber.

        'dhcpClass'

            The name of the class matching the DHCP DISCOVER

    message

            received from the subscriber.

        'serviceName'

            The name identifying the service associated with the

            subscriber.

         'tunnelName'

             The name of the VPDN used to carry the subscriber

             session.

    .. data:: other = 1

    .. data:: ifIndex = 2

    .. data:: subscriberLabel = 3

    .. data:: macAddress = 4

    .. data:: nativeVrf = 5

    .. data:: nativeIpAddress = 6

    .. data:: domainVrf = 7

    .. data:: domainIpAddress = 8

    .. data:: pbhk = 9

    .. data:: remoteId = 10

    .. data:: circuitId = 11

    .. data:: nasPort = 12

    .. data:: domain = 13

    .. data:: username = 14

    .. data:: acctSessionId = 15

    .. data:: dnis = 16

    .. data:: media = 17

    .. data:: mlpNegotiated = 18

    .. data:: protocol = 19

    .. data:: serviceName = 20

    .. data:: dhcpClass = 21

    .. data:: tunnelName = 22

    """

    other = 1

    ifIndex = 2

    subscriberLabel = 3

    macAddress = 4

    nativeVrf = 5

    nativeIpAddress = 6

    domainVrf = 7

    domainIpAddress = 8

    pbhk = 9

    remoteId = 10

    circuitId = 11

    nasPort = 12

    domain = 13

    username = 14

    acctSessionId = 15

    dnis = 16

    media = 17

    mlpNegotiated = 18

    protocol = 19

    serviceName = 20

    dhcpClass = 21

    tunnelName = 22


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_SUBSCRIBER_IDENTITY_TC_MIB as meta
        return meta._meta_table['SubsessionidentityEnum']


class Subsessionidentities(FixedBitsDict):
    """
    Subsessionidentities

    A bit string describing a set of subscriber session identities\:
    
    'ifIndex'
        The ifIndex assigned to the interface representing the
        subscriber session.
    
    'subscriberLabel'
        The arbitrary integer\-value assigned by the system
        to uniquely identify the subscriber session within the
        scope of the system.
    
    'macAddress'
        The subscriber's MAC address.
    
    'nativeVrf'
        The name of the VRF on which the subscriber session
        originates.
    
    'nativeIpAddress'
        The IP address assigned to the subscriber session on the
        customer\-facing side of the system.
    
    'domainVrf'
        The name of the VRF to which the system transfers the
        subscriber session traffic.
    
    'domainIpAddress'
        The IP address assigned to the subscriber session on the
        service\-facing side of the system.
    
    'pbhk'
        The Port\-Bundle Host Key (PBHK) uniquely identifying the
        subscriber session.  A PBHK consists of a source IP
        address and a TCP port number.
    
    'remoteId'
        The name identifying the 'calling station' or access
        multiplexor providing access to the subscriber.
    
    'circuitId'
        The name identifying the circuit on the 'calling
        station', access multiplexor, or access switch that
        provides access to the subscriber.
    
    'nasPort'
        An octet string identifying the port on the Network
        Access Server (NAS) that provides access to the
        subscriber.
    
    'domain'
        The subscriber's domain name.
    
    'username'
        The subscriber's username.
    
    'dnis'
        The Dialed Number Identification Service (DNIS) number
        (or called\-party number) dialed by the subscriber.
    
    'acctSessionId'
        The subscriber's accounting session identifier.
    
    'media'
        The type of media providing access to the subscriber.
    
    'mlpNegotiated'
        Indicates whether the subscriber session was established
        using multi\-link PPP negotiation.
    
    'protocol'
        The type of protocol providing access to the subscriber.
    
    'serviceName'
        The name identifying the service associated with the
        subscriber.
    
    'dhcpClass'
        The name of the class matching the DHCP DISCOVER message
        received from the subscriber.
    
    'tunnelName'
        The name of the VPDN used to carry the subscriber
        session.
    Keys are:- protocol , circuitId , remoteId , serviceName , media , nativeIpAddress , acctSessionId , nativeVrf , subscriberLabel , mlpNegotiated , tunnelName , domain , domainIpAddress , macAddress , pbhk , ifIndex , username , domainVrf , nasPort , dhcpClass , dnis

    """

    def __init__(self):
        self._dictionary = { 
            'protocol':False,
            'circuitId':False,
            'remoteId':False,
            'serviceName':False,
            'media':False,
            'nativeIpAddress':False,
            'acctSessionId':False,
            'nativeVrf':False,
            'subscriberLabel':False,
            'mlpNegotiated':False,
            'tunnelName':False,
            'domain':False,
            'domainIpAddress':False,
            'macAddress':False,
            'pbhk':False,
            'ifIndex':False,
            'username':False,
            'domainVrf':False,
            'nasPort':False,
            'dhcpClass':False,
            'dnis':False,
        }
        self._pos_map = { 
            'protocol':17,
            'circuitId':9,
            'remoteId':8,
            'serviceName':18,
            'media':15,
            'nativeIpAddress':4,
            'acctSessionId':13,
            'nativeVrf':3,
            'subscriberLabel':1,
            'mlpNegotiated':16,
            'tunnelName':20,
            'domain':11,
            'domainIpAddress':6,
            'macAddress':2,
            'pbhk':7,
            'ifIndex':0,
            'username':12,
            'domainVrf':5,
            'nasPort':10,
            'dhcpClass':19,
            'dnis':14,
        }


