""" Cisco_IOS_XR_ethernet_lldp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-lldp package configuration.

This module contains definitions
for the following management objects\:
  lldp\: Enable LLDP, or configure global LLDP subcommands

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Lldp(Entity):
    """
    Enable LLDP, or configure global LLDP subcommands
    
    .. attribute:: enable
    
    	Enable or disable LLDP globally
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: enable_subintf
    
    	Enable or disable LLDP on Sub\-interfaces as well globally
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: extended_show_width
    
    	Enable or disable LLDP Show LLDP Neighbor Extended Width
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: holdtime
    
    	Length  of time  (in sec) that receiver must keep this packet
    	**type**\:  int
    
    	**range:** 0..65535
    
    .. attribute:: reinit
    
    	Delay (in sec) for LLDP initialization on any interface
    	**type**\:  int
    
    	**range:** 2..5
    
    	**default value**\: 2
    
    .. attribute:: timer
    
    	Specify the rate at which LLDP packets are sent (in sec)
    	**type**\:  int
    
    	**range:** 5..65534
    
    	**default value**\: 30
    
    .. attribute:: tlv_select
    
    	Selection of LLDP TLVs to disable
    	**type**\:   :py:class:`TlvSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ethernet-lldp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lldp, self).__init__()
        self._top_entity = None

        self.yang_name = "lldp"
        self.yang_parent_name = "Cisco-IOS-XR-ethernet-lldp-cfg"

        self.enable = YLeaf(YType.boolean, "enable")

        self.enable_subintf = YLeaf(YType.boolean, "enable-subintf")

        self.extended_show_width = YLeaf(YType.boolean, "extended-show-width")

        self.holdtime = YLeaf(YType.uint32, "holdtime")

        self.reinit = YLeaf(YType.uint32, "reinit")

        self.timer = YLeaf(YType.uint32, "timer")

        self.tlv_select = None
        self._children_name_map["tlv_select"] = "tlv-select"
        self._children_yang_names.add("tlv-select")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable",
                        "enable_subintf",
                        "extended_show_width",
                        "holdtime",
                        "reinit",
                        "timer") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Lldp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Lldp, self).__setattr__(name, value)


    class TlvSelect(Entity):
        """
        Selection of LLDP TLVs to disable
        
        .. attribute:: management_address
        
        	Management Address TLV
        	**type**\:   :py:class:`ManagementAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.ManagementAddress>`
        
        .. attribute:: port_description
        
        	Port Description TLV
        	**type**\:   :py:class:`PortDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.PortDescription>`
        
        .. attribute:: system_capabilities
        
        	System Capabilities TLV
        	**type**\:   :py:class:`SystemCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemCapabilities>`
        
        .. attribute:: system_description
        
        	System Description TLV
        	**type**\:   :py:class:`SystemDescription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemDescription>`
        
        .. attribute:: system_name
        
        	System Name TLV
        	**type**\:   :py:class:`SystemName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg.Lldp.TlvSelect.SystemName>`
        
        .. attribute:: tlv_select_enter
        
        	enter lldp tlv\-select submode
        	**type**\:  bool
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ethernet-lldp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lldp.TlvSelect, self).__init__()

            self.yang_name = "tlv-select"
            self.yang_parent_name = "lldp"
            self.is_presence_container = True

            self.tlv_select_enter = YLeaf(YType.boolean, "tlv-select-enter")

            self.management_address = Lldp.TlvSelect.ManagementAddress()
            self.management_address.parent = self
            self._children_name_map["management_address"] = "management-address"
            self._children_yang_names.add("management-address")

            self.port_description = Lldp.TlvSelect.PortDescription()
            self.port_description.parent = self
            self._children_name_map["port_description"] = "port-description"
            self._children_yang_names.add("port-description")

            self.system_capabilities = Lldp.TlvSelect.SystemCapabilities()
            self.system_capabilities.parent = self
            self._children_name_map["system_capabilities"] = "system-capabilities"
            self._children_yang_names.add("system-capabilities")

            self.system_description = Lldp.TlvSelect.SystemDescription()
            self.system_description.parent = self
            self._children_name_map["system_description"] = "system-description"
            self._children_yang_names.add("system-description")

            self.system_name = Lldp.TlvSelect.SystemName()
            self.system_name.parent = self
            self._children_name_map["system_name"] = "system-name"
            self._children_yang_names.add("system-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("tlv_select_enter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Lldp.TlvSelect, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Lldp.TlvSelect, self).__setattr__(name, value)


        class SystemName(Entity):
            """
            System Name TLV
            
            .. attribute:: disable
            
            	disable System Name TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.TlvSelect.SystemName, self).__init__()

                self.yang_name = "system-name"
                self.yang_parent_name = "tlv-select"

                self.disable = YLeaf(YType.boolean, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.TlvSelect.SystemName, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.TlvSelect.SystemName, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-name" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix


        class PortDescription(Entity):
            """
            Port Description TLV
            
            .. attribute:: disable
            
            	disable Port Description TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.TlvSelect.PortDescription, self).__init__()

                self.yang_name = "port-description"
                self.yang_parent_name = "tlv-select"

                self.disable = YLeaf(YType.boolean, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.TlvSelect.PortDescription, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.TlvSelect.PortDescription, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "port-description" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix


        class SystemDescription(Entity):
            """
            System Description TLV
            
            .. attribute:: disable
            
            	disable System Description TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.TlvSelect.SystemDescription, self).__init__()

                self.yang_name = "system-description"
                self.yang_parent_name = "tlv-select"

                self.disable = YLeaf(YType.boolean, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.TlvSelect.SystemDescription, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.TlvSelect.SystemDescription, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-description" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix


        class SystemCapabilities(Entity):
            """
            System Capabilities TLV
            
            .. attribute:: disable
            
            	disable System Capabilities TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.TlvSelect.SystemCapabilities, self).__init__()

                self.yang_name = "system-capabilities"
                self.yang_parent_name = "tlv-select"

                self.disable = YLeaf(YType.boolean, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.TlvSelect.SystemCapabilities, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.TlvSelect.SystemCapabilities, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "system-capabilities" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix


        class ManagementAddress(Entity):
            """
            Management Address TLV
            
            .. attribute:: disable
            
            	disable Management Address TLV
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'ethernet-lldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lldp.TlvSelect.ManagementAddress, self).__init__()

                self.yang_name = "management-address"
                self.yang_parent_name = "tlv-select"

                self.disable = YLeaf(YType.boolean, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Lldp.TlvSelect.ManagementAddress, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Lldp.TlvSelect.ManagementAddress, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "management-address" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/tlv-select/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.tlv_select_enter.is_set or
                (self.management_address is not None and self.management_address.has_data()) or
                (self.port_description is not None and self.port_description.has_data()) or
                (self.system_capabilities is not None and self.system_capabilities.has_data()) or
                (self.system_description is not None and self.system_description.has_data()) or
                (self.system_name is not None and self.system_name.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.tlv_select_enter.yfilter != YFilter.not_set or
                (self.management_address is not None and self.management_address.has_operation()) or
                (self.port_description is not None and self.port_description.has_operation()) or
                (self.system_capabilities is not None and self.system_capabilities.has_operation()) or
                (self.system_description is not None and self.system_description.has_operation()) or
                (self.system_name is not None and self.system_name.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tlv-select" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.tlv_select_enter.is_set or self.tlv_select_enter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tlv_select_enter.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "management-address"):
                if (self.management_address is None):
                    self.management_address = Lldp.TlvSelect.ManagementAddress()
                    self.management_address.parent = self
                    self._children_name_map["management_address"] = "management-address"
                return self.management_address

            if (child_yang_name == "port-description"):
                if (self.port_description is None):
                    self.port_description = Lldp.TlvSelect.PortDescription()
                    self.port_description.parent = self
                    self._children_name_map["port_description"] = "port-description"
                return self.port_description

            if (child_yang_name == "system-capabilities"):
                if (self.system_capabilities is None):
                    self.system_capabilities = Lldp.TlvSelect.SystemCapabilities()
                    self.system_capabilities.parent = self
                    self._children_name_map["system_capabilities"] = "system-capabilities"
                return self.system_capabilities

            if (child_yang_name == "system-description"):
                if (self.system_description is None):
                    self.system_description = Lldp.TlvSelect.SystemDescription()
                    self.system_description.parent = self
                    self._children_name_map["system_description"] = "system-description"
                return self.system_description

            if (child_yang_name == "system-name"):
                if (self.system_name is None):
                    self.system_name = Lldp.TlvSelect.SystemName()
                    self.system_name.parent = self
                    self._children_name_map["system_name"] = "system-name"
                return self.system_name

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "management-address" or name == "port-description" or name == "system-capabilities" or name == "system-description" or name == "system-name" or name == "tlv-select-enter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "tlv-select-enter"):
                self.tlv_select_enter = value
                self.tlv_select_enter.value_namespace = name_space
                self.tlv_select_enter.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.enable.is_set or
            self.enable_subintf.is_set or
            self.extended_show_width.is_set or
            self.holdtime.is_set or
            self.reinit.is_set or
            self.timer.is_set or
            (self.tlv_select is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.enable_subintf.yfilter != YFilter.not_set or
            self.extended_show_width.yfilter != YFilter.not_set or
            self.holdtime.yfilter != YFilter.not_set or
            self.reinit.yfilter != YFilter.not_set or
            self.timer.yfilter != YFilter.not_set or
            (self.tlv_select is not None and self.tlv_select.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ethernet-lldp-cfg:lldp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.enable_subintf.is_set or self.enable_subintf.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable_subintf.get_name_leafdata())
        if (self.extended_show_width.is_set or self.extended_show_width.yfilter != YFilter.not_set):
            leaf_name_data.append(self.extended_show_width.get_name_leafdata())
        if (self.holdtime.is_set or self.holdtime.yfilter != YFilter.not_set):
            leaf_name_data.append(self.holdtime.get_name_leafdata())
        if (self.reinit.is_set or self.reinit.yfilter != YFilter.not_set):
            leaf_name_data.append(self.reinit.get_name_leafdata())
        if (self.timer.is_set or self.timer.yfilter != YFilter.not_set):
            leaf_name_data.append(self.timer.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "tlv-select"):
            if (self.tlv_select is None):
                self.tlv_select = Lldp.TlvSelect()
                self.tlv_select.parent = self
                self._children_name_map["tlv_select"] = "tlv-select"
            return self.tlv_select

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "tlv-select" or name == "enable" or name == "enable-subintf" or name == "extended-show-width" or name == "holdtime" or name == "reinit" or name == "timer"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "enable-subintf"):
            self.enable_subintf = value
            self.enable_subintf.value_namespace = name_space
            self.enable_subintf.value_namespace_prefix = name_space_prefix
        if(value_path == "extended-show-width"):
            self.extended_show_width = value
            self.extended_show_width.value_namespace = name_space
            self.extended_show_width.value_namespace_prefix = name_space_prefix
        if(value_path == "holdtime"):
            self.holdtime = value
            self.holdtime.value_namespace = name_space
            self.holdtime.value_namespace_prefix = name_space_prefix
        if(value_path == "reinit"):
            self.reinit = value
            self.reinit.value_namespace = name_space
            self.reinit.value_namespace_prefix = name_space_prefix
        if(value_path == "timer"):
            self.timer = value
            self.timer.value_namespace = name_space
            self.timer.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Lldp()
        return self._top_entity

