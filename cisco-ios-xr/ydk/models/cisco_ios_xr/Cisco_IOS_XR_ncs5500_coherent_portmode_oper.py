""" Cisco_IOS_XR_ncs5500_coherent_portmode_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-portmode package operational data.

This module contains definitions
for the following management objects\:
  controller\-port\-mode\: Coherent PortMode  operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ControllerPortMode(Entity):
    """
    Coherent PortMode  operational data
    
    .. attribute:: optics_name
    
    	Name of optics controller
    	**type**\: list of    :py:class:`OpticsName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper.ControllerPortMode.OpticsName>`
    
    

    """

    _prefix = 'ncs5500-coherent-portmode-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ControllerPortMode, self).__init__()
        self._top_entity = None

        self.yang_name = "controller-port-mode"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5500-coherent-portmode-oper"

        self.optics_name = YList(self)

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
                    super(ControllerPortMode, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(ControllerPortMode, self).__setattr__(name, value)


    class OpticsName(Entity):
        """
        Name of optics controller
        
        .. attribute:: interface_name  <key>
        
        	Interface Name
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: port_mode_info
        
        	PortMode  operational data
        	**type**\:   :py:class:`PortModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper.ControllerPortMode.OpticsName.PortModeInfo>`
        
        

        """

        _prefix = 'ncs5500-coherent-portmode-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ControllerPortMode.OpticsName, self).__init__()

            self.yang_name = "optics-name"
            self.yang_parent_name = "controller-port-mode"

            self.interface_name = YLeaf(YType.str, "interface-name")

            self.port_mode_info = ControllerPortMode.OpticsName.PortModeInfo()
            self.port_mode_info.parent = self
            self._children_name_map["port_mode_info"] = "port-mode-info"
            self._children_yang_names.add("port-mode-info")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("interface_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ControllerPortMode.OpticsName, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ControllerPortMode.OpticsName, self).__setattr__(name, value)


        class PortModeInfo(Entity):
            """
            PortMode  operational data
            
            .. attribute:: diff
            
            	diff
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: fec
            
            	fec
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: intf_name
            
            	intf name
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: modulation
            
            	modulation
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: speed
            
            	speed
            	**type**\:  str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'ncs5500-coherent-portmode-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ControllerPortMode.OpticsName.PortModeInfo, self).__init__()

                self.yang_name = "port-mode-info"
                self.yang_parent_name = "optics-name"

                self.diff = YLeaf(YType.str, "diff")

                self.fec = YLeaf(YType.str, "fec")

                self.intf_name = YLeaf(YType.str, "intf-name")

                self.modulation = YLeaf(YType.str, "modulation")

                self.speed = YLeaf(YType.str, "speed")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("diff",
                                "fec",
                                "intf_name",
                                "modulation",
                                "speed") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ControllerPortMode.OpticsName.PortModeInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ControllerPortMode.OpticsName.PortModeInfo, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.diff.is_set or
                    self.fec.is_set or
                    self.intf_name.is_set or
                    self.modulation.is_set or
                    self.speed.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.diff.yfilter != YFilter.not_set or
                    self.fec.yfilter != YFilter.not_set or
                    self.intf_name.yfilter != YFilter.not_set or
                    self.modulation.yfilter != YFilter.not_set or
                    self.speed.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "port-mode-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.diff.is_set or self.diff.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.diff.get_name_leafdata())
                if (self.fec.is_set or self.fec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fec.get_name_leafdata())
                if (self.intf_name.is_set or self.intf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intf_name.get_name_leafdata())
                if (self.modulation.is_set or self.modulation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.modulation.get_name_leafdata())
                if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.speed.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diff" or name == "fec" or name == "intf-name" or name == "modulation" or name == "speed"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "diff"):
                    self.diff = value
                    self.diff.value_namespace = name_space
                    self.diff.value_namespace_prefix = name_space_prefix
                if(value_path == "fec"):
                    self.fec = value
                    self.fec.value_namespace = name_space
                    self.fec.value_namespace_prefix = name_space_prefix
                if(value_path == "intf-name"):
                    self.intf_name = value
                    self.intf_name.value_namespace = name_space
                    self.intf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "modulation"):
                    self.modulation = value
                    self.modulation.value_namespace = name_space
                    self.modulation.value_namespace_prefix = name_space_prefix
                if(value_path == "speed"):
                    self.speed = value
                    self.speed.value_namespace = name_space
                    self.speed.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.interface_name.is_set or
                (self.port_mode_info is not None and self.port_mode_info.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.interface_name.yfilter != YFilter.not_set or
                (self.port_mode_info is not None and self.port_mode_info.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "optics-name" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ncs5500-coherent-portmode-oper:controller-port-mode/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "port-mode-info"):
                if (self.port_mode_info is None):
                    self.port_mode_info = ControllerPortMode.OpticsName.PortModeInfo()
                    self.port_mode_info.parent = self
                    self._children_name_map["port_mode_info"] = "port-mode-info"
                return self.port_mode_info

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "port-mode-info" or name == "interface-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "interface-name"):
                self.interface_name = value
                self.interface_name.value_namespace = name_space
                self.interface_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.optics_name:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.optics_name:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ncs5500-coherent-portmode-oper:controller-port-mode" + path_buffer

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

        if (child_yang_name == "optics-name"):
            for c in self.optics_name:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = ControllerPortMode.OpticsName()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.optics_name.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "optics-name"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ControllerPortMode()
        return self._top_entity

