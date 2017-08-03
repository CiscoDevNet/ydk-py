""" IANA_RTPROTO_MIB 

This MIB module defines the IANAipRouteProtocol and
IANAipMRouteProtocol textual conventions for use in MIBs
which need to identify unicast or multicast routing
mechanisms.

Any additions or changes to the contents of this MIB module
require either publication of an RFC, or Designated Expert
Review as defined in RFC 2434, Guidelines for Writing an
IANA Considerations Section in RFCs.  The Designated Expert 
will be selected by the IESG Area Director(s) of the Routing
Area.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ianaipmrouteprotocol(Enum):
    """
    Ianaipmrouteprotocol

    The multicast routing protocol.  Inclusion of values for

    multicast routing protocols is not intended to imply that

    those protocols need be supported.

    .. data:: other = 1

    .. data:: local = 2

    .. data:: netmgmt = 3

    .. data:: dvmrp = 4

    .. data:: mospf = 5

    .. data:: pimSparseDense = 6

    .. data:: cbt = 7

    .. data:: pimSparseMode = 8

    .. data:: pimDenseMode = 9

    .. data:: igmpOnly = 10

    .. data:: bgmp = 11

    .. data:: msdp = 12

    """

    other = Enum.YLeaf(1, "other")

    local = Enum.YLeaf(2, "local")

    netmgmt = Enum.YLeaf(3, "netmgmt")

    dvmrp = Enum.YLeaf(4, "dvmrp")

    mospf = Enum.YLeaf(5, "mospf")

    pimSparseDense = Enum.YLeaf(6, "pimSparseDense")

    cbt = Enum.YLeaf(7, "cbt")

    pimSparseMode = Enum.YLeaf(8, "pimSparseMode")

    pimDenseMode = Enum.YLeaf(9, "pimDenseMode")

    igmpOnly = Enum.YLeaf(10, "igmpOnly")

    bgmp = Enum.YLeaf(11, "bgmp")

    msdp = Enum.YLeaf(12, "msdp")


class Ianaiprouteprotocol(Enum):
    """
    Ianaiprouteprotocol

    A mechanism for learning routes.  Inclusion of values for

    routing protocols is not intended to imply that those

    protocols need be supported.

    .. data:: other = 1

    .. data:: local = 2

    .. data:: netmgmt = 3

    .. data:: icmp = 4

    .. data:: egp = 5

    .. data:: ggp = 6

    .. data:: hello = 7

    .. data:: rip = 8

    .. data:: isIs = 9

    .. data:: esIs = 10

    .. data:: ciscoIgrp = 11

    .. data:: bbnSpfIgp = 12

    .. data:: ospf = 13

    .. data:: bgp = 14

    .. data:: idpr = 15

    .. data:: ciscoEigrp = 16

    .. data:: dvmrp = 17

    """

    other = Enum.YLeaf(1, "other")

    local = Enum.YLeaf(2, "local")

    netmgmt = Enum.YLeaf(3, "netmgmt")

    icmp = Enum.YLeaf(4, "icmp")

    egp = Enum.YLeaf(5, "egp")

    ggp = Enum.YLeaf(6, "ggp")

    hello = Enum.YLeaf(7, "hello")

    rip = Enum.YLeaf(8, "rip")

    isIs = Enum.YLeaf(9, "isIs")

    esIs = Enum.YLeaf(10, "esIs")

    ciscoIgrp = Enum.YLeaf(11, "ciscoIgrp")

    bbnSpfIgp = Enum.YLeaf(12, "bbnSpfIgp")

    ospf = Enum.YLeaf(13, "ospf")

    bgp = Enum.YLeaf(14, "bgp")

    idpr = Enum.YLeaf(15, "idpr")

    ciscoEigrp = Enum.YLeaf(16, "ciscoEigrp")

    dvmrp = Enum.YLeaf(17, "dvmrp")



