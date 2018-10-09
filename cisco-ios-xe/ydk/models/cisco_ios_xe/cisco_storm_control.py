""" cisco_storm_control 

This module defines data model for strom control feature.

Traffic storm occurs when packets flood a bridge, creating
excessive traffic and degrading network performance. Traffic
storm control prevents bridge disruption by suppressing traffic
when the number of packets reaches configured threshold
levels.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class StormControlAction(Identity):
    """
    Actions to be taken once storm control limit threshold is
    exceeded for a traffic class.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-storm-control", pref="cisco-storm-control", tag="cisco-storm-control:storm-control-action"):
        super(StormControlAction, self).__init__(ns, pref, tag)


class ActionShutdown(StormControlAction):
    """
    Shutdown service.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-storm-control", pref="cisco-storm-control", tag="cisco-storm-control:action-shutdown"):
        super(ActionShutdown, self).__init__(ns, pref, tag)


class ActionSnmpTrap(StormControlAction):
    """
    Generate SNMP traps.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-storm-control", pref="cisco-storm-control", tag="cisco-storm-control:action-snmp-trap"):
        super(ActionSnmpTrap, self).__init__(ns, pref, tag)


class ActionDrop(StormControlAction):
    """
    Drop packets.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self, ns="urn:cisco:params:xml:ns:yang:cisco-storm-control", pref="cisco-storm-control", tag="cisco-storm-control:action-drop"):
        super(ActionDrop, self).__init__(ns, pref, tag)


