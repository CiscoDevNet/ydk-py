""" Cisco_IOS_XR_parser_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR parser package configuration.

This module contains definitions
for the following management objects\:
  parser\: Parser configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2015-06-02'

    def __init__(self):
        super(Parser, self).__init__()
        self._top_entity = None

        self.yang_name = "parser"
        self.yang_parent_name = "Cisco-IOS-XR-parser-cfg"

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


    class Indentation(Entity):
        """
        indentation tracking
        
        .. attribute:: indentation_disable
        
        	disable the indentation
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.Indentation, self).__init__()

            self.yang_name = "indentation"
            self.yang_parent_name = "parser"

            self.indentation_disable = YLeaf(YType.boolean, "indentation-disable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("indentation_disable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Parser.Indentation, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Parser.Indentation, self).__setattr__(name, value)

        def has_data(self):
            return self.indentation_disable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.indentation_disable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "indentation" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.indentation_disable.is_set or self.indentation_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.indentation_disable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "indentation-disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "indentation-disable"):
                self.indentation_disable = value
                self.indentation_disable.value_namespace = name_space
                self.indentation_disable.value_namespace_prefix = name_space_prefix


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
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.Alias, self).__init__()

            self.yang_name = "alias"
            self.yang_parent_name = "parser"

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


        class Execs(Entity):
            """
            Exec command alias
            
            .. attribute:: exec_
            
            	Exec alias name
            	**type**\: list of    :py:class:`Exec_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs.Exec_>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                super(Parser.Alias.Execs, self).__init__()

                self.yang_name = "execs"
                self.yang_parent_name = "alias"

                self.exec_ = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Parser.Alias.Execs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Parser.Alias.Execs, self).__setattr__(name, value)


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
                _revision = '2015-06-02'

                def __init__(self):
                    super(Parser.Alias.Execs.Exec_, self).__init__()

                    self.yang_name = "exec"
                    self.yang_parent_name = "execs"

                    self.identifier = YLeaf(YType.str, "identifier")

                    self.identifier_xr = YLeaf(YType.str, "identifier-xr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("identifier",
                                    "identifier_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Parser.Alias.Execs.Exec_, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Parser.Alias.Execs.Exec_, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.identifier.is_set or
                        self.identifier_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.identifier.yfilter != YFilter.not_set or
                        self.identifier_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "exec" + "[identifier='" + self.identifier.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-parser-cfg:parser/alias/execs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.identifier.is_set or self.identifier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.identifier.get_name_leafdata())
                    if (self.identifier_xr.is_set or self.identifier_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.identifier_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "identifier" or name == "identifier-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "identifier"):
                        self.identifier = value
                        self.identifier.value_namespace = name_space
                        self.identifier.value_namespace_prefix = name_space_prefix
                    if(value_path == "identifier-xr"):
                        self.identifier_xr = value
                        self.identifier_xr.value_namespace = name_space
                        self.identifier_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.exec_:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.exec_:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "execs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "exec"):
                    for c in self.exec_:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Parser.Alias.Execs.Exec_()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.exec_.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "exec"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Configurations(Entity):
            """
            Configuration command alias
            
            .. attribute:: configuration
            
            	Configuration Alias name
            	**type**\: list of    :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations.Configuration>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                super(Parser.Alias.Configurations, self).__init__()

                self.yang_name = "configurations"
                self.yang_parent_name = "alias"

                self.configuration = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Parser.Alias.Configurations, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Parser.Alias.Configurations, self).__setattr__(name, value)


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
                _revision = '2015-06-02'

                def __init__(self):
                    super(Parser.Alias.Configurations.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "configurations"

                    self.identifier = YLeaf(YType.str, "identifier")

                    self.identifier_xr = YLeaf(YType.str, "identifier-xr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("identifier",
                                    "identifier_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Parser.Alias.Configurations.Configuration, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Parser.Alias.Configurations.Configuration, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.identifier.is_set or
                        self.identifier_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.identifier.yfilter != YFilter.not_set or
                        self.identifier_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configuration" + "[identifier='" + self.identifier.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-parser-cfg:parser/alias/configurations/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.identifier.is_set or self.identifier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.identifier.get_name_leafdata())
                    if (self.identifier_xr.is_set or self.identifier_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.identifier_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "identifier" or name == "identifier-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "identifier"):
                        self.identifier = value
                        self.identifier.value_namespace = name_space
                        self.identifier.value_namespace_prefix = name_space_prefix
                    if(value_path == "identifier-xr"):
                        self.identifier_xr = value
                        self.identifier_xr.value_namespace = name_space
                        self.identifier_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.configuration:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.configuration:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "configurations" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "configuration"):
                    for c in self.configuration:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Parser.Alias.Configurations.Configuration()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.configuration.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configuration"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Alls(Entity):
            """
            Table of all aliases configured
            
            .. attribute:: all
            
            	Alias name to command mapping
            	**type**\: list of    :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls.All>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                super(Parser.Alias.Alls, self).__init__()

                self.yang_name = "alls"
                self.yang_parent_name = "alias"

                self.all = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Parser.Alias.Alls, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Parser.Alias.Alls, self).__setattr__(name, value)


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
                _revision = '2015-06-02'

                def __init__(self):
                    super(Parser.Alias.Alls.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "alls"

                    self.identifier = YLeaf(YType.str, "identifier")

                    self.identifier_xr = YLeaf(YType.str, "identifier-xr")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("identifier",
                                    "identifier_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Parser.Alias.Alls.All, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Parser.Alias.Alls.All, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.identifier.is_set or
                        self.identifier_xr.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.identifier.yfilter != YFilter.not_set or
                        self.identifier_xr.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "all" + "[identifier='" + self.identifier.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-parser-cfg:parser/alias/alls/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.identifier.is_set or self.identifier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.identifier.get_name_leafdata())
                    if (self.identifier_xr.is_set or self.identifier_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.identifier_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "identifier" or name == "identifier-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "identifier"):
                        self.identifier = value
                        self.identifier.value_namespace = name_space
                        self.identifier.value_namespace_prefix = name_space_prefix
                    if(value_path == "identifier-xr"):
                        self.identifier_xr = value
                        self.identifier_xr.value_namespace = name_space
                        self.identifier_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.all:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.all:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "alls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-parser-cfg:parser/alias/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "all"):
                    for c in self.all:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Parser.Alias.Alls.All()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.all.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "all"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.alls is not None and self.alls.has_data()) or
                (self.configurations is not None and self.configurations.has_data()) or
                (self.execs is not None and self.execs.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.alls is not None and self.alls.has_operation()) or
                (self.configurations is not None and self.configurations.has_operation()) or
                (self.execs is not None and self.execs.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "alias" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "alls"):
                if (self.alls is None):
                    self.alls = Parser.Alias.Alls()
                    self.alls.parent = self
                    self._children_name_map["alls"] = "alls"
                return self.alls

            if (child_yang_name == "configurations"):
                if (self.configurations is None):
                    self.configurations = Parser.Alias.Configurations()
                    self.configurations.parent = self
                    self._children_name_map["configurations"] = "configurations"
                return self.configurations

            if (child_yang_name == "execs"):
                if (self.execs is None):
                    self.execs = Parser.Alias.Execs()
                    self.execs.parent = self
                    self._children_name_map["execs"] = "execs"
                return self.execs

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "alls" or name == "configurations" or name == "execs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class History(Entity):
        """
        cli commands history
        
        .. attribute:: size
        
        	maximum number of commands in history
        	**type**\:  int
        
        	**range:** 1000..5000
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.History, self).__init__()

            self.yang_name = "history"
            self.yang_parent_name = "parser"

            self.size = YLeaf(YType.uint32, "size")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("size") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Parser.History, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Parser.History, self).__setattr__(name, value)

        def has_data(self):
            return self.size.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.size.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "history" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.size.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "size"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "size"):
                self.size = value
                self.size.value_namespace = name_space
                self.size.value_namespace_prefix = name_space_prefix


    class InterfaceDisplay(Entity):
        """
        Configure the Interface display order
        
        .. attribute:: slot_order
        
        	Configure Interface display order as slot order
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.InterfaceDisplay, self).__init__()

            self.yang_name = "interface-display"
            self.yang_parent_name = "parser"

            self.slot_order = YLeaf(YType.boolean, "slot-order")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("slot_order") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Parser.InterfaceDisplay, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Parser.InterfaceDisplay, self).__setattr__(name, value)

        def has_data(self):
            return self.slot_order.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.slot_order.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface-display" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.slot_order.is_set or self.slot_order.yfilter != YFilter.not_set):
                leaf_name_data.append(self.slot_order.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "slot-order"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "slot-order"):
                self.slot_order = value
                self.slot_order.value_namespace = name_space
                self.slot_order.value_namespace_prefix = name_space_prefix


    class NetmaskFormat(Entity):
        """
        Ipv4 netmask\-format to be configured
        
        .. attribute:: bit_count
        
        	Enable ipv4 netmask\-format as bit\-count
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.NetmaskFormat, self).__init__()

            self.yang_name = "netmask-format"
            self.yang_parent_name = "parser"

            self.bit_count = YLeaf(YType.boolean, "bit-count")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bit_count") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Parser.NetmaskFormat, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Parser.NetmaskFormat, self).__setattr__(name, value)

        def has_data(self):
            return self.bit_count.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bit_count.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "netmask-format" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bit_count.is_set or self.bit_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bit_count.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bit-count"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bit-count"):
                self.bit_count = value
                self.bit_count.value_namespace = name_space
                self.bit_count.value_namespace_prefix = name_space_prefix


    class Configuration(Entity):
        """
        cli configuration services
        
        .. attribute:: disable
        
        	disable for read\-only access users
        	**type**\:   :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg.Parser.Configuration.Disable>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.Configuration, self).__init__()

            self.yang_name = "configuration"
            self.yang_parent_name = "parser"

            self.disable = Parser.Configuration.Disable()
            self.disable.parent = self
            self._children_name_map["disable"] = "disable"
            self._children_yang_names.add("disable")


        class Disable(Entity):
            """
            disable for read\-only access users
            
            .. attribute:: usergroup
            
            	Disable config mode for usergroup
            	**type**\:  str
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                super(Parser.Configuration.Disable, self).__init__()

                self.yang_name = "disable"
                self.yang_parent_name = "configuration"

                self.usergroup = YLeaf(YType.str, "usergroup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("usergroup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Parser.Configuration.Disable, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Parser.Configuration.Disable, self).__setattr__(name, value)

            def has_data(self):
                return self.usergroup.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.usergroup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "disable" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-parser-cfg:parser/configuration/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.usergroup.is_set or self.usergroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.usergroup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "usergroup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "usergroup"):
                    self.usergroup = value
                    self.usergroup.value_namespace = name_space
                    self.usergroup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.disable is not None and self.disable.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.disable is not None and self.disable.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "configuration" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "disable"):
                if (self.disable is None):
                    self.disable = Parser.Configuration.Disable()
                    self.disable.parent = self
                    self._children_name_map["disable"] = "disable"
                return self.disable

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SubmodeExit(Entity):
        """
        Exit submode when only '!' seen in interactive
        mode
        
        .. attribute:: enable
        
        	Enable the feature
        	**type**\:  bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            super(Parser.SubmodeExit, self).__init__()

            self.yang_name = "submode-exit"
            self.yang_parent_name = "parser"

            self.enable = YLeaf(YType.boolean, "enable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Parser.SubmodeExit, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Parser.SubmodeExit, self).__setattr__(name, value)

        def has_data(self):
            return self.enable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "submode-exit" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-parser-cfg:parser/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.alias is not None and self.alias.has_data()) or
            (self.configuration is not None and self.configuration.has_data()) or
            (self.history is not None and self.history.has_data()) or
            (self.indentation is not None and self.indentation.has_data()) or
            (self.interface_display is not None and self.interface_display.has_data()) or
            (self.netmask_format is not None and self.netmask_format.has_data()) or
            (self.submode_exit is not None and self.submode_exit.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.alias is not None and self.alias.has_operation()) or
            (self.configuration is not None and self.configuration.has_operation()) or
            (self.history is not None and self.history.has_operation()) or
            (self.indentation is not None and self.indentation.has_operation()) or
            (self.interface_display is not None and self.interface_display.has_operation()) or
            (self.netmask_format is not None and self.netmask_format.has_operation()) or
            (self.submode_exit is not None and self.submode_exit.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-parser-cfg:parser" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "alias"):
            if (self.alias is None):
                self.alias = Parser.Alias()
                self.alias.parent = self
                self._children_name_map["alias"] = "alias"
            return self.alias

        if (child_yang_name == "configuration"):
            if (self.configuration is None):
                self.configuration = Parser.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
            return self.configuration

        if (child_yang_name == "history"):
            if (self.history is None):
                self.history = Parser.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"
            return self.history

        if (child_yang_name == "indentation"):
            if (self.indentation is None):
                self.indentation = Parser.Indentation()
                self.indentation.parent = self
                self._children_name_map["indentation"] = "indentation"
            return self.indentation

        if (child_yang_name == "interface-display"):
            if (self.interface_display is None):
                self.interface_display = Parser.InterfaceDisplay()
                self.interface_display.parent = self
                self._children_name_map["interface_display"] = "interface-display"
            return self.interface_display

        if (child_yang_name == "netmask-format"):
            if (self.netmask_format is None):
                self.netmask_format = Parser.NetmaskFormat()
                self.netmask_format.parent = self
                self._children_name_map["netmask_format"] = "netmask-format"
            return self.netmask_format

        if (child_yang_name == "submode-exit"):
            if (self.submode_exit is None):
                self.submode_exit = Parser.SubmodeExit()
                self.submode_exit.parent = self
                self._children_name_map["submode_exit"] = "submode-exit"
            return self.submode_exit

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "alias" or name == "configuration" or name == "history" or name == "indentation" or name == "interface-display" or name == "netmask-format" or name == "submode-exit"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Parser()
        return self._top_entity

