""" Cisco_IOS_XR_parser_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR parser package configuration.

This module contains definitions
for the following management objects\:
  parser\: Parser configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Parser(Entity):
    """
    Parser configuration
    
    .. attribute:: alias
    
    	Alias for command mapping
    	**type**\:   :py:class:`Alias <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias>`
    
    .. attribute:: configuration
    
    	cli configuration services
    	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Configuration>`
    
    .. attribute:: history
    
    	cli commands history
    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.History>`
    
    .. attribute:: indentation
    
    	indentation tracking
    	**type**\:   :py:class:`Indentation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Indentation>`
    
    .. attribute:: interactive
    
    	interactive mode
    	**type**\:   :py:class:`Interactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Interactive>`
    
    .. attribute:: interface_display
    
    	Configure the Interface display order
    	**type**\:   :py:class:`InterfaceDisplay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.InterfaceDisplay>`
    
    .. attribute:: netmask_format
    
    	Ipv4 netmask\-format to be configured
    	**type**\:   :py:class:`NetmaskFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.NetmaskFormat>`
    
    .. attribute:: submode_exit
    
    	Exit submode when only '!' seen in interactive mode
    	**type**\:   :py:class:`SubmodeExit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.SubmodeExit>`
    
    

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
        self._child_container_classes = {"alias" : ("alias", Parser.Alias), "configuration" : ("configuration", Parser.Configuration), "history" : ("history", Parser.History), "indentation" : ("indentation", Parser.Indentation), "interactive" : ("interactive", Parser.Interactive), "interface-display" : ("interface_display", Parser.InterfaceDisplay), "netmask-format" : ("netmask_format", Parser.NetmaskFormat), "submode-exit" : ("submode_exit", Parser.SubmodeExit)}
        self._child_list_classes = {}

        self.alias = Parser.Alias()
        self.alias.parent = self
        self._children_name_map["alias"] = "alias"
        self._children_yang_names.add("alias")

        self.configuration = Parser.Configuration()
        self.configuration.parent = self
        self._children_name_map["configuration"] = "configuration"
        self._children_yang_names.add("configuration")

        self.history = Parser.History()
        self.history.parent = self
        self._children_name_map["history"] = "history"
        self._children_yang_names.add("history")

        self.indentation = Parser.Indentation()
        self.indentation.parent = self
        self._children_name_map["indentation"] = "indentation"
        self._children_yang_names.add("indentation")

        self.interactive = Parser.Interactive()
        self.interactive.parent = self
        self._children_name_map["interactive"] = "interactive"
        self._children_yang_names.add("interactive")

        self.interface_display = Parser.InterfaceDisplay()
        self.interface_display.parent = self
        self._children_name_map["interface_display"] = "interface-display"
        self._children_yang_names.add("interface-display")

        self.netmask_format = Parser.NetmaskFormat()
        self.netmask_format.parent = self
        self._children_name_map["netmask_format"] = "netmask-format"
        self._children_yang_names.add("netmask-format")

        self.submode_exit = Parser.SubmodeExit()
        self.submode_exit.parent = self
        self._children_name_map["submode_exit"] = "submode-exit"
        self._children_yang_names.add("submode-exit")
        self._segment_path = lambda: "Cisco-IOS-XR-parser-cfg:parser"


    class Alias(Entity):
        """
        Alias for command mapping
        
        .. attribute:: alls
        
        	Table of all aliases configured
        	**type**\:   :py:class:`Alls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls>`
        
        .. attribute:: configurations
        
        	Configuration command alias
        	**type**\:   :py:class:`Configurations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations>`
        
        .. attribute:: execs
        
        	Exec command alias
        	**type**\:   :py:class:`Execs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Alias, self).__init__()

            self.yang_name = "alias"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"alls" : ("alls", Parser.Alias.Alls), "configurations" : ("configurations", Parser.Alias.Configurations), "execs" : ("execs", Parser.Alias.Execs)}
            self._child_list_classes = {}

            self.alls = Parser.Alias.Alls()
            self.alls.parent = self
            self._children_name_map["alls"] = "alls"
            self._children_yang_names.add("alls")

            self.configurations = Parser.Alias.Configurations()
            self.configurations.parent = self
            self._children_name_map["configurations"] = "configurations"
            self._children_yang_names.add("configurations")

            self.execs = Parser.Alias.Execs()
            self.execs.parent = self
            self._children_name_map["execs"] = "execs"
            self._children_yang_names.add("execs")
            self._segment_path = lambda: "alias"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()


        class Alls(Entity):
            """
            Table of all aliases configured
            
            .. attribute:: all
            
            	Alias name to command mapping
            	**type**\: list of    :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls.All>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Alias.Alls, self).__init__()

                self.yang_name = "alls"
                self.yang_parent_name = "alias"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"all" : ("all", Parser.Alias.Alls.All)}

                self.all = YList(self)
                self._segment_path = lambda: "alls"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Alias.Alls, [], name, value)


            class All(Entity):
                """
                Alias name to command mapping
                
                .. attribute:: identifier  <key>
                
                	Alias name
                	**type**\:  str
                
                	**length:** 1..30
                
                .. attribute:: identifier_xr
                
                	The actual command
                	**type**\:  str
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.identifier = YLeaf(YType.str, "identifier")

                    self.identifier_xr = YLeaf(YType.str, "identifier-xr")
                    self._segment_path = lambda: "all" + "[identifier='" + self.identifier.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/alls/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Parser.Alias.Alls.All, ['identifier', 'identifier_xr'], name, value)


        class Configurations(Entity):
            """
            Configuration command alias
            
            .. attribute:: configuration
            
            	Configuration Alias name
            	**type**\: list of    :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations.Configuration>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Alias.Configurations, self).__init__()

                self.yang_name = "configurations"
                self.yang_parent_name = "alias"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"configuration" : ("configuration", Parser.Alias.Configurations.Configuration)}

                self.configuration = YList(self)
                self._segment_path = lambda: "configurations"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Alias.Configurations, [], name, value)


            class Configuration(Entity):
                """
                Configuration Alias name
                
                .. attribute:: identifier  <key>
                
                	Configuration alias name
                	**type**\:  str
                
                	**length:** 1..30
                
                .. attribute:: identifier_xr
                
                	Aliased config command
                	**type**\:  str
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.identifier = YLeaf(YType.str, "identifier")

                    self.identifier_xr = YLeaf(YType.str, "identifier-xr")
                    self._segment_path = lambda: "configuration" + "[identifier='" + self.identifier.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/configurations/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Parser.Alias.Configurations.Configuration, ['identifier', 'identifier_xr'], name, value)


        class Execs(Entity):
            """
            Exec command alias
            
            .. attribute:: exec_
            
            	Exec alias name
            	**type**\: list of    :py:class:`Exec_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs.Exec_>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Alias.Execs, self).__init__()

                self.yang_name = "execs"
                self.yang_parent_name = "alias"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"exec" : ("exec_", Parser.Alias.Execs.Exec_)}

                self.exec_ = YList(self)
                self._segment_path = lambda: "execs"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Alias.Execs, [], name, value)


            class Exec_(Entity):
                """
                Exec alias name
                
                .. attribute:: identifier  <key>
                
                	Exec Alias name
                	**type**\:  str
                
                	**length:** 1..30
                
                .. attribute:: identifier_xr
                
                	Aliased exec command
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2017-05-09'

                def __init__(self):
                    super(Parser.Alias.Execs.Exec_, self).__init__()

                    self.yang_name = "exec"
                    self.yang_parent_name = "execs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.identifier = YLeaf(YType.str, "identifier")

                    self.identifier_xr = YLeaf(YType.str, "identifier-xr")
                    self._segment_path = lambda: "exec" + "[identifier='" + self.identifier.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/alias/execs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Parser.Alias.Execs.Exec_, ['identifier', 'identifier_xr'], name, value)


    class Configuration(Entity):
        """
        cli configuration services
        
        .. attribute:: disable
        
        	disable for read\-only access users
        	**type**\:   :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Configuration.Disable>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Configuration, self).__init__()

            self.yang_name = "configuration"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"disable" : ("disable", Parser.Configuration.Disable)}
            self._child_list_classes = {}

            self.disable = Parser.Configuration.Disable()
            self.disable.parent = self
            self._children_name_map["disable"] = "disable"
            self._children_yang_names.add("disable")
            self._segment_path = lambda: "configuration"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()


        class Disable(Entity):
            """
            disable for read\-only access users
            
            .. attribute:: usergroup
            
            	Disable config mode for usergroup
            	**type**\:  str
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2017-05-09'

            def __init__(self):
                super(Parser.Configuration.Disable, self).__init__()

                self.yang_name = "disable"
                self.yang_parent_name = "configuration"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.usergroup = YLeaf(YType.str, "usergroup")
                self._segment_path = lambda: "disable"
                self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/configuration/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Parser.Configuration.Disable, ['usergroup'], name, value)


    class History(Entity):
        """
        cli commands history
        
        .. attribute:: size
        
        	maximum number of commands in history
        	**type**\:  int
        
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.size = YLeaf(YType.uint32, "size")
            self._segment_path = lambda: "history"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.History, ['size'], name, value)


    class Indentation(Entity):
        """
        indentation tracking
        
        .. attribute:: indentation_disable
        
        	disable the indentation
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Indentation, self).__init__()

            self.yang_name = "indentation"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.indentation_disable = YLeaf(YType.boolean, "indentation-disable")
            self._segment_path = lambda: "indentation"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.Indentation, ['indentation_disable'], name, value)


    class Interactive(Entity):
        """
        interactive mode
        
        .. attribute:: interactive_disable
        
        	disable interactive mode
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.Interactive, self).__init__()

            self.yang_name = "interactive"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.interactive_disable = YLeaf(YType.boolean, "interactive-disable")
            self._segment_path = lambda: "interactive"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.Interactive, ['interactive_disable'], name, value)


    class InterfaceDisplay(Entity):
        """
        Configure the Interface display order
        
        .. attribute:: slot_order
        
        	Configure Interface display order as slot order
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.InterfaceDisplay, self).__init__()

            self.yang_name = "interface-display"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.slot_order = YLeaf(YType.boolean, "slot-order")
            self._segment_path = lambda: "interface-display"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.InterfaceDisplay, ['slot_order'], name, value)


    class NetmaskFormat(Entity):
        """
        Ipv4 netmask\-format to be configured
        
        .. attribute:: bit_count
        
        	Enable ipv4 netmask\-format as bit\-count
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.NetmaskFormat, self).__init__()

            self.yang_name = "netmask-format"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.bit_count = YLeaf(YType.boolean, "bit-count")
            self._segment_path = lambda: "netmask-format"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.NetmaskFormat, ['bit_count'], name, value)


    class SubmodeExit(Entity):
        """
        Exit submode when only '!' seen in interactive
        mode
        
        .. attribute:: enable
        
        	Enable the feature
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2017-05-09'

        def __init__(self):
            super(Parser.SubmodeExit, self).__init__()

            self.yang_name = "submode-exit"
            self.yang_parent_name = "parser"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.boolean, "enable")
            self._segment_path = lambda: "submode-exit"
            self._absolute_path = lambda: "Cisco-IOS-XR-parser-cfg:parser/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Parser.SubmodeExit, ['enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Parser()
        return self._top_entity

