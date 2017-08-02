""" cisco_storm_control 

This module defines data model for strom control feature.

Traffic storm occurs when packets flood a bridge, creating
excessive traffic and degrading network performance. Traffic
storm control prevents bridge disruption by suppressing traffic
when the number of packets reaches configured threshold
levels.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class StormControlAction(Identity):
    """
    Actions to be taken once storm control limit threshold is
    exceeded for a traffic class.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        super(StormControlAction, self).__init__("urn:cisco:params:xml:ns:yang:cisco-storm-control", "cisco-storm-control", "cisco-storm-control:storm-control-action")


class ActionDrop(Identity):
    """
    Drop packets.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        super(ActionDrop, self).__init__("urn:cisco:params:xml:ns:yang:cisco-storm-control", "cisco-storm-control", "cisco-storm-control:action-drop")


class ActionShutdown(Identity):
    """
    Shutdown service.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        super(ActionShutdown, self).__init__("urn:cisco:params:xml:ns:yang:cisco-storm-control", "cisco-storm-control", "cisco-storm-control:action-shutdown")


class ActionSnmpTrap(Identity):
    """
    Generate SNMP traps.
    
    

    """

    _prefix = 'cisco-stormctrl'
    _revision = '2016-12-14'

    def __init__(self):
        super(ActionSnmpTrap, self).__init__("urn:cisco:params:xml:ns:yang:cisco-storm-control", "cisco-storm-control", "cisco-storm-control:action-snmp-trap")


