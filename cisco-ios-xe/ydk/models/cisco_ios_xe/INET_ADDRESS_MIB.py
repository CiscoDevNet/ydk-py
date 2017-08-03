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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Inetaddresstype(Enum):
    """
    Inetaddresstype

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

    unknown = Enum.YLeaf(0, "unknown")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    ipv4z = Enum.YLeaf(3, "ipv4z")

    ipv6z = Enum.YLeaf(4, "ipv6z")

    dns = Enum.YLeaf(16, "dns")


class Inetscopetype(Enum):
    """
    Inetscopetype

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

    interfaceLocal = Enum.YLeaf(1, "interfaceLocal")

    linkLocal = Enum.YLeaf(2, "linkLocal")

    subnetLocal = Enum.YLeaf(3, "subnetLocal")

    adminLocal = Enum.YLeaf(4, "adminLocal")

    siteLocal = Enum.YLeaf(5, "siteLocal")

    organizationLocal = Enum.YLeaf(8, "organizationLocal")

    global_ = Enum.YLeaf(14, "global")


class Inetversion(Enum):
    """
    Inetversion

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

    unknown = Enum.YLeaf(0, "unknown")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")



