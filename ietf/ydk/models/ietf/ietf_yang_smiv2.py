""" ietf_yang_smiv2 

This module defines YANG extensions that are used to translate
SMIv2 concepts into YANG.

Copyright (c) 2012 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6643; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ObjectIdentityIdentity(object):
    """
    Base identity for all SMIv2 OBJECT\-IDENTITYs.
    
    

    """

    _prefix = 'ietf-yang-smiv2'
    _revision = '2012-06-22'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_yang_smiv2 as meta
        return meta._meta_table['ObjectIdentityIdentity']['meta_info']


