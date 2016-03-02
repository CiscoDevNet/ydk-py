""" INET_ADDRESS_MIB 

This MIB module defines textual conventions for
representing Internet addresses.  An Internet
address can be an IPv4 address, an IPv6 address,
or a DNS domain name.  This module also defines
textual conventions for Internet port numbers,
autonomous system numbers, and the length of an
Internet address prefix.

Copyright (C) The Internet Society (2005).  This version
of this MIB module is part of RFC 4001, see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class InetAddressType_Enum(Enum):
    """
    InetAddressType_Enum

    A value that represents a type of Internet address.
    
    unknown(0)  An unknown address type.  This value MUST
                be used if the value of the corresponding
                InetAddress object is a zero\-length string.
                It may also be used to indicate an IP address
                that is not in one of the formats defined
                below.
    
    ipv4(1)     An IPv4 address as defined by the
                InetAddressIPv4 textual convention.
    
    ipv6(2)     An IPv6 address as defined by the
                InetAddressIPv6 textual convention.
    
    ipv4z(3)    A non\-global IPv4 address including a zone
                index as defined by the InetAddressIPv4z
                textual convention.
    
    ipv6z(4)    A non\-global IPv6 address including a zone
                index as defined by the InetAddressIPv6z
                textual convention.
    
    dns(16)     A DNS domain name as defined by the
                InetAddressDNS textual convention.
    
    Each definition of a concrete InetAddressType value must be
    accompanied by a definition of a textual convention for use
    with that InetAddressType.
    
    To support future extensions, the InetAddressType textual
    convention SHOULD NOT be sub\-typed in object type definitions.
    It MAY be sub\-typed in compliance statements in order to
    require only a subset of these address types for a compliant
    implementation.
    
    Implementations must ensure that InetAddressType objects
    and any dependent objects (e.g., InetAddress objects) are
    consistent.  An inconsistentValue error must be generated
    if an attempt to change an InetAddressType object would,
    for example, lead to an undefined InetAddress value.  In
    
    
    particular, InetAddressType/InetAddress pairs must be
    changed together if the address type changes (e.g., from
    ipv6(2) to ipv4(1)).

    """

    UNKNOWN = 0

    IPV4 = 1

    IPV6 = 2

    IPV4Z = 3

    IPV6Z = 4

    DNS = 16


    @staticmethod
    def _meta_info():
        from ydk.models.inet._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetAddressType_Enum']


class InetScopeType_Enum(Enum):
    """
    InetScopeType_Enum

    Represents a scope type.  This textual convention can be used
    in cases where a MIB has to represent different scope types
    and there is no context information, such as an InetAddress
    object, that implicitly defines the scope type.
    
    Note that not all possible values have been assigned yet, but
    they may be assigned in future revisions of this specification.
    Applications should therefore be able to deal with values
    not yet assigned.

    """

    INTERFACELOCAL = 1

    LINKLOCAL = 2

    SUBNETLOCAL = 3

    ADMINLOCAL = 4

    SITELOCAL = 5

    ORGANIZATIONLOCAL = 8

    GLOBAL = 14


    @staticmethod
    def _meta_info():
        from ydk.models.inet._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetScopeType_Enum']


class InetVersion_Enum(Enum):
    """
    InetVersion_Enum

    A value representing a version of the IP protocol.
    
    unknown(0)  An unknown or unspecified version of the IP
                protocol.
    
    
    ipv4(1)     The IPv4 protocol as defined in RFC 791 (STD 5).
    
    ipv6(2)     The IPv6 protocol as defined in RFC 2460.
    
    Note that this textual convention SHOULD NOT be used to
    distinguish different address types associated with IP
    protocols.  The InetAddressType has been designed for this
    purpose.

    """

    UNKNOWN = 0

    IPV4 = 1

    IPV6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.inet._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetVersion_Enum']



