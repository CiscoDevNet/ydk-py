""" Cisco_IOS_XE_rpc 

NED RPC YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Switch(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Switch, self).__init__()
        self._top_entity = None

        self.yang_name = "switch"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Switch.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Switch.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:switch"


    class Input(Entity):
        """
        
        
        .. attribute:: y_switch_number
        
        	
        	**type**\: int
        
        	**range:** 1..9
        
        	**mandatory**\: True
        
        .. attribute:: priority
        
        	<1\-15>  Switch Priority
        	**type**\: int
        
        	**range:** 1..15
        
        .. attribute:: renumber
        
        	<1\-9>  New number of the Switch
        	**type**\: int
        
        	**range:** 1..9
        
        .. attribute:: statck
        
        	
        	**type**\:  :py:class:`Statck <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input.Statck>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Switch.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "switch"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("statck", ("statck", Switch.Input.Statck))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('y_switch_number', YLeaf(YType.uint8, '_switch-number')),
                ('priority', YLeaf(YType.uint8, 'priority')),
                ('renumber', YLeaf(YType.uint8, 'renumber')),
            ])
            self.y_switch_number = None
            self.priority = None
            self.renumber = None

            self.statck = Switch.Input.Statck()
            self.statck.parent = self
            self._children_name_map["statck"] = "statck"
            self._children_yang_names.add("statck")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:switch/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Switch.Input, ['y_switch_number', 'priority', 'renumber'], name, value)


        class Statck(Entity):
            """
            
            
            .. attribute:: port
            
            	<1\-2>  Stack port number to enable/disable
            	**type**\: int
            
            	**range:** 1..2
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Switch.Input.Statck, self).__init__()

                self.yang_name = "statck"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('port', YLeaf(YType.uint8, 'port')),
                ])
                self.port = None
                self._segment_path = lambda: "statck"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:switch/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Switch.Input.Statck, ['port'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Switch.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "switch"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:switch/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Switch.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Switch()
        return self._top_entity

class Default(Entity):
    """
    Set a command to its defaults
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Default, self).__init__()
        self._top_entity = None

        self.yang_name = "default"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Default.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Default.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:default"


    class Input(Entity):
        """
        
        
        .. attribute:: interface
        
        	Select an interface to configure
        	**type**\: str
        
        	**pattern:** [A\-Za\-z]([\\w/.\-]+)
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Default.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "default"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('interface', YLeaf(YType.str, 'interface')),
            ])
            self.interface = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:default/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Default.Input, ['interface'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Default.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "default"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:default/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Default.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Default()
        return self._top_entity

class Clear(Entity):
    """
    Clear
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Clear, self).__init__()
        self._top_entity = None

        self.yang_name = "clear"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Clear.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Clear.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:clear"


    class Input(Entity):
        """
        
        
        .. attribute:: interface
        
        	Select an interface to clear
        	**type**\: str
        
        	**pattern:** [A\-Za\-z]([\\w/.\-]+)
        
        .. attribute:: count
        
        	Select an interface to clear
        	**type**\: str
        
        	**pattern:** [A\-Za\-z]([\\w/.\-]+)
        
        .. attribute:: flow
        
        	Flow monitor clear commands
        	**type**\:  :py:class:`Flow <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Flow>`
        
        .. attribute:: ip
        
        	
        	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Ip>`
        
        .. attribute:: arp_cache
        
        	Clear the entire ARP cache
        	**type**\:  :py:class:`ArpCache <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.ArpCache>`
        
        	**presence node**\: True
        
        .. attribute:: aaa
        
        	Clear AAA values
        	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Aaa>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Clear.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("flow", ("flow", Clear.Input.Flow)), ("ip", ("ip", Clear.Input.Ip)), ("arp-cache", ("arp_cache", Clear.Input.ArpCache)), ("aaa", ("aaa", Clear.Input.Aaa))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('interface', YLeaf(YType.str, 'interface')),
                ('count', YLeaf(YType.str, 'count')),
            ])
            self.interface = None
            self.count = None

            self.flow = Clear.Input.Flow()
            self.flow.parent = self
            self._children_name_map["flow"] = "flow"
            self._children_yang_names.add("flow")

            self.ip = Clear.Input.Ip()
            self.ip.parent = self
            self._children_name_map["ip"] = "ip"
            self._children_yang_names.add("ip")

            self.arp_cache = None
            self._children_name_map["arp_cache"] = "arp-cache"
            self._children_yang_names.add("arp-cache")

            self.aaa = Clear.Input.Aaa()
            self.aaa.parent = self
            self._children_name_map["aaa"] = "aaa"
            self._children_yang_names.add("aaa")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Clear.Input, ['interface', 'count'], name, value)


        class Flow(Entity):
            """
            Flow monitor clear commands
            
            .. attribute:: monitor
            
            	
            	**type**\:  :py:class:`Monitor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Flow.Monitor>`
            
            .. attribute:: exporter
            
            	
            	**type**\:  :py:class:`Exporter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Flow.Exporter>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Clear.Input.Flow, self).__init__()

                self.yang_name = "flow"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("monitor", ("monitor", Clear.Input.Flow.Monitor)), ("exporter", ("exporter", Clear.Input.Flow.Exporter))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.monitor = Clear.Input.Flow.Monitor()
                self.monitor.parent = self
                self._children_name_map["monitor"] = "monitor"
                self._children_yang_names.add("monitor")

                self.exporter = Clear.Input.Flow.Exporter()
                self.exporter.parent = self
                self._children_name_map["exporter"] = "exporter"
                self._children_yang_names.add("exporter")
                self._segment_path = lambda: "flow"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/%s" % self._segment_path()


            class Monitor(Entity):
                """
                
                
                .. attribute:: name
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: force_export
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: statistics
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: cache
                
                	
                	**type**\:  :py:class:`Cache <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Flow.Monitor.Cache>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Clear.Input.Flow.Monitor, self).__init__()

                    self.yang_name = "monitor"
                    self.yang_parent_name = "flow"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("cache", ("cache", Clear.Input.Flow.Monitor.Cache))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('force_export', YLeaf(YType.empty, 'force-export')),
                        ('statistics', YLeaf(YType.empty, 'statistics')),
                    ])
                    self.name = None
                    self.force_export = None
                    self.statistics = None

                    self.cache = Clear.Input.Flow.Monitor.Cache()
                    self.cache.parent = self
                    self._children_name_map["cache"] = "cache"
                    self._children_yang_names.add("cache")
                    self._segment_path = lambda: "monitor"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/flow/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Input.Flow.Monitor, ['name', 'force_export', 'statistics'], name, value)


                class Cache(Entity):
                    """
                    
                    
                    .. attribute:: force_export
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ios-xe-rpc'
                    _revision = '2017-12-06'

                    def __init__(self):
                        super(Clear.Input.Flow.Monitor.Cache, self).__init__()

                        self.yang_name = "cache"
                        self.yang_parent_name = "monitor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('force_export', YLeaf(YType.empty, 'force-export')),
                        ])
                        self.force_export = None
                        self._segment_path = lambda: "cache"
                        self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/flow/monitor/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.Input.Flow.Monitor.Cache, ['force_export'], name, value)


            class Exporter(Entity):
                """
                
                
                .. attribute:: name
                
                	
                	**type**\: str
                
                .. attribute:: statistics
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Clear.Input.Flow.Exporter, self).__init__()

                    self.yang_name = "exporter"
                    self.yang_parent_name = "flow"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('statistics', YLeaf(YType.empty, 'statistics')),
                    ])
                    self.name = None
                    self.statistics = None
                    self._segment_path = lambda: "exporter"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/flow/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Input.Flow.Exporter, ['name', 'statistics'], name, value)


        class Ip(Entity):
            """
            
            
            .. attribute:: dhcp
            
            	Delete items from the DHCP database
            	**type**\:  :py:class:`Dhcp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Ip.Dhcp>`
            
            .. attribute:: ospf
            
            	
            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Ip.Ospf>`
            
            .. attribute:: bgp
            
            	Clear BGP connections
            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Ip.Bgp>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Clear.Input.Ip, self).__init__()

                self.yang_name = "ip"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("dhcp", ("dhcp", Clear.Input.Ip.Dhcp)), ("ospf", ("ospf", Clear.Input.Ip.Ospf)), ("bgp", ("bgp", Clear.Input.Ip.Bgp))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.dhcp = Clear.Input.Ip.Dhcp()
                self.dhcp.parent = self
                self._children_name_map["dhcp"] = "dhcp"
                self._children_yang_names.add("dhcp")

                self.ospf = Clear.Input.Ip.Ospf()
                self.ospf.parent = self
                self._children_name_map["ospf"] = "ospf"
                self._children_yang_names.add("ospf")

                self.bgp = Clear.Input.Ip.Bgp()
                self.bgp.parent = self
                self._children_name_map["bgp"] = "bgp"
                self._children_yang_names.add("bgp")
                self._segment_path = lambda: "ip"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/%s" % self._segment_path()


            class Dhcp(Entity):
                """
                Delete items from the DHCP database
                
                .. attribute:: binding
                
                	DHCP address bindings
                	**type**\:  :py:class:`Binding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Ip.Dhcp.Binding>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Clear.Input.Ip.Dhcp, self).__init__()

                    self.yang_name = "dhcp"
                    self.yang_parent_name = "ip"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("binding", ("binding", Clear.Input.Ip.Dhcp.Binding))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.binding = Clear.Input.Ip.Dhcp.Binding()
                    self.binding.parent = self
                    self._children_name_map["binding"] = "binding"
                    self._children_yang_names.add("binding")
                    self._segment_path = lambda: "dhcp"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/ip/%s" % self._segment_path()


                class Binding(Entity):
                    """
                    DHCP address bindings
                    
                    .. attribute:: vrf
                    
                    	DHCP vrf bindings
                    	**type**\: str
                    
                    .. attribute:: y_all
                    
                    	Clear all automatic bindings
                    	**type**\: str
                    
                    	**pattern:** [\*]
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ios-xe-rpc'
                    _revision = '2017-12-06'

                    def __init__(self):
                        super(Clear.Input.Ip.Dhcp.Binding, self).__init__()

                        self.yang_name = "binding"
                        self.yang_parent_name = "dhcp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf', YLeaf(YType.str, 'vrf')),
                            ('y_all', YLeaf(YType.str, '_all')),
                        ])
                        self.vrf = None
                        self.y_all = None
                        self._segment_path = lambda: "binding"
                        self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/ip/dhcp/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Clear.Input.Ip.Dhcp.Binding, ['vrf', 'y_all'], name, value)


            class Ospf(Entity):
                """
                
                
                .. attribute:: y_id
                
                	Process ID number
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Clear.Input.Ip.Ospf, self).__init__()

                    self.yang_name = "ospf"
                    self.yang_parent_name = "ip"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('y_id', YLeaf(YType.uint16, '_id')),
                        ('process', YLeaf(YType.empty, 'process')),
                    ])
                    self.y_id = None
                    self.process = None
                    self._segment_path = lambda: "ospf"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/ip/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Input.Ip.Ospf, ['y_id', 'process'], name, value)


            class Bgp(Entity):
                """
                Clear BGP connections
                
                .. attribute:: y_peer_address
                
                	BGP neighbor address to clear
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: vrf
                
                	Select a VPN Routing/Forwarding instance
                	**type**\: str
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Clear.Input.Ip.Bgp, self).__init__()

                    self.yang_name = "bgp"
                    self.yang_parent_name = "ip"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('y_peer_address', YLeaf(YType.str, '_peer-address')),
                        ('vrf', YLeaf(YType.str, 'vrf')),
                    ])
                    self.y_peer_address = None
                    self.vrf = None
                    self._segment_path = lambda: "bgp"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/ip/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Clear.Input.Ip.Bgp, ['y_peer_address', 'vrf'], name, value)


        class ArpCache(Entity):
            """
            Clear the entire ARP cache
            
            .. attribute:: vrf
            
            	Clear entries for a VPN Routing/Forwarding instance
            	**type**\: str
            
            .. attribute:: interface
            
            	Clear the entire ARP cache on the interface
            	**type**\: str
            
            	**pattern:** [A\-Za\-z]([\\w/.\-]+)
            
            .. attribute:: y_ip
            
            	IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Clear.Input.ArpCache, self).__init__()

                self.yang_name = "arp-cache"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('vrf', YLeaf(YType.str, 'vrf')),
                    ('interface', YLeaf(YType.str, 'interface')),
                    ('y_ip', YLeaf(YType.str, '_ip')),
                ])
                self.vrf = None
                self.interface = None
                self.y_ip = None
                self._segment_path = lambda: "arp-cache"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Clear.Input.ArpCache, ['vrf', 'interface', 'y_ip'], name, value)


        class Aaa(Entity):
            """
            Clear AAA values
            
            .. attribute:: local
            
            	Clear AAA local method options
            	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Aaa.Local>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Clear.Input.Aaa, self).__init__()

                self.yang_name = "aaa"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("local", ("local", Clear.Input.Aaa.Local))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.local = Clear.Input.Aaa.Local()
                self.local.parent = self
                self._children_name_map["local"] = "local"
                self._children_yang_names.add("local")
                self._segment_path = lambda: "aaa"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/%s" % self._segment_path()


            class Local(Entity):
                """
                Clear AAA local method options
                
                .. attribute:: user
                
                	Clear local AAA users
                	**type**\:  :py:class:`User <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Aaa.Local.User>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Clear.Input.Aaa.Local, self).__init__()

                    self.yang_name = "local"
                    self.yang_parent_name = "aaa"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("user", ("user", Clear.Input.Aaa.Local.User))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.user = Clear.Input.Aaa.Local.User()
                    self.user.parent = self
                    self._children_name_map["user"] = "user"
                    self._children_yang_names.add("user")
                    self._segment_path = lambda: "local"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/aaa/%s" % self._segment_path()


                class User(Entity):
                    """
                    Clear local AAA users
                    
                    .. attribute:: lockout
                    
                    	Clear locked out local AAA users
                    	**type**\:  :py:class:`Lockout <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Clear.Input.Aaa.Local.User.Lockout>`
                    
                    

                    """

                    _prefix = 'ios-xe-rpc'
                    _revision = '2017-12-06'

                    def __init__(self):
                        super(Clear.Input.Aaa.Local.User, self).__init__()

                        self.yang_name = "user"
                        self.yang_parent_name = "local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("lockout", ("lockout", Clear.Input.Aaa.Local.User.Lockout))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.lockout = Clear.Input.Aaa.Local.User.Lockout()
                        self.lockout.parent = self
                        self._children_name_map["lockout"] = "lockout"
                        self._children_yang_names.add("lockout")
                        self._segment_path = lambda: "user"
                        self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/aaa/local/%s" % self._segment_path()


                    class Lockout(Entity):
                        """
                        Clear locked out local AAA users
                        
                        .. attribute:: username
                        
                        	Username of the locked\-user
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ios-xe-rpc'
                        _revision = '2017-12-06'

                        def __init__(self):
                            super(Clear.Input.Aaa.Local.User.Lockout, self).__init__()

                            self.yang_name = "lockout"
                            self.yang_parent_name = "user"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('username', YLeaf(YType.str, 'username')),
                            ])
                            self.username = None
                            self._segment_path = lambda: "lockout"
                            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/input/aaa/local/user/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Clear.Input.Aaa.Local.User.Lockout, ['username'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Clear.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:clear/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Clear.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Clear()
        return self._top_entity

class Release(Entity):
    """
    Release a resource
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Release.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Release.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Release, self).__init__()
        self._top_entity = None

        self.yang_name = "release"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Release.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Release.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:release"


    class Input(Entity):
        """
        
        
        .. attribute:: dhcp
        
        	Release a dhcp lease (an interface)
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Release.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "release"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('dhcp', YLeaf(YType.str, 'dhcp')),
            ])
            self.dhcp = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:release/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Release.Input, ['dhcp'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Release.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "release"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:release/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Release.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Release()
        return self._top_entity

class Reload(Entity):
    """
    Halt and perform a cold restart
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Reload.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Reload.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Reload, self).__init__()
        self._top_entity = None

        self.yang_name = "reload"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Reload.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Reload.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:reload"


    class Input(Entity):
        """
        
        
        .. attribute:: force
        
        	Force a restart even if there is unsaved config
        	**type**\: bool
        
        .. attribute:: reason
        
        	Reload reason
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Reload.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "reload"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('force', YLeaf(YType.boolean, 'force')),
                ('reason', YLeaf(YType.str, 'reason')),
            ])
            self.force = None
            self.reason = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:reload/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Reload.Input, ['force', 'reason'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Reload.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "reload"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:reload/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Reload.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Reload()
        return self._top_entity

class Cellular(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Cellular, self).__init__()
        self._top_entity = None

        self.yang_name = "cellular"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Cellular.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Cellular.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:cellular"


    class Input(Entity):
        """
        
        
        .. attribute:: y_if_name
        
        	
        	**type**\: str
        
        .. attribute:: lte
        
        	
        	**type**\:  :py:class:`Lte <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Input.Lte>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Cellular.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "cellular"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("lte", ("lte", Cellular.Input.Lte))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('y_if_name', YLeaf(YType.str, '_if-name')),
            ])
            self.y_if_name = None

            self.lte = Cellular.Input.Lte()
            self.lte.parent = self
            self._children_name_map["lte"] = "lte"
            self._children_yang_names.add("lte")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Cellular.Input, ['y_if_name'], name, value)


        class Lte(Entity):
            """
            
            
            .. attribute:: technology
            
            	
            	**type**\:  :py:class:`Technology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Input.Lte.Technology>`
            
            .. attribute:: profile
            
            	
            	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Input.Lte.Profile>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Cellular.Input.Lte, self).__init__()

                self.yang_name = "lte"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("technology", ("technology", Cellular.Input.Lte.Technology)), ("profile", ("profile", Cellular.Input.Lte.Profile))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.technology = Cellular.Input.Lte.Technology()
                self.technology.parent = self
                self._children_name_map["technology"] = "technology"
                self._children_yang_names.add("technology")

                self.profile = Cellular.Input.Lte.Profile()
                self.profile.parent = self
                self._children_name_map["profile"] = "profile"
                self._children_yang_names.add("profile")
                self._segment_path = lambda: "lte"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/input/%s" % self._segment_path()


            class Technology(Entity):
                """
                
                
                .. attribute:: lte
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: auto
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: umts
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Cellular.Input.Lte.Technology, self).__init__()

                    self.yang_name = "technology"
                    self.yang_parent_name = "lte"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lte', YLeaf(YType.empty, 'lte')),
                        ('auto', YLeaf(YType.empty, 'auto')),
                        ('umts', YLeaf(YType.empty, 'umts')),
                    ])
                    self.lte = None
                    self.auto = None
                    self.umts = None
                    self._segment_path = lambda: "technology"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/input/lte/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Cellular.Input.Lte.Technology, ['lte', 'auto', 'umts'], name, value)


            class Profile(Entity):
                """
                
                
                .. attribute:: delete
                
                	Delete a Profile
                	**type**\:  :py:class:`Delete <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Input.Lte.Profile.Delete>`
                
                .. attribute:: create
                
                	Create a Profile
                	**type**\:  :py:class:`Create <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Cellular.Input.Lte.Profile.Create>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Cellular.Input.Lte.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "lte"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("delete", ("delete", Cellular.Input.Lte.Profile.Delete)), ("create", ("create", Cellular.Input.Lte.Profile.Create))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.delete = Cellular.Input.Lte.Profile.Delete()
                    self.delete.parent = self
                    self._children_name_map["delete"] = "delete"
                    self._children_yang_names.add("delete")

                    self.create = Cellular.Input.Lte.Profile.Create()
                    self.create.parent = self
                    self._children_name_map["create"] = "create"
                    self._children_yang_names.add("create")
                    self._segment_path = lambda: "profile"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/input/lte/%s" % self._segment_path()


                class Delete(Entity):
                    """
                    Delete a Profile
                    
                    .. attribute:: y_profile_id
                    
                    	Profile ID
                    	**type**\: int
                    
                    	**range:** 1..16
                    
                    

                    """

                    _prefix = 'ios-xe-rpc'
                    _revision = '2017-12-06'

                    def __init__(self):
                        super(Cellular.Input.Lte.Profile.Delete, self).__init__()

                        self.yang_name = "delete"
                        self.yang_parent_name = "profile"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('y_profile_id', YLeaf(YType.uint8, '_profile-id')),
                        ])
                        self.y_profile_id = None
                        self._segment_path = lambda: "delete"
                        self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/input/lte/profile/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cellular.Input.Lte.Profile.Delete, ['y_profile_id'], name, value)


                class Create(Entity):
                    """
                    Create a Profile
                    
                    .. attribute:: y_profile_id
                    
                    	Profile ID
                    	**type**\: int
                    
                    	**range:** 1..16
                    
                    .. attribute:: y_prof_name
                    
                    	Profile name
                    	**type**\: str
                    
                    .. attribute:: none
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: chap
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: pap
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: pap_chap
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: y_user_name
                    
                    	Username for authentication
                    	**type**\: str
                    
                    .. attribute:: y_password
                    
                    	Password for authentication
                    	**type**\: str
                    
                    .. attribute:: ipv4
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: ipv6
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: ipv4v6
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ios-xe-rpc'
                    _revision = '2017-12-06'

                    def __init__(self):
                        super(Cellular.Input.Lte.Profile.Create, self).__init__()

                        self.yang_name = "create"
                        self.yang_parent_name = "profile"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('y_profile_id', YLeaf(YType.uint8, '_profile-id')),
                            ('y_prof_name', YLeaf(YType.str, '_prof_name')),
                            ('none', YLeaf(YType.empty, 'none')),
                            ('chap', YLeaf(YType.empty, 'chap')),
                            ('pap', YLeaf(YType.empty, 'pap')),
                            ('pap_chap', YLeaf(YType.empty, 'pap_chap')),
                            ('y_user_name', YLeaf(YType.str, '_user_name')),
                            ('y_password', YLeaf(YType.str, '_password')),
                            ('ipv4', YLeaf(YType.empty, 'ipv4')),
                            ('ipv6', YLeaf(YType.empty, 'ipv6')),
                            ('ipv4v6', YLeaf(YType.empty, 'ipv4v6')),
                        ])
                        self.y_profile_id = None
                        self.y_prof_name = None
                        self.none = None
                        self.chap = None
                        self.pap = None
                        self.pap_chap = None
                        self.y_user_name = None
                        self.y_password = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self.ipv4v6 = None
                        self._segment_path = lambda: "create"
                        self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/input/lte/profile/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cellular.Input.Lte.Profile.Create, ['y_profile_id', 'y_prof_name', 'none', 'chap', 'pap', 'pap_chap', 'y_user_name', 'y_password', 'ipv4', 'ipv6', 'ipv4v6'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Cellular.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "cellular"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:cellular/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Cellular.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Cellular()
        return self._top_entity

class License(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(License, self).__init__()
        self._top_entity = None

        self.yang_name = "license"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = License.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = License.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:license"


    class Input(Entity):
        """
        
        
        .. attribute:: smart
        
        	
        	**type**\:  :py:class:`Smart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(License.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "license"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("smart", ("smart", License.Input.Smart))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.smart = License.Input.Smart()
            self.smart.parent = self
            self._children_name_map["smart"] = "smart"
            self._children_yang_names.add("smart")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/%s" % self._segment_path()


        class Smart(Entity):
            """
            
            
            .. attribute:: register
            
            	
            	**type**\:  :py:class:`Register <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Register>`
            
            .. attribute:: deregister
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: renew
            
            	
            	**type**\:  :py:class:`Renew <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Renew>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(License.Input.Smart, self).__init__()

                self.yang_name = "smart"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("register", ("register", License.Input.Smart.Register)), ("renew", ("renew", License.Input.Smart.Renew))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('deregister', YLeaf(YType.empty, 'deregister')),
                ])
                self.deregister = None

                self.register = License.Input.Smart.Register()
                self.register.parent = self
                self._children_name_map["register"] = "register"
                self._children_yang_names.add("register")

                self.renew = License.Input.Smart.Renew()
                self.renew.parent = self
                self._children_name_map["renew"] = "renew"
                self._children_yang_names.add("renew")
                self._segment_path = lambda: "smart"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(License.Input.Smart, ['deregister'], name, value)


            class Register(Entity):
                """
                
                
                .. attribute:: idtoken
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: force
                
                	Forcefully register
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(License.Input.Smart.Register, self).__init__()

                    self.yang_name = "register"
                    self.yang_parent_name = "smart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('idtoken', YLeaf(YType.str, 'idtoken')),
                        ('force', YLeaf(YType.empty, 'force')),
                    ])
                    self.idtoken = None
                    self.force = None
                    self._segment_path = lambda: "register"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/input/smart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(License.Input.Smart.Register, ['idtoken', 'force'], name, value)


            class Renew(Entity):
                """
                
                
                .. attribute:: id
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: auth
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(License.Input.Smart.Renew, self).__init__()

                    self.yang_name = "renew"
                    self.yang_parent_name = "smart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('id', YLeaf(YType.empty, 'ID')),
                        ('auth', YLeaf(YType.empty, 'auth')),
                    ])
                    self.id = None
                    self.auth = None
                    self._segment_path = lambda: "renew"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/input/smart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(License.Input.Smart.Renew, ['id', 'auth'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(License.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "license"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(License.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = License()
        return self._top_entity

class Service(Entity):
    """
    SD\-AVC service management
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Service, self).__init__()
        self._top_entity = None

        self.yang_name = "service"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Service.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Service.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:service"


    class Input(Entity):
        """
        
        
        .. attribute:: sd_avc
        
        	
        	**type**\:  :py:class:`SdAvc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input.SdAvc>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Service.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("sd-avc", ("sd_avc", Service.Input.SdAvc))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.sd_avc = Service.Input.SdAvc()
            self.sd_avc.parent = self
            self._children_name_map["sd_avc"] = "sd-avc"
            self._children_yang_names.add("sd-avc")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/%s" % self._segment_path()


        class SdAvc(Entity):
            """
            
            
            .. attribute:: activate
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: configure
            
            	
            	**type**\:  :py:class:`Configure <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input.SdAvc.Configure>`
            
            .. attribute:: connect
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: help
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: deactivate
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: install
            
            	
            	**type**\:  :py:class:`Install <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input.SdAvc.Install>`
            
            .. attribute:: status
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: unconfigure
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: uninstall
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: upgrade
            
            	
            	**type**\:  :py:class:`Upgrade <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input.SdAvc.Upgrade>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(Service.Input.SdAvc, self).__init__()

                self.yang_name = "sd-avc"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("configure", ("configure", Service.Input.SdAvc.Configure)), ("install", ("install", Service.Input.SdAvc.Install)), ("upgrade", ("upgrade", Service.Input.SdAvc.Upgrade))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('activate', YLeaf(YType.empty, 'activate')),
                    ('connect', YLeaf(YType.empty, 'connect')),
                    ('help', YLeaf(YType.empty, 'help')),
                    ('deactivate', YLeaf(YType.empty, 'deactivate')),
                    ('status', YLeaf(YType.empty, 'status')),
                    ('unconfigure', YLeaf(YType.empty, 'unconfigure')),
                    ('uninstall', YLeaf(YType.empty, 'uninstall')),
                ])
                self.activate = None
                self.connect = None
                self.help = None
                self.deactivate = None
                self.status = None
                self.unconfigure = None
                self.uninstall = None

                self.configure = Service.Input.SdAvc.Configure()
                self.configure.parent = self
                self._children_name_map["configure"] = "configure"
                self._children_yang_names.add("configure")

                self.install = Service.Input.SdAvc.Install()
                self.install.parent = self
                self._children_name_map["install"] = "install"
                self._children_yang_names.add("install")

                self.upgrade = Service.Input.SdAvc.Upgrade()
                self.upgrade.parent = self
                self._children_name_map["upgrade"] = "upgrade"
                self._children_yang_names.add("upgrade")
                self._segment_path = lambda: "sd-avc"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Service.Input.SdAvc, ['activate', 'connect', 'help', 'deactivate', 'status', 'unconfigure', 'uninstall'], name, value)


            class Configure(Entity):
                """
                
                
                .. attribute:: gateway
                
                	
                	**type**\:  :py:class:`Gateway <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input.SdAvc.Configure.Gateway>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Service.Input.SdAvc.Configure, self).__init__()

                    self.yang_name = "configure"
                    self.yang_parent_name = "sd-avc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("gateway", ("gateway", Service.Input.SdAvc.Configure.Gateway))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.gateway = Service.Input.SdAvc.Configure.Gateway()
                    self.gateway.parent = self
                    self._children_name_map["gateway"] = "gateway"
                    self._children_yang_names.add("gateway")
                    self._segment_path = lambda: "configure"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/input/sd-avc/%s" % self._segment_path()


                class Gateway(Entity):
                    """
                    
                    
                    .. attribute:: interface
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: service_ip
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: activate
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ios-xe-rpc'
                    _revision = '2017-12-06'

                    def __init__(self):
                        super(Service.Input.SdAvc.Configure.Gateway, self).__init__()

                        self.yang_name = "gateway"
                        self.yang_parent_name = "configure"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('service_ip', YLeaf(YType.str, 'service-ip')),
                            ('activate', YLeaf(YType.empty, 'activate')),
                        ])
                        self.interface = None
                        self.service_ip = None
                        self.activate = None
                        self._segment_path = lambda: "gateway"
                        self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/input/sd-avc/configure/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Service.Input.SdAvc.Configure.Gateway, ['interface', 'service_ip', 'activate'], name, value)


            class Install(Entity):
                """
                
                
                .. attribute:: package
                
                	
                	**type**\: str
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Service.Input.SdAvc.Install, self).__init__()

                    self.yang_name = "install"
                    self.yang_parent_name = "sd-avc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('package', YLeaf(YType.str, 'package')),
                    ])
                    self.package = None
                    self._segment_path = lambda: "install"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/input/sd-avc/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Service.Input.SdAvc.Install, ['package'], name, value)


            class Upgrade(Entity):
                """
                
                
                .. attribute:: package
                
                	
                	**type**\: str
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-12-06'

                def __init__(self):
                    super(Service.Input.SdAvc.Upgrade, self).__init__()

                    self.yang_name = "upgrade"
                    self.yang_parent_name = "sd-avc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('package', YLeaf(YType.str, 'package')),
                    ])
                    self.package = None
                    self._segment_path = lambda: "upgrade"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/input/sd-avc/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Service.Input.SdAvc.Upgrade, ['package'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Service.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Service.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Service()
        return self._top_entity

class VirtualService(Entity):
    """
    Virtual\-service management
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.VirtualService.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.VirtualService.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(VirtualService, self).__init__()
        self._top_entity = None

        self.yang_name = "virtual-service"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = VirtualService.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = VirtualService.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:virtual-service"


    class Input(Entity):
        """
        
        
        .. attribute:: install
        
        	
        	**type**\:  :py:class:`Install <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.VirtualService.Input.Install>`
        
        .. attribute:: uninstall
        
        	
        	**type**\:  :py:class:`Uninstall <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.VirtualService.Input.Uninstall>`
        
        .. attribute:: upgrade
        
        	
        	**type**\:  :py:class:`Upgrade <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.VirtualService.Input.Upgrade>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(VirtualService.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "virtual-service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("install", ("install", VirtualService.Input.Install)), ("uninstall", ("uninstall", VirtualService.Input.Uninstall)), ("upgrade", ("upgrade", VirtualService.Input.Upgrade))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.install = VirtualService.Input.Install()
            self.install.parent = self
            self._children_name_map["install"] = "install"
            self._children_yang_names.add("install")

            self.uninstall = VirtualService.Input.Uninstall()
            self.uninstall.parent = self
            self._children_name_map["uninstall"] = "uninstall"
            self._children_yang_names.add("uninstall")

            self.upgrade = VirtualService.Input.Upgrade()
            self.upgrade.parent = self
            self._children_name_map["upgrade"] = "upgrade"
            self._children_yang_names.add("upgrade")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:virtual-service/%s" % self._segment_path()


        class Install(Entity):
            """
            
            
            .. attribute:: name
            
            	
            	**type**\: str
            
            .. attribute:: package
            
            	
            	**type**\: str
            
            .. attribute:: media
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(VirtualService.Input.Install, self).__init__()

                self.yang_name = "install"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('package', YLeaf(YType.str, 'package')),
                    ('media', YLeaf(YType.str, 'media')),
                ])
                self.name = None
                self.package = None
                self.media = None
                self._segment_path = lambda: "install"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:virtual-service/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualService.Input.Install, ['name', 'package', 'media'], name, value)


        class Uninstall(Entity):
            """
            
            
            .. attribute:: name
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(VirtualService.Input.Uninstall, self).__init__()

                self.yang_name = "uninstall"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None
                self._segment_path = lambda: "uninstall"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:virtual-service/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualService.Input.Uninstall, ['name'], name, value)


        class Upgrade(Entity):
            """
            
            
            .. attribute:: name
            
            	
            	**type**\: str
            
            .. attribute:: package
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(VirtualService.Input.Upgrade, self).__init__()

                self.yang_name = "upgrade"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('package', YLeaf(YType.str, 'package')),
                ])
                self.name = None
                self.package = None
                self._segment_path = lambda: "upgrade"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:virtual-service/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualService.Input.Upgrade, ['name', 'package'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(VirtualService.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "virtual-service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:virtual-service/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualService.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = VirtualService()
        return self._top_entity

class Copy(Entity):
    """
    Copy from one file to another
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Copy.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Copy.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Copy, self).__init__()
        self._top_entity = None

        self.yang_name = "copy"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Copy.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Copy.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:copy"


    class Input(Entity):
        """
        
        
        .. attribute:: y_source
        
        	
        	**type**\: str
        
        	**pattern:** ((((bootflash\:)\|(harddisk\:)\|(flash\:)\|(nvram\:)\|(ftp\:)\|(http\:)\|(https\:)\|(scp\:)\|(tftp\:)).\*)\|((running\-config)\|(startup\-config)))
        
        	**mandatory**\: True
        
        .. attribute:: y_destination
        
        	
        	**type**\: str
        
        	**pattern:** ((((bootflash\:)\|(harddisk\:)\|(flash\:)\|(nvram\:)\|(ftp\:)\|(http\:)\|(https\:)\|(scp\:)\|(tftp\:)).\*)\|((running\-config)\|(startup\-config)))
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Copy.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "copy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('y_source', YLeaf(YType.str, '_source')),
                ('y_destination', YLeaf(YType.str, '_destination')),
            ])
            self.y_source = None
            self.y_destination = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:copy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Copy.Input, ['y_source', 'y_destination'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Copy.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "copy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:copy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Copy.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Copy()
        return self._top_entity

class Delete(Entity):
    """
    Delete a file
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Delete.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Delete.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Delete, self).__init__()
        self._top_entity = None

        self.yang_name = "delete"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Delete.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Delete.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:delete"


    class Input(Entity):
        """
        
        
        .. attribute:: y_filename
        
        	
        	**type**\: str
        
        	**pattern:** (((bootflash\:)\|(harddisk\:)\|(flash\:)\|(nvram\:)).\*)
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Delete.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "delete"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('y_filename', YLeaf(YType.str, '_filename')),
            ])
            self.y_filename = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:delete/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Delete.Input, ['y_filename'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Delete.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "delete"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:delete/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Delete.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Delete()
        return self._top_entity

class AppHosting(Entity):
    """
    App\-hosting management
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(AppHosting, self).__init__()
        self._top_entity = None

        self.yang_name = "app-hosting"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = AppHosting.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = AppHosting.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:app-hosting"


    class Input(Entity):
        """
        
        
        .. attribute:: install
        
        	
        	**type**\:  :py:class:`Install <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input.Install>`
        
        .. attribute:: uninstall
        
        	
        	**type**\:  :py:class:`Uninstall <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input.Uninstall>`
        
        .. attribute:: activate
        
        	
        	**type**\:  :py:class:`Activate <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input.Activate>`
        
        .. attribute:: deactivate
        
        	
        	**type**\:  :py:class:`Deactivate <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input.Deactivate>`
        
        .. attribute:: start
        
        	
        	**type**\:  :py:class:`Start <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input.Start>`
        
        .. attribute:: stop
        
        	
        	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.AppHosting.Input.Stop>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(AppHosting.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "app-hosting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("install", ("install", AppHosting.Input.Install)), ("uninstall", ("uninstall", AppHosting.Input.Uninstall)), ("activate", ("activate", AppHosting.Input.Activate)), ("deactivate", ("deactivate", AppHosting.Input.Deactivate)), ("start", ("start", AppHosting.Input.Start)), ("stop", ("stop", AppHosting.Input.Stop))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.install = AppHosting.Input.Install()
            self.install.parent = self
            self._children_name_map["install"] = "install"
            self._children_yang_names.add("install")

            self.uninstall = AppHosting.Input.Uninstall()
            self.uninstall.parent = self
            self._children_name_map["uninstall"] = "uninstall"
            self._children_yang_names.add("uninstall")

            self.activate = AppHosting.Input.Activate()
            self.activate.parent = self
            self._children_name_map["activate"] = "activate"
            self._children_yang_names.add("activate")

            self.deactivate = AppHosting.Input.Deactivate()
            self.deactivate.parent = self
            self._children_name_map["deactivate"] = "deactivate"
            self._children_yang_names.add("deactivate")

            self.start = AppHosting.Input.Start()
            self.start.parent = self
            self._children_name_map["start"] = "start"
            self._children_yang_names.add("start")

            self.stop = AppHosting.Input.Stop()
            self.stop.parent = self
            self._children_name_map["stop"] = "stop"
            self._children_yang_names.add("stop")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/%s" % self._segment_path()


        class Install(Entity):
            """
            
            
            .. attribute:: appid
            
            	
            	**type**\: str
            
            .. attribute:: package
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(AppHosting.Input.Install, self).__init__()

                self.yang_name = "install"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('appid', YLeaf(YType.str, 'appid')),
                    ('package', YLeaf(YType.str, 'package')),
                ])
                self.appid = None
                self.package = None
                self._segment_path = lambda: "install"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AppHosting.Input.Install, ['appid', 'package'], name, value)


        class Uninstall(Entity):
            """
            
            
            .. attribute:: appid
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(AppHosting.Input.Uninstall, self).__init__()

                self.yang_name = "uninstall"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('appid', YLeaf(YType.str, 'appid')),
                ])
                self.appid = None
                self._segment_path = lambda: "uninstall"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AppHosting.Input.Uninstall, ['appid'], name, value)


        class Activate(Entity):
            """
            
            
            .. attribute:: appid
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(AppHosting.Input.Activate, self).__init__()

                self.yang_name = "activate"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('appid', YLeaf(YType.str, 'appid')),
                ])
                self.appid = None
                self._segment_path = lambda: "activate"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AppHosting.Input.Activate, ['appid'], name, value)


        class Deactivate(Entity):
            """
            
            
            .. attribute:: appid
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(AppHosting.Input.Deactivate, self).__init__()

                self.yang_name = "deactivate"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('appid', YLeaf(YType.str, 'appid')),
                ])
                self.appid = None
                self._segment_path = lambda: "deactivate"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AppHosting.Input.Deactivate, ['appid'], name, value)


        class Start(Entity):
            """
            
            
            .. attribute:: appid
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(AppHosting.Input.Start, self).__init__()

                self.yang_name = "start"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('appid', YLeaf(YType.str, 'appid')),
                ])
                self.appid = None
                self._segment_path = lambda: "start"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AppHosting.Input.Start, ['appid'], name, value)


        class Stop(Entity):
            """
            
            
            .. attribute:: appid
            
            	
            	**type**\: str
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-12-06'

            def __init__(self):
                super(AppHosting.Input.Stop, self).__init__()

                self.yang_name = "stop"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('appid', YLeaf(YType.str, 'appid')),
                ])
                self.appid = None
                self._segment_path = lambda: "stop"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(AppHosting.Input.Stop, ['appid'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(AppHosting.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "app-hosting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:app-hosting/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AppHosting.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = AppHosting()
        return self._top_entity

class Guestshell(Entity):
    """
    guestshell managementshell
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Guestshell.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Guestshell.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-12-06'

    def __init__(self):
        super(Guestshell, self).__init__()
        self._top_entity = None

        self.yang_name = "guestshell"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Guestshell.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Guestshell.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:guestshell"


    class Input(Entity):
        """
        
        
        .. attribute:: destroy
        
        	Destroy guestshell
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: disable
        
        	Disable guestshell
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: enable
        
        	Enable guestshell
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Guestshell.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "guestshell"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('destroy', YLeaf(YType.empty, 'destroy')),
                ('disable', YLeaf(YType.empty, 'disable')),
                ('enable', YLeaf(YType.empty, 'enable')),
            ])
            self.destroy = None
            self.disable = None
            self.enable = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:guestshell/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Guestshell.Input, ['destroy', 'disable', 'enable'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-12-06'

        def __init__(self):
            super(Guestshell.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "guestshell"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:guestshell/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Guestshell.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Guestshell()
        return self._top_entity

