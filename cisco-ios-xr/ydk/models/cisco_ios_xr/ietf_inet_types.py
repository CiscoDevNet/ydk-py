""" ietf_inet_types 

This module contains a collection of generally useful derived
YANG data types for Internet addresses and related things.

Copyright (c) 2013 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6991; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IpVersion(Enum):
    """
    IpVersion

    This value represents the version of the IP protocol.

    In the value set and its semantics, this type is equivalent

    to the InetVersion textual convention of the SMIv2.

    .. data:: unknown = 0

    	An unknown or unspecified version of the Internet

    	protocol.

    .. data:: ipv4 = 1

    	The IPv4 protocol as defined in RFC 791.

    .. data:: ipv6 = 2

    	The IPv6 protocol as defined in RFC 2460.

    """

    unknown = Enum.YLeaf(0, "unknown")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")



