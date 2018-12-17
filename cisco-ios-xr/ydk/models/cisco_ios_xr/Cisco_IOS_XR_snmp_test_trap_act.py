""" Cisco_IOS_XR_snmp_test_trap_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SnmpColdStart(Entity):
    """
    Generate SNMPv2\-MIB\:\:coldStart
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(SnmpColdStart, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp-cold-start"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:snmp-cold-start"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = SnmpColdStart()
        return self._top_entity

class SnmpWarmStart(Entity):
    """
    Generate SNMPv2\-MIB\:\:warmStart
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(SnmpWarmStart, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp-warm-start"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:snmp-warm-start"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = SnmpWarmStart()
        return self._top_entity

class InterfaceLinkUp(Entity):
    """
    Generate IF\-MIB\:\:linkUp
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.InterfaceLinkUp.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InterfaceLinkUp, self).__init__()
        self._top_entity = None

        self.yang_name = "interface-link-up"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InterfaceLinkUp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:interface-link-up"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate LinkUp trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(InterfaceLinkUp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "interface-link-up"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
            ])
            self.ifindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:interface-link-up/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceLinkUp.Input, ['ifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfaceLinkUp()
        return self._top_entity

class InterfaceLinkDown(Entity):
    """
    Generate IF\-MIB\:\:linkDown
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.InterfaceLinkDown.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InterfaceLinkDown, self).__init__()
        self._top_entity = None

        self.yang_name = "interface-link-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InterfaceLinkDown.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:interface-link-down"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate LinkDown trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(InterfaceLinkDown.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "interface-link-down"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
            ])
            self.ifindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:interface-link-down/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InterfaceLinkDown.Input, ['ifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfaceLinkDown()
        return self._top_entity

class SonetSectionStatus(Entity):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetSectionStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetSectionStatus.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(SonetSectionStatus, self).__init__()
        self._top_entity = None

        self.yang_name = "sonet-section-status"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = SonetSectionStatus.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:sonet-section-status"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetSectionStatusChange trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(SonetSectionStatus.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sonet-section-status"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
            ])
            self.ifindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:sonet-section-status/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SonetSectionStatus.Input, ['ifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = SonetSectionStatus()
        return self._top_entity

class SonetLineStatus(Entity):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetLineStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetLineStatus.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(SonetLineStatus, self).__init__()
        self._top_entity = None

        self.yang_name = "sonet-line-status"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = SonetLineStatus.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:sonet-line-status"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetLineStatusChange trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(SonetLineStatus.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sonet-line-status"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
            ])
            self.ifindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:sonet-line-status/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SonetLineStatus.Input, ['ifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = SonetLineStatus()
        return self._top_entity

class SonetPathStatus(Entity):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetPathStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetPathStatus.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(SonetPathStatus, self).__init__()
        self._top_entity = None

        self.yang_name = "sonet-path-status"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = SonetPathStatus.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:sonet-path-status"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetPathStatusChange trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(SonetPathStatus.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sonet-path-status"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
            ])
            self.ifindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:sonet-path-status/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SonetPathStatus.Input, ['ifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = SonetPathStatus()
        return self._top_entity

class InfraSyslogMessageGenerated(Entity):
    """
    Generate CISCO\-SYSLOG\-MIB\:\:clogMessageGenerated
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraSyslogMessageGenerated, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-syslog-message-generated"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-syslog-message-generated"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraSyslogMessageGenerated()
        return self._top_entity

class InfraFlashDeviceInserted(Entity):
    """
    Generate CISCO\-FLASH\-MIB\:\:ciscoFlashDeviceInsertedNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraFlashDeviceInserted, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-flash-device-inserted"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-flash-device-inserted"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraFlashDeviceInserted()
        return self._top_entity

class InfraFlashDeviceRemoved(Entity):
    """
    Generate CISCO\-FLASH\-MIB\:\:ciscoFlashDeviceRemovedNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraFlashDeviceRemoved, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-flash-device-removed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-flash-device-removed"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraFlashDeviceRemoved()
        return self._top_entity

class InfraRedundancyProgression(Entity):
    """
    Generate CISCO\-RF\-MIB\:\:ciscoRFProgressionNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraRedundancyProgression, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-redundancy-progression"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-redundancy-progression"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraRedundancyProgression()
        return self._top_entity

class InfraRedundancySwitch(Entity):
    """
    Generate CISCO\-RF\-MIB\:\:ciscoRFSwactNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraRedundancySwitch, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-redundancy-switch"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-redundancy-switch"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraRedundancySwitch()
        return self._top_entity

class InfraBridgeNewRoot(Entity):
    """
    Generate BRIDGE\-MIB\:\:newRoot
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraBridgeNewRoot, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-bridge-new-root"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-bridge-new-root"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraBridgeNewRoot()
        return self._top_entity

class InfraBridgeTopologyChange(Entity):
    """
    Generate BRIDGE\-MIB\:\:topologyChange
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraBridgeTopologyChange, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-bridge-topology-change"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-bridge-topology-change"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraBridgeTopologyChange()
        return self._top_entity

class InfraConfigEvent(Entity):
    """
    Generate CISCO\-CONFIG\-MAN\-MIB\:\:ciscoConfigManEvent
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(InfraConfigEvent, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-config-event"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:infra-config-event"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = InfraConfigEvent()
        return self._top_entity

class EntitySensorThresholdNotification(Entity):
    """
    Generate CISCO\-ENTITY\-SENSOR\-MIB\:\:entSensorThresholdNotification
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntitySensorThresholdNotification.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntitySensorThresholdNotification, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-sensor-threshold-notification"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntitySensorThresholdNotification.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-sensor-threshold-notification"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntitySensorThresholdNotification.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-sensor-threshold-notification"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-sensor-threshold-notification/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntitySensorThresholdNotification.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntitySensorThresholdNotification()
        return self._top_entity

class EntityFruPowerStatusChangeFailed(Entity):
    """
    oper status changed to failed
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruPowerStatusChangeFailed.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntityFruPowerStatusChangeFailed, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-power-status-change-failed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntityFruPowerStatusChangeFailed.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-power-status-change-failed"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntityFruPowerStatusChangeFailed.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-power-status-change-failed"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-power-status-change-failed/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntityFruPowerStatusChangeFailed.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntityFruPowerStatusChangeFailed()
        return self._top_entity

class EntityFruModuleStatusChangeUp(Entity):
    """
    fu trap module status changed as ok
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruModuleStatusChangeUp.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntityFruModuleStatusChangeUp, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-module-status-change-up"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntityFruModuleStatusChangeUp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-up"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntityFruModuleStatusChangeUp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-module-status-change-up"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-up/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntityFruModuleStatusChangeUp.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntityFruModuleStatusChangeUp()
        return self._top_entity

class EntityFruModuleStatusChangeDown(Entity):
    """
    fu trap module status changed as failed
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruModuleStatusChangeDown.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntityFruModuleStatusChangeDown, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-module-status-change-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntityFruModuleStatusChangeDown.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-down"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntityFruModuleStatusChangeDown.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-module-status-change-down"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-down/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntityFruModuleStatusChangeDown.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntityFruModuleStatusChangeDown()
        return self._top_entity

class EntityFruFanTrayOperStatusUp(Entity):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFanTrayStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayOperStatusUp.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntityFruFanTrayOperStatusUp, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-fan-tray-oper-status-up"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntityFruFanTrayOperStatusUp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-oper-status-up"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntityFruFanTrayOperStatusUp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-fan-tray-oper-status-up"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-oper-status-up/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntityFruFanTrayOperStatusUp.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntityFruFanTrayOperStatusUp()
        return self._top_entity

class EntityFruFanTrayInserted(Entity):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFRUInserted
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayInserted.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntityFruFanTrayInserted, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-fan-tray-inserted"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntityFruFanTrayInserted.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-inserted"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntityFruFanTrayInserted.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-fan-tray-inserted"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-inserted/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntityFruFanTrayInserted.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntityFruFanTrayInserted()
        return self._top_entity

class EntityFruFanTrayRemoved(Entity):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFRURemoved
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayRemoved.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(EntityFruFanTrayRemoved, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-fan-tray-removed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EntityFruFanTrayRemoved.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-removed"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\: int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(EntityFruFanTrayRemoved.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-fan-tray-removed"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entindex', (YLeaf(YType.uint32, 'entindex'), ['int'])),
            ])
            self.entindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-removed/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EntityFruFanTrayRemoved.Input, ['entindex'], name, value)

    def clone_ptr(self):
        self._top_entity = EntityFruFanTrayRemoved()
        return self._top_entity

class PlatformHfrBundleDownedLink(Entity):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhBundleDownedLinkNotification
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrBundleDownedLink.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(PlatformHfrBundleDownedLink, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-hfr-bundle-downed-link"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = PlatformHfrBundleDownedLink.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-downed-link"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: bundle_name
        
        	bundle name for which to generate the trap
        	**type**\: str
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(PlatformHfrBundleDownedLink.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "platform-hfr-bundle-downed-link"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('bundle_name', (YLeaf(YType.str, 'bundle-name'), ['str'])),
            ])
            self.bundle_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-downed-link/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformHfrBundleDownedLink.Input, ['bundle_name'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformHfrBundleDownedLink()
        return self._top_entity

class PlatformHfrBundleState(Entity):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhBundleStateNotification
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrBundleState.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(PlatformHfrBundleState, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-hfr-bundle-state"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = PlatformHfrBundleState.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-state"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: bundle_name
        
        	bundle name for which to generate the trap
        	**type**\: str
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(PlatformHfrBundleState.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "platform-hfr-bundle-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('bundle_name', (YLeaf(YType.str, 'bundle-name'), ['str'])),
            ])
            self.bundle_name = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-state/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformHfrBundleState.Input, ['bundle_name'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformHfrBundleState()
        return self._top_entity

class PlatformHfrPlaneState(Entity):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhPlaneStateNotification
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrPlaneState.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(PlatformHfrPlaneState, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-hfr-plane-state"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = PlatformHfrPlaneState.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-plane-state"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: plane_id
        
        	plane identifier for which to generate the trap
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(PlatformHfrPlaneState.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "platform-hfr-plane-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('plane_id', (YLeaf(YType.uint32, 'plane-id'), ['int'])),
            ])
            self.plane_id = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-plane-state/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformHfrPlaneState.Input, ['plane_id'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformHfrPlaneState()
        return self._top_entity

class RoutingBgpEstablished(Entity):
    """
    Generate BGP4\-MIB\:\:bglEstablishedNotification
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingBgpEstablished, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-established"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingBgpEstablished()
        return self._top_entity

class RoutingBgpEstablishedRemotePeer(Entity):
    """
    Generate BGP4\-MIB\:\:bglEstablishedNotification remote peer
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingBgpEstablishedRemotePeer.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingBgpEstablishedRemotePeer, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-established-remote-peer"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingBgpEstablishedRemotePeer.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established-remote-peer"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: address
        
        	BGP remote peer IP address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingBgpEstablishedRemotePeer.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-bgp-established-remote-peer"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
            ])
            self.address = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established-remote-peer/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingBgpEstablishedRemotePeer.Input, ['address'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingBgpEstablishedRemotePeer()
        return self._top_entity

class RoutingBgpStateChange(Entity):
    """
    Generate CISCO\-BGP\-MIB\:\:cbgpBackwardTransition
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingBgpStateChange, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-state-change"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingBgpStateChange()
        return self._top_entity

class RoutingBgpStateChangeRemotePeer(Entity):
    """
    Generate CISCO\-BGP\-MIB\:\:cbgpBackwardTransition remote peer
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingBgpStateChangeRemotePeer.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingBgpStateChangeRemotePeer, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-state-change-remote-peer"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingBgpStateChangeRemotePeer.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change-remote-peer"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: address
        
        	BGP remote peer IP address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingBgpStateChangeRemotePeer.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-bgp-state-change-remote-peer"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
            ])
            self.address = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change-remote-peer/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingBgpStateChangeRemotePeer.Input, ['address'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingBgpStateChangeRemotePeer()
        return self._top_entity

class RoutingOspfNeighborStateChange(Entity):
    """
    Generate OSPF\-TRAP\-MIB\:\:ospfNbrStateChange
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingOspfNeighborStateChange, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-ospf-neighbor-state-change"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingOspfNeighborStateChange()
        return self._top_entity

class RoutingOspfNeighborStateChangeAddress(Entity):
    """
    Generate OSPF\-TRAP\-MIB\:\:ospfNbrStateChange address
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingOspfNeighborStateChangeAddress.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingOspfNeighborStateChangeAddress, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-ospf-neighbor-state-change-address"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingOspfNeighborStateChangeAddress.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change-address"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: address
        
        	neighbor's IP source address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: ifindex
        
        	0 for interfaces having IP addresses or IF\-MIB ifindex of addressless interface
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingOspfNeighborStateChangeAddress.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-ospf-neighbor-state-change-address"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ('ifindex', (YLeaf(YType.uint32, 'ifindex'), ['int'])),
            ])
            self.address = None
            self.ifindex = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change-address/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingOspfNeighborStateChangeAddress.Input, ['address', 'ifindex'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingOspfNeighborStateChangeAddress()
        return self._top_entity

class RoutingMplsLdpSessionDown(Entity):
    """
    Generate MPLS\-LDP\-STD\-MIB\:\:mplsLdpSessionDown
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsLdpSessionDown, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-ldp-session-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingMplsLdpSessionDown()
        return self._top_entity

class RoutingMplsLdpSessionDownEntityId(Entity):
    """
    Generate MPLS\-LDP\-STD\-MIB\:\:mplsLdpSessionDown entity\-id
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsLdpSessionDownEntityId.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsLdpSessionDownEntityId, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-ldp-session-down-entity-id"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingMplsLdpSessionDownEntityId.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down-entity-id"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: entity_id
        
        	entity ldp\-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
        	**type**\: str
        
        	**length:** 23
        
        	**mandatory**\: True
        
        .. attribute:: entity_index
        
        	entity index for which to generate the trap
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: peer_id
        
        	peer ldp\-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
        	**type**\: str
        
        	**length:** 23
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingMplsLdpSessionDownEntityId.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-ldp-session-down-entity-id"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entity_id', (YLeaf(YType.str, 'entity-id'), ['str'])),
                ('entity_index', (YLeaf(YType.uint32, 'entity-index'), ['int'])),
                ('peer_id', (YLeaf(YType.str, 'peer-id'), ['str'])),
            ])
            self.entity_id = None
            self.entity_index = None
            self.peer_id = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down-entity-id/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingMplsLdpSessionDownEntityId.Input, ['entity_id', 'entity_index', 'peer_id'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingMplsLdpSessionDownEntityId()
        return self._top_entity

class RoutingMplsTunnelReRouted(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelRerouted
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsTunnelReRouted, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-routed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReRouted()
        return self._top_entity

class RoutingMplsTunnelReRoutedIndex(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelRerouted index
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelReRoutedIndex.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsTunnelReRoutedIndex, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-routed-index"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingMplsTunnelReRoutedIndex.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed-index"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\: int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\: int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	source address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingMplsTunnelReRoutedIndex.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-tunnel-re-routed-index"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
            ])
            self.index = None
            self.instance = None
            self.source = None
            self.destination = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed-index/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingMplsTunnelReRoutedIndex.Input, ['index', 'instance', 'source', 'destination'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReRoutedIndex()
        return self._top_entity

class RoutingMplsTunnelReOptimized(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelReoptimized
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsTunnelReOptimized, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-optimized"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReOptimized()
        return self._top_entity

class RoutingMplsTunnelReOptimizedIndex(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelReoptimized index
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelReOptimizedIndex.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsTunnelReOptimizedIndex, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-optimized-index"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingMplsTunnelReOptimizedIndex.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized-index"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\: int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\: int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	source address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingMplsTunnelReOptimizedIndex.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-tunnel-re-optimized-index"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
            ])
            self.index = None
            self.instance = None
            self.source = None
            self.destination = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized-index/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingMplsTunnelReOptimizedIndex.Input, ['index', 'instance', 'source', 'destination'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReOptimizedIndex()
        return self._top_entity

class RoutingMplsTunnelDown(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelDown
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsTunnelDown, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelDown()
        return self._top_entity

class RoutingMplsTunnelDownIndex(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelDown index
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelDownIndex.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(RoutingMplsTunnelDownIndex, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-down-index"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RoutingMplsTunnelDownIndex.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down-index"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\: int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\: int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	src address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2017-05-01'

        def __init__(self):
            super(RoutingMplsTunnelDownIndex.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-tunnel-down-index"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('instance', (YLeaf(YType.uint32, 'instance'), ['int'])),
                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                ('destination', (YLeaf(YType.str, 'destination'), ['str'])),
            ])
            self.index = None
            self.instance = None
            self.source = None
            self.destination = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down-index/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingMplsTunnelDownIndex.Input, ['index', 'instance', 'source', 'destination'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelDownIndex()
        return self._top_entity

class All(Entity):
    """
    generate all the supported traps
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2017-05-01'

    def __init__(self):
        super(All, self).__init__()
        self._top_entity = None

        self.yang_name = "all"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-snmp-test-trap-act:all"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = All()
        return self._top_entity

