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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IANAipMRouteProtocol_Enum(Enum):
    """
    IANAipMRouteProtocol_Enum

    The multicast routing protocol.  Inclusion of values for
    multicast routing protocols is not intended to imply that
    those protocols need be supported.

    """

    OTHER = 1

    LOCAL = 2

    NETMGMT = 3

    DVMRP = 4

    MOSPF = 5

    PIMSPARSEDENSE = 6

    CBT = 7

    PIMSPARSEMODE = 8

    PIMDENSEMODE = 9

    IGMPONLY = 10

    BGMP = 11

    MSDP = 12


    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _IANA_RTPROTO_MIB as meta
        return meta._meta_table['IANAipMRouteProtocol_Enum']


class IANAipRouteProtocol_Enum(Enum):
    """
    IANAipRouteProtocol_Enum

    A mechanism for learning routes.  Inclusion of values for
    routing protocols is not intended to imply that those
    protocols need be supported.

    """

    OTHER = 1

    LOCAL = 2

    NETMGMT = 3

    ICMP = 4

    EGP = 5

    GGP = 6

    HELLO = 7

    RIP = 8

    ISIS = 9

    ESIS = 10

    CISCOIGRP = 11

    BBNSPFIGP = 12

    OSPF = 13

    BGP = 14

    IDPR = 15

    CISCOEIGRP = 16

    DVMRP = 17


    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _IANA_RTPROTO_MIB as meta
        return meta._meta_table['IANAipRouteProtocol_Enum']



