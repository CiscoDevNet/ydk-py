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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_diffserv_policy import ActionType



class Marking(ActionType):
    """
    marking action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:marking"):
        super(Marking, self).__init__(ns, pref, tag)


class DropType(Identity):
    """
    drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:drop-type"):
        super(DropType, self).__init__(ns, pref, tag)


class MinRate(ActionType):
    """
    min\-rate action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:min-rate"):
        super(MinRate, self).__init__(ns, pref, tag)


class Meter(ActionType):
    """
    meter action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:meter"):
        super(Meter, self).__init__(ns, pref, tag)


class Priority(ActionType):
    """
    priority action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:priority"):
        super(Priority, self).__init__(ns, pref, tag)


class MaxRate(ActionType):
    """
    max\-rate action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:max-rate"):
        super(MaxRate, self).__init__(ns, pref, tag)


class MeterActionType(Identity):
    """
    action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:meter-action-type"):
        super(MeterActionType, self).__init__(ns, pref, tag)


class AlgorithmicDrop(ActionType):
    """
    algorithmic\-drop action type
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:algorithmic-drop"):
        super(AlgorithmicDrop, self).__init__(ns, pref, tag)


class AlwaysDrop(DropType):
    """
    always drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:always-drop"):
        super(AlwaysDrop, self).__init__(ns, pref, tag)


class TailDrop(DropType):
    """
    tail drop algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:tail-drop"):
        super(TailDrop, self).__init__(ns, pref, tag)


class MeterActionDrop(MeterActionType):
    """
    drop action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:meter-action-drop"):
        super(MeterActionDrop, self).__init__(ns, pref, tag)


class MeterActionSet(MeterActionType):
    """
    mark action type in a meter
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:meter-action-set"):
        super(MeterActionSet, self).__init__(ns, pref, tag)


class RandomDetect(DropType):
    """
    random detect algorithm
    
    

    """

    _prefix = 'action'
    _revision = '2015-04-07'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-diffserv-action", pref="ietf-diffserv-action", tag="ietf-diffserv-action:random-detect"):
        super(RandomDetect, self).__init__(ns, pref, tag)


