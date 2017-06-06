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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IanaipmrouteprotocolEnum(Enum):
    """
    IanaipmrouteprotocolEnum

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

    other = 1

    local = 2

    netmgmt = 3

    dvmrp = 4

    mospf = 5

    pimSparseDense = 6

    cbt = 7

    pimSparseMode = 8

    pimDenseMode = 9

    igmpOnly = 10

    bgmp = 11

    msdp = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IANA_RTPROTO_MIB as meta
        return meta._meta_table['IanaipmrouteprotocolEnum']


class IanaiprouteprotocolEnum(Enum):
    """
    IanaiprouteprotocolEnum

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

    other = 1

    local = 2

    netmgmt = 3

    icmp = 4

    egp = 5

    ggp = 6

    hello = 7

    rip = 8

    isIs = 9

    esIs = 10

    ciscoIgrp = 11

    bbnSpfIgp = 12

    ospf = 13

    bgp = 14

    idpr = 15

    ciscoEigrp = 16

    dvmrp = 17


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IANA_RTPROTO_MIB as meta
        return meta._meta_table['IanaiprouteprotocolEnum']



