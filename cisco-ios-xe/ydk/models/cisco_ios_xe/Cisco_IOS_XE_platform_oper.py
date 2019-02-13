""" Cisco_IOS_XE_platform_oper 

This module contains a collection of YANG definitions
for monitoring of platform components.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PlatformCompType(Enum):
    """
    PlatformCompType (Enum Class)

    Component Type

    .. data:: comp_chassis = 0

    .. data:: comp_backplane = 1

    .. data:: comp_power_supply = 2

    .. data:: comp_fan = 3

    .. data:: comp_sensor = 4

    .. data:: comp_module = 5

    .. data:: comp_linecard = 6

    .. data:: comp_port = 7

    .. data:: comp_cpu = 8

    .. data:: comp_operating_system = 9

    .. data:: comp_optical_channel = 10

    .. data:: comp_container = 11

    """

    comp_chassis = Enum.YLeaf(0, "comp-chassis")

    comp_backplane = Enum.YLeaf(1, "comp-backplane")

    comp_power_supply = Enum.YLeaf(2, "comp-power-supply")

    comp_fan = Enum.YLeaf(3, "comp-fan")

    comp_sensor = Enum.YLeaf(4, "comp-sensor")

    comp_module = Enum.YLeaf(5, "comp-module")

    comp_linecard = Enum.YLeaf(6, "comp-linecard")

    comp_port = Enum.YLeaf(7, "comp-port")

    comp_cpu = Enum.YLeaf(8, "comp-cpu")

    comp_operating_system = Enum.YLeaf(9, "comp-operating-system")

    comp_optical_channel = Enum.YLeaf(10, "comp-optical-channel")

    comp_container = Enum.YLeaf(11, "comp-container")


class PlatformPropValueType(Enum):
    """
    PlatformPropValueType (Enum Class)

    Property value type

    .. data:: property_string = 0

    .. data:: property_boolean = 1

    .. data:: property_int64 = 2

    .. data:: property_uint64 = 3

    .. data:: property_decimal64 = 4

    """

    property_string = Enum.YLeaf(0, "property-string")

    property_boolean = Enum.YLeaf(1, "property-boolean")

    property_int64 = Enum.YLeaf(2, "property-int64")

    property_uint64 = Enum.YLeaf(3, "property-uint64")

    property_decimal64 = Enum.YLeaf(4, "property-decimal64")



class Components(Entity):
    """
    Enclosing container for the components in the system
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of  		 :py:class:`Component <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component>`
    
    	**config**\: False
    
    

    """

    _prefix = 'platform-ios-xe-oper'
    _revision = '2017-10-11'

    def __init__(self):
        super(Components, self).__init__()
        self._top_entity = None

        self.yang_name = "components"
        self.yang_parent_name = "Cisco-IOS-XE-platform-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("component", ("component", Components.Component))])
        self._leafs = OrderedDict()

        self.component = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-platform-oper:components"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Components, [], name, value)


    class Component(Entity):
        """
        List of components, keyed by component name
        
        .. attribute:: cname  (key)
        
        	References component name
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: state
        
        	Operational state data for each component
        	**type**\:  :py:class:`State <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.State>`
        
        	**config**\: False
        
        .. attribute:: platform_properties
        
        	Platform component properties
        	**type**\:  :py:class:`PlatformProperties <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformProperties>`
        
        	**config**\: False
        
        .. attribute:: platform_subcomponents
        
        	Platform subcomponents
        	**type**\:  :py:class:`PlatformSubcomponents <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformSubcomponents>`
        
        	**config**\: False
        
        

        """

        _prefix = 'platform-ios-xe-oper'
        _revision = '2017-10-11'

        def __init__(self):
            super(Components.Component, self).__init__()

            self.yang_name = "component"
            self.yang_parent_name = "components"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['cname']
            self._child_classes = OrderedDict([("state", ("state", Components.Component.State)), ("platform-properties", ("platform_properties", Components.Component.PlatformProperties)), ("platform-subcomponents", ("platform_subcomponents", Components.Component.PlatformSubcomponents))])
            self._leafs = OrderedDict([
                ('cname', (YLeaf(YType.str, 'cname'), ['str'])),
            ])
            self.cname = None

            self.state = Components.Component.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.platform_properties = Components.Component.PlatformProperties()
            self.platform_properties.parent = self
            self._children_name_map["platform_properties"] = "platform-properties"

            self.platform_subcomponents = Components.Component.PlatformSubcomponents()
            self.platform_subcomponents.parent = self
            self._children_name_map["platform_subcomponents"] = "platform-subcomponents"
            self._segment_path = lambda: "component" + "[cname='" + str(self.cname) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-platform-oper:components/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Components.Component, ['cname'], name, value)


        class State(Entity):
            """
            Operational state data for each component
            
            .. attribute:: type
            
            	Type of component as identified by the system
            	**type**\:  :py:class:`PlatformCompType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.PlatformCompType>`
            
            	**config**\: False
            
            .. attribute:: id
            
            	Unique identifier assigned to the component by the system
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
            
            .. attribute:: version
            
            	System\-defined version string for a hardware, firmware, or software component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: serial_no
            
            	System\-assigned serial number of the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: part_no
            
            	System\-assigned part number for the component.  This should be present in particular if the component is also an FRU (field replacable unit)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: temp
            
            	Temperature in degrees Celsius of the component. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
            	**type**\:  :py:class:`Temp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.State.Temp>`
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-ios-xe-oper'
            _revision = '2017-10-11'

            def __init__(self):
                super(Components.Component.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("temp", ("temp", Components.Component.State.Temp))])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper', 'PlatformCompType', '')])),
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('mfg_name', (YLeaf(YType.str, 'mfg-name'), ['str'])),
                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                    ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                    ('part_no', (YLeaf(YType.str, 'part-no'), ['str'])),
                ])
                self.type = None
                self.id = None
                self.description = None
                self.mfg_name = None
                self.version = None
                self.serial_no = None
                self.part_no = None

                self.temp = Components.Component.State.Temp()
                self.temp.parent = self
                self._children_name_map["temp"] = "temp"
                self._segment_path = lambda: "state"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.State, ['type', 'id', 'description', 'mfg_name', 'version', 'serial_no', 'part_no'], name, value)


            class Temp(Entity):
                """
                Temperature in degrees Celsius of the component. Values include
                the instantaneous, average, minimum, and maximum statistics. If
                avg/min/max statistics are not supported, the target is expected
                to just supply the instant value
                
                .. attribute:: temp_instant
                
                	Instantaneous temperature value of a component
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: temp_avg
                
                	Arithmetic mean value of the statistic over a sampling period
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: temp_max
                
                	High water mark value of the statistic over a sampling period
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: temp_min
                
                	Low water mark value of the statistic over a sampling period
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-ios-xe-oper'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Components.Component.State.Temp, self).__init__()

                    self.yang_name = "temp"
                    self.yang_parent_name = "state"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('temp_instant', (YLeaf(YType.str, 'temp-instant'), ['Decimal64'])),
                        ('temp_avg', (YLeaf(YType.str, 'temp-avg'), ['Decimal64'])),
                        ('temp_max', (YLeaf(YType.str, 'temp-max'), ['Decimal64'])),
                        ('temp_min', (YLeaf(YType.str, 'temp-min'), ['Decimal64'])),
                    ])
                    self.temp_instant = None
                    self.temp_avg = None
                    self.temp_max = None
                    self.temp_min = None
                    self._segment_path = lambda: "temp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.State.Temp, ['temp_instant', 'temp_avg', 'temp_max', 'temp_min'], name, value)




        class PlatformProperties(Entity):
            """
            Platform component properties
            
            .. attribute:: platform_property
            
            	List of platform component properties
            	**type**\: list of  		 :py:class:`PlatformProperty <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformProperties.PlatformProperty>`
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-ios-xe-oper'
            _revision = '2017-10-11'

            def __init__(self):
                super(Components.Component.PlatformProperties, self).__init__()

                self.yang_name = "platform-properties"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("platform-property", ("platform_property", Components.Component.PlatformProperties.PlatformProperty))])
                self._leafs = OrderedDict()

                self.platform_property = YList(self)
                self._segment_path = lambda: "platform-properties"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.PlatformProperties, [], name, value)


            class PlatformProperty(Entity):
                """
                List of platform component properties
                
                .. attribute:: name  (key)
                
                	Property name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: value
                
                	Property value
                	**type**\:  :py:class:`Value <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformProperties.PlatformProperty.Value>`
                
                	**config**\: False
                
                .. attribute:: configurable
                
                	Indication of whether the property is user\-configurable
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-ios-xe-oper'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Components.Component.PlatformProperties.PlatformProperty, self).__init__()

                    self.yang_name = "platform-property"
                    self.yang_parent_name = "platform-properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("value", ("value", Components.Component.PlatformProperties.PlatformProperty.Value))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('configurable', (YLeaf(YType.boolean, 'configurable'), ['bool'])),
                    ])
                    self.name = None
                    self.configurable = None

                    self.value = Components.Component.PlatformProperties.PlatformProperty.Value()
                    self.value.parent = self
                    self._children_name_map["value"] = "value"
                    self._segment_path = lambda: "platform-property" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.PlatformProperties.PlatformProperty, ['name', 'configurable'], name, value)


                class Value(Entity):
                    """
                    Property value
                    
                    .. attribute:: string
                    
                    	String property value
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: boolean
                    
                    	Boolean property value
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: intsixfour
                    
                    	Integer64 property value
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    .. attribute:: uintsixfour
                    
                    	Unsigned integer64 property value
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: decimal
                    
                    	Decimal64 property value
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'platform-ios-xe-oper'
                    _revision = '2017-10-11'

                    def __init__(self):
                        super(Components.Component.PlatformProperties.PlatformProperty.Value, self).__init__()

                        self.yang_name = "value"
                        self.yang_parent_name = "platform-property"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ('boolean', (YLeaf(YType.boolean, 'boolean'), ['bool'])),
                            ('intsixfour', (YLeaf(YType.int64, 'intsixfour'), ['int'])),
                            ('uintsixfour', (YLeaf(YType.uint64, 'uintsixfour'), ['int'])),
                            ('decimal', (YLeaf(YType.str, 'decimal'), ['Decimal64'])),
                        ])
                        self.string = None
                        self.boolean = None
                        self.intsixfour = None
                        self.uintsixfour = None
                        self.decimal = None
                        self._segment_path = lambda: "value"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.PlatformProperties.PlatformProperty.Value, ['string', 'boolean', 'intsixfour', 'uintsixfour', 'decimal'], name, value)





        class PlatformSubcomponents(Entity):
            """
            Platform subcomponents
            
            .. attribute:: platform_subcomponent
            
            	List of platform subcomponents
            	**type**\: list of  		 :py:class:`PlatformSubcomponent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformSubcomponents.PlatformSubcomponent>`
            
            	**config**\: False
            
            

            """

            _prefix = 'platform-ios-xe-oper'
            _revision = '2017-10-11'

            def __init__(self):
                super(Components.Component.PlatformSubcomponents, self).__init__()

                self.yang_name = "platform-subcomponents"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("platform-subcomponent", ("platform_subcomponent", Components.Component.PlatformSubcomponents.PlatformSubcomponent))])
                self._leafs = OrderedDict()

                self.platform_subcomponent = YList(self)
                self._segment_path = lambda: "platform-subcomponents"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.PlatformSubcomponents, [], name, value)


            class PlatformSubcomponent(Entity):
                """
                List of platform subcomponents
                
                .. attribute:: name  (key)
                
                	Subcomponent name
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'platform-ios-xe-oper'
                _revision = '2017-10-11'

                def __init__(self):
                    super(Components.Component.PlatformSubcomponents.PlatformSubcomponent, self).__init__()

                    self.yang_name = "platform-subcomponent"
                    self.yang_parent_name = "platform-subcomponents"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None
                    self._segment_path = lambda: "platform-subcomponent" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.PlatformSubcomponents.PlatformSubcomponent, ['name'], name, value)




    def clone_ptr(self):
        self._top_entity = Components()
        return self._top_entity



