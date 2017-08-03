""" ietf_diffserv_action 

This module contains a collection of YANG definitions for configuring
diffserv specification implementations. Copyright (c) 2014 IETF
Trust and the persons identified as authors of the code. All rights
reserved. Redistribution and use in source and binary forms, with
or without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents (http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC XXXX; see the
RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Marking(Identity):
    """
    marking action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(Marking, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:marking")


class DropType(Identity):
    """
    drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(DropType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:drop-type")


class MeterActionType(Identity):
    """
    action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(MeterActionType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:meter-action-type")


class Meter(Identity):
    """
    meter action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(Meter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:meter")


class AlgorithmicDrop(Identity):
    """
    algorithmic\-drop action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(AlgorithmicDrop, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:algorithmic-drop")


class MinRate(Identity):
    """
    min\-rate action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(MinRate, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:min-rate")


class MaxRate(Identity):
    """
    max\-rate action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(MaxRate, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:max-rate")


class Priority(Identity):
    """
    priority action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(Priority, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:priority")


class AlwaysDrop(Identity):
    """
    always drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(AlwaysDrop, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:always-drop")


class RandomDetect(Identity):
    """
    random detect algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(RandomDetect, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:random-detect")


class MeterActionSet(Identity):
    """
    mark action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(MeterActionSet, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:meter-action-set")


class TailDrop(Identity):
    """
    tail drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(TailDrop, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:tail-drop")


class MeterActionDrop(Identity):
    """
    drop action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self):
        super(MeterActionDrop, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-action", "ietf-diffserv-action", "ietf-diffserv-action:meter-action-drop")


