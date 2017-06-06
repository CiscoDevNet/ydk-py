""" ietf_diffserv_target 

This module contains a collection of YANG definitions for
configuring diffserv specification implementations.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class DirectionIdentity(object):
    """
    This is identity of traffic direction
    
    

    """

    _prefix = 'target'
    _revision = '2015-04-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_diffserv_target as meta
        return meta._meta_table['DirectionIdentity']['meta_info']


class InboundIdentity(DirectionIdentity):
    """
    Direction of traffic coming into the network entry
    
    

    """

    _prefix = 'target'
    _revision = '2015-04-07'

    def __init__(self):
        DirectionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_diffserv_target as meta
        return meta._meta_table['InboundIdentity']['meta_info']


class OutboundIdentity(DirectionIdentity):
    """
    Direction of traffic going out of the network entry
    
    

    """

    _prefix = 'target'
    _revision = '2015-04-07'

    def __init__(self):
        DirectionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_diffserv_target as meta
        return meta._meta_table['OutboundIdentity']['meta_info']


