""" Cisco_IOS_XR_sysadmin_console 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module defines the top level container for
all 'console' commands for Sysadmin.

Copyright(c) 2015\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Console(Entity):
    """
    
    
    .. attribute:: config
    
    	
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config>`
    
    

    """

    _prefix = 'calvados_console'
    _revision = '2017-01-31'

    def __init__(self):
        super(Console, self).__init__()
        self._top_entity = None

        self.yang_name = "console"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-console"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("config", ("config", Console.Config))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.config = Console.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-console:console"


    class Config(Entity):
        """
        
        
        .. attribute:: attach_sdr
        
        	
        	**type**\:  :py:class:`AttachSdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config.AttachSdr>`
        
        

        """

        _prefix = 'calvados_console'
        _revision = '2017-01-31'

        def __init__(self):
            super(Console.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "console"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("attach-sdr", ("attach_sdr", Console.Config.AttachSdr))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.attach_sdr = Console.Config.AttachSdr()
            self.attach_sdr.parent = self
            self._children_name_map["attach_sdr"] = "attach-sdr"
            self._children_yang_names.add("attach-sdr")
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-console:console/%s" % self._segment_path()


        class AttachSdr(Entity):
            """
            
            
            .. attribute:: runtime
            
            	
            	**type**\:  :py:class:`Runtime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config.AttachSdr.Runtime>`
            
            .. attribute:: boot
            
            	
            	**type**\:  :py:class:`Boot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config.AttachSdr.Boot>`
            
            

            """

            _prefix = 'calvados_console'
            _revision = '2017-01-31'

            def __init__(self):
                super(Console.Config.AttachSdr, self).__init__()

                self.yang_name = "attach-sdr"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("runtime", ("runtime", Console.Config.AttachSdr.Runtime)), ("boot", ("boot", Console.Config.AttachSdr.Boot))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.runtime = Console.Config.AttachSdr.Runtime()
                self.runtime.parent = self
                self._children_name_map["runtime"] = "runtime"
                self._children_yang_names.add("runtime")

                self.boot = Console.Config.AttachSdr.Boot()
                self.boot.parent = self
                self._children_name_map["boot"] = "boot"
                self._children_yang_names.add("boot")
                self._segment_path = lambda: "attach-sdr"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-console:console/config/%s" % self._segment_path()


            class Runtime(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config.AttachSdr.Runtime.Location>`
                
                

                """

                _prefix = 'calvados_console'
                _revision = '2017-01-31'

                def __init__(self):
                    super(Console.Config.AttachSdr.Runtime, self).__init__()

                    self.yang_name = "runtime"
                    self.yang_parent_name = "attach-sdr"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("location", ("location", Console.Config.AttachSdr.Runtime.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "runtime"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-console:console/config/attach-sdr/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Console.Config.AttachSdr.Runtime, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location_rp  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((0?[0\-9]\|1[1\-5])/([rR][pP]\\d{1,2}))(/[cC][pP][uU]0)?
                    
                    .. attribute:: tty_name
                    
                    	
                    	**type**\: list of  		 :py:class:`TtyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config.AttachSdr.Runtime.Location.TtyName>`
                    
                    

                    """

                    _prefix = 'calvados_console'
                    _revision = '2017-01-31'

                    def __init__(self):
                        super(Console.Config.AttachSdr.Runtime.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "runtime"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location_rp']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("tty-name", ("tty_name", Console.Config.AttachSdr.Runtime.Location.TtyName))])
                        self._leafs = OrderedDict([
                            ('location_rp', YLeaf(YType.str, 'location-rp')),
                        ])
                        self.location_rp = None

                        self.tty_name = YList(self)
                        self._segment_path = lambda: "location" + "[location-rp='" + str(self.location_rp) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-console:console/config/attach-sdr/runtime/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Console.Config.AttachSdr.Runtime.Location, ['location_rp'], name, value)


                    class TtyName(Entity):
                        """
                        
                        
                        .. attribute:: ttyname  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** console1\|console2
                        
                        .. attribute:: sdr_name
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9\_.{}+\-]+
                        
                        

                        """

                        _prefix = 'calvados_console'
                        _revision = '2017-01-31'

                        def __init__(self):
                            super(Console.Config.AttachSdr.Runtime.Location.TtyName, self).__init__()

                            self.yang_name = "tty-name"
                            self.yang_parent_name = "location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ttyname']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ttyname', YLeaf(YType.str, 'ttyname')),
                                ('sdr_name', YLeaf(YType.str, 'sdr-name')),
                            ])
                            self.ttyname = None
                            self.sdr_name = None
                            self._segment_path = lambda: "tty-name" + "[ttyname='" + str(self.ttyname) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Console.Config.AttachSdr.Runtime.Location.TtyName, ['ttyname', 'sdr_name'], name, value)


            class Boot(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_console.Console.Config.AttachSdr.Boot.Location>`
                
                

                """

                _prefix = 'calvados_console'
                _revision = '2017-01-31'

                def __init__(self):
                    super(Console.Config.AttachSdr.Boot, self).__init__()

                    self.yang_name = "boot"
                    self.yang_parent_name = "attach-sdr"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("location", ("location", Console.Config.AttachSdr.Boot.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "boot"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-console:console/config/attach-sdr/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Console.Config.AttachSdr.Boot, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: location_rp  (key)
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** ((0?[0\-9]\|1[1\-5])/([rR][pP]\\d{1,2}))(/[cC][pP][uU]0)?
                    
                    .. attribute:: sdr_name
                    
                    	
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9\_.{}+\-]+
                    
                    

                    """

                    _prefix = 'calvados_console'
                    _revision = '2017-01-31'

                    def __init__(self):
                        super(Console.Config.AttachSdr.Boot.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "boot"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location_rp']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('location_rp', YLeaf(YType.str, 'location-rp')),
                            ('sdr_name', YLeaf(YType.str, 'sdr-name')),
                        ])
                        self.location_rp = None
                        self.sdr_name = None
                        self._segment_path = lambda: "location" + "[location-rp='" + str(self.location_rp) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-console:console/config/attach-sdr/boot/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Console.Config.AttachSdr.Boot.Location, ['location_rp', 'sdr_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Console()
        return self._top_entity

