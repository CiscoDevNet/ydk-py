""" openconfig_platform 

This module defines a data model for representing a system
component inventory, which can include hardware or software
elements arranged in an arbitrary structure. The primary
relationship supported by the model is containment, e.g.,
components containing subcomponents.

It is expected that this model reflects every field replacable
unit on the device at a minimum (i.e., additional information
may be supplied about non\-replacable components).

Every element in the inventory is termed a 'component' with each
component expected to have a unique name and type, and optionally
a unique system\-assigned identifier and FRU number.  The
uniqueness is guaranteed by the system within the device.

Components may have properties defined by the system that are
modeled as a list of key\-value pairs. These may or may not be
user\-configurable.  The model provides a flag for the system
to optionally indicate which properties are user configurable.

Each component also has a list of 'subcomponents' which are
references to other components. Appearance in a list of
subcomponents indicates a containment relationship as described
above.  For example, a linecard component may have a list of
references to port components that reside on the linecard.

This schema is generic to allow devices to express their own
platform\-specific structure.  It may be augmented by additional
component type\-specific schemas that provide a common structure
for well\-known component types.  In these cases, the system is
expected to populate the common component schema, and may
optionally also represent the component and its properties in the
generic structure.

The properties for each component may include dynamic values,
e.g., in the 'state' part of the schema.  For example, a CPU
component may report its utilization, temperature, or other
physical properties.  The intent is to capture all platform\-
specific physical data in one location, including inventory
(presence or absence of a component) and state (physical
attributes or status).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Components(_Entity_):
    """
    Enclosing container for the components in the system.
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of  		 :py:class:`Component <ydk.models.openconfig.openconfig_platform.Components.Component>`
    
    

    """

    _prefix = 'oc-platform'
    _revision = '2018-06-29'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Components, self).__init__()
        self._top_entity = None

        self.yang_name = "components"
        self.yang_parent_name = "openconfig-platform"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("component", ("component", Components.Component))])
        self._leafs = OrderedDict()

        self.component = YList(self)
        self._segment_path = lambda: "openconfig-platform:components"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Components, [], name, value)


    class Component(_Entity_):
        """
        List of components, keyed by component name.
        
        .. attribute:: name  (key)
        
        	References the component name
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
        
        .. attribute:: config
        
        	Configuration data for each component
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
        
        .. attribute:: state
        
        	Operational state data for each component
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.State>`
        
        	**config**\: False
        
        .. attribute:: properties
        
        	Enclosing container 
        	**type**\:  :py:class:`Properties <ydk.models.openconfig.openconfig_platform.Components.Component.Properties>`
        
        .. attribute:: subcomponents
        
        	Enclosing container for subcomponent references
        	**type**\:  :py:class:`Subcomponents <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents>`
        
        .. attribute:: chassis
        
        	Data for chassis components
        	**type**\:  :py:class:`Chassis <ydk.models.openconfig.openconfig_platform.Components.Component.Chassis>`
        
        .. attribute:: port
        
        	Data for physical port components
        	**type**\:  :py:class:`Port <ydk.models.openconfig.openconfig_platform.Components.Component.Port>`
        
        .. attribute:: power_supply
        
        	Data for power supply components
        	**type**\:  :py:class:`PowerSupply <ydk.models.openconfig.openconfig_platform.Components.Component.PowerSupply>`
        
        .. attribute:: fan
        
        	Data for fan components
        	**type**\:  :py:class:`Fan <ydk.models.openconfig.openconfig_platform.Components.Component.Fan>`
        
        .. attribute:: fabric
        
        	Data for fabric components
        	**type**\:  :py:class:`Fabric <ydk.models.openconfig.openconfig_platform.Components.Component.Fabric>`
        
        .. attribute:: storage
        
        	Data for storage components
        	**type**\:  :py:class:`Storage <ydk.models.openconfig.openconfig_platform.Components.Component.Storage>`
        
        .. attribute:: cpu
        
        	Data for cpu components
        	**type**\:  :py:class:`Cpu <ydk.models.openconfig.openconfig_platform.Components.Component.Cpu>`
        
        .. attribute:: integrated_circuit
        
        	Data for chip components, such as ASIC, NPUs, etc
        	**type**\:  :py:class:`IntegratedCircuit <ydk.models.openconfig.openconfig_platform.Components.Component.IntegratedCircuit>`
        
        .. attribute:: backplane
        
        	Data for backplane components
        	**type**\:  :py:class:`Backplane <ydk.models.openconfig.openconfig_platform.Components.Component.Backplane>`
        
        .. attribute:: transceiver
        
        	Top\-level container for client port transceiver data
        	**type**\:  :py:class:`Transceiver <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver>`
        
        .. attribute:: optical_channel
        
        	Enclosing container for the list of optical channels
        	**type**\:  :py:class:`OpticalChannel <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel>`
        
        .. attribute:: optical_port
        
        	Top\-level container 
        	**type**\:  :py:class:`OpticalPort <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort>`
        
        .. attribute:: linecard
        
        	Top\-level container for linecard data
        	**type**\:  :py:class:`Linecard <ydk.models.openconfig.openconfig_platform.Components.Component.Linecard>`
        
        

        """

        _prefix = 'oc-platform'
        _revision = '2018-06-29'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Components.Component, self).__init__()

            self.yang_name = "component"
            self.yang_parent_name = "components"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("config", ("config", Components.Component.Config)), ("state", ("state", Components.Component.State)), ("properties", ("properties", Components.Component.Properties)), ("subcomponents", ("subcomponents", Components.Component.Subcomponents)), ("chassis", ("chassis", Components.Component.Chassis)), ("port", ("port", Components.Component.Port)), ("power-supply", ("power_supply", Components.Component.PowerSupply)), ("fan", ("fan", Components.Component.Fan)), ("fabric", ("fabric", Components.Component.Fabric)), ("storage", ("storage", Components.Component.Storage)), ("cpu", ("cpu", Components.Component.Cpu)), ("integrated-circuit", ("integrated_circuit", Components.Component.IntegratedCircuit)), ("backplane", ("backplane", Components.Component.Backplane)), ("openconfig-platform-transceiver:transceiver", ("transceiver", Components.Component.Transceiver)), ("openconfig-terminal-device:optical-channel", ("optical_channel", Components.Component.OpticalChannel)), ("openconfig-transport-line-common:optical-port", ("optical_port", Components.Component.OpticalPort)), ("openconfig-platform-linecard:linecard", ("linecard", Components.Component.Linecard))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
            ])
            self.name = None

            self.config = Components.Component.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = Components.Component.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.properties = Components.Component.Properties()
            self.properties.parent = self
            self._children_name_map["properties"] = "properties"

            self.subcomponents = Components.Component.Subcomponents()
            self.subcomponents.parent = self
            self._children_name_map["subcomponents"] = "subcomponents"

            self.chassis = Components.Component.Chassis()
            self.chassis.parent = self
            self._children_name_map["chassis"] = "chassis"

            self.port = Components.Component.Port()
            self.port.parent = self
            self._children_name_map["port"] = "port"

            self.power_supply = Components.Component.PowerSupply()
            self.power_supply.parent = self
            self._children_name_map["power_supply"] = "power-supply"

            self.fan = Components.Component.Fan()
            self.fan.parent = self
            self._children_name_map["fan"] = "fan"

            self.fabric = Components.Component.Fabric()
            self.fabric.parent = self
            self._children_name_map["fabric"] = "fabric"

            self.storage = Components.Component.Storage()
            self.storage.parent = self
            self._children_name_map["storage"] = "storage"

            self.cpu = Components.Component.Cpu()
            self.cpu.parent = self
            self._children_name_map["cpu"] = "cpu"

            self.integrated_circuit = Components.Component.IntegratedCircuit()
            self.integrated_circuit.parent = self
            self._children_name_map["integrated_circuit"] = "integrated-circuit"

            self.backplane = Components.Component.Backplane()
            self.backplane.parent = self
            self._children_name_map["backplane"] = "backplane"

            self.transceiver = Components.Component.Transceiver()
            self.transceiver.parent = self
            self._children_name_map["transceiver"] = "openconfig-platform-transceiver:transceiver"

            self.optical_channel = Components.Component.OpticalChannel()
            self.optical_channel.parent = self
            self._children_name_map["optical_channel"] = "openconfig-terminal-device:optical-channel"

            self.optical_port = Components.Component.OpticalPort()
            self.optical_port.parent = self
            self._children_name_map["optical_port"] = "openconfig-transport-line-common:optical-port"

            self.linecard = Components.Component.Linecard()
            self.linecard.parent = self
            self._children_name_map["linecard"] = "openconfig-platform-linecard:linecard"
            self._segment_path = lambda: "component" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "openconfig-platform:components/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Components.Component, ['name'], name, value)


        class Config(_Entity_):
            """
            Configuration data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations.  Where component preconfiguration is supported, for example, the component name may be configurable
            	**type**\: str
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None
                self._segment_path = lambda: "config"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Config, ['name'], name, value)



        class State(_Entity_):
            """
            Operational state data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations.  Where component preconfiguration is supported, for example, the component name may be configurable
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: type
            
            	Type of component as identified by the system
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`OPENCONFIGHARDWARECOMPONENT <ydk.models.openconfig.openconfig_platform_types.OPENCONFIGHARDWARECOMPONENT>`
            
            		**type**\:  :py:class:`OPENCONFIGSOFTWARECOMPONENT <ydk.models.openconfig.openconfig_platform_types.OPENCONFIGSOFTWARECOMPONENT>`
            
            	**config**\: False
            
            .. attribute:: id
            
            	Unique identifier assigned by the system for the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: location
            
            	System\-supplied description of the location of the component within the system. This could be a bay position, slot number, socket location, etc. For component types that have an explicit slot\-id attribute, such as linecards, the system should populate the more specific slot\-id
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: description
            
            	System\-supplied description of the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mfg_name
            
            	System\-supplied identifier for the manufacturer of the component.  This data is particularly useful when a component manufacturer is different than the overall device vendor
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mfg_date
            
            	System\-supplied representation of the component's manufacturing date
            	**type**\: str
            
            	**pattern:** ^[0\-9]{4}\\\-[0\-9]{2}\\\-[0\-9]{2}$
            
            	**config**\: False
            
            .. attribute:: hardware_version
            
            	For hardware components, this is the hardware revision of the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: firmware_version
            
            	For hardware components, this is the version of associated firmware that is running on the component, if applicable
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: software_version
            
            	For software components such as operating system or other software module, this is the version of the currently running software
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: serial_no
            
            	System\-assigned serial number of the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: part_no
            
            	System\-assigned part number for the component.  This should be present in particular if the component is also an FRU (field replaceable unit)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: removable
            
            	If true, this component is removable or is a field replaceable unit
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: oper_status
            
            	If applicable, this reports the current operational status of the component
            	**type**\:  :py:class:`COMPONENTOPERSTATUS <ydk.models.openconfig.openconfig_platform_types.COMPONENTOPERSTATUS>`
            
            	**config**\: False
            
            .. attribute:: empty
            
            	The empty leaf may be used by the device to indicate that a component position exists but is not populated.  Using this flag, it is possible for the management system to learn how many positions are available (e.g., occupied vs. empty linecard slots in a chassis)
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: parent_
            
            	Reference to the name of the parent component.  Note that this reference must be kept synchronized with the corresponding subcomponent reference from the parent component
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
            
            	**config**\: False
            
            .. attribute:: temperature
            
            	Temperature in degrees Celsius of the component. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
            	**type**\:  :py:class:`Temperature <ydk.models.openconfig.openconfig_platform.Components.Component.State.Temperature>`
            
            	**config**\: False
            
            .. attribute:: memory
            
            	For components that have associated memory, these values report information about available and utilized memory
            	**type**\:  :py:class:`Memory <ydk.models.openconfig.openconfig_platform.Components.Component.State.Memory>`
            
            	**config**\: False
            
            .. attribute:: allocated_power
            
            	Power allocated by the system for the component
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: watts
            
            .. attribute:: used_power
            
            	Actual power used by the component
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: watts
            
            .. attribute:: entity_id
            
            	A unique numeric identifier assigned by the system to the component. This identifier may be used to represent the corresponding SNMP Entity MIB identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: equipment_failure
            
            	If true, the hardware indicates that the component's physical equipment has failed
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            .. attribute:: equipment_mismatch
            
            	If true, the hardware indicates that the component inserted into the affected component's physical location is of a different type than what is configured
            	**type**\: bool
            
            	**config**\: False
            
            	**default value**\: false
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("temperature", ("temperature", Components.Component.State.Temperature)), ("memory", ("memory", Components.Component.State.Memory))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('type', (YLeaf(YType.str, 'type'), [('ydk.models.openconfig.openconfig_platform_types', 'OPENCONFIGHARDWARECOMPONENT'),('ydk.models.openconfig.openconfig_platform_types', 'OPENCONFIGSOFTWARECOMPONENT')])),
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('mfg_name', (YLeaf(YType.str, 'mfg-name'), ['str'])),
                    ('mfg_date', (YLeaf(YType.str, 'mfg-date'), ['str'])),
                    ('hardware_version', (YLeaf(YType.str, 'hardware-version'), ['str'])),
                    ('firmware_version', (YLeaf(YType.str, 'firmware-version'), ['str'])),
                    ('software_version', (YLeaf(YType.str, 'software-version'), ['str'])),
                    ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                    ('part_no', (YLeaf(YType.str, 'part-no'), ['str'])),
                    ('removable', (YLeaf(YType.boolean, 'removable'), ['bool'])),
                    ('oper_status', (YLeaf(YType.identityref, 'oper-status'), [('ydk.models.openconfig.openconfig_platform_types', 'COMPONENTOPERSTATUS')])),
                    ('empty', (YLeaf(YType.boolean, 'empty'), ['bool'])),
                    ('parent_', (YLeaf(YType.str, 'parent'), ['str'])),
                    ('allocated_power', (YLeaf(YType.uint32, 'allocated-power'), ['int'])),
                    ('used_power', (YLeaf(YType.uint32, 'used-power'), ['int'])),
                    ('entity_id', (YLeaf(YType.uint32, 'openconfig-platform-ext:entity-id'), ['int'])),
                    ('equipment_failure', (YLeaf(YType.boolean, 'openconfig-alarms:equipment-failure'), ['bool'])),
                    ('equipment_mismatch', (YLeaf(YType.boolean, 'openconfig-alarms:equipment-mismatch'), ['bool'])),
                ])
                self.name = None
                self.type = None
                self.id = None
                self.location = None
                self.description = None
                self.mfg_name = None
                self.mfg_date = None
                self.hardware_version = None
                self.firmware_version = None
                self.software_version = None
                self.serial_no = None
                self.part_no = None
                self.removable = None
                self.oper_status = None
                self.empty = None
                self.parent_ = None
                self.allocated_power = None
                self.used_power = None
                self.entity_id = None
                self.equipment_failure = None
                self.equipment_mismatch = None

                self.temperature = Components.Component.State.Temperature()
                self.temperature.parent = self
                self._children_name_map["temperature"] = "temperature"

                self.memory = Components.Component.State.Memory()
                self.memory.parent = self
                self._children_name_map["memory"] = "memory"
                self._segment_path = lambda: "state"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.State, ['name', 'type', 'id', 'location', 'description', 'mfg_name', 'mfg_date', 'hardware_version', 'firmware_version', 'software_version', 'serial_no', 'part_no', 'removable', 'oper_status', 'empty', 'parent_', 'allocated_power', 'used_power', 'entity_id', 'equipment_failure', 'equipment_mismatch'], name, value)


            class Temperature(_Entity_):
                """
                Temperature in degrees Celsius of the component. Values include
                the instantaneous, average, minimum, and maximum statistics. If
                avg/min/max statistics are not supported, the target is expected
                to just supply the instant value
                
                .. attribute:: instant
                
                	The instantaneous value of the statistic
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-922337203685477580.8..922337203685477580.7
                
                	**config**\: False
                
                	**units**\: celsius
                
                .. attribute:: avg
                
                	The arithmetic mean value of the statistic over the sampling period
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-922337203685477580.8..922337203685477580.7
                
                	**config**\: False
                
                	**units**\: celsius
                
                .. attribute:: min
                
                	The minimum value of the statistic over the sampling period
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-922337203685477580.8..922337203685477580.7
                
                	**config**\: False
                
                	**units**\: celsius
                
                .. attribute:: max
                
                	The maximum value of the statistic over the sampling period
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-922337203685477580.8..922337203685477580.7
                
                	**config**\: False
                
                	**units**\: celsius
                
                .. attribute:: interval
                
                	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: min_time
                
                	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: max_time
                
                	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: alarm_status
                
                	A value of true indicates the alarm has been raised or asserted.  The value should be false when the alarm is cleared
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: alarm_threshold
                
                	The threshold value that was crossed for this alarm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: alarm_severity
                
                	The severity of the current alarm
                	**type**\:  :py:class:`OPENCONFIGALARMSEVERITY <ydk.models.openconfig.openconfig_alarm_types.OPENCONFIGALARMSEVERITY>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.State.Temperature, self).__init__()

                    self.yang_name = "temperature"
                    self.yang_parent_name = "state"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                        ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                        ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                        ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                        ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                        ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ('alarm_status', (YLeaf(YType.boolean, 'alarm-status'), ['bool'])),
                        ('alarm_threshold', (YLeaf(YType.uint32, 'alarm-threshold'), ['int'])),
                        ('alarm_severity', (YLeaf(YType.identityref, 'alarm-severity'), [('ydk.models.openconfig.openconfig_alarm_types', 'OPENCONFIGALARMSEVERITY')])),
                    ])
                    self.instant = None
                    self.avg = None
                    self.min = None
                    self.max = None
                    self.interval = None
                    self.min_time = None
                    self.max_time = None
                    self.alarm_status = None
                    self.alarm_threshold = None
                    self.alarm_severity = None
                    self._segment_path = lambda: "temperature"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.State.Temperature, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time', 'alarm_status', 'alarm_threshold', 'alarm_severity'], name, value)



            class Memory(_Entity_):
                """
                For components that have associated memory, these values
                report information about available and utilized memory.
                
                .. attribute:: available
                
                	The available memory physically installed, or logically allocated to the component
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: bytes
                
                .. attribute:: utilized
                
                	The memory currently in use by processes running on the component, not considering reserved memory that is not available for use
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: bytes
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.State.Memory, self).__init__()

                    self.yang_name = "memory"
                    self.yang_parent_name = "state"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('available', (YLeaf(YType.uint64, 'available'), ['int'])),
                        ('utilized', (YLeaf(YType.uint64, 'utilized'), ['int'])),
                    ])
                    self.available = None
                    self.utilized = None
                    self._segment_path = lambda: "memory"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.State.Memory, ['available', 'utilized'], name, value)




        class Properties(_Entity_):
            """
            Enclosing container 
            
            .. attribute:: property
            
            	List of system properties for the component
            	**type**\: list of  		 :py:class:`Property <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Properties, self).__init__()

                self.yang_name = "properties"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("property", ("property", Components.Component.Properties.Property))])
                self._leafs = OrderedDict()

                self.property = YList(self)
                self._segment_path = lambda: "properties"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Properties, [], name, value)


            class Property(_Entity_):
                """
                List of system properties for the component
                
                .. attribute:: name  (key)
                
                	Reference to the property name
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.Config>`
                
                .. attribute:: config
                
                	Configuration data for each property
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.Config>`
                
                .. attribute:: state
                
                	Operational state data for each property
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Properties.Property, self).__init__()

                    self.yang_name = "property"
                    self.yang_parent_name = "properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", Components.Component.Properties.Property.Config)), ("state", ("state", Components.Component.Properties.Property.State))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = Components.Component.Properties.Property.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Components.Component.Properties.Property.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "property" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Properties.Property, ['name'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    		**type**\: bool
                    
                    		**type**\: int
                    
                    			**range:** \-9223372036854775808..9223372036854775807
                    
                    		**type**\: int
                    
                    			**range:** 0..18446744073709551615
                    
                    		**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    			**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2018-06-29'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Properties.Property.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "property"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str','bool','int','int','Decimal64'])),
                        ])
                        self.name = None
                        self.value = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Properties.Property.Config, ['name', 'value'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    		**type**\: bool
                    
                    		**type**\: int
                    
                    			**range:** \-9223372036854775808..9223372036854775807
                    
                    		**type**\: int
                    
                    			**range:** 0..18446744073709551615
                    
                    		**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    			**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: configurable
                    
                    	Indication whether the property is user\-configurable
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2018-06-29'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Properties.Property.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "property"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str','bool','int','int','Decimal64'])),
                            ('configurable', (YLeaf(YType.boolean, 'configurable'), ['bool'])),
                        ])
                        self.name = None
                        self.value = None
                        self.configurable = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Properties.Property.State, ['name', 'value', 'configurable'], name, value)





        class Subcomponents(_Entity_):
            """
            Enclosing container for subcomponent references
            
            .. attribute:: subcomponent
            
            	List of subcomponent references
            	**type**\: list of  		 :py:class:`Subcomponent <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Subcomponents, self).__init__()

                self.yang_name = "subcomponents"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("subcomponent", ("subcomponent", Components.Component.Subcomponents.Subcomponent))])
                self._leafs = OrderedDict()

                self.subcomponent = YList(self)
                self._segment_path = lambda: "subcomponents"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Subcomponents, [], name, value)


            class Subcomponent(_Entity_):
                """
                List of subcomponent references
                
                .. attribute:: name  (key)
                
                	Reference to the name list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: config
                
                	Configuration data for the subcomponent
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: state
                
                	Operational state data for the subcomponent
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Subcomponents.Subcomponent, self).__init__()

                    self.yang_name = "subcomponent"
                    self.yang_parent_name = "subcomponents"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", Components.Component.Subcomponents.Subcomponent.Config)), ("state", ("state", Components.Component.Subcomponents.Subcomponent.State))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = Components.Component.Subcomponents.Subcomponent.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Components.Component.Subcomponents.Subcomponent.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "subcomponent" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Subcomponents.Subcomponent, ['name'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for the subcomponent
                    
                    .. attribute:: name
                    
                    	Reference to the name of the subcomponent
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2018-06-29'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Subcomponents.Subcomponent.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "subcomponent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Subcomponents.Subcomponent.Config, ['name'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for the subcomponent
                    
                    .. attribute:: name
                    
                    	Reference to the name of the subcomponent
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2018-06-29'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Subcomponents.Subcomponent.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subcomponent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Subcomponents.Subcomponent.State, ['name'], name, value)





        class Chassis(_Entity_):
            """
            Data for chassis components
            
            .. attribute:: config
            
            	Configuration data for chassis components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Chassis.Config>`
            
            .. attribute:: state
            
            	Operational state data for chassis components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Chassis.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Chassis, self).__init__()

                self.yang_name = "chassis"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Chassis.Config)), ("state", ("state", Components.Component.Chassis.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Chassis.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Chassis.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "chassis"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Chassis, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for chassis components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Chassis.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "chassis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for chassis components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Chassis.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "chassis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True




        class Port(_Entity_):
            """
            Data for physical port components
            
            .. attribute:: config
            
            	Configuration data for physical port components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Port.Config>`
            
            .. attribute:: state
            
            	Operational state data for physical port components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Port.State>`
            
            	**config**\: False
            
            .. attribute:: breakout_mode
            
            	Top\-level container for port breakout data
            	**type**\:  :py:class:`BreakoutMode <ydk.models.openconfig.openconfig_platform.Components.Component.Port.BreakoutMode>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Port, self).__init__()

                self.yang_name = "port"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Port.Config)), ("state", ("state", Components.Component.Port.State)), ("openconfig-platform-port:breakout-mode", ("breakout_mode", Components.Component.Port.BreakoutMode))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Port.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Port.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.breakout_mode = Components.Component.Port.BreakoutMode()
                self.breakout_mode.parent = self
                self._children_name_map["breakout_mode"] = "openconfig-platform-port:breakout-mode"
                self._segment_path = lambda: "port"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Port, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for physical port components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Port.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for physical port components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Port.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True



            class BreakoutMode(_Entity_):
                """
                Top\-level container for port breakout data
                
                .. attribute:: config
                
                	Configuration data for port breakout
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Port.BreakoutMode.Config>`
                
                .. attribute:: state
                
                	Operational state data for port breakout
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Port.BreakoutMode.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-port'
                _revision = '2018-01-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Port.BreakoutMode, self).__init__()

                    self.yang_name = "breakout-mode"
                    self.yang_parent_name = "port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", Components.Component.Port.BreakoutMode.Config)), ("state", ("state", Components.Component.Port.BreakoutMode.State))])
                    self._leafs = OrderedDict()

                    self.config = Components.Component.Port.BreakoutMode.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Components.Component.Port.BreakoutMode.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "openconfig-platform-port:breakout-mode"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Port.BreakoutMode, [], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for port breakout
                    
                    .. attribute:: num_channels
                    
                    	Sets the number of channels to 'breakout' on a port capable of channelization
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: channel_speed
                    
                    	Sets the channel speed on each channel \-\- the supported values are defined by the ETHERNET\_SPEED identity
                    	**type**\:  :py:class:`ETHERNETSPEED <ydk.models.openconfig.openconfig_if_ethernet.ETHERNETSPEED>`
                    
                    

                    """

                    _prefix = 'oc-port'
                    _revision = '2018-01-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Port.BreakoutMode.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "breakout-mode"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('num_channels', (YLeaf(YType.uint8, 'num-channels'), ['int'])),
                            ('channel_speed', (YLeaf(YType.identityref, 'channel-speed'), [('ydk.models.openconfig.openconfig_if_ethernet', 'ETHERNETSPEED')])),
                        ])
                        self.num_channels = None
                        self.channel_speed = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Port.BreakoutMode.Config, ['num_channels', 'channel_speed'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for port breakout
                    
                    .. attribute:: num_channels
                    
                    	Sets the number of channels to 'breakout' on a port capable of channelization
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: channel_speed
                    
                    	Sets the channel speed on each channel \-\- the supported values are defined by the ETHERNET\_SPEED identity
                    	**type**\:  :py:class:`ETHERNETSPEED <ydk.models.openconfig.openconfig_if_ethernet.ETHERNETSPEED>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-port'
                    _revision = '2018-01-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Port.BreakoutMode.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "breakout-mode"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('num_channels', (YLeaf(YType.uint8, 'num-channels'), ['int'])),
                            ('channel_speed', (YLeaf(YType.identityref, 'channel-speed'), [('ydk.models.openconfig.openconfig_if_ethernet', 'ETHERNETSPEED')])),
                        ])
                        self.num_channels = None
                        self.channel_speed = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Port.BreakoutMode.State, ['num_channels', 'channel_speed'], name, value)





        class PowerSupply(_Entity_):
            """
            Data for power supply components
            
            .. attribute:: config
            
            	Configuration data for power supply components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.PowerSupply.Config>`
            
            .. attribute:: state
            
            	Operational state data for power supply components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.PowerSupply.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.PowerSupply, self).__init__()

                self.yang_name = "power-supply"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.PowerSupply.Config)), ("state", ("state", Components.Component.PowerSupply.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.PowerSupply.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.PowerSupply.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "power-supply"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.PowerSupply, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for power supply components
                
                .. attribute:: enabled
                
                	Adminsitrative control on the on/off state of the power supply unit
                	**type**\: bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.PowerSupply.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "power-supply"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.boolean, 'openconfig-platform-psu:enabled'), ['bool'])),
                    ])
                    self.enabled = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.PowerSupply.Config, ['enabled'], name, value)



            class State(_Entity_):
                """
                Operational state data for power supply components
                
                .. attribute:: enabled
                
                	Adminsitrative control on the on/off state of the power supply unit
                	**type**\: bool
                
                	**config**\: False
                
                	**default value**\: true
                
                .. attribute:: capacity
                
                	Maximum power capacity of the power supply
                	**type**\: str
                
                	**length:** 4..4
                
                	**config**\: False
                
                	**units**\: watts
                
                .. attribute:: input_current
                
                	The input current draw of the power supply
                	**type**\: str
                
                	**length:** 4..4
                
                	**config**\: False
                
                	**units**\: amps
                
                .. attribute:: input_voltage
                
                	Input voltage to the power supply
                	**type**\: str
                
                	**length:** 4..4
                
                	**config**\: False
                
                	**units**\: volts
                
                .. attribute:: output_current
                
                	The output current supplied by the power supply
                	**type**\: str
                
                	**length:** 4..4
                
                	**config**\: False
                
                	**units**\: amps
                
                .. attribute:: output_voltage
                
                	Output voltage supplied by the power supply
                	**type**\: str
                
                	**length:** 4..4
                
                	**config**\: False
                
                	**units**\: volts
                
                .. attribute:: output_power
                
                	Output power supplied by the power supply
                	**type**\: str
                
                	**length:** 4..4
                
                	**config**\: False
                
                	**units**\: watts
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.PowerSupply.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "power-supply"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.boolean, 'openconfig-platform-psu:enabled'), ['bool'])),
                        ('capacity', (YLeaf(YType.str, 'openconfig-platform-psu:capacity'), ['str'])),
                        ('input_current', (YLeaf(YType.str, 'openconfig-platform-psu:input-current'), ['str'])),
                        ('input_voltage', (YLeaf(YType.str, 'openconfig-platform-psu:input-voltage'), ['str'])),
                        ('output_current', (YLeaf(YType.str, 'openconfig-platform-psu:output-current'), ['str'])),
                        ('output_voltage', (YLeaf(YType.str, 'openconfig-platform-psu:output-voltage'), ['str'])),
                        ('output_power', (YLeaf(YType.str, 'openconfig-platform-psu:output-power'), ['str'])),
                    ])
                    self.enabled = None
                    self.capacity = None
                    self.input_current = None
                    self.input_voltage = None
                    self.output_current = None
                    self.output_voltage = None
                    self.output_power = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.PowerSupply.State, ['enabled', 'capacity', 'input_current', 'input_voltage', 'output_current', 'output_voltage', 'output_power'], name, value)




        class Fan(_Entity_):
            """
            Data for fan components
            
            .. attribute:: config
            
            	Configuration data for fan components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Fan.Config>`
            
            .. attribute:: state
            
            	Operational state data for fan components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Fan.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Fan, self).__init__()

                self.yang_name = "fan"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Fan.Config)), ("state", ("state", Components.Component.Fan.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Fan.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Fan.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "fan"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Fan, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for fan components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Fan.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "fan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for fan components
                
                .. attribute:: speed
                
                	Current (instantaneous) fan speed
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: rpm
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Fan.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "fan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('speed', (YLeaf(YType.uint32, 'openconfig-platform-fan:speed'), ['int'])),
                    ])
                    self.speed = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Fan.State, ['speed'], name, value)




        class Fabric(_Entity_):
            """
            Data for fabric components
            
            .. attribute:: config
            
            	Configuration data for fabric components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Fabric.Config>`
            
            .. attribute:: state
            
            	Operational state data for fabric components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Fabric.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Fabric, self).__init__()

                self.yang_name = "fabric"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Fabric.Config)), ("state", ("state", Components.Component.Fabric.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Fabric.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Fabric.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "fabric"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Fabric, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for fabric components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Fabric.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "fabric"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for fabric components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Fabric.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "fabric"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True




        class Storage(_Entity_):
            """
            Data for storage components
            
            .. attribute:: config
            
            	Configuration data for storage components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Storage.Config>`
            
            .. attribute:: state
            
            	Operational state data for storage components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Storage.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Storage, self).__init__()

                self.yang_name = "storage"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Storage.Config)), ("state", ("state", Components.Component.Storage.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Storage.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Storage.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "storage"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Storage, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for storage components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Storage.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "storage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for storage components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Storage.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "storage"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True




        class Cpu(_Entity_):
            """
            Data for cpu components
            
            .. attribute:: config
            
            	Configuration data for cpu components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Cpu.Config>`
            
            .. attribute:: state
            
            	Operational state data for cpu components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Cpu.State>`
            
            	**config**\: False
            
            .. attribute:: utilization
            
            	Statistics representing CPU utilization of the component
            	**type**\:  :py:class:`Utilization <ydk.models.openconfig.openconfig_platform.Components.Component.Cpu.Utilization>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Cpu, self).__init__()

                self.yang_name = "cpu"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Cpu.Config)), ("state", ("state", Components.Component.Cpu.State)), ("openconfig-platform-cpu:utilization", ("utilization", Components.Component.Cpu.Utilization))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Cpu.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Cpu.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.utilization = Components.Component.Cpu.Utilization()
                self.utilization.parent = self
                self._children_name_map["utilization"] = "openconfig-platform-cpu:utilization"
                self._segment_path = lambda: "cpu"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Cpu, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for cpu components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Cpu.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "cpu"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for cpu components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Cpu.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "cpu"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True



            class Utilization(_Entity_):
                """
                Statistics representing CPU utilization of the
                component.
                
                .. attribute:: state
                
                	Operational state variables relating to the utilization of the CPU
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Cpu.Utilization.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-cpu'
                _revision = '2018-01-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Cpu.Utilization, self).__init__()

                    self.yang_name = "utilization"
                    self.yang_parent_name = "cpu"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("state", ("state", Components.Component.Cpu.Utilization.State))])
                    self._leafs = OrderedDict()

                    self.state = Components.Component.Cpu.Utilization.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "openconfig-platform-cpu:utilization"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Cpu.Utilization, [], name, value)


                class State(_Entity_):
                    """
                    Operational state variables relating to the utilization
                    of the CPU.
                    
                    .. attribute:: instant
                    
                    	The instantaneous percentage value
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the percentage measure of the statistic over the time interval
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-cpu'
                    _revision = '2018-01-30'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Cpu.Utilization.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "utilization"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.uint8, 'instant'), ['int'])),
                            ('avg', (YLeaf(YType.uint8, 'avg'), ['int'])),
                            ('min', (YLeaf(YType.uint8, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint8, 'max'), ['int'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Cpu.Utilization.State, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





        class IntegratedCircuit(_Entity_):
            """
            Data for chip components, such as ASIC, NPUs, etc.
            
            .. attribute:: config
            
            	Configuration data for chip components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.IntegratedCircuit.Config>`
            
            .. attribute:: state
            
            	Operational state data for chip components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.IntegratedCircuit.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.IntegratedCircuit, self).__init__()

                self.yang_name = "integrated-circuit"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.IntegratedCircuit.Config)), ("state", ("state", Components.Component.IntegratedCircuit.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.IntegratedCircuit.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.IntegratedCircuit.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "integrated-circuit"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.IntegratedCircuit, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for chip components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.IntegratedCircuit.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "integrated-circuit"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for chip components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.IntegratedCircuit.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "integrated-circuit"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True




        class Backplane(_Entity_):
            """
            Data for backplane components
            
            .. attribute:: config
            
            	Configuration data for backplane components
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Backplane.Config>`
            
            .. attribute:: state
            
            	Operational state data for backplane components
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Backplane.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2018-06-29'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Backplane, self).__init__()

                self.yang_name = "backplane"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Backplane.Config)), ("state", ("state", Components.Component.Backplane.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Backplane.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Backplane.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "backplane"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Backplane, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for backplane components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Backplane.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "backplane"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "config"
                    self._is_frozen = True



            class State(_Entity_):
                """
                Operational state data for backplane components
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2018-06-29'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Backplane.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "backplane"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict()
                    self._segment_path = lambda: "state"
                    self._is_frozen = True




        class Transceiver(_Entity_):
            """
            Top\-level container for client port transceiver data
            
            .. attribute:: config
            
            	Configuration data for client port transceivers
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.Config>`
            
            .. attribute:: state
            
            	Operational state data for client port transceivers
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State>`
            
            	**config**\: False
            
            .. attribute:: physical_channels
            
            	Enclosing container for client channels
            	**type**\:  :py:class:`PhysicalChannels <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels>`
            
            

            """

            _prefix = 'oc-transceiver'
            _revision = '2018-11-25'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Transceiver, self).__init__()

                self.yang_name = "transceiver"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Transceiver.Config)), ("state", ("state", Components.Component.Transceiver.State)), ("physical-channels", ("physical_channels", Components.Component.Transceiver.PhysicalChannels))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Transceiver.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Transceiver.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.physical_channels = Components.Component.Transceiver.PhysicalChannels()
                self.physical_channels.parent = self
                self._children_name_map["physical_channels"] = "physical-channels"
                self._segment_path = lambda: "openconfig-platform-transceiver:transceiver"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Transceiver, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for client port transceivers
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\: bool
                
                .. attribute:: form_factor_preconf
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not pluggable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:  :py:class:`TRANSCEIVERFORMFACTORTYPE <ydk.models.openconfig.openconfig_transport_types.TRANSCEIVERFORMFACTORTYPE>`
                
                .. attribute:: ethernet_pmd_preconf
                
                	The Ethernet PMD is a property of the optical transceiver used on the port, indicating the type of physical connection. It is included in configuration data to allow pre\-configuring a port/transceiver with the expected PMD.  The actual PMD is indicated by the ethernet\-pmd state leaf
                	**type**\:  :py:class:`ETHERNETPMDTYPE <ydk.models.openconfig.openconfig_transport_types.ETHERNETPMDTYPE>`
                
                .. attribute:: fec_mode
                
                	The FEC mode indicates the mode of operation for the transceiver's FEC. This defines typical operational modes and does not aim to specify more granular FEC capabilities
                	**type**\:  :py:class:`FECMODETYPE <ydk.models.openconfig.openconfig_platform_types.FECMODETYPE>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2018-11-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Transceiver.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "transceiver"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('form_factor_preconf', (YLeaf(YType.identityref, 'form-factor-preconf'), [('ydk.models.openconfig.openconfig_transport_types', 'TRANSCEIVERFORMFACTORTYPE')])),
                        ('ethernet_pmd_preconf', (YLeaf(YType.identityref, 'ethernet-pmd-preconf'), [('ydk.models.openconfig.openconfig_transport_types', 'ETHERNETPMDTYPE')])),
                        ('fec_mode', (YLeaf(YType.identityref, 'fec-mode'), [('ydk.models.openconfig.openconfig_platform_types', 'FECMODETYPE')])),
                    ])
                    self.enabled = None
                    self.form_factor_preconf = None
                    self.ethernet_pmd_preconf = None
                    self.fec_mode = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Transceiver.Config, ['enabled', 'form_factor_preconf', 'ethernet_pmd_preconf', 'fec_mode'], name, value)



            class State(_Entity_):
                """
                Operational state data for client port transceivers
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: form_factor_preconf
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not pluggable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:  :py:class:`TRANSCEIVERFORMFACTORTYPE <ydk.models.openconfig.openconfig_transport_types.TRANSCEIVERFORMFACTORTYPE>`
                
                	**config**\: False
                
                .. attribute:: ethernet_pmd_preconf
                
                	The Ethernet PMD is a property of the optical transceiver used on the port, indicating the type of physical connection. It is included in configuration data to allow pre\-configuring a port/transceiver with the expected PMD.  The actual PMD is indicated by the ethernet\-pmd state leaf
                	**type**\:  :py:class:`ETHERNETPMDTYPE <ydk.models.openconfig.openconfig_transport_types.ETHERNETPMDTYPE>`
                
                	**config**\: False
                
                .. attribute:: fec_mode
                
                	The FEC mode indicates the mode of operation for the transceiver's FEC. This defines typical operational modes and does not aim to specify more granular FEC capabilities
                	**type**\:  :py:class:`FECMODETYPE <ydk.models.openconfig.openconfig_platform_types.FECMODETYPE>`
                
                	**config**\: False
                
                .. attribute:: present
                
                	Indicates whether a transceiver is present in the specified client port
                	**type**\:  :py:class:`Present <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.Present>`
                
                	**config**\: False
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not pluggable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example)
                	**type**\:  :py:class:`TRANSCEIVERFORMFACTORTYPE <ydk.models.openconfig.openconfig_transport_types.TRANSCEIVERFORMFACTORTYPE>`
                
                	**config**\: False
                
                .. attribute:: connector_type
                
                	Connector type used on this port
                	**type**\:  :py:class:`FIBERCONNECTORTYPE <ydk.models.openconfig.openconfig_transport_types.FIBERCONNECTORTYPE>`
                
                	**config**\: False
                
                .. attribute:: vendor
                
                	Full name of transceiver vendor. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                	**type**\: str
                
                	**length:** 1..16
                
                	**config**\: False
                
                .. attribute:: vendor_part
                
                	Transceiver vendor's part number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part number is undefined, all 16 octets = 0h
                	**type**\: str
                
                	**length:** 1..16
                
                	**config**\: False
                
                .. attribute:: vendor_rev
                
                	Transceiver vendor's revision number. 2\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                	**type**\: str
                
                	**length:** 1..2
                
                	**config**\: False
                
                .. attribute:: ethernet_pmd
                
                	Ethernet PMD (physical medium dependent sublayer) that the transceiver supports. The SFF/QSFP MSAs have registers for this and CFP MSA has similar
                	**type**\:  :py:class:`ETHERNETPMDTYPE <ydk.models.openconfig.openconfig_transport_types.ETHERNETPMDTYPE>`
                
                	**config**\: False
                
                .. attribute:: sonet_sdh_compliance_code
                
                	SONET/SDH application code supported by the port
                	**type**\:  :py:class:`SONETAPPLICATIONCODE <ydk.models.openconfig.openconfig_transport_types.SONETAPPLICATIONCODE>`
                
                	**config**\: False
                
                .. attribute:: otn_compliance_code
                
                	OTN application code supported by the port
                	**type**\:  :py:class:`OTNAPPLICATIONCODE <ydk.models.openconfig.openconfig_transport_types.OTNAPPLICATIONCODE>`
                
                	**config**\: False
                
                .. attribute:: serial_no
                
                	Transceiver serial number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part serial number is undefined, all 16 octets = 0h
                	**type**\: str
                
                	**length:** 1..16
                
                	**config**\: False
                
                .. attribute:: date_code
                
                	Representation of the transceiver date code, typically stored as YYMMDD.  The time portion of the value is undefined and not intended to be read
                	**type**\: str
                
                	**pattern:** ^[0\-9]{4}\\\-[0\-9]{2}\\\-[0\-9]{2}T[0\-9]{2}\:[0\-9]{2}\:[0\-9]{2}(\\.[0\-9]+)?Z[+\-][0\-9]{2}\:[0\-9]{2}$
                
                	**config**\: False
                
                .. attribute:: fault_condition
                
                	Indicates if a fault condition exists in the transceiver
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: fec_status
                
                	Operational status of FEC
                	**type**\:  :py:class:`FECSTATUSTYPE <ydk.models.openconfig.openconfig_platform_types.FECSTATUSTYPE>`
                
                	**config**\: False
                
                .. attribute:: fec_uncorrectable_blocks
                
                	The number of blocks that were uncorrectable by the FEC
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: fec_uncorrectable_words
                
                	The number of words that were uncorrectable by the FEC
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: fec_corrected_bytes
                
                	The number of bytes that were corrected by the FEC
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: fec_corrected_bits
                
                	The number of bits that were corrected by the FEC
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pre_fec_ber
                
                	Bit error rate before forward error correction \-\- computed value with 18 decimal precision. Note that decimal64 supports values as small as i x 10^\-18 where i is an integer. Values smaller than this should be reported as 0 to inidicate error free or near error free performance. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`PreFecBer <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.PreFecBer>`
                
                	**config**\: False
                
                .. attribute:: post_fec_ber
                
                	Bit error rate after forward error correction \-\- computed value with 18 decimal precision. Note that decimal64 supports values as small as i x 10^\-18 where i is an integer. Values smaller than this should be reported as 0 to inidicate error free or near error free performance. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`PostFecBer <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.PostFecBer>`
                
                	**config**\: False
                
                .. attribute:: output_power
                
                	The output optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels, or an aggregate of multiple physical channels (i.e., for the overall transceiver). For an aggregate, this may be a measurement from a photodetector or a a calculation performed on the device by summing up all of the related individual physical channels. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.OutputPower>`
                
                	**config**\: False
                
                .. attribute:: input_power
                
                	The input optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels, or an aggregate of multiple physical channels (i.e., for the overall transceiver). For an aggregate, this may be a measurement from a photodetector or a a calculation performed on the device by summing up all of the related individual physical channels. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.InputPower>`
                
                	**config**\: False
                
                .. attribute:: laser_bias_current
                
                	The current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.LaserBiasCurrent>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2018-11-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Transceiver.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "transceiver"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pre-fec-ber", ("pre_fec_ber", Components.Component.Transceiver.State.PreFecBer)), ("post-fec-ber", ("post_fec_ber", Components.Component.Transceiver.State.PostFecBer)), ("output-power", ("output_power", Components.Component.Transceiver.State.OutputPower)), ("input-power", ("input_power", Components.Component.Transceiver.State.InputPower)), ("laser-bias-current", ("laser_bias_current", Components.Component.Transceiver.State.LaserBiasCurrent))])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('form_factor_preconf', (YLeaf(YType.identityref, 'form-factor-preconf'), [('ydk.models.openconfig.openconfig_transport_types', 'TRANSCEIVERFORMFACTORTYPE')])),
                        ('ethernet_pmd_preconf', (YLeaf(YType.identityref, 'ethernet-pmd-preconf'), [('ydk.models.openconfig.openconfig_transport_types', 'ETHERNETPMDTYPE')])),
                        ('fec_mode', (YLeaf(YType.identityref, 'fec-mode'), [('ydk.models.openconfig.openconfig_platform_types', 'FECMODETYPE')])),
                        ('present', (YLeaf(YType.enumeration, 'present'), [('ydk.models.openconfig.openconfig_platform', 'Components', 'Component.Transceiver.State.Present')])),
                        ('form_factor', (YLeaf(YType.identityref, 'form-factor'), [('ydk.models.openconfig.openconfig_transport_types', 'TRANSCEIVERFORMFACTORTYPE')])),
                        ('connector_type', (YLeaf(YType.identityref, 'connector-type'), [('ydk.models.openconfig.openconfig_transport_types', 'FIBERCONNECTORTYPE')])),
                        ('vendor', (YLeaf(YType.str, 'vendor'), ['str'])),
                        ('vendor_part', (YLeaf(YType.str, 'vendor-part'), ['str'])),
                        ('vendor_rev', (YLeaf(YType.str, 'vendor-rev'), ['str'])),
                        ('ethernet_pmd', (YLeaf(YType.identityref, 'ethernet-pmd'), [('ydk.models.openconfig.openconfig_transport_types', 'ETHERNETPMDTYPE')])),
                        ('sonet_sdh_compliance_code', (YLeaf(YType.identityref, 'sonet-sdh-compliance-code'), [('ydk.models.openconfig.openconfig_transport_types', 'SONETAPPLICATIONCODE')])),
                        ('otn_compliance_code', (YLeaf(YType.identityref, 'otn-compliance-code'), [('ydk.models.openconfig.openconfig_transport_types', 'OTNAPPLICATIONCODE')])),
                        ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                        ('date_code', (YLeaf(YType.str, 'date-code'), ['str'])),
                        ('fault_condition', (YLeaf(YType.boolean, 'fault-condition'), ['bool'])),
                        ('fec_status', (YLeaf(YType.identityref, 'fec-status'), [('ydk.models.openconfig.openconfig_platform_types', 'FECSTATUSTYPE')])),
                        ('fec_uncorrectable_blocks', (YLeaf(YType.uint64, 'fec-uncorrectable-blocks'), ['int'])),
                        ('fec_uncorrectable_words', (YLeaf(YType.uint64, 'fec-uncorrectable-words'), ['int'])),
                        ('fec_corrected_bytes', (YLeaf(YType.uint64, 'fec-corrected-bytes'), ['int'])),
                        ('fec_corrected_bits', (YLeaf(YType.uint64, 'fec-corrected-bits'), ['int'])),
                    ])
                    self.enabled = None
                    self.form_factor_preconf = None
                    self.ethernet_pmd_preconf = None
                    self.fec_mode = None
                    self.present = None
                    self.form_factor = None
                    self.connector_type = None
                    self.vendor = None
                    self.vendor_part = None
                    self.vendor_rev = None
                    self.ethernet_pmd = None
                    self.sonet_sdh_compliance_code = None
                    self.otn_compliance_code = None
                    self.serial_no = None
                    self.date_code = None
                    self.fault_condition = None
                    self.fec_status = None
                    self.fec_uncorrectable_blocks = None
                    self.fec_uncorrectable_words = None
                    self.fec_corrected_bytes = None
                    self.fec_corrected_bits = None

                    self.pre_fec_ber = Components.Component.Transceiver.State.PreFecBer()
                    self.pre_fec_ber.parent = self
                    self._children_name_map["pre_fec_ber"] = "pre-fec-ber"

                    self.post_fec_ber = Components.Component.Transceiver.State.PostFecBer()
                    self.post_fec_ber.parent = self
                    self._children_name_map["post_fec_ber"] = "post-fec-ber"

                    self.output_power = Components.Component.Transceiver.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"

                    self.input_power = Components.Component.Transceiver.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"

                    self.laser_bias_current = Components.Component.Transceiver.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self._children_name_map["laser_bias_current"] = "laser-bias-current"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Transceiver.State, ['enabled', 'form_factor_preconf', 'ethernet_pmd_preconf', 'fec_mode', 'present', 'form_factor', 'connector_type', 'vendor', 'vendor_part', 'vendor_rev', 'ethernet_pmd', 'sonet_sdh_compliance_code', 'otn_compliance_code', 'serial_no', 'date_code', 'fault_condition', 'fec_status', 'fec_uncorrectable_blocks', 'fec_uncorrectable_words', 'fec_corrected_bytes', 'fec_corrected_bits'], name, value)

                class Present(Enum):
                    """
                    Present (Enum Class)

                    Indicates whether a transceiver is present in

                    the specified client port.

                    .. data:: PRESENT = 0

                    	Transceiver is present on the port

                    .. data:: NOT_PRESENT = 1

                    	Transceiver is not present on the port

                    """

                    PRESENT = Enum.YLeaf(0, "PRESENT")

                    NOT_PRESENT = Enum.YLeaf(1, "NOT_PRESENT")



                class PreFecBer(_Entity_):
                    """
                    Bit error rate before forward error correction \-\- computed
                    value with 18 decimal precision. Note that decimal64
                    supports values as small as i x 10^\-18 where i is an
                    integer. Values smaller than this should be reported as 0
                    to inidicate error free or near error free performance.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2018-11-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Transceiver.State.PreFecBer, self).__init__()

                        self.yang_name = "pre-fec-ber"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "pre-fec-ber"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.State.PreFecBer, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class PostFecBer(_Entity_):
                    """
                    Bit error rate after forward error correction \-\- computed
                    value with 18 decimal precision. Note that decimal64
                    supports values as small as i x 10^\-18 where i is an
                    integer. Values smaller than this should be reported as 0
                    to inidicate error free or near error free performance.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-9.223372036854775808..9.223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: bit-errors-per-second
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2018-11-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Transceiver.State.PostFecBer, self).__init__()

                        self.yang_name = "post-fec-ber"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "post-fec-ber"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.State.PostFecBer, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class OutputPower(_Entity_):
                    """
                    The output optical power of a physical channel in units
                    of 0.01dBm, which may be associated with individual
                    physical channels, or an aggregate of multiple physical
                    channels (i.e., for the overall transceiver). For an
                    aggregate, this may be a measurement from a photodetector
                    or a a calculation performed on the device by summing up
                    all of the related individual physical channels.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2018-11-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Transceiver.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "output-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.State.OutputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class InputPower(_Entity_):
                    """
                    The input optical power of a physical channel in units
                    of 0.01dBm, which may be associated with individual
                    physical channels, or an aggregate of multiple physical
                    channels (i.e., for the overall transceiver). For an
                    aggregate, this may be a measurement from a photodetector
                    or a a calculation performed on the device by summing up
                    all of the related individual physical channels.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2018-11-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Transceiver.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "input-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.State.InputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class LaserBiasCurrent(_Entity_):
                    """
                    The current applied by the system to the transmit laser to
                    achieve the output power. The current is expressed in mA
                    with up to two decimal precision. Values include the
                    instantaneous, average, minimum, and maximum statistics.
                    If avg/min/max statistics are not supported, the target is
                    expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2018-11-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Transceiver.State.LaserBiasCurrent, self).__init__()

                        self.yang_name = "laser-bias-current"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "laser-bias-current"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)




            class PhysicalChannels(_Entity_):
                """
                Enclosing container for client channels
                
                .. attribute:: channel
                
                	List of client channels, keyed by index within a physical client port.  A physical port with a single channel would have a single zero\-indexed element
                	**type**\: list of  		 :py:class:`Channel <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2018-11-25'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Transceiver.PhysicalChannels, self).__init__()

                    self.yang_name = "physical-channels"
                    self.yang_parent_name = "transceiver"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("channel", ("channel", Components.Component.Transceiver.PhysicalChannels.Channel))])
                    self._leafs = OrderedDict()

                    self.channel = YList(self)
                    self._segment_path = lambda: "physical-channels"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Transceiver.PhysicalChannels, [], name, value)


                class Channel(_Entity_):
                    """
                    List of client channels, keyed by index within a physical
                    client port.  A physical port with a single channel would
                    have a single zero\-indexed element
                    
                    .. attribute:: index  (key)
                    
                    	Reference to the index number of the channel
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for physical channels
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for channels
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2018-11-25'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.Transceiver.PhysicalChannels.Channel, self).__init__()

                        self.yang_name = "channel"
                        self.yang_parent_name = "physical-channels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([("config", ("config", Components.Component.Transceiver.PhysicalChannels.Channel.Config)), ("state", ("state", Components.Component.Transceiver.PhysicalChannels.Channel.State))])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.str, 'index'), ['int'])),
                        ])
                        self.index = None

                        self.config = Components.Component.Transceiver.PhysicalChannels.Channel.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Components.Component.Transceiver.PhysicalChannels.Channel.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "channel" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel, ['index'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for physical channels
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\: str
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\: bool
                        
                        .. attribute:: target_output_power
                        
                        	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dBm
                        
                        

                        """

                        _prefix = 'oc-transceiver'
                        _revision = '2018-11-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "channel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('tx_laser', (YLeaf(YType.boolean, 'tx-laser'), ['bool'])),
                                ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                            ])
                            self.index = None
                            self.description = None
                            self.tx_laser = None
                            self.target_output_power = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.Config, ['index', 'description', 'tx_laser', 'target_output_power'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for channels
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: target_output_power
                        
                        	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dBm
                        
                        .. attribute:: output_frequency
                        
                        	The frequency in MHz of the individual physical channel (e.g. ITU C50 \- 195.0THz and would be reported as 195,000,000 MHz in this model). This attribute is not configurable on most client ports
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_power
                        
                        	The output optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels, or an aggregate of multiple physical channels (i.e., for the overall transceiver). For an aggregate, this may be a measurement from a photodetector or a a calculation performed on the device by summing up all of the related individual physical channels. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower>`
                        
                        	**config**\: False
                        
                        .. attribute:: input_power
                        
                        	The input optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels, or an aggregate of multiple physical channels (i.e., for the overall transceiver). For an aggregate, this may be a measurement from a photodetector or a a calculation performed on the device by summing up all of the related individual physical channels. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower>`
                        
                        	**config**\: False
                        
                        .. attribute:: laser_bias_current
                        
                        	The current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-transceiver'
                        _revision = '2018-11-25'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "channel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("output-power", ("output_power", Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower)), ("input-power", ("input_power", Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower)), ("laser-bias-current", ("laser_bias_current", Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('tx_laser', (YLeaf(YType.boolean, 'tx-laser'), ['bool'])),
                                ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                                ('output_frequency', (YLeaf(YType.uint64, 'output-frequency'), ['int'])),
                            ])
                            self.index = None
                            self.description = None
                            self.tx_laser = None
                            self.target_output_power = None
                            self.output_frequency = None

                            self.output_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower()
                            self.output_power.parent = self
                            self._children_name_map["output_power"] = "output-power"

                            self.input_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower()
                            self.input_power.parent = self
                            self._children_name_map["input_power"] = "input-power"

                            self.laser_bias_current = Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent()
                            self.laser_bias_current.parent = self
                            self._children_name_map["laser_bias_current"] = "laser-bias-current"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State, ['index', 'description', 'tx_laser', 'target_output_power', 'output_frequency'], name, value)


                        class OutputPower(_Entity_):
                            """
                            The output optical power of a physical channel in units
                            of 0.01dBm, which may be associated with individual
                            physical channels, or an aggregate of multiple physical
                            channels (i.e., for the overall transceiver). For an
                            aggregate, this may be a measurement from a photodetector
                            or a a calculation performed on the device by summing up
                            all of the related individual physical channels.
                            Values include the instantaneous, average, minimum, and
                            maximum statistics. If avg/min/max statistics are not
                            supported, the target is expected to just supply the
                            instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2018-11-25'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, self).__init__()

                                self.yang_name = "output-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "output-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                        class InputPower(_Entity_):
                            """
                            The input optical power of a physical channel in units
                            of 0.01dBm, which may be associated with individual
                            physical channels, or an aggregate of multiple physical
                            channels (i.e., for the overall transceiver). For an
                            aggregate, this may be a measurement from a photodetector
                            or a a calculation performed on the device by summing up
                            all of the related individual physical channels.
                            Values include the instantaneous, average, minimum, and
                            maximum statistics. If avg/min/max statistics are not
                            supported, the target is expected to just supply the
                            instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2018-11-25'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, self).__init__()

                                self.yang_name = "input-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "input-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                        class LaserBiasCurrent(_Entity_):
                            """
                            The current applied by the system to the transmit laser to
                            achieve the output power. The current is expressed in mA
                            with up to two decimal precision. Values include the
                            instantaneous, average, minimum, and maximum statistics.
                            If avg/min/max statistics are not supported, the target is
                            expected to just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: mA
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: mA
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: mA
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: mA
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2018-11-25'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, self).__init__()

                                self.yang_name = "laser-bias-current"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "laser-bias-current"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)







        class OpticalChannel(_Entity_):
            """
            Enclosing container for the list of optical channels
            
            .. attribute:: config
            
            	Configuration data for optical channels
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.Config>`
            
            .. attribute:: state
            
            	Operational state data for optical channels
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2018-11-21'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.OpticalChannel, self).__init__()

                self.yang_name = "optical-channel"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.OpticalChannel.Config)), ("state", ("state", Components.Component.OpticalChannel.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.OpticalChannel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.OpticalChannel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "openconfig-terminal-device:optical-channel"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.OpticalChannel, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for optical channels
                
                .. attribute:: frequency
                
                	Frequency of the optical channel, expressed in MHz
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: target_output_power
                
                	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel.  The specified operational mode must exist in the list of supported operational modes supplied by the device
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel.  The target port should be a component in the physical inventory data model
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.OpticalChannel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "optical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('frequency', (YLeaf(YType.uint64, 'frequency'), ['int'])),
                        ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                        ('operational_mode', (YLeaf(YType.uint16, 'operational-mode'), ['int'])),
                        ('line_port', (YLeaf(YType.str, 'line-port'), ['str'])),
                    ])
                    self.frequency = None
                    self.target_output_power = None
                    self.operational_mode = None
                    self.line_port = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalChannel.Config, ['frequency', 'target_output_power', 'operational_mode', 'line_port'], name, value)



            class State(_Entity_):
                """
                Operational state data for optical channels
                
                .. attribute:: frequency
                
                	Frequency of the optical channel, expressed in MHz
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: target_output_power
                
                	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dBm
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel.  The specified operational mode must exist in the list of supported operational modes supplied by the device
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel.  The target port should be a component in the physical inventory data model
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                	**config**\: False
                
                .. attribute:: group_id
                
                	If the device places constraints on which optical channels must be managed together (e.g., transmitted on the same line port), it can indicate that by setting the group\-id to the same value across related optical channels
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: output_power
                
                	The output optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels, or an aggregate of multiple physical channels (i.e., for the overall transceiver). For an aggregate, this may be a measurement from a photodetector or a a calculation performed on the device by summing up all of the related individual physical channels. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.OutputPower>`
                
                	**config**\: False
                
                .. attribute:: input_power
                
                	The input optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels, or an aggregate of multiple physical channels (i.e., for the overall transceiver). For an aggregate, this may be a measurement from a photodetector or a a calculation performed on the device by summing up all of the related individual physical channels. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.InputPower>`
                
                	**config**\: False
                
                .. attribute:: laser_bias_current
                
                	The current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.LaserBiasCurrent>`
                
                	**config**\: False
                
                .. attribute:: chromatic_dispersion
                
                	Chromatic Dispersion of an optical channel in picoseconds / nanometer (ps/nm) as reported by receiver with two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`ChromaticDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.ChromaticDispersion>`
                
                	**config**\: False
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion of an optical channel in picosends (ps) as reported by receiver with two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`PolarizationModeDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.PolarizationModeDispersion>`
                
                	**config**\: False
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion of an optical channel in picoseconds squared (ps^2) as reported by receiver with two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`SecondOrderPolarizationModeDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion>`
                
                	**config**\: False
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss of an optical channel in dB as reported by receiver with two decimal precision. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`PolarizationDependentLoss <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.PolarizationDependentLoss>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.OpticalChannel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "optical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("output-power", ("output_power", Components.Component.OpticalChannel.State.OutputPower)), ("input-power", ("input_power", Components.Component.OpticalChannel.State.InputPower)), ("laser-bias-current", ("laser_bias_current", Components.Component.OpticalChannel.State.LaserBiasCurrent)), ("chromatic-dispersion", ("chromatic_dispersion", Components.Component.OpticalChannel.State.ChromaticDispersion)), ("polarization-mode-dispersion", ("polarization_mode_dispersion", Components.Component.OpticalChannel.State.PolarizationModeDispersion)), ("second-order-polarization-mode-dispersion", ("second_order_polarization_mode_dispersion", Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion)), ("polarization-dependent-loss", ("polarization_dependent_loss", Components.Component.OpticalChannel.State.PolarizationDependentLoss))])
                    self._leafs = OrderedDict([
                        ('frequency', (YLeaf(YType.uint64, 'frequency'), ['int'])),
                        ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                        ('operational_mode', (YLeaf(YType.uint16, 'operational-mode'), ['int'])),
                        ('line_port', (YLeaf(YType.str, 'line-port'), ['str'])),
                        ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ])
                    self.frequency = None
                    self.target_output_power = None
                    self.operational_mode = None
                    self.line_port = None
                    self.group_id = None

                    self.output_power = Components.Component.OpticalChannel.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"

                    self.input_power = Components.Component.OpticalChannel.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"

                    self.laser_bias_current = Components.Component.OpticalChannel.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self._children_name_map["laser_bias_current"] = "laser-bias-current"

                    self.chromatic_dispersion = Components.Component.OpticalChannel.State.ChromaticDispersion()
                    self.chromatic_dispersion.parent = self
                    self._children_name_map["chromatic_dispersion"] = "chromatic-dispersion"

                    self.polarization_mode_dispersion = Components.Component.OpticalChannel.State.PolarizationModeDispersion()
                    self.polarization_mode_dispersion.parent = self
                    self._children_name_map["polarization_mode_dispersion"] = "polarization-mode-dispersion"

                    self.second_order_polarization_mode_dispersion = Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion()
                    self.second_order_polarization_mode_dispersion.parent = self
                    self._children_name_map["second_order_polarization_mode_dispersion"] = "second-order-polarization-mode-dispersion"

                    self.polarization_dependent_loss = Components.Component.OpticalChannel.State.PolarizationDependentLoss()
                    self.polarization_dependent_loss.parent = self
                    self._children_name_map["polarization_dependent_loss"] = "polarization-dependent-loss"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalChannel.State, ['frequency', 'target_output_power', 'operational_mode', 'line_port', 'group_id'], name, value)


                class OutputPower(_Entity_):
                    """
                    The output optical power of a physical channel in units
                    of 0.01dBm, which may be associated with individual
                    physical channels, or an aggregate of multiple physical
                    channels (i.e., for the overall transceiver). For an
                    aggregate, this may be a measurement from a photodetector
                    or a a calculation performed on the device by summing up
                    all of the related individual physical channels.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "output-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.OutputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class InputPower(_Entity_):
                    """
                    The input optical power of a physical channel in units
                    of 0.01dBm, which may be associated with individual
                    physical channels, or an aggregate of multiple physical
                    channels (i.e., for the overall transceiver). For an
                    aggregate, this may be a measurement from a photodetector
                    or a a calculation performed on the device by summing up
                    all of the related individual physical channels.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "input-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.InputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class LaserBiasCurrent(_Entity_):
                    """
                    The current applied by the system to the transmit laser to
                    achieve the output power. The current is expressed in mA
                    with up to two decimal precision. Values include the
                    instantaneous, average, minimum, and maximum statistics.
                    If avg/min/max statistics are not supported, the target is
                    expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: mA
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.LaserBiasCurrent, self).__init__()

                        self.yang_name = "laser-bias-current"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "laser-bias-current"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class ChromaticDispersion(_Entity_):
                    """
                    Chromatic Dispersion of an optical channel in
                    picoseconds / nanometer (ps/nm) as reported by receiver
                    with two decimal precision. Values include the instantaneous,
                    average, minimum, and maximum statistics. If avg/min/max
                    statistics are not supported, the target is expected to just
                    supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps-nm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps-nm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps-nm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps-nm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.ChromaticDispersion, self).__init__()

                        self.yang_name = "chromatic-dispersion"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "chromatic-dispersion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.ChromaticDispersion, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class PolarizationModeDispersion(_Entity_):
                    """
                    Polarization Mode Dispersion of an optical channel
                    in picosends (ps) as reported by receiver with two decimal
                    precision. Values include the instantaneous, average,
                    minimum, and maximum statistics. If avg/min/max statistics
                    are not supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.PolarizationModeDispersion, self).__init__()

                        self.yang_name = "polarization-mode-dispersion"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "polarization-mode-dispersion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.PolarizationModeDispersion, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class SecondOrderPolarizationModeDispersion(_Entity_):
                    """
                    Second Order Polarization Mode Dispersion of an optical
                    channel in picoseconds squared (ps^2) as reported by
                    receiver with two decimal precision. Values include the
                    instantaneous, average, minimum, and maximum statistics.
                    If avg/min/max statistics are not supported, the target
                    is expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps^2
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps^2
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps^2
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: ps^2
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, self).__init__()

                        self.yang_name = "second-order-polarization-mode-dispersion"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "second-order-polarization-mode-dispersion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class PolarizationDependentLoss(_Entity_):
                    """
                    Polarization Dependent Loss of an optical channel
                    in dB as reported by receiver with two decimal precision.
                    Values include the instantaneous, average, minimum, and
                    maximum statistics. If avg/min/max statistics are not
                    supported, the target is expected to just supply the
                    instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dB
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dB
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dB
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dB
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalChannel.State.PolarizationDependentLoss, self).__init__()

                        self.yang_name = "polarization-dependent-loss"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "polarization-dependent-loss"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.PolarizationDependentLoss, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





        class OpticalPort(_Entity_):
            """
            Top\-level container 
            
            .. attribute:: config
            
            	Operational config data for optical line ports
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.Config>`
            
            .. attribute:: state
            
            	Operational state data for optical line ports
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-line-com'
            _revision = '2018-07-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.OpticalPort, self).__init__()

                self.yang_name = "optical-port"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.OpticalPort.Config)), ("state", ("state", Components.Component.OpticalPort.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.OpticalPort.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.OpticalPort.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "openconfig-transport-line-common:optical-port"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.OpticalPort, [], name, value)


            class Config(_Entity_):
                """
                Operational config data for optical line ports
                
                .. attribute:: admin_state
                
                	Sets the admin state of the optical\-port
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                

                """

                _prefix = 'oc-line-com'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.OpticalPort.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "optical-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.openconfig.openconfig_transport_types', 'AdminStateType', '')])),
                    ])
                    self.admin_state = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalPort.Config, ['admin_state'], name, value)



            class State(_Entity_):
                """
                Operational state data for optical line ports
                
                .. attribute:: admin_state
                
                	Sets the admin state of the optical\-port
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                	**config**\: False
                
                .. attribute:: optical_port_type
                
                	Indicates the type of transport line port.  This is an informational field that should be made available by the device (e.g., in the openconfig\-platform model)
                	**type**\:  :py:class:`OPTICALLINEPORTTYPE <ydk.models.openconfig.openconfig_transport_line_common.OPTICALLINEPORTTYPE>`
                
                	**config**\: False
                
                .. attribute:: input_power
                
                	The total input optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.State.InputPower>`
                
                	**config**\: False
                
                .. attribute:: output_power
                
                	The total output optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.State.OutputPower>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-line-com'
                _revision = '2018-07-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.OpticalPort.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "optical-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("input-power", ("input_power", Components.Component.OpticalPort.State.InputPower)), ("output-power", ("output_power", Components.Component.OpticalPort.State.OutputPower))])
                    self._leafs = OrderedDict([
                        ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.openconfig.openconfig_transport_types', 'AdminStateType', '')])),
                        ('optical_port_type', (YLeaf(YType.identityref, 'optical-port-type'), [('ydk.models.openconfig.openconfig_transport_line_common', 'OPTICALLINEPORTTYPE')])),
                    ])
                    self.admin_state = None
                    self.optical_port_type = None

                    self.input_power = Components.Component.OpticalPort.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"

                    self.output_power = Components.Component.OpticalPort.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalPort.State, ['admin_state', 'optical_port_type'], name, value)


                class InputPower(_Entity_):
                    """
                    The total input optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-com'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalPort.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "input-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalPort.State.InputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)



                class OutputPower(_Entity_):
                    """
                    The total output optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the time interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: interval
                    
                    	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: min_time
                    
                    	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: max_time
                    
                    	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-com'
                    _revision = '2018-07-17'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Components.Component.OpticalPort.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                            ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                            ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                            ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self.interval = None
                        self.min_time = None
                        self.max_time = None
                        self._segment_path = lambda: "output-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalPort.State.OutputPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





        class Linecard(_Entity_):
            """
            Top\-level container for linecard data
            
            .. attribute:: config
            
            	Configuration data for linecards
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Linecard.Config>`
            
            .. attribute:: state
            
            	Operational state data for linecards
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Linecard.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-linecard'
            _revision = '2017-08-03'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Components.Component.Linecard, self).__init__()

                self.yang_name = "linecard"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Linecard.Config)), ("state", ("state", Components.Component.Linecard.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Linecard.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Linecard.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "openconfig-platform-linecard:linecard"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Linecard, [], name, value)


            class Config(_Entity_):
                """
                Configuration data for linecards
                
                .. attribute:: power_admin_state
                
                	Enable or disable power to the linecard
                	**type**\:  :py:class:`ComponentPowerType <ydk.models.openconfig.openconfig_platform_types.ComponentPowerType>`
                
                	**default value**\: POWER_ENABLED
                
                

                """

                _prefix = 'oc-linecard'
                _revision = '2017-08-03'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Linecard.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "linecard"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('power_admin_state', (YLeaf(YType.enumeration, 'power-admin-state'), [('ydk.models.openconfig.openconfig_platform_types', 'ComponentPowerType', '')])),
                    ])
                    self.power_admin_state = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Linecard.Config, ['power_admin_state'], name, value)



            class State(_Entity_):
                """
                Operational state data for linecards
                
                .. attribute:: power_admin_state
                
                	Enable or disable power to the linecard
                	**type**\:  :py:class:`ComponentPowerType <ydk.models.openconfig.openconfig_platform_types.ComponentPowerType>`
                
                	**config**\: False
                
                	**default value**\: POWER_ENABLED
                
                .. attribute:: slot_id
                
                	Identifier for the slot or chassis position in which the linecard is installed
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-linecard'
                _revision = '2017-08-03'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Components.Component.Linecard.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "linecard"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('power_admin_state', (YLeaf(YType.enumeration, 'power-admin-state'), [('ydk.models.openconfig.openconfig_platform_types', 'ComponentPowerType', '')])),
                        ('slot_id', (YLeaf(YType.str, 'slot-id'), ['str'])),
                    ])
                    self.power_admin_state = None
                    self.slot_id = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Linecard.State, ['power_admin_state', 'slot_id'], name, value)




    def clone_ptr(self):
        self._top_entity = Components()
        return self._top_entity



