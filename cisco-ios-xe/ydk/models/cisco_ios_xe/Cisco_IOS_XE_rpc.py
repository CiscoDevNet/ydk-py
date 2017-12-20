""" Cisco_IOS_XE_rpc 

NED RPC YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Switch(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-08-28'

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
        _revision = '2017-08-28'

        def __init__(self):
            super(Switch.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "switch"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"statck" : ("statck", Switch.Input.Statck)}
            self._child_list_classes = {}

            self.y_switch_number = YLeaf(YType.uint8, "_switch-number")

            self.priority = YLeaf(YType.uint8, "priority")

            self.renumber = YLeaf(YType.uint8, "renumber")

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
            _revision = '2017-08-28'

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
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-08-28'

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

class Default(Entity):
    """
    Set a command to its defaults
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-08-28'

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
        	**type**\: str
        
        	**pattern:** [A\-Za\-z]([\\w/.\-]+)
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-08-28'

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
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-08-28'

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

class Reload(Entity):
    """
    Halt and perform a cold restart
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Reload.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Reload.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-08-28'

    def __init__(self):
        super(Reload, self).__init__()
        self._top_entity = None

        self.yang_name = "reload"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

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
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-08-28'

        def __init__(self):
            super(Reload.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "reload"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.force = YLeaf(YType.boolean, "force")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:reload/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Reload.Input, ['force'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-08-28'

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

class License(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-08-28'

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
        
        	
        	**type**\:  :py:class:`Smart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-08-28'

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
            
            
            .. attribute:: register
            
            	
            	**type**\:  :py:class:`Register <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Register>`
            
            .. attribute:: deregister
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: renew
            
            	
            	**type**\:  :py:class:`Renew <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Renew>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-08-28'

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
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-08-28'

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
                
                
                .. attribute:: id
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: auth
                
                	
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-08-28'

                def __init__(self):
                    super(License.Input.Smart.Renew, self).__init__()

                    self.yang_name = "renew"
                    self.yang_parent_name = "smart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.id = YLeaf(YType.empty, "id")

                    self.auth = YLeaf(YType.empty, "auth")
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
        _revision = '2017-08-28'

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

class Service(Entity):
    """
    SD\-AVC service management
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Service.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-08-28'

    def __init__(self):
        super(Service, self).__init__()
        self._top_entity = None

        self.yang_name = "service"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

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
        _revision = '2017-08-28'

        def __init__(self):
            super(Service.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"sd-avc" : ("sd_avc", Service.Input.SdAvc)}
            self._child_list_classes = {}

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
            _revision = '2017-08-28'

            def __init__(self):
                super(Service.Input.SdAvc, self).__init__()

                self.yang_name = "sd-avc"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"configure" : ("configure", Service.Input.SdAvc.Configure), "install" : ("install", Service.Input.SdAvc.Install), "upgrade" : ("upgrade", Service.Input.SdAvc.Upgrade)}
                self._child_list_classes = {}

                self.activate = YLeaf(YType.empty, "activate")

                self.connect = YLeaf(YType.empty, "connect")

                self.help = YLeaf(YType.empty, "help")

                self.deactivate = YLeaf(YType.empty, "deactivate")

                self.status = YLeaf(YType.empty, "status")

                self.unconfigure = YLeaf(YType.empty, "unconfigure")

                self.uninstall = YLeaf(YType.empty, "uninstall")

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
                _revision = '2017-08-28'

                def __init__(self):
                    super(Service.Input.SdAvc.Configure, self).__init__()

                    self.yang_name = "configure"
                    self.yang_parent_name = "sd-avc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"gateway" : ("gateway", Service.Input.SdAvc.Configure.Gateway)}
                    self._child_list_classes = {}

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
                    _revision = '2017-08-28'

                    def __init__(self):
                        super(Service.Input.SdAvc.Configure.Gateway, self).__init__()

                        self.yang_name = "gateway"
                        self.yang_parent_name = "configure"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")

                        self.service_ip = YLeaf(YType.str, "service-ip")

                        self.activate = YLeaf(YType.empty, "activate")
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
                _revision = '2017-08-28'

                def __init__(self):
                    super(Service.Input.SdAvc.Install, self).__init__()

                    self.yang_name = "install"
                    self.yang_parent_name = "sd-avc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.package = YLeaf(YType.str, "package")
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
                _revision = '2017-08-28'

                def __init__(self):
                    super(Service.Input.SdAvc.Upgrade, self).__init__()

                    self.yang_name = "upgrade"
                    self.yang_parent_name = "sd-avc"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.package = YLeaf(YType.str, "package")
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
        _revision = '2017-08-28'

        def __init__(self):
            super(Service.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "service"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.result = YLeaf(YType.str, "result")
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-rpc:service/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Service.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Service()
        return self._top_entity

