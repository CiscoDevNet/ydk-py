""" Cisco_IOS_XR_snmp_test_trap_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SnmpColdStart(Entity):
    """
    Generate SNMPv2\-MIB\:\:coldStart
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(SnmpColdStart, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp-cold-start"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:snmp-cold-start" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SnmpColdStart()
        return self._top_entity

class SnmpWarmStart(Entity):
    """
    Generate SNMPv2\-MIB\:\:warmStart
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(SnmpWarmStart, self).__init__()
        self._top_entity = None

        self.yang_name = "snmp-warm-start"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:snmp-warm-start" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SnmpWarmStart()
        return self._top_entity

class InterfaceLinkUp(Entity):
    """
    Generate IF\-MIB\:\:linkUp
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.InterfaceLinkUp.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InterfaceLinkUp, self).__init__()
        self._top_entity = None

        self.yang_name = "interface-link-up"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = InterfaceLinkUp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate LinkUp trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(InterfaceLinkUp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "interface-link-up"

            self.ifindex = YLeaf(YType.uint32, "ifindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(InterfaceLinkUp.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InterfaceLinkUp.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.ifindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:interface-link-up/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifindex"):
                self.ifindex = value
                self.ifindex.value_namespace = name_space
                self.ifindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:interface-link-up" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = InterfaceLinkUp.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InterfaceLinkUp()
        return self._top_entity

class InterfaceLinkDown(Entity):
    """
    Generate IF\-MIB\:\:linkDown
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.InterfaceLinkDown.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InterfaceLinkDown, self).__init__()
        self._top_entity = None

        self.yang_name = "interface-link-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = InterfaceLinkDown.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate LinkDown trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(InterfaceLinkDown.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "interface-link-down"

            self.ifindex = YLeaf(YType.uint32, "ifindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(InterfaceLinkDown.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InterfaceLinkDown.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.ifindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:interface-link-down/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifindex"):
                self.ifindex = value
                self.ifindex.value_namespace = name_space
                self.ifindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:interface-link-down" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = InterfaceLinkDown.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InterfaceLinkDown()
        return self._top_entity

class SonetSectionStatus(Entity):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetSectionStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetSectionStatus.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(SonetSectionStatus, self).__init__()
        self._top_entity = None

        self.yang_name = "sonet-section-status"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = SonetSectionStatus.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetSectionStatusChange trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(SonetSectionStatus.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sonet-section-status"

            self.ifindex = YLeaf(YType.uint32, "ifindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SonetSectionStatus.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetSectionStatus.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.ifindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:sonet-section-status/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifindex"):
                self.ifindex = value
                self.ifindex.value_namespace = name_space
                self.ifindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:sonet-section-status" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = SonetSectionStatus.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SonetSectionStatus()
        return self._top_entity

class SonetLineStatus(Entity):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetLineStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetLineStatus.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(SonetLineStatus, self).__init__()
        self._top_entity = None

        self.yang_name = "sonet-line-status"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = SonetLineStatus.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetLineStatusChange trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(SonetLineStatus.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sonet-line-status"

            self.ifindex = YLeaf(YType.uint32, "ifindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SonetLineStatus.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetLineStatus.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.ifindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:sonet-line-status/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifindex"):
                self.ifindex = value
                self.ifindex.value_namespace = name_space
                self.ifindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:sonet-line-status" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = SonetLineStatus.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SonetLineStatus()
        return self._top_entity

class SonetPathStatus(Entity):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetPathStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetPathStatus.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(SonetPathStatus, self).__init__()
        self._top_entity = None

        self.yang_name = "sonet-path-status"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = SonetPathStatus.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetPathStatusChange trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(SonetPathStatus.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sonet-path-status"

            self.ifindex = YLeaf(YType.uint32, "ifindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ifindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SonetPathStatus.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SonetPathStatus.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.ifindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ifindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:sonet-path-status/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ifindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ifindex"):
                self.ifindex = value
                self.ifindex.value_namespace = name_space
                self.ifindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:sonet-path-status" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = SonetPathStatus.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SonetPathStatus()
        return self._top_entity

class InfraSyslogMessageGenerated(Entity):
    """
    Generate CISCO\-SYSLOG\-MIB\:\:clogMessageGenerated
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraSyslogMessageGenerated, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-syslog-message-generated"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-syslog-message-generated" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraSyslogMessageGenerated()
        return self._top_entity

class InfraFlashDeviceInserted(Entity):
    """
    Generate CISCO\-FLASH\-MIB\:\:ciscoFlashDeviceInsertedNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraFlashDeviceInserted, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-flash-device-inserted"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-flash-device-inserted" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraFlashDeviceInserted()
        return self._top_entity

class InfraFlashDeviceRemoved(Entity):
    """
    Generate CISCO\-FLASH\-MIB\:\:ciscoFlashDeviceRemovedNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraFlashDeviceRemoved, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-flash-device-removed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-flash-device-removed" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraFlashDeviceRemoved()
        return self._top_entity

class InfraRedundancyProgression(Entity):
    """
    Generate CISCO\-RF\-MIB\:\:ciscoRFProgressionNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraRedundancyProgression, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-redundancy-progression"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-redundancy-progression" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraRedundancyProgression()
        return self._top_entity

class InfraRedundancySwitch(Entity):
    """
    Generate CISCO\-RF\-MIB\:\:ciscoRFSwactNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraRedundancySwitch, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-redundancy-switch"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-redundancy-switch" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraRedundancySwitch()
        return self._top_entity

class InfraBridgeNewRoot(Entity):
    """
    Generate BRIDGE\-MIB\:\:newRoot
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraBridgeNewRoot, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-bridge-new-root"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-bridge-new-root" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraBridgeNewRoot()
        return self._top_entity

class InfraBridgeTopologyChange(Entity):
    """
    Generate BRIDGE\-MIB\:\:topologyChange
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraBridgeTopologyChange, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-bridge-topology-change"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-bridge-topology-change" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraBridgeTopologyChange()
        return self._top_entity

class InfraConfigEvent(Entity):
    """
    Generate CISCO\-CONFIG\-MAN\-MIB\:\:ciscoConfigManEvent
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(InfraConfigEvent, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-config-event"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:infra-config-event" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InfraConfigEvent()
        return self._top_entity

class EntitySensorThresholdNotification(Entity):
    """
    Generate CISCO\-ENTITY\-SENSOR\-MIB\:\:entSensorThresholdNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntitySensorThresholdNotification.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntitySensorThresholdNotification, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-sensor-threshold-notification"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntitySensorThresholdNotification.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntitySensorThresholdNotification.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-sensor-threshold-notification"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntitySensorThresholdNotification.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntitySensorThresholdNotification.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-sensor-threshold-notification/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-sensor-threshold-notification" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntitySensorThresholdNotification.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntitySensorThresholdNotification()
        return self._top_entity

class EntityFruPowerStatusChangeFailed(Entity):
    """
    oper status changed to failed
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruPowerStatusChangeFailed.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntityFruPowerStatusChangeFailed, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-power-status-change-failed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntityFruPowerStatusChangeFailed.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntityFruPowerStatusChangeFailed.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-power-status-change-failed"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityFruPowerStatusChangeFailed.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityFruPowerStatusChangeFailed.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-power-status-change-failed/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-power-status-change-failed" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntityFruPowerStatusChangeFailed.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityFruPowerStatusChangeFailed()
        return self._top_entity

class EntityFruModuleStatusChangeUp(Entity):
    """
    fu trap module status changed as ok
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruModuleStatusChangeUp.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntityFruModuleStatusChangeUp, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-module-status-change-up"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntityFruModuleStatusChangeUp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntityFruModuleStatusChangeUp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-module-status-change-up"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityFruModuleStatusChangeUp.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityFruModuleStatusChangeUp.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-up/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-up" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntityFruModuleStatusChangeUp.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityFruModuleStatusChangeUp()
        return self._top_entity

class EntityFruModuleStatusChangeDown(Entity):
    """
    fu trap module status changed as failed
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruModuleStatusChangeDown.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntityFruModuleStatusChangeDown, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-module-status-change-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntityFruModuleStatusChangeDown.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntityFruModuleStatusChangeDown.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-module-status-change-down"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityFruModuleStatusChangeDown.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityFruModuleStatusChangeDown.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-down/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-down" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntityFruModuleStatusChangeDown.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityFruModuleStatusChangeDown()
        return self._top_entity

class EntityFruFanTrayOperStatusUp(Entity):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFanTrayStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayOperStatusUp.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntityFruFanTrayOperStatusUp, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-fan-tray-oper-status-up"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntityFruFanTrayOperStatusUp.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntityFruFanTrayOperStatusUp.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-fan-tray-oper-status-up"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityFruFanTrayOperStatusUp.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityFruFanTrayOperStatusUp.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-oper-status-up/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-oper-status-up" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntityFruFanTrayOperStatusUp.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityFruFanTrayOperStatusUp()
        return self._top_entity

class EntityFruFanTrayInserted(Entity):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFRUInserted
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayInserted.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntityFruFanTrayInserted, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-fan-tray-inserted"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntityFruFanTrayInserted.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntityFruFanTrayInserted.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-fan-tray-inserted"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityFruFanTrayInserted.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityFruFanTrayInserted.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-inserted/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-inserted" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntityFruFanTrayInserted.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityFruFanTrayInserted()
        return self._top_entity

class EntityFruFanTrayRemoved(Entity):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFRURemoved
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayRemoved.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(EntityFruFanTrayRemoved, self).__init__()
        self._top_entity = None

        self.yang_name = "entity-fru-fan-tray-removed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = EntityFruFanTrayRemoved.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(EntityFruFanTrayRemoved.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "entity-fru-fan-tray-removed"

            self.entindex = YLeaf(YType.uint32, "entindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EntityFruFanTrayRemoved.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntityFruFanTrayRemoved.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.entindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-removed/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entindex.is_set or self.entindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entindex"):
                self.entindex = value
                self.entindex.value_namespace = name_space
                self.entindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-removed" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = EntityFruFanTrayRemoved.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntityFruFanTrayRemoved()
        return self._top_entity

class PlatformHfrBundleDownedLink(Entity):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhBundleDownedLinkNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrBundleDownedLink.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(PlatformHfrBundleDownedLink, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-hfr-bundle-downed-link"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = PlatformHfrBundleDownedLink.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: bundle_name
        
        	bundle name for which to generate the trap
        	**type**\:  str
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(PlatformHfrBundleDownedLink.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "platform-hfr-bundle-downed-link"

            self.bundle_name = YLeaf(YType.str, "bundle-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bundle_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PlatformHfrBundleDownedLink.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformHfrBundleDownedLink.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.bundle_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bundle_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-downed-link/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bundle_name.is_set or self.bundle_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bundle_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bundle-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bundle-name"):
                self.bundle_name = value
                self.bundle_name.value_namespace = name_space
                self.bundle_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-downed-link" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = PlatformHfrBundleDownedLink.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PlatformHfrBundleDownedLink()
        return self._top_entity

class PlatformHfrBundleState(Entity):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhBundleStateNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrBundleState.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(PlatformHfrBundleState, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-hfr-bundle-state"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = PlatformHfrBundleState.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: bundle_name
        
        	bundle name for which to generate the trap
        	**type**\:  str
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(PlatformHfrBundleState.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "platform-hfr-bundle-state"

            self.bundle_name = YLeaf(YType.str, "bundle-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bundle_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PlatformHfrBundleState.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformHfrBundleState.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.bundle_name.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bundle_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bundle_name.is_set or self.bundle_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bundle_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bundle-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bundle-name"):
                self.bundle_name = value
                self.bundle_name.value_namespace = name_space
                self.bundle_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-state" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = PlatformHfrBundleState.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PlatformHfrBundleState()
        return self._top_entity

class PlatformHfrPlaneState(Entity):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhPlaneStateNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrPlaneState.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(PlatformHfrPlaneState, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-hfr-plane-state"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = PlatformHfrPlaneState.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: plane_id
        
        	plane identifier for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(PlatformHfrPlaneState.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "platform-hfr-plane-state"

            self.plane_id = YLeaf(YType.uint32, "plane-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("plane_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PlatformHfrPlaneState.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PlatformHfrPlaneState.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.plane_id.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.plane_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-plane-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.plane_id.is_set or self.plane_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.plane_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "plane-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "plane-id"):
                self.plane_id = value
                self.plane_id.value_namespace = name_space
                self.plane_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-plane-state" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = PlatformHfrPlaneState.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PlatformHfrPlaneState()
        return self._top_entity

class RoutingBgpEstablished(Entity):
    """
    Generate BGP4\-MIB\:\:bglEstablishedNotification
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingBgpEstablished, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-established"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingBgpEstablished()
        return self._top_entity

class RoutingBgpEstablishedRemotePeer(Entity):
    """
    Generate BGP4\-MIB\:\:bglEstablishedNotification remote peer
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingBgpEstablishedRemotePeer.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingBgpEstablishedRemotePeer, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-established-remote-peer"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingBgpEstablishedRemotePeer.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: address
        
        	BGP remote peer IP address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingBgpEstablishedRemotePeer.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-bgp-established-remote-peer"

            self.address = YLeaf(YType.str, "address")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingBgpEstablishedRemotePeer.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingBgpEstablishedRemotePeer.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.address.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established-remote-peer/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address"):
                self.address = value
                self.address.value_namespace = name_space
                self.address.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established-remote-peer" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingBgpEstablishedRemotePeer.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingBgpEstablishedRemotePeer()
        return self._top_entity

class RoutingBgpStateChange(Entity):
    """
    Generate CISCO\-BGP\-MIB\:\:cbgpBackwardTransition
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingBgpStateChange, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-state-change"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingBgpStateChange()
        return self._top_entity

class RoutingBgpStateChangeRemotePeer(Entity):
    """
    Generate CISCO\-BGP\-MIB\:\:cbgpBackwardTransition remote peer
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingBgpStateChangeRemotePeer.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingBgpStateChangeRemotePeer, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-bgp-state-change-remote-peer"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingBgpStateChangeRemotePeer.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: address
        
        	BGP remote peer IP address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingBgpStateChangeRemotePeer.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-bgp-state-change-remote-peer"

            self.address = YLeaf(YType.str, "address")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingBgpStateChangeRemotePeer.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingBgpStateChangeRemotePeer.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.address.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change-remote-peer/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address"):
                self.address = value
                self.address.value_namespace = name_space
                self.address.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change-remote-peer" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingBgpStateChangeRemotePeer.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingBgpStateChangeRemotePeer()
        return self._top_entity

class RoutingOspfNeighborStateChange(Entity):
    """
    Generate OSPF\-TRAP\-MIB\:\:ospfNbrStateChange
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingOspfNeighborStateChange, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-ospf-neighbor-state-change"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingOspfNeighborStateChange()
        return self._top_entity

class RoutingOspfNeighborStateChangeAddress(Entity):
    """
    Generate OSPF\-TRAP\-MIB\:\:ospfNbrStateChange address
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingOspfNeighborStateChangeAddress.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingOspfNeighborStateChangeAddress, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-ospf-neighbor-state-change-address"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingOspfNeighborStateChangeAddress.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: address
        
        	neighbor's IP source address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: ifindex
        
        	0 for interfaces having IP addresses or IF\-MIB ifindex of addressless interface
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingOspfNeighborStateChangeAddress.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-ospf-neighbor-state-change-address"

            self.address = YLeaf(YType.str, "address")

            self.ifindex = YLeaf(YType.uint32, "ifindex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address",
                            "ifindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingOspfNeighborStateChangeAddress.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingOspfNeighborStateChangeAddress.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.address.is_set or
                self.ifindex.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address.yfilter != YFilter.not_set or
                self.ifindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change-address/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address.get_name_leafdata())
            if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ifindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address" or name == "ifindex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address"):
                self.address = value
                self.address.value_namespace = name_space
                self.address.value_namespace_prefix = name_space_prefix
            if(value_path == "ifindex"):
                self.ifindex = value
                self.ifindex.value_namespace = name_space
                self.ifindex.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change-address" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingOspfNeighborStateChangeAddress.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingOspfNeighborStateChangeAddress()
        return self._top_entity

class RoutingMplsLdpSessionDown(Entity):
    """
    Generate MPLS\-LDP\-STD\-MIB\:\:mplsLdpSessionDown
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsLdpSessionDown, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-ldp-session-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsLdpSessionDown()
        return self._top_entity

class RoutingMplsLdpSessionDownEntityId(Entity):
    """
    Generate MPLS\-LDP\-STD\-MIB\:\:mplsLdpSessionDown entity\-id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsLdpSessionDownEntityId.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsLdpSessionDownEntityId, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-ldp-session-down-entity-id"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingMplsLdpSessionDownEntityId.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: entity_id
        
        	entity ldp\-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
        	**type**\:  str
        
        	**length:** 23
        
        	**mandatory**\: True
        
        .. attribute:: entity_index
        
        	entity index for which to generate the trap
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: peer_id
        
        	peer ldp\-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
        	**type**\:  str
        
        	**length:** 23
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingMplsLdpSessionDownEntityId.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-ldp-session-down-entity-id"

            self.entity_id = YLeaf(YType.str, "entity-id")

            self.entity_index = YLeaf(YType.uint32, "entity-index")

            self.peer_id = YLeaf(YType.str, "peer-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entity_id",
                            "entity_index",
                            "peer_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingMplsLdpSessionDownEntityId.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingMplsLdpSessionDownEntityId.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.entity_id.is_set or
                self.entity_index.is_set or
                self.peer_id.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entity_id.yfilter != YFilter.not_set or
                self.entity_index.yfilter != YFilter.not_set or
                self.peer_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down-entity-id/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entity_id.is_set or self.entity_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entity_id.get_name_leafdata())
            if (self.entity_index.is_set or self.entity_index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entity_index.get_name_leafdata())
            if (self.peer_id.is_set or self.peer_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.peer_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entity-id" or name == "entity-index" or name == "peer-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entity-id"):
                self.entity_id = value
                self.entity_id.value_namespace = name_space
                self.entity_id.value_namespace_prefix = name_space_prefix
            if(value_path == "entity-index"):
                self.entity_index = value
                self.entity_index.value_namespace = name_space
                self.entity_index.value_namespace_prefix = name_space_prefix
            if(value_path == "peer-id"):
                self.peer_id = value
                self.peer_id.value_namespace = name_space
                self.peer_id.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down-entity-id" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingMplsLdpSessionDownEntityId.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsLdpSessionDownEntityId()
        return self._top_entity

class RoutingMplsTunnelReRouted(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelRerouted
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsTunnelReRouted, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-routed"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReRouted()
        return self._top_entity

class RoutingMplsTunnelReRoutedIndex(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelRerouted index
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelReRoutedIndex.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsTunnelReRoutedIndex, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-routed-index"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingMplsTunnelReRoutedIndex.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	source address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingMplsTunnelReRoutedIndex.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-tunnel-re-routed-index"

            self.destination = YLeaf(YType.str, "destination")

            self.index = YLeaf(YType.uint32, "index")

            self.instance = YLeaf(YType.uint32, "instance")

            self.source = YLeaf(YType.str, "source")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("destination",
                            "index",
                            "instance",
                            "source") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingMplsTunnelReRoutedIndex.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingMplsTunnelReRoutedIndex.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.destination.is_set or
                self.index.is_set or
                self.instance.is_set or
                self.source.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.destination.yfilter != YFilter.not_set or
                self.index.yfilter != YFilter.not_set or
                self.instance.yfilter != YFilter.not_set or
                self.source.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed-index/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                leaf_name_data.append(self.destination.get_name_leafdata())
            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.index.get_name_leafdata())
            if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                leaf_name_data.append(self.instance.get_name_leafdata())
            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination" or name == "index" or name == "instance" or name == "source"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "destination"):
                self.destination = value
                self.destination.value_namespace = name_space
                self.destination.value_namespace_prefix = name_space_prefix
            if(value_path == "index"):
                self.index = value
                self.index.value_namespace = name_space
                self.index.value_namespace_prefix = name_space_prefix
            if(value_path == "instance"):
                self.instance = value
                self.instance.value_namespace = name_space
                self.instance.value_namespace_prefix = name_space_prefix
            if(value_path == "source"):
                self.source = value
                self.source.value_namespace = name_space
                self.source.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed-index" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingMplsTunnelReRoutedIndex.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReRoutedIndex()
        return self._top_entity

class RoutingMplsTunnelReOptimized(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelReoptimized
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsTunnelReOptimized, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-optimized"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReOptimized()
        return self._top_entity

class RoutingMplsTunnelReOptimizedIndex(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelReoptimized index
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelReOptimizedIndex.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsTunnelReOptimizedIndex, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-re-optimized-index"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingMplsTunnelReOptimizedIndex.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	source address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingMplsTunnelReOptimizedIndex.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-tunnel-re-optimized-index"

            self.destination = YLeaf(YType.str, "destination")

            self.index = YLeaf(YType.uint32, "index")

            self.instance = YLeaf(YType.uint32, "instance")

            self.source = YLeaf(YType.str, "source")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("destination",
                            "index",
                            "instance",
                            "source") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingMplsTunnelReOptimizedIndex.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingMplsTunnelReOptimizedIndex.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.destination.is_set or
                self.index.is_set or
                self.instance.is_set or
                self.source.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.destination.yfilter != YFilter.not_set or
                self.index.yfilter != YFilter.not_set or
                self.instance.yfilter != YFilter.not_set or
                self.source.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized-index/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                leaf_name_data.append(self.destination.get_name_leafdata())
            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.index.get_name_leafdata())
            if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                leaf_name_data.append(self.instance.get_name_leafdata())
            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination" or name == "index" or name == "instance" or name == "source"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "destination"):
                self.destination = value
                self.destination.value_namespace = name_space
                self.destination.value_namespace_prefix = name_space_prefix
            if(value_path == "index"):
                self.index = value
                self.index.value_namespace = name_space
                self.index.value_namespace_prefix = name_space_prefix
            if(value_path == "instance"):
                self.instance = value
                self.instance.value_namespace = name_space
                self.instance.value_namespace_prefix = name_space_prefix
            if(value_path == "source"):
                self.source = value
                self.source.value_namespace = name_space
                self.source.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized-index" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingMplsTunnelReOptimizedIndex.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelReOptimizedIndex()
        return self._top_entity

class RoutingMplsTunnelDown(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelDown
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsTunnelDown, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-down"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelDown()
        return self._top_entity

class RoutingMplsTunnelDownIndex(Entity):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelDown index
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelDownIndex.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(RoutingMplsTunnelDownIndex, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-mpls-tunnel-down-index"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

        self.input = RoutingMplsTunnelDownIndex.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	src address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            super(RoutingMplsTunnelDownIndex.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "routing-mpls-tunnel-down-index"

            self.destination = YLeaf(YType.str, "destination")

            self.index = YLeaf(YType.uint32, "index")

            self.instance = YLeaf(YType.uint32, "instance")

            self.source = YLeaf(YType.str, "source")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("destination",
                            "index",
                            "instance",
                            "source") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RoutingMplsTunnelDownIndex.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingMplsTunnelDownIndex.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.destination.is_set or
                self.index.is_set or
                self.instance.is_set or
                self.source.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.destination.yfilter != YFilter.not_set or
                self.index.yfilter != YFilter.not_set or
                self.instance.yfilter != YFilter.not_set or
                self.source.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down-index/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                leaf_name_data.append(self.destination.get_name_leafdata())
            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.index.get_name_leafdata())
            if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                leaf_name_data.append(self.instance.get_name_leafdata())
            if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination" or name == "index" or name == "instance" or name == "source"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "destination"):
                self.destination = value
                self.destination.value_namespace = name_space
                self.destination.value_namespace_prefix = name_space_prefix
            if(value_path == "index"):
                self.index = value
                self.index.value_namespace = name_space
                self.index.value_namespace_prefix = name_space_prefix
            if(value_path == "instance"):
                self.instance = value
                self.instance.value_namespace = name_space
                self.instance.value_namespace_prefix = name_space_prefix
            if(value_path == "source"):
                self.source = value
                self.source.value_namespace = name_space
                self.source.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down-index" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RoutingMplsTunnelDownIndex.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingMplsTunnelDownIndex()
        return self._top_entity

class All(Entity):
    """
    generate all the supported traps
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        super(All, self).__init__()
        self._top_entity = None

        self.yang_name = "all"
        self.yang_parent_name = "Cisco-IOS-XR-snmp-test-trap-act"

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-snmp-test-trap-act:all" + path_buffer

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

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = All()
        return self._top_entity

