""" openconfig_inet_types 

This module contains a set of Internet address related
types for use in OpenConfig modules.

Portions of this code were derived from IETF RFC 6021.
Please reproduce this note if possible.

IETF code is subject to the following copyright and license\:
Copyright (c) IETF Trust and the persons identified as authors of
the code.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, is permitted pursuant to, and subject to the license
terms contained in, the Simplified BSD License set forth in
Section 4.c of the IETF Trust's Legal Provisions Relating
to IETF Documents (http\://trustee.ietf.org/license\-info).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpVersion(Enum):
    """
    IpVersion (Enum Class)

    This value represents the version of the IP protocol.

    Note that integer representation of the enumerated values

    are not specified, and are not required to follow the

    InetVersion textual convention in SMIv2.

    .. data:: UNKNOWN = 0

    	An unknown or unspecified version of the Internet

    	protocol.

    .. data:: IPV4 = 4

    	The IPv4 protocol as defined in RFC 791.

    .. data:: IPV6 = 6

    	The IPv6 protocol as defined in RFC 2460.

    """

    UNKNOWN = Enum.YLeaf(0, "UNKNOWN")

    IPV4 = Enum.YLeaf(4, "IPV4")

    IPV6 = Enum.YLeaf(6, "IPV6")



