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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Direction(Identity):
    """
    This is identity of traffic direction
    
    

    """

    _prefix = 'target'
    _revision = '2015-04-07'

    def __init__(self):
        super(Direction, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-target", "ietf-diffserv-target", "ietf-diffserv-target:direction")


class Inbound(Identity):
    """
    Direction of traffic coming into the network entry
    
    

    """

    _prefix = 'target'
    _revision = '2015-04-07'

    def __init__(self):
        super(Inbound, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-target", "ietf-diffserv-target", "ietf-diffserv-target:inbound")


class Outbound(Identity):
    """
    Direction of traffic going out of the network entry
    
    

    """

    _prefix = 'target'
    _revision = '2015-04-07'

    def __init__(self):
        super(Outbound, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-target", "ietf-diffserv-target", "ietf-diffserv-target:outbound")


