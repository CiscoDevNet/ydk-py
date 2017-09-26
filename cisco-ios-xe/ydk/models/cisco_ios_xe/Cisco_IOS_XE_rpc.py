""" Cisco_IOS_XE_rpc 

NED RPC YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Default(Entity):
    """
    Set a command to its defaults
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(Default, self).__init__()
        self._top_entity = None

        self.yang_name = "default"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

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
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Default.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "default"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.interface = YLeaf(YType.str, "interface")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:default/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Default.Input, ['interface'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Default.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "default"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.result = YLeaf(YType.str, "result")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:default/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Default.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Default()
        return self._top_entity

class License(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(License, self).__init__()
        self._top_entity = None

        self.yang_name = "license"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

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
        
        	
        	**type**\:   :py:class:`Smart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(License.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "license"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"smart" : ("smart", License.Input.Smart)}
            self._child_list_classes = {}

            self.smart = License.Input.Smart()
            self.smart.parent = self
            self._children_name_map["smart"] = "smart"
            self._children_yang_names.add("smart")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/%s" % self._segment_path()


        class Smart(Entity):
            """
            
            
            .. attribute:: deregister
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: register
            
            	
            	**type**\:   :py:class:`Register <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Register>`
            
            .. attribute:: renew
            
            	
            	**type**\:   :py:class:`Renew <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Renew>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-02-07'

            def __init__(self):
                super(License.Input.Smart, self).__init__()

                self.yang_name = "smart"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"register" : ("register", License.Input.Smart.Register), "renew" : ("renew", License.Input.Smart.Renew)}
                self._child_list_classes = {}

                self.deregister = YLeaf(YType.empty, "deregister")

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
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-02-07'

                def __init__(self):
                    super(License.Input.Smart.Register, self).__init__()

                    self.yang_name = "register"
                    self.yang_parent_name = "smart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.idtoken = YLeaf(YType.empty, "idtoken")
                    self._segment_path = lambda: "register"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/input/smart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(License.Input.Smart.Register, ['idtoken'], name, value)


            class Renew(Entity):
                """
                
                
                .. attribute:: auth
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: id
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-02-07'

                def __init__(self):
                    super(License.Input.Smart.Renew, self).__init__()

                    self.yang_name = "renew"
                    self.yang_parent_name = "smart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.auth = YLeaf(YType.empty, "auth")

                    self.id = YLeaf(YType.empty, "id")
                    self._segment_path = lambda: "renew"
                    self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/input/smart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(License.Input.Smart.Renew, ['auth', 'id'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(License.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "license"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.result = YLeaf(YType.str, "result")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:license/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(License.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = License()
        return self._top_entity

class Reload(Entity):
    """
    Halt and perform a cold restart
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Reload.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(Reload, self).__init__()
        self._top_entity = None

        self.yang_name = "reload"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.output = Reload.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-rpc:reload"


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Reload.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "reload"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.result = YLeaf(YType.str, "result")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:reload/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Reload.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Reload()
        return self._top_entity

class Switch(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(Switch, self).__init__()
        self._top_entity = None

        self.yang_name = "switch"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

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
        
        
        .. attribute:: priority
        
        	<1\-15>  Switch Priority
        	**type**\:  int
        
        	**range:** 1..15
        
        .. attribute:: renumber
        
        	<1\-9>  New number of the Switch
        	**type**\:  int
        
        	**range:** 1..9
        
        .. attribute:: statck
        
        	
        	**type**\:   :py:class:`Statck <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input.Statck>`
        
        .. attribute:: switch_number
        
        	
        	**type**\:  int
        
        	**range:** 1..9
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Switch.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "switch"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"statck" : ("statck", Switch.Input.Statck)}
            self._child_list_classes = {}

            self.priority = YLeaf(YType.uint8, "priority")

            self.renumber = YLeaf(YType.uint8, "renumber")

            self.switch_number = YLeaf(YType.uint8, "switch-number")

            self.statck = Switch.Input.Statck()
            self.statck.parent = self
            self._children_name_map["statck"] = "statck"
            self._children_yang_names.add("statck")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:switch/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Switch.Input, ['priority', 'renumber', 'switch_number'], name, value)


        class Statck(Entity):
            """
            
            
            .. attribute:: port
            
            	<1\-2>  Stack port number to enable/disable
            	**type**\:  int
            
            	**range:** 1..2
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-02-07'

            def __init__(self):
                super(Switch.Input.Statck, self).__init__()

                self.yang_name = "statck"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.port = YLeaf(YType.uint8, "port")
                self._segment_path = lambda: "statck"
                self._absolute_path = lambda: "Cisco-IOS-XE-rpc:switch/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Switch.Input.Statck, ['port'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Switch.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "switch"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.result = YLeaf(YType.str, "result")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:switch/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Switch.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Switch()
        return self._top_entity

