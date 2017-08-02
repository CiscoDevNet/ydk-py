""" CISCO_SUBSCRIBER_IDENTITY_TC_MIB 

This MIB module defines textual conventions describing
subscriber session identities.  A subscriber session identity
consists of data associated with a subscriber session serving as
credentials used to determine authority, status, rights, or
entitlement to privileges.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Subscribermediatype(Enum):
    """
    Subscribermediatype

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

    other = Enum.YLeaf(1, "other")

    async = Enum.YLeaf(2, "async")

    atm = Enum.YLeaf(3, "atm")

    ethernet = Enum.YLeaf(4, "ethernet")

    ip = Enum.YLeaf(5, "ip")

    isdn = Enum.YLeaf(6, "isdn")

    mpls = Enum.YLeaf(7, "mpls")

    sync = Enum.YLeaf(8, "sync")


class Subscriberprotocoltype(Enum):
    """
    Subscriberprotocoltype

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

    other = Enum.YLeaf(1, "other")

    atom = Enum.YLeaf(2, "atom")

    ip = Enum.YLeaf(3, "ip")

    psdn = Enum.YLeaf(4, "psdn")

    ppp = Enum.YLeaf(5, "ppp")

    vpdn = Enum.YLeaf(6, "vpdn")


class Subsessionidentity(Enum):
    """
    Subsessionidentity

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

    other = Enum.YLeaf(1, "other")

    ifIndex = Enum.YLeaf(2, "ifIndex")

    subscriberLabel = Enum.YLeaf(3, "subscriberLabel")

    macAddress = Enum.YLeaf(4, "macAddress")

    nativeVrf = Enum.YLeaf(5, "nativeVrf")

    nativeIpAddress = Enum.YLeaf(6, "nativeIpAddress")

    domainVrf = Enum.YLeaf(7, "domainVrf")

    domainIpAddress = Enum.YLeaf(8, "domainIpAddress")

    pbhk = Enum.YLeaf(9, "pbhk")

    remoteId = Enum.YLeaf(10, "remoteId")

    circuitId = Enum.YLeaf(11, "circuitId")

    nasPort = Enum.YLeaf(12, "nasPort")

    domain = Enum.YLeaf(13, "domain")

    username = Enum.YLeaf(14, "username")

    acctSessionId = Enum.YLeaf(15, "acctSessionId")

    dnis = Enum.YLeaf(16, "dnis")

    media = Enum.YLeaf(17, "media")

    mlpNegotiated = Enum.YLeaf(18, "mlpNegotiated")

    protocol = Enum.YLeaf(19, "protocol")

    serviceName = Enum.YLeaf(20, "serviceName")

    dhcpClass = Enum.YLeaf(21, "dhcpClass")

    tunnelName = Enum.YLeaf(22, "tunnelName")


class Subsessionidentities(Bits):
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
    Keys are:- nasPort , serviceName , pbhk , protocol , macAddress , username , media , mlpNegotiated , domainIpAddress , acctSessionId , subscriberLabel , remoteId , dhcpClass , ifIndex , nativeVrf , nativeIpAddress , domainVrf , tunnelName , circuitId , dnis , domain

    """

    def __init__(self):
        super(Subsessionidentities, self).__init__()


