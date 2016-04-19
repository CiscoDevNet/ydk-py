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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IpVersionEnum(Enum):
    """
    IpVersionEnum

    This value represents the version of the IP protocol.

    In the value set and its semantics, this type is equivalent

    to the InetVersion textual convention of the SMIv2.

    .. data:: UNKNOWN = 0

    	An unknown or unspecified version of the Internet

    	protocol.

    .. data:: IPV4 = 1

    	The IPv4 protocol as defined in RFC 791.

    .. data:: IPV6 = 2

    	The IPv6 protocol as defined in RFC 2460.

    """

    UNKNOWN = 0

    IPV4 = 1

    IPV6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_inet_types as meta
        return meta._meta_table['IpVersionEnum']



