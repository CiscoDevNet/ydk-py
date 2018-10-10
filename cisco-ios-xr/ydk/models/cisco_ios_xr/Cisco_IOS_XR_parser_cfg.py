""" Cisco_IOS_XR_parser_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR parser package configuration.

This module contains definitions
for the following management objects\:
  parser\: Parser configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Parser(Entity):
    """
    Parser configuration
    
    .. attribute:: indentation
    
    	indentation tracking
    	**type**\:  :py:class:`Indentation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Indentation>`
    
    .. attribute:: alias
    
    	Alias for command mapping
    	**type**\:  :py:class:`Alias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias>`
    
    .. attribute:: history
    
    	cli commands history
    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.History>`
    
    .. attribute:: interactive
    
    	interactive mode
    	**type**\:  :py:class:`Interactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Interactive>`
    
    .. attribute:: commit_optimized
    
    	Enable optimization for regular commit
    	**type**\:  :py:class:`CommitOptimized <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.CommitOptimized>`
    
    .. attribute:: sysadmin_login_banner
    
    	Configuration to disable sysadmin login banner
    	**type**\:  :py:class:`SysadminLoginBanner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.SysadminLoginBanner>`
    
    .. attribute:: interface_display
    
    	Configure the Interface display order
    	**type**\:  :py:class:`InterfaceDisplay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.InterfaceDisplay>`
    
    .. attribute:: netmask_format
    
    	Ipv4 netmask\-format to be configured
    	**type**\:  :py:class:`NetmaskFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.NetmaskFormat>`
    
    .. attribute:: configuration
    
    	cli configuration services
    	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Configuration>`
    
    .. attribute:: submode_exit
    
    	Exit submode when only '!' seen in interactive mode
    	**type**\:  :py:class:`SubmodeExit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.SubmodeExit>`
    
    

    """

    _prefix = 'parser-cfg'
    _revision = '2017-05-09'

    def __init__(self):
        super(Parser, self).__init__()
        self._top_entity = None

        self.yang_name = "parser"
        self.yang_parent_name = "Cisco-IOS-XR-parser-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("indentation", ("indentation", Parser.Indentation)), ("alias", ("alias", Parser.Alias)), ("history", ("history", Parser.History)), ("interactive", ("interactive", Parser.Interactive)), ("commit-optimized", ("commit_optimized", Parser.CommitOptimized)), ("sysadmin-login-banner", ("sysadmin_login_banner", Parser.SysadminLoginBanner)), ("interface-display", ("interface_display", Parser.InterfaceDisplay)), ("netmask-format", ("netmask_format", Parser.NetmaskFormat)), ("configuration", ("configuration", Parser.Configuration)), ("submode-exit", ("submode_exit", Parser.SubmodeExit))])
        self._leafs = OrderedDict()

        self.indentation = Parser.Indentation()
        self.indentation.parent = self
        self._children_name_map["indentation"] = "indentation"

        self.alias = Parser.Alias()
        self.alias.parent = self
        self._children_name_map["alias"] = "alias"

        self.history = Parser.History()
        self.history.parent = self
        self._children_name_map["history"] = "history"

        self.interactive = Parser.Interactive()
        self.interactive.parent = self
        self._children_name_map["interactive"] = "interactive"

        self.commit_optimized = Parser.CommitOptimized()
        self.commit_optimized.parent = self
        self._children_name_map["commit_optimized"] = "commit-optimized"

        self.sysadmin_login_banner = Parser.SysadminLoginBanner()
        self.sysadmin_login_banner.parent = self
        self._children_name_map["sysadmin_login_banner"] = "sysadmin-login-banner"

        self.interface_display = Parser.InterfaceDisplay()
        self.interface_display.parent = self
        self._children_name_map["interface_display"] = "interface-display"

        self.netmask_format = Parser.NetmaskFormat()
        self.netmask_format.parent = self
        self._children_name_map["netmask_format"] = "netmask-format"

        self.configuration = Parser.Configuration()
        self.configuration.parent = self
        self._children_name_map["configuration"] = "configuration"

        self.submode_exit = Parser.SubmodeExit()
        self.submode_exit.parent = self
        self._children_name_map["submode_exit"] = "submode-exit"
        self._segment_path = lambda: "Cisco-IOS-XR-parser-cfg:parser"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Parser, [], name, value)


    class Indentation(Entity):
        """
        indentation tracking
        
        .. attribute:: indentation_disable
        
        	disable the indentation
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Indentation, self).__init__()

            self.yang_name = "indentation"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('indentation_disable', (YLeaf(YType.boolean, 'indentation-disable'), ['bool'])),
            ])
            self.indentation_disable = None
            self._segment_path = lambda: "indentation"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.Indentation, ['indentation_disable'], name, value)


    class Alias(Entity):
        """
        Alias for command mapping
        
        .. attribute:: execs
        
        	Exec command alias
        	**type**\:  :py:class:`Execs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs>`
        
        .. attribute:: configurations
        
        	Configuration command alias
        	**type**\:  :py:class:`Configurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations>`
        
        .. attribute:: alls
        
        	Table of all aliases configured
        	**type**\:  :py:class:`Alls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Alias, self).__init__()

            self.yang_name = "alias"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("execs", ("execs", Parser.Alias.Execs)), ("configurations", ("configurations", Parser.Alias.Configurations)), ("alls", ("alls", Parser.Alias.Alls))])
            self._leafs = OrderedDict()

            self.execs = Parser.Alias.Execs()
            self.execs.parent = self
            self._children_name_map["execs"] = "execs"

            self.configurations = Parser.Alias.Configurations()
            self.configurations.parent = self
            self._children_name_map["configurations"] = "configurations"

            self.alls = Parser.Alias.Alls()
            self.alls.parent = self
            self._children_name_map["alls"] = "alls"
            self._segment_path = lambda: "alias"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.Alias, [], name, value)


        class Execs(Entity):
            """
            Exec command alias
            
            .. attribute:: exec_
            
            	Exec alias name
            	**type**\: list of  		 :py:class:`Exec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs.Exec>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Alias.Execs, self).__init__()

                self.yang_name = "execs"
                self.yang_parent_name = "alias"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("exec", ("exec_", Parser.Alias.Execs.Exec))])
                self._leafs = OrderedDict()

                self.exec_ = YList(self)
                self._segment_path = lambda: "execs"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Alias.Execs, [], name, value)


            class Exec(Entity):
                """
                Exec alias name
                
                .. attribute:: identifier  (key)
                
                	Exec Alias name
                	**type**\: str
                
                	**length:** 1..30
                
                .. attribute:: identifier_xr
                
                	Aliased exec command
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2017-05-09'

                def __init__(self):
                    super(Parser.Alias.Execs.Exec, self).__init__()

                    self.yang_name = "exec"
                    self.yang_parent_name = "execs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['identifier']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                        ('identifier_xr', (YLeaf(YType.str, 'identifier-xr'), ['str'])),
                    ])
                    self.identifier = None
                    self.identifier_xr = None
                    self._segment_path = lambda: "exec" + "[identifier='" + str(self.identifier) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/execs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Parser.Alias.Execs.Exec, ['identifier', 'identifier_xr'], name, value)


        class Configurations(Entity):
            """
            Configuration command alias
            
            .. attribute:: configuration
            
            	Configuration Alias name
            	**type**\: list of  		 :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations.Configuration>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Alias.Configurations, self).__init__()

                self.yang_name = "configurations"
                self.yang_parent_name = "alias"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("configuration", ("configuration", Parser.Alias.Configurations.Configuration))])
                self._leafs = OrderedDict()

                self.configuration = YList(self)
                self._segment_path = lambda: "configurations"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Alias.Configurations, [], name, value)


            class Configuration(Entity):
                """
                Configuration Alias name
                
                .. attribute:: identifier  (key)
                
                	Configuration alias name
                	**type**\: str
                
                	**length:** 1..30
                
                .. attribute:: identifier_xr
                
                	Aliased config command
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2017-05-09'

                def __init__(self):
                    super(Parser.Alias.Configurations.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "configurations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['identifier']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                        ('identifier_xr', (YLeaf(YType.str, 'identifier-xr'), ['str'])),
                    ])
                    self.identifier = None
                    self.identifier_xr = None
                    self._segment_path = lambda: "configuration" + "[identifier='" + str(self.identifier) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/configurations/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Parser.Alias.Configurations.Configuration, ['identifier', 'identifier_xr'], name, value)


        class Alls(Entity):
            """
            Table of all aliases configured
            
            .. attribute:: all
            
            	Alias name to command mapping
            	**type**\: list of  		 :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls.All>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Alias.Alls, self).__init__()

                self.yang_name = "alls"
                self.yang_parent_name = "alias"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("all", ("all", Parser.Alias.Alls.All))])
                self._leafs = OrderedDict()

                self.all = YList(self)
                self._segment_path = lambda: "alls"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Alias.Alls, [], name, value)


            class All(Entity):
                """
                Alias name to command mapping
                
                .. attribute:: identifier  (key)
                
                	Alias name
                	**type**\: str
                
                	**length:** 1..30
                
                .. attribute:: identifier_xr
                
                	The actual command
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2017-05-09'

                def __init__(self):
                    super(Parser.Alias.Alls.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "alls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['identifier']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                        ('identifier_xr', (YLeaf(YType.str, 'identifier-xr'), ['str'])),
                    ])
                    self.identifier = None
                    self.identifier_xr = None
                    self._segment_path = lambda: "all" + "[identifier='" + str(self.identifier) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/alls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Parser.Alias.Alls.All, ['identifier', 'identifier_xr'], name, value)


    class History(Entity):
        """
        cli commands history
        
        .. attribute:: size
        
        	maximum number of commands in history
        	**type**\: int
        
        	**range:** 1000..5000
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.History, self).__init__()

            self.yang_name = "history"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
            ])
            self.size = None
            self._segment_path = lambda: "history"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.History, ['size'], name, value)


    class Interactive(Entity):
        """
        interactive mode
        
        .. attribute:: interactive_disable
        
        	disable interactive mode
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Interactive, self).__init__()

            self.yang_name = "interactive"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('interactive_disable', (YLeaf(YType.boolean, 'interactive-disable'), ['bool'])),
            ])
            self.interactive_disable = None
            self._segment_path = lambda: "interactive"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.Interactive, ['interactive_disable'], name, value)


    class CommitOptimized(Entity):
        """
        Enable optimization for regular commit
        
        .. attribute:: commit_optimized_enable
        
        	Enable the feature
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.CommitOptimized, self).__init__()

            self.yang_name = "commit-optimized"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('commit_optimized_enable', (YLeaf(YType.boolean, 'commit-optimized-enable'), ['bool'])),
            ])
            self.commit_optimized_enable = None
            self._segment_path = lambda: "commit-optimized"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.CommitOptimized, ['commit_optimized_enable'], name, value)


    class SysadminLoginBanner(Entity):
        """
        Configuration to disable sysadmin login banner
        
        .. attribute:: sysadmin_login_banner_disable
        
        	Disable sysadmin login banner
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.SysadminLoginBanner, self).__init__()

            self.yang_name = "sysadmin-login-banner"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sysadmin_login_banner_disable', (YLeaf(YType.boolean, 'sysadmin-login-banner-disable'), ['bool'])),
            ])
            self.sysadmin_login_banner_disable = None
            self._segment_path = lambda: "sysadmin-login-banner"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.SysadminLoginBanner, ['sysadmin_login_banner_disable'], name, value)


    class InterfaceDisplay(Entity):
        """
        Configure the Interface display order
        
        .. attribute:: slot_order
        
        	Configure Interface display order as slot order
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.InterfaceDisplay, self).__init__()

            self.yang_name = "interface-display"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('slot_order', (YLeaf(YType.boolean, 'slot-order'), ['bool'])),
            ])
            self.slot_order = None
            self._segment_path = lambda: "interface-display"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.InterfaceDisplay, ['slot_order'], name, value)


    class NetmaskFormat(Entity):
        """
        Ipv4 netmask\-format to be configured
        
        .. attribute:: bit_count
        
        	Enable ipv4 netmask\-format as bit\-count
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.NetmaskFormat, self).__init__()

            self.yang_name = "netmask-format"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('bit_count', (YLeaf(YType.boolean, 'bit-count'), ['bool'])),
            ])
            self.bit_count = None
            self._segment_path = lambda: "netmask-format"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.NetmaskFormat, ['bit_count'], name, value)


    class Configuration(Entity):
        """
        cli configuration services
        
        .. attribute:: disable
        
        	disable for read\-only access users
        	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Configuration.Disable>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Configuration, self).__init__()

            self.yang_name = "configuration"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("disable", ("disable", Parser.Configuration.Disable))])
            self._leafs = OrderedDict()

            self.disable = Parser.Configuration.Disable()
            self.disable.parent = self
            self._children_name_map["disable"] = "disable"
            self._segment_path = lambda: "configuration"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.Configuration, [], name, value)


        class Disable(Entity):
            """
            disable for read\-only access users
            
            .. attribute:: usergroup
            
            	Disable config mode for usergroup
            	**type**\: str
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Configuration.Disable, self).__init__()

                self.yang_name = "disable"
                self.yang_parent_name = "configuration"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('usergroup', (YLeaf(YType.str, 'usergroup'), ['str'])),
                ])
                self.usergroup = None
                self._segment_path = lambda: "disable"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/configuration/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Configuration.Disable, ['usergroup'], name, value)


    class SubmodeExit(Entity):
        """
        Exit submode when only '!' seen in interactive
        mode
        
        .. attribute:: enable
        
        	Enable the feature
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.SubmodeExit, self).__init__()

            self.yang_name = "submode-exit"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
            ])
            self.enable = None
            self._segment_path = lambda: "submode-exit"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.SubmodeExit, ['enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Parser()
        return self._top_entity

