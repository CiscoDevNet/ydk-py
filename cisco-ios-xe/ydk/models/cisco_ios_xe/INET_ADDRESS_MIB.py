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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class InetaddresstypeEnum(Enum):
    """
    InetaddresstypeEnum

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

    .. data:: unknown = 0

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    .. data:: ipv4z = 3

    .. data:: ipv6z = 4

    .. data:: dns = 16

    """

    unknown = 0

    ipv4 = 1

    ipv6 = 2

    ipv4z = 3

    ipv6z = 4

    dns = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetaddresstypeEnum']


class InetscopetypeEnum(Enum):
    """
    InetscopetypeEnum

    Represents a scope type.  This textual convention can be used

    in cases where a MIB has to represent different scope types

    and there is no context information, such as an InetAddress

    object, that implicitly defines the scope type.

    Note that not all possible values have been assigned yet, but

    they may be assigned in future revisions of this specification.

    Applications should therefore be able to deal with values

    not yet assigned.

    .. data:: interfaceLocal = 1

    .. data:: linkLocal = 2

    .. data:: subnetLocal = 3

    .. data:: adminLocal = 4

    .. data:: siteLocal = 5

    .. data:: organizationLocal = 8

    .. data:: global_ = 14

    """

    interfaceLocal = 1

    linkLocal = 2

    subnetLocal = 3

    adminLocal = 4

    siteLocal = 5

    organizationLocal = 8

    global_ = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetscopetypeEnum']


class InetversionEnum(Enum):
    """
    InetversionEnum

    A value representing a version of the IP protocol.

    unknown(0)  An unknown or unspecified version of the IP

                protocol.

    ipv4(1)     The IPv4 protocol as defined in RFC 791 (STD 5).

    ipv6(2)     The IPv6 protocol as defined in RFC 2460.

    Note that this textual convention SHOULD NOT be used to

    distinguish different address types associated with IP

    protocols.  The InetAddressType has been designed for this

    purpose.

    .. data:: unknown = 0

    .. data:: ipv4 = 1

    .. data:: ipv6 = 2

    """

    unknown = 0

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _INET_ADDRESS_MIB as meta
        return meta._meta_table['InetversionEnum']



