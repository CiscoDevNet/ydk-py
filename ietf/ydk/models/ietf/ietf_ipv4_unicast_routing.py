""" ietf_ipv4_unicast_routing 

This YANG module augments the 'ietf\-routing' module with basic
configuration and state data for IPv4 unicast routing.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code. All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject to
the license terms contained in, the Simplified BSD License set
forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

The key words 'MUST', 'MUST NOT', 'REQUIRED', 'SHALL', 'SHALL
NOT', 'SHOULD', 'SHOULD NOT', 'RECOMMENDED', 'MAY', and
'OPTIONAL' in the module text are to be interpreted as described
in RFC 2119 (http\://tools.ietf.org/html/rfc2119).

This version of this YANG module is part of RFC XXXX
(http\://tools.ietf.org/html/rfcXXXX); see the RFC itself for
full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_routing import Ipv4Identity


class Ipv4UnicastIdentity(Ipv4Identity):
    """
    This identity represents the IPv4 unicast address family.
    
    

    """

    _prefix = 'v4ur'
    _revision = '2015-05-25'

    def __init__(self):
        Ipv4Identity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ipv4_unicast_routing as meta
        return meta._meta_table['Ipv4UnicastIdentity']['meta_info']


