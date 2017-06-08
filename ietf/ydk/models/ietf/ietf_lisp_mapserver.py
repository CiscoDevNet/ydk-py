""" ietf_lisp_mapserver 

This YANG module defines the generic configuration
data for a LISP Map\-Server. The module can be extended by
vendors to define vendor\-specific configuration parameters
and policies.

Copyright (c) 2015 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6338; see
the RFC itself for full legal notices.


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_lisp import LispRoleIdentity


class MsIdentity(LispRoleIdentity):
    """
    LISP Map\-Server.
    
    

    """

    _prefix = 'lisp-ms'
    _revision = '2016-06-30'

    def __init__(self):
        LispRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_mapserver as meta
        return meta._meta_table['MsIdentity']['meta_info']


