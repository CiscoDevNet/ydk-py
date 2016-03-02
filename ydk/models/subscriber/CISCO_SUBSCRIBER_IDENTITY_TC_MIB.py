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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SubSessionIdentity_Enum(Enum):
    """
    SubSessionIdentity_Enum

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

    """

    OTHER = 1

    IFINDEX = 2

    SUBSCRIBERLABEL = 3

    MACADDRESS = 4

    NATIVEVRF = 5

    NATIVEIPADDRESS = 6

    DOMAINVRF = 7

    DOMAINIPADDRESS = 8

    PBHK = 9

    REMOTEID = 10

    CIRCUITID = 11

    NASPORT = 12

    DOMAIN = 13

    USERNAME = 14

    ACCTSESSIONID = 15

    DNIS = 16

    MEDIA = 17

    MLPNEGOTIATED = 18

    PROTOCOL = 19

    SERVICENAME = 20

    DHCPCLASS = 21

    TUNNELNAME = 22


    @staticmethod
    def _meta_info():
        from ydk.models.subscriber._meta import _CISCO_SUBSCRIBER_IDENTITY_TC_MIB as meta
        return meta._meta_table['SubSessionIdentity_Enum']


class SubscriberMediaType_Enum(Enum):
    """
    SubscriberMediaType_Enum

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

    """

    OTHER = 1

    ASYNC = 2

    ATM = 3

    ETHERNET = 4

    IP = 5

    ISDN = 6

    MPLS = 7

    SYNC = 8


    @staticmethod
    def _meta_info():
        from ydk.models.subscriber._meta import _CISCO_SUBSCRIBER_IDENTITY_TC_MIB as meta
        return meta._meta_table['SubscriberMediaType_Enum']


class SubscriberProtocolType_Enum(Enum):
    """
    SubscriberProtocolType_Enum

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

    """

    OTHER = 1

    ATOM = 2

    IP = 3

    PSDN = 4

    PPP = 5

    VPDN = 6


    @staticmethod
    def _meta_info():
        from ydk.models.subscriber._meta import _CISCO_SUBSCRIBER_IDENTITY_TC_MIB as meta
        return meta._meta_table['SubscriberProtocolType_Enum']


class SubSessionIdentities_Bits(FixedBitsDict):
    """
    SubSessionIdentities_Bits

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
    Keys are:- nativeVrf , macAddress , domain , subscriberLabel , protocol , domainIpAddress , remoteId , mlpNegotiated , media , tunnelName , username , nativeIpAddress , circuitId , pbhk , ifIndex , acctSessionId , dnis , domainVrf , nasPort , dhcpClass , serviceName

    """

    def __init__(self):
        self._dictionary = { 
            'nativeVrf':False,
            'macAddress':False,
            'domain':False,
            'subscriberLabel':False,
            'protocol':False,
            'domainIpAddress':False,
            'remoteId':False,
            'mlpNegotiated':False,
            'media':False,
            'tunnelName':False,
            'username':False,
            'nativeIpAddress':False,
            'circuitId':False,
            'pbhk':False,
            'ifIndex':False,
            'acctSessionId':False,
            'dnis':False,
            'domainVrf':False,
            'nasPort':False,
            'dhcpClass':False,
            'serviceName':False,
        }
        self._pos_map = { 
            'nativeVrf':3,
            'macAddress':2,
            'domain':11,
            'subscriberLabel':1,
            'protocol':17,
            'domainIpAddress':6,
            'remoteId':8,
            'mlpNegotiated':16,
            'media':15,
            'tunnelName':20,
            'username':12,
            'nativeIpAddress':4,
            'circuitId':9,
            'pbhk':7,
            'ifIndex':0,
            'acctSessionId':13,
            'dnis':14,
            'domainVrf':5,
            'nasPort':10,
            'dhcpClass':19,
            'serviceName':18,
        }


